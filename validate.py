"""
DIEM Questionnaire Validation — entry point.

Usage:
    python validate.py

Reads tool: from configuration/validation_config.yaml and dispatches
to the matching validator in scripts/.
"""
import sys
import subprocess
import pathlib
import yaml

from scripts.output_housekeeping import run_output_housekeeping
from scripts.template_sync import sync_templates

ROOT    = pathlib.Path(__file__).parent
CFG     = ROOT / "configuration" / "validation_config.yaml"
SCRIPTS = ROOT / "scripts"

VALIDATORS = {
    "geopoll": SCRIPTS / "geopoll_validator.py",
    "kobo":    SCRIPTS / "kobo_validator.py",
}


def main() -> None:
    if not CFG.exists():
        print(f"ERROR: configuration file not found: {CFG}")
        sys.exit(1)

    raw = yaml.safe_load(CFG.read_text(encoding="utf-8")) or {}

    # Resolve config profile if one is set
    profile_name = str(raw.get("config_profile") or "").strip()
    if profile_name:
        profiles_dir = pathlib.Path(
            raw.get("config_profiles_dir")
            or (pathlib.Path(raw.get("output_dir") or raw.get("working_dir") or "C:/Temp") / "config_profiles")
        )
        candidate = pathlib.Path(profile_name)
        if not candidate.is_absolute():
            candidate = profiles_dir / candidate
        for suffix in ("", ".yaml", ".yml"):
            p = candidate if suffix == "" else candidate.with_suffix(suffix)
            if p.exists():
                override = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
                raw.update(override)
                break

    tool = str(raw.get("tool") or "").strip().lower()

    if tool not in VALIDATORS:
        known = ", ".join(sorted(VALIDATORS.keys()))
        print(f"ERROR: 'tool' in validation_config.yaml must be one of: {known}")
        print(f"       Got: {tool!r}")
        sys.exit(1)

    hk_result = run_output_housekeeping(raw)
    if hk_result.get("enabled"):
        dry_flag = " (dry-run)" if hk_result.get("dry_run") else ""
        print(f"Housekeeping{dry_flag}:")
        print(f"  Base output dir : {hk_result.get('base_output_dir')}")
        print(f"  Scanned files   : {hk_result.get('scanned_files', 0)}")
        print(f"  Kept files      : {hk_result.get('kept_files', 0)}")
        print(f"  Candidates      : {hk_result.get('candidate_files', 0)}")
        if hk_result.get("dry_run"):
            print(f"  Planned actions : {len(hk_result.get('actions') or [])}")
        else:
            print(f"  Archived files  : {hk_result.get('archived_files', 0)}")
            print(f"  Deleted files   : {hk_result.get('deleted_files', 0)}")
            print(f"  Purged archives : {hk_result.get('archive_deleted_files', 0)}")
        if hk_result.get("errors"):
            print(f"  Housekeeping warnings: {len(hk_result.get('errors'))}")
            for msg in (hk_result.get("errors") or [])[:5]:
                print(f"    - {msg}")

    # Refresh local templates from the official shared folder (if configured)
    # so latest_template mode always compares against the newest template.
    sync = sync_templates(
        raw.get("templates_source_dir") or "",
        raw.get("templates_dir") or (ROOT / "Template"),
        tools=list(VALIDATORS.keys()),
    )
    if sync["enabled"]:
        print("Template sync:")
        print(f"  Source          : {sync['source_dir']}")
        print(f"  Copied          : {', '.join(sync['copied']) or 'none (already up to date)'}")
        for msg in sync["errors"]:
            print(f"  WARNING: {msg} -- using templates already in templates_dir")

    script = VALIDATORS[tool]
    if not script.exists():
        print(f"ERROR: validator script not found: {script}")
        sys.exit(1)

    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=str(ROOT),
    )
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
