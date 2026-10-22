"""
Subprocess launcher for the Streamlit UI.

Every script is invoked exactly the way its .bat launcher does:
``python <repo-relative script> [args]``, cwd=repo root — see CLAUDE.md
"Entry point and dispatch" and the .bat launcher contents. The validator
scripts are never imported (CLAUDE.md > Known gotchas: "Validator scripts
are not importable — kobo_validator.py and geopoll_validator.py execute
config loading, AGOL fetches, and validation at module level").

Output is redirected to a UTF-8 log file, and the child process gets
PYTHONIOENCODING/PYTHONUTF8 set explicitly, to avoid the Windows cp1252
UnicodeEncodeError documented in CLAUDE.md > Known gotchas > "Windows
stdout encoding".
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def start(argv: list[str], cwd: Path, log_path: Path) -> subprocess.Popen:
    """Launch `python argv[0] argv[1:]`, streaming combined stdout/stderr to log_path."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_file = open(log_path, "w", encoding="utf-8", errors="replace")
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8:replace"
    env["PYTHONUTF8"] = "1"
    proc = subprocess.Popen(
        [sys.executable, *argv],
        cwd=str(cwd),
        stdout=log_file,
        stderr=subprocess.STDOUT,
        env=env,
    )
    # Keep a reference on the Popen object so the log file isn't closed/GC'd
    # while the child is still writing to it.
    proc._diem_log_file = log_file  # type: ignore[attr-defined]
    return proc


def poll(proc: subprocess.Popen) -> int | None:
    return proc.poll()


def finish(proc: subprocess.Popen) -> None:
    """Close the log file handle once the process has exited."""
    log_file = getattr(proc, "_diem_log_file", None)
    if log_file is not None and not log_file.closed:
        log_file.close()


def read_log(log_path: Path) -> str:
    if not log_path.exists():
        return ""
    try:
        return log_path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        return f"(could not read log: {exc})"
