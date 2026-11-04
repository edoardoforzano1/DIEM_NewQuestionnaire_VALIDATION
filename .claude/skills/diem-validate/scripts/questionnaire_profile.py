"""
Composition of a country questionnaire compared with its reference, for the
summary message and the final validation report. Read-only; prints JSON.

  - questions by type (mandatory / recommended / low priority / customized),
    spiels counted separately, for the country file and the reference
  - questions added and removed, grouped by type (removed ones take the
    reference's type, added ones the country's)
  - admin levels: rows per level (GeoPoll "Admin N info" sheets; KoBo admin
    choice lists)
  - selected crops (Crop list sheet)
  - interview length from the "Weighted duration" column (seconds -> minutes)

Works for GeoPoll (survey `varname_new` + `module`) and KoBo (survey `name`).
A row counts as a question when it has a variable name and a filled
`Mandatory` cell; that is how both templates mark their questions.

Usage:
  python questionnaire_profile.py COUNTRY.xlsx REFERENCE.xlsx [--validated VALIDATED.xlsx]
--validated: take admin lists from the validated questionnaire (refreshed
from AGOL) instead of the country file.
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys

import openpyxl

ORDER = ["mandatory", "recommended", "low priority", "customized", "other"]


def category(mandatory) -> str:
    m = str(mandatory or "").strip().lower()
    if m == "spiel":
        return "spiel"
    if m.startswith("yes"):
        return "mandatory"
    if "recommended" in m:
        return "recommended"
    if "low priority" in m:
        return "low priority"
    if "custom" in m:
        return "customized"
    return "other"


def _sheet(wb, name):
    return next((wb[n] for n in wb.sheetnames if n.strip().lower() == name.lower()), None)


def read_questions(path) -> tuple[str, dict[str, str], dict[str, dict]]:
    """Returns (tool, {variable: category} in file order, {variable: row dict})."""
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    rows = list(_sheet(wb, "survey").iter_rows(values_only=True))
    hdr = [str(c).strip() if c is not None else "" for c in rows[0]]
    tool = "geopoll" if "varname_new" in hdr else "kobo"
    name_col = "varname_new" if tool == "geopoll" else "name"
    mand_col = next((h for h in hdr if h.lower() == "mandatory"), None)
    out, full = {}, {}
    for r in rows[1:]:
        d = dict(zip(hdr, r))
        name = str(d.get(name_col) or "").strip()
        if not name or not mand_col or not str(d.get(mand_col) or "").strip():
            continue
        if tool == "geopoll" and not str(d.get("module") or "").strip():
            continue  # section banner rows
        out.setdefault(name, category(d.get(mand_col)))
        full.setdefault(name, d)
    return tool, out, full


def read_admin(path, tool) -> dict:
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    levels = {}
    if tool == "geopoll":
        for lvl in range(1, 5):
            ws = _sheet(wb, f"Admin {lvl} info")
            if ws is not None:
                levels[f"admin{lvl}"] = sum(1 for r in list(ws.iter_rows(values_only=True))[1:] if any(r))
    else:
        ws = _sheet(wb, "choices")
        if ws is not None:
            rows = list(ws.iter_rows(values_only=True))
            hdr = [str(c).strip() if c is not None else "" for c in rows[0]]
            if "list_name" in hdr:
                li = hdr.index("list_name")
                counts = collections.Counter(str(r[li]).strip() for r in rows[1:] if r and r[li])
                for lst, n in counts.items():
                    m = re.search(r"adm(?:in)?_?(\d)", lst.lower())
                    if m:
                        levels[f"admin{m.group(1)} ({lst})"] = n
    return levels


def read_crops(path) -> list[str]:
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = _sheet(wb, "Crop list")
    if ws is None:
        return []
    rows = list(ws.iter_rows(values_only=True))
    for i, r in enumerate(rows[:6]):
        hdr = [str(c).strip() if c is not None else "" for c in r]
        sel = next((j for j, h in enumerate(hdr) if h.lower().startswith("select top")), None)
        lab = next((j for j, h in enumerate(hdr) if h.lower() in ("label (en)", "label(en)")), None)
        if sel is not None and lab is not None:
            return [str(x[lab]).strip() for x in rows[i + 1:]
                    if x and len(x) > max(sel, lab) and str(x[sel] or "").strip().lower() not in ("", "0", "none", "nan")]
    return []


def length_minutes(full: dict[str, dict], cats: dict[str, str]) -> dict:
    tot = collections.Counter()
    for name, d in full.items():
        try:
            tot[cats[name]] += float(d.get("Weighted duration") or 0) / 60
        except (TypeError, ValueError):
            pass
    core_rec = tot["mandatory"] + tot["spiel"] + tot["recommended"]
    return {
        "mandatory_and_recommended": round(core_rec, 1),
        "total": round(sum(tot.values()), 1),
        "by_type": {k: round(v, 1) for k, v in tot.items()},
    }


def _counts(cats: dict[str, str]) -> dict:
    c = collections.Counter(cats.values())
    return {
        "questions": sum(v for k, v in c.items() if k != "spiel"),
        "spiels": c.get("spiel", 0),
        "by_type": {k: c[k] for k in ORDER if c.get(k)},
    }


def _group(names, cats) -> dict:
    g = collections.OrderedDict((k, []) for k in ORDER + ["spiel"])
    for n in names:
        g[cats[n]].append(n)
    return {k: v for k, v in g.items() if v}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("country")
    ap.add_argument("reference")
    ap.add_argument("--validated", default="")
    a = ap.parse_args()

    tool, cur, cur_full = read_questions(a.country)
    _, ref, _ = read_questions(a.reference)
    added = [n for n in cur if n not in ref]
    removed = [n for n in ref if n not in cur]
    out = {
        "tool": tool,
        "country": _counts(cur),
        "reference": _counts(ref),
        "added": {"total": len(added), "by_type": _group(added, cur)},
        "removed": {"total": len(removed), "by_type": _group(removed, ref)},
        "admin_levels": read_admin(a.validated or a.country, tool),
        "admin_source": "validated questionnaire (refreshed from AGOL)" if a.validated else "country file",
        "selected_crops": read_crops(a.country),
        "interview_length_min": length_minutes(cur_full, cur),
    }
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
