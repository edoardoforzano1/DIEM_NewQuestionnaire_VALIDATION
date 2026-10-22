# Streamlit UI

A browser front end over the CLI commands (`validate`, `tool_admin_check`, `tool_admin_sync`, `tool_admin_parent_remap`). It is additive: launching it never changes how those commands behave, and nothing here is required to run the pipeline — every page shells out to the exact same scripts the `.bat` launchers call.

```powershell
streamlit_ui
```

Opens at `http://localhost:8501/`. Requires the `diem-validation` conda environment (same as every other command in this repo) — it adds `streamlit` and `ruamel.yaml` as dependencies.

---

## Run Validation

A form for the fields in `configuration/validation_config.yaml`, followed by a live log of the run.

1. Fill in the form (tool, working dir, questionnaire file, language, ISO3, reference mode, module lists, tool-specific options, housekeeping, report metadata).
2. Click **Prepare run** — nothing is written yet. A diff of exactly what would change in `configuration/validation_config.yaml` is shown.
3. Click **Confirm & write config + run** to save and launch `validate.py`.

### What this writes to disk

Both validators read `configuration/validation_config.yaml` directly at module level — there is no way to point them at a different file — so this page does update that tracked file. It does so narrowly:

- Only the fields shown in the form are ever changed; every other line, and every one of the file's extensive inline comments, is left exactly as it was.
- A timestamped backup is written to `configuration/.streamlit_backups/` before every save.
- If `config_profile` is currently set, the page warns you — a profile's keys are applied *after* this form's values when `validate.py` runs, so it can override what you just set. You can clear it for the run from a checkbox.

`validate.py` itself, and the KoBo/GeoPoll validator scripts, run completely unmodified.

## Results Browser

Read-only. Pick a tool and browse `report_*` / `validated_questionnaire_*` files under `output_dir/<tool>_output/`, newest first:

- Preview any sheet of a report as a table, with a severity filter where a `severity` column is present.
- Download the report or validated questionnaire as-is.

## Admin Tools

Runs `tool_admin_check`, `tool_admin_sync`, or `tool_admin_parent_remap`, live, with the same source-selection fields documented in [Admin Tools](admin-tools.md). Every run still hits AGOL live — there is no caching, same as the CLI.

This page never edits the tracked `configuration/admin_tools_config.yaml`. It writes a throwaway full copy (the tracked file plus your overrides from the form) and passes it to the tool with the `--config` flag the admin tools already support.

---

## What it never does

- Never imports `kobo_validator.py`, `geopoll_validator.py`, or any `tool_admin_*.py` script — every run is a subprocess, exactly like the `.bat` launchers.
- Never edits `configuration/admin_tools_config.yaml`.
- Never edits any part of `configuration/validation_config.yaml` outside the fields shown on the Run Validation form.
