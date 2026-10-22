"""
Independent checks on a *validated questionnaire* produced by the DIEM
validator (validated_questionnaire_{tool}_{lang}_{ISO3}_*.xlsx) -- i.e. the
file that will actually be sent to GeoPoll / deployed in KoBo. The report
says what differs from the template; this script checks that the output is
deployable: every placeholder replaced, crops sorted, Additional information
complete, TLU weights valid, admin lists present, interview length OK.

It reads the file only; it never modifies it.

Usage:
  python check_validated_output.py VALIDATED.xlsx [--source ORIGINAL.xlsx] [--loi-limit 30]

--source: the country file before validation; used to tell which language
columns the country actually filled (so blank AR replacements only matter
when the AR text is in use).
"""
from __future__ import annotations

import argparse
import collections
import re
import sys

import openpyxl

TEXT_COLS = ["English", "French", "Arabic", "Spanish", "Portuguese", "Local Language",
             "Skip pattern", "Skip Pattern", "Conditional", "varname_new_multiple", "Notes"]
LANG_COLS = {"EN": "English", "FR": "French", "AR": "Arabic", "ES": "Spanish", "PT": "Portuguese"}
PLACEHOLDER = re.compile(r"\$[^$\r\n]+\$")
RUNTIME_VAR = re.compile(r"#[A-Za-z][A-Za-z0-9_ /]{1,40}#")
REPEATED_WORD = re.compile(r"(?<!\w)(\w{3,})\s+\1(?!\w)", re.UNICODE)
OPTION = re.compile(r"(?m)^\s*(\d+)\)\s*(.+?)\s*$")
# Latin words legitimately found in Arabic questionnaire text.
LATIN_OK_IN_ARABIC = {"geopoll", "sms", "whatsapp", "mobile", "money", "operator", "hint", "null", "admin"}

results: list[tuple[str, str, str]] = []  # (status, check, details)


def add(status, check, details=""):
    results.append((status, check, details))


def sheet(wb, name):
    return next((wb[n] for n in wb.sheetnames if n.strip().lower() == name.lower()), None)


def rows_with_header(ws, must_contain: str, scan=6):
    rows = list(ws.iter_rows(values_only=True))
    for i, r in enumerate(rows[:scan]):
        labels = [str(c).strip() if c is not None else "" for c in r]
        if any(must_contain.lower() == l.lower() or l.lower().startswith(must_contain.lower()) for l in labels):
            return labels, [dict(zip(labels, x)) for x in rows[i + 1:] if any(c is not None for c in x)], i + 1
    return None, [], 0


