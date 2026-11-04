# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does

Validates DIEM household questionnaire files (KoBo XLSForm or GeoPoll Excel format) against a reference — either the latest official template or the previous round — and produces a structured Excel report classifying every difference by severity. Two standalone tools handle the administrative boundary lists separately.

## Conda environment

All commands must run inside the `diem-validation` conda environment. When running scripts manually:

```powershell
conda activate diem-validation
```

Core dependencies: `polars`, `openpyxl`, `pyyaml`, `xlsxwriter`, `mkdocs-material`, `streamlit`, `ruamel.yaml`.

## Commands

```powershell
# Run validation (reads configuration/validation_config.yaml)
validate

# Check admin boundary lists in a validated questionnaire against AGOL
tool_admin_check

# Create a new questionnaire file with updated admin boundary lists
tool_admin_sync

# Launch local documentation site at http://127.0.0.1:8000/
.\documentation

# Launch the Streamlit UI (browser front end over the commands above)
streamlit_ui

# Regenerate auto-built function reference pages after editing validator scripts
python scripts/regenerate_function_docs.py

# Smoke test — run the full pipeline and verify output structure (also checks
# the Streamlit UI's config_schema.py for drift, see "Streamlit UI (app/)" below)
smoke_test
```

Each `.bat` launcher at the repo root simply calls `python "%~dp0<script>.py" %*`, except `streamlit_ui.bat` which calls `streamlit run "%~dp0app\Home.py" %*`.

Optional CLI flags for admin tools:

```powershell
tool_admin_check --source-file "filename.xlsx" --config "path/to/config.yaml"
tool_admin_sync  --source-file "filename.xlsx" --sync-mode full_from_agol
```

## Architecture

### Entry point and dispatch

`validate.py` reads `configuration/validation_config.yaml`, resolves an optional `config_profile` override, then **launches the selected validator as a subprocess** (`subprocess.run([sys.executable, str(script)])`). It does not import the validators — they are not importable modules.

Before dispatch, `validate.py` also calls `scripts/template_sync.py`: when `templates_source_dir` is set (the DIEM Toolbox folder on SharePoint/OneDrive), any newer or missing `*geopoll*`/`*kobo*` template there is copied into the local `templates_dir`. Templates are copied rather than read in place because OneDrive placeholder files raise `PermissionError` when opened directly from Python (`shutil.copy2` works). An unreachable source only warns.

Before dispatch, `validate.py` calls `scripts/output_housekeeping.py` to archive or delete old output files according to retention rules in the `housekeeping:` config block.

### Validator scripts

`scripts/kobo_validator.py` and `scripts/geopoll_validator.py` are **converted Jupyter notebooks**. They execute top-to-bottom when run as scripts. Config is read at module level from `configuration/validation_config.yaml`. They share a common structure:

1. Load config → resolve questionnaire path → resolve reference file
2. Read questionnaire and reference into Polars DataFrames
3. Run comparison functions (one per check type) that each return a list of issue dicts
4. Collect all issues into a single Polars DataFrame
5. Write the Excel report and validated questionnaire output

The `# SECTION: ## Step N` comments in the validators are parsed by `regenerate_function_docs.py` to build the function reference documentation — do not remove or reformat them.

### KoBo placeholder pipeline

KoBo produces a validated output questionnaire in addition to the report. The pipeline for this file runs five steps inside `produce_validated_questionnaire()`:

1. Copy source workbook
2. Inject crop choices from the Crop list sheet
3. Inject admin choices (fetched live from AGOL)
4. Restore `#placeholder#` tokens from the template (runs even when no replacement pairs are available — passes `replacement_pairs=None` to restore all placeholders without replacing)
5. Apply replacements from the Additional information sheet (only runs when pairs are available)

`_can_run_restore` and `_can_run_replace` are the two flags controlling steps 4/5. They are separate — restore always runs unless `skip_restore_and_replacement: true` is set.

### Admin tools

`scripts/admin_tools_common.py` is the shared utilities module. It provides:
- `merge_runtime_config(repo_root, explicit_cfg)` — merges `validation_config.yaml` + `admin_tools_config.yaml` into a single flat dict; this is the config contract for all admin tools
- `fetch_agol_admin_rows(iso3, include_admin3)` — queries two AGOL FeatureServer REST endpoints live; requires internet; 40-second timeout
- `resolve_source_workbook(cfg)` — source file selection in `standard` mode (auto-picks latest matching `validated_questionnaire_{tool}_*.xlsx`) or `custom` mode (searches `custom_dir`, `validated_dir`, `working_dir`, repo root by filename)
- `detect_label_column(headers, language)` — finds the correct `label::Language (xx)` column index

