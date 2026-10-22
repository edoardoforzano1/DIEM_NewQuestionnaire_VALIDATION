"""
Read-only Excel preview helpers for the Results Browser / Admin Tools pages.

Uses openpyxl (already a core dependency) in read_only mode and returns
polars DataFrames, matching this repo's stated Polars convention
(CLAUDE.md > Code conventions > Polars). Deliberately generic — it does not
hardcode issue-sheet column names, since those are self-describing in the
workbook's own header row; only the sheet-name/qualifying-column contract in
app/config_schema.py is treated as something that needs to be kept in sync.
"""
from __future__ import annotations

import html
from pathlib import Path

import openpyxl
import polars as pl


def list_sheets(xlsx_path: Path) -> list[str]:
    wb = openpyxl.load_workbook(xlsx_path, read_only=True)
    try:
        # Only user-visible sheets — see CLAUDE.md > Known gotchas > "Hidden Excel sheets".
        return [ws.title for ws in wb.worksheets if ws.sheet_state == "visible"]
    finally:
        wb.close()


def read_sheet_as_table(
    xlsx_path: Path,
    sheet_name: str,
    header_hint: str = "severity",
    max_scan_rows: int = 10,
    max_rows: int = 2000,
) -> pl.DataFrame:
    """Read a sheet into a DataFrame, auto-detecting the header row.

    Some report sheets have a title/banner row above the real column
    headers (see CLAUDE.md > GeoPoll conventions > "Template header row
    auto-detection" for the analogous case on the input side) — this scans
    the first few rows for one containing `header_hint` and treats that as
    the header row. Falls back to row 1 if no such row is found.
    """
    wb = openpyxl.load_workbook(xlsx_path, data_only=True, read_only=True)
    try:
        if sheet_name not in wb.sheetnames:
            return pl.DataFrame()
        ws = wb[sheet_name]
        rows = list(ws.iter_rows(values_only=True))
    finally:
        wb.close()

    if not rows:
        return pl.DataFrame()

    header_idx = 0
    hint = header_hint.strip().lower()
    for i, row in enumerate(rows[:max_scan_rows]):
        cells = [str(c).strip().lower() if c is not None else "" for c in row]
        if hint in cells:
            header_idx = i
            break

    raw_header = rows[header_idx]
    seen: dict[str, int] = {}
    header: list[str] = []
    for j, c in enumerate(raw_header):
        name = str(c).strip() if c is not None else ""
        if not name:
            name = f"col_{j}"
        if name in seen:
            seen[name] += 1
            name = f"{name}_{seen[name]}"
        else:
            seen[name] = 0
        header.append(name)

    n = len(header)
    data_rows = [r for r in rows[header_idx + 1 :] if any(c is not None for c in r)][:max_rows]
    records = [dict(zip(header, (list(r[:n]) + [None] * (n - len(r))))) for r in data_rows]
    if not records:
        return pl.DataFrame(schema={h: pl.Utf8 for h in header})
    return pl.DataFrame(records, strict=False)


def _rgb_hex(color) -> str | None:
    """Best-effort #RRGGBB for an openpyxl Color object (fgColor or font
    color), or None for "unset"/theme/indexed colors this report generator
    doesn't use (see render_summary_html)."""
    if color is None or getattr(color, "type", None) != "rgb":
        return None
    rgb = color.rgb
    if not isinstance(rgb, str) or len(rgb) != 8:
        return None
    return f"#{rgb[2:]}"  # drop the leading ARGB alpha byte


def _fill_hex(fill) -> str | None:
    if fill is None or fill.patternType is None:
        return None
    return _rgb_hex(fill.fgColor)


def render_summary_html(xlsx_path: Path, sheet_name: str = "Summary") -> str:
    """Render a sheet as an HTML table that mirrors its actual Excel layout
    (merged title/section rows, PASS/FAIL/WARN/info fills, bold headers)
    instead of flattening it into a generic dataframe. Built for the
    Summary sheet specifically — see docs/report-output/ for the section
    layout this reproduces (title block, then one title-row + header-row +
    colored-status-rows block per section). Reads each cell's explicit fill
    and font color rather than assuming a color scheme, so it stays correct
    if the report writer's palette changes.

    Not read_only (need real style objects, not the read-only cell view),
    but these sheets are small (well under 100 rows) so this is cheap.
    """
    wb = openpyxl.load_workbook(xlsx_path, data_only=True)
    try:
        if sheet_name not in wb.sheetnames:
            return ""
        ws = wb[sheet_name]

        merges = list(ws.merged_cells.ranges)
        span_at: dict[tuple[int, int], tuple[int, int]] = {}  # (row,col) -> (rowspan,colspan)
        covered: set[tuple[int, int]] = set()
        for rng in merges:
            span_at[(rng.min_row, rng.min_col)] = (rng.max_row - rng.min_row + 1, rng.max_col - rng.min_col + 1)
            for r in range(rng.min_row, rng.max_row + 1):
                for c in range(rng.min_col, rng.max_col + 1):
                    if (r, c) != (rng.min_row, rng.min_col):
                        covered.add((r, c))

        rows_html: list[str] = []
        for row in ws.iter_rows(min_row=1, max_row=ws.max_row, max_col=ws.max_column):
            cells_html: list[str] = []
            for cell in row:
                pos = (cell.row, cell.column)
                if pos in covered:
                    continue
                rowspan, colspan = span_at.get(pos, (1, 1))
                text = "" if cell.value is None else html.escape(str(cell.value))
                text = text.replace("\n", "<br>")
                styles = ["padding:4px 8px", "border:1px solid #ddd", "vertical-align:top"]
                bg = _fill_hex(cell.fill)
                if bg:
                    styles.append(f"background:{bg}")
                # The report writer sets explicit font colors for contrast
                # against colored fills (e.g. white text on the dark-green
                # section-header rows) — use them; #111 is just the default
                # for cells that don't set one (matches how Excel renders
                # "automatic" black text on this sheet's pale status fills).
                fg = _rgb_hex(cell.font.color) if cell.font else None
                styles.append(f"color:{fg or '#111'}")
                if cell.font and cell.font.bold:
                    styles.append("font-weight:600")
                span_attrs = ""
                if rowspan > 1:
                    span_attrs += f' rowspan="{rowspan}"'
                if colspan > 1:
                    span_attrs += f' colspan="{colspan}"'
                cells_html.append(f'<td style="{";".join(styles)}"{span_attrs}>{text}</td>')
            if cells_html:
                rows_html.append(f"<tr>{''.join(cells_html)}</tr>")
    finally:
        wb.close()

    table_style = "border-collapse:collapse;width:100%;font-size:0.85rem;color:#111"
    wrapper_style = "background:#fff;color:#111;padding:12px;border-radius:6px;border:1px solid #ddd;overflow-x:auto"
    return f'<div style="{wrapper_style}"><table style="{table_style}">{"".join(rows_html)}</table></div>'
