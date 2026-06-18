# Getting Started

## 1. Create and Activate Conda Environment

An `environment.yml` is included in the repository root. Run once:

```powershell
conda env create -f environment.yml
conda activate diem-validation
```

This installs Python 3.12, all validator dependencies (`polars`, `openpyxl`, `pyyaml`, `xlsxwriter`), and the documentation packages (`mkdocs`, `mkdocs-material`).

> **Already have the environment?** Update it instead:
> ```powershell
> conda env update -f environment.yml --prune
> ```

## 2. Launch Interactive Documentation (Recommended)

From the repository root, with the environment activated:

```powershell
.\documentation
```

Opens the local docs site at `http://127.0.0.1:8000/`.

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
| `language` | Language code for label comparison | `en`, `fr`, `ar`, `es` |
| `iso3` | Country code | Three-letter ISO code (e.g. `YEM`, `AFG`) |
| `reference_mode` | Which baseline to compare against | `latest_template` or `previous_round` |
| `working_dir` | Folder where your input questionnaire file lives | Set to the folder on your machine that contains the questionnaire |
| `questionnaire_file` | Filename of the questionnaire to validate | Filename only — the file must be inside `working_dir` |
| `previous_round_file` | Filename of the previous-round baseline | Only used when `reference_mode: previous_round` |
| `config_profile` | Optional YAML overlay for quick switching between run configurations | Resolved from `config_profiles_dir`, or `<output_dir>/config_profiles/` by default |

### Path settings that are specific to each user

`templates_dir` ships with the repo and normally needs no changes — it defaults to the repo-local `Template/` folder, which contains both the KoBo and GeoPoll official templates side by side:

```yaml
templates_dir: "c:/git/DIEM_NewQuestionnaire_VALIDATION/Template"
```

`latest_template` mode auto-selects the newest file in that folder matching the configured `tool` and `language`. Only change this if you keep templates somewhere else (e.g. a shared drive).

`output_dir` — where reports are written. This path is specific to each user and must be set once on first setup. Each tool writes to its own subfolder:

```yaml
output_dir: "C:/Temp/questionnaire_validation"
# reports land in:
#   output_dir/geopoll_output/   (GeoPoll)
#   output_dir/kobo_output/      (KoBo)
```

You can set this to any folder that exists on your machine.

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
keeps the newest files for each tool/type/country/language/round group.

```yaml
housekeeping:
  enabled: true
  dry_run: false
  keep_all_for_last_days: 0
  protect_today_files: false
  keep_reports_per_group: 3
  keep_validated_per_group: 3
  keep_config_snapshots_per_group: 30
  archive_before_delete: true
  archive_dir: ""
  delete_archives_older_than_days: 180
```

- Use `dry_run: true` to print planned actions without changing files.
- With `archive_before_delete: true`, excess files move to
  `<output_dir>/archive/<YYYY-MM>/...`.
- A sidecar file named `<filename>.keep` protects that file from retention and
  archive purging.
- The configured `previous_round_file` is also protected.

### KoBo replacement and admin options

```yaml
kobo_options:
  include_admin3: false
  skip_restore_and_replacement: false
  require_additional_info: true
  require_crop_list: true
```

`include_admin3` enables AGOL admin3 fetching and rebuilding. By default,
admin3 values are left untouched. `skip_restore_and_replacement` bypasses
placeholder restoration, replacement, and crop-list rebuilding; use it only
for an already-personalized workbook. The two `require_*` settings control
whether missing or invalid input sheets become explicit HIGH replacement
failures.

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
| `mkdocs` + `mkdocs-material` | Local documentation site |
