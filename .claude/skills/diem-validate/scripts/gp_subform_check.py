"""Check a GeoPoll Submission Form ("Subform" sheet) against the DIEM GeoPoll
template and the validated KoBo questionnaire of the same country/round.

usage: gp_subform_check.py SUBFORM.xlsx KOBO_FINAL.xlsx GP_TEMPLATE.xlsx OUT.xlsx
Writes an Excel report (sheet "Issues": Issue type, Q Name, Row, Severity,
Field, Detail) readable by validation_case.py, and prints counts.
"""
import sys, re, difflib, unicodedata, collections
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

SUB, KF, GT, OUT = sys.argv[1:5]
OPT = re.compile(r"^\s*(\d+)\s*\)\s*(.*?)\s*$")
RUNTIME = {"#CATI_MOBILENUMBER#", "#OPERATOR#", "#resp_name#", "#resp_gender#", "#resp_age#",
           "#ADM1#", "#ADM2#", "#hh_agricactivity#", "#ls_main_tie_detector#"}
DKR = {"dontknow", "refused", "nesaitpas", "refus"}


def split_opts(t):
    if not isinstance(t, str):
        return "", []
    q, o = [], []
    for l in t.split("\n"):
        m = OPT.match(l)
        if m:
            o.append((int(m.group(1)), m.group(2)))
        elif not o:
            q.append(l)
    return "\n".join(q).strip(), o


def k(x):
    x = str(x).replace("’", "'").replace("–", "-").replace("\xa0", " ")
    x = unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "", x)


def words(x):
    x = str(x).replace("’", "'").replace("\xa0", " ")
    x = unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", x).strip()


# ---------- load
wb = openpyxl.load_workbook(SUB, read_only=True)
R = list(wb["Subform"].iter_rows(values_only=True))
sub = []
for i, r in enumerate(R[3:], start=4):
    if not r or not r[1]:
        continue
    qen, oen = split_opts(r[3]); qfr, ofr = split_opts(r[5])
    sub.append(dict(row=i, name=str(r[1]).strip(), en=r[3], fr=r[5], qen=qen, qfr=qfr, oen=oen, ofr=ofr,
                    type=r[7], cond=r[8], prog=r[9], skip=r[12], comment=r[13]))
S = {s["name"]: s for s in sub}
idx = {s["name"]: n for n, s in enumerate(sub)}

kw = openpyxl.load_workbook(KF, read_only=True)
ks = list(kw["survey"].iter_rows(values_only=True)); kh = list(ks[0])
K = {r[kh.index("name")]: dict(zip(kh, r)) for r in ks[1:] if r and r[kh.index("name")]}
kc = list(kw["choices"].iter_rows(values_only=True)); kch = list(kc[0])
KC = collections.defaultdict(list)
for r in kc[1:]:
    if r and r[0]:
        KC[str(r[0])].append(dict(zip(kch, r)))
KAI = {}
if "Additional information" in kw.sheetnames:
    for r in kw["Additional information"].iter_rows(values_only=True):
        if r and len(r) > 3 and isinstance(r[2], str):
            KAI[r[2].strip().upper()] = r[3]

gw = openpyxl.load_workbook(GT, read_only=True)
gs = list(gw["survey"].iter_rows(values_only=True)); gh = list(gs[0])
G = {r[gh.index("varname_new")]: dict(zip(gh, r)) for r in gs[1:] if r and r[gh.index("varname_new")]}

issues = []


def add(itype, s, sev, field, detail):
    issues.append({"Issue type": itype, "Q Name": s["name"] if isinstance(s, dict) else s,
                   "Row": s["row"] if isinstance(s, dict) else "", "Severity": sev,
                   "Field": field, "Detail": detail})


