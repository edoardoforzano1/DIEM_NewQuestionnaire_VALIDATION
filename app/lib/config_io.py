"""
Config read/write helpers for the Streamlit UI.

Reading is plain PyYAML (matches the rest of the repo). Writing back to the
*tracked* configuration/validation_config.yaml uses ruamel.yaml's round-trip
loader instead, so the extensive inline documentation comments in that file
("Edit ONLY this file. Never touch the notebook code.") survive a save made
from the UI. Only the dotted keys in WRITABLE_KEYS are ever touched — every
other key, comment, and ordering in the file is left exactly as it was on
disk, and a timestamped backup is written before every save.

configuration/admin_tools_config.yaml is never edited in place: the Admin
Tools page always writes a throwaway full copy of it and points the tool at
it with the `--config` CLI flag the admin tools already support (see
scripts/admin_tools_common.py: merge_runtime_config). No comment
preservation is needed there because the tracked file itself is untouched.

Tested round-trip against a scratch copy of the real validation_config.yaml
(which has a UTF-8 BOM, CRLF line endings, and 4-space-indented block
lists) before ever pointing this at the tracked file:
  - BOM and CRLF are both preserved by reading/writing with
    encoding="utf-8-sig" in text mode.
  - `_ryaml.indent(mapping=2, sequence=4, offset=2)` matches this file's
    existing block-list style, so untouched lists are not reformatted.
  - One known, narrow, purely-cosmetic residual: a boolean written in the
    file with non-canonical casing (e.g. `False`/`True`/`Yes`/`No` instead
    of `false`/`true`) gets normalized to lowercase on any save made
    through this module, even if that key wasn't touched — ruamel's
    round-trip loader does not retain original casing for bool scalars
    (unlike str/int, which it does preserve). This never changes the
    parsed value (`yaml.safe_load` reads both forms identically), only the
    on-disk spelling of that one line.
  - List-valued keys (ignore_modules_from_comparison,
    kobo_options.country_specific_list_names, etc.) do NOT go through
    ruamel at all, even when unchanged — verified with a zero-edit
    load-then-dump round trip that every comment survives *except* around
    keys whose list value is actually replaced: ruamel's comment
    attachments near a block list (e.g. a section-banner comment right
    after the list's last item) are keyed to that node's original parsed
    position, and get silently dropped once the list's rendered line count
    changes, whether the list object is replaced outright or mutated in
    place. So list edits are instead applied with a small line-level
    patcher (_replace_list_lines) that only ever rewrites the exact lines
    belonging to that one list's own `- item` entries, leaving every
    surrounding line — including trailing comments — untouched. See
    write_validation_config_keys().
"""
from __future__ import annotations

import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml
from ruamel.yaml import YAML

from app.lib.paths import VALIDATION_CFG_PATH, ADMIN_CFG_PATH

_ryaml = YAML()
_ryaml.preserve_quotes = True
_ryaml.width = 4096  # don't rewrap long comment lines on save
_ryaml.indent(mapping=2, sequence=4, offset=2)  # matches this file's existing block-list style

# Dotted keys the Run Validation page is allowed to write back into the
# tracked validation_config.yaml. Keep this in sync with the form fields in
# app/pages/1_Run_Validation.py — see also app/config_schema.py and
# CLAUDE.md > "Before adding or changing anything".
WRITABLE_KEYS: tuple[str, ...] = (
    "config_profile",
    "tool",
    "working_dir",
    "questionnaire_file",
    "language",
    "iso3",
    "reference_mode",
    "previous_round_file",
    "templates_dir",
    "output_dir",
    "housekeeping.enabled",
    "housekeeping.dry_run",
    "ignore_modules_from_comparison",
    "skip_modules_from_validated_output",
    "kobo_options.include_admin3",
    "kobo_options.skip_restore_and_replacement",
    "kobo_options.require_additional_info",
    "kobo_options.require_crop_list",
    "kobo_options.country_specific_list_names",
    "kobo_options.exclude_qnames_from_option_compare",
    "geopoll_options.max_qname_length",
    "geopoll_options.modality",
    "validation_number",
    "user_name",
)


