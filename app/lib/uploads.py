"""
Drag-and-drop upload helpers for the Run Validation page.

st.file_uploader already provides drag-and-drop in the browser; these
helpers just save the uploaded bytes to the right folder and check whether
an uploaded template's filename would actually be picked up by the "latest
template" auto-detection in each validator — a template that doesn't match
naming won't be found at all, so the UI warns before that surprises anyone
at run time.
"""
from __future__ import annotations

from pathlib import Path


def save_uploaded_file(uploaded_file, dest_dir: Path) -> Path:
    """Save a Streamlit UploadedFile to dest_dir under its own name."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / uploaded_file.name
    dest.write_bytes(uploaded_file.getvalue())
    return dest


def template_name_matches(tool: str, language: str, filename: str) -> bool:
    """Mirrors the exact filename predicate each validator's "latest
    template" auto-detection uses, so the UI can warn before an upload that
    won't actually be found:
      - kobo:    find_kobo_template() in kobo_validator.py
                 -> templates_dir.glob(f"*kobo*{LANG}*.xlsx")
      - geopoll: find_latest_template() in geopoll_validator.py
                 -> "geopoll" in name.lower() and f"_{lang}_" in name.lower()
    Both are effectively case-insensitive: kobo's glob runs on a
    case-insensitive Windows filesystem, geopoll's check lowercases both
    sides explicitly.
    """
    name = filename.lower()
    lang = language.lower()
    if tool == "kobo":
        return "kobo" in name and lang in name
    return "geopoll" in name and f"_{lang}_" in name
