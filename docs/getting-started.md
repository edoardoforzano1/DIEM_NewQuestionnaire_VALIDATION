# Getting Started

## 1. Create and Activate Conda Environment

An `environment.yml` is included in the repository root. Run once:

```powershell
conda env create -f environment.yml
conda activate diem-validation
```

This installs Python 3.12, all validator dependencies (`polars`, `openpyxl`, `pyyaml`, `xlsxwriter`), `python-docx` (Word documents produced by the agent), and the documentation packages (`mkdocs`, `mkdocs-material`).

!!! tip "Running validations with the agent"
    Operators do not need the rest of this page: open Claude Code in the
    repository folder and ask for the validation in plain language. The
    agent sets the configuration for each run and restores it afterwards.
    See [Working with the agent](agent/index.md). This page describes the
    manual route and every configuration key.

> **Already have the environment?** Update it instead:
> ```powershell
> conda env update -f environment.yml --prune
> ```

## 2. Launch Interactive Documentation (Recommended)

From the repository root, with the environment activated:

```powershell
.\documentation
```

Opens the local docs site at `http://127.0.0.1:8000/`. You can also ask the
agent: *"open the documentation"*.

### Optional: install a global `documentation` command

Run once to register the command inside the conda env:

```powershell
.\install-documentation-command.cmd
```

After that, with `diem-validation` active, you can run `documentation` from any folder.

## 3. Configure and Run Validation

Edit `configuration/validation_config.yaml`, then from the repository root:

```powershell
validate
```

### Key settings to change each run

| Setting | What it controls | Notes |
|---|---|---|
| `tool` | Which validator to run | `kobo` or `geopoll` |
| `language` | Main (deployment) language for label comparison and output names | `en`, `fr`, `ar`, `es` |
| `languages_in_scope` | Languages checked in the placeholder / replacement scans | List, e.g. `["en", "ar"]`. Empty = every filled language. Other language columns stay in the file, unchecked (e.g. Arabic columns left over from the template in a French country) |
| `iso3` | Country code | Three-letter ISO code (e.g. `YEM`, `AFG`) |
| `reference_mode` | Which baseline to compare against | `latest_template` or `previous_round` |
| `working_dir` | Folder where your input questionnaire file lives | Set to the folder on your machine that contains the questionnaire |
| `questionnaire_file` | Filename of the questionnaire to validate | Filename only — the file must be inside `working_dir` |
| `previous_round_file` | Filename of the previous-round baseline | Only used when `reference_mode: previous_round` |
| `config_profile` | Optional YAML overlay for quick switching between run configurations | Resolved from `config_profiles_dir`, or `<output_dir>/config_profiles/` by default |
| `config_profiles_dir` | Custom folder containing profile files | Optional; defaults to `<output_dir>/config_profiles/` when empty |

### Path settings that are specific to each user

`templates_dir` is the local folder the validators read templates from — the repo-local `Template/` folder, which contains both the KoBo and GeoPoll templates side by side. `templates_source_dir` is the official DIEM Toolbox folder on SharePoint (synced by OneDrive):

```yaml
templates_dir: "c:/git/DIEM_NewQuestionnaire_VALIDATION/Template"
templates_source_dir: "C:/Users/<you>/Food and Agriculture Organization/OER - 01. DIEM Monitoring/03. Toolbox/02. Questionnaires"
```

Before every run, `validate.py` copies any newer or missing `*geopoll*` / `*kobo*` template from `templates_source_dir` into `templates_dir`, so `latest_template` always uses the newest official version. Files are copied, never opened in place or modified: OneDrive placeholder files cannot be opened directly from Python, and the originals must stay untouched. If the Toolbox folder is unreachable the run continues with the templates already copied, with a warning. Leave `templates_source_dir` empty to turn the sync off. See [Template and Previous Round](data-sources/template-and-previous-round.md).

`latest_template` mode auto-selects the newest file in `templates_dir` for the configured `tool`, by the 8-digit date in the filename. Multilingual templates (from 20261007) have no language code in the name and match every language.

`output_dir` — the DIEM questionnaire validation folder where every result is published, split by tool:

```yaml
output_dir: "C:/Temp/DIEM_questionnaire_validation"
```

```
C:/Temp/DIEM_questionnaire_validation/
  geopoll_output/                       reports + validated questionnaires (GeoPoll)
    validation_cases/<ISO3>_<round>/    one folder per GeoPoll case (agent)
  kobo_output/                          the same for KoBo
    validation_cases/<ISO3>_<round>/
  configuration/                        config snapshot of each run
  archive/<YYYY-MM>/                    files moved out by housekeeping
  admin_tools_output/                   admin tools (admin_tools_config.yaml)
  _agent_runs/                          agent scratch files
```

You can point it to another folder; the subfolders are created automatically.

### Where to put the input file

Place the questionnaire file you want to validate inside the folder set as `working_dir`, then set `questionnaire_file` to its filename:

```yaml
working_dir: "C:/Temp"
questionnaire_file: "my_questionnaire_en_AFG_20260101.xlsx"
```

The validator reads the file from `working_dir/questionnaire_file`. If the file is not found at that path, the run will stop with an error.

### Output housekeeping

Housekeeping runs before validation when `housekeeping.enabled: true`. It scans
`kobo_output`, `geopoll_output`, and the output configuration snapshots, then
keeps the newest files for each tool/type/country/language/round group. A file
is archived if it's **either** past its group's keep-count limit **or** older
than `archive_older_than_days` (whichever comes first, same as standard log
rotation) — the two protective settings (`keep_all_for_last_days`,
`protect_today_files`) always take precedence over both triggers.

