# Maintaining the agent

For developers. The agent's behaviour comes from files in this repository,
so it changes with the code and is the same for everyone who clones it.

## Where the behaviour is defined

| File | Role |
|---|---|
| `CLAUDE.md` | project rules the agent always reads: architecture, conventions, "plan first, then change code", never touch SharePoint originals |
| `.claude/skills/diem-validate/SKILL.md` | the standard validation procedure, step by step, with the message, email and document templates |
| `AGENTS.md` (repo root) | the same procedure for Codex and other agents; read automatically by Codex |
| `diem_case.bat` (repo root) | launcher of `diem_case.py`, the procedure as one command |
| `.claude/skills/diem-validate/references/issue-guide.md` | what each issue type means, the usual fix, known noise and template-side problems |
| `.claude/skills/diem-docs/SKILL.md` | how the agent answers documentation questions and opens this site |
| `.claude/settings.json` | hook that regenerates the function reference after a validator edit |

A skill is loaded when a request matches its `description`; the body is then
followed as instructions.

## Bundled scripts (`.claude/skills/diem-validate/scripts/`)

| Script | Does |
|---|---|
| `inspect_questionnaire.py` | read-only facts about a file: tool, languages filled, Additional information columns, modality hints |
| `run_validation.py` | runs `validate.py` on one file through a temporary `config_profile`, restores `validation_config.yaml` byte for byte, returns report and validated paths as JSON |
| `summarize_report.py` | compact digest of a report |
| `check_validated_output.py` | checks on the validated questionnaire: placeholders, repeated words, English left in Arabic, crops, Additional information, TLU, admin sheets, interview length |
| `validation_case.py` | case file: `new`, `find`, `keys`, `add-points`, `iterate` (also returns `seen_before`: earlier rounds where the same issue was a point), `set`, `status`, `history` (earlier points of a country, once each, with outcome) |
| `questionnaire_profile.py` | questions by type, added/removed by type, admin units, crops, interview length |
| `make_fix_document.py` | Word document in the house style from a JSON spec |
| `build_final_package.py` | final validated questionnaire and final report from a closed case (incl. minor corrections made by DIEM) |
| `diem_case.py` | the whole procedure as one command: `setup`, `start`, `run`, `fix`, `points`, `outputs`, `decide`, `status`, `final` |
| `check_setup.py` | setup check of the computer; `--fix` sets `templates_dir` / `templates_source_dir` |
| `apply_minor_fixes.py` | small text corrections by DIEM on a copy of the file, recorded in the case (tag *Fixed by DIEM*) |
| `gp_subform_check.py` | check of a GeoPoll programmed form (Subform) against the validated KoBo questionnaire and the GeoPoll template |

`.claude/skills/diem-docs/scripts/serve_docs.py` finds a Python with MkDocs
and starts this site.

They need the `diem-validation` environment (`python-docx` included, see
`environment.yml`).

## Changing the procedure

1. Change `.claude/skills/diem-validate/SKILL.md`, `AGENTS.md`,
   `diem_case.py` and [Standard procedure](standard-procedure.md) together;
   they describe the same steps for Claude, for other agents and for
   operators.
2. If the case file changes, keep old `case.json` files readable
   (`validation_case.py` reads them directly).
3. Run one case end to end on a real file in a scratch `--root`
   (`validation_case.py new --root <scratch>`), including `build_final_package.py`,
   and look at the Word files rendered to PDF.

## Changing the validators

Follow `CLAUDE.md`: describe the plan, wait for confirmation, trace the data
flow through both validators, then

```powershell
python scripts/regenerate_function_docs.py   # function reference pages
smoke_test                                   # pipeline + Streamlit schema
```

and update the pages that describe the change (logic pages,
`checks-and-severity.md`, `getting-started.md` for config keys). New
templates-side problems the agent should recognise go in `issue-guide.md`.
