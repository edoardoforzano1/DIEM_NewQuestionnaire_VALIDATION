"""
Start the local documentation site (MkDocs) for this repository and print
the URL. Finds a Python that has mkdocs + mkdocs-material: the interpreter
running this script first, then the conda envs (diem-validation first).

Usage:
  python serve_docs.py [--repo <repo>] [--port 8000] [--page workflow/geopoll-logic]
Prints JSON {"url", "python", "pid"} and leaves the server running.
If something already answers on the port, it is reused.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path


def _has_mkdocs(py: str) -> bool:
    try:
        return subprocess.run([py, "-c", "import mkdocs, material"], capture_output=True, timeout=60).returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


def _candidates() -> list[str]:
    out = [sys.executable]
    roots = [Path(os.environ.get("CONDA_PREFIX", "")).parent, Path.home() / "anaconda3" / "envs",
             Path.home() / "miniconda3" / "envs", Path.home() / ".conda" / "envs"]
    envs = []
    for r in roots:
        if r and r.is_dir():
            envs += sorted(r.glob("*/python.exe")) + sorted(r.glob("*/bin/python"))
    envs.sort(key=lambda p: 0 if p.parent.name == "diem-validation" or p.parent.parent.name == "diem-validation" else 1)
    out += [str(p) for p in envs]
    for base in (Path.home() / "anaconda3" / "python.exe", Path.home() / "miniconda3" / "python.exe"):
        if base.exists():
            out.append(str(base))
    seen, uniq = set(), []
    for p in out:
        if p not in seen:
            seen.add(p)
            uniq.append(p)
    return uniq


def _root(url: str) -> str | None:
    """The site root as served, or None if nothing answers. mkdocs serve
    redirects "/" to the site_url path (e.g. /DIEM_Questionnaire_Validation/)."""
    try:
        with urllib.request.urlopen(url, timeout=2) as r:
            return r.geturl() if r.status == 200 else None
    except OSError:
        return None


def _page_url(root: str, page: str) -> str:
    # the "offline" plugin in mkdocs.yml serves pages as <page>.html
    page = page.strip("/").removesuffix(".md").removesuffix(".html")
    return root.rstrip("/") + "/" + (page + ".html" if page else "")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parents[4]))
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--page", default="")
    a = ap.parse_args()
    base = f"http://127.0.0.1:{a.port}/"
    root = _root(base)
    if root:
        print(json.dumps({"url": _page_url(root, a.page), "reused": True}))
        return 0
    py = next((p for p in _candidates() if _has_mkdocs(p)), None)
    if not py:
        print(json.dumps({"error": "no Python with mkdocs + mkdocs-material found; "
                                   "create the env: conda env create -f environment.yml"}))
        return 1
    log = open(Path(a.repo) / "site_serve.log", "w", encoding="utf-8")
    flags = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0) | getattr(subprocess, "DETACHED_PROCESS", 0)
    proc = subprocess.Popen([py, "-m", "mkdocs", "serve", "-a", f"127.0.0.1:{a.port}"], cwd=a.repo,
                            stdout=log, stderr=subprocess.STDOUT, creationflags=flags)
    for _ in range(90):
        root = _root(base)
        if root:
            print(json.dumps({"url": _page_url(root, a.page), "python": py, "pid": proc.pid}))
            return 0
        if proc.poll() is not None:
            break
        time.sleep(1)
    print(json.dumps({"error": "mkdocs did not start; see site_serve.log", "python": py}))
    return 1


if __name__ == "__main__":
    sys.exit(main())
