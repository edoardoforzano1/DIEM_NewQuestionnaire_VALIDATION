---
name: diem-validate
description: Run the standard DIEM household questionnaire validation (GeoPoll or KoBo) for an operator, round after round, until the questionnaire is validated - intake of the required inputs, validator run, report reading, checks of the validated output (placeholders, Additional information, crop list top-10 and sorting, TLU, admin lists, interview length), a summary message, a Word document and cover email for the country team, memory of open points across versions, operator decisions ("SMAR said it's fine"), and the final package (validated questionnaire, final report, final email). Use this whenever the user shares or mentions a country questionnaire file (e.g. diem_household_questionnaire_geopoll_<country>_*.xlsx), a new version of one, asks to "validate", "check", "review" a questionnaire, asks what a validation report means or what the country must fix, says a point is accepted or solved, or asks whether a questionnaire is ready to send to GeoPoll / deploy — even if they don't say "skill" or name the validator.
---

# DIEM questionnaire validation — standard procedure

Goal: any operator gets the same, trustworthy answer to "what does the country
have to fix before this questionnaire can be deployed?", round after round,
until it is validated. The operator-facing description of this procedure is
`docs/agent/standard-procedure.md`.

**Documentation rule — every change is reflected in the docs.** Whenever you
change this skill, its scripts or references, the validators, the
configuration keys or the folder layout, update the documentation in the same
piece of work, before saying the change is done:
- procedure, messages, outputs, case folder → `docs/agent/` (`standard-procedure.md`, `case-folder.md`, `requests.md`, `maintaining.md`);
- issue types, severities, checks → `docs/workflow/geopoll-logic.md` / `kobo-logic.md` and `checks-and-severity.md`;
- config keys, output folders, housekeeping → `docs/getting-started.md`;
- templates and sync → `docs/data-sources/template-and-previous-round.md`.
Never edit `docs/function-reference/*` by hand (`python scripts/regenerate_function_docs.py`). Build the site (`<python> -m mkdocs build`) to check links when pages or the nav change, and list the pages you updated in your answer. The `diem-docs` skill covers answering from and opening the docs.

The loop: **intake → run → read → check output → outputs (summary, Word
document, cover email) → wait for the new version → re-validate against the
open points → … → when nothing is open, ask, then build the final package.**

**One command for the whole loop — `scripts/diem_case.py`** (`diem_case.bat`
at the repo root): `setup` → `start` → `run` → (`fix`) → `points` → `outputs`
→ … `decide` … → `final`. Use it for every case: it runs the setup check
before anything, refuses to guess intake answers (prints the questions to ask),
puts every file in the case folder with the standard names, and builds the
Word document and the email draft. The same procedure is written for other
agents (Codex) in `AGENTS.md` at the repo root — keep the two in step. The
sections below give the detail of each step (what to read, how to write the
points, the message shapes); the low-level scripts stay available.

Repo: the working directory (`validate.py`, `scripts/`, `configuration/`).
Bundled tools (run with the validation environment's Python; `python-docx`
is needed for the Word files):
- `scripts/inspect_questionnaire.py` — read-only facts about the file (tool, languages filled, settings, Additional information columns, modality hint)
- `scripts/run_validation.py` — runs the validator on one file without permanently editing config
- `scripts/summarize_report.py` — compact digest of the report
- `scripts/check_validated_output.py` — deployability checks on the validated questionnaire
- `scripts/validation_case.py` — the case file: inputs, iterations, points and their status across rounds
- `scripts/questionnaire_profile.py` — questions by type, added/removed by type, admin levels, crops, interview length
- `scripts/make_fix_document.py` — Word document in the house style from a JSON spec
- `scripts/build_final_package.py` — final validated questionnaire + final report from a closed case
- `scripts/diem_case.py` — the procedure as one command (see above)
- `scripts/check_setup.py` — setup check of the computer (`--fix` sets the two machine-specific folder paths)
- `scripts/apply_minor_fixes.py` — minor text fixes made by DIEM on a copy of the file, recorded in the case (tag *Fixed by DIEM*)
- `scripts/gp_subform_check.py` — check of a GeoPoll programmed form (Subform) against the validated KoBo questionnaire and the GeoPoll template (exception only)
- `references/issue-guide.md` — what each issue type means, typical fix, known noise. Read it before writing the points.

