"""
Validation case tracker: remembers one country questionnaire across rounds of
"validate -> send points to the country -> receive a new version -> validate
again", so the next run knows what is still pending.

One case = one country + tool + round, stored next to that tool's reports:
    <output_dir>/<tool>_output/validation_cases/<ISO3>_<round>/case.json
(e.g. geopoll_output/validation_cases/YEM_R1/). Output housekeeping never
archives or deletes anything in validation_cases: cases are the record. Every file produced for the
case (fix document, emails, final report) goes in the same folder.

A *point* is one item sent to the country team (or to SMAR): it has a
section, a type (To fix / To confirm / Placeholder / Optional / Template side),
a title, and a status:
    open      still to be solved
    fixed     no longer found in a later run (proposed by `iterate`, confirmed by the agent)
    accepted  closed by the operator: an agreed exception ("SMAR confirmed ...")
    dropped   not a real problem / withdrawn by the operator
Points carry `keys` ("issue_type|Q Name or Set" from the report) and/or
`output_match` (text of a WARN/FAIL line of check_validated_output.py), so a
new run can tell whether each point is still there.

Country history: the case files ARE the record, so nothing is copied. The
`history` command reads every earlier case of the same country (any round,
optionally one tool) and prints each point once, with its final status and
the note saying how it was solved. `iterate` also returns `seen_before`:
for the issues of the new run, the earlier rounds where the same key was a
point and how it ended — so a recurring problem comes with its past solution.
Write the solution in the note when closing a point (`set --note`), e.g.
"country restored the template Conditional", not just "not found".

Commands (all print JSON or plain text; nothing here touches the questionnaire):
  new        create a case               --root --country --iso3 --tool --round
                                           --reference-mode [--previous-round] --languages
                                           --deploy-language --source
  find       list cases (open counts)     --root [--iso3]
  keys       report issue keys            --report [--all]   (high+medium by default)
  add-points add points from a JSON list  --case --points points.json --iteration N
             (each: section, tag, title, [detail, keys, output_match,
              status + note + by to record it already accepted/dropped])
  iterate    record a new run and compare --case --file --report --validated [--output-check]
  set        change a point's status      --case --id P03 --status accepted --note "..." --by "..."
  status     open / closed points         --case
  history    earlier rounds of a country  --root --iso3 [--tool] [--exclude-case case.json]
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import openpyxl  # noqa: E402
from summarize_report import read_issue_rows  # noqa: E402

STATUSES = ("open", "fixed", "accepted", "dropped")
TAGS = ("To fix", "To confirm", "Placeholder", "Optional", "Template side")


def case_dir_for(root, tool: str, iso3: str, rnd: str) -> Path:
    """<output_dir>/<tool>_output/validation_cases/<ISO3>_<round>/"""
    return Path(root) / f"{tool.lower()}_output" / "validation_cases" / f"{iso3.upper()}_{rnd}"


def _now() -> str:
    return _dt.datetime.now().strftime("%Y-%m-%d %H:%M")


def _root_of(case_path) -> Path:
    """<root>/<tool>_output/validation_cases/<ISO3>_<round>/case.json -> <root>"""
    return Path(case_path).resolve().parents[3]


def _other_cases(root, iso3: str, tool: str = "", exclude: str = "") -> list[tuple[Path, dict]]:
    """Earlier cases of the same country, oldest first."""
    ex = Path(exclude).resolve() if exclude else None
    out = []
    for p in Path(root).glob("*_output/validation_cases/*/case.json"):
        if ex is not None and p.resolve() == ex:
            continue
        c = _load(p)
        if c.get("iso3") != iso3.upper() or (tool and c.get("tool") != tool):
            continue
        out.append((p, c))
    return sorted(out, key=lambda pc: pc[1].get("created", ""))


def _outcome(p: dict) -> str:
    """One line: final status, who, and how it was solved."""
    r = p.get("resolution") or {}
    if p["status"] == "open":
        return "still open"
    by = f' by {r["by"]}' if r.get("by") and r["by"] not in ("agent", "operator") else ""
    note = f': {r["note"]}' if r.get("note") else ""
    return f'{p["status"]}{by}{note}'


def seen_before(case: dict, case_path, keys: list[str]) -> dict[str, list[str]]:
    """For each key, the earlier rounds of this country where it was a point."""
    hits: dict[str, list[str]] = {}
    for _, c in _other_cases(_root_of(case_path), case["iso3"], exclude=str(case_path)):
        for p in c["points"]:
            for k in set(p.get("keys", [])) & set(keys):
                hits.setdefault(k, []).append(
                    f'{c["round"]} {c["tool"]} {p["id"]} "{p["title"]}" → {_outcome(p)}')
    return hits


def cmd_history(a) -> list:
    """Every earlier point of the country, once, with its final outcome."""
    out = []
    for p, c in _other_cases(a.root, a.iso3, a.tool, a.exclude_case):
        out.append({
            "case": f'{c["country"]} {c["tool"]} {c["round"]}',
            "iterations": len(c["iterations"]),
            "validated": bool(c.get("closed")),
            "points": [f'{x["id"]} [{x["tag"]}] {x["section"]} — {x["title"]} → {_outcome(x)}' for x in c["points"]],
        })
    return out


def _load(path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _save(path, case) -> None:
    Path(path).write_text(json.dumps(case, ensure_ascii=False, indent=2), encoding="utf-8")


def report_keys(report: str, severities=("high", "medium")) -> dict[str, dict]:
    """{'issue_type|Q Name or Set': {severity, sheet, field}} for the report's issue rows."""
    wb = openpyxl.load_workbook(report, read_only=True, data_only=True)
    keys = {}
    for name in wb.sheetnames:
        if name == "Summary":
            continue
        for d in read_issue_rows(wb[name]):
            sev = str(d.get("Severity") or "").lower()
            if severities and sev not in severities:
                continue
            itype = str(d.get("Issue type") or d.get("Check") or "?").strip()
            target = str(d.get("Q Name") or d.get("Set") or "").strip()
            keys.setdefault(f"{itype}|{target}", {
                "severity": sev, "sheet": name,
                "field": str(d.get("Field") or d.get("Detail") or "")[:160],
            })
    return keys


