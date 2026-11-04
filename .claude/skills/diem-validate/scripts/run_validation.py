"""
Run the DIEM questionnaire validator on one questionnaire file without
permanently editing configuration/validation_config.yaml.

How it works
------------
The validators read the tracked config at a fixed path, but that config
supports a `config_profile:` override file. This script:
  1. copies the questionnaire into <output_dir>/_skill_staging/ (avoids
     OneDrive/Excel file locks and keeps the original untouched),
  2. writes a profile YAML with the run-specific keys,
  3. points `config_profile:` at it for the duration of the run only,
  4. runs validate.py with the given Python interpreter, logging to a file,
  5. restores validation_config.yaml byte-for-byte (always, via finally),
  6. prints a JSON summary with the produced report / validated file paths.

Usage
-----
  python run_validation.py --repo C:/git/DIEM_NewQuestionnaire_VALIDATION \
      --questionnaire "C:/path/diem_household_questionnaire_geopoll_yemen.xlsx" \
      --tool geopoll --language en --iso3 YEM \
      [--reference-mode latest_template | previous_round --previous-round FILE] \
      [--python C:/path/to/env/python.exe]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

import yaml


def _newest(folder: Path, pattern: str, since: float) -> str | None:
    hits = [p for p in folder.glob(pattern) if p.stat().st_mtime >= since - 1]
    return str(max(hits, key=lambda p: p.stat().st_mtime)) if hits else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--questionnaire", required=True)
    ap.add_argument("--tool", required=True, choices=["geopoll", "kobo"])
    ap.add_argument("--language", required=True)
    ap.add_argument("--iso3", required=True)
    ap.add_argument("--reference-mode", default="latest_template", choices=["latest_template", "previous_round"])
    ap.add_argument("--previous-round", default="", help="previous-round file (copied to staging too)")
    ap.add_argument("--python", default=sys.executable, help="interpreter of the validation env")
    ap.add_argument("--languages", default="", help="comma-separated languages in scope (e.g. en,fr); "
                    "other language columns stay in the file but are not checked")
    ap.add_argument("--extra", default="{}", help="JSON dict of extra top-level config overrides")
    ap.add_argument("--toolbox-dir", default="", help="official template folder to compare against templates_dir "
                    "(default: templates_source_dir from validation_config.yaml, which validate.py syncs from)")
    args = ap.parse_args()

    repo = Path(args.repo)
    cfg_path = repo / "configuration" / "validation_config.yaml"
    original_bytes = cfg_path.read_bytes()
    base = yaml.safe_load(original_bytes.decode("utf-8-sig")) or {}

    output_dir = Path(base.get("output_dir") or base.get("working_dir") or "C:/Temp/DIEM_questionnaire_validation")
    # All scratch files of agent runs live in <output_dir>/_agent_runs/, which
    # output housekeeping clears after delete_agent_run_files_after_days.
    agent_runs = output_dir / "_agent_runs"
    staging = agent_runs / "staging"
    staging.mkdir(parents=True, exist_ok=True)
    src = Path(args.questionnaire)
    if not src.exists():
        print(json.dumps({"ok": False, "error": f"questionnaire not found: {src}"}))
        return 2
    staged = staging / src.name
    shutil.copy2(src, staged)
    # Fresh timestamp: housekeeping (run by validate.py before the validator)
    # deletes _agent_runs files by age, and copy2 keeps the source's old mtime.
    os.utime(staged, None)

    profile = {
        "tool": args.tool,
        "language": args.language.lower(),
        "iso3": args.iso3.upper(),
        "working_dir": staging.as_posix(),
        "questionnaire_file": staged.name,
        "reference_mode": args.reference_mode,
    }
    if args.previous_round:
        prev = Path(args.previous_round)
        if not prev.is_absolute():
            prev = Path(base.get("working_dir") or ".") / prev
        shutil.copy2(prev, staging / prev.name)
        os.utime(staging / prev.name, None)
        profile["previous_round_file"] = prev.name
    if args.languages:
        profile["languages_in_scope"] = [l.strip().lower() for l in args.languages.split(",") if l.strip()]
    profile.update(json.loads(args.extra or "{}"))

    profiles_dir = agent_runs / "profiles"
    profiles_dir.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    profile_path = profiles_dir / f"skill_run_{args.tool}_{args.iso3.upper()}_{stamp}.yaml"
    profile_path.write_text(yaml.safe_dump(profile, allow_unicode=True, sort_keys=False), encoding="utf-8")

    text = original_bytes.decode("utf-8-sig")
    new_line = f'config_profile: "{profile_path.as_posix()}"'
    if re.search(r"(?m)^config_profile:.*$", text):
        patched = re.sub(r"(?m)^config_profile:.*$", new_line, text, count=1)
    else:
        patched = new_line + "\n" + text
    bom = b"\xef\xbb\xbf" if original_bytes.startswith(b"\xef\xbb\xbf") else b""
    (agent_runs / "logs").mkdir(parents=True, exist_ok=True)
    log_path = agent_runs / "logs" / f"skill_run_{args.tool}_{args.iso3.upper()}_{stamp}.log"

    started = time.time()
    try:
        cfg_path.write_bytes(bom + patched.encode("utf-8"))
        with open(log_path, "w", encoding="utf-8") as log:
            proc = subprocess.run(
                [args.python, str(repo / "validate.py")],
                cwd=str(repo), stdout=log, stderr=subprocess.STDOUT,
                env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"},
            )
        rc = proc.returncode
    finally:
        cfg_path.write_bytes(original_bytes)  # always restore the tracked config

    tool_out = output_dir / f"{args.tool}_output"
    lang, iso = args.language.lower(), args.iso3.upper()
    result = {
        "ok": rc == 0,
        "returncode": rc,
        "log": str(log_path),
        "profile": str(profile_path),
        "staged_questionnaire": str(staged),
        "report": _newest(tool_out, f"report_{args.tool}_{lang}_{iso}*.xlsx", started),
        "validated": _newest(tool_out, f"validated_questionnaire_{args.tool}_{lang}_{iso}*.xlsx", started),
        "config_restored": cfg_path.read_bytes() == original_bytes,
    }
    log_text = log_path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"HIGH\s+(\d+).*?MEDIUM\s+(\d+).*?INFO\s+(\d+)", log_text, re.S)
    if m:
        result["counts"] = {"high": int(m.group(1)), "medium": int(m.group(2)), "info": int(m.group(3))}
    # Which reference was used, read back from the report's Summary sheet,
    # plus the templates available -- a stale Template/ folder silently
    # validates against an old template, which inflates every count.
    if result["report"]:
        try:
            import openpyxl
            ws = openpyxl.load_workbook(result["report"], read_only=True)["Summary"]
            for row in ws.iter_rows(max_row=10, values_only=True):
                txt = " ".join(str(c) for c in row if c)
                if txt.startswith("Checked against"):
                    result["reference"] = txt
                    break
        except Exception as exc:  # report unreadable: leave it to the caller
            result["reference"] = f"(could not read report: {exc})"
    tpl_dir = Path(base.get("templates_dir") or repo / "Template")
    result["templates_available"] = sorted(
        (p.name for p in tpl_dir.glob("*.xlsx") if args.tool in p.name.lower() and not p.name.startswith("~$")),
        key=lambda n: (re.findall(r"\d{8}", n) or ["0"])[0], reverse=True,
    )
    toolbox = args.toolbox_dir or str(base.get("templates_source_dir") or "")
    sync_lines = [l.strip() for l in log_text.splitlines()
                  if l.strip().startswith(("Copied ", "WARNING: templates_source_dir", "Source "))]
    if sync_lines:
        result["template_sync"] = sync_lines
    if toolbox and Path(toolbox).is_dir():
        tb = Path(toolbox)
        result["toolbox_templates"] = sorted(
            (p.name for p in tb.glob("*.xlsx") if args.tool in p.name.lower() and not p.name.startswith("~$")),
            key=lambda n: (re.findall(r"\d{8}", n) or ["0"])[0], reverse=True,
        )
    if rc != 0:
        result["log_tail"] = log_text[-3000:]
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if rc == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
