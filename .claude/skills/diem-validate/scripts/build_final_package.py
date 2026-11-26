"""
Final package of a validation case, built once every point of the case is
closed (fixed / accepted / dropped):

  1. <case dir>/<ISO3>_<round>_<tool>_validated_questionnaire_FINAL.xlsx
     a copy of the last iteration's validated questionnaire (never the
     SharePoint original);
  2. <case dir>/<ISO3>_<round>_<tool>_final_validation_report.docx
     composition by question type, questions added / removed by type, admin
     levels, selected crops, interview length, the fixes made during the
     validation (round raised -> round fixed), the minor corrections DIEM made
     itself, accepted exceptions with who approved them, and template-side
     issues sent to SMAR. For a GeoPoll programmed form (Subform), which has
     no survey sheet to profile, the composition part is left out;
  3. <case dir>/final_report_spec.json, the spec the report was built from
     (make_fix_document.py format), so the text can be adjusted and rebuilt.

It refuses to run while points are still open, unless --force.

Usage:
  python build_final_package.py --case case.json --reference TEMPLATE.xlsx [--force]
The reference is the template (or previous-round file) of the last run.
"""
from __future__ import annotations

import argparse
import contextlib
import datetime as _dt
import json
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from make_fix_document import build  # noqa: E402

TYPE_LABEL = {
    "mandatory": "Mandatory", "recommended": "Optional – recommended",
    "low priority": "Optional – low priority", "customized": "Customized",
    "other": "Other", "spiel": "Spiel",
}


def _profile(country, reference, validated) -> dict:
    out = subprocess.run(
        [sys.executable, str(HERE / "questionnaire_profile.py"), country, reference, "--validated", validated],
        capture_output=True, text=True, encoding="utf-8", check=True,
    )
    return json.loads(out.stdout)


def _by_type_lines(groups: dict) -> list[dict]:
    return [{"p": f"**{TYPE_LABEL.get(k, k)} ({len(v)}):** " + ", ".join(f"`{n}`" for n in v)}
            for k, v in groups.items()]


def _composition(blocks: list, prof: dict) -> None:
    c, r = prof["country"], prof["reference"]
    blocks.append({"h1": "Questionnaire composition"})
    types = [t for t in TYPE_LABEL if t != "spiel" and (c["by_type"].get(t) or r["by_type"].get(t))]
    rows = [[TYPE_LABEL[t], str(c["by_type"].get(t, 0)), str(r["by_type"].get(t, 0))] for t in types]
    rows.append(["**Total questions**", f'**{c["questions"]}**', f'**{r["questions"]}**'])
    rows.append(["Spiels", str(c["spiels"]), str(r["spiels"])])
    blocks.append({"table": {"header": ["Type", "Questionnaire", "Reference"], "rows": rows, "widths": [6, 4, 4]}})
    blocks.append({"h2": f'Questions added ({prof["added"]["total"]})'})
    blocks += _by_type_lines(prof["added"]["by_type"]) or [{"p": "None."}]
    blocks.append({"h2": f'Questions removed ({prof["removed"]["total"]})'})
    blocks += _by_type_lines(prof["removed"]["by_type"]) or [{"p": "None."}]
    blocks.append({"h1": "Admin levels"})
    if prof["admin_levels"]:
        blocks.append({"table": {"header": ["Level", "Units"],
                                 "rows": [[k, str(v)] for k, v in prof["admin_levels"].items()], "widths": [6, 3]}})
        blocks.append({"p": f'Source: {prof["admin_source"]}.'})
    else:
        blocks.append({"p": "No admin lists found in the validated questionnaire."})
    if prof["selected_crops"]:
        blocks.append({"h1": "Crop list"})
        blocks.append({"p": f'{len(prof["selected_crops"])} crops selected: ' + ", ".join(prof["selected_crops"]) + "."})
    L = prof["interview_length_min"]
    blocks.append({"h1": "Interview length"})
    blocks.append({"p": f'Mandatory and recommended questions: **{L["mandatory_and_recommended"]} min**. '
                        f'Whole questionnaire: **{L["total"]} min** (estimate from the `Weighted duration` column).'})