`scripts/tool_admin_check.py` and `scripts/tool_admin_sync.py` each follow the same pattern: `main()` → `merge_runtime_config()` → `run(cfg: dict) → int`.

### Config system

**`configuration/validation_config.yaml`** — main config for the validators. The `config_profile` key can point to a YAML file (filename only, resolved under `output_dir/config_profiles/`, or absolute path) whose keys override the base config. This lets you switch country/language/round without editing the base file.

`languages_in_scope` (top level, both validators) limits the placeholder/replacement scans to the listed languages; other language columns stay in the file untouched and are not reported. Empty = every filled language. Replacement Issues rows are grouped per placeholder and cause (`build_unresolved_placeholder_issues` in KoBo, `_group_placeholder_issue_rows` in GeoPoll), so Q Name there can hold a comma-separated list.

**`configuration/admin_tools_config.yaml`** — config for the two admin tools. Falls back to `validation_config.yaml` for `tool`, `language`, `iso3` when those keys are absent. The `source:` and `sync:` blocks are admin-tool-specific.

**`configuration/critical_sets.yaml`** — GeoPoll only. Defines `exact_sets`, `min_count_sets`, and `crop_harvest` validation rules. Edit this file when the questionnaire structure changes; no code changes needed.

### Output naming

Reports: `report_{tool}_{lang}_{ISO3}_{timestamp}.xlsx`
Validated questionnaires: `validated_questionnaire_{tool}_{lang}_{ISO3}_{timestamp}.xlsx`
Config snapshots: `config_{tool}_{lang}_{ISO3}_{timestamp}.yaml`
Admin tool outputs: `admin_check_report_{source}_{timestamp}.xlsx`, `{source}_adminsync_{mode}_{timestamp}.xlsx`

All land in subfolders of `output_dir`: `kobo_output/` or `geopoll_output/` for validators, `admin_tools_output/` for admin tools.

### Streamlit UI (app/)

`app/` is an **additive** browser front end over the CLI above — a "Run Validation" page, a "Results Browser" page, and an "Admin Tools" page. It never imports `kobo_validator.py`/`geopoll_validator.py` (see Known gotchas below) and never imports `tool_admin_check.py`/`tool_admin_sync.py`/`tool_admin_parent_remap.py` either — every run it starts shells out exactly the way the `.bat` launchers do (`app/lib/subprocess_runner.py`). The CLI/`.bat` workflow is unchanged and works exactly as before whether or not `app/` is ever used.

- **Run Validation** writes changed fields back into the *tracked* `configuration/validation_config.yaml` — this is the only page that touches a tracked config file, because both validators read that exact path at module level with no override hook (see `_cfg_base_path` in each validator). It does so narrowly: `app/lib/config_io.py`'s `WRITABLE_KEYS` whitelist is the only set of dotted keys it will ever write, and it backs up the previous version to `configuration/.streamlit_backups/` before every save. Two different mechanisms depending on value type, not one — see the module docstring: scalar keys go through a comment-preserving `ruamel.yaml` round-trip (not `yaml.safe_dump`, which would destroy every comment in that heavily-documented file); list keys (e.g. `kobo_options.country_specific_list_names`) instead go through a small line-level text patcher (`_replace_list_lines`), because testing against the real file showed ruamel's round-trip silently drops comments adjacent to a block list whenever that list's *value* changes — even mutated in place — while leaving everything else untouched. One narrow, tested, purely-cosmetic residual on the ruamel side: a boolean written with non-canonical casing (`False`/`True` instead of `false`/`true`) gets normalized to lowercase on any save, even on an untouched key — semantically identical, never changes the parsed value.
- **Admin Tools** never edits the tracked `configuration/admin_tools_config.yaml`: it writes a throwaway full copy (base file + your overrides) and passes it via the `--config` flag the admin tools already support (`merge_runtime_config`), so the tracked file is untouched.
- **Results Browser** is read-only.

**Keeping the UI in sync when the validators/config change**: most config keys the UI shows are rendered generically from whatever is in the YAML, so adding/removing an ordinary key needs no UI change. The exceptions — enum choices not declared anywhere in YAML (`tool`, `language`, `reference_mode`, `source.mode`, `sync.mode`, `modality`), and the output file/sheet contract the Results Browser reads — are collected in one file, `app/config_schema.py`, whose docstring names exactly what to update. `smoke_test.py` imports its `REQUIRED_SHEETS`/`ISSUE_COLUMNS_REQUIRED` from that same file and cross-checks it against the live config on every `smoke_test` run, so drift between `app/config_schema.py` and reality fails the smoke test instead of silently going stale in the UI.

## Standard validation procedure (operators)

