---
name: diem-validate
description: Run the DIEM household questionnaire validation (GeoPoll or KoBo) on a country questionnaire, read the Excel report, and turn it into a prioritized fix list for the country team, plus independent checks of the validated output questionnaire (unreplaced $placeholders$, Additional information values, crop list top-10 selection and sorting, TLU weights, admin lists, interview length). Use this whenever the user shares or mentions a country questionnaire file (e.g. diem_household_questionnaire_geopoll_<country>_*.xlsx), asks to "validate", "check", "review" a questionnaire, asks what a validation report means or what the country must fix, or asks whether a validated questionnaire is ready to send to GeoPoll / deploy — even if they don't say "skill" or name the validator.
---

# DIEM questionnaire validation

Goal: give the user (a DIEM analyst) a trustworthy answer to "what does the
country have to fix before this questionnaire can be deployed?" — not a dump
of the report. The validator's report compares the country file against the
template; the validated output is what GeoPoll will receive. Both matter, and
the report alone has known blind spots, so always do both halves below.

Repo: the working directory (`validate.py`, `scripts/`, `configuration/`).
Bundled tools (run with the validation environment's Python):
- `scripts/inspect_questionnaire.py` — read-only facts about the file (tool, languages filled, settings, Additional information columns, modality hint) for the analyst check-in
- `scripts/run_validation.py` — runs the validator on one file without permanently editing config
- `scripts/summarize_report.py` — compact digest of the report
- `scripts/check_validated_output.py` — deployability checks on the validated questionnaire
- `scripts/make_fix_document.py` — builds the Word document for the country team from a JSON spec (step 7)
- `references/issue-guide.md` — what each issue type means, typical fix, known noise. Read it before writing the fix list.

**Never modify the original files on SharePoint/OneDrive** (templates under `templates_source_dir`, or country questionnaires shared from there) — no edit, rename, move, delete or re-save, for any reason. Read or copy only; always work on a local copy.

## 1. Gather inputs

Infer what you can and confirm only what is ambiguous:
- **Questionnaire path** — the country file.
- **Tool** — `geopoll` / `kobo`, from the filename or sheets (GeoPoll survey has `varname_new`; KoBo has `type`/`name` + `choices`).
- **ISO3** — from the filename or `Admin 1 info` sheet (`adm0_ISO3`). Confirm.
- **Language** — the deployment language (`en`/`fr`/`ar`/…). The validator always checks the other filled language columns too, but the main comparison and output names follow this. If the country deploys in Arabic or French and the user didn't say, ask.
- **Reference** — default `latest_template`. Use `previous_round` only when the user asks to compare with last round (needs that file).

## 1b. Check in with the analyst (before running)

Decisions the file can't settle on its own produce whole blocks of false
issues when guessed wrong (e.g. Arabic columns left over from the template
reported as dozens of unresolved placeholders). Settle them before the run,
not by spotting them in the output. Work on a copy, then run:

```bash
<env-python> .claude/skills/diem-validate/scripts/inspect_questionnaire.py "<copy of the file>"
```

Show the analyst what you found and ask, in **one** message (use the
question tool, recommended answer first), only the points that are open:
- **Languages in scope** — list every language with filled `label`/`hint` cells and filled `Replacement (xx)` columns. A language filled in the survey but empty in Additional information is usually a template leftover. Ask which languages count; out-of-scope columns stay in the file and are simply not checked (`--languages en,fr`). Never delete a language column unless asked.
- **Deployment language** — default from `settings.default_language` (KoBo) or the filename; confirm.
- **Modality** — CAPI/CATI (KoBo `Sample` calculation, GeoPoll is normally CATI). Sets the FS-indicator ceiling and explains removed `cluster`/`gps_*`.
- **Form type** — if `looks_like_kii` or the file is not a household questionnaire, there is no matching template: say so and agree on structural checks or a previous-round comparison instead of running against the household template.
- **Reference** — latest template vs previous round, if the analyst hinted at a round comparison.
- **Admin3** — whether admin3 should be rebuilt from AGOL (`include_admin3`), when the file has an admin3 list.

Skip the check-in only when every point is already clear from the request.
Record the answers and pass them to the runner; mention them in the final
answer's header line.

## 2. Pre-flight (cheap, prevents misleading reports)

- **Python env**: CLAUDE.md says `diem-validation`. If `conda env list` doesn't have it, use an env that imports `polars`, `openpyxl`, `yaml`, `xlsxwriter`, and tell the user which one you used. Call that interpreter's `python.exe` directly (not `conda run`, which crashes on non-ASCII output on Windows).
- **Template freshness**: the official templates live in the DIEM Toolbox folder on SharePoint (`templates_source_dir` in `validation_config.yaml`, e.g. `…/03. Toolbox/02. Questionnaires/`). `validate.py` copies any newer template from there into the local `templates_dir` before every run, so nothing to do normally. After the run, check `template_sync` in the runner output: if it shows a WARNING (SharePoint folder not reachable / OneDrive not synced), the run used whatever was already local — compare `reference` with `toolbox_templates` and tell the user if the reference is older, because an old template produces dozens of false issues. (Files are copied, not read in place, because OneDrive placeholder files can't be opened directly from Python.)

## 2b. Forms without a template (KII, traders)

The validator can't run on these. Check them directly instead:
- convert with `pyxform` (`xls2xform_convert(..., validate=False)`) to catch XLSForm errors;
- every `select_*` list exists in `choices`, every `${var}` exists, groups and repeats are balanced, each repeat has a `repeat_count`;
- every code used in `relevant`, `constraint`, `choice_filter` and `calculation` (`${q} = 'x'`, `selected(${q}, 'x')`, `name != 'x'`) exists in that question's list, and `=` is not used on a `select_multiple`;
- labels are filled for every language in scope and no `#…#` / `$…$` is left;
- for every list or variable name shared with the household template: same codes, same labels, same type. Data that should be joined with the household survey must use the same codes and variable names. A correspondence sheet in the file, if there is one, says which variables are meant to match;
- admin lists against AGOL (`fetch_agol_admin_rows`): the same pcode scheme as the household survey.

## 3. Run

```bash
<env-python> .claude/skills/diem-validate/scripts/run_validation.py --repo <repo> \
  --questionnaire "<path>" --tool geopoll --language en --iso3 YEM \
  --languages en,fr --python <env-python>
```

`--languages` sets `languages_in_scope` for the run (the languages agreed in
1b); leave it out to check every filled language.

It stages a copy of the file (avoids OneDrive/Excel locks), points `config_profile` at a temporary profile, runs `validate.py`, and restores `validation_config.yaml` byte-for-byte. Don't hand-edit `validation_config.yaml` for a run — CLAUDE.md requires confirmation for config edits, and the runner makes it unnecessary. Check in the JSON output: `ok`, `config_restored: true`, `reference` (which template was actually used — sanity-check its date against `templates_available`/`toolbox_templates`), and `counts`. On failure read `log_tail`.

The run also hits AGOL live for admin lists (needs internet) and applies output housekeeping (old outputs in `output_dir` may be archived) — that's normal validator behaviour.

## 4. Read the report

```bash
<env-python> .claude/skills/diem-validate/scripts/summarize_report.py "<report.xlsx>"
```

Read the digest, then `references/issue-guide.md`. Before you call anything a country error, spot-check suspicious items against the actual country file (open the row): the report can flag template rows the country removed, and some issues are template-side (listed in the guide). A finding you verified is worth more than ten you repeated.

## 5. Check the validated output

```bash
<env-python> .claude/skills/diem-validate/scripts/check_validated_output.py "<validated.xlsx>" --source "<country file>"
```

GeoPoll checks: no `$…$` left, no malformed `$…#`, runtime `#VAR#` inventory, repeated adjacent words (a replacement inserted next to the same word, e.g. "محافظة محافظة" — the country text already had the word), interview length (core+recommended ≤ 30 min), exactly 10 crops selected and selected crops listed first in every crop question, mandatory Additional information keys filled for each language in use, TLU weights, Admin 1/2(/3) sheets and parent codes.

For KoBo the script's survey checks don't apply as-is; check manually: `settings` `form_title` has `#ADMIN0#` replaced by the country name, no `#placeholder#`/`$…$` left in `survey`/`choices` labels, crop and admin choice lists injected.

## 5b. Second check-in (only if needed)

If the report turns up a decision that changes the verdict and that the
analyst can answer faster than the file can, ask it before writing the fix
list, in one message: e.g. old vs new admin pcode scheme (deploy the
country's own lists or rebuild from AGOL?), a core module removed that may be
an approved exception (fish in a non-fishing country), a custom logic block
replacing a template one. If the answer means a different run (other
languages, admin3 on, other reference), re-run instead of explaining the
noise away.

## 6. Write the answer

Lead with the verdict, then the fix list. Use this structure:

```
## <Country> GeoPoll questionnaire — validation <date>
Verdict: Not ready / Ready after fixes / Ready.  (reference: <template file>, language <xx>)
Counts: high N · medium N · info N   |   Output check: N fail, N warn

### Must fix before deployment
1. <what is wrong, where (variable / sheet / row)> → <concrete fix>
...
### Should fix / confirm with the country team
...
### Template-side issues (raise with SMAR, not the country)
...
### Checked and fine
<one line: e.g. FS indicators, FIXED_CODES, TLU, admin lists, placeholders resolved>
```

Guidance for the list:
- Group the same root cause into one item (e.g. three skip patterns pointing to `o_debt` → "rename `o_debt` to `c_debt` in income_main/sec/third skip patterns").
- Give the exact replacement when you can (target variable, code range, which Additional information row/column).
- Rank by consequence: broken routing, missing core blocks, fixed codes, TLU, unreplaced placeholders first; wording and info last.
- Keep info-level items out of the list unless they explain something (e.g. 58 optional removals = normal module selection).
- Mention the interview length and whether low-priority questions are justified under the 30-minute rule.

Offer next steps: produce a corrected copy of the country file (only if asked — never overwrite the original), re-run after fixes, or draft the email to the country team. If the run exposed a validator false positive, say so and offer to fix the validator separately (following CLAUDE.md: plan first, confirm, then regenerate docs and run `smoke_test`).

## 7. Word document for the country team (always)

Every validation ends with a Word document the analyst can send to the
country team, in addition to the answer in chat. Build it with the bundled
script, so the style is always the same (Arial, blue headings, `Consolas`
for variable names and formulas, grey formula blocks, shaded tables):

```bash
<python-with-python-docx> .claude/skills/diem-validate/scripts/make_fix_document.py spec.json "<output_dir>/<Country>_<round>_<tool>_points_to_review.docx"
```

The script's docstring describes `spec.json` (blocks `h1`, `h2` + `tag`, `p`,
`bullet`, `action`, `code`, `table`, `summary`; inline `**bold**` and
`` `code` ``). Save the document next to the report and never in the
SharePoint folder. If Word has the file open, write a new version (`_v2`).
Before sending it, render it to PDF (Word COM `ExportAsFixedFormat`, or
LibreOffice when available) and look at the pages.

**Structure**
1. Title, the file reviewed, the reference it was compared with, and one line on
   how to read the rows: they are rows of the country's file, and "template
   row N" means a row of the reference.
2. A summary table of every point: number, section, type, short name, rows.
3. One `h1` section per part of the questionnaire, **in questionnaire order**
   (e.g. Settings, Introduction and consent, Location / admin, Crop production,
   Crop sales, Livestock, Fishing, Shocks, Food security, Needs and
   assistance, Closing). Each point inside is an `h2` with a `tag`:
   - `To fix`: a difference from the template that has to change.
   - `Placeholder`: text the country must type in now.
   - `To confirm`: a difference that may be intended. Ask, and say what to
     copy from the template if it was not intended.
   - `Optional`: cleanup that does not affect the data.
   Only parts that have points get a section. Number the points across the
   whole document, not per section.
4. Last section, **Template side**: problems in the template itself (typos,
   wrong labels, logic bugs) to raise with SMAR. Say clearly that the country
   team has nothing to do on these. Leave the section out when there are none.

**How to write each point**
- Always say where the point is: the sheet, the row(s), the variable name and
  **the column by its name** (`relevant`, `calculation`, `choice_filter`,
  `constraint`, `label::French (fr)`, `name`, `list_name`…). Never use column
  letters.
- Say what the cell holds now and what the template holds. Show a formula in a
  `code` block only when it is short enough to read.
- The action tells the team to **copy the cells from the template rows**
  ("copy the `relevant` cells of template rows 274–276 into your rows
  216–218"). It never tells them to copy text from the document.
- Say in one sentence why the point matters (what breaks in the form or in the
  data). No jargon, and no validator check names or severities.
- Plain, short sentences in the analyst's voice. Use "we" for DIEM and "you"
  for the country team. No filler.
- Keep out the decisions the analyst handles separately: admin list
  explanations and mandatory-question counts are left for the final
  validation email, unless the analyst asks for them.
- Leave out points the analyst said to drop (e.g. a module the country does
  not need).

Offer a short cover email (plain text, no AI style) that presents the
document's sections in one line each.
