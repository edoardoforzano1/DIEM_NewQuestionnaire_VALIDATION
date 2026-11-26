# AGENTS.md — instructions for coding agents (Codex and others)

This repository validates DIEM household questionnaires (KoBo or GeoPoll)
against the official template or the previous round. Read `CLAUDE.md` for
the code base (architecture, conventions, what not to touch); it applies to
every agent, not only Claude.

When an operator asks you to **validate a country questionnaire** (or gives
you a new version of one, says a point is agreed, or asks for the final
version), follow the standard procedure below. Claude follows the same one
(`.claude/skills/diem-validate/SKILL.md`, which has the full detail: read it
when unsure). The operator's guide is `docs/agent/standard-procedure.md`.
**Every step goes through `diem_case`**, so the questions, the order, the
file names and the documents are the same whoever runs it.

```
python .claude/skills/diem-validate/scripts/diem_case.py <step> ...      (or: diem_case <step> ...)
```

Use the validation environment's Python (`conda activate diem-validation`;
call its `python.exe` directly if `conda run` breaks on non-ASCII output).

## Hard rules

- **Never modify the original files** on SharePoint/OneDrive (DIEM Toolbox
  templates, country questionnaires shared from there): copy only.
- **Never guess intake answers.** If `start` lists questions, ask the
  operator all of them in one message and wait.
- **Never send emails or files.** You prepare them; the operator sends.
- **Never edit `configuration/validation_config.yaml` for a run** (runs use
  a temporary profile; only `setup --fix` may set the two folder paths).
- Code changes to the validators: describe the plan and wait for the
  operator's yes (see `CLAUDE.md`).

## The procedure

0. **`diem_case setup`** — checks the environment, the output folder, the
   templates and AGOL. Nothing starts while a line FAILs. On a new computer
   `setup --fix` sets `templates_dir` and `templates_source_dir`.
1. **Explain the steps** to the operator in plain English at the start of a
   new case (inputs → validation → summary, Word document and email →
   corrections → final version; files in the case folder).
2. **`diem_case start --file F --tool kobo|geopoll --reference latest|previous
   [--previous-round FILE] --languages en,fr --country X --iso3 XXX --round R12`**
   — creates the case folder and prints the country's history. If the file
   is a GeoPoll programmed form (sheet `Subform`), checking it is an
   exception: the operator must accept it and give the validated KoBo
   questionnaire of the same round (`--kobo-reference`); the email reminds
   the country to send the DIEM template format next time.
3. **`diem_case run --case CASE --file F`** — validates, records the round,
   writes `iter<N>_digest.md` and `iter<N>_output_check.md`, and compares with
   the open points.
4. **Read and verify.** Read the digest and
   `.claude/skills/diem-validate/references/issue-guide.md`. Check each
   finding in the file before calling it a country error (some are noise or
   template-side). One point = one root cause.
5. **Minor fixes by DIEM (standard).** Text-only corrections that do not
   change what is asked or who is asked — typos, doubled words or
   punctuation, unbalanced brackets, an option left in English in another
   language column, a placeholder still showing `#`/`$`, a repeated operator
   instruction, a `Mandatory` value spelled differently — are **proposed to
   the operator** in one line ("I can fix these N small text errors myself so
   the country can focus on the main fixes — OK?"). On yes:
   `diem_case fix --case CASE --fixes fixes.json` writes
   `<file>_DIEM-fixes.xlsx` in the case folder and records each fix (tag
   *Fixed by DIEM*). Never use it for routing, conditions, relevant,
   constraints, calculations, or adding/removing questions or options.
6. **`diem_case points --case CASE --points points.json`** — the remaining
   points: `section`, `tag` (To fix / To confirm / Placeholder / Optional /
   Template side), `title`, `keys` from the report.
7. **`diem_case outputs --case CASE --spec spec.json --operator NAME`** —
   builds `<ISO3>_<round>_<tool>_points_to_fix_v<N>.docx` (agreed layout:
   summary table, one section per part of the questionnaire, each point with
   row, variable and column name and what to do; the DIEM corrections table
   is added automatically at the end) and the email draft
   `<ISO3>_<round>_<tool>_email_v<N>.txt`. Spec format: docstring of
   `make_fix_document.py`. Write the points in plain short sentences, columns
   by name, "copy from template row N". No validator check names.
8. **Summary to the operator** (shape in SKILL.md §7a): READY / NOT READY,
   reference, languages, counts, points by section, what DIEM fixed, files to
   send (Word document, corrected questionnaire if any, email). Then stop.
9. **New version** → `run` again on the case. Close what is gone with
   `diem_case decide --case CASE --id P03 --status fixed --by country --note "<how it was solved>"`.
10. **Operator decisions** → `decide --status accepted|dropped --by "<who, when>" --note "<what was agreed>"`.
11. **Final** — when `status` shows nothing open, ask the operator; on yes
   `diem_case final --case CASE --operator NAME` builds the final
   questionnaire, the final report (including the DIEM corrections and the
   agreed exceptions) and the final email. If DIEM fixed the last file of a
   template-format case, `final` asks to `run` the corrected copy first.

## Where files go

`<output_dir>/<geopoll|kobo>_output/validation_cases/<ISO3>_<round>/`
(`output_dir` = `C:/Temp/DIEM_questionnaire_validation` by default): the
received version, `case.json`, digests and checks of each round, the Word
documents, the corrected copies, email drafts and the final package.
Housekeeping never deletes case folders.

## Keep in step

When the procedure changes, update together: this file, `SKILL.md`,
`docs/agent/*.md` and `diem_case.py`.