# ---------- 1. French still in English
ENW = re.compile(r"\b(the|and|but|not|now|time|week|continue|next|someone|answer)\b", re.I)
for s in sub:
    if s["name"].startswith("hh_admin") or s["name"] in ("Optin", "calldispo", "NoAnswer", "NonWorkingNumber",
                                                           "End poll callback", "CallBack_Introduction", "CallBack_Confirmation"):
        continue
    for (c, e), (_, f) in zip(s["oen"], s["ofr"]):
        if k(e) == k(f) and ENW.search(e):
            add("fr_label_in_english", s, "medium", f"fr_French option {c}", f"'{f}'")

# ---------- 2. placeholders left
for s in sub:
    for col, t in (("English", s["en"]), ("fr_French", s["fr"])):
        for tok in re.findall(r"#[^#\s][^#\n]*#|\$[^$\n]+\$", str(t or "")):
            if tok not in RUNTIME and tok.strip("#") not in S:
                add("unresolved_placeholder", s, "high", col, tok)

# ---------- 3. EN/FR option count
for s in sub:
    if len(s["oen"]) != len(s["ofr"]):
        add("en_fr_options_differ", s, "high", "English / fr_French",
            f"{len(s['oen'])} English options, {len(s['ofr'])} French options")
    else:
        dup = [l for l, n in collections.Counter(k(l) for _, l in s["ofr"]).items() if n > 1]
        if dup and not s["name"].startswith("hh_admin"):
            add("duplicate_option", s, "high", "fr_French", f"repeated: {dup}")

# ---------- 4. skip patterns
LINE = re.compile(r"^\s*(.+?)\s*=\s*(.+?)\s*$")


def parse_skip(s):
    out = []
    for line in str(s["skip"] or "").split("\n"):
        line = line.strip()
        if not line or line == "NA":
            continue
        if line.lower().startswith("end poll"):
            out.append(("END", line)); continue
        m = LINE.match(line)
        if not m:
            out.append(("??", line)); continue
        lhs, tgt = m.group(1), re.sub(r"\s*\[[^\]]*\]\s*$", "", m.group(2)).strip()
        codes, tag = set(), None
        for part in re.split(r"\s*,\s*", lhs):
            r = re.match(r"^(-?\d+)\s*-\s*(-?\d+)$", part)
            if r:
                a, b = int(r.group(1)), int(r.group(2))
                if b - a < 1000:
                    codes |= set(range(a, b + 1))
                else:
                    tag = "range"
            elif re.match(r"^-?\d+$", part):
                codes.add(int(part))
            else:
                tag = part
        out.append((tag or codes, tgt))
    return out


edges = collections.defaultdict(set)
for n, s in enumerate(sub):
    sk = parse_skip(s); covered = set(); tagged = False
    for c, t in sk:
        if c == "END" or t.lower().startswith("end poll"):
            if isinstance(c, set):
                covered |= c
            continue
        if c == "??":
            add("skip_unreadable", s, "medium", "Skip Pattern", t); continue
        if isinstance(c, str):
            tagged = True
        if t not in idx:
            alt = [x for x in idx if x.lower() == t.lower()]
            add("skip_target_missing", s, "high" if not alt else "low", "Skip Pattern",
                f"'{t}'" + (f" (written with different case: {alt[0]})" if alt else ""))
            if alt:
                edges[s["name"]].add(alt[0])
            if isinstance(c, set):
                covered |= c
            continue
        edges[s["name"]].add(t)
        if isinstance(c, set):
            covered |= c
    if s["oen"] and sk and s["type"] in ("Single Choice", "Select All That Apply", "StartRecording") and not tagged:
        codes = {c for c, _ in s["oen"]}
        if codes - covered:
            add("codes_not_routed", s, "high", "Skip Pattern",
                f"codes {sorted(codes - covered)} ({', '.join(l for c, l in s['oen'] if c in codes - covered)}) have no route")
        if covered - codes:
            add("routes_missing_codes", s, "medium", "Skip Pattern", f"routes codes {sorted(covered - codes)} that are not options")
    # programming instructions referring to codes that do not exist
    if s["oen"]:
        nmax = max(c for c, _ in s["oen"])
        for line in str(s["prog"] or "").split("\n"):
            m = re.match(r"^\s*([\d,\s]+)\s*=\s*Is(Anchored|None)", line)
            if m:
                bad = [int(x) for x in re.findall(r"\d+", m.group(1)) if int(x) > nmax]
                if bad:
                    add("prog_missing_codes", s, "medium", "Programming Instructions",
                        f"'{line.strip()}' refers to code(s) {bad}; the question has {nmax} options")

