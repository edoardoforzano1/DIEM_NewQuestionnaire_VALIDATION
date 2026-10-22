"""
DIEM Questionnaire Validation — Streamlit UI (Home).

This is an *additive* front end over the existing CLI pipeline
(validate.py, scripts/tool_admin_check.py, scripts/tool_admin_sync.py). It
never imports the validator scripts (CLAUDE.md > Known gotchas: "Validator
scripts are not importable") — every run shells out exactly the way the
.bat launchers do. See CLAUDE.md > Architecture > "Streamlit UI (app/)".

Launch with (inside the diem-validation conda env):
    streamlit_ui
or directly:
    streamlit run app/Home.py
"""
from __future__ import annotations

import sys
from pathlib import Path

# Streamlit puts this script's own directory (app/) on sys.path, not the
# repo root, so `import app...` needs a manual bootstrap here — every page
# module under app/pages/ repeats this same snippet for the same reason.
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import streamlit as st

from app.lib.paths import REPO_ROOT, VALIDATION_CFG_PATH, ADMIN_CFG_PATH

st.set_page_config(page_title="DIEM Questionnaire Validation", page_icon="\U0001f9ed", layout="wide")

st.title("DIEM Questionnaire Validation")
st.caption(
    "A browser front end over the existing validate / tool_admin_check / tool_admin_sync CLI "
    "pipeline — nothing here replaces it. The .bat commands still work exactly as before."
)

st.markdown(
    """
Use the pages in the sidebar:

- **Run Validation** — configure and run the KoBo/GeoPoll validator, with a live log.
- **Results Browser** — browse and preview past reports and validated questionnaires.
- **Admin Tools** — run the admin boundary check/sync tools against AGOL.

Every run started here does exactly what the corresponding `.bat` launcher does — same
scripts, same subprocess boundary, same output folders.
"""
)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Environment")
    st.write(f"Repo root: `{REPO_ROOT}`")
    st.write("validation_config.yaml: " + ("found" if VALIDATION_CFG_PATH.exists() else "**missing**"))
    st.write("admin_tools_config.yaml: " + ("found" if ADMIN_CFG_PATH.exists() else "**missing**"))

with col2:
    st.subheader("Reminder")
    st.info(
        "This UI must run inside the `diem-validation` conda environment, same as every "
        "other command in this repo."
    )
