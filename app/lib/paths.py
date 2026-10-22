"""
Path constants shared by the Streamlit UI.

Mirrors how validate.py resolves the repo root
(``ROOT = pathlib.Path(__file__).parent``), one directory further up since
this module lives in app/lib/.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / "scripts"
CONFIG_DIR = REPO_ROOT / "configuration"

VALIDATE_PY = REPO_ROOT / "validate.py"
VALIDATION_CFG_PATH = CONFIG_DIR / "validation_config.yaml"
ADMIN_CFG_PATH = CONFIG_DIR / "admin_tools_config.yaml"

TOOL_ADMIN_CHECK_PY = SCRIPTS_DIR / "tool_admin_check.py"
TOOL_ADMIN_SYNC_PY = SCRIPTS_DIR / "tool_admin_sync.py"
TOOL_ADMIN_PARENT_REMAP_PY = SCRIPTS_DIR / "tool_admin_parent_remap.py"

# Scratch space for Streamlit-generated run configs and subprocess logs.
# Never written into by anything else in the repo, and outside git tracking
# (see .gitignore additions made alongside this file).
STREAMLIT_SCRATCH_DIR = REPO_ROOT / "batch_output" / "streamlit_ui"

# Make repo-root-level modules (e.g. `import app...`, `from smoke_test import
# ...`) importable regardless of Streamlit's own sys.path handling.
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
