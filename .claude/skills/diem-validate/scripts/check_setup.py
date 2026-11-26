"""
Setup check before a validation: is this computer ready to validate and to
save every file in the right place?

Usage:
    python check_setup.py [--repo REPO] [--fix] [--json]

Checks (PASS / WARN / FAIL):
  - Python packages of the validation environment;
  - configuration/validation_config.yaml readable;
  - output_dir exists and is writable, with geopoll_output/, kobo_output/ and
    their validation_cases/ folders (created when missing);
  - templates_dir exists and holds a KoBo and a GeoPoll template;
  - templates_source_dir (DIEM Toolbox on OneDrive/SharePoint) reachable, and
    the local templates not older than the Toolbox ones;
  - AGOL admin boundary service reachable (needed for admin lists).

templates_dir and templates_source_dir are absolute paths of one computer.
On another computer they usually fail: --fix looks for the repo's Template
folder and the DIEM Toolbox folder under the user's OneDrive and writes the
two lines of validation_config.yaml (only those two lines; comments kept).

Exit code 0 when nothing FAILs, 1 otherwise. A validation must not start
while a check FAILs.
"""
from __future__ import annotations

import argparse
import importlib
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

import yaml

PACKAGES = ["polars", "openpyxl", "yaml", "xlsxwriter", "docx", "ruamel.yaml"]
AGOL_URL = ("https://services5.arcgis.com/sjP4Ugu5s0dZWLjd/arcgis/rest/services"
            "/Administrative_Boundaries_Reference_(view_layer)/FeatureServer?f=json")
TOOLBOX_TAIL = Path("03. Toolbox") / "02. Questionnaires"


def _find_toolbox() -> str:
    """Look for the DIEM Toolbox questionnaires folder under the user's OneDrive / SharePoint sync folders."""
    home = Path.home()
    for base in [p for p in home.iterdir() if p.is_dir()] if home.exists() else []:
        for cand in base.glob("*DIEM Monitoring*"):
            tb = cand / TOOLBOX_TAIL
            if tb.is_dir():
                return str(tb).replace("\\", "/")
    return ""


def _set_yaml_line(cfg_path: Path, key: str, value: str) -> bool:
    text = cfg_path.read_text(encoding="utf-8-sig")
    new, n = re.subn(rf'(?m)^({re.escape(key)}:\s*)(".*?"|\S.*?)?(\s*#.*)?$',
                     lambda m: f'{m.group(1)}"{value}"{m.group(3) or ""}', text, count=1)
    if n:
        cfg_path.write_text(new, encoding="utf-8")
    return bool(n)


def run(repo: Path, fix: bool) -> list[dict]:
    res: list[dict] = []
    add = lambda level, check, detail="": res.append({"level": level, "check": check, "detail": detail})

    add("PASS" if sys.version_info >= (3, 10) else "FAIL", "Python version", sys.version.split()[0])
    missing = []
    for p in PACKAGES:
        try:
            importlib.import_module(p)
        except Exception:
            missing.append(p.replace("docx", "python-docx").replace("yaml", "pyyaml", 1) if p in ("docx", "yaml") else p)
    add("FAIL" if missing else "PASS", "Python packages",
        f"missing: {', '.join(missing)} (activate the validation environment, or pip install them)" if missing
        else f"{', '.join(PACKAGES)} ({sys.executable})")

    cfg_path = repo / "configuration" / "validation_config.yaml"
    try:
        cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8-sig")) or {}
        add("PASS", "Configuration", str(cfg_path))
    except Exception as e:
        add("FAIL", "Configuration", f"{cfg_path}: {e}")
        return res

    if cfg.get("config_profile"):
        add("WARN", "config_profile", f"validation_config.yaml points to a profile ({cfg['config_profile']}); "
            "runs started by the agent set their own profile, but a manual `validate` will use this one")

    # Templates folder (machine-specific path)
    tdir = Path(str(cfg.get("templates_dir") or ""))
    if not tdir.is_dir() and fix and (repo / "Template").is_dir():
        _set_yaml_line(cfg_path, "templates_dir", str(repo / "Template").replace("\\", "/"))
        tdir = repo / "Template"
        add("WARN", "templates_dir fixed", f"set to {tdir}")
    if tdir.is_dir():
        kobo = sorted(tdir.glob("diem_household_questionnaire_kobo_*_ISO3.xlsx"))
        gp = sorted(tdir.glob("diem_household_questionnaire_geopoll_*_ISO3.xlsx"))
        add("PASS" if kobo and gp else "FAIL", "Templates folder",
            f"{tdir} — latest KoBo: {kobo[-1].name if kobo else 'none'}, latest GeoPoll: {gp[-1].name if gp else 'none'}")
    else:
        add("FAIL", "Templates folder", f"templates_dir does not exist on this computer: {tdir}. "
            f"Set it to {repo / 'Template'} (run with --fix)")
        kobo = gp = []

    # DIEM Toolbox (source of the official templates)
    sdir = Path(str(cfg.get("templates_source_dir") or ""))
    if not sdir.is_dir() and fix:
        found = _find_toolbox()
        if found:
            _set_yaml_line(cfg_path, "templates_source_dir", found)
            sdir = Path(found)
            add("WARN", "templates_source_dir fixed", f"set to {found}")
    if sdir.is_dir():
        try:
            names = sorted(p.name for p in sdir.glob("diem_household_questionnaire_*_ISO3.xlsx"))
            local = {p.name for p in list(kobo) + list(gp)}
            newer = [n for n in names if n not in local]
            add("WARN" if newer else "PASS", "DIEM Toolbox templates",
                f"not yet copied locally (the next run copies them): {', '.join(newer)}" if newer else f"{sdir} — local templates up to date")
        except OSError as e:
            add("WARN", "DIEM Toolbox templates", f"{sdir}: {e}")
    else:
        add("WARN", "DIEM Toolbox templates", f"templates_source_dir not reachable: {sdir}. Runs will use the local "
            "templates only; sync the DIEM Monitoring SharePoint folder with OneDrive and run with --fix")

    # Output folders
    out = Path(str(cfg.get("output_dir") or "C:/Temp/DIEM_questionnaire_validation"))
    try:
        for sub in ("geopoll_output/validation_cases", "kobo_output/validation_cases", "_agent_runs"):
            (out / sub).mkdir(parents=True, exist_ok=True)
        probe = out / "_agent_runs" / ".write_test"
        probe.write_text("ok", encoding="utf-8"); probe.unlink()
        add("PASS", "Output folder", f"{out} (geopoll_output, kobo_output, validation_cases ready)")
    except OSError as e:
        add("FAIL", "Output folder", f"{out}: {e}")

    # AGOL
    try:
        with urllib.request.urlopen(AGOL_URL, timeout=15) as r:
            add("PASS" if r.status == 200 else "WARN", "AGOL admin boundaries", f"HTTP {r.status}")
    except Exception as e:
        add("WARN", "AGOL admin boundaries", f"not reachable ({e.__class__.__name__}); admin lists cannot be refreshed")
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parents[4]))
    ap.add_argument("--fix", action="store_true", help="set templates_dir / templates_source_dir for this computer")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    res = run(Path(a.repo), a.fix)
    sys.stdout.reconfigure(encoding="utf-8")
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        for r in res:
            print(f'{r["level"]:5} {r["check"]}: {r["detail"]}')
        print("READY" if not any(r["level"] == "FAIL" for r in res) else "NOT READY — fix the FAIL lines before validating")
    return 1 if any(r["level"] == "FAIL" for r in res) else 0


if __name__ == "__main__":
    sys.exit(main())