**Never modify the original files on SharePoint/OneDrive** (templates under
`templates_source_dir`, or country questionnaires shared from there) — no
edit, rename, move, delete or re-save, for any reason. Read or copy only.

## Where results go

Everything is published under `output_dir` (`validation_config.yaml`), the
DIEM questionnaire validation folder in Temp, split by tool:

```
C:/Temp/DIEM_questionnaire_validation/
  geopoll_output/                       reports + validated questionnaires (GeoPoll)
    validation_cases/<ISO3>_<round>/    one folder per GeoPoll case: case.json, Word docs, FINAL files
  kobo_output/                          the same for KoBo
    validation_cases/<ISO3>_<round>/
  configuration/                        config snapshot of each run
  archive/<YYYY-MM>/                    older reports / validated files moved out by housekeeping
  _agent_runs/                          scratch (staged copies, temp profiles, logs) — deleted after 7 days
```

Housekeeping runs before every validation (`housekeeping:` block): it keeps
the last 3 reports and validated questionnaires per tool/country/language/
round and moves older ones to `archive/` (purged after 180 days), clears
`_agent_runs/`, and never touches `validation_cases/`. Put every file you
produce for a case (Word documents, email text, output checks, final files)
in that case's folder, never elsewhere.

## 0. Explain the procedure, then find the case

**At the start of a new case, before asking for inputs, tell the operator in
plain English what is going to happen** — short, no jargon, no script names.
Use this, adapted to what they already gave you:

