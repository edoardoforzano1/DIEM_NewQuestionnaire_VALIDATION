# Template and Previous Round

## Where the templates come from

The official templates are published in the **DIEM Toolbox** on SharePoint:
`OER - 01. DIEM Monitoring / 03. Toolbox / 02. Questionnaires`. That folder
is set as `templates_source_dir` in `configuration/validation_config.yaml`.

Before every run, `validate.py` copies every `*geopoll*` / `*kobo*` template
that is new or newer in the Toolbox into the local `templates_dir` (the
repo's `Template/` folder). The run log shows a **Template sync** block with
the files copied.

- The Toolbox files are **copied, never opened in place or changed**. OneDrive
  placeholder files raise "Permission denied" when Python opens them
  directly, and the originals must stay untouched.
- If the Toolbox is not reachable (offline, OneDrive not synced), the run
  continues with the templates already in `Template/` and prints a warning.
  The agent compares the template it used with the Toolbox list and tells you
  if it was older.
- A template that disappears from the Toolbox is not deleted locally.
- Leave `templates_source_dir` empty to turn the sync off.

## Template baseline

In `latest_template` mode, the validator selects the newest template in
`templates_dir` for the configured `tool`, by the 8-digit date in the file
name, then by file time.

- **Multilingual templates** (from 20261007, e.g.
  `diem_household_questionnaire_geopoll_20261007_ISO3.xlsx`) carry no
  language code in the name and match every language.
- Older templates with a language code (`_EN_`, `_FR_`) match only that
  language.

The report's Summary sheet says which file was used ("Checked against").
When a template changes during a validation (a new version in the Toolbox),
some differences may come from the template rather than from the country.

## Previous round baseline

In `previous_round` mode, the validator uses `previous_round_file` resolved
under `working_dir`, usually last round's validated questionnaire. The
template is still used to restore placeholders before the comparison.

## Why both matter

- Template protects standard structure consistency.
- Previous round protects longitudinal consistency.

Using both strategically across the workflow reduces false positives and
preserves comparability over time.