Country validations follow one standard loop, described for operators in `docs/agent/standard-procedure.md` and for the agent in the `diem-validate` skill (`.claude/skills/diem-validate/SKILL.md`): intake of the required inputs (file location, KoBo/GeoPoll, latest template or previous round, languages besides English — asked, never guessed) → run → summary message, Word document and cover email → re-validation of each new version against the open points → operator decisions (accepted / dropped, with who decided) → final package once nothing is open. Results are published in `output_dir` (`C:/Temp/DIEM_questionnaire_validation`), split into `geopoll_output/` and `kobo_output/`; case state lives in `<output_dir>/<tool>_output/validation_cases/<ISO3>_<round>/case.json` (`validation_case.py`). Housekeeping archives older reports/validated files, clears the agent scratch folder `_agent_runs/` after `delete_agent_run_files_after_days`, and never touches `validation_cases/`. At the start of a new case the agent first explains the steps to the operator in plain English. Keep the doc pages and the skill in step when the procedure changes.

## Documentation

The MkDocs site (`docs/`, nav in `mkdocs.yml`) is the user documentation; operators reach it through the agent via the `diem-docs` skill (answers from the pages, or `serve_docs.py` starts `mkdocs serve` and the page is opened in the browser pane — the site is served under `/DIEM_Questionnaire_Validation/` with `.html` page URLs). The "Working with the Agent" section (`docs/agent/`) is the operator guide. **Any change to the validators, the config keys, the skills or the procedure updates the matching pages in the same piece of work** (logic pages and `checks-and-severity.md` for issue types and severities, `getting-started.md` for config keys, `docs/agent/` for the procedure); `docs/function-reference/*` is only regenerated.

## Working approach

Before making any code change, describe the plan and wait for explicit confirmation. This applies to all edits — new functions, bug fixes, refactors, config changes. The only exception is when the user has explicitly said to go ahead.

## Code conventions

### Polars

Use native Polars patterns throughout. Prefer `pl.Expr`-based operations over row iteration or `.to_pandas()` conversions. Key patterns used in this codebase:

- Column operations are written as expressions: `pl.col("name").str.strip_chars().str.to_lowercase()`
- Aggregations use `group_by().agg()`, not loops
- Functions that operate on a column accept a `col_name: str` parameter and return `pl.Expr`, so callers can compose them — see `normalize_text_expr()`, `_normalized_list_expr()`, `_canonical_option_key_expr()` for the established pattern
- Use `df.filter()`, `df.with_columns()`, `df.join()` rather than conditional Python logic on rows
- Avoid `.to_dicts()` loops except for final output serialization

### Naming

Follow the verb-noun pattern established across both validators:

- `read_*` — load data from a file into a DataFrame or dict
- `compare_*` — take current and reference DataFrames, return a list of issue dicts
- `build_*` — construct a derived DataFrame or structure from inputs
- `normalize_*` / `_normalize_*` — return a cleaned/canonicalized value or `pl.Expr`
- `fetch_*` — retrieve data from an external source (network, AGOL)
- `detect_*` / `resolve_*` — find or determine something from available context
- `_` prefix for private helpers not meant to be called from outside their module

New functions doing the same class of work as an existing function should mirror its name. Check the existing function list before naming.

### Config over hardcoding

No hardcoded paths, column names, list names, country-specific values, or thresholds inside function bodies. These belong in:
- `configuration/validation_config.yaml` — runtime parameters and per-run settings
- `configuration/critical_sets.yaml` — GeoPoll structural rules
- `configuration/admin_tools_config.yaml` — admin tool parameters
- A new config file if neither of the above fits

Functions receive values from config as parameters. If a function needs a value that currently comes from a global `cfg` dict, pass it explicitly rather than reading `cfg` directly inside the function.

## Before adding or changing anything

The validators are large, tightly coupled scripts where a change in one place can silently break something downstream. Before implementing:

1. **Trace the data flow**: find where the value or structure you are changing is produced, then follow every place it is consumed. In `kobo_validator.py` and `geopoll_validator.py` this often spans hundreds of lines because they run top-to-bottom as scripts — a variable set in one section is read in a later section with no import boundary to signal the dependency.

2. **Check both validators**: KoBo and GeoPoll share concepts (module filtering, placeholder handling, output naming) but implement them separately. A change that makes sense for one may need a parallel change in the other, or may conflict with the other's existing logic.

3. **Check the output contract**: functions that return issue dicts must produce the exact columns (`check`, `status`, `details`, `severity`) that the report writer expects. Functions that produce DataFrames for comparison must preserve the column names that downstream `compare_*` functions join on.

4. **Check config-driven behavior**: if you change a function that reads from `cfg`, verify that all config keys it reads are documented in `validation_config.yaml` and that existing config files still work — no silent key renames.