def load_plain_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def read_validation_config() -> dict:
    """Plain read of the tracked validation_config.yaml (config_profile not applied)."""
    return load_plain_yaml(VALIDATION_CFG_PATH)


def read_admin_tools_config() -> dict:
    return load_plain_yaml(ADMIN_CFG_PATH)


def resolve_effective_config(raw: dict) -> dict:
    """Apply config_profile override exactly like validate.py does."""
    cfg = dict(raw)
    profile_name = str(cfg.get("config_profile") or "").strip()
    if not profile_name:
        return cfg
    profiles_dir = Path(
        cfg.get("config_profiles_dir")
        or (Path(cfg.get("output_dir") or cfg.get("working_dir") or "C:/Temp") / "config_profiles")
    )
    candidate = Path(profile_name)
    if not candidate.is_absolute():
        candidate = profiles_dir / candidate
    for suffix in ("", ".yaml", ".yml"):
        p = candidate if suffix == "" else candidate.with_suffix(suffix)
        if p.exists():
            cfg.update(load_plain_yaml(p))
            break
    return cfg


def _get_nested(d: dict, dotted: str) -> Any:
    node: Any = d
    for part in dotted.split("."):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node


def _set_nested(node: dict, dotted: str, value: Any) -> None:
    """Set a plain dict/CommentedMap key. Scalars only in practice for the
    ruamel path (write_validation_config_keys routes list values through
    _replace_list_lines instead — see its docstring); used as-is for
    write_scratch_admin_config's throwaway plain-dict output, where there's
    no comment-preservation concern either way."""
    parts = dotted.split(".")
    for part in parts[:-1]:
        if part not in node or not isinstance(node.get(part), dict):
            node[part] = {}
        node = node[part]
    node[parts[-1]] = value


def _find_nested_key_line(lines: list[str], dotted: str) -> tuple[int, int]:
    """Return (line_index, indent) of dotted key's own `key:` line, by
    walking each segment within the previous segment's indented block."""
    parts = dotted.split(".")
    search_start, search_end, indent = 0, len(lines), 0
    for depth, part in enumerate(parts):
        pattern = re.compile(r"^ {" + str(indent) + "}" + re.escape(part) + r"\s*:")
        found = next((i for i in range(search_start, search_end) if pattern.match(lines[i])), None)
        if found is None:
            raise KeyError(f"Could not find {dotted!r} (segment {part!r} at indent {indent}) in validation_config.yaml")
        if depth == len(parts) - 1:
            return found, indent
        child_indent = indent + 2
        block_end = found + 1
        while block_end < len(lines):
            stripped = lines[block_end].strip()
            this_indent = len(lines[block_end]) - len(lines[block_end].lstrip(" "))
            if stripped and not stripped.startswith("#") and this_indent < child_indent:
                break
            block_end += 1
        search_start, search_end, indent = found + 1, block_end, child_indent
    raise KeyError(dotted)


def _replace_list_lines(lines: list[str], dotted: str, values: list[str]) -> list[str]:
    """Rewrite only the lines holding `dotted`'s YAML list value (flow-style
    `key: [...]` on one line, or block-style `key:` + `- item` lines right
    after it) — every other line, including anything that follows the list
    (comments, banners, the next key), is passed through byte-identical.
    See write_validation_config_keys() / module docstring for why this
    exists instead of doing list edits through ruamel."""
    key_idx, indent = _find_nested_key_line(lines, dotted)
    key_line = lines[key_idx]
    key_text = key_line.split(":", 1)[0]
    eol = "\r\n" if key_line.endswith("\r\n") else "\n"
    item_indent = " " * (indent + 2)

    if values:
        new_lines = [f"{key_text}:{eol}"] + [f'{item_indent}- "{v}"{eol}' for v in values]
    else:
        new_lines = [f"{key_text}: []{eol}"]

    after_colon = key_line.split(":", 1)[1].strip() if ":" in key_line else ""
    if after_colon:
        # Flow-style value lives entirely on the key's own line.
        return lines[:key_idx] + new_lines + lines[key_idx + 1 :]

    item_prefix = " " * (indent + 2) + "-"
    end_idx = key_idx + 1
    while end_idx < len(lines) and lines[end_idx].startswith(item_prefix):
        end_idx += 1
    return lines[:key_idx] + new_lines + lines[end_idx:]


