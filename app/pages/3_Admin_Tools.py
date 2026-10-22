"""
Admin Tools — run tool_admin_check / tool_admin_sync / tool_admin_parent_remap
against AGOL, live.

Never edits the tracked configuration/admin_tools_config.yaml: builds a
throwaway full copy of it (base file + your overrides here) with
app/lib/config_io.write_scratch_admin_config and passes it via the
`--config` flag the admin tools already support (see
scripts/admin_tools_common.py > merge_runtime_config). Each tool script
itself runs completely unmodified, exactly as its .bat launcher does.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import streamlit as st

from app.config_schema import LANGUAGES, SOURCE_MODES, SYNC_MODES, TOOLS
from app.lib import config_io, subprocess_runner
from app.lib.paths import (
    REPO_ROOT,
    STREAMLIT_SCRATCH_DIR,
    TOOL_ADMIN_CHECK_PY,
    TOOL_ADMIN_PARENT_REMAP_PY,
    TOOL_ADMIN_SYNC_PY,
)
from scripts.admin_tools_common import merge_runtime_config, resolve_source_workbook

st.set_page_config(page_title="Admin Tools — DIEM", page_icon="\U0001f5fa", layout="wide")
st.title("Admin Tools")
st.caption(
    "Compares/rebuilds admin1-3 boundary lists against AGOL. Every run hits the network live "
    "— see CLAUDE.md > Known gotchas > \"AGOL fetch is always live\"."
)

runtime_cfg = merge_runtime_config(REPO_ROOT)
run_in_progress = st.session_state.get("admin_run_proc") is not None
if run_in_progress:
    st.warning("A run is already in progress below — new runs are disabled until it finishes.")

st.subheader("Source selection (shared by all three tools below)")
c1, c2, c3 = st.columns(3)
with c1:
    tool = st.selectbox("tool", TOOLS, index=TOOLS.index(runtime_cfg["tool"]) if runtime_cfg["tool"] in TOOLS else 0)
    language = st.selectbox(
        "language",
        LANGUAGES,
        index=LANGUAGES.index(runtime_cfg["language"]) if runtime_cfg["language"] in LANGUAGES else 0,
    )
    iso3 = st.text_input("iso3", value=runtime_cfg["iso3"])
with c2:
    source_mode = st.selectbox(
        "source.mode",
        SOURCE_MODES,
        index=SOURCE_MODES.index(runtime_cfg["source_mode"]) if runtime_cfg["source_mode"] in SOURCE_MODES else 0,
    )
    include_admin3 = st.checkbox("include_admin3", value=bool(runtime_cfg["include_admin3"]))
with c3:
    source_file = ""
    source_custom_dir = ""
    if source_mode == "custom":
        source_custom_dir = st.text_input("source.custom_dir", value=runtime_cfg.get("source_custom_dir") or "")
        names = [p.name for p in config_io.list_xlsx(source_custom_dir)] if source_custom_dir else []
        current = runtime_cfg.get("source_file") or ""
        if current and current not in names:
            names = [current] + names
        source_file = st.selectbox("source.file_name", names or [""])

base_overrides = {
    "tool": tool,
    "language": language,
    "iso3": iso3.strip().upper(),
    "include_admin3": include_admin3,
    "source.mode": source_mode,
    "source.file_name": source_file,
    "source.custom_dir": source_custom_dir,
}

try:
    preview_cfg = dict(runtime_cfg)
    preview_cfg.update(
        tool=tool,
        language=language,
        iso3=iso3.strip().upper(),
        source_mode=source_mode,
        source_file=source_file,
        source_custom_dir=source_custom_dir,
    )
    resolved = resolve_source_workbook(preview_cfg)
    st.info(f"Resolved source workbook: `{resolved}`")
except Exception as exc:
    st.warning(f"Could not resolve a source workbook yet: {exc}")

st.divider()


def _launch(script_path: Path, run_overrides: dict, label: str) -> None:
    scratch_cfg_dir = STREAMLIT_SCRATCH_DIR / "admin_configs"
    cfg_path = config_io.write_scratch_admin_config(run_overrides, scratch_cfg_dir)
    log_dir = STREAMLIT_SCRATCH_DIR / "logs"
    stamp = time.strftime("%Y%m%d_%H%M%S")
    log_path = log_dir / f"{script_path.stem}_{stamp}.log"
    proc = subprocess_runner.start([str(script_path), "--config", str(cfg_path)], cwd=REPO_ROOT, log_path=log_path)
    st.session_state["admin_run_proc"] = proc
    st.session_state["admin_run_log_path"] = log_path
    st.session_state["admin_run_label"] = label
    st.rerun()


tab_check, tab_sync, tab_remap = st.tabs(["tool_admin_check", "tool_admin_sync", "tool_admin_parent_remap"])

with tab_check:
    st.write("Compares the current admin lists in the selected questionnaire against AGOL and exports a mismatch report.")
    if st.button("Run tool_admin_check", disabled=run_in_progress):
        _launch(TOOL_ADMIN_CHECK_PY, base_overrides, "tool_admin_check")

with tab_sync:
    sync_cfg = dict(config_io.read_admin_tools_config().get("sync") or {})
    s1, s2 = st.columns(2)
    with s1:
        sync_mode = st.selectbox(
            "sync.mode",
            SYNC_MODES,
            index=SYNC_MODES.index(sync_cfg.get("mode")) if sync_cfg.get("mode") in SYNC_MODES else 1,
        )
        preserve_sample = st.checkbox(
            "sync.preserve_my_filter_sample", value=bool(sync_cfg.get("preserve_my_filter_sample", True))
        )
    with s2:
        fuzzy_threshold = st.slider(
            "sync.fuzzy_match_threshold (full_from_agol only)",
            min_value=0.0,
            max_value=1.0,
            value=float(sync_cfg.get("fuzzy_match_threshold", 0.85)),
        )
    st.write("Creates a new questionnaire file with admin lists rebuilt from AGOL, using the selected sync mode.")
    if st.button("Run tool_admin_sync", disabled=run_in_progress):
        overrides = dict(base_overrides)
        overrides.update(
            {
                "sync.mode": sync_mode,
                "sync.preserve_my_filter_sample": preserve_sample,
                "sync.fuzzy_match_threshold": fuzzy_threshold,
            }
        )
        _launch(TOOL_ADMIN_SYNC_PY, overrides, "tool_admin_sync")

with tab_remap:
    dry_run = st.checkbox("dry_run (analyse only; do not write the workbook/reports)", value=True)
    st.write("Repairs invalid admin3 parents when old admin2 codes were replaced by merged local codes.")
    if st.button("Run tool_admin_parent_remap", disabled=run_in_progress):
        overrides = dict(base_overrides)
        overrides["dry_run"] = dry_run
        _launch(TOOL_ADMIN_PARENT_REMAP_PY, overrides, "tool_admin_parent_remap")


@st.fragment(run_every=2)
def _tail_admin_run() -> None:
    proc = st.session_state.get("admin_run_proc")
    log_path = st.session_state.get("admin_run_log_path")
    label = st.session_state.get("admin_run_label")
    if proc is None or log_path is None:
        return

    st.subheader(f"Live output — {label}")
    st.code(subprocess_runner.read_log(log_path) or "(waiting for output...)", language="text")

    rc = subprocess_runner.poll(proc)
    if rc is None:
        if st.button("Stop run", key="stop_admin_run"):
            proc.terminate()
    else:
        subprocess_runner.finish(proc)
        st.session_state["admin_run_proc"] = None
        if rc == 0:
            st.success(f"{label} finished (exit code 0). Output written under admin_tools_output/.")
        else:
            st.error(f"{label} exited with code {rc}. See the log above.")


if st.session_state.get("admin_run_proc") is not None:
    _tail_admin_run()