```yaml
housekeeping:
  enabled: true
  dry_run: false
  keep_all_for_last_days: 0
  protect_today_files: false
  keep_reports_per_group: 3
  keep_validated_per_group: 3
  keep_config_snapshots_per_group: 30
  archive_older_than_days: 0
  archive_before_delete: true
  archive_dir: ""
  delete_archives_older_than_days: 180
  delete_agent_run_files_after_days: 7
```

- Use `dry_run: true` to print planned actions without changing files.
- Reports and validated questionnaires saved with a time suffix (because a
  file of the same name was open in Excel) are grouped and archived like the
  others.
- `delete_agent_run_files_after_days` clears `<output_dir>/_agent_runs/` (the
  agent's staged copies, temporary profiles and run logs) after that many
  days; 0 keeps them. These files are never archived.
- `validation_cases/` folders are never archived or deleted: they are the
  record of each validation.
- `archive_older_than_days` (0 = disabled) archives a file once it's this many
  days old, independent of its group's count limit — e.g. `10` archives
  anything older than 10 days even if the group hasn't exceeded
  `keep_reports_per_group` yet.
- With `archive_before_delete: true`, excess files move to
  `<output_dir>/archive/<YYYY-MM>/...`.
- A sidecar file named `<filename>.keep` protects that file from retention and
  archive purging.
- The configured `previous_round_file` is also protected.

### Module filtering

Two settings let you narrow what gets compared or what appears in the validated output:

```yaml
ignore_modules_from_comparison: []
skip_modules_from_validated_output: []
```

`ignore_modules_from_comparison` — differences inside the listed modules are excluded from issue reporting. The modules are still read; they just produce no report rows. Useful for optional country-specific modules that are expected to diverge from the template.

`skip_modules_from_validated_output` — goes further: the listed modules are excluded from both comparison and the validated output file.

For GeoPoll, use the short module code from the `module` column (e.g. `"migration"`, `"remit"`). For KoBo, use the `begin_group` name or the visible group label.

```yaml
ignore_modules_from_comparison:
  - migration
skip_modules_from_validated_output:
  - remit
```

### Report metadata

Two optional fields recorded in the report header:

```yaml
validation_number: 1
user_name: "Edoardo"
```

`validation_number` is a sequential counter — increment it when you run multiple passes for the same questionnaire (e.g. after corrections). `user_name` identifies who ran the validation in the report header.

### GeoPoll options

```yaml
geopoll_options:
  max_qname_length: 28
  modality: "cati"
  derived_placeholders:
    MAX DIGIT DK:  {source: "MAX AMOUNT", repeat_digit: "8", extra_digits: 0}
    MAX DIGIT REF: {source: "MAX AMOUNT", repeat_digit: "9", extra_digits: 0}
  crop_list_closing_options:
    EN: {no_crop: "No crop production", dont_know: "DON'T KNOW", refused: "REFUSED"}
    FR: {no_crop: "Aucune production végétale", dont_know: "NE SAIT PAS", refused: "REFUS"}
    AR: {no_crop: "عدم إنتاج المحاصيل", dont_know: "لا أعرف", refused: "رفض الاجابة"}
```

- `max_qname_length`: variable names longer than this are flagged (medium).
- `modality`: `cati` or `capi`; `capi` applies the FS-indicator ceiling.
- `derived_placeholders`: placeholders computed from another Additional
  information value instead of typed by the country. With `MAX AMOUNT =
  10000000`, `$MAX DIGIT DK$` becomes `88888888` and `$MAX DIGIT REF$`
  `99999999`. A value typed in the sheet always wins; remove an entry to stop
  deriving it.
- `crop_list_closing_options`: the closing options appended to the expanded
  crop lists (91 no crop production / 92 don't know / 93 refused), in each
  language column's own language. A language not listed uses English.

### KoBo replacement and admin options

```yaml
kobo_options:
  include_admin3: false
  skip_restore_and_replacement: false
  require_additional_info: true
  require_crop_list: true
  max_qname_length: 32
  modality: "capi"
```

`include_admin3` enables AGOL admin3 fetching and rebuilding. By default,
admin3 values are left untouched. `skip_restore_and_replacement` bypasses
placeholder restoration, replacement, and crop-list rebuilding; use it only
for an already-personalized workbook. The two `require_*` settings control
whether missing or invalid input sheets become explicit HIGH replacement
failures. `max_qname_length` and `modality` work as in `geopoll_options`
(default 32 characters for KoBo).

## 4. Admin Tools (Optional)

Three standalone tools are available for checking and updating admin boundary
lists in a validated questionnaire. They use
`configuration/admin_tools_config.yaml`.

The minimum settings to review before running either tool:

| Setting | What it controls |
|---|---|
| `iso3` | Country code — must match the questionnaire you are checking |
| `language` | Language code (`en`, `fr`, `ar`, `es`) — controls which label column is read |
| `source.mode` | `standard` to auto-pick the latest validated output, `custom` to specify a file by name |
| `output_dir` | Where the check report or synced file will be written |

Run from the repository root with the environment active:

```powershell
tool_admin_check   # compare questionnaire admin lists against AGOL
tool_admin_sync    # create a new questionnaire file with admin lists updated from AGOL
tool_admin_parent_remap  # repair admin3 parents that should point to merged admin2 codes
```

See [Admin Tools](tools/admin-tools.md) for the full reference.

## Environment Contents

| Package | Purpose |
|---|---|
| `polars` | DataFrame engine used throughout the validation pipeline |
| `openpyxl` | Read/write Excel questionnaire and report files |
| `pyyaml` | Parse `validation_config.yaml` and `critical_sets.yaml` |
| `xlsxwriter` | Write formatted Excel report workbooks |
| `python-docx` | Word documents for the country team and the final report (agent) |
| `mkdocs` + `mkdocs-material` | Local documentation site |
