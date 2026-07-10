# Report Output Overview

## Output Locations

- KoBo reports: `<output_dir>/kobo_output/`
- GeoPoll reports: `<output_dir>/geopoll_output/`

## Typical Files

- `report_kobo_<lang>_<iso3>_...xlsx`
- `report_geopoll_<lang>_<iso3>_...xlsx`
- `validated_questionnaire_kobo_<lang>_<iso3>_...xlsx`
- `validated_questionnaire_geopoll_<lang>_<iso3>_...xlsx`

When output housekeeping is enabled, older files beyond the configured
per-group limits, or older than `archive_older_than_days` (if set), are
archived or deleted before the next validation starts.

## Color Semantics

- Red: High severity
- Orange: Medium severity
- Blue: Info
- Green: Pass

Go to the next pages for per-tool sheet details and image placeholders.
