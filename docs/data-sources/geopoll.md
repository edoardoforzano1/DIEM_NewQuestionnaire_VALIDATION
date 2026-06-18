# GeoPoll Inputs

## Minimum Required Inputs

- GeoPoll questionnaire workbook with a `survey` sheet (current template: one banner row, then headers on row 2).
- Config with enumerator language/ISO context.

## Key GeoPoll Survey Columns

The current template column names differ from the raw header names used internally — `read_survey_sheet()` resolves aliases automatically.

| Internal name | Source column | Notes |
|---|---|---|
| `Q Name` | `varname_new` | Question identifier, used in skip patterns and data joins. |
| `Codes` | `varname_new_multiple` | For Select All That Apply questions: numbered sub-codes (`1)token`, `2)token`, ...). Identical to `varname_new` for non-multi questions. |
| `module` | `module` | Per-row module code (e.g. `resp_info`, `shock`). Blank on section-divider rows — this is how the validator tells a divider row apart from a real question. |
| `Mandatory` | `Mandatory` | One of six categories: `yes - core`, `yes - panel`, `no - low priority`, `no - but recommended in applicable contexts`, `no - but recommended if of interest`, `spiel`. |
| `Skip Pattern` | `Skip pattern` | Single routing column. (Older `Default skip patterns & conditional` / `Specify skip pattern variable` columns no longer exist in the current template — comparisons against those columns are dormant unless an old-format file is read.) |
| `Universe` | `Universe` | Who the question is asked to — read and compared, but not used for skip-routing checks. |
| — | `To be asked to recent panelists (<6 months)?` | Cross-checked against `Mandatory`'s panel category for consistency. |
| `English` / `French` / ... | same | Question text plus numbered answer options (`1)label`, `2)label`, ...). |

Columns that existed in the older format but are absent from the current template (`Suggested Qname`, `Randomize`, `Programming Instructions`, `Core questions only`) are simply skipped — no error, but no comparison either.

## GeoPoll Parsing Scope

- Question IDs and types.
- Mandatory markers.
- Module assignment per question.
- Text labels in selected language column, including numbered answer options.
- Codes and option structures.
- Skip/logic references.
- Universe and panelist-targeting metadata.

## Critical Rule Inputs

- `configuration/critical_sets.yaml` for exact sets, minimum counts, and crop-harvest logic.
