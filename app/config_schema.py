"""
Single source of truth for the small set of values the Streamlit UI (app/)
hardcodes about the validators and admin tools: enum choices that are not
declared anywhere in the YAML configs (nothing in
configuration/validation_config.yaml says what the valid values of
`reference_mode` are — only code does), plus the output-file/sheet contract
the Results Browser reads.

Everything else the UI surfaces (working_dir, iso3, housekeeping numbers,
etc.) is a plain YAML key rendered directly from whatever is in the config
file, so adding/removing an ordinary config key needs no change here.

See CLAUDE.md > "Before adding or changing anything" — the checklist there
says: if you change one of the values below in a validator, an admin tool,
or validate.py, update it here too. smoke_test.py imports
REQUIRED_REPORT_SHEETS / ISSUE_COLUMNS_REQUIRED from this module (rather
than defining its own copy), so running `smoke_test` after such a change
will fail loudly instead of the UI silently going stale.
"""
from __future__ import annotations

# --- Enum choices --------------------------------------------------------
# Source of truth: validate.py's VALIDATORS dict (TOOLS), the
# LANG_LABEL_COL / detect_label_column languages in admin_tools_common.py
# (LANGUAGES), the reference_mode branch in kobo_validator.py /
# geopoll_validator.py (REFERENCE_MODES), source.mode handling in
# resolve_source_workbook (SOURCE_MODES), sync.mode handling in
# tool_admin_sync.py (SYNC_MODES), and geopoll_options.modality /
# kobo_options.modality (MODALITIES).

TOOLS = ["kobo", "geopoll"]
LANGUAGES = ["en", "fr", "ar", "es"]
REFERENCE_MODES = ["latest_template", "previous_round"]
SOURCE_MODES = ["standard", "custom"]
SYNC_MODES = ["keep_previous", "subset_from_agol", "full_from_agol"]
MODALITIES = ["capi", "cati"]

# --- Output contract ------------------------------------------------------
# Source of truth: the report-writer sections of kobo_validator.py /
# geopoll_validator.py (sheet names), and the f-string output filenames in
# each validator and in scripts/tool_admin_check.py / tool_admin_sync.py.

REQUIRED_REPORT_SHEETS = {
    "kobo":    {"Summary", "Question Changes", "Choice Changes", "Questionnaire Structure", "Replacement Issues"},
    "geopoll": {"Summary", "Question Changes", "Option Changes",  "Questionnaire Structure", "Replacement Issues"},
}

ISSUE_COLUMNS_REQUIRED = {"issue_type", "severity"}

REPORT_GLOB = "report_{tool}_*.xlsx"
VALIDATED_GLOB = "validated_questionnaire_{tool}_*.xlsx"
ADMIN_CHECK_GLOB = "admin_check_report_*.xlsx"
ADMIN_SYNC_GLOB = "*_adminsync_*.xlsx"
