# Report issue guide (GeoPoll, template 20261007+)

What each issue type means, what the country team usually has to do, and the
known cases where it is noise. Use this to turn the report digest into a fix
list. Severity is the validator's; "Priority" is how to rank it in the fix list.

## Contents
1. Report sheets at a glance
2. Critical sets (structural rules from `configuration/critical_sets.yaml`)
3. Skip logic and conditionals
4. Question changes
5. Options and codes
6. Replacement issues (validated output)
7. Known template-side issues (not the country's fault)
8. DIEM design rules that are not automated

---

## 1. Report sheets at a glance

| Sheet | Answers the question |
|---|---|
| Summary | PASS/FAIL per rule family + counts + estimated LOI. Start here. |
| Critical Sets | Are the analytically required blocks there (FS indicators, CS counts, agri CS, wealth, crop harvest, TLU, fixed codes, variable pairs)? |
| Questionnaire Structure | Will the form route correctly (skip targets, conditionals, modules, duplicates, Q Types)? |
| Question Changes | Which template questions were removed/added/renamed/reworded, mandatory status, Universe. |
| Option Changes | Answer-option and Codes differences vs template. |
| Replacement Issues | Did placeholder replacement / crop expansion succeed in the validated output? |

## 2. Critical sets

| Issue type | Meaning | Typical fix | Priority |
|---|---|---|---|
| `fs_indicator_missing` | FIES, FCS or LCSI block absent | Restore the block from the template | Blocker |
| `fs_indicator_capi_excess` | CAPI with more than 4 FS indicators | Drop an optional indicator (HDDS/rCSI) | High |
| `agri_cs_count_insufficient` | Fewer than 4 coping strategies conditioned on agriculture (`hh_agricactivity` / `income_*` agri codes in Conditional) | Re-add agri CS from the template (`cs_stress_sold_more_animals`, `cs_crisis_harv_immat_crops`, `cs_crisis_consume_seed_stock`, …) or restore the Conditional on kept ones | Blocker (webinar rule: min 4 of 6) |
| min-count sets (`CS_stress`, `CS_crisis`, `CS_emergency`, `WEALTH`) | Below the minimum count by prefix | Add questions back | Blocker |
| `crop_harvest_violation` | Neither "minimal" nor "full" crop-harvest set | Keep only `crp_harv_change`, or the full set | High |
| `variable_pair_incomplete` | One half of a pair present (e.g. `crp_harv_vol` without `crp_harv_unit`; `ls_main_confirm` without `ls_main`) | Add the missing half | High |
| `fixed_codes_mismatch` | A dynamically-shown question lost its fixed codes (e.g. `ls_main_confirm` must be exactly 1-8, no DK/REF) | Restore the template option list | Blocker — GeoPoll would deliver position numbers |
| `tlu_weight_missing` / `_invalid` / `_inconsistent` | TLU weights blank, non-numeric, ≤ 0, or different per language column | Fill the TLU block of Additional information (weights agreed at planning) | Blocker (ls_main cannot be computed) |

Note: `WEALTH` counts `hh_wealth_*` **and** `c_hh_wealth_*`, so it passes when
core wealth questions are replaced by a custom one. If the country dropped
`hh_wealth_water/toilet/light` (core), say so explicitly in the fix list even
though the set is PASS.

## 3. Skip logic and conditionals

Template Skip pattern cells are a *menu*: `go to optional question [A / B] OR C`.
The country keeps the path matching the questions it kept. The validator
accepts any kept optional target in place of the default.

| Issue type | Meaning | Typical fix | Priority |
|---|---|---|---|
| `skipPattern_invalid_qname` | Routes to a variable that is not in the questionnaire | Rename to the real variable (common: forgot the `c_` prefix, legacy `o_` prefix, template renamed the target) or route to the next kept question | Blocker |
| `skipPattern_invalid_qnameCategory` | Optional slot routes to a mandatory question or vice versa | Fix target | High |
| `skipPattern_range_invalid` | Skip references option codes that do not exist | Fix codes | Blocker |
| `skipPattern_changes` / `_range_mismatch` (info) | Different routing but valid | Read once; usually the country's choice | Low |
| `conditional_invalid_qname` / `conditional_range_invalid` | Conditional refers to a missing variable / code | Fix reference | Blocker |
| `conditional_removed_mandatory` | A mandatory question lost its Conditional | Restore it (otherwise asked to everyone) | High |

A target the country dropped is **not** flagged when it is one of the "OR"
alternatives of a rule and another alternative is kept (e.g. "go to
crp_harv_storage OR crp_harv_consume" without crp_harv_storage): the rule
already allows either. Names that exist in neither file are still flagged.

Each `skipPattern_invalid_qname` row now says what happened to the missing target:
- *renamed to custom question c_X* → use the `c_` name in the skip text;
- *removed by the country* → restore the target (if core) or re-route to the next kept question;
- *not defined in the reference either* → outdated name copied from the template skip text
  (e.g. `confl_fs_imp`, renamed `confl_fs` in 20261007). Country fix: use the closest existing
  variable given; also list it under template-side issues.

## 4. Question changes

| Issue type | Meaning | Typical fix |
|---|---|---|
| `removed_question` high | A core/spiel question removed | Restore, or get documented approval (RA + SMAR) |
| `removed_question` info | Optional question removed | Nothing — allowed choice |
| `mandatory_to_optional` | Core question now optional, often because it was renamed `c_<name>` | Keep the template name for core questions; `c_` is only for genuinely custom questions |
| `added_question` info | New `c_` question | Check it has Universe, Skip pattern, Duration; country must document processing specs. Country-added questions take `c_` in the name and Mandatory = `customized` (confirmed by SMAR) |
| `mandatory_category_unrecognized` medium | Mandatory value not in the template categories (`customized` counts as valid) | Usually a typo; for a country-added question set `customized` |
| `question_label_mismatch` medium | Text differs from template (after normalisation; Arabic orthography is folded) | Confirm wording change is intended / translation approved |
| `universe_changed` | Audience text changed; info when the template cell was blank | Confirm |
| `module_removed` | Info when the module had only optional questions; high if it contained core questions | Restore core modules |

## 5. Options and codes

| Issue type | Meaning | Priority |
|---|---|---|
| `added_option` / `removed_option` / `*_with_drift` | Option list changed; *drift* = codes shift for every following option → breaks comparability and skip codes | High when drift on a core question |
| `option_label_mismatch` | Label wording differs | Medium; Arabic hamza/alef spelling is already ignored |
| `codes_*` | Sub-variable names (`varname_new_multiple`) differ from template | High for core — variable names feed the master table |
| `codes_option_count_mismatch` | Number of options ≠ number of sub-variable codes (not checked for Matrix Table) | High |

## 6. Replacement issues (validated output)

| Issue type | Meaning | Typical fix |
|---|---|---|
| `replacement_missing_key` | A `$KEY$` in a kept question has no value in Additional information | Fill the row in Additional information (the right language column) |
| `replacement_malformed_placeholder` | `$` and `#` mixed (e.g. `$ADM1#`) or unbalanced `$` | Fix delimiters: `$KEY$` = Additional information value, `#VAR#` = runtime variable filled by GeoPoll |
| `replacement_unresolved_placeholder` | Token still in output although a value exists | Usually a spelling variant of the key — align the spelling |
| `replacement_crop_selection_mismatch` | Not exactly 10 crops marked in Crop list | Mark exactly 10 |

Derived placeholders: `$MAX DIGIT DK$` / `$MAX DIGIT REF$` are computed from
`MAX AMOUNT` (8s / 9s, same digit count) via
`geopoll_options.derived_placeholders` — not typed by the country. If
`MAX AMOUNT` is blank they stay unresolved.

KoBo, done by DIEM in the validated questionnaire (nothing to ask the country;
the `choices` sheet is locked for them — SMAR, Nov 2026):
- **No local land unit**: `local measurement unit` blank in Additional
  information → `landsize_unit` option 5 (`#local measurement units#`) is
  deleted automatically (`kobo_options.drop_choices_when_additional_info_blank`).
  Do not raise it as a point; the blank `local measurement unit` rows are fine.
- **Unused languages**: language columns outside the case languages and the
  no-language `label::` columns are removed automatically
  (`kobo_options.drop_unused_language_columns`).
- **Label wording on a locked sheet** (e.g. a French crop name the country
  prefers, "Gombo" for okra): agreed with SMAR if the code is unchanged, then
  changed by DIEM in the final validated file.

## 7. Known template-side issues (not the country's fault)

Report these separately ("template issue — raise with SMAR/Renzi"), not as
country fixes:
- `id_panel` Arabic text contains `$ADM1#` / `$ADMIN2 AR#` in the stored cell value (template 20261007).
- Skip patterns of `confl_insec`, `confl_insec_res`, `confl_agri_imp` route to `confl_fs_imp`, which the template renamed `confl_fs`.
- `lcsi_intro` note says "4 agriculture-based CS out of the 6 available", but only 5 template CS carry an agriculture Conditional (`cs_stress_sold_more_animals`, `cs_crisis_harv_immat_crops`, `cs_crisis_consume_seed_stock`, `cs_crisis_decrease_input_exp`, `cs_emergency_sold_last_fem`); the AGRI_CS rule counts by Conditional, so it sees 5.
- Arabic text: `cs_crisis_decrease_input_exp` has "والأعلاف والأعلاف"; `crp_harv_vol` / `crp_harv_lastyr` keep "threshed" and `econshock_ls_dif` keeps "destocking" in English.
- If a removal/rename is flagged on *every* country, compare against the template first — the template may have changed.

## 8. DIEM design rules not (fully) automated

From the "New Household Questionnaire" webinar / SOPs — check manually and mention when relevant:
- Interview length: core + recommended ≤ 30 min before any low-priority question is added; total target ~20–25 min. `check_validated_output.py` reports both.
- Low-priority questions need a clear analytical purpose (relevance, analytical value, non-redundancy, time).
- Admin 3 should be collected where possible; Admin 4 optional.
- Recent-panelist logic: static questions marked "no" in *To be asked to recent panelists* can be skipped for recent panelists.
- Questions added outside the template need explicit processing specifications from the country team.
- Dynamic option lists (`ls_main_confirm`, `need_type_rank_*`): GeoPoll must keep the fixed codes, not list positions.
- Decisions must be documented and validated by RA, SMAR team and DIEM management.