def check_survey(wb, src_wb, loi_limit):
    ws = sheet(wb, "survey")
    if ws is None:
        add("FAIL", "survey sheet", "missing")
        return {}
    header, rows, hrow = rows_with_header(ws, "varname_new")
    if not header:
        add("FAIL", "survey header", "no 'varname_new' column in first rows")
        return {}
    cols = [c for c in TEXT_COLS if c in header]
    leftovers = collections.defaultdict(set)
    malformed, repeated, latin_in_ar = [], [], []
    runtime = collections.Counter()
    for i, r in enumerate(rows, start=hrow + 1):
        q = r.get("varname_new") or f"row{i}"
        for c in cols:
            v = r.get(c)
            if not isinstance(v, str) or not v:
                continue
            for t in PLACEHOLDER.findall(v):
                if "#" in t:  # $ and # delimiters mixed, e.g. "$ADM1#"
                    malformed.append((q, c, t))
                else:
                    leftovers[t].add(f"{q}[{c}]")
            if v.count("$") % 2 == 1:
                malformed.append((q, c, "odd number of $"))
            for t in RUNTIME_VAR.findall(v):
                runtime[t] += 1
            if c not in ("Skip pattern", "Skip Pattern", "Conditional", "varname_new_multiple"):
                for m in REPEATED_WORD.finditer(v):
                    if not m.group(1).isdigit():
                        repeated.append(f"{q}[{c}]: '{m.group(0)}'")
            # Latin words inside Arabic text usually mean a replacement fell
            # back to the English value (e.g. "expected" from $expected or nothing AR$).
            if c in ("Arabic", "Local Language") and re.search(r"[؀-ۿ]", v):
                stripped = re.sub(r"\{[^}]*\}|#[^#\n]*#|\[[A-Z][^\]]*\]", " ", v)
                for w in re.findall(r"(?<![A-Za-z])[A-Za-z]{4,}(?![A-Za-z])", stripped):
                    if w.lower() not in LATIN_OK_IN_ARABIC:
                        latin_in_ar.append(f"{q}[{c}]: '{w}'")
    if leftovers:
        add("FAIL", "Unreplaced $placeholders$",
            "; ".join(f"{t} in {', '.join(sorted(l)[:6])}{' …' if len(l) > 6 else ''}" for t, l in leftovers.items()))
    else:
        add("PASS", "Unreplaced $placeholders$", "none left")
    if malformed:
        add("FAIL", "Malformed placeholders", "; ".join(f"{q}[{c}]: {t}" for q, c, t in malformed[:10]))
    else:
        add("PASS", "Malformed placeholders", "none")
    add("INFO", "Runtime #variables# (filled by GeoPoll at call time, expected)",
        ", ".join(f"{k}×{v}" for k, v in runtime.most_common()))
    if latin_in_ar:
        add("WARN", "Latin words inside Arabic text (replacement fell back to English?)",
            "; ".join(sorted(set(latin_in_ar))[:12]))
    if repeated:
        add("WARN", "Repeated adjacent words (often a placeholder replaced next to the same word)",
            "; ".join(repeated[:12]))

    # Interview length, mirroring the template's LoI sheet categories.
    if "Weighted duration" in header and "Mandatory" in header:
        tot = collections.Counter()
        for r in rows:
            try:
                sec = float(r.get("Weighted duration") or 0)
            except (TypeError, ValueError):
                continue
            m = str(r.get("Mandatory") or "").lower()
            cat = "core" if "yes" in m or m == "spiel" else "recommended" if "recommended" in m \
                else "low priority" if "low priority" in m else "customized/other"
            tot[cat] += sec / 60
        core_rec = tot["core"] + tot["recommended"]
        detail = ", ".join(f"{k}: {v:.1f}" for k, v in tot.items()) + f" | total {sum(tot.values()):.1f} min"
        add("WARN" if core_rec > loi_limit else "PASS",
            f"Interview length (core+recommended <= {loi_limit} min before adding low-priority)",
            f"core+recommended {core_rec:.1f} min; {detail}")

    used_langs = set()
    src_ws = sheet(src_wb, "survey") if src_wb else ws
    if src_ws is not None:
        sh, srows, _ = rows_with_header(src_ws, "varname_new")
        for code, col in LANG_COLS.items():
            if sh and col in sh and sum(1 for r in srows if r.get(col)) > 20:
                used_langs.add(code)
    return {"rows": rows, "header": header, "used_langs": used_langs}


def check_crops(wb, survey):
    ws = sheet(wb, "Crop list")
    if ws is None:
        add("INFO", "Crop list", "no Crop list sheet")
        return
    header, rows, _ = rows_with_header(ws, "Select top")
    if not header:
        add("WARN", "Crop list", "header row not found")
        return
    sel_col = next(h for h in header if h.lower().startswith("select top"))
    m = re.search(r"\d+", sel_col)
    target = int(m.group(0)) if m else 10
    en_col = next((h for h in header if h.lower() in ("label (en)", "label(en)")), None)
    selected = [str(r.get(en_col) or "").strip() for r in rows
                if str(r.get(sel_col) or "").strip().lower() not in ("", "0", "none", "nan")]
    status = "PASS" if len(selected) == target else "FAIL"
    add(status, f"Crop selection (exactly {target})", f"{len(selected)} selected: {', '.join(selected)}")
    if not survey or not selected or not en_col:
        return
    sel_norm = [s.lower() for s in selected]
    checked = 0
    for r in survey["rows"]:
        opts = [o[1].strip().lower() for o in OPTION.findall(str(r.get("English") or ""))]
        if len(opts) < len(selected) or sum(1 for s in sel_norm if s in opts) < 0.8 * len(sel_norm):
            continue
        checked += 1
        q = r.get("varname_new")
        head = opts[: len(selected)]
        if head != sel_norm:
            add("FAIL", f"Crop options sorted (selected first) — {q}",
                f"first {len(selected)} options: {head}; expected {sel_norm}")
        else:
            add("PASS", f"Crop options sorted (selected first) — {q}", f"{len(opts)} options, selected crops first")
    if checked == 0:
        add("WARN", "Crop questions", "no question with the expanded crop list found (crop expansion may have failed)")


