"""
Run Validation — configure and launch validate.py (kobo/geopoll), live.

Design notes (see also app/lib/config_io.py docstring):
  - The form never writes anything until you click "Confirm & write config +
    run" — clicking "Prepare run" only computes and shows a diff.
  - Only the whitelisted keys in app/lib/config_io.WRITABLE_KEYS are ever
    changed in the tracked configuration/validation_config.yaml, via a
    comment-preserving round-trip (ruamel.yaml) — every other line in that
    file, including all its documentation comments, is left untouched.
  - A timestamped backup of validation_config.yaml is written to
    configuration/.streamlit_backups/ before every save.
  - validate.py itself is run completely unmodified, exactly as `validate`
    (the .bat launcher) does.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

import streamlit as st

from app.config_schema import LANGUAGES, REFERENCE_MODES, TOOLS, MODALITIES
from app.lib import config_io, subprocess_runner, uploads
from app.lib.paths import REPO_ROOT, STREAMLIT_SCRATCH_DIR, VALIDATE_PY

st.set_page_config(page_title="Run Validation — DIEM", page_icon="▶", layout="wide")
st.title("Run Validation")

cfg = config_io.read_validation_config()


def _list_names(directory: str) -> list[str]:
    return [p.name for p in config_io.list_xlsx(directory)]


def _csv_to_list(text: str) -> list[str]:
    return [x.strip() for x in text.split(",") if x.strip()]


def _list_to_csv(values) -> str:
    return ", ".join(str(v) for v in (values or []))


# ---------------------------------------------------------------------------
# Core settings — deliberately OUTSIDE the form below: widgets inside an
# st.form do not rerun the script until the form is submitted, so the
# "type manually" fallback and the file lists (which depend on working_dir)
# need to live here to update live as you type/select.
# ---------------------------------------------------------------------------

if st.session_state.get("run_proc") is not None:
    st.warning("A run is already in progress below — inputs are locked until it finishes.")

st.subheader("Core settings")
c1, c2, c3 = st.columns(3)
with c1:
    tool = st.selectbox("Tool", TOOLS, index=TOOLS.index(cfg.get("tool")) if cfg.get("tool") in TOOLS else 0)
    language = st.selectbox(
        "Language", LANGUAGES, index=LANGUAGES.index(cfg.get("language")) if cfg.get("language") in LANGUAGES else 0
    )
    iso3 = st.text_input("ISO3 country code", value=str(cfg.get("iso3") or ""))
with c2:
    working_dir = st.text_input("Working dir", value=str(cfg.get("working_dir") or ""))
    q_options = _list_names(working_dir)
    current_q = str(cfg.get("questionnaire_file") or "")
    if current_q and current_q not in q_options:
        q_options = [current_q] + q_options
    q_options = q_options + ["— type manually —"]
    default_idx = q_options.index(current_q) if current_q in q_options else 0
    q_choice = st.selectbox("Questionnaire file (in working dir)", q_options, index=default_idx)
    questionnaire_file = (
        st.text_input("Questionnaire filename", value=current_q)
        if q_choice == "— type manually —"
        else q_choice
    )
    uploaded_q = st.file_uploader(
        "...or drag & drop a questionnaire file here", type=["xlsx"], key="upload_questionnaire"
    )
    if uploaded_q is not None:
        dest = uploads.save_uploaded_file(uploaded_q, Path(working_dir))
        questionnaire_file = uploaded_q.name
        st.caption(f"Saved to `{dest}` and selected above as the questionnaire file.")
with c3:
    reference_mode = st.selectbox(
        "Reference mode",
        REFERENCE_MODES,
        index=REFERENCE_MODES.index(cfg.get("reference_mode")) if cfg.get("reference_mode") in REFERENCE_MODES else 0,
    )
    templates_dir = st.text_input("Templates dir", value=str(cfg.get("templates_dir") or ""))
    previous_round_file = str(cfg.get("previous_round_file") or "")
    if reference_mode == "previous_round":
        prev_options = _list_names(working_dir)
        if previous_round_file and previous_round_file not in prev_options:
            prev_options = [previous_round_file] + prev_options
        previous_round_file = st.selectbox(
            "Previous round file (in working dir)",
            prev_options or [previous_round_file],
            index=(prev_options.index(previous_round_file) if previous_round_file in prev_options else 0),
        )
        uploaded_prev = st.file_uploader(
            "...or drag & drop a previous-round file here", type=["xlsx"], key="upload_previous_round"
        )
        if uploaded_prev is not None:
            dest = uploads.save_uploaded_file(uploaded_prev, Path(working_dir))
            previous_round_file = uploaded_prev.name
            st.caption(f"Saved to `{dest}` and selected above as the previous round file.")
    else:
        uploaded_tpl = st.file_uploader(
            "...or drag & drop a template file here (used as the reference since reference_mode=latest_template)",
            type=["xlsx"],
            key="upload_template",
        )
        if uploaded_tpl is not None:
            dest = uploads.save_uploaded_file(uploaded_tpl, Path(templates_dir))
            if uploads.template_name_matches(tool, language, uploaded_tpl.name):
                st.caption(f"Saved to `{dest}` — will be auto-detected as the newest {tool} template for {language.upper()}.")
            else:
                st.warning(
                    f"Saved to `{dest}`, but 'latest_template' auto-detection for {tool}/{language.upper()} "
                    f"looks for a filename containing both `{tool}` and `{language.upper()}` "
                    "— this file won't be picked up as the reference until renamed to match."
                )

output_dir = st.text_input("Output dir", value=str(cfg.get("output_dir") or ""))

# ---------------------------------------------------------------------------
# Remaining settings — batched in a form since none of these have dynamic
# reveal/dependency logic, so there's no reason to rerun on every keystroke.
# ---------------------------------------------------------------------------

with st.form("run_validation_form"):
    existing_profile = str(cfg.get("config_profile") or "").strip()
    clear_profile = False
    if existing_profile:
        st.warning(
            f"config_profile is currently set to `{existing_profile}` — its keys are applied "
            "*after* this form's values when validate.py runs, so it can silently override what "
            "you set below."
        )
        clear_profile = st.checkbox("Clear config_profile for this run", value=False)

    st.subheader("Modules")
    m1, m2 = st.columns(2)
    with m1:
        ignore_modules = st.text_area(
            "ignore_modules_from_comparison (comma-separated)",
            value=_list_to_csv(cfg.get("ignore_modules_from_comparison")),
        )
    with m2:
        skip_modules = st.text_area(
            "skip_modules_from_validated_output (comma-separated)",
            value=_list_to_csv(cfg.get("skip_modules_from_validated_output")),
        )

    kobo_opts = dict(cfg.get("kobo_options") or {})
    geopoll_opts = dict(cfg.get("geopoll_options") or {})

    if tool == "kobo":
        with st.expander("KoBo options (advanced)", expanded=False):
            k1, k2 = st.columns(2)
            with k1:
                include_admin3 = st.checkbox("include_admin3", value=bool(kobo_opts.get("include_admin3", False)))
                skip_restore = st.checkbox(
                    "skip_restore_and_replacement", value=bool(kobo_opts.get("skip_restore_and_replacement", False))
                )
                require_additional_info = st.checkbox(
                    "require_additional_info", value=bool(kobo_opts.get("require_additional_info", True))
                )
                require_crop_list = st.checkbox(
                    "require_crop_list", value=bool(kobo_opts.get("require_crop_list", True))
                )
            with k2:
                country_specific_list_names = st.text_area(
                    "country_specific_list_names (comma-separated)",
                    value=_list_to_csv(kobo_opts.get("country_specific_list_names")),
                )
                exclude_qnames_from_option_compare = st.text_area(
                    "exclude_qnames_from_option_compare (comma-separated)",
                    value=_list_to_csv(kobo_opts.get("exclude_qnames_from_option_compare")),
                )
    else:
        with st.expander("GeoPoll options (advanced)", expanded=False):
            g1, g2 = st.columns(2)
            with g1:
                max_qname_length = st.number_input(
                    "max_qname_length", min_value=1, value=int(geopoll_opts.get("max_qname_length", 28))
                )
            with g2:
                modality = st.selectbox(
                    "modality",
                    MODALITIES,
                    index=MODALITIES.index(geopoll_opts.get("modality")) if geopoll_opts.get("modality") in MODALITIES else 0,
                )

    st.subheader("Housekeeping")
    h1, h2 = st.columns(2)
    hk_cfg = dict(cfg.get("housekeeping") or {})
    with h1:
        hk_enabled = st.checkbox("housekeeping.enabled", value=bool(hk_cfg.get("enabled", True)))
    with h2:
        hk_dry_run = st.checkbox("housekeeping.dry_run", value=bool(hk_cfg.get("dry_run", False)))

    st.subheader("Report metadata")
    r1, r2 = st.columns(2)
    with r1:
        validation_number = st.number_input("validation_number", min_value=1, value=int(cfg.get("validation_number", 1)))
    with r2:
        user_name = st.text_input("user_name", value=str(cfg.get("user_name") or ""))

    prepare_clicked = st.form_submit_button(
        "Prepare run", disabled=st.session_state.get("run_proc") is not None
    )

if prepare_clicked:
    new_values: dict = {
        "tool": tool,
        "working_dir": working_dir,
        "questionnaire_file": questionnaire_file,
        "language": language,
        "iso3": iso3.strip().upper(),
        "reference_mode": reference_mode,
        "previous_round_file": previous_round_file,
        "templates_dir": templates_dir,
        "output_dir": output_dir,
        "housekeeping.enabled": hk_enabled,
        "housekeeping.dry_run": hk_dry_run,
        "ignore_modules_from_comparison": _csv_to_list(ignore_modules),
        "skip_modules_from_validated_output": _csv_to_list(skip_modules),
        "validation_number": int(validation_number),
        "user_name": user_name,
    }
    if tool == "kobo":
        new_values.update(
            {
                "kobo_options.include_admin3": include_admin3,
                "kobo_options.skip_restore_and_replacement": skip_restore,
                "kobo_options.require_additional_info": require_additional_info,
                "kobo_options.require_crop_list": require_crop_list,
                "kobo_options.country_specific_list_names": _csv_to_list(country_specific_list_names),
                "kobo_options.exclude_qnames_from_option_compare": _csv_to_list(exclude_qnames_from_option_compare),
            }
        )
    else:
        new_values.update(
            {
                "geopoll_options.max_qname_length": int(max_qname_length),
                "geopoll_options.modality": modality,
            }
        )
    if clear_profile:
        new_values["config_profile"] = ""

    st.session_state["run_plan"] = new_values

# ---------------------------------------------------------------------------
# Diff preview + confirm
# ---------------------------------------------------------------------------

plan = st.session_state.get("run_plan")
if plan and st.session_state.get("run_proc") is None:
    changes = config_io.diff_writable_keys(plan)
    st.subheader("Changes to configuration/validation_config.yaml")
    if not changes:
        st.info("No changes — the tracked config already matches this form.")
    else:
        for key, old, new in changes:
            st.write(f"**{key}**: `{old!r}` → `{new!r}`")
    st.caption("A timestamped backup is written to configuration/.streamlit_backups/ before saving.")

    if st.button("Confirm & write config + run", type="primary"):
        config_io.write_validation_config_keys(plan)
        log_dir = STREAMLIT_SCRATCH_DIR / "logs"
        stamp = time.strftime("%Y%m%d_%H%M%S")
        log_path = log_dir / f"validate_{stamp}.log"
        proc = subprocess_runner.start([str(VALIDATE_PY)], cwd=REPO_ROOT, log_path=log_path)
        st.session_state["run_proc"] = proc
        st.session_state["run_log_path"] = log_path
        st.session_state["run_plan"] = None
        st.rerun()

# ---------------------------------------------------------------------------
# Live log
# ---------------------------------------------------------------------------


@st.fragment(run_every=2)
def _tail_run() -> None:
    proc = st.session_state.get("run_proc")
    log_path = st.session_state.get("run_log_path")
    if proc is None or log_path is None:
        return

    st.subheader("Live output")
    st.code(subprocess_runner.read_log(log_path) or "(waiting for output...)", language="text")

    rc = subprocess_runner.poll(proc)
    if rc is None:
        if st.button("Stop run"):
            proc.terminate()
    else:
        subprocess_runner.finish(proc)
        st.session_state["run_proc"] = None
        if rc == 0:
            st.success("validate.py finished (exit code 0). See the Results Browser page for the report.")
        else:
            st.error(f"validate.py exited with code {rc}. See the log above.")


if st.session_state.get("run_proc") is not None:
    _tail_run()
