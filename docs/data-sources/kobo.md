# KoBo Inputs

## Minimum Required Inputs

- Questionnaire XLSX with at least `survey` and `choices` sheets.
- Config with correct `language`, `iso3`, and `reference_mode`.

## Important KoBo Columns

### survey

The current template has a draft-warning banner in row 1, with the actual XLSForm headers on row 2 — the validator scans for the header row (the first row containing both `type` and `name`) rather than assuming row 1, so older single-row-header files still work too.

- `type`
- `name`
- `required`
- `relevant`
- language label columns (`label::...`)
- language hint columns (`hint::...`) — resolved the same way as labels, falling back to a plain `hint` column for older files.
- `Mandatory` — custom tracking column (`yes - core`, `yes - panel`, `no - low priority`, `spiel`).

### choices

- `list_name`
- `name`
- language label columns

## Optional but Operationally Important

- `Crop list` sheet for crop options.
- `Additional information` replacements for placeholder resolution, including `$ADMIN1$`–`$ADMIN4$` tokens.

!!! note "admin4"
    The current template adds a fourth administrative level (`adm4_pcode`), but there is no AGOL admin4 boundary list available yet — admin4 choices are not fetched or rebuilt. This is a known gap, not a bug.