def check_additional_info(wb, used_langs):
    ws = sheet(wb, "Additional information")
    if ws is None:
        add("WARN", "Additional information", "sheet missing")
        return
    header, rows, _ = rows_with_header(ws, "Original")
    if not header:
        add("WARN", "Additional information", "header row not found")
        return
    orig = next(h for h in header if h.lower().startswith("original"))
    lead = header[: header.index(orig)]
    repl = {re.sub(r".*\((\w*)\).*", r"\1", h).upper(): h for h in header if h.lower().startswith("replacement")}
    section, blanks, tlu = "", [], []
    for r in rows:
        banner = " ".join(str(r.get(h) or "") for h in lead if h).strip()
        if banner:
            section = banner.upper()
        key = str(r.get(orig) or "").strip()
        if not key:
            continue
        if "TROPICAL LIVESTOCK" in section:
            tlu.append((key, {k: r.get(c) for k, c in repl.items() if k}))
            continue
        if "MANDATORY" not in section:
            continue
        for lang in ["EN"] + sorted(l for l in used_langs if l != "EN"):
            col = repl.get(lang)
            if col and str(r.get(col) or "").strip() == "":
                blanks.append(f"{key} ({lang})")
    if blanks:
        en_blank = [b for b in blanks if b.endswith("(EN)")]
        add("FAIL" if en_blank else "WARN", "Additional information — mandatory keys filled",
            "blank: " + ", ".join(blanks) + ("" if en_blank else " (non-EN blanks fall back to EN text)"))
    else:
        add("PASS", "Additional information — mandatory keys filled", "all filled for " + ", ".join(["EN"] + sorted(used_langs - {"EN"})))
    if tlu:
        bad = []
        for sp, vals in tlu:
            nums = []
            for k, v in vals.items():
                if v in (None, ""):
                    continue
                try:
                    nums.append(float(str(v).replace(",", ".")))
                except ValueError:
                    bad.append(f"{sp}: {k}={v!r} not numeric")
            if not nums:
                bad.append(f"{sp}: blank")
            elif min(nums) <= 0 or len(set(round(n, 6) for n in nums)) > 1:
                bad.append(f"{sp}: {nums}")
        add("FAIL" if bad else "PASS", "TLU weights", "; ".join(bad) if bad else
            ", ".join(f"{sp}={next((v for v in vals.values() if v not in (None, '')), '')}" for sp, vals in tlu))


def check_admin(wb):
    found = {}
    for lvl in (1, 2, 3):
        ws = sheet(wb, f"Admin {lvl} info")
        if ws is None:
            continue
        rows = list(ws.iter_rows(values_only=True))
        hdr = [str(c or "").strip() for c in rows[0]] if rows else []
        found[lvl] = (hdr, [dict(zip(hdr, r)) for r in rows[1:] if any(r)])
    if not found:
        add("FAIL", "Admin lists", "no 'Admin N info' sheets")
        return
    add("PASS" if 1 in found and 2 in found else "FAIL", "Admin lists present",
        ", ".join(f"Admin {k}: {len(v[1])} rows" for k, v in sorted(found.items())))
    if 1 in found and 2 in found:
        p1 = {str(r.get("adm1_pcode")) for r in found[1][1]}
        orphans = sorted({str(r.get("adm1_pcode")) for r in found[2][1]} - p1)
        add("FAIL" if orphans else "PASS", "Admin 2 → Admin 1 parent codes",
            f"admin1 pcodes missing for: {orphans[:10]}" if orphans else "all admin2 parents exist in Admin 1")
        isos = {str(r.get("adm0_ISO3")) for _, rows in [found[1], found[2]] for r in rows if r.get("adm0_ISO3")}
        if len(isos) > 1:
            add("FAIL", "Admin ISO3 consistency", f"several ISO3 values: {sorted(isos)}")
    if 3 in found:
        add("INFO", "Admin 3 info", f"{len(found[3][1])} rows, header {found[3][0][:4]}… — kept as supplied "
            "(the validator refreshes only Admin 1/2 from AGOL)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("validated")
    ap.add_argument("--source", default="")
    ap.add_argument("--loi-limit", type=float, default=30.0)
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.validated, read_only=True, data_only=True)
    src_wb = openpyxl.load_workbook(a.source, read_only=True, data_only=True) if a.source else None

    hidden = [ws.title for ws in wb.worksheets if ws.sheet_state != "visible"]
    if hidden:
        add("WARN", "Hidden sheets", ", ".join(hidden))
    survey = check_survey(wb, src_wb, a.loi_limit)
    check_crops(wb, survey)
    check_additional_info(wb, survey.get("used_langs", set()) if survey else set())
    check_admin(wb)

    icon = {"PASS": "✅", "FAIL": "❌", "WARN": "⚠️", "INFO": "ℹ️"}
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"# Validated output check: {a.validated.replace(chr(92), '/').split('/')[-1]}\n")
    for st, chk, det in results:
        print(f"- {icon.get(st, '')} **{st}** {chk}" + (f" — {det}" if det else ""))
    n = collections.Counter(st for st, _, _ in results)
    print(f"\n{n['FAIL']} fail, {n['WARN']} warn, {n['PASS']} pass")
    return 1 if n["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
