---
name: diem-docs
description: Open, search and explain the DIEM questionnaire validation documentation (the MkDocs site in docs/). Use this whenever the user asks for the documentation, the manual, the guide or "the docs", asks how a check, issue type, severity, report sheet, config key, admin tool or the validation procedure works, asks "where is it explained…", or wants the docs site opened — and when the docs must be updated after a change to the validators, config, skill or procedure.
---

# DIEM validation documentation

The documentation is the MkDocs site built from `docs/` (navigation in
`mkdocs.yml`). Two ways to give it to the user — pick by the question:

## Answer a question from the docs

For "how does X work / what does this issue mean / where do I set Y":
1. Find the page: `mkdocs.yml` `nav` gives the map; search `docs/` (excluding
   `docs/function-reference/*`, which is generated and very long, unless the
   question is about a specific function).
2. Answer in a few sentences, then name the page and section so they can read
   more, e.g. *Validation Workflow → GeoPoll Logic → Critical Sets*.
3. If the docs and the code disagree, trust the code, say so, and offer to
   fix the page.

Where things are:

| Topic | Page |
|---|---|
| How an operator works with the agent, example requests | `docs/agent/*.md` (Working with the Agent) |
| Standard validation procedure (rounds, points, final package) | `docs/agent/standard-procedure.md` |
| Setup, config keys, running by hand | `docs/getting-started.md` |
| Templates, Toolbox sync, previous round | `docs/data-sources/template-and-previous-round.md` |
| Every GeoPoll / KoBo check and issue type | `docs/workflow/geopoll-logic.md`, `docs/workflow/kobo-logic.md` |
| Severity rules | `docs/workflow/checks-and-severity.md` |
| Reading the Excel report | `docs/report-output/*.md` |
| Admin tools | `docs/tools/admin-tools.md` |
| Streamlit UI | `docs/tools/streamlit-ui.md` |

## Open the site

When the user wants to browse ("open the documentation", "show me the docs"):

```bash
<python> .claude/skills/diem-docs/scripts/serve_docs.py [--page agent/standard-procedure]
```

It finds a Python with `mkdocs` + `mkdocs-material` (the `diem-validation`
env first), starts `mkdocs serve` on http://127.0.0.1:8000 in the background
(or reuses a running one) and prints the URL. Open that URL in the built-in
browser pane (`preview_start` with `url`), on the page that answers the
question when there is one. If no env has mkdocs, say how to create it
(`conda env create -f environment.yml`). The plain-terminal equivalent is the
`documentation` command at the repo root.

## Keep the docs current

After any change to the validators, `configuration/*.yaml`, the
`diem-validate` skill or the procedure, update the matching page(s) in the
same piece of work: new issue types and severities in the logic pages and
`checks-and-severity.md`, new config keys in `getting-started.md`, procedure
changes in `docs/agent/`. `docs/function-reference/*` is regenerated with
`python scripts/regenerate_function_docs.py`, never edited by hand. Check
the build with `<python> -m mkdocs build --strict` when a page or the nav
changed.
