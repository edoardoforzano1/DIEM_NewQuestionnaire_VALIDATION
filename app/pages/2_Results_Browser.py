"""
Results Browser — browse past reports and validated questionnaires without
leaving the browser. Read-only: nothing on this page writes anything.

Output layout mirrors CLAUDE.md > Output naming:
  report_{tool}_{lang}_{ISO3}_{timestamp}.xlsx
  validated_questionnaire_{tool}_{lang}_{ISO3}_{timestamp}.xlsx
under output_dir/kobo_output/ or output_dir/geopoll_output/.
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import polars as pl
import streamlit as st

from app.config_schema import REPORT_GLOB, TOOLS, VALIDATED_GLOB
from app.lib import config_io, report_preview

st.set_page_config(page_title="Results Browser — DIEM", page_icon="\U0001f4c2", layout="wide")
st.title("Results Browser")

cfg = config_io.read_validation_config()
output_base = st.text_input("Output base dir", value=str(cfg.get("output_dir") or ""))
tool = st.selectbox("Tool", TOOLS, index=TOOLS.index(cfg.get("tool")) if cfg.get("tool") in TOOLS else 0)

out_dir = Path(output_base) / f"{tool}_output"
if not out_dir.exists():
    st.warning(f"Folder not found: {out_dir}")
    st.stop()


def _glob(pattern_tpl: str) -> list[Path]:
    pattern = pattern_tpl.format(tool=tool)
    return sorted(out_dir.glob(pattern), key=lambda p: p.stat().st_mtime, reverse=True)


tab_reports, tab_validated = st.tabs(["Reports", "Validated questionnaires"])

with tab_reports:
    reports = _glob(REPORT_GLOB)
    if not reports:
        st.info(f"No report files found in {out_dir}")
    else:
        chosen = st.selectbox("Report file", reports, format_func=lambda p: p.name, key="report_pick")
        st.download_button(
            "Download this report",
            data=chosen.read_bytes(),
            file_name=chosen.name,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        sheets = report_preview.list_sheets(chosen)
        default_sheet = "Summary" if "Summary" in sheets else (sheets[0] if sheets else "")
        sheet = st.selectbox("Sheet", sheets, index=sheets.index(default_sheet) if default_sheet in sheets else 0)
        if sheet == "Summary":
            # The Summary sheet is a sequence of colored PASS/FAIL/WARN
            # section blocks, not a flat table — render it as it actually
            # looks in Excel (merged section titles, fills, bold) instead
            # of flattening it into a generic dataframe.
            summary_html = report_preview.render_summary_html(chosen, sheet)
            if summary_html:
                st.markdown(summary_html, unsafe_allow_html=True)
            else:
                st.info("Summary sheet is empty.")
        elif sheet:
            df = report_preview.read_sheet_as_table(chosen, sheet)
            if "severity" in df.columns:
                severities = sorted(v for v in df["severity"].unique().to_list() if v)
                picked = st.multiselect("Filter by severity", severities, default=severities)
                if picked:
                    df = df.filter(pl.col("severity").is_in(picked))
            st.dataframe(df, use_container_width=True)
            st.caption(f"{df.height} row(s)")

with tab_validated:
    validated = _glob(VALIDATED_GLOB)
    if not validated:
        st.info(f"No validated questionnaire files found in {out_dir}")
    else:
        chosen_v = st.selectbox("Validated questionnaire file", validated, format_func=lambda p: p.name, key="validated_pick")
        st.download_button(
            "Download this file",
            data=chosen_v.read_bytes(),
            file_name=chosen_v.name,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            key="dl_validated",
        )
        st.write("Sheets:", ", ".join(report_preview.list_sheets(chosen_v)))