def _points(blocks: list, case: dict) -> None:
    rnd = lambda p: str(p.get("opened_iteration") or "")
    pts = case["points"]
    fixed = [p for p in pts if p["status"] == "fixed" and p["tag"] not in ("Template side", "Fixed by DIEM")]
    diem = [p for p in pts if p["tag"] == "Fixed by DIEM" and p.get("fix")]
    accepted = [p for p in pts if p["status"] == "accepted"]
    template = [p for p in pts if p["tag"] == "Template side"]
    if fixed:
        blocks.append({"h1": "Changes made during the validation"})
        blocks.append({"table": {"header": ["#", "Section", "Point", "Raised", "Fixed", "By"],
                                 "rows": [[p["id"], p["section"], p["title"], rnd(p),
                                           str((p["resolution"] or {}).get("iteration", "")),
                                           "DIEM" if "DIEM" in str((p["resolution"] or {}).get("by", "")) else "country"]
                                          for p in fixed],
                                 "widths": [1.0, 3.0, 7.6, 1.4, 1.4, 1.6]}})
    if diem:
        blocks.append({"h1": "Minor corrections made by DIEM"})
        blocks.append({"p": "Text corrections DIEM made itself, so that the country team could focus on the main fixes."})
        blocks.append({"table": {"header": ["Round", "Row", "Question", "Column", "Before", "After"],
                                 "rows": [[rnd(p), str(p["fix"]["row"]), f'`{p["fix"]["question"]}`',
                                           f'`{p["fix"]["column"]}`', p["fix"]["before"], p["fix"]["after"]]
                                          for p in diem],
                                 "widths": [1.3, 1.2, 3.4, 2.6, 4.0, 4.0]}})
    if accepted:
        blocks.append({"h1": "Accepted exceptions"})
        blocks.append({"p": "Differences from the reference kept on purpose, with who agreed them."})
        blocks.append({"table": {"header": ["#", "Section", "Point", "Agreed by", "Note"],
                                 "rows": [[p["id"], p["section"], p["title"], (p["resolution"] or {}).get("by", ""),
                                           (p["resolution"] or {}).get("note", "")] for p in accepted],
                                 "widths": [1.0, 2.8, 6.0, 3.0, 3.2]}})
    if template:
        blocks.append({"h1": "Template side (reported to SMAR)"})
        blocks += [{"bullet": f'{p["title"]} — {p["status"]}'} for p in template]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True)
    ap.add_argument("--reference", required=True)
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    case_path = Path(a.case)
    case = json.loads(case_path.read_text(encoding="utf-8"))
    open_pts = [p for p in case["points"] if p["status"] == "open"]
    if open_pts and not a.force:
        print(json.dumps({"refused": "points still open", "open": [p["id"] + " " + p["title"] for p in open_pts]},
                         ensure_ascii=False, indent=2))
        return 1
    if not case["iterations"]:
        raise SystemExit("no iteration recorded in the case")
    last = case["iterations"][-1]
    tag = f'{case["iso3"]}_{case["round"]}_{case["tool"]}'
    case_dir = case_path.parent
    # The final questionnaire is the last validated questionnaire; for a
    # programmed form (no validator output) it is the file checked last.
    src = last.get("validated") or last["file"]
    final_xlsx = case_dir / f"{tag}_validated_questionnaire_FINAL.xlsx"
    shutil.copy2(src, final_xlsx)
    try:
        prof = _profile(last["file"], a.reference, src)
    except Exception:  # e.g. a GeoPoll Subform: no survey sheet to profile
        prof = None

    tool = "GeoPoll" if case["tool"] == "geopoll" else "KoBo"
    blocks = [{"h1": "Validation rounds"}, {"table": {
        "header": ["Round", "Date", "File", "High", "Medium"],
        "rows": [[str(it["n"]), it["date"][:10], f'`{Path(it["file"]).name}`',
                  str(it["counts"]["high"]), str(it["counts"]["medium"])] for it in case["iterations"]],
        "widths": [1.3, 2.7, 8.9, 1.5, 1.8]}}]
    if prof is None:
        blocks.append({"p": "The questionnaire is a programmed form, not the DIEM template format: question "
                            "composition, admin levels and interview length are not computed here."})
    else:
        _composition(blocks, prof)
    _points(blocks, case)

    spec = {
        "title": f'{case["country"]} {case["round"]} {tool} questionnaire – final validation',
        "meta": [
            ["Validated file", f'`{Path(last["file"]).name}`'],
            ["Compared with", f'`{Path(a.reference).name}` ({case["reference_mode"].replace("_", " ")})'],
            ["Languages checked", ", ".join(l.upper() for l in case["languages"])],
            ["Deployment language", case["deploy_language"].upper()],
            ["Final questionnaire", f"`{final_xlsx.name}`"],
            ["Date", _dt.date.today().strftime("%d %B %Y")],
        ],
        "intro": ["**Status: validated.** All points raised during the validation are fixed or agreed (see below)."],
        "blocks": blocks,
    }
    spec_path = case_dir / "final_report_spec.json"
    spec_path.write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")
    report = case_dir / f"{tag}_final_validation_report.docx"
    if report.exists():
        try:
            report.open("ab").close()
        except PermissionError:  # open in Word
            report = report.with_name(report.stem + "_v2.docx")
    with contextlib.redirect_stdout(sys.stderr):  # keep stdout pure JSON
        build(spec, str(report))

    case["closed"] = {"date": _dt.datetime.now().strftime("%Y-%m-%d %H:%M"), "final_questionnaire": str(final_xlsx),
                      "final_report": str(report), "forced": bool(open_pts)}
    case_path.write_text(json.dumps(case, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"final_questionnaire": str(final_xlsx), "final_report": str(report),
                      "spec": str(spec_path), "profile": prof}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