> Here's how this works:
> 1. **Inputs** — I need the file location, KoBo or GeoPoll, whether to compare with the latest template or the previous round, and the languages to check besides English. I'll ask for anything missing.
> 2. **Validation** — I run the check and look at the questionnaire that would be sent to GeoPoll / deployed in KoBo.
> 3. **Results** — you get a short summary saying whether it's ready, the points **to fix** and the points **to confirm**, a Word document for the country team and a cover email. I don't send anything myself.
> 4. **Corrections** — when the country sends a new version, give it to me: I check it against the open points and tell you what's solved and what's still pending. If a point is settled outside the file (e.g. SMAR agrees), just tell me and I'll close it.
> 5. **Final version** — when nothing is pending, I'll ask whether to prepare the validated questionnaire and the final report (questions added/removed, admin levels, accepted exceptions).
>
> Everything is saved in `C:\Temp\DIEM_questionnaire_validation\<geopoll|kobo>_output\validation_cases\<country>_<round>\`.

Skip the explanation for a new version of an existing case, or when the
operator says they know the procedure; a one-line reminder of where you are
in it ("round 2 — checking the new version against 3 open points") is enough.

A case is one country + tool + round, kept in
`<output_dir>/<tool>_output/validation_cases/<ISO3>_<round>/case.json`.
Look before asking anything:

```bash
<env-python> .claude/skills/diem-validate/scripts/validation_case.py find --root <output_dir> [--iso3 YEM]
```

**Always check the country's history** (earlier rounds, both tools) before
the first run of a case:

```bash
<env-python> .claude/skills/diem-validate/scripts/validation_case.py history --root <output_dir> --iso3 YEM [--exclude-case <this case.json>]
```

It prints each earlier point once, with its final outcome and how it was
solved (built from the earlier `case.json` files — nothing is duplicated).
Read it yourself; tell the operator only what helps, in at most two lines
(e.g. "R12 had 3 agreed exceptions — I'll flag them if they come back").
`iterate` then returns `seen_before` for every issue of the run that was a
point in an earlier round, with that round's outcome.

- **Open case for this country/tool** and the operator brings a new version →
  go to step 8 (re-validation). Take tool, reference, languages and
  deployment language from the case; do not ask again.
- The operator closes a point ("SMAR said …") → step 9.
- Otherwise it is a new case → step 1.

## 1. Intake (new case)

The run needs these. **Ask for what is missing; never guess a value the file
does not prove.** Ask everything open in **one** message (question tool,
your proposal first).

| Input | How to get it |
|---|---|
| Location of the file | from the message; must exist |
| Tool: KoBo or GeoPoll | from the sheets (GeoPoll survey has `varname_new`; KoBo has `type`/`name` + `choices`); confirm if the file name disagrees |
| Reference: latest template or previous round | ask unless said; previous round also needs that file |
| Languages besides English | English is always checked. Ask which others; propose the ones filled in the survey and in `Replacement (xx)` (from `inspect_questionnaire.py`) |
| Country, ISO3, round | propose from the file name / `Admin 1 info`; the round (R1, R12…) is the case key, so confirm it |
| Deployment language | default: the non-English language in scope, or `settings.default_language` (KoBo); confirm when there are several |

Then run the inspector on a copy and settle, in the same message, only the
points still open:

```bash
<env-python> .claude/skills/diem-validate/scripts/inspect_questionnaire.py "<copy of the file>"
```

- **Languages in scope**: a language filled in the survey but empty in Additional information is usually a template leftover; out-of-scope columns are not checked (`--languages en,fr`). KoBo removes them, and the no-language `label::` columns, from the validated questionnaire (SMAR, Nov 2026); never touch them in the country's file.
- **Modality**: CAPI/CATI (KoBo `Sample` calculation; GeoPoll is normally CATI). Sets the FS-indicator ceiling and explains removed `cluster`/`gps_*`.
- **Form type**: if `looks_like_kii` or not a household questionnaire, there is no matching template — see 2b.
- **Admin3**: whether admin3 is rebuilt from AGOL (`include_admin3`) when the file has an admin3 list.

Create the case:

```bash
<env-python> .claude/skills/diem-validate/scripts/validation_case.py new --root <output_dir> \
  --country Yemen --iso3 YEM --tool geopoll --round R1 --reference-mode latest_template \
  --languages en,ar --deploy-language ar --source "<folder of the file>" [--previous-round <file>]
```

## 2. Pre-flight

- **Setup check**: `diem_case.py setup` (also run automatically by `start` and `run`). Nothing starts while a line FAILs; on a new computer `setup --fix` sets the two machine-specific folder paths.
- **Python env**: CLAUDE.md says `diem-validation`. If `conda env list` doesn't have it, use an env that imports `polars`, `openpyxl`, `yaml`, `xlsxwriter`, `docx`, and say which one you used. Call its `python.exe` directly (not `conda run`, which crashes on non-ASCII output on Windows).
- **Template freshness**: `validate.py` copies newer templates from `templates_source_dir` (DIEM Toolbox) into `templates_dir` before every run. After the run check `template_sync` in the runner output; on a WARNING the run used what was already local — compare `reference` with `toolbox_templates` and tell the operator if it is older (an old template produces dozens of false issues). If a new template appeared since the last iteration, say so: some differences may come from the template, not the country.

## 2b. Forms without a template (KII, traders)

The validator can't run on these. Check them directly instead:
- convert with `pyxform` (`xls2xform_convert(..., validate=False)`) to catch XLSForm errors;
- every `select_*` list exists in `choices`, every `${var}` exists, groups and repeats are balanced, each repeat has a `repeat_count`;
- every code used in `relevant`, `constraint`, `choice_filter` and `calculation` exists in that question's list, and `=` is not used on a `select_multiple`;
- labels are filled for every language in scope and no `#…#` / `$…$` is left;
- for every list or variable name shared with the household template: same codes, labels and type;
- admin lists against AGOL (`fetch_agol_admin_rows`): the same pcode scheme as the household survey.

## 3. Run