# ---------- 5. conditionals
CL = re.compile(r'"([^"]+)"\s+"(Equals|Contains|Not Equals|Does Not Contain)"\s+"([^"]*)"', re.I)
FT = re.compile(r'if not satisfied go to\s+"([^"]+)"', re.I)
for s in sub:
    c = str(s["cond"] or "")
    for m in FT.finditer(c):
        t = m.group(1)
        if t in idx:
            edges[s["name"]].add(t)
        else:
            add("cond_target_missing", s, "high", "Conditional", t)
    bad = collections.defaultdict(set)
    for q, op, val in CL.findall(c):
        if q not in S or re.match(r"^-?\d+(\.\d+)?(\s*-\s*\d+(\.\d+)?)?$", val.strip()):
            continue
        if "Include selected" in str(S[q]["prog"]):
            continue  # dynamic list
        labels = [words(l) for _, l in S[q]["oen"]]
        ok = words(val) in labels if op.lower() in ("equals", "not equals") else any(words(val) in l for l in labels)
        if not ok:
            bad[q].add(val)
    for q, vals in bad.items():
        add("cond_label_not_an_option", s, "high", "Conditional",
            f"refers to {q} = " + " | ".join(v[:70] + "…" for v in vals) + " — no option of " + q + " has this text")

# reachability
start = sub[0]["name"]; seen = {start}; stack = [start]
while stack:
    x = stack.pop()
    for y in edges.get(x, ()):
        if y not in seen:
            seen.add(y); stack.append(y)
for s in sub:
    if s["name"] not in seen and not s["name"].lower().startswith(("callback", "end poll")) and s["type"]:
        add("question_never_reached", s, "medium", "Skip Pattern / Conditional",
            "no skip pattern or condition leads to this question" + (f"; GeoPoll comment: {str(s['comment'])[:120]}" if s["comment"] else ""))
for s in sub:
    if re.search(r"question removed", str(s["comment"] or ""), re.I):
        add("removed_question_still_in_form", s, "medium", "row", str(s["comment"])[:150])

# ---------- 6. piping
for s in sub:
    for t in (s["en"], s["fr"]):
        for x in set(re.findall(r"\{([^}]+)\}", str(t or ""))):
            if x not in S and not x.startswith("ADM") and not any(d["Issue type"] == "piped_value_not_a_question" and d["Q Name"] == s["name"] for d in issues):
                add("piped_value_not_a_question", s, "high", "English / fr_French", "{" + x + "} is used in the text but no question or calculation is called " + x)

# ---------- 7. text vs template (LCSI wording) and typos
def lcsi_norm(t):
    t = re.sub(r"\[[^\]]*(OPERAT|OPÉRAT)[^\]]*\]", "", str(t or ""), flags=re.I)
    t = words(t)
    t = re.sub(r"\b(you or|vous ou)\b", "", t)
    t = re.sub(r"\b(a lack of|un manque de|d un manque de)\b", "lack of", t)
    t = re.sub(r"\bto buy food\b|\bpour acheter de la nourriture\b", "", t)
    return re.sub(r"\s+", " ", t).strip()


for s in sub:
    if not s["name"].startswith("cs_") or s["name"] not in G:
        continue
    for col, a, b in (("English", G[s["name"]]["English"], s["qen"]), ("fr_French", G[s["name"]]["French"], s["qfr"])):
        ga, sb = lcsi_norm(split_opts(a)[0]), lcsi_norm(b)
        r = difflib.SequenceMatcher(None, ga, sb).ratio()
        if r < 0.7:
            add("lcsi_text_differs_from_template", s, "high", col, f"now: '{split_opts(b)[0][:160]}' | template: '{split_opts(a)[0][:160]}'")