def diff_writable_keys(new_values: dict[str, Any]) -> list[tuple[str, Any, Any]]:
    """Return (dotted_key, old_value, new_value) only for keys that would actually change."""
    unknown = set(new_values) - set(WRITABLE_KEYS)
    if unknown:
        raise KeyError(f"Not in config_io.WRITABLE_KEYS: {sorted(unknown)}")
    current = read_validation_config()
    changes = []
    for key, new_val in new_values.items():
        old_val = _get_nested(current, key)
        if old_val != new_val:
            changes.append((key, old_val, new_val))
    return changes


def backup_validation_config() -> Path | None:
    if not VALIDATION_CFG_PATH.exists():
        return None
    backup_dir = VALIDATION_CFG_PATH.parent / ".streamlit_backups"
    backup_dir.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = backup_dir / f"validation_config_{stamp}.yaml"
    shutil.copy2(VALIDATION_CFG_PATH, dest)
    return dest


def write_validation_config_keys(new_values: dict[str, Any]) -> Path:
    """Update only the given whitelisted keys in the tracked
    validation_config.yaml, preserving every comment. Always backs up the
    previous version first (configuration/.streamlit_backups/).

    Two passes, deliberately not one: scalar keys go through ruamel's
    round-trip loader (comment-preserving as long as the list nodes it
    passes through are never mutated); list keys go through
    _replace_list_lines' line-level text patch instead, applied to the
    ruamel pass's own output. See the module docstring for why list values
    can't safely go through ruamel here.
    """
    unknown = set(new_values) - set(WRITABLE_KEYS)
    if unknown:
        raise KeyError(f"Refusing to write non-whitelisted keys: {sorted(unknown)}")
    backup_validation_config()

    scalar_values = {k: v for k, v in new_values.items() if not isinstance(v, list)}
    list_values = {k: v for k, v in new_values.items() if isinstance(v, list)}

    # utf-8-sig (not utf-8) on both sides: the tracked file has a UTF-8 BOM,
    # and this is the pairing verified (against a scratch copy of the real
    # file) to round-trip the BOM and CRLF line endings byte-for-byte.
    doc = _ryaml.load(VALIDATION_CFG_PATH.read_text(encoding="utf-8-sig"))
    for key, value in scalar_values.items():
        _set_nested(doc, key, value)
    with VALIDATION_CFG_PATH.open("w", encoding="utf-8-sig") as f:
        _ryaml.dump(doc, f)

    if list_values:
        lines = VALIDATION_CFG_PATH.read_text(encoding="utf-8-sig").splitlines(keepends=True)
        for key, value in list_values.items():
            lines = _replace_list_lines(lines, key, [str(v) for v in value])
        with VALIDATION_CFG_PATH.open("w", encoding="utf-8-sig") as f:
            f.writelines(lines)

    return VALIDATION_CFG_PATH


def write_scratch_admin_config(overrides: dict[str, Any], scratch_dir: Path) -> Path:
    """Write a full throwaway admin_tools_config.yaml-shaped file (tracked
    file + overrides) for use with the admin tools' existing --config flag.
    Never touches the tracked configuration/admin_tools_config.yaml."""
    merged = dict(read_admin_tools_config())
    for key, value in overrides.items():
        _set_nested(merged, key, value)
    scratch_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S%f")
    dest = scratch_dir / f"admin_tools_config_{stamp}.yaml"
    dest.write_text(yaml.safe_dump(merged, sort_keys=False), encoding="utf-8")
    return dest


def list_xlsx(directory: str | Path) -> list[Path]:
    d = Path(directory)
    if not d.exists():
        return []
    return sorted(d.glob("*.xlsx"), key=lambda p: p.stat().st_mtime, reverse=True)