```bash
<env-python> .claude/skills/diem-validate/scripts/run_validation.py --repo <repo> \
  --questionnaire "<path>" --tool geopoll --language <deploy language> --iso3 YEM \
  --languages en,ar --python <env-python>
```

It stages a copy (avoids OneDrive/Excel locks), points `config_profile` at a temporary profile, runs `validate.py`, and restores `validation_config.yaml` byte-for-byte. Never hand-edit `validation_config.yaml` for a run. Check `ok`, `config_restored: true`, `reference`, `counts`; on failure read `log_tail`. **Use the `report` and `validated` paths it returns**: when an older output is open in Excel the validator writes a time-suffixed name instead. The run hits AGOL live (internet needed) and applies output housekeeping — normal.

Then record the iteration (save the output check of step 5 first, see there):

```bash
<env-python> .claude/skills/diem-validate/scripts/validation_case.py iterate --case <case.json> \
  --file "<original file path>" --report "<report>" --validated "<validated>" --output-check "<check.md>"
```

## 4. Read the report

```bash
<env-python> .claude/skills/diem-validate/scripts/summarize_report.py "<report.xlsx>"
```

Read the digest and `references/issue-guide.md`. Spot-check suspicious items in the country file before calling them country errors: some are template-side (listed in the guide), some are noise. A verified finding is worth more than ten repeated ones. If the report shows a decision that changes the verdict and the operator can answer faster than the file (e.g. a removed core module that may be an approved exception), ask before writing the points; if the answer means a different run, re-run.

## 5. Check the validated output

```bash
<env-python> .claude/skills/diem-validate/scripts/check_validated_output.py "<validated.xlsx>" --source "<country file>" > "<case dir>/iter<N>_output_check.md"
```

GeoPoll: no `$…$` left, no malformed `$…#`, runtime `#VAR#` inventory, repeated adjacent words, English words inside Arabic text, interview length, exactly 10 crops selected and selected crops first, mandatory Additional information keys per language, TLU weights, Admin 1/2(/3) sheets and parent codes. KoBo: check manually that `settings` `form_title` has `#ADMIN0#` replaced, no `#…#`/`$…$` left in `survey`/`choices`, crop and admin choice lists injected.

## 6. Points: what goes to the country

Turn the findings into **points** and record them in the case. One point =
one root cause (three skip patterns pointing to `o_debt` = one point). Each
point has a section (part of the questionnaire, in questionnaire order), a
type, a short title, and `keys` from the report so the next run can tell if
it is still there:

```bash
<env-python> .claude/skills/diem-validate/scripts/validation_case.py keys --report "<report>"
```

`keys` are `issue_type|Q Name or Set` strings from that list; for an
output-check finding use `output_match` with text of its WARN/FAIL line
(e.g. `"Crop selection"`). Types: `To fix`, `To confirm`, `Placeholder`,
`Optional`, `Template side`.

- **Recurring issues** (`seen_before` from `iterate`): reuse what worked.
  - Fixed last time → same point, and you may add one sentence to the
    action: "Last round this was solved by …".
  - Accepted last time (an agreed exception) → do not close it yourself; ask
    the operator in one line whether the same exception still holds
    ("R12: SMAR accepted 3 agri CS — same for this round?"), then record it
    as accepted with the new `by`/`note`, or as open.
  - Keep it light: at most a short "(also R12: …)" tag on the point in the
    summary message. Never add history to the Excel report or a history
    section to the Word document.
- Differences the operator already explained or agreed (e.g. in an email
  they paste) go in as `"status": "accepted"` with `note` and `by`, so they
  are documented exceptions and do not come back as new.
- Points the operator said to drop are not sent; record them as `dropped`
  with a note.
- Remaining high/medium report rows that are noise or template-side: say so
  in the summary; record template problems as `Template side` points.

```bash
<env-python> .claude/skills/diem-validate/scripts/validation_case.py add-points --case <case.json> --points points.json --iteration <N>
```
(or `diem_case.py points --case <case.json> --points points.json`).