LCSI_END = {"en": "lack of food or money", "fr": "manque de nourriture ou d argent"}
for s in sub:
    if not s["name"].startswith("cs_") or s["name"] not in K:
        continue
    for col, lang, txt, kl in (("English", "en", s["qen"], "label::English (en)"), ("fr_French", "fr", s["qfr"], "label::French (fr)")):
        t = words(txt)
        if LCSI_END[lang] not in t:
            add("lcsi_reason_missing", s, "high", col, f"the reason 'because of lack of food or money' is missing: '{txt.splitlines()[0][:160]}'")

cs_items = [x for x in sub if x["name"].startswith("cs_")]
for col, key in (("English", "qen"), ("fr_French", "qfr")):
    for i, a in enumerate(cs_items):
        for b in cs_items[i + 1:]:
            if words(a[key]) and words(a[key]) == words(b[key]):
                add("lcsi_same_text_as_other_item", b, "high", col, f"same text as {a['name']} (row {a['row']}): '{b[key].splitlines()[0][:150]}'")

OPTLINE = re.compile(r"^\s*\d+\s*\)")
for s in sub:
    if s["name"].startswith("hh_admin"):
        continue
    for col, t in (("English", s["en"]), ("fr_French", s["fr"])):
        if not isinstance(t, str):
            continue
        for line in t.split("\n"):
            body = OPTLINE.sub("", line, count=1)
            if body.count("[") != body.count("]") or body.count("(") != body.count(")"):
                add("typo_brackets", s, "low", col, line.strip()[:140])
        if re.search(r"\bvous ou vous\b", t):
            add("typo_repeated_words", s, "low", col, "'vous ou vous ou'")
        if "anyonein" in t:
            add("typo_word", s, "low", col, "'anyonein'")
        if ".." in t.replace("...", ""):
            add("typo_punctuation", s, "low", col, "'..'")
        if t.count("[OPÉRATEUR") + t.count("[OPERATOR") > 1:
            add("typo_repeated_instruction", s, "low", col, "operator instruction written twice")

# ---------- 8. admin
def routes(s):
    out = {}
    for line in str(s["skip"] or "").split("\n"):
        m = re.match(r"^\s*(\d+)(?:\s*-\s*(\d+))?\s*=\s*(\S+)", line)
        if m:
            for c in range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1):
                out[c] = m.group(3)
    return out


gp = collections.defaultdict(list)


def walk(q, lvl, parent):
    s = S.get(q)
    if not s:
        return
    r = routes(s); fr = dict(s["ofr"])
    for c, en in s["oen"]:
        if k(en) in DKR:
            t = r.get(c, "")
            if lvl == 4 and t.startswith("hh_admin4_") and t != q:
                walk(t, lvl, parent)  # list split in two questions (_a / _b)
                break
            continue
        f = fr.get(c) or en
        gp[lvl].append(parent + (k(f),))
        if k(en) != k(f) and lvl <= 2:
            add("admin_english_name_differs", s, "medium", f"English option {c}", f"English '{en}' vs French '{f}'")
        if re.search(r"[A-Z] [A-Z]$", en.strip()) and lvl <= 2:
            add("admin_english_name_differs", s, "medium", f"English option {c}", f"'{en}' (space inside the name)")
        if lvl < 4 and r.get(c, "").startswith(f"hh_admin{lvl + 1}_"):
            walk(r[c], lvl + 1, parent + (k(f),))


walk("hh_admin1", 1, ())
lab, par = {}, {}
for lvl in (1, 2, 3, 4):
    for d in KC.get(f"admin{lvl}", []):
        lab[(lvl, str(d["name"]))] = d.get("label::French (fr)") or d.get("label::English (en)")
        par[(lvl, str(d["name"]))] = str(d.get("my_filter_admin") or "")


