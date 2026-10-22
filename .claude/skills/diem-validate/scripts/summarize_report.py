"""
Condense a DIEM validation report (report_{tool}_{lang}_{ISO3}_*.xlsx) into a
compact Markdown digest that is cheap to read: the Summary sheet's status
rows, issue counts per sheet x severity, and every high/medium issue grouped
by issue type. Info rows are only counted (pass --show-info to list them).

Usage:
  python summarize_report.py REPORT.xlsx [--show-info] [--max-len 220]
"""
from __future__ import annotations

import argparse
import collections
import sys

import openpyxl

STATUS_WORDS = {"PASS", "FAIL", "WARN", "WARNING", "INFO"}
SEVERITIES = ("high", "medium", "info")


def _clip(v, n):
    s = " ".join(str(v).split())
    return s if len(s) <= n else s[: n - 1] + "…"


def read_issue_rows(ws):
    """Yield dicts for every data row under any header row containing 'Severity'.
    Report sheets stack several sections, each with its own header row."""
    header = None
    for row in ws.iter_rows(values_only=True):
        cells = [c for c in row]
        labels = [str(c).strip() if c is not None else "" for c in cells]
        if "Severity" in labels:
            header = labels
            continue
        if header is None or not any(c not in (None, "") for c in cells):
            continue
        d = {h: c for h, c in zip(header, cells) if h}
        sev = str(d.get("Severity") or "").strip().lower()
        if sev in SEVERITIES:
            yield d


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("--show-info", action="store_true")
    ap.add_argument("--max-len", type=int, default=220)
    a = ap.parse_args()

    wb = openpyxl.load_workbook(a.report, read_only=True, data_only=True)
    out = [f"# Report digest: {a.report.replace(chr(92), '/').split('/')[-1]}", ""]

    if "Summary" in wb.sheetnames:
        out += ["## Summary sheet", ""]
        for row in wb["Summary"].iter_rows(values_only=True):
            vals = [c for c in row if c not in (None, "")]
            if not vals:
                continue
            if len(vals) >= 2 and str(vals[1]).strip().upper() in STATUS_WORDS:
                out.append(f"- **{vals[1]}** {vals[0]}: {_clip(' | '.join(map(str, vals[2:])), a.max_len)}")
            elif len(vals) == 1 and len(str(vals[0])) < 140:
                out.append(f"- {vals[0]}")
            elif str(vals[0]).startswith(("Estimated duration", "Checked against", "Current questionnaire", "Language scope")):
                out.append(f"- {_clip(' '.join(map(str, vals)), a.max_len)}")
        out.append("")

    counts = collections.Counter()
    grouped = collections.defaultdict(list)
    for name in wb.sheetnames:
        if name == "Summary":
            continue
        for d in read_issue_rows(wb[name]):
            sev = str(d["Severity"]).lower()
            itype = str(d.get("Issue type") or d.get("Check") or "?")
            counts[(name, sev)] += 1
            if sev != "info" or a.show_info:
                grouped[(sev, name, itype)].append(d)

    out += ["## Counts", "", "| Sheet | high | medium | info |", "|---|---|---|---|"]
    for name in [n for n in wb.sheetnames if n != "Summary"]:
        row = [counts[(name, s)] for s in SEVERITIES]
        if any(row):
            out.append(f"| {name} | " + " | ".join(map(str, row)) + " |")
    out.append("")

    order = {s: i for i, s in enumerate(SEVERITIES)}
    for (sev, sheet, itype), rows in sorted(grouped.items(), key=lambda k: (order[k[0][0]], k[0][1], k[0][2])):
        out.append(f"## [{sev}] {itype} — {sheet} ({len(rows)})")
        for d in rows:
            q = d.get("Q Name") or d.get("Set") or ""
            parts = [f"`{q}`" if q else "", str(d.get("Field") or d.get("Detail") or "")]
            cur, ref = d.get("Current value"), d.get("Reference / rule")
            line = " ".join(p for p in parts if p)
            if cur not in (None, ""):
                line += f" | current: {_clip(cur, a.max_len)}"
            if ref not in (None, ""):
                line += f" | ref: {_clip(ref, a.max_len)}"
            if d.get("Excel row"):
                line += f" | row {d['Excel row']}"
            out.append(f"- {line}")
        out.append("")

    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
