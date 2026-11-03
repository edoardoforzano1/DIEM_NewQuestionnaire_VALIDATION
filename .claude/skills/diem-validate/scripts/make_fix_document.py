"""
Build the Word document for the country team from a JSON spec, in the house
style (Arial 10, blue headings, Consolas for variable names / formulas,
grey code blocks, shaded table headers).

Usage:
    python make_fix_document.py spec.json out.docx

Needs python-docx (pip install python-docx in any env).

spec.json:
{
  "title": "Niger R12 KoBo questionnaire – points to review before validation",
  "meta": [["File reviewed", "`DIEM_Niger_R12_….xlsx`"], ["Compared with", "`diem_household_…_20261022_ISO3.xlsx` (latest template)"]],
  "intro": ["Row numbers refer to …"],
  "blocks": [
    {"h1": "Livestock"},
    {"h2": "2. Main livestock – variable names", "tag": "To fix"},
    {"p": "Where: **rows 310, 308**, `name` column."},
    {"bullet": "`lsmain` (row 310) → `ls_main`"},
    {"bullet2": "second-level bullet"},
    {"action": "Please copy the `relevant` cells from the template (rows 274–276) into your file (rows 216–218)."},
    {"code": "${ls_num_now_cattle} * 0.5"},
    {"table": {"header": ["Question", "Your row", "Template row"], "rows": [["`ls_feed_type`", "317", "390"]], "widths": [4, 2, 3]}},
    {"summary": [["1", "Livestock", "To fix", "TLU formulas", "272–279"]]}
  ]
}

Inline markup in every string: **bold**, `code` (variable names, list names,
formulas, column names, file names).
"""
import json
import re
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

MONO = "Consolas"
BLUE = RGBColor(0x1F, 0x4E, 0x78)
TAG_FILL = {"To fix": "F8D7DA", "To confirm": "FFF2CC", "Placeholder": "DCE6F1", "Template side": "E2EFDA", "Optional": "EDEDED"}


def _setup(doc):
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2.2)
    sec.top_margin = sec.bottom_margin = Cm(2)
    st = doc.styles["Normal"]
    st.font.name = "Arial"
    st.font.size = Pt(10)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    st.paragraph_format.space_after = Pt(4)
    for name, size in (("Title", 18), ("Heading 1", 14), ("Heading 2", 11.5)):
        s = doc.styles[name]
        s.font.name = "Arial"
        s.font.size = Pt(size)
        s.font.bold = True
        s.font.color.rgb = BLUE
        s.paragraph_format.space_before = Pt(12 if name != "Title" else 0)
        s.paragraph_format.space_after = Pt(4)
        s.paragraph_format.keep_with_next = True


def _runs(p, text, size=9):
    """Add text to paragraph p, honouring **bold** and `code` markup."""
    for piece in re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text):
        if not piece:
            continue
        if piece.startswith("**"):
            p.add_run(piece[2:-2]).bold = True
        elif piece.startswith("`"):
            r = p.add_run(piece[1:-1])
            r.font.name = MONO
            r.font.size = Pt(size)
            r._element.rPr.rFonts.set(qn("w:eastAsia"), MONO)
        else:
            p.add_run(piece)


def _shade(target, fill, cell=True):
    pr = target._tc.get_or_add_tcPr() if cell else target._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    pr.append(shd)


def _table(doc, header, rows, widths):
    t = doc.add_table(rows=1, cols=len(header))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(header):
        c = t.rows[0].cells[i]
        c.text = ""
        c.paragraphs[0].add_run(h).bold = True
        _shade(c, "DCE6F1")
    for row in rows:
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = ""
            _runs(cells[i].paragraphs[0], str(v))
            if str(v) in TAG_FILL:
                _shade(cells[i], TAG_FILL[str(v)])
    for row in t.rows:
        for i, w in enumerate(widths):
            row.cells[i].width = Cm(w)
    doc.add_paragraph()


def build(spec, out):
    doc = Document()
    _setup(doc)
    doc.add_paragraph(spec["title"], style="Title")
    for label, value in spec.get("meta", []):
        _runs(doc.add_paragraph(), f"**{label}:** {value}")
    for line in spec.get("intro", []):
        _runs(doc.add_paragraph(), line)
    for b in spec["blocks"]:
        if "h1" in b:
            doc.add_paragraph(b["h1"], style="Heading 1")
        elif "h2" in b:
            p = doc.add_paragraph(style="Heading 2")
            p.add_run(b["h2"])
            if b.get("tag"):
                r = p.add_run(f"   [{b['tag']}]")
                r.font.size = Pt(9)
                r.font.color.rgb = RGBColor(0x59, 0x59, 0x59)
        elif "p" in b:
            _runs(doc.add_paragraph(), b["p"])
        elif "bullet" in b:
            _runs(doc.add_paragraph(style="List Bullet"), b["bullet"])
        elif "bullet2" in b:
            _runs(doc.add_paragraph(style="List Bullet 2"), b["bullet2"])
        elif "action" in b:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.6)
            p.add_run("→ ").bold = True
            _runs(p, b["action"])
        elif "code" in b:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.6)
            r = p.add_run(b["code"])
            r.font.name = MONO
            r.font.size = Pt(8)
            r._element.rPr.rFonts.set(qn("w:eastAsia"), MONO)
            _shade(p, "F2F2F2", cell=False)
        elif "table" in b:
            t = b["table"]
            _table(doc, t["header"], t["rows"], t["widths"])
        elif "summary" in b:
            _table(doc, ["#", "Section", "Type", "Point", "Rows"], b["summary"], [0.8, 3.2, 2.4, 7.0, 3.2])
        else:
            raise ValueError(f"unknown block: {b}")
    doc.save(out)
    print("saved", out)


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        build(json.load(f), sys.argv[2])