def kpath(lvl, code):
    p = []
    while lvl >= 1:
        p.append(k(lab[(lvl, code)])); code = par[(lvl, code)]; lvl -= 1
    return tuple(reversed(p))


admin_summary = []
for lvl in (1, 2, 3, 4):
    a = collections.Counter(kpath(lvl, c) for (l, c) in lab if l == lvl); b = collections.Counter(gp[lvl])
    diff = (a - b) + (b - a)
    admin_summary.append((lvl, sum(a.values()), sum(b.values()), sum(diff.values())))
    if diff:
        add("admin_tree_differs", f"hh_admin{lvl}", "high", "options", f"{sum(diff.values())} unit(s) differ from the validated KoBo lists")

# ---------- 9. crops
ca = S.get("crp_all")
if ca:
    if re.search(r"\bRandomize\b", str(ca["prog"])):
        add("crop_list_randomized", ca, "high", "Programming Instructions",
            "Randomize shuffles the 90 crops, so the 10 most common crops are no longer shown first")
    kc_en = [k(d.get("label::English (en)")) for d in KC.get("crop", [])][:10]
    if [k(l) for _, l in ca["oen"][:10]] != kc_en:
        add("crop_top10_differs", ca, "high", "options", "first 10 crops differ from the validated KoBo crop list")
cs = S.get("crp_salesmain")
if cs:
    if re.search(r"Exclude selected", str(cs["prog"])):
        add("crop_sold_excludes_main_crop", cs, "high", "Programming Instructions",
            "'Exclude selected crp_main': the household cannot name its main crop as the main crop sold (the question 'was the main crop also the main crop sold' was removed)")
    if any(k(l) == "nootheropcrop" or k(l) == "nootherrop" or k(l) == "noothercrop" for _, l in cs["oen"]):
        add("crop_sold_extra_option", cs, "medium", "options", "'No other crop' is not an answer to 'main crop sold'")

# ---------- 10. ranges vs KoBo / Additional information
mx = KAI.get("MAX AMOUNT")
for q in ("income_main_amount", "income_sec_amount", "income_third_amount"):
    s = S.get(q)
    if not s or not mx:
        continue
    hi = max([int(b) for a, b in re.findall(r"(\d+)\s*-\s*(\d+)\s*=", str(s["skip"]))] or [0])
    if hi and hi < int(mx):
        add("range_below_country_max", s, "medium", "Skip Pattern",
            f"highest accepted amount {hi:,}; the country's MAX AMOUNT is {int(mx):,}")

# ---------- write
wbo = openpyxl.Workbook(); ws = wbo.active; ws.title = "Issues"
cols = ["Issue type", "Q Name", "Row", "Severity", "Field", "Detail"]
ws.append(cols)
for c in ws[1]:
    c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="1F4E79")
order = {"high": 0, "medium": 1, "low": 2}
for d in sorted(issues, key=lambda d: (order.get(d["Severity"], 3), d["Row"] if isinstance(d["Row"], int) else 0)):
    ws.append([d[c] for c in cols])
for i, w in enumerate([30, 26, 7, 9, 26, 110], start=1):
    ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = w
ws.freeze_panes = "A2"; ws.auto_filter.ref = ws.dimensions
sm = wbo.create_sheet("Checked")
sm.append(["Check", "Result"])
sm.append(["Questions in the form", len(sub)])
for lvl, a, b, d in admin_summary:
    sm.append([f"Admin {lvl}: validated KoBo / GeoPoll / differing", f"{a} / {b} / {d}"])
sm.append(["Crops in crp_all", len(ca["oen"]) if ca else 0])
wbo.save(OUT)
c = collections.Counter(d["Severity"] for d in issues)
print(dict(c)); print(collections.Counter(d["Issue type"] for d in issues))