5. **The placeholder pipeline is order-dependent**: steps 1–5 in `produce_validated_questionnaire()` must run in sequence. Adding a step or changing what a step writes to the workbook can corrupt the input to subsequent steps.

6. **Check the Streamlit UI**: if you change a config key enum (`tool`, `language`, `reference_mode`, `source.mode`, `sync.mode`, `modality`), a report/validated-questionnaire filename pattern, a required report sheet name, or an admin/validator CLI flag, update `app/config_schema.py` to match — see "Streamlit UI (app/)" above. Run `smoke_test` afterwards; it checks `app/config_schema.py` against the live config and will fail if it's now stale.

## Do not touch

- **The original files on SharePoint/OneDrive — never, for any reason.** Everything under `templates_source_dir` (DIEM Toolbox, `…/03. Toolbox/02. Questionnaires/`) and any country questionnaire the user shares from there is read-only: no edits, renames, moves, deletes or re-saves. Only *copy* them (e.g. `template_sync.py` into `templates_dir`, or staging into the scratchpad) and work on the copy.
- `docs/function-reference/kobo-validator.md` and `docs/function-reference/geopoll-validator.md` — auto-generated by `regenerate_function_docs.py`; regenerate after editing the validator scripts
- `site/` — MkDocs build output, not source
- `batch_output/` — runtime output, not tracked in git

## GeoPoll questionnaire conventions

### Question name prefixes

- `c_` prefix marks **custom questions** — questions the country team added or modified beyond the template. Option and code changes on `c_` questions are downgraded to `info` severity (expected customisation). This prefix replaced the legacy `o_` prefix; `o_` is still recognised for backward compatibility when validating against previous-round files.
- No prefix: standard mandatory or non-mandatory template question. All changes flagged at full severity.

### Rule-based validation checks (GeoPoll and KoBo)

These checks are config-driven via `configuration/critical_sets.yaml` and appear in the **Critical Sets** and **Summary** sheets of the report. Both validators implement them separately: KoBo reads `relevant` instead of Conditional for `agri_cs_check`, uses `kobo_values` / `kobo_codes` where KoBo choice names differ from GeoPoll codes, and takes `max_qname_length` / `modality` from `kobo_options`. Both also check `fixed_option_codes` and `tlu_weights`. KoBo recognises the `c_` custom prefix alongside the legacy `o_` (`CUSTOM_QNAME_PREFIXES`).

| Rule type | Config key | What it checks |
|---|---|---|
| `fs_indicators` | `critical_sets.yaml` → `fs_indicators` | Mandatory FS indicators (FIES, FCS, LCSI) must be present. CAPI ceiling applied when `modality=capi` in `validation_config.yaml`. |
| `agri_cs_check` | `critical_sets.yaml` → `agri_cs_check` | At least N CS questions must reference `hh_agricactivity` or `income_main/sec/third` with agri values in the Conditional column. |
| `variable_pairs` | `critical_sets.yaml` → `variable_pairs` | If one variable of a pair is present, both must be (e.g. `crp_harv_vol` + `crp_harv_unit`). |
| `qname_too_long` | `geopoll_options.max_qname_length` / `kobo_options.max_qname_length` in `validation_config.yaml` | Variable names exceeding the limit (default 28 GeoPoll, 32 KoBo) are flagged as medium. |

HDDS is no longer a `critical_set` — it is treated as a regular template question and checked via the standard question presence / mandatory comparison.

### Template header row auto-detection

`read_survey_sheet` detects whether the file has a banner row: if row 1 contains known column names (`varname_new`, `module`, etc.) it uses row 1 as headers. Older templates had a title/banner row above the headers on row 2. Both formats are handled automatically.

## Known gotchas

**Hidden Excel sheets**: `openpyxl` reads sheets with `sheet_state='hidden'` or `'veryHidden'` silently — `wb.sheetnames` includes them and `wb["Sheet Name"]` succeeds even though the tab is invisible in Excel. Always check `.sheet_state` if you need to distinguish user-visible from hidden sheets.

**Validator scripts are not importable**: `kobo_validator.py` and `geopoll_validator.py` execute config loading, AGOL fetches, and validation at module level. Never `import` them from another script. Call them via subprocess as `validate.py` does.

**Windows stdout encoding**: running Python scripts via `conda run` on Windows can cause `UnicodeEncodeError` (cp1252) when the script prints non-ASCII characters. Write output to a file and read it back if you need to capture output from a subprocess.

**`my_filter_sample` column**: during admin sync, this column controls sample-based filtering in the questionnaire. `preserve_my_filter_sample: true` (default) carries the original values into the rewritten rows. Do not remove this behavior.

**AGOL fetch is always live**: `fetch_agol_admin_rows()` has no caching. Every run of either admin tool hits the network. Do not add caching without considering that country admin hierarchies change between rounds.
