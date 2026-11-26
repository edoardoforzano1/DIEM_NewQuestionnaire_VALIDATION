"""
Apply minor fixes made by DIEM to a COPY of the country questionnaire, and
record them in the case, so the country office only deals with the real
problems.

Minor fixes are text-only corrections that do not change what is asked or
who is asked: typos, doubled words or punctuation, unbalanced brackets, an
option left in English in another language column, a placeholder that still
shows its # / $ signs, a repeated operator instruction, a `Mandatory` value
spelled differently. Never use it for routing, conditions, relevant,
constraints, calculations, adding or removing questions or options: those
stay points for the country.

Usage:
    python apply_minor_fixes.py --case case.json --source FILE.xlsx --fixes fixes.json [--out OUT.xlsx]

fixes.json — a list; each fix locates one cell either by address or by
question name + column header:
  {"sheet": "Subform", "cell": "F10", "old": "1)CONTINUE", "new": "1)CONTINUER",
   "question": "introduction", "column": "fr_French", "reason": "French option left in English"}
  {"sheet": "survey", "question": "hh_agricactivity_now_", "column": "label::English (en)",
   "old": "actvity", "new": "activity", "reason": "typo"}
`old` must occur exactly once in the cell, otherwise nothing is saved.

Output: <case dir>/<source stem>_DIEM-fixes.xlsx (rich text in comment cells
kept). Each fix becomes a case point with tag "Fixed by DIEM", status fixed,
and a `fix` record (row, question, column, before, after, file) that the
Word document, the email and the final report list.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
from pathlib import Path

import openpyxl

NAME_HEADERS = ("name", "Q Name", "varname_new")


def _header_row(ws) -> tuple[int, dict]:
    for r in range(1, 6):
        vals = {str(c.value).strip(): c.column for c in ws[r] if c.value not in (None, "")}
        if any(h in vals for h in NAME_HEADERS):
            return r, vals
    raise SystemExit(f"sheet {ws.title}: no header row with {NAME_HEADERS}")


def _locate(ws, fx) -> tuple[int, int]:
    if fx.get("cell"):
        c = ws[fx["cell"]]
        return c.row, c.column
    hr, H = _header_row(ws)
    name_col = next(H[h] for h in NAME_HEADERS if h in H)
    if fx["column"] not in H:
        raise SystemExit(f'{ws.title}: no column "{fx["column"]}"')
    for r in range(hr + 1, ws.max_row + 1):
        if str(ws.cell(r, name_col).value or "").strip() == fx["question"]:
            return r, H[fx["column"]]
    raise SystemExit(f'{ws.title}: no question "{fx["question"]}"')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True)
    ap.add_argument("--source", required=True)
    ap.add_argument("--fixes", required=True)
    ap.add_argument("--out", default="")
    a = ap.parse_args()

    case_path = Path(a.case)
    case = json.loads(case_path.read_text(encoding="utf-8"))
    fixes = json.loads(Path(a.fixes).read_text(encoding="utf-8"))
    src = Path(a.source)
    out = Path(a.out) if a.out else case_path.parent / f"{re.sub(r'_DIEM-(text-)?fixes$', '', src.stem)}_DIEM-fixes.xlsx"

    wb = openpyxl.load_workbook(src, rich_text=True)
    errors, done = [], []
    for fx in fixes:
        ws = wb[fx.get("sheet") or wb.sheetnames[0]]
        r, c = _locate(ws, fx)
        cell = ws.cell(r, c)
        val = cell.value if isinstance(cell.value, str) else str(cell.value or "")
        n = val.count(fx["old"])
        if n != 1:
            errors.append(f'{ws.title}!{cell.coordinate}: "{fx["old"][:60]}" found {n} times')
            continue
        cell.value = val.replace(fx["old"], fx["new"])
        hr, H = _header_row(ws)
        col_name = fx.get("column") or next((h for h, i in H.items() if i == c), cell.column_letter)
        q = fx.get("question") or str(ws.cell(r, next(H[h] for h in NAME_HEADERS if h in H)).value or "")
        done.append({"sheet": ws.title, "row": r, "cell": cell.coordinate, "question": q, "column": col_name,
                     "before": fx["old"], "after": fx["new"] or "(removed)", "reason": fx.get("reason", "")})
    if errors:
        print(json.dumps({"saved": False, "errors": errors}, ensure_ascii=False, indent=2))
        return 1
    wb.save(out)

    it = len(case["iterations"])
    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    n = len(case["points"])
    ids = []
    for d in done:
        n += 1
        pid = f"P{n:02d}"
        note = f'{d["column"]}: "{d["before"]}" -> "{d["after"]}"'
        res = {"status": "fixed", "note": note, "by": "DIEM", "date": now, "iteration": it}
        case["points"].append({
            "id": pid, "section": d["sheet"], "tag": "Fixed by DIEM",
            "title": f'{d["question"]}: {d["reason"] or "text correction"}', "detail": note,
            "keys": [], "output_match": [], "status": "fixed", "opened_iteration": it,
            "history": [dict(res)], "resolution": res, "fix": {**d, "file": out.name},
        })
        ids.append(pid)
    case.setdefault("diem_fixed_files", []).append({"iteration": it, "file": str(out), "source": str(src)})
    case_path.write_text(json.dumps(case, ensure_ascii=False, indent=2), encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps({"saved": str(out), "points": ids, "fixes": done}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