def output_problem_lines(path: str) -> list[str]:
    """WARN / FAIL lines of a saved check_validated_output.py result."""
    if not path:
        return []
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    return [l for l in text.splitlines() if "**FAIL**" in l or "**WARN**" in l]


def cmd_new(a) -> dict:
    case_dir = case_dir_for(a.root, a.tool, a.iso3, a.round)
    case_dir.mkdir(parents=True, exist_ok=True)
    path = case_dir / "case.json"
    if path.exists():
        return {"exists": str(path), "note": "case already exists; use it"}
    case = {
        "country": a.country, "iso3": a.iso3.upper(), "tool": a.tool, "round": a.round,
        "reference_mode": a.reference_mode, "previous_round_file": a.previous_round or "",
        "languages": [l.strip().lower() for l in a.languages.split(",") if l.strip()],
        "deploy_language": a.deploy_language.lower(), "source": a.source,
        "created": _now(), "closed": None, "iterations": [], "points": [],
    }
    _save(path, case)
    return {"created": str(path)}


def cmd_find(a) -> list:
    out = []
    for p in sorted(Path(a.root).glob("*_output/validation_cases/*/case.json")):
        c = _load(p)
        if a.iso3 and c["iso3"] != a.iso3.upper():
            continue
        st = [pt["status"] for pt in c["points"]]
        out.append({
            "case": str(p), "country": c["country"], "tool": c["tool"], "round": c["round"],
            "iterations": len(c["iterations"]), "open": st.count("open"),
            "closed": len(st) - st.count("open"), "final_done": bool(c.get("closed")),
            "last_file": c["iterations"][-1]["file"] if c["iterations"] else "",
        })
    return out


def cmd_add_points(a) -> dict:
    case = _load(a.case)
    new = json.loads(Path(a.points).read_text(encoding="utf-8"))
    n = len(case["points"])
    added = []
    for p in new:
        if p.get("tag") not in TAGS:
            raise SystemExit(f"tag must be one of {TAGS}: {p}")
        n += 1
        pid = f"P{n:02d}"
        # A point can be recorded as already closed (e.g. a difference agreed
        # before the run): give "status" plus "note" and "by". It is still
        # tracked, so later runs do not report it as new, and it appears in
        # the final report's exceptions.
        status = p.get("status", "open")
        if status not in STATUSES:
            raise SystemExit(f"status must be one of {STATUSES}: {p}")
        hist = {"iteration": a.iteration, "status": status, "date": _now()}
        resolution = None
        if status != "open":
            hist.update(note=p.get("note", ""), by=p.get("by", "operator"))
            resolution = {"status": status, "note": p.get("note", ""), "by": p.get("by", "operator"),
                          "date": _now(), "iteration": a.iteration}
        case["points"].append({
            "id": pid, "section": p["section"], "tag": p["tag"], "title": p["title"],
            "detail": p.get("detail", ""), "keys": p.get("keys", []),
            "output_match": p.get("output_match", []), "status": status,
            "opened_iteration": a.iteration, "history": [hist], "resolution": resolution,
        })
        added.append(pid)
    _save(a.case, case)
    return {"added": added}


