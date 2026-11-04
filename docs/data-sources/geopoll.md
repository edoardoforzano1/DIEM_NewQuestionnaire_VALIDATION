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
| `Mandatory` | `Mandatory` | One of seven categories: `yes - core`, `yes - panel`, `no - low priority`, `no - but recommended in applicable contexts`, `no - but recommended if of interest`, `spiel`, `customized`. |
| `Skip Pattern` | `Skip pattern` | Single routing column. (Older `Default skip patterns & conditional` / `Specify skip pattern variable` columns no longer exist in the current template — comparisons against those columns are dormant unless an old-format file is read.) |
| `Conditional` | `Conditional` | Inbound relevance gate — `variable = code(s)` referencing an *earlier* question, as opposed to `Skip Pattern`'s outbound routing. Checked for text changes plus (current-file only) broken variable references and invalid option codes. |
| `Universe` | `Universe` | Who the question is asked to — read and compared, but not used for skip-routing checks. |
| — | `To be asked to recent panelists (<6 months)?` | Read and carried through as data, but no longer cross-checked against `Mandatory`'s panel category — that check was removed (empirically the two columns are independent axes, not a consistency pair). |
| `English` / `French` / `Arabic` / ... | same | Question text plus numbered answer options (`1)label`, `2)label`, ...). Placeholders are replaced in each language column with that language's `Replacement (xx)` value. |
| `Local Language` | `Local Language` | Free column for an extra language or the country's own notes; placeholders are replaced there too. Not compared with the template. |
| `Q Type` | `Q Type` | Includes `Matrix Table` (template 20261007): one answer scale (options in the text) asked for several rows, listed as sub-variables in `varname_new_multiple`. |

Columns that existed in the older format but are absent from the current template (`Suggested Qname`, `Randomize`, `Programming Instructions`, `Core questions only`) are simply skipped — no error, but no comparison either.

## Other sheets

| Sheet | Used for |
|---|---|
| `Crop list` | the top-10 crops (`Select top 10 crops`), labels per language; expands the crop questions (`crp_all`, `crp_salesmain`…) with the selected crops first |
| `Additional information` | placeholder values (`Original` → `Replacement (EN/FR/AR…)`), in sections: core (mandatory), **Tropical Livestock Unit weights** (mandatory, one row per species — read as a table, not as placeholders), optional |
| `Admin 1 info`, `Admin 2 info` | admin lists; rebuilt from AGOL in the validated questionnaire |
| `Admin 3 info` | kept as supplied |
| `LoI estimation_weighted` | the template's own length estimate; the validator recomputes length from `Weighted duration` instead |

## GeoPoll Parsing Scope

- Question IDs and types.
- Mandatory markers.
- Module assignment per question.
- Text labels in selected language column, including numbered answer options.
- Codes and option structures.
- Skip/logic references.
- Universe and panelist-targeting metadata.

## Critical Rule Inputs

- `configuration/critical_sets.yaml`: exact sets, minimum counts, crop-harvest logic, FS indicators, agriculture-related coping strategies, variable pairs, fixed answer codes and TLU weights. See [GeoPoll Logic → Critical Sets](../workflow/geopoll-logic.md#2-critical-sets-sheet).
- `configuration/validation_config.yaml` → `geopoll_options`: name length, modality, derived placeholders, crop-list closing options.
