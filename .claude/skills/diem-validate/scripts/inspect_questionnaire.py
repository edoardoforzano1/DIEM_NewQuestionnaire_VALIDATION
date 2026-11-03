"""
Quick facts about a country questionnaire, to confirm with the analyst
BEFORE running the validator (languages in scope, deployment language,
modality, form type...). Read-only: opens the file with openpyxl in
read-only mode and prints JSON.

Usage
-----
  python inspect_questionnaire.py "<questionnaire.xlsx>"
"""
from __future__ import annotations

import json
import re
import sys

import openpyxl

_LANG_RE = re.compile(r"::\s*([^()]*?)\s*\((\w+)\)\s*$")


def _rows(ws):
    return [r for r in ws.iter_rows(values_only=True)]


def _lang_of(header: str) -> str | None:
    m = _LANG_RE.search(header or "")
    return m.group(2).lower() if m else None


def main() -> int:
    path = sys.argv[1]
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    out: dict = {"file": path, "sheets": wb.sheetnames}
    hidden = [ws.title for ws in wb.worksheets if ws.sheet_state != "visible"]
    if hidden:
        out["hidden_sheets"] = hidden

    if "survey" not in wb.sheetnames:
        print(json.dumps({**out, "error": "no survey sheet"}, ensure_ascii=False, indent=2))
        return 1
    rows = _rows(wb["survey"])
    headers = [str(h).strip() if h is not None else "" for h in rows[0]]
    body = [r for r in rows[1:] if r and any(c is not None for c in r)]
    tool = "geopoll" if "varname_new" in headers else ("kobo" if {"type", "name"} <= set(headers) else "unknown")
    out["tool"] = tool
    name_col = "varname_new" if tool == "geopoll" else "name"
    ni = headers.index(name_col) if name_col in headers else None
    names = [str(r[ni]).strip() for r in body if ni is not None and ni < len(r) and r[ni]]
    out["n_questions"] = len(names)
    out["prefixes"] = {p: sum(n.startswith(p) for n in names) for p in ("c_", "o_", "kii_")}
    out["looks_like_kii"] = out["prefixes"]["kii_"] > 10

    # Filled cells per language for label / hint columns
    lang_fill: dict[str, dict[str, int]] = {}
    for i, h in enumerate(headers):
        lang = _lang_of(h)
        if not lang or not h.split("::")[0].lower().startswith(("label", "hint")):
            continue
        n = sum(1 for r in body if i < len(r) and r[i] not in (None, ""))
        lang_fill.setdefault(lang, {})[h.split("::")[0]] = n
    out["survey_language_fill"] = lang_fill
    out["has_module_column"] = "module" in headers

    if "settings" in wb.sheetnames:
        s = _rows(wb["settings"])
        if len(s) >= 2:
            out["settings"] = {str(k): v for k, v in zip(s[0], s[1]) if k}

    # Additional information: filled Replacement cells per language column
    if "Additional information" in wb.sheetnames:
        ai = _rows(wb["Additional information"])
        hdr = next((r for r in ai[:3] if r and any(str(c or "").strip().lower().startswith("original") for c in r)), None)
        if hdr:
            h = [str(c).strip() if c is not None else "" for c in hdr]
            start = ai.index(hdr) + 1
            out["additional_info_filled"] = {
                col: sum(1 for r in ai[start:] if i < len(r) and r[i] not in (None, ""))
                for i, col in enumerate(h) if col.lower().startswith("replacement")
            }

    if tool == "kobo" and ni is not None:
        ci = headers.index("calculation") if "calculation" in headers else None
        for r in body:
            if ci is not None and str(r[ni]).strip() == "Sample":
                out["sample_calculation"] = r[ci]
    print(json.dumps(out, ensure_ascii=False, indent=2, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