def cmd_iterate(a) -> dict:
    case = _load(a.case)
    keys = report_keys(a.report)
    problems = output_problem_lines(a.output_check)
    it = {
        "n": len(case["iterations"]) + 1, "date": _now(), "file": a.file,
        "report": a.report, "validated": a.validated, "output_check": a.output_check,
        "counts": {s: sum(1 for v in report_keys(a.report, (s,)).values()) for s in ("high", "medium", "info")},
    }
    case["iterations"].append(it)
    proposals, covered = [], set()
    for p in case["points"]:
        covered.update(p["keys"])
        if p["status"] != "open":
            continue
        if not p["keys"] and not p["output_match"]:
            proposals.append({"id": p["id"], "title": p["title"], "proposal": "check by hand (no automatic key)"})
            continue
        still = [k for k in p["keys"] if k in keys] + [m for m in p["output_match"] if any(m in l for l in problems)]
        proposals.append({
            "id": p["id"], "title": p["title"], "tag": p["tag"],
            "proposal": "still present" if still else "not found any more -> fixed?",
            "evidence": still,
        })
    uncovered = {k: v for k, v in keys.items() if k not in covered}
    open_keys = [k for p in case["points"] if p["status"] == "open" for k in p["keys"]]
    _save(a.case, case)
    return {"iteration": it["n"], "counts": it["counts"], "open_points": proposals,
            "new_issues_not_in_any_point": uncovered, "output_check_problems": problems,
            "seen_before": seen_before(case, a.case, list(uncovered) + open_keys)}


def cmd_set(a) -> dict:
    case = _load(a.case)
    if a.status not in STATUSES:
        raise SystemExit(f"status must be one of {STATUSES}")
    it = len(case["iterations"])
    changed = []
    for pid in a.id.split(","):
        p = next((x for x in case["points"] if x["id"] == pid.strip()), None)
        if p is None:
            raise SystemExit(f"no point {pid}")
        p["status"] = a.status
        p["history"].append({"iteration": it, "status": a.status, "date": _now(), "note": a.note, "by": a.by})
        p["resolution"] = None if a.status == "open" else {"status": a.status, "note": a.note, "by": a.by, "date": _now(), "iteration": it}
        changed.append(p["id"])
    _save(a.case, case)
    return {"changed": changed, "status": a.status}


def cmd_status(a) -> dict:
    case = _load(a.case)
    pts = case["points"]
    pick = lambda s: [{k: p[k] for k in ("id", "section", "tag", "title", "resolution")} for p in pts if p["status"] == s]
    return {
        "case": f'{case["country"]} {case["tool"]} {case["round"]}', "iterations": len(case["iterations"]),
        "last_iteration": case["iterations"][-1] if case["iterations"] else None,
        "open": pick("open"), "fixed": pick("fixed"), "accepted": pick("accepted"), "dropped": pick("dropped"),
        "ready_to_close": bool(pts) and not any(p["status"] == "open" for p in pts),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("new")
    for k in ("root", "country", "iso3", "tool", "round", "reference_mode", "languages", "deploy_language", "source"):
        s.add_argument(f"--{k.replace('_', '-')}", required=True)
    s.add_argument("--previous-round", default="")
    s = sub.add_parser("find"); s.add_argument("--root", required=True); s.add_argument("--iso3", default="")
    s = sub.add_parser("keys"); s.add_argument("--report", required=True); s.add_argument("--all", action="store_true")
    s = sub.add_parser("add-points"); s.add_argument("--case", required=True); s.add_argument("--points", required=True); s.add_argument("--iteration", type=int, required=True)
    s = sub.add_parser("iterate")
    for k in ("case", "file", "report", "validated"):
        s.add_argument(f"--{k}", required=True)
    s.add_argument("--output-check", default="")
    s = sub.add_parser("set")
    for k in ("case", "id", "status"):
        s.add_argument(f"--{k}", required=True)
    s.add_argument("--note", default=""); s.add_argument("--by", default="operator")
    s = sub.add_parser("status"); s.add_argument("--case", required=True)
    s = sub.add_parser("history"); s.add_argument("--root", required=True); s.add_argument("--iso3", required=True)
    s.add_argument("--tool", default=""); s.add_argument("--exclude-case", default="")
    a = ap.parse_args()

    if a.cmd == "keys":
        res = report_keys(a.report, ("high", "medium", "info") if a.all else ("high", "medium"))
    else:
        res = {"new": cmd_new, "find": cmd_find, "add-points": cmd_add_points, "iterate": cmd_iterate,
               "set": cmd_set, "status": cmd_status, "history": cmd_history}[a.cmd](a)
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
