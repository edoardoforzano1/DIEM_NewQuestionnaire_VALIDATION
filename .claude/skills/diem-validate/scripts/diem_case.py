"""
diem_case — the standard DIEM questionnaire validation procedure as one
command, the same for every agent (Claude, Codex, ...) and for a person.

Steps, in this order (each refuses to run before the previous one is done):

  setup     check this computer (environment, output folder, templates, AGOL)
  start     intake: create the case. Missing inputs are NOT guessed: the
            command lists the questions to ask the operator and stops.
  run       validate a version of the questionnaire, record the round, write
            the digest and the output check in the case folder
  fix       apply minor text fixes made by DIEM to a copy of the file
            (typos, brackets, untranslated options...; never logic)
  points    record the points of this round (to fix / to confirm / ...)
  outputs   build the Word document (agreed layout) and the email draft for
            this round, and list the files to send
  decide    close a point outside the file (accepted / dropped / fixed, with who)
  status    where the case stands
  final     when nothing is open: final questionnaire, final report, final email

Every file goes into the case folder:
  <output_dir>/<tool>_output/validation_cases/<ISO3>_<round>/

Usage examples (run with the validation environment's Python):
  python diem_case.py setup [--fix]
  python diem_case.py start --file "C:/.../questionnaire.xlsx" --tool kobo --reference latest \
         --languages en,fr --country Niger --iso3 NER --round R12 [--deploy-language fr]
         [--previous-round FILE] [--kobo-reference VALIDATED_KOBO.xlsx  (GeoPoll programmed form only)]
  python diem_case.py run --case CASE.json --file "C:/.../new_version.xlsx"
  python diem_case.py fix --case CASE.json --fixes fixes.json [--source FILE]
  python diem_case.py points --case CASE.json --points points.json
  python diem_case.py outputs --case CASE.json --spec spec.json [--operator "Edoardo"]
  python diem_case.py decide --case CASE.json --id P04 --status accepted --by "SMAR (email 26 Nov)" --note "..."
  python diem_case.py final --case CASE.json [--operator "Edoardo"]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import openpyxl
import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
PY = sys.executable
ENV = {**os.environ, "PYTHONIOENCODING": "utf-8"}


# ---------------------------------------------------------------- helpers
def _run(script: str, *args, check=True) -> str:
    p = subprocess.run([PY, str(HERE / script), *map(str, args)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=ENV)
    if check and p.returncode != 0:
        raise SystemExit(f"{script} failed ({p.returncode}):\n{p.stdout[-3000:]}\n{p.stderr[-3000:]}")
    return p.stdout


def _json(script: str, *args, check=True):
    out = _run(script, *args, check=check)
    i = out.find("{") if out.find("{") != -1 and (out.find("[") == -1 or out.find("{") < out.find("[")) else out.find("[")
    return json.loads(out[i:]) if i != -1 else {}


def _cfg() -> dict:
    return yaml.safe_load((REPO / "configuration" / "validation_config.yaml").read_text(encoding="utf-8-sig")) or {}


def _output_dir() -> Path:
    c = _cfg()
    return Path(c.get("output_dir") or "C:/Temp/DIEM_questionnaire_validation")


def _load(case: str) -> dict:
    return json.loads(Path(case).read_text(encoding="utf-8"))


def _save(case: str, d: dict) -> None:
    Path(case).write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")


def _latest_template(tool: str) -> Path:
    tdir = Path(str(_cfg().get("templates_dir") or REPO / "Template"))
    hits = sorted(tdir.glob(f"diem_household_questionnaire_{tool}_*_ISO3.xlsx"))
    if not hits:
        raise SystemExit(f"no {tool} template in {tdir}")
    return hits[-1]


def _is_subform(path: str) -> bool:
    try:
        return "Subform" in openpyxl.load_workbook(path, read_only=True).sheetnames
    except Exception:
        return False


def _setup_ok() -> None:
    p = subprocess.run([PY, str(HERE / "check_setup.py"), "--repo", str(REPO)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=ENV)
    if p.returncode != 0:
        raise SystemExit("Setup check failed — fix this first (python diem_case.py setup --fix):\n" + p.stdout)


def _say(d) -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(d, ensure_ascii=False, indent=2) if not isinstance(d, str) else d)


def _iteration(case: dict) -> int:
    return len(case["iterations"])


# ---------------------------------------------------------------- setup
def cmd_setup(a):
    p = subprocess.run([PY, str(HERE / "check_setup.py"), "--repo", str(REPO)] + (["--fix"] if a.fix else []),
                       text=True, encoding="utf-8", errors="replace", env=ENV)
    return p.returncode


# ---------------------------------------------------------------- start
def cmd_start(a):
    _setup_ok()
    if not Path(a.file).exists():
        raise SystemExit(f"file not found: {a.file}")
    subform = _is_subform(a.file)
    facts = {} if subform else _json("inspect_questionnaire.py", a.file, check=False)
    detected_tool = "geopoll" if subform else facts.get("tool")
    questions = []
    if not a.tool:
        questions.append({"ask": "Is it a KoBo or a GeoPoll questionnaire?", "proposal": detected_tool})
    elif detected_tool and a.tool != detected_tool:
        questions.append({"ask": f"The file looks like {detected_tool}, not {a.tool}: which is it?", "proposal": detected_tool})
    if subform:
        if not a.kobo_reference:
            questions.append({"ask": "This is a GeoPoll programmed form (Subform), not the DIEM GeoPoll template. "
                                     "Countries must send the DIEM template format; checking the Subform is an exception. "
                                     "Does the operator accept the exception, and which validated KoBo questionnaire "
                                     "of the same country/round holds the agreed content?", "proposal": None})
    elif not a.reference:
        questions.append({"ask": "Compare with the latest template or with the previous round (which file)?",
                          "proposal": "latest"})
    if a.reference == "previous" and not a.previous_round:
        questions.append({"ask": "Which file is the previous round?", "proposal": None})
    if not a.languages:
        filled = sorted((facts.get("survey_language_fill") or {}).keys())
        questions.append({"ask": "Which languages must be checked besides English?",
                          "proposal": ",".join(filled) or "en"})
    for k, q in (("country", "Which country?"), ("iso3", "ISO3 code of the country?"), ("round", "Which round (e.g. R12)?")):
        if not getattr(a, k):
            questions.append({"ask": q, "proposal": None})
    if questions:
        _say({"status": "questions_for_the_operator",
              "rule": "Ask the operator these questions (in one message) and run start again with the answers. Never guess.",
              "questions": questions, "file_facts": facts or {"format": "GeoPoll Subform"}})
        return 3

    tool = a.tool
    langs = ",".join(l.strip().lower() for l in a.languages.split(",") if l.strip())
    deploy = a.deploy_language or next((l for l in langs.split(",") if l != "en"), "en")
    root = _output_dir()
    res = _json("validation_case.py", "new", "--root", root, "--country", a.country, "--iso3", a.iso3,
                "--tool", tool, "--round", a.round,
                "--reference-mode", "previous_round" if a.reference == "previous" else "latest_template",
                "--languages", langs, "--deploy-language", deploy, "--source", str(Path(a.file).parent),
                "--previous-round", a.previous_round or "")
    case_path = res.get("created") or res.get("exists")
    case = _load(case_path)
    case["format"] = "subform" if subform else "template"
    if a.kobo_reference:
        case["kobo_reference"] = a.kobo_reference
    _save(case_path, case)
    hist = _json("validation_case.py", "history", "--root", root, "--iso3", a.iso3, "--exclude-case", case_path)
    _say({"case": case_path, "existing_case": bool(res.get("exists")), "format": case["format"],
          "country_history": hist,
          "next": f'python diem_case.py run --case "{case_path}" --file "{a.file}"'})
    return 0


# ---------------------------------------------------------------- run
def cmd_run(a):
    _setup_ok()
    case = _load(a.case)
    cdir = Path(a.case).parent
    n = _iteration(case) + 1
    received = cdir / Path(a.file).name
    if Path(a.file).resolve() != received.resolve():
        shutil.copy2(a.file, received)  # keep the version received (never the SharePoint original)
    if case.get("format") == "subform":
        if not case.get("kobo_reference"):
            raise SystemExit("subform case without kobo_reference: run start again with --kobo-reference")
        report = cdir / f"iter{n}_subform_check.xlsx"
        _run("gp_subform_check.py", received, case["kobo_reference"], _latest_template("geopoll"), report)
        validated, check_md, reference = str(received), "", str(_latest_template("geopoll"))
    else:
        args = ["--repo", REPO, "--questionnaire", received, "--tool", case["tool"],
                "--language", case["deploy_language"], "--iso3", case["iso3"],
                "--reference-mode", case["reference_mode"], "--languages", ",".join(case["languages"]), "--python", PY]
        if case.get("previous_round_file"):
            args += ["--previous-round", case["previous_round_file"]]
        r = _json("run_validation.py", *args)
        if not r.get("ok") or not r.get("config_restored", True):
            raise SystemExit(f"validation failed: {json.dumps(r, ensure_ascii=False)[:3000]}")
        report, validated, reference = Path(r["report"]), r["validated"], r.get("reference", "")
        (cdir / f"iter{n}_digest.md").write_text(_run("summarize_report.py", report), encoding="utf-8")
        check_md = cdir / f"iter{n}_output_check.md"
        check_md.write_text(_run("check_validated_output.py", validated, "--source", received, check=False), encoding="utf-8")
    it = _json("validation_case.py", "iterate", "--case", a.case, "--file", received, "--report", report,
               "--validated", validated, "--output-check", check_md)
    (cdir / f"iter{n}_iterate.json").write_text(json.dumps(it, ensure_ascii=False, indent=2), encoding="utf-8")
    case = _load(a.case)
    case["iterations"][-1]["reference"] = reference
    _save(a.case, case)
    _say({"round": n, "reference": reference, "report": str(report), "validated": validated,
          "digest": str(cdir / f"iter{n}_digest.md") if case.get("format") != "subform" else str(report),
          "counts": it.get("counts"), "open_points": it.get("open_points"),
          "new_issues_not_in_any_point": list((it.get("new_issues_not_in_any_point") or {}).keys()),
          "seen_before": it.get("seen_before"),
          "next": ["read the digest / report and references/issue-guide.md; confirm each finding in the file",
                   "close open points that are gone: diem_case.py decide --status fixed --by country --note '<how>'",
                   "propose to the operator the minor text fixes DIEM can make itself; on yes: diem_case.py fix",
                   "record the remaining points: diem_case.py points",
                   "build the Word document and the email: diem_case.py outputs"]})
    return 0


# ---------------------------------------------------------------- fix
def cmd_fix(a):
    case = _load(a.case)
    if not case["iterations"]:
        raise SystemExit("run the validation first")
    src = a.source or case["iterations"][-1]["file"]
    out = _json("apply_minor_fixes.py", "--case", a.case, "--source", src, "--fixes", a.fixes, check=False)
    _say(out)
    return 0 if out.get("saved") else 1


# ---------------------------------------------------------------- points / decide / status
def cmd_points(a):
    case = _load(a.case)
    if not case["iterations"]:
        raise SystemExit("run the validation first")
    _say(_json("validation_case.py", "add-points", "--case", a.case, "--points", a.points,
               "--iteration", _iteration(case)))
    return 0


def cmd_decide(a):
    _say(_json("validation_case.py", "set", "--case", a.case, "--id", a.id, "--status", a.status,
               "--by", a.by, "--note", a.note))
    return 0


def cmd_status(a):
    _say(_json("validation_case.py", "status", "--case", a.case))
    return 0


# ---------------------------------------------------------------- outputs
def _diem_fixes(case: dict, iteration: int) -> list[dict]:
    return [p for p in case["points"] if p["tag"] == "Fixed by DIEM" and p.get("fix")
            and p.get("opened_iteration") == iteration]


def _diem_file(case: dict, iteration: int) -> str:
    files = [f["file"] for f in case.get("diem_fixed_files", []) if f["iteration"] == iteration]
    return files[-1] if files else ""


def _add_diem_table(spec: dict, fixes: list[dict], file_name: str) -> None:
    if not fixes or any(b.get("h1", "").startswith("Corrections already made by DIEM") for b in spec["blocks"]):
        return
    spec["blocks"] += [
        {"h1": "Corrections already made by DIEM"},
        {"p": f"Nothing to do on your side: these are already corrected in the attached file `{file_name}`."},
        {"table": {"header": ["Row", "Question", "Column", "Before", "After"],
                   "rows": [[str(p["fix"]["row"]), f'`{p["fix"]["question"]}`', f'`{p["fix"]["column"]}`',
                             p["fix"]["before"], p["fix"]["after"]] for p in fixes],
                   "widths": [1.4, 3.8, 2.4, 4.2, 4.2]}},
    ]


def _n(k: int, word: str) -> str:
    return f"{k} {word}{'' if k == 1 else 's'}"


def _email(case: dict, n: int, open_pts: list, fixes: list, diem_file: str, operator: str) -> str:
    tool = "GeoPoll" if case["tool"] == "geopoll" else "KoBo"
    fix = [p for p in open_pts if p["tag"] in ("To fix", "Placeholder")]
    conf = [p for p in open_pts if p["tag"] == "To confirm"]
    ref = Path(case["iterations"][-1].get("reference", "") or "").name or "the latest DIEM template"
    lines = [f'Subject: {case["country"]} {case["round"]} questionnaire – validation points' + (f" (version {n})" if n > 1 else ""),
             "", "Dear colleagues,", "",
             f"Thank you for the questionnaire. We validated it against {ref}. <one sentence: what is fine>", ""]
    if fixes:
        lines += [f"To save you time, we corrected {_n(len(fixes), 'minor text issue')} ourselves in the attached file "
                  f"({diem_file}); they are listed at the end of the document. Please make the remaining fixes in that file.", ""]
    if fix or conf:
        lines += [f"The attached document lists {_n(len(fix), 'point')} to fix and {len(conf)} to confirm, mainly:"]
        lines += [f"- {p['title']};" for p in (fix + conf)[:6]]
        lines += ["If any of these were agreed with the SMAR team, just let us know.", "",
                  "Once the file is updated, please send it back and we will check it again.", ""]
    else:
        lines += ["Nothing else is needed from your side.", ""]
    if case.get("format") == "subform":
        lines += ["One note for the next rounds: this time we checked the programmed form directly, to speed things up, "
                  "but this is an exception. From the next round, please send us the questionnaire in the DIEM GeoPoll "
                  "template format, with all its sheets filled (survey, Additional information, Crop list, etc.), so that "
                  "it can go through the standard validation before programming.", ""]
    lines += ["Best regards,", operator]
    return "\n".join(lines) + "\n"


def cmd_outputs(a):
    case = _load(a.case)
    cdir = Path(a.case).parent
    n = _iteration(case)
    if not n:
        raise SystemExit("run the validation first")
    open_pts = [p for p in case["points"] if p["status"] == "open" and p["tag"] != "Template side"]
    fixes = _diem_fixes(case, n)
    if not open_pts and not fixes:
        _say({"note": "no open point and no DIEM fix in this round: ask the operator whether to build the final package (diem_case.py final)"})
        return 0
    spec = json.loads(Path(a.spec).read_text(encoding="utf-8"))
    diem_file = Path(_diem_file(case, n)).name
    _add_diem_table(spec, fixes, diem_file)
    spec_path = cdir / f"spec_v{n}.json"
    spec_path.write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
    tag = f'{case["iso3"]}_{case["round"]}_{case["tool"]}'
    docx = cdir / f"{tag}_points_to_fix_v{n}.docx"
    try:
        if docx.exists():
            docx.open("ab").close()
    except PermissionError:
        docx = docx.with_name(docx.stem + "b.docx")
    _run("make_fix_document.py", spec_path, docx)
    email = cdir / f"{tag}_email_v{n}.txt"
    email.write_text(_email(case, n, open_pts, fixes, diem_file, a.operator), encoding="utf-8")
    send = [str(docx)] + ([str(cdir / diem_file)] if diem_file else [])
    _say({"word": str(docx), "email_draft": str(email), "corrected_questionnaire": str(cdir / diem_file) if diem_file else "",
          "send_to_country": send,
          "next": "finish the email's first sentence, check the Word document, then stop: the operator sends them. "
                  "Never send anything yourself."})
    return 0


# ---------------------------------------------------------------- final
def cmd_final(a):
    case = _load(a.case)
    st = _json("validation_case.py", "status", "--case", a.case)
    if not st.get("ready_to_close"):
        _say({"refused": "points still open", "open": st.get("open")})
        return 1
    last = case["iterations"][-1]
    ref = last.get("reference") or ""
    ref_file = next((t for t in (_latest_template(case["tool"]),) if Path(t).name in ref), _latest_template(case["tool"]))
    if case["reference_mode"] == "previous_round" and case.get("previous_round_file"):
        ref_file = case["previous_round_file"]
    # A DIEM-corrected copy of the last file is what goes out when it exists.
    diem_file = _diem_file(case, len(case["iterations"]))
    if diem_file and case.get("format") == "subform":
        last["validated"] = diem_file
        _save(a.case, case)
    elif diem_file and Path(diem_file).name != Path(last["file"]).name:
        # Template format: the validated questionnaire must be built from the corrected copy.
        _say({"refused": "DIEM fixed the last file after the run: validate the corrected copy first",
              "next": f'python diem_case.py run --case "{a.case}" --file "{diem_file}"'})
        return 1
    res = _json("build_final_package.py", "--case", a.case, "--reference", ref_file)
    tool = "GeoPoll" if case["tool"] == "geopoll" else "KoBo"
    case = _load(a.case)
    nfix = sum(1 for p in case["points"] if p["tag"] == "Fixed by DIEM")
    cdir = Path(a.case).parent
    tag = f'{case["iso3"]}_{case["round"]}_{case["tool"]}'
    mail = [f'Subject: {case["country"]} {case["round"]} questionnaire – validated', "", "Dear colleagues,", "",
            f'The {case["country"]} {case["round"]} {tool} questionnaire is validated. Attached:',
            f'- the validated questionnaire ({Path(res["final_questionnaire"]).name}), to '
            + ("send to GeoPoll;" if case["tool"] == "geopoll" else "deploy in KoBo;"),
            "- the final validation report: the questionnaire composition, the changes made during the validation"
            + (f", the {nfix} minor corrections we made ourselves" if nfix else "")
            + " and the exceptions agreed.", "",
            "Thank you for the quick follow-up.", "", "Best regards,", a.operator]
    (cdir / f"{tag}_final_email.txt").write_text("\n".join(mail) + "\n", encoding="utf-8")
    _say({**{k: res[k] for k in ("final_questionnaire", "final_report", "spec")},
          "final_email": str(cdir / f"{tag}_final_email.txt"),
          "next": "check the final questionnaire (no #/$ placeholder left) and the report, then give the files to the operator"})
    return 0


# ---------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("setup"); s.add_argument("--fix", action="store_true")
    s = sub.add_parser("start")
    s.add_argument("--file", required=True)
    s.add_argument("--tool", choices=["kobo", "geopoll"])
    s.add_argument("--reference", choices=["latest", "previous"])
    s.add_argument("--previous-round", default="")
    s.add_argument("--languages", default="")
    s.add_argument("--deploy-language", default="")
    for k in ("country", "iso3", "round", "kobo_reference"):
        s.add_argument(f"--{k.replace('_', '-')}", default="")
    s = sub.add_parser("run"); s.add_argument("--case", required=True); s.add_argument("--file", required=True)
    s = sub.add_parser("fix"); s.add_argument("--case", required=True); s.add_argument("--fixes", required=True)
    s.add_argument("--source", default="")
    s = sub.add_parser("points"); s.add_argument("--case", required=True); s.add_argument("--points", required=True)
    s = sub.add_parser("outputs"); s.add_argument("--case", required=True); s.add_argument("--spec", required=True)
    s.add_argument("--operator", default="<operator name>")
    s = sub.add_parser("decide")
    for k in ("case", "id", "status"):
        s.add_argument(f"--{k}", required=True)
    s.add_argument("--by", required=True); s.add_argument("--note", default="")
    s = sub.add_parser("status"); s.add_argument("--case", required=True)
    s = sub.add_parser("final"); s.add_argument("--case", required=True); s.add_argument("--operator", default="<operator name>")
    a = ap.parse_args()
    return {"setup": cmd_setup, "start": cmd_start, "run": cmd_run, "fix": cmd_fix, "points": cmd_points,
            "outputs": cmd_outputs, "decide": cmd_decide, "status": cmd_status, "final": cmd_final}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
