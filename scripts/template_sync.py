"""
Template sync: copy the official questionnaire templates from the shared
DIEM Toolbox folder (SharePoint, synced locally by OneDrive) into the local
templates_dir before each validation run.

Why copy instead of reading the shared folder directly: OneDrive files are
reparse-point placeholders, and opening them in place from Python fails with
PermissionError while a Windows file copy (shutil.copy2 -> CopyFile2) works.
The validators therefore keep reading the local templates_dir, which this
module keeps up to date.

Only top-level *.xlsx files whose name contains the tool name (geopoll /
kobo) are copied; Office lock files (~$...) are skipped. A file is copied
when it is missing locally or the source is newer or a different size.
Failures never stop a run -- they are reported so the caller can warn.
"""
from __future__ import annotations

import shutil
from pathlib import Path


def sync_templates(source_dir: Path | str, target_dir: Path | str, tools: list[str]) -> dict:
    """Returns {"enabled", "source_dir", "copied": [...], "up_to_date": [...], "errors": [...]}."""
    result = {"enabled": bool(str(source_dir or "").strip()), "source_dir": str(source_dir or ""),
              "copied": [], "up_to_date": [], "errors": []}
    if not result["enabled"]:
        return result
    src_dir, dst_dir = Path(source_dir), Path(target_dir)
    if not src_dir.is_dir():
        result["errors"].append(f"templates_source_dir not reachable: {src_dir}")
        return result
    dst_dir.mkdir(parents=True, exist_ok=True)

    for src in sorted(src_dir.glob("*.xlsx")):
        name = src.name
        if name.startswith("~$") or not any(t.lower() in name.lower() for t in tools):
            continue
        dst = dst_dir / name
        try:
            s = src.stat()
            if dst.exists():
                d = dst.stat()
                if d.st_size == s.st_size and d.st_mtime >= s.st_mtime - 2:
                    result["up_to_date"].append(name)
                    continue
            shutil.copy2(src, dst)
            result["copied"].append(name)
        except OSError as exc:
            result["errors"].append(f"{name}: {exc}")
    return result