### 6b. Minor fixes made by DIEM (standard)

To keep the country office on the main fixes, **propose to the operator, in
one line, to fix the minor text errors yourself** ("I can correct these N
small text errors in a copy so the country focuses on the main fixes — OK?").
Minor = text only, no effect on what is asked or who is asked: typos, doubled
words or punctuation, unbalanced brackets, an option left in English in
another language column, a placeholder still showing its `#`/`$`, a repeated
operator instruction, a `Mandatory` value spelled differently. Never routing,
conditions, `relevant`, constraints, calculations, or adding/removing
questions or options — those stay points for the country.

On yes, write `fixes.json` (docstring of `apply_minor_fixes.py`) and run
`diem_case.py fix --case <case.json> --fixes fixes.json`. It writes
`<file>_DIEM-fixes.xlsx` in the case folder and records each fix as a point
(tag *Fixed by DIEM*, status fixed). Then:
- the Word document ends with **"Corrections already made by DIEM"** (row,
  question, column, before, after), added automatically by `outputs`;
- the email says how many were corrected and asks the country to make the
  remaining fixes **in the attached corrected file**;
- the final report lists them under **"Minor corrections made by DIEM"**.
Re-check the corrected copy (the minor issues must be gone). For a
template-format case, the next round starts from the corrected copy the
country sends back; if DIEM fixed the last file itself, `run` the corrected
copy before `final`.

## 7. Outputs of each round

Produce all three, then stop.

### 7a. Summary message (chat, always this shape)

```
## <Country> <round> <GeoPoll|KoBo> questionnaire — validation <date> (version <file date>)
**<READY / NOT READY>** — <one line why>
Reference: <template or previous-round file> · Languages: EN + <xx> · Deployment: <xx>
Report: high N · medium N · info N | Output check: N fail · N warn | Interview: <m+r> min mandatory+recommended, <total> min total

### Since the last version            (from the 2nd round on)
Fixed: P01 …, P03 …   Accepted: P04 … (by …)   Still open: P02 …

### To fix
**<Section>**
- P05 <what, where: sheet/row/variable/column> → <action>
### To confirm
**<Section>**
- P06 …
### Template side (SMAR — nothing for the country)
- …
### Checked and fine
<one line>

Files: <Word document> · <cover email> · <report> · <validated questionnaire>
```

READY only when no point is open. Mention the 30-minute rule when the
interview is long (mandatory+recommended ≤ 30 min before low-priority
questions; the template's LoI sheet warns above 30 min in total).

### 7b. Word document for the country team

Build it with `make_fix_document.py` (house style: Arial, blue headings,
`Consolas` for names and formulas, shaded tables), **open points only**,
saved in the case folder (`<output_dir>/<tool>_output/validation_cases/<ISO3>_<round>/`) as `<ISO3>_<round>_<tool>_points_to_fix_v<N>.docx` (`diem_case.py outputs` builds it with the email draft `<ISO3>_<round>_<tool>_email_v<N>.txt`)
(new name if Word has it open):

```bash
<env-python> .claude/skills/diem-validate/scripts/make_fix_document.py spec.json "<case dir>/<file>.docx"
```

The script's docstring describes `spec.json`. Render to PDF (Word COM
`ExportAsFixedFormat`, or LibreOffice) and look at it before handing it over.

Structure:
1. Title, file reviewed, reference, one line on how to read rows ("rows" are
   rows of the country's file; "template row N" a row of the reference).
2. Summary table of every point: number (the case id, P01…), section, type,
   short name, rows.
3. One `h1` per part of the questionnaire, in questionnaire order; each point
   an `h2` with its `tag`.
4. **Template side** last, saying the country has nothing to do.

How to write each point:
- Where: sheet, row(s), variable, and **the column by its name** (`relevant`,
  `calculation`, `Skip pattern`, `label::French (fr)`…), never column letters.
- What the cell holds now and what the template holds; formulas in a `code`
  block only when short.
- The action tells the team to **copy the cells from the template rows**,
  never to copy text from the document.
- One sentence on why it matters. No validator check names or severities.
- Plain, short sentences; "we" for DIEM, "you" for the country team. Do not
  translate or judge wording in a language the operator cannot read: show
  template vs current side by side and ask to confirm.
- Admin explanations and question counts go in the final report, not here.

### 7c. Cover email (plain text, short, no AI style)

```
Subject: <Country> <round> questionnaire – validation points

Dear colleagues,

Thank you for the questionnaire. We validated it against <reference>.
<One sentence: what is fine.>

The attached document lists <N> points: <n> to fix and <n> to confirm,
by part of the questionnaire. Points marked as template issues come from the
template itself; we will correct them there.
If any of these were agreed with the SMAR team, just let us know.

Once the file is updated, please send it back and we will check it again.

Best regards,
<operator name>
```

Then **stop and tell the operator**: "Send me the new version when the
country replies, or tell me if a point is agreed (e.g. by SMAR)."

## 8. New version of an open case

1. `status` the case and show the open points in one short block.
2. Run steps 3–5 with the case's inputs, then `iterate`.
3. For each open point `iterate` proposes *still present* or *not found any
   more -> fixed?*. Confirm by looking at the file, then
   `set --status fixed --by agent --note "<how it was solved>"` — the note is
   the solution future rounds will see ("country restored the template
   Conditional"), so describe what changed in the file, not just "not found".
   Points with no keys: check by hand.
4. `new_issues_not_in_any_point`: new problems (or old ones never recorded)
   become new points (step 6).
5. Outputs as in step 7, with the "Since the last version" block; the Word
   document and email cover only what is still open or new.

## 9. Operator decisions

When the operator says a point is solved outside the file ("SMAR said 3
agriculture coping strategies are fine", "the country confirmed no
incentive"), close it with who decided:

```bash
<env-python> .claude/skills/diem-validate/scripts/validation_case.py set --case <case.json> \
  --id P04 --status accepted --by "SMAR (email 22 Oct)" --note "3 agri CS accepted for Yemen"
```

Use `accepted` for agreed exceptions, `dropped` for points that were not real
problems. The note is what later rounds will read: say what was agreed and
why, in one line. Confirm back in one line, then show what is still open. Do not
close a point because the country *says* it fixed it: re-validate.

## 10. Closing

When `status` shows `ready_to_close: true` (no open point), **ask** the
operator whether to produce the final package. Only on a yes:

```bash
<env-python> .claude/skills/diem-validate/scripts/build_final_package.py --case <case.json> --reference "<reference used in the last run>"
```

It refuses while points are open (`--force` only if the operator insists,
and say it in the final report). It writes to the case folder:
- `<ISO3>_<round>_<tool>_validated_questionnaire_FINAL.xlsx` — copy of the last validated questionnaire;
- `<ISO3>_<round>_<tool>_final_validation_report.docx` — validation rounds, questions by type, added/removed by type, admin levels and units, crops, interview length, fixes by round, accepted exceptions with who agreed them, template issues sent to SMAR;
- `final_report_spec.json` — to adjust wording and rebuild with `make_fix_document.py`.

Render the report to PDF and look at it. Then write the final email:

```
Subject: <Country> <round> questionnaire – validated

Dear colleagues,

The <Country> <round> <GeoPoll|KoBo> questionnaire is validated. Attached:
- the validated questionnaire (<file>), to <send to GeoPoll | deploy in KoBo>;
- the final validation report: questions by type, questions added and removed,
  admin levels (<a1> / <a2> / <a3> units), selected crops, interview length
  (<m+r> min mandatory and recommended, <total> min in total), and the
  exceptions agreed during the validation.

Thank you for the quick follow-up.

Best regards,
<operator name>
```

If the run exposed a validator false positive, say so and offer to fix the
validator separately (CLAUDE.md: plan first, confirm, regenerate docs, run
`smoke_test`).
