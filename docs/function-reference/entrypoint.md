# Entrypoint (`validate.py`)

## Main Responsibility

- Load centralized config.
- Resolve optional config profile overlay.
- Validate `tool` value.
- Run configured output housekeeping before validation.
- Dispatch execution to the selected validator script.

## Main Function

- `main()` controls all dispatch behavior.
- `run_output_housekeeping()` applies retention limits and optional archive
  purging for reports, validated files, and config snapshots.

## Dispatch Map

- `geopoll` -> `scripts/geopoll_validator.py`
- `kobo` -> `scripts/kobo_validator.py`
