# KoBo Validator (`C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py`)

This page is organized by the validator pipeline stages used in the script.
Use the stage map to navigate quickly, then open each function spec for parameters and full source.

Total functions documented: **233**

## Pipeline Function Map

### 1. Runtime and logger helpers

- [`_NullOutput.write`](#fn-write-17)
- [`_NullOutput.flush`](#fn-flush-18)
- [`_NullOutput.fileno`](#fn-fileno-19)
- [`_banner`](#fn--banner-25)
- [`_info`](#fn--info-37)
- [`_step`](#fn--step-41)
- [`_summary`](#fn--summary-50)

### 2. Step 1 -- Configuration

- [`_load_effective_config`](#fn--load-effective-config-120)

### 3. Step 2 -- Reference file resolution

- [`_write_config_snapshot_kobo`](#fn--write-config-snapshot-kobo-202)
- [`find_kobo_template`](#fn-find-kobo-template-230)
- [`find_kobo_template._has_lang_token`](#fn--has-lang-token-239)
- [`find_kobo_template._date_key`](#fn--date-key-249)
- [`_reference_scope_label`](#fn--reference-scope-label-292)
- [`_extract_round_token_kobo`](#fn--extract-round-token-kobo-299)
- [`_reference_descriptor_kobo`](#fn--reference-descriptor-kobo-314)
- [`_language_scope_descriptor_kobo`](#fn--language-scope-descriptor-kobo-326)
- [`_not_in_reference_text`](#fn--not-in-reference-text-334)
- [`_as_bool`](#fn--as-bool-338)

### 4. Step 3 -- Readers

- [`_custom_qname_expr`](#fn--custom-qname-expr-387)
- [`_core_qname_expr`](#fn--core-qname-expr-392)
- [`_custom_variants`](#fn--custom-variants-401)
- [`_normalize_survey_type_token`](#fn--normalize-survey-type-token-407)
- [`_find_label_col`](#fn--find-label-col-411)
- [`_find_hint_col`](#fn--find-hint-col-426)
- [`_find_xlsform_header_row_idx`](#fn--find-xlsform-header-row-idx-436)
- [`_find_ws_header_row_1based`](#fn--find-ws-header-row-1based-446)
- [`_choices_header_key`](#fn--choices-header-key-465)
- [`_choices_header_concept`](#fn--choices-header-concept-469)
- [`_resolve_choices_output_headers`](#fn--resolve-choices-output-headers-476)
- [`_remap_choices_row_to_headers`](#fn--remap-choices-row-to-headers-494)
- [`_read_choices_headers_from_workbook`](#fn--read-choices-headers-from-workbook-533)
- [`_normalize_list_token`](#fn--normalize-list-token-558)
- [`_normalize_module_token`](#fn--normalize-module-token-569)
- [`_extract_select_list_name_from_type`](#fn--extract-select-list-name-from-type-576)
- [`_canonical_option_name_token`](#fn--canonical-option-name-token-601)
- [`_normalized_list_expr`](#fn--normalized-list-expr-615)
- [`_normalize_mandatory`](#fn--normalize-mandatory-619)
- [`read_kobo_survey`](#fn-read-kobo-survey-632)
- [`read_kobo_survey.get`](#fn-get-662)
- [`read_kobo_choices`](#fn-read-kobo-choices-761)
- [`read_kobo_choices.get`](#fn-get-778)
- [`build_question_options`](#fn-build-question-options-796)
- [`_normalized_module_expr`](#fn--normalized-module-expr-857)
- [`_resolve_module_keys_from_tokens`](#fn--resolve-module-keys-from-tokens-861)
- [`_filter_survey_by_module_keys`](#fn--filter-survey-by-module-keys-899)
- [`_module_display_map`](#fn--module-display-map-910)
- [`_collect_skip_module_payload`](#fn--collect-skip-module-payload-925)
- [`_dedupe_keep_order`](#fn--dedupe-keep-order-965)
- [`_format_module_scope_for_display`](#fn--format-module-scope-for-display-980)

### 5. Step 4 -- Load files

- [`_normalize_languages_in_scope`](#fn--normalize-languages-in-scope-1049)

### 6. Step 4b -- Placeholder normalization

- [`_normalize_additional_info_header`](#fn--normalize-additional-info-header-1167)
- [`_additional_info_replacement_indexes`](#fn--additional-info-replacement-indexes-1171)
- [`_placeholder_aliases`](#fn--placeholder-aliases-1188)
- [`read_additional_info_all_languages`](#fn-read-additional-info-all-languages-1204)
- [`read_additional_info_with_status`](#fn-read-additional-info-with-status-1252)
- [`read_additional_info`](#fn-read-additional-info-1348)
- [`restore_to_vanilla`](#fn-restore-to-vanilla-1353)
- [`apply_replacements`](#fn-apply-replacements-1395)
- [`read_crop_choice_rows_for_compare_with_status`](#fn-read-crop-choice-rows-for-compare-with-status-1421)
- [`read_crop_choice_rows_for_compare`](#fn-read-crop-choice-rows-for-compare-1503)
- [`fetch_admin_choice_rows_for_compare`](#fn-fetch-admin-choice-rows-for-compare-1508)
- [`replace_choice_lists_for_compare`](#fn-replace-choice-lists-for-compare-1565)
- [`_add_replacement_input_issue`](#fn--add-replacement-input-issue-1601)
- [`_count_hash_placeholders_in_text_df`](#fn--count-hash-placeholders-in-text-df-1625)

### 7. Step 5 -- Normalisation helpers

- [`normalize_text_expr`](#fn-normalize-text-expr-1882)
- [`normalize_simple_expr`](#fn-normalize-simple-expr-1892)
- [`normalize_logic_expr`](#fn-normalize-logic-expr-1901)

### 8. Step 6 -- Comparison functions

- [`compare_question_presence`](#fn-compare-question-presence-1916)
- [`compare_mandatory_kobo`](#fn-compare-mandatory-kobo-1932)
- [`validate_mandatory_category_unrecognized`](#fn-validate-mandatory-category-unrecognized-1970)
- [`compare_list_name_changes`](#fn-compare-list-name-changes-2000)
- [`compare_question_labels`](#fn-compare-question-labels-2030)
- [`compare_constraint_changes`](#fn-compare-constraint-changes-2192)
- [`validate_constraint_removed_for_mandatory`](#fn-validate-constraint-removed-for-mandatory-2249)
- [`compare_required_changes`](#fn-compare-required-changes-2304)
- [`compare_choice_filter_changes`](#fn-compare-choice-filter-changes-2341)
- [`compare_appearance_changes`](#fn-compare-appearance-changes-2378)
- [`compare_calculation_changes`](#fn-compare-calculation-changes-2415)
- [`_normalize_qtype_value_kobo`](#fn--normalize-qtype-value-kobo-2453)
- [`_qtype_mode_kobo`](#fn--qtype-mode-kobo-2467)
- [`_is_known_qtype_value_kobo`](#fn--is-known-qtype-value-kobo-2503)
- [`_qtype_change_severity_kobo`](#fn--qtype-change-severity-kobo-2514)
- [`compare_type_changes`](#fn-compare-type-changes-2569)
- [`_canonical_option_key_expr`](#fn--canonical-option-key-expr-2647)
- [`compare_option_labels_single`](#fn-compare-option-labels-single-2652)
- [`compare_option_presence_single`](#fn-compare-option-presence-single-2689)
- [`compare_option_name_renumber_single`](#fn-compare-option-name-renumber-single-2733)
- [`compare_hint_changes`](#fn-compare-hint-changes-2816)

### 9. Step 7 -- Relevant validation (KoBO skip logic)

- [`_has_broken_hash_placeholder_token`](#fn--has-broken-hash-placeholder-token-2859)
- [`_has_malformed_kobo_ref_token`](#fn--has-malformed-kobo-ref-token-2880)
- [`validate_relevant`](#fn-validate-relevant-2895)
- [`validate_choice_label_language_completeness`](#fn-validate-choice-label-language-completeness-2977)
- [`validate_questionnaire_structure`](#fn-validate-questionnaire-structure-3038)
- [`_module_rows_from_survey`](#fn--module-rows-from-survey-3252)
- [`validate_module_presence`](#fn-validate-module-presence-3307)
- [`_attach_module_column_to_issues`](#fn--attach-module-column-to-issues-3377)
- [`_attach_module_column_to_issues._lookup_part`](#fn--lookup-part-3394)
- [`_attach_module_column_to_issues._lookup_part_en`](#fn--lookup-part-en-3409)

### 10. Step 8 -- Critical sets

- [`validate_critical_sets`](#fn-validate-critical-sets-3490)
- [`validate_critical_sets._wealth_optional_variants`](#fn--wealth-optional-variants-3514)
- [`validate_prefix_counts`](#fn-validate-prefix-counts-3561)
- [`validate_crop_harvest`](#fn-validate-crop-harvest-3592)
- [`_rule_issues_df`](#fn--rule-issues-df-3647)
- [`_indicator_present`](#fn--indicator-present-3651)
- [`validate_fs_indicators`](#fn-validate-fs-indicators-3662)
- [`_agri_signal_patterns_kobo`](#fn--agri-signal-patterns-kobo-3714)
- [`validate_agri_cs_count`](#fn-validate-agri-cs-count-3736)
- [`validate_variable_pairs`](#fn-validate-variable-pairs-3776)
- [`_code_sort_key`](#fn--code-sort-key-3804)
- [`validate_fixed_option_codes`](#fn-validate-fixed-option-codes-3808)
- [`read_tlu_weights`](#fn-read-tlu-weights-3853)
- [`validate_tlu_weights`](#fn-validate-tlu-weights-3897)
- [`validate_tlu_weights._issue`](#fn--issue-3915)
- [`validate_qname_length`](#fn-validate-qname-length-3950)

### 11. Step 9 -- Issue unifiers

- [`make_presence_issues`](#fn-make-presence-issues-3974)
- [`make_mandatory_issues`](#fn-make-mandatory-issues-4075)
- [`make_option_issues`](#fn-make-option-issues-4088)
- [`make_option_presence_issues`](#fn-make-option-presence-issues-4101)
- [`make_option_name_renumber_issues`](#fn-make-option-name-renumber-issues-4121)
- [`merge_option_issue_views_en_target`](#fn-merge-option-issue-views-en-target-4135)
- [`classify_choice_name_root_causes`](#fn-classify-choice-name-root-causes-4193)
- [`classify_choice_name_root_causes._is_numeric_name`](#fn--is-numeric-name-4316)
- [`classify_choice_name_root_causes._name_sort_key`](#fn--name-sort-key-4319)
- [`classify_choice_name_root_causes._uniq`](#fn--uniq-4325)
- [`classify_choice_name_root_causes._join_limited`](#fn--join-limited-4336)
- [`classify_choice_name_root_causes._join_names`](#fn--join-names-4344)
- [`classify_choice_name_root_causes._format_choice_list`](#fn--format-choice-list-4353)
- [`classify_mandatory_choice_set_replaced`](#fn-classify-mandatory-choice-set-replaced-4619)
- [`classify_mandatory_choice_set_replaced._name_sort_key`](#fn--name-sort-key-4750)
- [`classify_mandatory_choice_set_replaced._uniq`](#fn--uniq-4756)
- [`classify_mandatory_choice_set_replaced._join_names`](#fn--join-names-4767)
- [`classify_mandatory_choice_set_replaced._format_choice_list`](#fn--format-choice-list-4776)
- [`collapse_cluster_ea_option_changes`](#fn-collapse-cluster-ea-option-changes-4870)
- [`_join_tokens_limited`](#fn--join-tokens-limited-4919)
- [`_format_collapsed_choice_side`](#fn--format-collapsed-choice-side-4935)
- [`_format_choice_entries`](#fn--format-choice-entries-4950)
- [`_build_choice_lookup`](#fn--build-choice-lookup-4980)
- [`_collapsed_choice_detail`](#fn--collapsed-choice-detail-5009)
- [`_ordered_unique_names`](#fn--ordered-unique-names-5027)
- [`_ordered_added_removed_names`](#fn--ordered-added-removed-names-5040)
- [`merge_added_removed_choice_rows`](#fn-merge-added-removed-choice-rows-5072)
- [`collapse_choice_issue_rows_by_key`](#fn-collapse-choice-issue-rows-by-key-5197)
- [`collapse_choice_issue_rows_by_key._filter_choice_entries_by_names`](#fn--filter-choice-entries-by-names-5227)
- [`suppress_enumerator_option_details`](#fn-suppress-enumerator-option-details-5370)
- [`suppress_enumerator_option_details._split`](#fn--split-5391)
- [`suppress_structural_choice_label_noise`](#fn-suppress-structural-choice-label-noise-5451)
- [`suppress_structural_choice_label_noise._norm_lbl`](#fn--norm-lbl-5499)
- [`suppress_structural_choice_label_noise._name_to_label`](#fn--name-to-label-5502)

### 12. Step 10 -- Run pipeline

- [`_dedupe_questions_for_compare`](#fn--dedupe-questions-for-compare-5576)
- [`_with_choice_cols`](#fn--with-choice-cols-5940)

### 13. Step 11 -- Export

- [`_hdr`](#fn--hdr-6264)
- [`_sect`](#fn--sect-6271)
- [`_style_row`](#fn--style-row-6278)
- [`_autofit`](#fn--autofit-6286)
- [`_ensure_column_widths_from_header`](#fn--ensure-column-widths-from-header-6292)
- [`_action_for_issue_type`](#fn--action-for-issue-type-6368)
- [`_col_map_with_field_header`](#fn--col-map-with-field-header-6400)
- [`_prepare_table_df`](#fn--prepare-table-df-6412)
- [`_resolve_table_cols`](#fn--resolve-table-cols-6422)
- [`_table`](#fn--table-6454)
- [`_tokenize_for_word_diff`](#fn--tokenize-for-word-diff-6476)
- [`_coalesce_segments`](#fn--coalesce-segments-6489)
- [`_build_diff_segments`](#fn--build-diff-segments-6501)
- [`_set_rich_text`](#fn--set-rich-text-6520)
- [`_set_rich_text_with_bold_tokens`](#fn--set-rich-text-with-bold-tokens-6536)
- [`_apply_inline_diff_for_issue`](#fn--apply-inline-diff-for-issue-6574)
- [`_apply_inline_diff_for_issue._match_issue`](#fn--match-issue-6588)
- [`_apply_choice_detail_highlights`](#fn--apply-choice-detail-highlights-6615)
- [`_with_lang_scope_tag`](#fn--with-lang-scope-tag-6667)
- [`_question_change_expr`](#fn--question-change-expr-6741)
- [`_ensure_question_field_detail`](#fn--ensure-question-field-detail-6745)
- [`_normalise_qtype_for_summary`](#fn--normalise-qtype-for-summary-6779)
- [`_grouped_table`](#fn--grouped-table-6808)
- [`write_summary_sheet`](#fn-write-summary-sheet-6846)
- [`write_summary_sheet._set_row`](#fn--set-row-6907)
- [`write_summary_sheet._check_row`](#fn--check-row-6988)
- [`write_critical_sets_sheet`](#fn-write-critical-sets-sheet-7106)
- [`write_questionnaire_structure_sheet`](#fn-write-questionnaire-structure-sheet-7132)
- [`write_replacement_issues_sheet`](#fn-write-replacement-issues-sheet-7190)
- [`write_relevant_sheet`](#fn-write-relevant-sheet-7221)
- [`write_question_changes_sheet`](#fn-write-question-changes-sheet-7231)
- [`write_option_changes_sheet`](#fn-write-option-changes-sheet-7285)
- [`export_report`](#fn-export-report-7308)

### 14. Step 12 -- Validated questionnaire output

- [`_crop_label_idx`](#fn--crop-label-idx-7373)
- [`_read_crop_choices`](#fn--read-crop-choices-7387)
- [`_merge_crop_rows_for_multilang`](#fn--merge-crop-rows-for-multilang-7470)
- [`_fetch_admin_choices`](#fn--fetch-admin-choices-7534)
- [`_fetch_admin_choices._get`](#fn--get-7544)
- [`_fetch_admin3_choices`](#fn--fetch-admin3-choices-7565)
- [`_rebuild_choices_sheet`](#fn--rebuild-choices-sheet-7588)
- [`_rebuild_choices_sheet._row_values`](#fn--row-values-7616)
- [`_rebuild_choices_sheet._row_styles`](#fn--row-styles-7622)
- [`_rebuild_choices_sheet._norm_key`](#fn--norm-key-7659)
- [`_rebuild_choices_sheet._is_empty`](#fn--is-empty-7662)
- [`_rebuild_choices_sheet._remember_sample`](#fn--remember-sample-7669)
- [`_rebuild_choices_sheet._is_blank`](#fn--is-blank-7684)
- [`_strip_skipped_module_blocks_from_survey_sheet`](#fn--strip-skipped-module-blocks-from-survey-sheet-7852)
- [`_strip_skipped_module_blocks_from_survey_sheet._cell`](#fn--cell-7893)
- [`_remove_choices_lists_rows`](#fn--remove-choices-lists-rows-7950)
- [`_remove_choices_lists_rows._cell`](#fn--cell-7972)
- [`_detect_kobo_header_language`](#fn--detect-kobo-header-language-7996)
- [`_apply_replacements_to_wb`](#fn--apply-replacements-to-wb-8020)
- [`_restore_placeholder_tokens_from_template`](#fn--restore-placeholder-tokens-from-template-8058)
- [`_restore_placeholder_tokens_from_template._norm_txt`](#fn--norm-txt-8085)
- [`_restore_placeholder_tokens_from_template._can_restore_template_value`](#fn--can-restore-template-value-8094)
- [`_count_choices_list_rows`](#fn--count-choices-list-rows-8230)
- [`_choices_header_index_map`](#fn--choices-header-index-map-8242)
- [`_count_blank_labels_for_lists`](#fn--count-blank-labels-for-lists-8253)
- [`_validate_admin_parent_links_in_choices_sheet`](#fn--validate-admin-parent-links-in-choices-sheet-8276)
- [`_highlight_admin_parent_issue_rows_in_choices_sheet`](#fn--highlight-admin-parent-issue-rows-in-choices-sheet-8361)
- [`_write_admin_parent_mismatch_text_report`](#fn--write-admin-parent-mismatch-text-report-8394)
- [`_choices_has_language_col`](#fn--choices-has-language-col-8432)
- [`_crop_list_has_language_col`](#fn--crop-list-has-language-col-8450)
- [`_normalize_choice_text_token`](#fn--normalize-choice-text-token-8467)
- [`_choice_pair_set_by_list`](#fn--choice-pair-set-by-list-8474)
- [`_choice_pair_set_from_rows`](#fn--choice-pair-set-from-rows-8490)
- [`_choice_code_set_by_list`](#fn--choice-code-set-by-list-8504)
- [`_choice_code_set_from_rows`](#fn--choice-code-set-from-rows-8518)
- [`_fmt_choice_pairs`](#fn--fmt-choice-pairs-8530)
- [`_fmt_choice_pairs._sort_key`](#fn--sort-key-8531)
- [`_fmt_choice_codes`](#fn--fmt-choice-codes-8546)
- [`_column_language`](#fn--column-language-8560)
- [`_column_in_scope`](#fn--column-in-scope-8569)
- [`_sheet_scope_mask`](#fn--sheet-scope-mask-8577)
- [`read_additional_info_keys`](#fn-read-additional-info-keys-8582)
- [`build_unresolved_placeholder_issues`](#fn-build-unresolved-placeholder-issues-8607)
- [`_scan_unresolved_placeholders`](#fn--scan-unresolved-placeholders-8676)
- [`_collect_unresolved_placeholder_cells`](#fn--collect-unresolved-placeholder-cells-8699)
- [`_scan_malformed_placeholder_syntax`](#fn--scan-malformed-placeholder-syntax-8745)
- [`produce_validated_questionnaire`](#fn-produce-validated-questionnaire-8773)
- [`produce_validated_questionnaire._add_row`](#fn--add-row-8805)
- [`produce_validated_questionnaire._add_issue`](#fn--add-issue-8813)
- [`produce_validated_questionnaire._add_issue_row`](#fn--add-issue-row-8827)

## Full Specifications

### `_NullOutput.write` {#fn-write-17}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:17`

**Signature**

```python
def write(self, *a, **kw):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Runtime and logger helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `self` | positional_or_keyword | Yes | `-` | `-` | Internal helper parameter used by runtime/logging wrapper code. |
| `*a` | var_positional | Yes | `-` | `-` | Internal helper parameter used by runtime/logging wrapper code. |
| `**kw` | var_keyword | Yes | `-` | `-` | Internal helper parameter used by runtime/logging wrapper code. |

??? note "Function source"

    ```python
    def write(self, *a, **kw): pass
    ```

### `_NullOutput.flush` {#fn-flush-18}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:18`

**Signature**

```python
def flush(self, *a, **kw):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Runtime and logger helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `self` | positional_or_keyword | Yes | `-` | `-` | Internal helper parameter used by runtime/logging wrapper code. |
| `*a` | var_positional | Yes | `-` | `-` | Internal helper parameter used by runtime/logging wrapper code. |
| `**kw` | var_keyword | Yes | `-` | `-` | Internal helper parameter used by runtime/logging wrapper code. |

??? note "Function source"

    ```python
    def flush(self, *a, **kw): pass
    ```

### `_NullOutput.fileno` {#fn-fileno-19}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:19`

**Signature**

```python
def fileno(self):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Runtime and logger helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `self` | positional_or_keyword | Yes | `-` | `-` | Internal helper parameter used by runtime/logging wrapper code. |

??? note "Function source"

    ```python
    def fileno(self): raise OSError("not a real file")
    ```

### `_banner` {#fn--banner-25}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:25`

**Signature**

```python
def _banner(tool: str, language: str, iso3: str, mode: str) -> None:
```

**Returns:** `None`

**What it does:** Implements logic in the `Runtime and logger helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `tool` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Runtime and logger helpers` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `iso3` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Runtime and logger helpers` stage. |
| `mode` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Runtime and logger helpers` stage. |

??? note "Function source"

    ```python
    def _banner(tool: str, language: str, iso3: str, mode: str) -> None:
        global _T_START
        _T_START = _time.perf_counter()
        _sys.stdout = _NullOutput()
        print("", file=_REAL_STDOUT)
        print("=" * _BANNER_W, file=_REAL_STDOUT)
        print("  DIEM Questionnaire Validation v2", file=_REAL_STDOUT)
        print(f"  Tool: {tool.upper()}  |  Language: {language.upper()}  |  Country: {iso3.upper()}", file=_REAL_STDOUT)
        print(f"  Reference mode: {mode}", file=_REAL_STDOUT)
        print("=" * _BANNER_W, file=_REAL_STDOUT)
    ```

### `_info` {#fn--info-37}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:37`

**Signature**

```python
def _info(label: str, value: str) -> None:
```

**Returns:** `None`

**What it does:** Implements logic in the `Runtime and logger helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `label` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Runtime and logger helpers` stage. |
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Runtime and logger helpers` stage. |

??? note "Function source"

    ```python
    def _info(label: str, value: str) -> None:
        print(f"  {label:<12} {value}", file=_REAL_STDOUT)
    ```

### `_step` {#fn--step-41}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:41`

**Signature**

```python
def _step(label: str, detail: str='') -> None:
```

**Returns:** `None`

**What it does:** Implements logic in the `Runtime and logger helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `label` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Runtime and logger helpers` stage. |
| `detail` | positional_or_keyword | No | `''` | `str` | Input used by the `Runtime and logger helpers` stage. |

??? note "Function source"

    ```python
    def _step(label: str, detail: str = "") -> None:
        global _STEP_N
        _STEP_N += 1
        tag  = f"[{_STEP_N}/{_STEP_TOTAL}]"
        pad  = "." * max(1, 44 - len(label))
        tail = f"  {detail}" if detail else ""
        print(f"  {tag} {label} {pad}{tail}", file=_REAL_STDOUT, flush=True)
    ```

### `_summary` {#fn--summary-50}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:50`

**Signature**

```python
def _summary(all_issues=None, report_path=None, extra_paths=None) -> None:
```

**Returns:** `None`

**What it does:** Implements logic in the `Runtime and logger helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `all_issues` | positional_or_keyword | No | `None` | `-` | Polars DataFrame carrying records for this processing stage. |
| `report_path` | positional_or_keyword | No | `None` | `-` | Filesystem path used for reading inputs or writing outputs. |
| `extra_paths` | positional_or_keyword | No | `None` | `-` | Filesystem path used for reading inputs or writing outputs. |

??? note "Function source"

    ```python
    def _summary(all_issues=None, report_path=None, extra_paths=None) -> None:
        _sys.stdout = _REAL_STDOUT
        print()
        print("-" * _BANNER_W)
        print("  VALIDATION SUMMARY")
        print("-" * _BANNER_W)
        try:
            import polars as _pl
            if all_issues is not None and all_issues.height > 0:
                sev = {r["severity"]: r["n"] for r in
                       all_issues.group_by("severity").agg(_pl.len().alias("n")).to_dicts()}
                high   = sev.get("high",   0)
                medium = sev.get("medium", 0)
                info   = sev.get("info",   0)
                print(f"  {'HIGH':<10} {high:>4}   {'Must fix before deployment' if high else 'None'}")
                print(f"  {'MEDIUM':<10} {medium:>4}   {'Review suggested' if medium else 'None'}")
                print(f"  {'INFO':<10} {info:>4}   Informational")
                print(f"  {'PASS':<10} {'yes' if high == 0 and medium == 0 else 'no':>4}")
            else:
                print("  No issues found — questionnaire passed all checks.")
        except Exception as _e:
            print(f"  (summary unavailable: {_e})")
        _added_df = globals().get("added")
        _removed_df = globals().get("removed")
        if _added_df is not None and _removed_df is not None:
            _added_names = _added_df["Q Name"].to_list()
            _removed_names = _removed_df["Q Name"].to_list()
            print()
            print(f"  Questions added ({len(_added_names)})  : {', '.join(_added_names) if _added_names else '(none)'}")
            print(f"  Questions removed ({len(_removed_names)}): {', '.join(_removed_names) if _removed_names else '(none)'}")
        _mod_ignore = str(globals().get("_module_ignore_scope_summary") or "").strip()
        _mod_skip = str(globals().get("_module_skip_scope_summary") or "").strip()
        if _mod_ignore and _mod_ignore != "(none)":
            print(f"  {'IGNORED MOD':<10} {_mod_ignore}")
        if _mod_skip and _mod_skip != "(none)":
            print(f"  {'SKIPPED MOD':<10} {_mod_skip}")
        print()
        if report_path:
            print(f"  Report  : {report_path}")
        if extra_paths:
            for _lbl, _p in extra_paths:
                print(f"  {_lbl:<8}: {_p}")
        print(f"  Time    : {_time.perf_counter() - _T_START:.1f}s")
        print("=" * _BANNER_W)
        print()
    ```

### `_load_effective_config` {#fn--load-effective-config-120}

**Pipeline stage:** `Step 1 -- Configuration`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:120`

**Signature**

```python
def _load_effective_config(cfg_path: Path) -> tuple[dict, Path | None, Path]:
```

**Returns:** `tuple[dict, Path | None, Path]`

**What it does:** Implements logic in the `Step 1 -- Configuration` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cfg_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |

??? note "Function source"

    ```python
    def _load_effective_config(cfg_path: Path) -> tuple[dict, Path | None, Path]:
        base_cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
        if not isinstance(base_cfg, dict):
            raise TypeError(f"Config must be a mapping in {cfg_path}")

        profile_name = str(base_cfg.get("config_profile") or "").strip()
        profile_path: Path | None = None
        effective_cfg = dict(base_cfg)

        if profile_name:
            profiles_dir = Path(base_cfg.get("config_profiles_dir") or (Path(base_cfg.get("output_dir") or base_cfg.get("working_dir") or "C:/Temp/questionnaire_validation") / "config_profiles"))
            candidate = Path(profile_name)
            if not candidate.is_absolute():
                candidate = profiles_dir / candidate

            if candidate.suffix.lower() not in {".yaml", ".yml"}:
                if candidate.with_suffix(".yaml").exists():
                    candidate = candidate.with_suffix(".yaml")
                elif candidate.with_suffix(".yml").exists():
                    candidate = candidate.with_suffix(".yml")

            if not candidate.exists():
                raise FileNotFoundError(
                    f"Config profile not found: {candidate}\n"
                    f"Set 'config_profile' to an existing file or leave it empty."
                )

            profile_cfg = yaml.safe_load(candidate.read_text(encoding="utf-8")) or {}
            if not isinstance(profile_cfg, dict):
                raise TypeError(f"Config profile must be a mapping in {candidate}")

            effective_cfg.update(profile_cfg)
            profile_path = candidate.resolve()

        active_cfg_path = profile_path or cfg_path.resolve()
        return effective_cfg, profile_path, active_cfg_path
    ```

### `_write_config_snapshot_kobo` {#fn--write-config-snapshot-kobo-202}

**Pipeline stage:** `Step 2 -- Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:202`

**Signature**

```python
def _write_config_snapshot_kobo(cfg: dict, run: dict, cfg_base_path: Path, cfg_active_path: Path) -> Path:
```

**Returns:** `Path`

**What it does:** Implements logic in the `Step 2 -- Reference file resolution` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cfg` | positional_or_keyword | Yes | `-` | `dict` | Runtime configuration object for this validation run. |
| `run` | positional_or_keyword | Yes | `-` | `dict` | Runtime configuration object for this validation run. |
| `cfg_base_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `cfg_active_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |

??? note "Function source"

    ```python
    def _write_config_snapshot_kobo(
        cfg: dict,
        run: dict,
        cfg_base_path: Path,
        cfg_active_path: Path,
    ) -> Path:
        logs_root = Path(cfg.get("output_base_dir") or cfg.get("output_dir") or Path(run["questionnaire_path"]).parent)
        logs_dir = logs_root / "configuration"
        logs_dir.mkdir(parents=True, exist_ok=True)

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_file = logs_dir / f"config_kobo_{str(cfg.get('language','')).upper()}_{cfg.get('iso3','')}_{ts}.yaml"

        payload = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "tool": "kobo",
            "active_config_file": str(cfg_active_path),
            "base_config_file": str(cfg_base_path.resolve()),
            "config_profile": str(cfg.get("config_profile") or ""),
            "resolved_config": dict(cfg),
            "resolved_run_paths": {k: str(v) for k, v in run.items()},
        }

        with out_file.open("w", encoding="utf-8") as f:
            yaml.safe_dump(payload, f, sort_keys=False, allow_unicode=True)
        return out_file
    ```

### `find_kobo_template` {#fn-find-kobo-template-230}

**Pipeline stage:** `Step 2 -- Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:230`

**Signature**

```python
def find_kobo_template(language: str, templates_dir: Path) -> Path:
```

**Returns:** `Path`

**What it does:** Newest KoBo template for the language. Multilingual templates (from

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `templates_dir` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |

??? note "Function source"

    ```python
    def find_kobo_template(language: str, templates_dir: Path) -> Path:
        """
        Newest KoBo template for the language. Multilingual templates (from
        20261007 on) have no language token in the filename and match any
        language. Sorted by the 8-digit date in the filename, then mtime.
        """
        lang_upper = language.upper()
        lang_tokens = ("EN", "FR", "AR", "ES", "PT")

        def _has_lang_token(name: str, code: str) -> bool:
            return re.search(rf"(?i)(?:^|[_\-\s]){code}(?:$|[_\-\s.])", name) is not None

        candidates = [
            p for p in templates_dir.glob("*kobo*.xlsx")
            if not p.name.startswith("~$")
            and (_has_lang_token(p.stem, lang_upper)
                 or not any(_has_lang_token(p.stem, t) for t in lang_tokens))
        ]

        def _date_key(p: Path) -> tuple[int, float]:
            m = re.search(r"(\d{8})", p.name)
            return (int(m.group(1)) if m else 0, p.stat().st_mtime)

        candidates.sort(key=_date_key, reverse=True)
        if not candidates:
            raise FileNotFoundError(f"No KoBO template for language {language!r} in {templates_dir}")
        return candidates[0]
    ```

### `find_kobo_template._has_lang_token` {#fn--has-lang-token-239}

**Pipeline stage:** `Step 2 -- Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:239`

**Signature**

```python
def _has_lang_token(name: str, code: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 2 -- Reference file resolution` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 2 -- Reference file resolution` stage. |
| `code` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 2 -- Reference file resolution` stage. |

??? note "Function source"

    ```python
    def _has_lang_token(name: str, code: str) -> bool:
            return re.search(rf"(?i)(?:^|[_\-\s]){code}(?:$|[_\-\s.])", name) is not None
    ```

### `find_kobo_template._date_key` {#fn--date-key-249}

**Pipeline stage:** `Step 2 -- Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:249`

**Signature**

```python
def _date_key(p: Path) -> tuple[int, float]:
```

**Returns:** `tuple[int, float]`

**What it does:** Implements logic in the `Step 2 -- Reference file resolution` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `p` | positional_or_keyword | Yes | `-` | `Path` | Input used by the `Step 2 -- Reference file resolution` stage. |

??? note "Function source"

    ```python
    def _date_key(p: Path) -> tuple[int, float]:
            m = re.search(r"(\d{8})", p.name)
            return (int(m.group(1)) if m else 0, p.stat().st_mtime)
    ```

### `_reference_scope_label` {#fn--reference-scope-label-292}

**Pipeline stage:** `Step 2 -- Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:292`

**Signature**

```python
def _reference_scope_label() -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 2 -- Reference file resolution` phase.

**Parameters**

No parameters.

??? note "Function source"

    ```python
    def _reference_scope_label() -> str:
        mode = str(run.get("reference_mode", "") or "").strip().lower()
        if mode == "previous_round":
            return "previous round"
        return "latest template"
    ```

### `_extract_round_token_kobo` {#fn--extract-round-token-kobo-299}

**Pipeline stage:** `Step 2 -- Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:299`

**Signature**

```python
def _extract_round_token_kobo(name: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 2 -- Reference file resolution` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 2 -- Reference file resolution` stage. |

??? note "Function source"

    ```python
    def _extract_round_token_kobo(name: str) -> str:
        txt = str(name or "")
        patterns = [
            r"(?i)(?:^|[_\-\s])R(\d{1,3})(?=$|[_\-\s\.])",
            r"(?i)(?:^|[_\-\s])ROUND[_\-\s]*(\d{1,3})(?=$|[_\-\s\.])",
            # Fallback for suffix forms like "...copyr10.xlsx"
            r"(?i)R(?:OUND)?[_\-\s]*([0-9]{1,3})(?=(?:\.[A-Za-z0-9]+)?$)",
        ]
        for pat in patterns:
            m = re.search(pat, txt)
            if m:
                return f"R{m.group(1)}"
        return ""
    ```

### `_reference_descriptor_kobo` {#fn--reference-descriptor-kobo-314}

**Pipeline stage:** `Step 2 -- Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:314`

**Signature**

```python
def _reference_descriptor_kobo() -> str:
```

**Returns:** `str`

**What it does:** Human-readable reference descriptor for KoBo Summary header.

**Parameters**

No parameters.

??? note "Function source"

    ```python
    def _reference_descriptor_kobo() -> str:
        """Human-readable reference descriptor for KoBo Summary header."""
        mode = _reference_scope_label()
        ref_name = Path(run.get("reference_path", "")).name if run.get("reference_path") else ""
        iso = str(run.get("iso3", "") or "").upper()
        rnd = _extract_round_token_kobo(ref_name) or "R?"
        lang = str(run.get("language", "") or "").upper()
        if mode == "previous round":
            return f"{mode} | {iso} {rnd} | {ref_name}"
        return f"{mode} | {lang} template | {ref_name}"
    ```

### `_language_scope_descriptor_kobo` {#fn--language-scope-descriptor-kobo-326}

**Pipeline stage:** `Step 2 -- Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:326`

**Signature**

```python
def _language_scope_descriptor_kobo() -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 2 -- Reference file resolution` phase.

**Parameters**

No parameters.

??? note "Function source"

    ```python
    def _language_scope_descriptor_kobo() -> str:
        lang = str(run.get("language", "") or "").lower()
        label_col = LANG_LABEL_COL.get(lang, f"label::{lang}")
        if lang and lang != "en":
            return f"EN + {lang.upper()} labels ({LANG_LABEL_COL.get('en', 'label::English (en)')} + {label_col})"
        return f"{lang.upper()} labels ({label_col})"
    ```

### `_not_in_reference_text` {#fn--not-in-reference-text-334}

**Pipeline stage:** `Step 2 -- Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:334`

**Signature**

```python
def _not_in_reference_text() -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 2 -- Reference file resolution` phase.

**Parameters**

No parameters.

??? note "Function source"

    ```python
    def _not_in_reference_text() -> str:
        return f"(not in {_reference_scope_label()})"
    ```

### `_as_bool` {#fn--as-bool-338}

**Pipeline stage:** `Step 2 -- Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:338`

**Signature**

```python
def _as_bool(value, default: bool=False) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 2 -- Reference file resolution` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 2 -- Reference file resolution` stage. |
| `default` | positional_or_keyword | No | `False` | `bool` | Input used by the `Step 2 -- Reference file resolution` stage. |

??? note "Function source"

    ```python
    def _as_bool(value, default: bool = False) -> bool:
        if isinstance(value, bool):
            return value
        if value is None:
            return default
        txt = str(value).strip().lower()
        if txt in {"1", "true", "yes", "y", "on"}:
            return True
        if txt in {"0", "false", "no", "n", "off"}:
            return False
        return default
    ```

### `_custom_qname_expr` {#fn--custom-qname-expr-387}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:387`

**Signature**

```python
def _custom_qname_expr(col_name: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** True when the question name carries a custom/optional prefix.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _custom_qname_expr(col_name: str) -> pl.Expr:
        """True when the question name carries a custom/optional prefix."""
        return pl.col(col_name).cast(pl.Utf8).str.strip_chars().str.contains(_CUSTOM_QNAME_RE)
    ```

### `_core_qname_expr` {#fn--core-qname-expr-392}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:392`

**Signature**

```python
def _core_qname_expr(col_name: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Question name with any custom/optional prefix removed, lowercased.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _core_qname_expr(col_name: str) -> pl.Expr:
        """Question name with any custom/optional prefix removed, lowercased."""
        return (
            pl.col(col_name).cast(pl.Utf8).str.strip_chars()
            .str.replace(_CUSTOM_QNAME_RE, "")
            .str.to_lowercase()
        )
    ```

### `_custom_variants` {#fn--custom-variants-401}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:401`

**Signature**

```python
def _custom_variants(q_name: str) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Custom/optional spellings of a template question (hh_wealth_x -> c_hh_wealth_x, o_hh_wealth_x).

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `q_name` | positional_or_keyword | Yes | `-` | `str` | Question identifier used to join or compare records. |

??? note "Function source"

    ```python
    def _custom_variants(q_name: str) -> list[str]:
        """Custom/optional spellings of a template question (hh_wealth_x -> c_hh_wealth_x, o_hh_wealth_x)."""
        q = str(q_name or "").strip()
        return [f"{p}{q}" for p in CUSTOM_QNAME_PREFIXES] if q else []
    ```

### `_normalize_survey_type_token` {#fn--normalize-survey-type-token-407}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:407`

**Signature**

```python
def _normalize_survey_type_token(value) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _normalize_survey_type_token(value) -> str:
        txt = str(value or "").strip().lower()
        return re.sub(r"\s+", "_", txt)
    ```

### `_find_label_col` {#fn--find-label-col-411}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:411`

**Signature**

```python
def _find_label_col(headers: list, language: str) -> str | None:
```

**Returns:** `str | None`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `headers` | positional_or_keyword | Yes | `-` | `list` | Input used by the `Step 3 -- Readers` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _find_label_col(headers: list, language: str) -> str | None:
        target = LANG_LABEL_COL.get(language.lower(), f"label::{language}")
        if target in headers:
            return target
        return next((h for h in headers if h.startswith("label::")), None)
    ```

### `_find_hint_col` {#fn--find-hint-col-426}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:426`

**Signature**

```python
def _find_hint_col(headers: list, language: str) -> str | None:
```

**Returns:** `str | None`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `headers` | positional_or_keyword | Yes | `-` | `list` | Input used by the `Step 3 -- Readers` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _find_hint_col(headers: list, language: str) -> str | None:
        target = _LANG_HINT_COL.get(language.lower(), f"hint::{language}")
        if target in headers:
            return target
        fallback = next((h for h in headers if h.startswith("hint::") and len(h) > len("hint::")), None)
        if fallback:
            return fallback
        return "hint" if "hint" in headers else None
    ```

### `_find_xlsform_header_row_idx` {#fn--find-xlsform-header-row-idx-436}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:436`

**Signature**

```python
def _find_xlsform_header_row_idx(rows: list) -> int:
```

**Returns:** `int`

**What it does:** Find the 0-based index of the XLSForm header row (contains 'type' and 'name').

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `rows` | positional_or_keyword | Yes | `-` | `list` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _find_xlsform_header_row_idx(rows: list) -> int:
        """Find the 0-based index of the XLSForm header row (contains 'type' and 'name').
        Returns 0 if not found for backward compatibility."""
        for i, row in enumerate(rows[:10]):
            vals = {str(v).strip().lower() for v in row if v is not None}
            if "type" in vals and "name" in vals:
                return i
        return 0
    ```

### `_find_ws_header_row_1based` {#fn--find-ws-header-row-1based-446}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:446`

**Signature**

```python
def _find_ws_header_row_1based(ws, max_scan: int=10) -> int:
```

**Returns:** `int`

**What it does:** Return the 1-based Excel row number of the XLSForm header row (has 'type' and 'name').

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `max_scan` | positional_or_keyword | No | `10` | `int` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _find_ws_header_row_1based(ws, max_scan: int = 10) -> int:
        """Return the 1-based Excel row number of the XLSForm header row (has 'type' and 'name').
        Returns 1 if not found for backward compatibility."""
        for row_idx, row in enumerate(ws.iter_rows(min_row=1, max_row=max_scan, values_only=True), start=1):
            vals = {str(v).strip().lower() for v in row if v is not None}
            if "type" in vals and "name" in vals:
                return row_idx
        return 1
    ```

### `_choices_header_key` {#fn--choices-header-key-465}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:465`

**Signature**

```python
def _choices_header_key(value) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _choices_header_key(value) -> str:
        return str(value or "").strip().lower()
    ```

### `_choices_header_concept` {#fn--choices-header-concept-469}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:469`

**Signature**

```python
def _choices_header_concept(value) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _choices_header_concept(value) -> str:
        key = _choices_header_key(value)
        if key in _CHOICES_PARENT_HEADER_ALIASES:
            return "__admin_parent__"
        return key
    ```

### `_resolve_choices_output_headers` {#fn--resolve-choices-output-headers-476}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:476`

**Signature**

```python
def _resolve_choices_output_headers(current_headers: list[str], template_headers: list[str] | None=None) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_headers` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 3 -- Readers` stage. |
| `template_headers` | positional_or_keyword | No | `None` | `list[str] | None` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _resolve_choices_output_headers(current_headers: list[str], template_headers: list[str] | None = None) -> list[str]:
        out = [str(h or "").strip() for h in (template_headers or current_headers or [])]
        seen_keys = {_choices_header_key(h) for h in out if _choices_header_key(h)}
        seen_concepts = {_choices_header_concept(h) for h in out if _choices_header_key(h)}
        for header in current_headers or []:
            txt = str(header or "").strip()
            key = _choices_header_key(txt)
            if not key:
                continue
            concept = _choices_header_concept(txt)
            if key in seen_keys or concept in seen_concepts:
                continue
            out.append(txt)
            seen_keys.add(key)
            seen_concepts.add(concept)
        return out
    ```

### `_remap_choices_row_to_headers` {#fn--remap-choices-row-to-headers-494}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:494`

**Signature**

```python
def _remap_choices_row_to_headers(values: list, styles: list, source_headers: list[str], target_headers: list[str], fallback_styles: list | None=None) -> tuple[list, list]:
```

**Returns:** `tuple[list, list]`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `values` | positional_or_keyword | Yes | `-` | `list` | Input used by the `Step 3 -- Readers` stage. |
| `styles` | positional_or_keyword | Yes | `-` | `list` | Input used by the `Step 3 -- Readers` stage. |
| `source_headers` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 3 -- Readers` stage. |
| `target_headers` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 3 -- Readers` stage. |
| `fallback_styles` | positional_or_keyword | No | `None` | `list | None` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _remap_choices_row_to_headers(
        values: list,
        styles: list,
        source_headers: list[str],
        target_headers: list[str],
        fallback_styles: list | None = None,
    ) -> tuple[list, list]:
        target_len = len(target_headers)
        out_vals = [None] * target_len
        out_styles = [None] * target_len

        source_exact = {}
        source_by_concept = {}
        for idx, header in enumerate(source_headers):
            key = _choices_header_key(header)
            if not key:
                continue
            source_exact.setdefault(key, idx)
            source_by_concept.setdefault(_choices_header_concept(header), idx)

        generic_style = styles[0] if styles else None
        for idx, header in enumerate(target_headers):
            source_idx = source_exact.get(_choices_header_key(header))
            if source_idx is None:
                source_idx = source_by_concept.get(_choices_header_concept(header))
            if source_idx is not None and source_idx < len(values):
                out_vals[idx] = values[source_idx]
                if source_idx < len(styles):
                    out_styles[idx] = _style_copy(styles[source_idx])
            elif fallback_styles is not None and idx < len(fallback_styles) and fallback_styles[idx] is not None:
                out_styles[idx] = _style_copy(fallback_styles[idx])
            elif idx < len(styles) and styles[idx] is not None:
                out_styles[idx] = _style_copy(styles[idx])
            else:
                out_styles[idx] = _style_copy(generic_style) if generic_style is not None else None

        return out_vals, out_styles
    ```

### `_read_choices_headers_from_workbook` {#fn--read-choices-headers-from-workbook-533}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:533`

**Signature**

```python
def _read_choices_headers_from_workbook(path: str) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |

??? note "Function source"

    ```python
    def _read_choices_headers_from_workbook(path: str) -> list[str]:
        try:
            wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
        except Exception:
            return []
        try:
            if "choices" not in wb.sheetnames:
                return []
            row = next(wb["choices"].iter_rows(min_row=1, max_row=1, values_only=True), None)
            if not row:
                return []
            return [str(v).strip() if v is not None else "" for v in row]
        finally:
            wb.close()
    ```

### `_normalize_list_token` {#fn--normalize-list-token-558}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:558`

**Signature**

```python
def _normalize_list_token(value) -> str:
```

**Returns:** `str`

**What it does:** Canonical list token used to link survey select_one/select_multiple to choices.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _normalize_list_token(value) -> str:
        """
        Canonical list token used to link survey select_one/select_multiple to choices.
        Handles hidden unicode/spacing variants that are visually identical in Excel.
        """
        txt = unicodedata.normalize("NFKC", str(value or ""))
        txt = txt.translate(_INVISIBLE_TOKEN_CHARS).replace("\u00a0", " ")
        txt = re.sub(r"\s+", " ", txt).strip().lower()
        return txt
    ```

### `_normalize_module_token` {#fn--normalize-module-token-569}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:569`

**Signature**

```python
def _normalize_module_token(value) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _normalize_module_token(value) -> str:
        txt = unicodedata.normalize("NFKC", str(value or ""))
        txt = txt.translate(_INVISIBLE_TOKEN_CHARS).replace("\u00a0", " ")
        txt = re.sub(r"\s+", " ", txt).strip().lower()
        return txt
    ```

### `_extract_select_list_name_from_type` {#fn--extract-select-list-name-from-type-576}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:576`

**Signature**

```python
def _extract_select_list_name_from_type(q_type_raw: str) -> str:
```

**Returns:** `str`

**What it does:** Extract list token from KoBo/XLSForm select type declarations.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `q_type_raw` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _extract_select_list_name_from_type(q_type_raw: str) -> str:
        """
        Extract list token from KoBo/XLSForm select type declarations.
        Supports:
          - "select_one list_name"
          - "select_multiple list_name"
          - "select_one_list_name" (legacy)
          - "select_multiple_list_name" (legacy)
        """
        raw = str(q_type_raw or "").strip()
        if not raw:
            return ""

        raw_norm = _normalize_survey_type_token(raw)
        if raw_norm.startswith("select_one_"):
            return raw[len("select_one_"):].strip()
        if raw_norm.startswith("select_multiple_"):
            return raw[len("select_multiple_"):].strip()

        m = re.match(r"(?i)^\s*select[_\s]*(one|multiple)\s+(.+?)\s*$", raw)
        if m:
            return str(m.group(2) or "").strip()
        return ""
    ```

### `_canonical_option_name_token` {#fn--canonical-option-name-token-601}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:601`

**Signature**

```python
def _canonical_option_name_token(value) -> str:
```

**Returns:** `str`

**What it does:** Canonical choice name token:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _canonical_option_name_token(value) -> str:
        """
        Canonical choice name token:
        - unicode-normalized
        - hidden chars removed
        - trimmed
        - integer-like decimals normalized (1.0 -> 1)
        """
        txt = unicodedata.normalize("NFKC", str(value or ""))
        txt = txt.translate(_INVISIBLE_TOKEN_CHARS).replace("\u00a0", " ").strip()
        txt = re.sub(r"^([+-]?\d+)\.0+$", r"\1", txt)
        return txt
    ```

### `_normalized_list_expr` {#fn--normalized-list-expr-615}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:615`

**Signature**

```python
def _normalized_list_expr(col_name: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _normalized_list_expr(col_name: str) -> pl.Expr:
        return pl.col(col_name).map_elements(_normalize_list_token, return_dtype=pl.Utf8)
    ```

### `_normalize_mandatory` {#fn--normalize-mandatory-619}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:619`

**Signature**

```python
def _normalize_mandatory(val) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `val` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _normalize_mandatory(val) -> str:
        v = str(val or "").strip().lower()
        if v in ("yes", "true", "mandatory"):
            return "mandatory"
        if v in ("yes - panel", "yes-panel", "mandatory-panel"):
            return "mandatory-panel"
        if v in ("no", "false"):
            return "non-mandatory"
        if v.startswith("yes"):
            return "mandatory"
        return ""
    ```

### `read_kobo_survey` {#fn-read-kobo-survey-632}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:632`

**Signature**

```python
def read_kobo_survey(path: str, language: str='en', _wb=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |
| `language` | positional_or_keyword | No | `'en'` | `str` | Language selector used for language-specific text columns. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def read_kobo_survey(path: str, language: str = "en", _wb=None) -> pl.DataFrame:
        EMPTY = {
            "Q Name": pl.Utf8, "Q Type": pl.Utf8, "list_name": pl.Utf8,
            "module_key": pl.Utf8, "module": pl.Utf8, "module_en": pl.Utf8,
            "label": pl.Utf8, "label_en": pl.Utf8, "required": pl.Utf8, "mandatory_category": pl.Utf8,
            "mandatory_raw": pl.Utf8,
            "relevant": pl.Utf8, "constraint": pl.Utf8, "choice_filter": pl.Utf8,
            "appearance": pl.Utf8, "calculation": pl.Utf8, "hint": pl.Utf8,
            "excel_row": pl.Int64, "source_file": pl.Utf8,
        }
        owns_wb = _wb is None
        wb = _wb or openpyxl.load_workbook(path, data_only=True, read_only=True)
        try:
            ws   = wb["survey"]
            rows = list(ws.iter_rows(values_only=True))
        finally:
            if owns_wb:
                wb.close()

        if not rows:
            return pl.DataFrame(schema=EMPTY)

        _hdr_idx  = _find_xlsform_header_row_idx(rows)
        headers   = [str(h).strip() if h is not None else "" for h in rows[_hdr_idx]]
        col_idx   = {h: i for i, h in enumerate(headers)}
        label_col = _find_label_col(headers, language)
        label_col_en = _find_label_col(headers, "en")
        hint_col  = _find_hint_col(headers, language)
        mand_col  = next((h for h in headers if h.strip() == "Mandatory"), None)

        def get(row, col):
            i = col_idx.get(col)
            return row[i] if i is not None and i < len(row) else None

        module_stack: list[tuple[str, str]] = []
        records = []
        for excel_row, row in enumerate(rows[_hdr_idx + 1:], start=_hdr_idx + 2):
            q_type_raw = str(get(row, "type") or "").strip()
            q_name     = str(get(row, "name") or "").strip()
            if not q_type_raw:
                continue

            type_norm = _normalize_survey_type_token(q_type_raw)

            # Track begin/end module boundaries without emitting them as questions.
            if any(type_norm.startswith(t) for t in _GROUP_BEGIN_TYPES):
                module_key = q_name
                module_label = str(get(row, label_col) or "").strip() if label_col else ""
                module_label_en = str(get(row, label_col_en) or "").strip() if label_col_en else ""
                if not module_label and module_label_en:
                    module_label = module_label_en
                if not module_label:
                    module_label = module_key
                if not module_label_en:
                    module_label_en = module_label
                if module_key:
                    module_stack.append((module_key, module_label, module_label_en))
                continue

            if any(type_norm.startswith(t) for t in _GROUP_END_TYPES):
                if module_stack:
                    module_stack.pop()
                continue

            if not q_name:
                continue

            q_type_first = str(q_type_raw.split(None, 1)[0] if q_type_raw else "").strip().lower()
            if _normalize_survey_type_token(q_type_first) in _METADATA_TYPES:
                continue

            parts     = q_type_raw.split(None, 1)
            q_type    = parts[0]
            list_name = parts[1].strip() if len(parts) > 1 and q_type in _SELECT_TYPES else None

            # Support legacy KoBo encoding where list name is embedded with underscore,
            # e.g. "select_one_debt" / "select_multiple_debt".
            if list_name is None:
                if _normalize_survey_type_token(q_type_raw).startswith("select_one_"):
                    q_type = "select_one"
                    list_name = q_type_raw[len("select_one_"):].strip() or None
                elif _normalize_survey_type_token(q_type_raw).startswith("select_multiple_"):
                    q_type = "select_multiple"
                    list_name = q_type_raw[len("select_multiple_"):].strip() or None

            # Normalize spaced declaration forms like "select one list_name".
            list_name_from_type = _extract_select_list_name_from_type(q_type_raw)
            if list_name is None and list_name_from_type:
                list_name = list_name_from_type
                q_type = "select_one" if "select_one" in _normalize_survey_type_token(q_type_raw) else "select_multiple"

            q_type = _normalize_survey_type_token(q_type)
            if q_type not in _SELECT_TYPES and list_name is None:
                list_name = None

            mand_cat = _normalize_mandatory(get(row, mand_col))
            if not mand_cat and q_type in _DATA_TYPES:
                mand_cat = "non-mandatory"
            if q_name.startswith(CUSTOM_QNAME_PREFIXES):
                mand_cat = "optional"

            module_key = module_stack[-1][0] if module_stack else ""
            module_label = module_stack[-1][1] if module_stack else ""
            module_label_en = module_stack[-1][2] if module_stack else ""

            records.append({
                "Q Name"            : q_name,
                "Q Type"            : q_type,
                "list_name"         : list_name,
                "module_key"        : module_key,
                "module"            : module_label,
                "module_en"         : module_label_en,
                "label"             : str(get(row, label_col) or "") if label_col else "",
                "label_en"          : str(get(row, label_col_en) or "") if label_col_en else "",
                "required"          : str(get(row, "required")    or "").strip().lower(),
                "mandatory_category": mand_cat,
                "mandatory_raw"     : str(get(row, mand_col) or "").strip() if mand_col else "",
                "relevant"          : str(get(row, "relevant")    or "").strip(),
                "constraint"        : str(get(row, "constraint")  or "").strip(),
                "choice_filter"     : str(get(row, "choice_filter") or "").strip(),
                "appearance"        : str(get(row, "appearance")  or "").strip(),
                "calculation"       : str(get(row, "calculation") or "").strip(),
                "hint"             : str(get(row, hint_col) or "").strip() if hint_col else str(get(row, "hint") or "").strip(),
                "excel_row"         : excel_row,
                "source_file"       : str(path),
            })
        return pl.DataFrame(records) if records else pl.DataFrame(schema=EMPTY)
    ```

### `read_kobo_survey.get` {#fn-get-662}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:662`

**Signature**

```python
def get(row, col):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 3 -- Readers` stage. |
| `col` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def get(row, col):
            i = col_idx.get(col)
            return row[i] if i is not None and i < len(row) else None
    ```

### `read_kobo_choices` {#fn-read-kobo-choices-761}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:761`

**Signature**

```python
def read_kobo_choices(path: str, language: str='en', _wb=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |
| `language` | positional_or_keyword | No | `'en'` | `str` | Language selector used for language-specific text columns. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def read_kobo_choices(path: str, language: str = "en", _wb=None) -> pl.DataFrame:
        EMPTY = {"list_name": pl.Utf8, "option_name": pl.Utf8, "option_label": pl.Utf8}
        owns_wb = _wb is None
        wb = _wb or openpyxl.load_workbook(path, data_only=True, read_only=True)
        try:
            ws   = wb["choices"]
            rows = list(ws.iter_rows(values_only=True))
        finally:
            if owns_wb:
                wb.close()
        if not rows:
            return pl.DataFrame(schema=EMPTY)

        headers   = [str(h).strip() if h is not None else "" for h in rows[0]]
        col_idx   = {h: i for i, h in enumerate(headers)}
        label_col = _find_label_col(headers, language)

        def get(row, col):
            i = col_idx.get(col)
            return row[i] if i is not None and i < len(row) else None

        records = []
        for row in rows[1:]:
            list_name = get(row, "list_name")
            name_raw  = get(row, "name")
            if not list_name or name_raw is None:
                continue
            records.append({
                "list_name"   : str(list_name).strip(),
                "option_name" : str(name_raw).strip(),
                "option_label": str(get(row, label_col) or "").strip() if label_col else "",
            })
        return pl.DataFrame(records) if records else pl.DataFrame(schema=EMPTY)
    ```

### `read_kobo_choices.get` {#fn-get-778}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:778`

**Signature**

```python
def get(row, col):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 3 -- Readers` stage. |
| `col` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def get(row, col):
            i = col_idx.get(col)
            return row[i] if i is not None and i < len(row) else None
    ```

### `build_question_options` {#fn-build-question-options-796}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:796`

**Signature**

```python
def build_question_options(survey_df: pl.DataFrame, choices_df: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `survey_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `choices_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def build_question_options(survey_df: pl.DataFrame, choices_df: pl.DataFrame) -> pl.DataFrame:
        schema = {
            "Q Name": pl.Utf8,
            "Q Type": pl.Utf8,
            "list_name": pl.Utf8,
            "module_key": pl.Utf8,
            "module": pl.Utf8,
            "option_name": pl.Utf8,
            "option_label": pl.Utf8,
            "source_file": pl.Utf8,
        }
        if (
            survey_df is None
            or survey_df.height == 0
            or choices_df is None
            or choices_df.height == 0
        ):
            return pl.DataFrame(schema=schema)

        survey_rows = (
            survey_df
            .filter(pl.col("list_name").is_not_null() & (pl.col("list_name") != ""))
            .select(["Q Name", "Q Type", "list_name", "module_key", "module", "source_file"])
            .to_dicts()
        )
        if not survey_rows:
            return pl.DataFrame(schema=schema)

        # Dictionary model (GeoPoll-style): canonical list token -> choices rows.
        choices_by_list: dict[str, list[tuple[str, str]]] = {}
        for row in choices_df.select(["list_name", "option_name", "option_label"]).iter_rows(named=True):
            list_key = _normalize_list_token(row.get("list_name"))
            option_name_raw = str(row.get("option_name") or "").strip()
            if not list_key or _canonical_option_name_token(option_name_raw) == "":
                continue
            choices_by_list.setdefault(list_key, []).append((
                option_name_raw,
                str(row.get("option_label") or "").strip(),
            ))

        records = []
        for qrow in survey_rows:
            list_name_raw = str(qrow.get("list_name") or "")
            list_key = _normalize_list_token(list_name_raw)
            if not list_key:
                continue
            for option_name, option_label in choices_by_list.get(list_key, []):
                records.append({
                    "Q Name": str(qrow.get("Q Name") or ""),
                    "Q Type": str(qrow.get("Q Type") or ""),
                    "list_name": list_name_raw,
                    "module_key": str(qrow.get("module_key") or ""),
                    "module": str(qrow.get("module") or ""),
                    "option_name": option_name,
                    "option_label": option_label,
                    "source_file": str(qrow.get("source_file") or ""),
                })

        return pl.DataFrame(records, schema=schema) if records else pl.DataFrame(schema=schema)
    ```

### `_normalized_module_expr` {#fn--normalized-module-expr-857}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:857`

**Signature**

```python
def _normalized_module_expr(col_name: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _normalized_module_expr(col_name: str) -> pl.Expr:
        return pl.col(col_name).map_elements(_normalize_module_token, return_dtype=pl.Utf8)
    ```

### `_resolve_module_keys_from_tokens` {#fn--resolve-module-keys-from-tokens-861}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:861`

**Signature**

```python
def _resolve_module_keys_from_tokens(tokens: list[str], survey_dfs: list[pl.DataFrame]) -> tuple[set[str], list[str]]:
```

**Returns:** `tuple[set[str], list[str]]`

**What it does:** Resolve user-provided module names/labels to normalized module keys.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `tokens` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 3 -- Readers` stage. |
| `survey_dfs` | positional_or_keyword | Yes | `-` | `list[pl.DataFrame]` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def _resolve_module_keys_from_tokens(
        tokens: list[str],
        survey_dfs: list[pl.DataFrame],
    ) -> tuple[set[str], list[str]]:
        """
        Resolve user-provided module names/labels to normalized module keys.
        Accepts either module key (group name) or module label text.
        """
        alias_to_key: dict[str, str] = {}
        for df in survey_dfs:
            if df is None or df.height == 0 or "module_key" not in df.columns:
                continue
            for row in df.select(["module_key", "module"]).iter_rows(named=True):
                module_key_raw = str(row.get("module_key") or "").strip()
                module_label_raw = str(row.get("module") or "").strip()
                key_norm = _normalize_module_token(module_key_raw)
                if not key_norm:
                    continue
                alias_to_key.setdefault(key_norm, key_norm)
                if module_key_raw:
                    alias_to_key.setdefault(_normalize_module_token(module_key_raw), key_norm)
                if module_label_raw:
                    alias_to_key.setdefault(_normalize_module_token(module_label_raw), key_norm)

        resolved: set[str] = set()
        unresolved: list[str] = []
        for tok in tokens or []:
            t_norm = _normalize_module_token(tok)
            if not t_norm:
                continue
            key = alias_to_key.get(t_norm)
            if key:
                resolved.add(key)
            else:
                unresolved.append(str(tok))
        return resolved, unresolved
    ```

### `_filter_survey_by_module_keys` {#fn--filter-survey-by-module-keys-899}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:899`

**Signature**

```python
def _filter_survey_by_module_keys(df: pl.DataFrame, excluded_module_keys: set[str]) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `excluded_module_keys` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _filter_survey_by_module_keys(df: pl.DataFrame, excluded_module_keys: set[str]) -> pl.DataFrame:
        if df is None or df.height == 0 or not excluded_module_keys or "module_key" not in df.columns:
            return df
        return (
            df
            .with_columns(_normalized_module_expr("module_key").alias("_module_key_norm"))
            .filter(~pl.col("_module_key_norm").is_in(list(excluded_module_keys)))
            .drop("_module_key_norm")
        )
    ```

### `_module_display_map` {#fn--module-display-map-910}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:910`

**Signature**

```python
def _module_display_map(*survey_dfs: pl.DataFrame) -> dict[str, str]:
```

**Returns:** `dict[str, str]`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `*survey_dfs` | var_positional | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def _module_display_map(*survey_dfs: pl.DataFrame) -> dict[str, str]:
        out: dict[str, str] = {}
        for df in survey_dfs:
            if df is None or df.height == 0 or "module_key" not in df.columns:
                continue
            for row in df.select(["module_key", "module"]).iter_rows(named=True):
                key_norm = _normalize_module_token(row.get("module_key"))
                if not key_norm:
                    continue
                label = str(row.get("module") or "").strip()
                if key_norm not in out or (not out[key_norm] and label):
                    out[key_norm] = label or str(row.get("module_key") or "").strip()
        return out
    ```

### `_collect_skip_module_payload` {#fn--collect-skip-module-payload-925}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:925`

**Signature**

```python
def _collect_skip_module_payload(current_survey_df: pl.DataFrame, skip_module_keys: set[str]) -> tuple[set[str], set[str]]:
```

**Returns:** `tuple[set[str], set[str]]`

**What it does:** Return (skip_qnames, removable_choice_list_names) derived from current survey.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_survey_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `skip_module_keys` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _collect_skip_module_payload(
        current_survey_df: pl.DataFrame,
        skip_module_keys: set[str],
    ) -> tuple[set[str], set[str]]:
        """
        Return (skip_qnames, removable_choice_list_names) derived from current survey.
        Removable list names are those referenced only by skipped-module questions.
        """
        if (
            current_survey_df is None
            or current_survey_df.height == 0
            or not skip_module_keys
            or "module_key" not in current_survey_df.columns
        ):
            return set(), set()

        df = current_survey_df.with_columns(_normalized_module_expr("module_key").alias("_module_key_norm"))
        skip_df = df.filter(pl.col("_module_key_norm").is_in(list(skip_module_keys)))
        keep_df = df.filter(~pl.col("_module_key_norm").is_in(list(skip_module_keys)))

        skip_qnames = set(skip_df["Q Name"].to_list()) if "Q Name" in skip_df.columns else set()

        skip_lists = set(
            skip_df
            .filter(pl.col("list_name").is_not_null() & (pl.col("list_name") != ""))
            .get_column("list_name")
            .to_list()
        ) if "list_name" in skip_df.columns else set()

        keep_lists = set(
            keep_df
            .filter(pl.col("list_name").is_not_null() & (pl.col("list_name") != ""))
            .get_column("list_name")
            .to_list()
        ) if "list_name" in keep_df.columns else set()

        removable_lists = skip_lists - keep_lists
        return skip_qnames, removable_lists
    ```

### `_dedupe_keep_order` {#fn--dedupe-keep-order-965}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:965`

**Signature**

```python
def _dedupe_keep_order(items: list[str]) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `items` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _dedupe_keep_order(items: list[str]) -> list[str]:
        seen = set()
        out: list[str] = []
        for raw in items or []:
            txt = str(raw or "").strip()
            if not txt:
                continue
            key = txt.casefold()
            if key in seen:
                continue
            seen.add(key)
            out.append(txt)
        return out
    ```

### `_format_module_scope_for_display` {#fn--format-module-scope-for-display-980}

**Pipeline stage:** `Step 3 -- Readers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:980`

**Signature**

```python
def _format_module_scope_for_display(configured_tokens: list[str], resolved_keys: set[str], module_names: dict[str, str]) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 3 -- Readers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `configured_tokens` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 3 -- Readers` stage. |
| `resolved_keys` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 3 -- Readers` stage. |
| `module_names` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 3 -- Readers` stage. |

??? note "Function source"

    ```python
    def _format_module_scope_for_display(
        configured_tokens: list[str],
        resolved_keys: set[str],
        module_names: dict[str, str],
    ) -> str:
        cfg = _dedupe_keep_order(configured_tokens or [])
        resolved_parts = []
        for key in sorted(resolved_keys or set()):
            lbl = str(module_names.get(key, "") or "").strip()
            resolved_parts.append(f"{lbl} [{key}]" if lbl else key)
        cfg_txt = ", ".join(cfg) if cfg else "(none)"
        if resolved_parts:
            return f"{cfg_txt} -> {', '.join(resolved_parts)}"
        return cfg_txt
    ```

### `_normalize_languages_in_scope` {#fn--normalize-languages-in-scope-1049}

**Pipeline stage:** `Step 4 -- Load files`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1049`

**Signature**

```python
def _normalize_languages_in_scope(value) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** languages_in_scope config value -> lowercase codes; empty list = every filled language.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 4 -- Load files` stage. |

??? note "Function source"

    ```python
    def _normalize_languages_in_scope(value) -> list[str]:
        """languages_in_scope config value -> lowercase codes; empty list = every filled language."""
        if isinstance(value, str):
            value = [v for v in value.split(",")]
        return [str(v).strip().lower() for v in (value or []) if str(v).strip()]
    ```

### `_normalize_additional_info_header` {#fn--normalize-additional-info-header-1167}

**Pipeline stage:** `Step 4b -- Placeholder normalization`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1167`

**Signature**

```python
def _normalize_additional_info_header(value) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 4b -- Placeholder normalization` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 4b -- Placeholder normalization` stage. |

??? note "Function source"

    ```python
    def _normalize_additional_info_header(value) -> str:
        return re.sub(r"\s+", " ", str(value or "").strip()).lower()
    ```

### `_additional_info_replacement_indexes` {#fn--additional-info-replacement-indexes-1171}

**Pipeline stage:** `Step 4b -- Placeholder normalization`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1171`

**Signature**

```python
def _additional_info_replacement_indexes(headers: list[str]) -> dict[str, int | None]:
```

**Returns:** `dict[str, int | None]`

**What it does:** Implements logic in the `Step 4b -- Placeholder normalization` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `headers` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 4b -- Placeholder normalization` stage. |

??? note "Function source"

    ```python
    def _additional_info_replacement_indexes(headers: list[str]) -> dict[str, int | None]:
        norm_headers = [_normalize_additional_info_header(h) for h in headers]
        generic_idx = next((i for i, h in enumerate(norm_headers) if h == "replacement"), None)

        out: dict[str, int | None] = {}
        for lang in ("en", "fr", "ar", "es"):
            candidates = {
                f"replacement ({lang})",
                f"replacement {lang}",
                f"replacement({lang})",
            }
            out[lang] = next((i for i, h in enumerate(norm_headers) if h in candidates), None)
            if out[lang] is None and generic_idx is not None:
                out[lang] = generic_idx
        return out
    ```

### `_placeholder_aliases` {#fn--placeholder-aliases-1188}

**Pipeline stage:** `Step 4b -- Placeholder normalization`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1188`

**Signature**

```python
def _placeholder_aliases(s: str) -> set[str]:
```

**Returns:** `set[str]`

**What it does:** Generate tolerant alias tokens (case + simple singular/plural) for replacements.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `s` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4b -- Placeholder normalization` stage. |

??? note "Function source"

    ```python
    def _placeholder_aliases(s: str) -> set[str]:
        """Generate tolerant alias tokens (case + simple singular/plural) for replacements."""
        s = (s or "").strip()
        if not s:
            return set()
        aliases = {s, s.lower(), s.upper()}
        low = s.lower()
        if low.endswith("s") and len(s) > 1:
            stem = s[:-1]
            aliases |= {stem, stem.lower(), stem.upper()}
        else:
            plus = s + "s"
            aliases |= {plus, plus.lower(), plus.upper()}
        return aliases
    ```

### `read_additional_info_all_languages` {#fn-read-additional-info-all-languages-1204}

**Pipeline stage:** `Step 4b -- Placeholder normalization`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1204`

**Signature**

```python
def read_additional_info_all_languages(country_path: str) -> dict[str, dict[str, str]]:
```

**Returns:** `dict[str, dict[str, str]]`

**What it does:** Read Additional information replacements for each workbook language column.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `country_path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |

??? note "Function source"

    ```python
    def read_additional_info_all_languages(country_path: str) -> dict[str, dict[str, str]]:
        """Read Additional information replacements for each workbook language column."""
        out = {lang: {} for lang in ("en", "fr", "ar", "es")}
        try:
            wb = openpyxl.load_workbook(country_path, data_only=True, read_only=True)
            if "Additional information" not in wb.sheetnames:
                wb.close()
                return out
            ws = wb["Additional information"]
            rows = list(ws.iter_rows(values_only=True))
            wb.close()
        except Exception:
            return out

        if len(rows) < 2:
            return out

        headers = [str(h).strip() if h is not None else "" for h in rows[1]]
        orig_idx = next((i for i, h in enumerate(headers) if _normalize_additional_info_header(h).startswith("original")), None)
        if orig_idx is None:
            return out

        replacement_idx_by_lang = _additional_info_replacement_indexes(headers)

        for row in rows[2:]:
            orig = row[orig_idx] if orig_idx < len(row) else None
            if not orig or str(orig).strip() == "":
                continue
            row_pairs: dict[str, str] = {}
            for lang, repl_idx in replacement_idx_by_lang.items():
                if repl_idx is None or repl_idx >= len(row):
                    continue
                repl = row[repl_idx]
                repl_str = str(repl).strip() if repl is not None else ""
                if repl_str in ("", "nan", "None"):
                    continue
                row_pairs[lang] = repl_str

            if not row_pairs:
                continue

            for lang, repl_str in row_pairs.items():
                for alias in _placeholder_aliases(str(orig)):
                    out[lang][f"#{alias}#"] = repl_str

        return out
    ```

### `read_additional_info_with_status` {#fn-read-additional-info-with-status-1252}

**Pipeline stage:** `Step 4b -- Placeholder normalization`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1252`

**Signature**

```python
def read_additional_info_with_status(country_path: str, language: str='en') -> tuple[dict[str, str], dict]:
```

**Returns:** `tuple[dict[str, str], dict]`

**What it does:** Read Additional information replacements and return:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `country_path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |
| `language` | positional_or_keyword | No | `'en'` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def read_additional_info_with_status(
        country_path: str,
        language: str = "en",
    ) -> tuple[dict[str, str], dict]:
        """
        Read Additional information replacements and return:
          - pairs: {#placeholder#: value}
          - status: diagnostics for strict replacement checks/reporting
        """
        status = {
            "sheet_found": False,
            "headers_found": False,
            "rows_total": 0,
            "rows_with_original": 0,
            "rows_with_replacement": 0,
            "pairs_count": 0,
            "missing_replacement_rows": [],
            "status": "FAIL",
            "severity": "high",
            "message": "Additional information sheet not found",
        }
        try:
            wb = openpyxl.load_workbook(country_path, data_only=True, read_only=True)
            if "Additional information" not in wb.sheetnames:
                wb.close()
                return {}, status
            status["sheet_found"] = True
            ws = wb["Additional information"]
            rows = list(ws.iter_rows(values_only=True))
            wb.close()
        except Exception as e:
            status["message"] = f"Could not read Additional information sheet: {e}"
            return {}, status

        if len(rows) < 2:
            status["message"] = "Additional information sheet has no header row"
            return {}, status
        headers = [str(h).strip() if h is not None else "" for h in rows[1]]

        orig_idx = next((i for i, h in enumerate(headers) if _normalize_additional_info_header(h).startswith("original")), None)
        replacement_idx_by_lang = _additional_info_replacement_indexes(headers)
        repl_idx = replacement_idx_by_lang.get(str(language or "en").strip().lower())

        if orig_idx is None or repl_idx is None:
            status["message"] = "Original/Replacement columns not found in Additional information sheet"
            return {}, status
        status["headers_found"] = True

        pairs: dict[str, str] = {}
        missing_rows: list[dict] = []
        row_total = 0
        row_with_original = 0
        row_with_replacement = 0
        for excel_row, row in enumerate(rows[2:], start=3):
            row_total += 1
            orig = row[orig_idx] if orig_idx < len(row) else None
            repl = row[repl_idx] if repl_idx < len(row) else None
            if not orig or str(orig).strip() == "":
                continue
            row_with_original += 1
            repl_str = str(repl).strip() if repl is not None else ""
            if repl_str in ("", "nan", "None"):
                missing_rows.append({"excel_row": excel_row, "original": str(orig).strip()})
                continue
            row_with_replacement += 1
            for _alias in _placeholder_aliases(str(orig)):
                pairs[f"#{_alias}#"] = repl_str

        status["rows_total"] = row_total
        status["rows_with_original"] = row_with_original
        status["rows_with_replacement"] = row_with_replacement
        status["pairs_count"] = len(pairs)
        status["missing_replacement_rows"] = missing_rows
        if row_with_original == 0:
            status["status"] = "WARN"
            status["severity"] = "medium"
            status["message"] = "No placeholder rows found in Additional information sheet"
        elif row_with_replacement == 0:
            status["status"] = "FAIL"
            status["severity"] = "high"
            status["message"] = "Additional information has placeholders but no replacement values"
        elif missing_rows:
            status["status"] = "WARN"
            status["severity"] = "medium"
            status["message"] = (
                f"Loaded {len(pairs)} replacement token(s); "
                f"{len(missing_rows)} row(s) have Original but blank Replacement"
            )
        else:
            status["status"] = "PASS"
            status["severity"] = "pass"
            status["message"] = f"Loaded {len(pairs)} replacement token(s)"

        return pairs, status
    ```

### `read_additional_info` {#fn-read-additional-info-1348}

**Pipeline stage:** `Step 4b -- Placeholder normalization`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1348`

**Signature**

```python
def read_additional_info(country_path: str, language: str='en') -> dict[str, str]:
```

**Returns:** `dict[str, str]`

**What it does:** Implements logic in the `Step 4b -- Placeholder normalization` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `country_path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |
| `language` | positional_or_keyword | No | `'en'` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def read_additional_info(country_path: str, language: str = "en") -> dict[str, str]:
        pairs, _ = read_additional_info_with_status(country_path, language)
        return pairs
    ```

### `restore_to_vanilla` {#fn-restore-to-vanilla-1353}

**Pipeline stage:** `Step 4b -- Placeholder normalization`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1353`

**Signature**

```python
def restore_to_vanilla(current_df: pl.DataFrame, reference_df: pl.DataFrame, cols: list[str], key_cols: list[str] | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** For every cell where the reference contains a #placeholder# token, overwrite

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 4b -- Placeholder normalization` stage. |
| `reference_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 4b -- Placeholder normalization` stage. |
| `cols` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 4b -- Placeholder normalization` stage. |
| `key_cols` | positional_or_keyword | No | `None` | `list[str] | None` | Input used by the `Step 4b -- Placeholder normalization` stage. |

??? note "Function source"

    ```python
    def restore_to_vanilla(
        current_df  : pl.DataFrame,
        reference_df: pl.DataFrame,
        cols        : list[str],
        key_cols    : list[str] | None = None,
    ) -> pl.DataFrame:
        """
        For every cell where the reference contains a #placeholder# token, overwrite
        the current questionnaire's value with the reference (vanilla) value.

        This prevents placeholder-filled country values from being flagged as deviations.
        key_cols: join keys -- defaults to ["Q Name"]; use ["Q Name", "option_name"] for options.
        cols    : columns to restore (e.g. ["label", "constraint"] or ["option_label"]).
        """
        if key_cols is None:
            key_cols = ["Q Name"]
        result = current_df
        for col in cols:
            if col not in reference_df.columns or col not in current_df.columns:
                continue
            ref_ph = (
                reference_df
                .filter(pl.col(col).str.contains(r'#[^#]+#'))
                .select(key_cols + [col])
                .rename({col: "__ref_vanilla__"})
            )
            if ref_ph.height == 0:
                continue
            result = (
                result
                .join(ref_ph, on=key_cols, how="left")
                .with_columns(
                    pl.when(pl.col("__ref_vanilla__").is_not_null())
                    .then(pl.col("__ref_vanilla__"))
                    .otherwise(pl.col(col))
                    .alias(col)
                )
                .drop("__ref_vanilla__")
            )
        return result
    ```

### `apply_replacements` {#fn-apply-replacements-1395}

**Pipeline stage:** `Step 4b -- Placeholder normalization`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1395`

**Signature**

```python
def apply_replacements(df: pl.DataFrame, pairs: dict[str, str], cols: list[str]) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Apply #placeholder# -> actual_value replacements to specified columns (re-personalise after comparison).

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `pairs` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 4b -- Placeholder normalization` stage. |
| `cols` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 4b -- Placeholder normalization` stage. |

??? note "Function source"

    ```python
    def apply_replacements(
        df   : pl.DataFrame,
        pairs: dict[str, str],
        cols : list[str],
    ) -> pl.DataFrame:
        """Apply #placeholder# -> actual_value replacements to specified columns (re-personalise after comparison)."""
        if not pairs:
            return df
        result = df
        for col in cols:
            if col not in result.columns:
                continue
            expr = pl.col(col)
            for key, val in sorted(pairs.items(), key=lambda kv: len(kv[0]), reverse=True):
                expr = expr.str.replace_all(key, val, literal=True)
            result = result.with_columns(expr.alias(col))
        return result
    ```

### `read_crop_choice_rows_for_compare_with_status` {#fn-read-crop-choice-rows-for-compare-with-status-1421}

**Pipeline stage:** `Step 4b -- Placeholder normalization`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1421`

**Signature**

```python
def read_crop_choice_rows_for_compare_with_status(country_path: str, language: str) -> tuple[dict[str, list[tuple[str, str]]], dict]:
```

**Returns:** `tuple[dict[str, list[tuple[str, str]]], dict]`

**What it does:** Read current questionnaire Crop list and build rows for crop/crop2/crop3 replacement.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `country_path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def read_crop_choice_rows_for_compare_with_status(
        country_path: str,
        language: str,
    ) -> tuple[dict[str, list[tuple[str, str]]], dict]:
        """Read current questionnaire Crop list and build rows for crop/crop2/crop3 replacement."""
        status = {
            "sheet_found": False,
            "headers_found": False,
            "selected_count": 0,
            "candidate_count": 0,
            "status": "FAIL",
            "severity": "high",
            "message": "Crop list sheet not found",
        }
        try:
            wb = openpyxl.load_workbook(country_path, data_only=True, read_only=True)
            if "Crop list" not in wb.sheetnames:
                wb.close()
                return {}, status
            status["sheet_found"] = True
            rows = list(wb["Crop list"].iter_rows(values_only=True))
            wb.close()
        except Exception as e:
            status["message"] = f"Could not read Crop list sheet: {e}"
            return {}, status

        if len(rows) < 3:
            status["message"] = "Crop list sheet has no crop rows"
            return {}, status

        headers = [str(h).strip() if h is not None else "" for h in rows[2]]
        sel_idx = next((i for i, h in enumerate(headers) if "Select top" in h), None)
        code_idx = next((i for i, h in enumerate(headers) if "Dataset code" in h), None)
        if language == "fr":
            lbl_idx = next((i for i, h in enumerate(headers) if "Label" in h and "FR" in h), None)
        elif language == "ar":
            lbl_idx = next((i for i, h in enumerate(headers) if "Label" in h and "AR" in h), None)
        elif language == "es":
            lbl_idx = next((i for i, h in enumerate(headers) if "Label" in h and "ES" in h), None)
        else:
            lbl_idx = next((i for i, h in enumerate(headers) if "Label" in h and "EN" in h), None)

        if code_idx is None or lbl_idx is None:
            status["message"] = "Crop list headers missing Dataset code / language label"
            return {}, status
        status["headers_found"] = True

        selected, unselected = [], []
        for row in rows[3:]:
            code = row[code_idx] if code_idx < len(row) else None
            lbl = row[lbl_idx] if lbl_idx < len(row) else None
            sel = row[sel_idx] if sel_idx is not None and sel_idx < len(row) else None
            if code is None or str(code).strip() in ("", "nan"):
                continue
            entry = (str(code).strip(), str(lbl or "").strip())
            (selected if sel is not None and str(sel).strip() else unselected).append(entry)

        selected.sort(key=lambda x: x[0])
        unselected.sort(key=lambda x: x[0])
        combined = selected + unselected
        status["selected_count"] = len(selected)
        status["candidate_count"] = len(combined)
        if len(selected) == 10:
            status["status"] = "PASS"
            status["severity"] = "pass"
            status["message"] = f"10 crops selected (OK) out of {len(combined)} candidates"
        elif len(selected) == 0:
            status["status"] = "FAIL"
            status["severity"] = "high"
            status["message"] = f"No crops selected (0/10) out of {len(combined)} candidates"
        elif len(selected) < 10:
            status["status"] = "WARN"
            status["severity"] = "medium"
            status["message"] = f"Only {len(selected)}/10 crops selected out of {len(combined)} candidates"
        else:
            status["status"] = "WARN"
            status["severity"] = "medium"
            status["message"] = f"{len(selected)}/10 crops selected (more than expected) out of {len(combined)} candidates"

        return ({name: combined + specials for name, specials in _CROP_SPECIALS_COMPARE.items()}, status)
    ```

### `read_crop_choice_rows_for_compare` {#fn-read-crop-choice-rows-for-compare-1503}

**Pipeline stage:** `Step 4b -- Placeholder normalization`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1503`

**Signature**

```python
def read_crop_choice_rows_for_compare(country_path: str, language: str) -> dict[str, list[tuple[str, str]]]:
```

**Returns:** `dict[str, list[tuple[str, str]]]`

**What it does:** Implements logic in the `Step 4b -- Placeholder normalization` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `country_path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def read_crop_choice_rows_for_compare(country_path: str, language: str) -> dict[str, list[tuple[str, str]]]:
        rows, _ = read_crop_choice_rows_for_compare_with_status(country_path, language)
        return rows
    ```

### `fetch_admin_choice_rows_for_compare` {#fn-fetch-admin-choice-rows-for-compare-1508}

**Pipeline stage:** `Step 4b -- Placeholder normalization`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1508`

**Signature**

```python
def fetch_admin_choice_rows_for_compare(iso3: str, include_admin3: bool=False) -> dict[str, list[tuple]]:
```

**Returns:** `dict[str, list[tuple]]`

**What it does:** Fetch admin rows from AGOL for comparison preprocessing.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `iso3` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4b -- Placeholder normalization` stage. |
| `include_admin3` | positional_or_keyword | No | `False` | `bool` | Input used by the `Step 4b -- Placeholder normalization` stage. |

??? note "Function source"

    ```python
    def fetch_admin_choice_rows_for_compare(iso3: str, include_admin3: bool = False) -> dict[str, list[tuple]]:
        """Fetch admin rows from AGOL for comparison preprocessing."""
        try:
            import urllib.request as _urlreq
            import json as _json

            _BASE_ADMIN12 = ("https://services5.arcgis.com/sjP4Ugu5s0dZWLjd/arcgis/rest/services"
                             "/Administrative_Boundaries_Reference_(view_layer)/FeatureServer")
            _BASE_ADMIN3 = ("https://services5.arcgis.com/sjP4Ugu5s0dZWLjd/arcgis/rest/services"
                            "/Reference_Admin_3_(view_layer)/FeatureServer")

            def _get_admin12(layer, fields):
                url = (f"{_BASE_ADMIN12}/{layer}/query"
                       f"?where=adm0_ISO3+%3D+%27{iso3}%27"
                       f"&outFields={fields}&returnGeometry=false&outSR=4326&f=json")
                with _urlreq.urlopen(url, timeout=30) as r:
                    return _json.loads(r.read().decode())["features"]

            def _get_admin3(fields):
                url = (f"{_BASE_ADMIN3}/0/query"
                       f"?where=adm0_ISO3+%3D+%27{iso3}%27"
                       f"&outFields={fields}&returnGeometry=false&outSR=4326&f=json")
                with _urlreq.urlopen(url, timeout=30) as r:
                    return _json.loads(r.read().decode())["features"]

            adm1 = sorted(
                [(f["attributes"]["adm1_pcode"], f["attributes"]["adm1_name"])
                 for f in _get_admin12(1, "adm1_name,adm1_pcode")],
                key=lambda x: x[0],
            )
            adm2 = sorted(
                [(f["attributes"]["adm2_pcode"], f["attributes"]["adm2_name"], f["attributes"]["adm1_pcode"])
                 for f in _get_admin12(0, "adm2_name,adm2_pcode,adm1_pcode")],
                key=lambda x: x[0],
            )
            rows = {"admin1": adm1, "admin2": adm2}

            if include_admin3:
                try:
                    adm3 = sorted(
                        [(f["attributes"]["adm3_pcode"], f["attributes"]["adm3_name"], f["attributes"]["adm2_pcode"])
                         for f in _get_admin3("adm3_name,adm3_pcode,adm2_pcode")],
                        key=lambda x: x[0],
                    )
                    rows["admin3"] = adm3
                    print(f"AGOL compare rows loaded: admin1={len(adm1)} admin2={len(adm2)} admin3={len(adm3)}")
                except Exception as e:
                    print(f"Warning: AGOL admin3 fetch failed during compare preprocessing: {e}")
                    print(f"AGOL compare rows loaded: admin1={len(adm1)} admin2={len(adm2)} admin3=0")
            else:
                print(f"AGOL compare rows loaded: admin1={len(adm1)} admin2={len(adm2)} (admin3 skipped)")
            return rows
        except Exception as e:
            print(f"Warning: AGOL fetch failed during compare preprocessing: {e}")
            return {}
    ```

### `replace_choice_lists_for_compare` {#fn-replace-choice-lists-for-compare-1565}

**Pipeline stage:** `Step 4b -- Placeholder normalization`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1565`

**Signature**

```python
def replace_choice_lists_for_compare(choices_df: pl.DataFrame, country_rows: dict[str, list[tuple]]) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Replace selected list_name blocks in choices_df with provided rows.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `choices_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `country_rows` | positional_or_keyword | Yes | `-` | `dict[str, list[tuple]]` | Input used by the `Step 4b -- Placeholder normalization` stage. |

??? note "Function source"

    ```python
    def replace_choice_lists_for_compare(choices_df: pl.DataFrame, country_rows: dict[str, list[tuple]]) -> pl.DataFrame:
        """Replace selected list_name blocks in choices_df with provided rows."""
        if not country_rows:
            return choices_df

        skip = list(country_rows.keys())
        kept = choices_df.filter(~pl.col("list_name").is_in(skip)) if choices_df.height > 0 else choices_df

        recs = []
        for list_name, entries in country_rows.items():
            for entry in entries:
                recs.append({
                    "list_name": str(list_name),
                    "option_name": str(entry[0]),
                    "option_label": str(entry[1] if len(entry) > 1 else ""),
                })

        new_df = (
            pl.DataFrame(recs)
            if recs else
            pl.DataFrame(schema={"list_name": pl.Utf8, "option_name": pl.Utf8, "option_label": pl.Utf8})
        )

        if kept.height == 0:
            return new_df
        if new_df.height == 0:
            return kept
        return pl.concat([kept, new_df], how="vertical")
    ```

### `_add_replacement_input_issue` {#fn--add-replacement-input-issue-1601}

**Pipeline stage:** `Step 4b -- Placeholder normalization`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1601`

**Signature**

```python
def _add_replacement_input_issue(issue_type: str, field: str, current: str, reference: str, severity: str='high', q_name: str='', list_name: str='', option_name: str='', excel_row: int | None=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 4b -- Placeholder normalization` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `issue_type` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4b -- Placeholder normalization` stage. |
| `field` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4b -- Placeholder normalization` stage. |
| `current` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4b -- Placeholder normalization` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4b -- Placeholder normalization` stage. |
| `severity` | positional_or_keyword | No | `'high'` | `str` | Severity label used for final issue classification. |
| `q_name` | positional_or_keyword | No | `''` | `str` | Question identifier used to join or compare records. |
| `list_name` | positional_or_keyword | No | `''` | `str` | Input used by the `Step 4b -- Placeholder normalization` stage. |
| `option_name` | positional_or_keyword | No | `''` | `str` | Input used by the `Step 4b -- Placeholder normalization` stage. |
| `excel_row` | positional_or_keyword | No | `None` | `int | None` | Input used by the `Step 4b -- Placeholder normalization` stage. |

??? note "Function source"

    ```python
    def _add_replacement_input_issue(
        issue_type: str,
        field: str,
        current: str,
        reference: str,
        severity: str = "high",
        q_name: str = "",
        list_name: str = "",
        option_name: str = "",
        excel_row: int | None = None,
    ):
        _replacement_input_issues_rows.append({
            "issue_type": issue_type,
            "set_name": "",
            "Q Name": q_name,
            "list_name": list_name,
            "option_name": option_name,
            "field": field,
            "current": current,
            "reference": reference,
            "severity": severity,
            "excel_row": excel_row,
        })
    ```

### `_count_hash_placeholders_in_text_df` {#fn--count-hash-placeholders-in-text-df-1625}

**Pipeline stage:** `Step 4b -- Placeholder normalization`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1625`

**Signature**

```python
def _count_hash_placeholders_in_text_df(df: pl.DataFrame, cols: list[str]) -> int:
```

**Returns:** `int`

**What it does:** Implements logic in the `Step 4b -- Placeholder normalization` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `cols` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 4b -- Placeholder normalization` stage. |

??? note "Function source"

    ```python
    def _count_hash_placeholders_in_text_df(df: pl.DataFrame, cols: list[str]) -> int:
        if df is None or df.height == 0:
            return 0
        total = 0
        for c in cols:
            if c not in df.columns:
                continue
            total += df.filter(pl.col(c).cast(pl.Utf8).fill_null("").str.contains(r"#[^#]+#")).height
        return int(total)
    ```

### `normalize_text_expr` {#fn-normalize-text-expr-1882}

**Pipeline stage:** `Step 5 -- Normalisation helpers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1882`

**Signature**

```python
def normalize_text_expr(col_name: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Implements logic in the `Step 5 -- Normalisation helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 5 -- Normalisation helpers` stage. |

??? note "Function source"

    ```python
    def normalize_text_expr(col_name: str) -> pl.Expr:
        return (
            pl.col(col_name).cast(pl.Utf8).fill_null("")
            .str.to_lowercase()
            .str.replace_all(r"[^\w\s]", "")
            .str.replace_all(r"\s+", " ")
            .str.strip_chars()
        )
    ```

### `normalize_simple_expr` {#fn-normalize-simple-expr-1892}

**Pipeline stage:** `Step 5 -- Normalisation helpers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1892`

**Signature**

```python
def normalize_simple_expr(col_name: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Implements logic in the `Step 5 -- Normalisation helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 5 -- Normalisation helpers` stage. |

??? note "Function source"

    ```python
    def normalize_simple_expr(col_name: str) -> pl.Expr:
        return (
            pl.col(col_name).cast(pl.Utf8).fill_null("")
            .str.to_lowercase()
            .str.replace_all(r"\s+", " ")
            .str.strip_chars()
        )
    ```

### `normalize_logic_expr` {#fn-normalize-logic-expr-1901}

**Pipeline stage:** `Step 5 -- Normalisation helpers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1901`

**Signature**

```python
def normalize_logic_expr(col_name: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Implements logic in the `Step 5 -- Normalisation helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 5 -- Normalisation helpers` stage. |

??? note "Function source"

    ```python
    def normalize_logic_expr(col_name: str) -> pl.Expr:
        return (
            pl.col(col_name).cast(pl.Utf8).fill_null("")
            .str.to_lowercase()
            .str.replace_all(r"\s+", " ")
            .str.replace_all(r"\s*([=<>!+\-*/(),])\s*", "$1")
            .str.strip_chars()
        )
    ```

### `compare_question_presence` {#fn-compare-question-presence-1916}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1916`

**Signature**

```python
def compare_question_presence(current, reference):
```

**Returns:** `None or implicit return`

**What it does:** Returns (added, removed). Each row has is_optional flag.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def compare_question_presence(current, reference):
        """Returns (added, removed). Each row has is_optional flag."""
        key = "Q Name"
        added = (
            current.select([key])
            .join(reference.select([key]), on=key, how="anti")
            .with_columns(_custom_qname_expr(key).alias("is_optional"))
        )
        removed = (
            reference.select([key])
            .join(current.select([key]), on=key, how="anti")
            .with_columns(_custom_qname_expr(key).alias("is_optional"))
        )
        return added, removed
    ```

### `compare_mandatory_kobo` {#fn-compare-mandatory-kobo-1932}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1932`

**Signature**

```python
def compare_mandatory_kobo(current, reference):
```

**Returns:** `None or implicit return`

**What it does:** Compare mandatory_category between current and reference.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def compare_mandatory_kobo(current, reference):
        """Compare mandatory_category between current and reference."""
        EMPTY = {
            "issue_type": pl.Utf8, "Q Name": pl.Utf8, "field": pl.Utf8,
            "Mandatory": pl.Utf8, "Mandatory_ref": pl.Utf8, "excel_row": pl.Int64,
        }
        if "mandatory_category" not in current.columns or "mandatory_category" not in reference.columns:
            return pl.DataFrame(schema=EMPTY)

        meaningful = {"mandatory", "mandatory-panel", "optional", "non-mandatory"}
        return (
            current.select(["Q Name", "mandatory_category", "excel_row"])
            .join(reference.select(["Q Name", "mandatory_category"]), on="Q Name", how="inner", suffix="_ref")
            .filter(
                pl.col("mandatory_category").is_in(list(meaningful)) |
                pl.col("mandatory_category_ref").is_in(list(meaningful))
            )
            .filter(pl.col("mandatory_category") != pl.col("mandatory_category_ref"))
            .with_columns([
                pl.lit("mandatory_column_mismatch").alias("issue_type"),
                pl.lit("mandatory_category").alias("field"),
            ])
            .rename({"mandatory_category": "Mandatory", "mandatory_category_ref": "Mandatory_ref"})
            .select(["issue_type", "Q Name", "field", "Mandatory", "Mandatory_ref", "excel_row"])
        )
    ```

### `validate_mandatory_category_unrecognized` {#fn-validate-mandatory-category-unrecognized-1970}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:1970`

**Signature**

```python
def validate_mandatory_category_unrecognized(survey: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Current-file-only authoring consistency check: flags a 'Mandatory' value

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `survey` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def validate_mandatory_category_unrecognized(survey: pl.DataFrame) -> pl.DataFrame:
        """
        Current-file-only authoring consistency check: flags a 'Mandatory' value
        that doesn't match any of the template's known categories -- usually a
        typo (e.g. a bare 'no' instead of 'no - low priority').
        """
        schema = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if "mandatory_raw" not in survey.columns:
            return pl.DataFrame(schema=schema)

        rows = []
        for r in survey.select(["Q Name", "mandatory_raw", "excel_row"]).iter_rows(named=True):
            raw = str(r.get("mandatory_raw") or "").strip()
            if not raw or raw.lower() in _KNOWN_MANDATORY_VALUES:
                continue
            rows.append({
                "issue_type": "mandatory_category_unrecognized",
                "set_name": "", "Q Name": r.get("Q Name"), "field": "Mandatory",
                "current": raw,
                "reference": "known categories: " + " | ".join(sorted(_KNOWN_MANDATORY_VALUES)),
                "severity": "medium", "excel_row": r.get("excel_row"),
            })

        return pl.DataFrame(rows, schema=schema) if rows else pl.DataFrame(schema=schema)
    ```

### `compare_list_name_changes` {#fn-compare-list-name-changes-2000}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2000`

**Signature**

```python
def compare_list_name_changes(current, reference):
```

**Returns:** `None or implicit return`

**What it does:** Flag questions where the choices list (list_name from type) changed.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def compare_list_name_changes(current, reference):
        """Flag questions where the choices list (list_name from type) changed."""
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        cur = current.filter(pl.col("list_name").is_not_null()).select(["Q Name", "list_name", "excel_row"])
        ref = reference.filter(pl.col("list_name").is_not_null()).select(["Q Name", "list_name"])
        result = (
            cur.join(ref, on="Q Name", how="inner", suffix="_ref")
            .with_columns([
                _normalized_list_expr("list_name").alias("_list_norm"),
                _normalized_list_expr("list_name_ref").alias("_list_norm_ref"),
            ])
            .filter(pl.col("_list_norm") != pl.col("_list_norm_ref"))
            .with_columns([
                pl.lit("choices_list_changed").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("type (list_name)").alias("field"),
                pl.col("list_name").alias("current"),
                pl.col("list_name_ref").alias("reference"),
                pl.lit("medium").alias("severity"),
            ])
            .drop(["_list_norm", "_list_norm_ref"])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
        return result if result.height > 0 else pl.DataFrame(schema=EMPTY)
    ```

### `compare_question_labels` {#fn-compare-question-labels-2030}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2030`

**Signature**

```python
def compare_question_labels(current_vanilla, reference, current_orig=None, language: str='en'):
```

**Returns:** `None or implicit return`

**What it does:** Compare question label text across both English and the target language.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_vanilla` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `current_orig` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `language` | positional_or_keyword | No | `'en'` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def compare_question_labels(current_vanilla, reference, current_orig=None, language: str = "en"):
        """
        Compare question label text across both English and the target language.

        current_vanilla: current survey with #placeholder# tokens restored (avoids false positives on
                         target-language labels; EN labels are taken as-is from the questionnaire).
        current_orig   : original current survey — used so the report shows actual filled-in values.
        language       : configured language code (e.g. "en", "ar", "fr").

        When language != "en" and label_en is present in both DataFrames, the function compares
        both columns independently and sets lang_scope to "EN only", "<LANG> only", or
        "EN + <LANG>" so the report clearly identifies which language(s) have a mismatch.
        """
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "current_lang": pl.Utf8, "reference_lang": pl.Utf8,
            "lang_scope": pl.Utf8, "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if "label" not in current_vanilla.columns or "label" not in reference.columns:
            return pl.DataFrame(schema=EMPTY)

        _lang = str(language or "en").strip().lower()
        _lang_tag = _lang.upper()
        dual = (
            _lang != "en"
            and "label_en" in current_vanilla.columns
            and "label_en" in reference.columns
        )

        if dual:
            joined = (
                current_vanilla.select(["Q Name", "label", "label_en", "excel_row"])
                .join(
                    reference.select(["Q Name", "label", "label_en"]),
                    on="Q Name", how="inner", suffix="_ref",
                )
                .with_columns([
                    normalize_text_expr("label").alias("_norm_tgt"),
                    normalize_text_expr("label_ref").alias("_norm_tgt_ref"),
                    normalize_text_expr("label_en").alias("_norm_en"),
                    normalize_text_expr("label_en_ref").alias("_norm_en_ref"),
                ])
            )
            _en_diff = (pl.col("_norm_en") != pl.col("_norm_en_ref")) & (pl.col("label_en_ref") != "")
            _tgt_diff = (pl.col("_norm_tgt") != pl.col("_norm_tgt_ref")) & (pl.col("label_ref") != "")
            diff = (
                joined
                .filter(_en_diff | _tgt_diff)
                .drop(["_norm_tgt", "_norm_tgt_ref", "_norm_en", "_norm_en_ref"])
            )
            if diff.height == 0:
                return pl.DataFrame(schema=EMPTY)

            # Replace vanilla labels with actual filled-in values for display
            if current_orig is not None:
                orig_cols = {"Q Name"}
                if "label" in current_orig.columns:
                    orig_cols.add("label")
                if "label_en" in current_orig.columns:
                    orig_cols.add("label_en")
                if len(orig_cols) > 1:
                    orig = current_orig.select(list(orig_cols))
                    rename_map = {}
                    if "label" in orig_cols:
                        rename_map["label"] = "_actual_tgt"
                    if "label_en" in orig_cols:
                        rename_map["label_en"] = "_actual_en"
                    orig = orig.rename(rename_map)
                    diff = diff.join(orig, on="Q Name", how="left")
                    if "_actual_tgt" in diff.columns:
                        diff = diff.with_columns(
                            pl.when(pl.col("_actual_tgt").is_not_null())
                            .then(pl.col("_actual_tgt"))
                            .otherwise(pl.col("label"))
                            .alias("label")
                        ).drop("_actual_tgt")
                    if "_actual_en" in diff.columns:
                        diff = diff.with_columns(
                            pl.when(pl.col("_actual_en").is_not_null())
                            .then(pl.col("_actual_en"))
                            .otherwise(pl.col("label_en"))
                            .alias("label_en")
                        ).drop("_actual_en")

            # Recompute diff flags on the (possibly orig-substituted) display values
            _en_diff_disp = (
                (normalize_text_expr("label_en").str.strip_chars() != normalize_text_expr("label_en_ref").str.strip_chars())
                & (pl.col("label_en_ref").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
            )
            _tgt_diff_disp = (
                (normalize_text_expr("label").str.strip_chars() != normalize_text_expr("label_ref").str.strip_chars())
                & (pl.col("label_ref").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
            )
            return (
                diff
                .with_columns([
                    pl.lit("label_mismatch").alias("issue_type"),
                    pl.lit("").alias("set_name"),
                    pl.lit("label").alias("field"),
                    pl.col("label_en").cast(pl.Utf8).fill_null("").alias("current"),
                    pl.col("label_en_ref").cast(pl.Utf8).fill_null("").alias("reference"),
                    pl.col("label").cast(pl.Utf8).fill_null("").alias("current_lang"),
                    pl.col("label_ref").cast(pl.Utf8).fill_null("").alias("reference_lang"),
                    pl.when(_en_diff_disp & _tgt_diff_disp).then(pl.lit(f"EN + {_lang_tag}"))
                    .when(_en_diff_disp).then(pl.lit("EN only"))
                    .when(_tgt_diff_disp).then(pl.lit(f"{_lang_tag} only"))
                    .otherwise(pl.lit(""))
                    .alias("lang_scope"),
                    pl.lit("medium").alias("severity"),
                ])
                .select(["issue_type", "set_name", "Q Name", "field",
                         "current", "reference", "current_lang", "reference_lang",
                         "lang_scope", "severity", "excel_row"])
            )

        # Single-language path: EN questionnaire or label_en not available in both DataFrames
        diff = (
            current_vanilla.select(["Q Name", "label", "excel_row"])
            .join(reference.select(["Q Name", "label"]), on="Q Name", how="inner", suffix="_ref")
            .with_columns([
                normalize_text_expr("label").alias("_norm"),
                normalize_text_expr("label_ref").alias("_norm_ref"),
            ])
            .filter((pl.col("_norm") != pl.col("_norm_ref")) & (pl.col("label_ref") != ""))
            .drop(["_norm", "_norm_ref"])
        )
        if diff.height == 0:
            return pl.DataFrame(schema=EMPTY)

        if current_orig is not None and "label" in current_orig.columns:
            orig = current_orig.select(["Q Name", "label"]).rename({"label": "_actual"})
            diff = (
                diff.join(orig, on="Q Name", how="left")
                .with_columns(
                    pl.when(pl.col("_actual").is_not_null())
                    .then(pl.col("_actual"))
                    .otherwise(pl.col("label"))
                    .alias("label")
                )
                .drop("_actual")
            )

        return (
            diff
            .with_columns([
                pl.lit("label_mismatch").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("label").alias("field"),
                pl.col("label").alias("current"),
                pl.col("label_ref").alias("reference"),
                pl.lit("").alias("current_lang"),
                pl.lit("").alias("reference_lang"),
                pl.lit("").alias("lang_scope"),
                pl.lit("medium").alias("severity"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field",
                     "current", "reference", "current_lang", "reference_lang",
                     "lang_scope", "severity", "excel_row"])
        )
    ```

### `compare_constraint_changes` {#fn-compare-constraint-changes-2192}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2192`

**Signature**

```python
def compare_constraint_changes(current_vanilla, reference, current_orig=None):
```

**Returns:** `None or implicit return`

**What it does:** Compare constraint expressions.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_vanilla` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `current_orig` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def compare_constraint_changes(current_vanilla, reference, current_orig=None):
        """
        Compare constraint expressions.
        Uses vanilla current so #placeholder#-containing constraints are not flagged.
        """
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if "constraint" not in current_vanilla.columns or "constraint" not in reference.columns:
            return pl.DataFrame(schema=EMPTY)

        diff = (
            current_vanilla
            .select(["Q Name", "constraint", "excel_row"])
            .join(
                reference.select(["Q Name", "constraint"]),
                on="Q Name", how="inner", suffix="_ref",
            )
            .with_columns([
                normalize_logic_expr("constraint").alias("_norm"),
                normalize_logic_expr("constraint_ref").alias("_norm_ref"),
            ])
            .filter((pl.col("_norm") != pl.col("_norm_ref")) & ((pl.col("_norm") != "") | (pl.col("_norm_ref") != "")))
            .drop(["_norm", "_norm_ref"])
        )
        if diff.height == 0:
            return pl.DataFrame(schema=EMPTY)

        if current_orig is not None and "constraint" in current_orig.columns:
            orig_c = current_orig.select(["Q Name", "constraint"]).rename({"constraint": "_actual"})
            diff = (
                diff.join(orig_c, on="Q Name", how="left")
                .with_columns(
                    pl.when(pl.col("_actual").is_not_null())
                    .then(pl.col("_actual"))
                    .otherwise(pl.col("constraint"))
                    .alias("constraint")
                )
                .drop("_actual")
            )

        return (
            diff
            .with_columns([
                pl.lit("constraint_modified").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("constraint").alias("field"),
                pl.col("constraint").alias("current"),
                pl.col("constraint_ref").alias("reference"),
                pl.lit("medium").alias("severity"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `validate_constraint_removed_for_mandatory` {#fn-validate-constraint-removed-for-mandatory-2249}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2249`

**Signature**

```python
def validate_constraint_removed_for_mandatory(current_vanilla: pl.DataFrame, reference: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** High-severity, narrow sibling of compare_constraint_changes(): flags only

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_vanilla` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def validate_constraint_removed_for_mandatory(
        current_vanilla: pl.DataFrame,
        reference: pl.DataFrame,
    ) -> pl.DataFrame:
        """
        High-severity, narrow sibling of compare_constraint_changes(): flags only
        the case where the reference has a constraint expression and the current
        questionnaire dropped it entirely on a mandatory/mandatory-panel question.
        Cosmetic rewording of constraint is still handled separately by
        compare_constraint_changes() at medium severity.
        """
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if "constraint" not in current_vanilla.columns or "constraint" not in reference.columns:
            return pl.DataFrame(schema=EMPTY)
        if "mandatory_category" not in current_vanilla.columns:
            return pl.DataFrame(schema=EMPTY)

        joined = (
            current_vanilla
            .select(["Q Name", "constraint", "mandatory_category", "excel_row"])
            .join(
                reference.select(["Q Name", "constraint"]),
                on="Q Name", how="inner", suffix="_ref",
            )
            .with_columns([
                pl.col("constraint").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_curr"),
                pl.col("constraint_ref").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_ref"),
            ])
            .filter(
                (pl.col("_ref") != "")
                & (pl.col("_curr") == "")
                & pl.col("mandatory_category").is_in(["mandatory", "mandatory-panel"])
            )
        )
        if joined.height == 0:
            return pl.DataFrame(schema=EMPTY)

        return (
            joined
            .with_columns([
                pl.lit("constraint_removed_mandatory").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("constraint").alias("field"),
                pl.lit("(blank)").alias("current"),
                pl.col("_ref").alias("reference"),
                pl.lit("high").alias("severity"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `compare_required_changes` {#fn-compare-required-changes-2304}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2304`

**Signature**

```python
def compare_required_changes(current, reference):
```

**Returns:** `None or implicit return`

**What it does:** Compare required column with whitespace/case-tolerant normalization.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def compare_required_changes(current, reference):
        """Compare required column with whitespace/case-tolerant normalization."""
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if "required" not in current.columns or "required" not in reference.columns:
            return pl.DataFrame(schema=EMPTY)

        diff = (
            current.select(["Q Name", "required", "excel_row"])
            .join(reference.select(["Q Name", "required"]), on="Q Name", how="inner", suffix="_ref")
            .with_columns([
                normalize_simple_expr("required").alias("_norm"),
                normalize_simple_expr("required_ref").alias("_norm_ref"),
            ])
            .filter((pl.col("_norm") != pl.col("_norm_ref")) & ((pl.col("_norm") != "") | (pl.col("_norm_ref") != "")))
            .drop(["_norm", "_norm_ref"])
        )
        if diff.height == 0:
            return pl.DataFrame(schema=EMPTY)

        return (
            diff
            .with_columns([
                pl.lit("required_modified").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("required").alias("field"),
                pl.col("required").alias("current"),
                pl.col("required_ref").alias("reference"),
                pl.lit("medium").alias("severity"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `compare_choice_filter_changes` {#fn-compare-choice-filter-changes-2341}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2341`

**Signature**

```python
def compare_choice_filter_changes(current, reference):
```

**Returns:** `None or implicit return`

**What it does:** Compare choice_filter with expression normalization to avoid cosmetic false positives.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def compare_choice_filter_changes(current, reference):
        """Compare choice_filter with expression normalization to avoid cosmetic false positives."""
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if "choice_filter" not in current.columns or "choice_filter" not in reference.columns:
            return pl.DataFrame(schema=EMPTY)

        diff = (
            current.select(["Q Name", "choice_filter", "excel_row"])
            .join(reference.select(["Q Name", "choice_filter"]), on="Q Name", how="inner", suffix="_ref")
            .with_columns([
                normalize_logic_expr("choice_filter").alias("_norm"),
                normalize_logic_expr("choice_filter_ref").alias("_norm_ref"),
            ])
            .filter((pl.col("_norm") != pl.col("_norm_ref")) & ((pl.col("_norm") != "") | (pl.col("_norm_ref") != "")))
            .drop(["_norm", "_norm_ref"])
        )
        if diff.height == 0:
            return pl.DataFrame(schema=EMPTY)

        return (
            diff
            .with_columns([
                pl.lit("choice_filter_modified").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("choice_filter").alias("field"),
                pl.col("choice_filter").alias("current"),
                pl.col("choice_filter_ref").alias("reference"),
                pl.lit("medium").alias("severity"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `compare_appearance_changes` {#fn-compare-appearance-changes-2378}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2378`

**Signature**

```python
def compare_appearance_changes(current, reference):
```

**Returns:** `None or implicit return`

**What it does:** Compare appearance with expression normalization that ignores tiny spacing differences.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def compare_appearance_changes(current, reference):
        """Compare appearance with expression normalization that ignores tiny spacing differences."""
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if "appearance" not in current.columns or "appearance" not in reference.columns:
            return pl.DataFrame(schema=EMPTY)

        diff = (
            current.select(["Q Name", "appearance", "excel_row"])
            .join(reference.select(["Q Name", "appearance"]), on="Q Name", how="inner", suffix="_ref")
            .with_columns([
                normalize_logic_expr("appearance").alias("_norm"),
                normalize_logic_expr("appearance_ref").alias("_norm_ref"),
            ])
            .filter((pl.col("_norm") != pl.col("_norm_ref")) & ((pl.col("_norm") != "") | (pl.col("_norm_ref") != "")))
            .drop(["_norm", "_norm_ref"])
        )
        if diff.height == 0:
            return pl.DataFrame(schema=EMPTY)

        return (
            diff
            .with_columns([
                pl.lit("appearance_modified").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("appearance").alias("field"),
                pl.col("appearance").alias("current"),
                pl.col("appearance_ref").alias("reference"),
                pl.lit("medium").alias("severity"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `compare_calculation_changes` {#fn-compare-calculation-changes-2415}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2415`

**Signature**

```python
def compare_calculation_changes(current, reference):
```

**Returns:** `None or implicit return`

**What it does:** Compare calculation with expression normalization that ignores tiny spacing differences.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def compare_calculation_changes(current, reference):
        """Compare calculation with expression normalization that ignores tiny spacing differences."""
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if "calculation" not in current.columns or "calculation" not in reference.columns:
            return pl.DataFrame(schema=EMPTY)

        diff = (
            current.select(["Q Name", "calculation", "excel_row"])
            .join(reference.select(["Q Name", "calculation"]), on="Q Name", how="inner", suffix="_ref")
            .with_columns([
                normalize_logic_expr("calculation").alias("_norm"),
                normalize_logic_expr("calculation_ref").alias("_norm_ref"),
            ])
            .filter((pl.col("_norm") != pl.col("_norm_ref")) & ((pl.col("_norm") != "") | (pl.col("_norm_ref") != "")))
            .drop(["_norm", "_norm_ref"])
        )
        if diff.height == 0:
            return pl.DataFrame(schema=EMPTY)

        return (
            diff
            .with_columns([
                pl.lit("calculation_modified").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("calculation").alias("field"),
                pl.col("calculation").alias("current"),
                pl.col("calculation_ref").alias("reference"),
                pl.lit("medium").alias("severity"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `_normalize_qtype_value_kobo` {#fn--normalize-qtype-value-kobo-2453}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2453`

**Signature**

```python
def _normalize_qtype_value_kobo(value: str) -> str:
```

**Returns:** `str`

**What it does:** Canonicalize KoBo Q Type text so cosmetic formatting does not trigger false positives.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def _normalize_qtype_value_kobo(value: str) -> str:
        """Canonicalize KoBo Q Type text so cosmetic formatting does not trigger false positives."""
        s = str(value or "").strip().lower()
        if not s:
            return ""
        s = re.sub(r"[\\/_-]+", " ", s)
        s = re.sub(r"\s+", " ", s).strip()
        if s in {"select one", "single choice"}:
            return "single choice"
        if s in {"select multiple", "select all that apply"}:
            return "select all that apply"
        return s
    ```

### `_qtype_mode_kobo` {#fn--qtype-mode-kobo-2467}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2467`

**Signature**

```python
def _qtype_mode_kobo(value: str) -> str:
```

**Returns:** `str`

**What it does:** Classify Q Type into compatibility families.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def _qtype_mode_kobo(value: str) -> str:
        """Classify Q Type into compatibility families."""
        t = _normalize_qtype_value_kobo(value)
        if not t:
            return ""
        if t == "select all that apply":
            return "multi_select"
        if t == "single choice":
            return "single_select"
        if "select one" in t:
            return "single_select"
        if "select multiple" in t:
            return "multi_select"
        return "non_option"
    ```

### `_is_known_qtype_value_kobo` {#fn--is-known-qtype-value-kobo-2503}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2503`

**Signature**

```python
def _is_known_qtype_value_kobo(value: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 6 -- Comparison functions` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def _is_known_qtype_value_kobo(value: str) -> bool:
        t = _normalize_qtype_value_kobo(value)
        if not t:
            return False
        if t in _KOBO_KNOWN_QTYPES_NORMALIZED:
            return True
        if t.startswith("select one") or t.startswith("select multiple"):
            return True
        return False
    ```

### `_qtype_change_severity_kobo` {#fn--qtype-change-severity-kobo-2514}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2514`

**Signature**

```python
def _qtype_change_severity_kobo(curr_mode: str, ref_mode: str, curr_option_count: int, ref_option_count: int, curr_type_norm: str, ref_type_norm: str, curr_type_known: bool, ref_type_known: bool) -> str:
```

**Returns:** `str`

**What it does:** Severity policy (independent of mandatory status):

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `curr_mode` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 6 -- Comparison functions` stage. |
| `ref_mode` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 6 -- Comparison functions` stage. |
| `curr_option_count` | positional_or_keyword | Yes | `-` | `int` | Input used by the `Step 6 -- Comparison functions` stage. |
| `ref_option_count` | positional_or_keyword | Yes | `-` | `int` | Input used by the `Step 6 -- Comparison functions` stage. |
| `curr_type_norm` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 6 -- Comparison functions` stage. |
| `ref_type_norm` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 6 -- Comparison functions` stage. |
| `curr_type_known` | positional_or_keyword | Yes | `-` | `bool` | Input used by the `Step 6 -- Comparison functions` stage. |
| `ref_type_known` | positional_or_keyword | Yes | `-` | `bool` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def _qtype_change_severity_kobo(
        curr_mode: str,
        ref_mode: str,
        curr_option_count: int,
        ref_option_count: int,
        curr_type_norm: str,
        ref_type_norm: str,
        curr_type_known: bool,
        ref_type_known: bool,
    ) -> str:
        """
        Severity policy (independent of mandatory status):
        - HIGH for incompatible/invalid transitions
        - MEDIUM for compatible type changes
        """
        cm = str(curr_mode or "")
        rm = str(ref_mode or "")
        modes = {cm, rm}
        curr_t = str(curr_type_norm or "").strip()
        ref_t = str(ref_type_norm or "").strip()

        # Invalid: current is blank while reference has a defined type.
        if (not curr_t) and ref_t:
            return "high"

        # Invalid: unknown/unlisted Q Type token on either side.
        if curr_t and (not bool(curr_type_known)):
            return "high"
        if ref_t and (not bool(ref_type_known)):
            return "high"

        # Incompatible family change: single <-> multi.
        if "single_select" in modes and "multi_select" in modes:
            return "high"

        # Incompatible option-bearing <-> non-option mode.
        if "non_option" in modes and (("single_select" in modes) or ("multi_select" in modes)):
            return "high"

        # Invalid option-count correctness checks:
        # option-bearing questions should normally have at least 2 options.
        curr_option_like = cm in {"single_select", "multi_select"}
        ref_option_like = rm in {"single_select", "multi_select"}
        if curr_option_like and int(curr_option_count or 0) <= 1:
            return "high"
        if ref_option_like and int(ref_option_count or 0) <= 1:
            return "high"
        if (cm == "non_option") and int(curr_option_count or 0) > 0:
            return "high"
        if (rm == "non_option") and int(ref_option_count or 0) > 0:
            return "high"

        return "medium"
    ```

### `compare_type_changes` {#fn-compare-type-changes-2569}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2569`

**Signature**

```python
def compare_type_changes(current, reference, current_options: pl.DataFrame | None=None, reference_options: pl.DataFrame | None=None):
```

**Returns:** `None or implicit return`

**What it does:** Risk-based Q Type comparison with normalization and integrity checks.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `current_options` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |
| `reference_options` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def compare_type_changes(
        current,
        reference,
        current_options: pl.DataFrame | None = None,
        reference_options: pl.DataFrame | None = None,
    ):
        """Risk-based Q Type comparison with normalization and integrity checks."""
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if "Q Type" not in current.columns or "Q Type" not in reference.columns:
            return pl.DataFrame(schema=EMPTY)

        if current_options is not None and current_options.height > 0 and "Q Name" in current_options.columns:
            _cur_opt_counts = current_options.group_by("Q Name").agg(pl.len().alias("_curr_opt_n"))
        else:
            _cur_opt_counts = pl.DataFrame(schema={"Q Name": pl.Utf8, "_curr_opt_n": pl.Int64})

        if reference_options is not None and reference_options.height > 0 and "Q Name" in reference_options.columns:
            _ref_opt_counts = reference_options.group_by("Q Name").agg(pl.len().alias("_ref_opt_n"))
        else:
            _ref_opt_counts = pl.DataFrame(schema={"Q Name": pl.Utf8, "_ref_opt_n": pl.Int64})

        result = (
            current.select(["Q Name", "Q Type", "excel_row"])
            .join(reference.select(["Q Name", "Q Type"]), on="Q Name", how="inner", suffix="_ref")
            .with_columns([
                pl.col("Q Type").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Q Type"),
                pl.col("Q Type_ref").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Q Type_ref"),
            ])
            .with_columns([
                pl.col("Q Type").map_elements(_normalize_qtype_value_kobo, return_dtype=pl.Utf8).alias("_type_norm"),
                pl.col("Q Type_ref").map_elements(_normalize_qtype_value_kobo, return_dtype=pl.Utf8).alias("_type_norm_ref"),
                pl.col("Q Type").map_elements(_qtype_mode_kobo, return_dtype=pl.Utf8).alias("_type_mode"),
                pl.col("Q Type_ref").map_elements(_qtype_mode_kobo, return_dtype=pl.Utf8).alias("_type_mode_ref"),
                pl.col("Q Type").map_elements(_is_known_qtype_value_kobo, return_dtype=pl.Boolean).alias("_type_known"),
                pl.col("Q Type_ref").map_elements(_is_known_qtype_value_kobo, return_dtype=pl.Boolean).alias("_type_known_ref"),
            ])
            .join(_cur_opt_counts, on="Q Name", how="left")
            .join(_ref_opt_counts, on="Q Name", how="left")
            .with_columns([
                pl.col("_curr_opt_n").fill_null(0).cast(pl.Int64),
                pl.col("_ref_opt_n").fill_null(0).cast(pl.Int64),
            ])
            .filter(pl.col("_type_norm") != pl.col("_type_norm_ref"))
            .with_columns(
                pl.struct([
                    "_type_mode", "_type_mode_ref", "_curr_opt_n", "_ref_opt_n",
                    "_type_norm", "_type_norm_ref", "_type_known", "_type_known_ref",
                ])
                .map_elements(
                    lambda r: _qtype_change_severity_kobo(
                        r.get("_type_mode"),
                        r.get("_type_mode_ref"),
                        r.get("_curr_opt_n"),
                        r.get("_ref_opt_n"),
                        r.get("_type_norm"),
                        r.get("_type_norm_ref"),
                        bool(r.get("_type_known")),
                        bool(r.get("_type_known_ref")),
                    ),
                    return_dtype=pl.Utf8,
                )
                .alias("severity")
            )
            .with_columns([
                pl.lit("type_changed").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("type").alias("field"),
                pl.col("Q Type").alias("current"),
                pl.col("Q Type_ref").alias("reference"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
        return result if result.height > 0 else pl.DataFrame(schema=EMPTY)
    ```

### `_canonical_option_key_expr` {#fn--canonical-option-key-expr-2647}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2647`

**Signature**

```python
def _canonical_option_key_expr(col_name: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Canonical option key: strip spaces and treat integer-like decimals as same key (1 == 1.0).

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def _canonical_option_key_expr(col_name: str) -> pl.Expr:
        """Canonical option key: strip spaces and treat integer-like decimals as same key (1 == 1.0)."""
        return pl.col(col_name).map_elements(_canonical_option_name_token, return_dtype=pl.Utf8)
    ```

### `compare_option_labels_single` {#fn-compare-option-labels-single-2652}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2652`

**Signature**

```python
def compare_option_labels_single(current_opts, reference_opts, lang_scope='EN'):
```

**Returns:** `None or implicit return`

**What it does:** Option label text changes for matching canonical Q Name + option_name.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `lang_scope` | positional_or_keyword | No | `'EN'` | `-` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def compare_option_labels_single(current_opts, reference_opts, lang_scope="EN"):
        """Option label text changes for matching canonical Q Name + option_name."""
        cur = current_opts.with_columns([
            pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.to_lowercase().alias("_qk"),
            _canonical_option_key_expr("option_name").alias("_ok"),
        ]).filter(
            pl.col("_qk").is_not_null() & (pl.col("_qk") != "") &
            pl.col("_ok").is_not_null() & (pl.col("_ok") != "")
        )
        ref = reference_opts.with_columns([
            pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.to_lowercase().alias("_qk"),
            _canonical_option_key_expr("option_name").alias("_ok"),
        ]).filter(
            pl.col("_qk").is_not_null() & (pl.col("_qk") != "") &
            pl.col("_ok").is_not_null() & (pl.col("_ok") != "")
        )
        return (
            cur
            .join(ref, on=["_qk", "_ok"], how="inner", suffix="_ref")
            .with_columns([
                normalize_text_expr("option_label").alias("_norm"),
                normalize_text_expr("option_label_ref").alias("_norm_ref"),
            ])
            .filter(pl.col("_norm") != pl.col("_norm_ref"))
            .drop(["_norm", "_norm_ref", "_qk", "_ok"])
            .with_columns([
                pl.lit("choice_label_mismatch").alias("issue_type"),
                pl.concat_str([pl.lit("option_"), pl.col("option_name")]).alias("field"),
                pl.lit("medium").alias("severity"),
                pl.lit(lang_scope).alias("lang_scope"),
                pl.lit(None).cast(pl.Int64).alias("excel_row"),
            ])
            .select(["issue_type", "Q Name", "list_name", "option_name", "field", "option_label", "option_label_ref",
                     "severity", "excel_row", "lang_scope"])
        )
    ```

### `compare_option_presence_single` {#fn-compare-option-presence-single-2689}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2689`

**Signature**

```python
def compare_option_presence_single(current_opts, reference_opts, lang_scope='EN'):
```

**Returns:** `None or implicit return`

**What it does:** Added / removed options for matching canonical Q Name + option_name.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `lang_scope` | positional_or_keyword | No | `'EN'` | `-` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def compare_option_presence_single(current_opts, reference_opts, lang_scope="EN"):
        """Added / removed options for matching canonical Q Name + option_name."""
        cur = current_opts.with_columns([
            pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.to_lowercase().alias("_qk"),
            _canonical_option_key_expr("option_name").alias("_ok"),
        ]).filter(
            pl.col("_qk").is_not_null() & (pl.col("_qk") != "") &
            pl.col("_ok").is_not_null() & (pl.col("_ok") != "")
        )
        ref = reference_opts.with_columns([
            pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.to_lowercase().alias("_qk"),
            _canonical_option_key_expr("option_name").alias("_ok"),
        ]).filter(
            pl.col("_qk").is_not_null() & (pl.col("_qk") != "") &
            pl.col("_ok").is_not_null() & (pl.col("_ok") != "")
        )
        key_cols = ["_qk", "_ok"]
        removed = (
            ref.select(key_cols + ["Q Name", "list_name", "option_name", "option_label"])
            .join(cur.select(key_cols), on=key_cols, how="anti")
            .drop(["_qk", "_ok"])
            .with_columns([
                pl.lit("removed_choice").alias("issue_type"),
                pl.concat_str([pl.lit("option_"), pl.col("option_name")]).alias("field"),
                pl.lit("high").alias("severity"),
                pl.lit(lang_scope).alias("lang_scope"),
            ])
            .select(["issue_type", "Q Name", "list_name", "option_name", "field", "option_label", "severity", "lang_scope"])
        )
        added = (
            cur.select(key_cols + ["Q Name", "list_name", "option_name", "option_label"])
            .join(ref.select(key_cols), on=key_cols, how="anti")
            .drop(["_qk", "_ok"])
            .with_columns([
                pl.lit("added_choice").alias("issue_type"),
                pl.concat_str([pl.lit("option_"), pl.col("option_name")]).alias("field"),
                pl.lit("high").alias("severity"),
                pl.lit(lang_scope).alias("lang_scope"),
            ])
            .select(["issue_type", "Q Name", "list_name", "option_name", "field", "option_label", "severity", "lang_scope"])
        )
        return added, removed
    ```

### `compare_option_name_renumber_single` {#fn-compare-option-name-renumber-single-2733}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2733`

**Signature**

```python
def compare_option_name_renumber_single(current_opts, reference_opts, lang_scope='EN'):
```

**Returns:** `None or implicit return`

**What it does:** Detect choice-name renumbering for the same normalized label within the same question.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 6 -- Comparison functions` stage. |
| `lang_scope` | positional_or_keyword | No | `'EN'` | `-` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def compare_option_name_renumber_single(current_opts, reference_opts, lang_scope="EN"):
        """
        Detect choice-name renumbering for the same normalized label within the same question.

        Example:
          reference: name=4, label="REFUSED"
          current  : name=3, label="REFUSED"

        We only emit when label->name mapping is 1:1 on both sides to avoid
        ambiguous many-to-many matches.
        """
        cur = current_opts.with_columns([
            pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.to_lowercase().alias("_qk"),
            normalize_text_expr("option_label").alias("_lk"),
            _canonical_option_key_expr("option_name").alias("_ok"),
        ]).filter(
            pl.col("_qk").is_not_null() & (pl.col("_qk") != "") &
            pl.col("_lk").is_not_null() & (pl.col("_lk") != "") &
            pl.col("_ok").is_not_null() & (pl.col("_ok") != "")
        )
        ref = reference_opts.with_columns([
            pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.to_lowercase().alias("_qk"),
            normalize_text_expr("option_label").alias("_lk"),
            _canonical_option_key_expr("option_name").alias("_ok"),
        ]).filter(
            pl.col("_qk").is_not_null() & (pl.col("_qk") != "") &
            pl.col("_lk").is_not_null() & (pl.col("_lk") != "") &
            pl.col("_ok").is_not_null() & (pl.col("_ok") != "")
        )

        cur_map = (
            cur
            .group_by(["_qk", "_lk"])
            .agg([
                pl.col("Q Name").first().alias("Q Name"),
                pl.col("list_name").first().alias("list_name"),
                pl.col("_ok").n_unique().alias("cur_n_names"),
                pl.col("_ok").first().alias("new_option_name_key"),
                pl.col("option_name").first().alias("new_option_name"),
                pl.col("option_label").first().alias("option_label"),
            ])
        )
        ref_map = (
            ref
            .group_by(["_qk", "_lk"])
            .agg([
                pl.col("_ok").n_unique().alias("ref_n_names"),
                pl.col("_ok").first().alias("old_option_name_key"),
                pl.col("option_name").first().alias("old_option_name"),
                pl.col("option_label").first().alias("option_label_ref"),
            ])
        )

        return (
            cur_map
            .join(ref_map, on=["_qk", "_lk"], how="inner")
            .filter(
                (pl.col("cur_n_names") == 1)
                & (pl.col("ref_n_names") == 1)
                & (pl.col("new_option_name_key") != pl.col("old_option_name_key"))
            )
            .with_columns([
                pl.lit("option_index_drift").alias("issue_type"),
                pl.concat_str([
                    pl.lit("name_"),
                    pl.col("old_option_name").cast(pl.Utf8),
                    pl.lit("_to_"),
                    pl.col("new_option_name").cast(pl.Utf8),
                ]).alias("field"),
                pl.col("new_option_name").cast(pl.Utf8).alias("option_name"),
                pl.lit("high").alias("severity"),
                pl.lit(None).cast(pl.Int64).alias("excel_row"),
                pl.lit(lang_scope).alias("lang_scope"),
            ])
            .select([
                "issue_type", "Q Name", "list_name", "option_name", "field",
                "new_option_name", "old_option_name",
                "option_label", "option_label_ref",
                "severity", "excel_row", "lang_scope",
            ])
        )
    ```

### `compare_hint_changes` {#fn-compare-hint-changes-2816}

**Pipeline stage:** `Step 6 -- Comparison functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2816`

**Signature**

```python
def compare_hint_changes(current: pl.DataFrame, reference: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Flag questions where the hint text differs from the template (medium severity).

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 6 -- Comparison functions` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 6 -- Comparison functions` stage. |

??? note "Function source"

    ```python
    def compare_hint_changes(current: pl.DataFrame, reference: pl.DataFrame) -> pl.DataFrame:
        """Flag questions where the hint text differs from the template (medium severity)."""
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        ref_hints = reference.filter(pl.col("hint") != "").select(["Q Name", "hint"])
        if ref_hints.is_empty():
            return pl.DataFrame(schema=EMPTY)
        joined = (
            current.select(["Q Name", "hint", "excel_row"])
            .join(ref_hints, on="Q Name", how="inner", suffix="_ref")
            .filter(pl.col("hint") != pl.col("hint_ref"))
        )
        if joined.is_empty():
            return pl.DataFrame(schema=EMPTY)
        return (
            joined.with_columns([
                pl.lit("hint_changed").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.col("hint").alias("current"),
                pl.col("hint_ref").alias("reference"),
                pl.lit("medium").alias("severity"),
                pl.lit("hint").alias("field"),
            ])
            .select(list(EMPTY.keys()))
        )
    ```

### `_has_broken_hash_placeholder_token` {#fn--has-broken-hash-placeholder-token-2859}

**Pipeline stage:** `Step 7 -- Relevant validation (KoBO skip logic)`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2859`

**Signature**

```python
def _has_broken_hash_placeholder_token(text: str) -> bool:
```

**Returns:** `bool`

**What it does:** Detect malformed hash placeholders by stripping valid #...# tokens

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 -- Relevant validation (KoBO skip logic)` stage. |

??? note "Function source"

    ```python
    def _has_broken_hash_placeholder_token(text: str) -> bool:
        """
        Detect malformed hash placeholders by stripping valid #...# tokens
        and checking for leftover hash markers.

        Examples caught:
          - '#token' (missing closing #)
          - 'token#' (dangling closing #)
          - '##' (empty token)
        """
        txt = str(text or "")
        if "#" not in txt:
            return False
        stripped = _HASH_TOKEN_RE.sub("", txt)
        # Avoid false positives for common language names such as C# / F#.
        stripped_compact = re.sub(r"\s+", "", stripped).lower()
        if stripped_compact in {"c#", "f#"}:
            return False
        return "#" in stripped
    ```

### `_has_malformed_kobo_ref_token` {#fn--has-malformed-kobo-ref-token-2880}

**Pipeline stage:** `Step 7 -- Relevant validation (KoBO skip logic)`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2880`

**Signature**

```python
def _has_malformed_kobo_ref_token(text: str) -> bool:
```

**Returns:** `bool`

**What it does:** Detect malformed KoBo reference syntax:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 -- Relevant validation (KoBO skip logic)` stage. |

??? note "Function source"

    ```python
    def _has_malformed_kobo_ref_token(text: str) -> bool:
        """
        Detect malformed KoBo reference syntax:
          - '${var' (missing closing brace)
          - '${}'   (empty reference)
        """
        txt = str(text or "")
        if "${" not in txt:
            return False
        if re.search(r"\$\{\s*\}", txt):
            return True
        stripped = _KOBO_REF_RE.sub("", txt)
        return "${" in stripped
    ```

### `validate_relevant` {#fn-validate-relevant-2895}

**Pipeline stage:** `Step 7 -- Relevant validation (KoBO skip logic)`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2895`

**Signature**

```python
def validate_relevant(current_survey: pl.DataFrame, reference_survey: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Layer 1a - broken_relevant_reference (high): ${var} points to a name not in the survey at all

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_survey` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_survey` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def validate_relevant(
        current_survey : pl.DataFrame,
        reference_survey: pl.DataFrame,
    ) -> pl.DataFrame:
        """
        Layer 1a - broken_relevant_reference (high): ${var} points to a name not in the survey at all
        Layer 1b - relevant_inexact_reference (high): exact name missing but o_<name> exists in survey
                    (reference is broken in KoBO; note helps debugging)
        Layer 2  - relevant_modified (medium): expression changed from template
        """
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }

        curr_qnames = set(current_survey["Q Name"].to_list())

        # Build lookup: stripped core name -> custom name for all custom-prefixed questions
        _optional_by_core: dict[str, str] = {
            re.sub(_CUSTOM_QNAME_RE, "", qn): qn for qn in curr_qnames if qn.startswith(CUSTOM_QNAME_PREFIXES)
        }

        cur_rows = {r["Q Name"]: r for r in
                    current_survey.select(["Q Name", "relevant", "excel_row"]).iter_rows(named=True)}
        ref_rows = {r["Q Name"]: r for r in
                    reference_survey.select(["Q Name", "relevant"]).iter_rows(named=True)}

        issues = []
        for qname, cr in cur_rows.items():
            relevant  = str(cr.get("relevant") or "").strip()
            excel_row = cr.get("excel_row")

            refs = _KOBO_REF_RE.findall(relevant) if relevant else []
            broken = [v for v in refs if v not in curr_qnames]

            has_high_relevant_issue = False
            if broken:
                truly_missing = [v for v in broken if v not in _optional_by_core]
                has_similar   = [v for v in broken if v in _optional_by_core]

                if truly_missing:
                    has_high_relevant_issue = True
                    issues.append({
                        "issue_type": "broken_relevant_reference",
                        "set_name": "", "Q Name": qname, "field": "relevant",
                        "current"  : relevant,
                        "reference": f"missing variables: {truly_missing}",
                        "severity" : "high", "excel_row": excel_row,
                    })

                for v in has_similar:
                    has_high_relevant_issue = True
                    similar = _optional_by_core[v]
                    issues.append({
                        "issue_type": "relevant_inexact_reference",
                        "set_name": "", "Q Name": qname, "field": "relevant",
                        "current"  : relevant,
                        "reference": f"${{{v}}} not found; {similar!r} exists with similar name",
                        "severity" : "high", "excel_row": excel_row,
                    })

            # Layer 2: changed from template (only when no high relevant integrity issue).
            # Apply only when question exists in BOTH files.
            # (Added questions should be checked structurally, not compared as template drift.)
            ref_relevant = str(ref_rows.get(qname, {}).get("relevant") or "").strip()
            if (not has_high_relevant_issue) and (qname in ref_rows) and (ref_relevant != relevant):
                issues.append({
                    "issue_type": "relevant_modified",
                    "set_name": "", "Q Name": qname, "field": "relevant",
                    "current"  : relevant,
                    "reference": ref_relevant,
                    "severity" : "medium", "excel_row": excel_row,
                })

        if not issues:
            return pl.DataFrame(schema=EMPTY)
        return pl.DataFrame(issues).unique(
            subset=["issue_type", "Q Name", "field", "current", "reference"], keep="first"
        )
    ```

### `validate_choice_label_language_completeness` {#fn-validate-choice-label-language-completeness-2977}

**Pipeline stage:** `Step 7 -- Relevant validation (KoBO skip logic)`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:2977`

**Signature**

```python
def validate_choice_label_language_completeness(path: str, target_language: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 7 -- Relevant validation (KoBO skip logic)` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |
| `target_language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def validate_choice_label_language_completeness(path: str, target_language: str) -> pl.DataFrame:
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        lang = str(target_language or "").strip().lower()
        if not path or lang == "en":
            return pl.DataFrame(schema=EMPTY)

        try:
            wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
        except Exception:
            return pl.DataFrame(schema=EMPTY)

        try:
            if "choices" not in wb.sheetnames:
                return pl.DataFrame(schema=EMPTY)
            ws = wb["choices"]
            rows = list(ws.iter_rows(values_only=True))
            if not rows:
                return pl.DataFrame(schema=EMPTY)

            headers = [str(h).strip() if h is not None else "" for h in rows[0]]
            idx = {h: i for i, h in enumerate(headers) if h}
            list_col = idx.get("list_name")
            name_col = idx.get("name")
            en_col = idx.get(LANG_LABEL_COL.get("en", "label::English (en)"))
            tgt_header = LANG_LABEL_COL.get(lang, f"label::{target_language}")
            tgt_col = idx.get(tgt_header)
            if list_col is None or name_col is None or en_col is None:
                return pl.DataFrame(schema=EMPTY)

            records: list[dict] = []
            for excel_row, row in enumerate(rows[1:], start=2):
                list_name = str((row[list_col] if list_col < len(row) else "") or "").strip()
                option_name = str((row[name_col] if name_col < len(row) else "") or "").strip()
                if not list_name or not option_name:
                    continue
                en_label = str((row[en_col] if en_col < len(row) else "") or "").strip()
                tgt_label = str((row[tgt_col] if tgt_col is not None and tgt_col < len(row) else "") or "").strip()
                if bool(en_label) == bool(tgt_label):
                    continue
                records.append({
                    "issue_type": "choice_missing_bilingual_label",
                    "set_name": "questionnaire_structure",
                    "Q Name": "",
                    "field": "choices bilingual label completeness",
                    "current": (
                        f"list={list_name} | name={option_name} | "
                        f"EN='{en_label}' | {lang.upper()}='{tgt_label}'"
                    ),
                    "reference": f"Both English and {lang.upper()} choice labels should be filled together",
                    "severity": "high",
                    "excel_row": excel_row,
                })
            return pl.DataFrame(records) if records else pl.DataFrame(schema=EMPTY)
        finally:
            wb.close()
    ```

### `validate_questionnaire_structure` {#fn-validate-questionnaire-structure-3038}

**Pipeline stage:** `Step 7 -- Relevant validation (KoBO skip logic)`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3038`

**Signature**

```python
def validate_questionnaire_structure(current_survey: pl.DataFrame, current_choices: pl.DataFrame | None=None, template_survey: pl.DataFrame | None=None, replacement_pairs: dict[str, str] | None=None, choices_label_completeness_issues: pl.DataFrame | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Structural checks for token/placeholder integrity in survey text/formula fields.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_survey` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `current_choices` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |
| `template_survey` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |
| `replacement_pairs` | positional_or_keyword | No | `None` | `dict[str, str] | None` | Input used by the `Step 7 -- Relevant validation (KoBO skip logic)` stage. |
| `choices_label_completeness_issues` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def validate_questionnaire_structure(
        current_survey: pl.DataFrame,
        current_choices: pl.DataFrame | None = None,
        template_survey: pl.DataFrame | None = None,
        replacement_pairs: dict[str, str] | None = None,
        choices_label_completeness_issues: pl.DataFrame | None = None,
    ) -> pl.DataFrame:
        """
        Structural checks for token/placeholder integrity in survey text/formula fields.
        - duplicate Q Name in survey
        - duplicate (list_name, name) in choices/options
        - malformed #...# placeholder syntax
        - #token# unresolved against template placeholders + Additional information
        - #token# that looks like a survey variable (likely ${var} expected)
        - malformed ${...} KoBo reference syntax
        - loose $var syntax (likely ${var} expected)
        - ${var} missing from survey (outside relevant column checks)
        """
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        _fields = [c for c in ["label", "hint", "constraint", "calculation"] if c in current_survey.columns]
        has_text_fields = bool(_fields)

        curr_qnames = set(current_survey["Q Name"].to_list())
        issues = []

        # 0) Structural duplicate checks
        if current_survey.height > 0 and "Q Name" in current_survey.columns:
            dup_q = (
                current_survey
                .select(["Q Name", "excel_row"])
                .with_columns(pl.col("Q Name").cast(pl.Utf8).str.strip_chars().alias("_q"))
                .filter(pl.col("_q") != "")
                .group_by("_q")
                .agg([
                    pl.len().alias("_n"),
                    pl.col("excel_row").max().alias("_row"),
                ])
                .filter(pl.col("_n") > 1)
            )
            for rr in dup_q.iter_rows(named=True):
                issues.append({
                    "issue_type": "duplicate_qname",
                    "set_name": "questionnaire_structure",
                    "Q Name": rr["_q"],
                    "field": "Q Name",
                    "current": rr["_q"],
                    "reference": f"Duplicate question name appears {rr['_n']} times",
                    "severity": "high",
                    "excel_row": rr["_row"],
                })

        if (
            current_choices is not None
            and current_choices.height > 0
            and {"list_name", "option_name"}.issubset(set(current_choices.columns))
        ):
            dup_opts = (
                current_choices
                .select(["list_name", "option_name"])
                .with_columns([
                    pl.col("list_name").cast(pl.Utf8).str.strip_chars().alias("_list"),
                    pl.col("option_name").cast(pl.Utf8).str.strip_chars().alias("_name"),
                ])
                .filter((pl.col("_list") != "") & (pl.col("_name") != ""))
                .group_by(["_list", "_name"])
                .agg([
                    pl.len().alias("_n"),
                ])
                .filter(pl.col("_n") > 1)
            )
            for rr in dup_opts.iter_rows(named=True):
                issues.append({
                    "issue_type": "duplicate_choice_name",
                    "set_name": "questionnaire_structure",
                    "Q Name": "",
                    "field": "choices",
                    "current": f"{rr['_list']} / {rr['_name']}",
                    "reference": f"Duplicate (list_name, name) appears {rr['_n']} times",
                    "severity": "high",
                    "excel_row": None,
                })

        if choices_label_completeness_issues is not None and choices_label_completeness_issues.height > 0:
            issues.extend(choices_label_completeness_issues.to_dicts())

        if not has_text_fields:
            return pl.DataFrame(issues) if issues else pl.DataFrame(schema=EMPTY)

        # Tokens considered resolvable: known in template OR in Additional information pairs.
        known_tokens = set()
        if template_survey is not None and template_survey.height > 0:
            tpl_fields = [c for c in _fields if c in template_survey.columns]
            if tpl_fields:
                for row in template_survey.select(tpl_fields).iter_rows(named=True):
                    for f in tpl_fields:
                        txt = str(row.get(f) or "")
                        for tok in _HASH_TOKEN_RE.findall(txt):
                            known_tokens.add(f"#{tok}#")
        if replacement_pairs:
            known_tokens |= set(replacement_pairs.keys())
        known_tokens_l = {t.lower() for t in known_tokens}

        iter_cols = ["Q Name", "excel_row"] + _fields
        for row in current_survey.select(iter_cols).iter_rows(named=True):
            qname = row.get("Q Name", "")
            excel_row = row.get("excel_row")
            for field in _fields:
                txt = str(row.get(field) or "").strip()
                if not txt:
                    continue

                # 1) malformed #...# placeholders
                if _has_broken_hash_placeholder_token(txt):
                    issues.append({
                        "issue_type": "replacement_malformed_placeholder",
                        "set_name": "questionnaire_structure",
                        "Q Name": qname,
                        "field": field,
                        "current": txt[:220],
                        "reference": "Malformed placeholder token; use balanced #token# syntax",
                        "severity": "medium",
                        "excel_row": excel_row,
                    })

                # 1) #token# checks
                for tok in _HASH_TOKEN_RE.findall(txt):
                    full = f"#{tok}#"
                    tok_core = str(tok).strip()

                    if tok_core in curr_qnames:
                        issues.append({
                            "issue_type": "placeholder_should_use_kobo_ref",
                            "set_name": "questionnaire_structure",
                            "Q Name": qname,
                            "field": field,
                            "current": txt[:220],
                            "reference": f"{full} matches survey variable '{tok_core}' - use ${{{tok_core}}}",
                            "severity": "high",
                            "excel_row": excel_row,
                        })
                    elif full.lower() not in known_tokens_l:
                        issues.append({
                            "issue_type": "placeholder_not_found",
                            "set_name": "questionnaire_structure",
                            "Q Name": qname,
                            "field": field,
                            "current": txt[:220],
                            "reference": f"{full} not in template placeholders or Additional information",
                            "severity": "high",
                            "excel_row": excel_row,
                        })

                # 2) malformed ${...} checks
                if _has_malformed_kobo_ref_token(txt):
                    issues.append({
                        "issue_type": "kobo_ref_malformed_syntax",
                        "set_name": "questionnaire_structure",
                        "Q Name": qname,
                        "field": field,
                        "current": txt[:220],
                        "reference": "Malformed KoBo reference; use ${var} with non-empty, closed braces",
                        "severity": "high",
                        "excel_row": excel_row,
                    })

                # 3) $var (missing braces) checks
                for m in _LOOSE_DOLLAR_RE.findall(txt):
                    var = m[1:]
                    if var in curr_qnames:
                        ref = f"{m} uses loose syntax; use ${{{var}}}"
                        sev = "high"
                    else:
                        ref = f"{m} uses loose syntax; expected ${{var}} format"
                        sev = "medium"
                    issues.append({
                        "issue_type": "kobo_ref_loose_syntax",
                        "set_name": "questionnaire_structure",
                        "Q Name": qname,
                        "field": field,
                        "current": txt[:220],
                        "reference": ref,
                        "severity": sev,
                        "excel_row": excel_row,
                    })

                # 4) ${var} checks (outside relevant field)
                for v in _KOBO_REF_RE.findall(txt):
                    v = str(v or "").strip()
                    if not v:
                        # Empty ${} is handled as malformed syntax above.
                        continue
                    if v not in curr_qnames:
                        issues.append({
                            "issue_type": "kobo_ref_missing_variable",
                            "set_name": "questionnaire_structure",
                            "Q Name": qname,
                            "field": field,
                            "current": txt[:220],
                            "reference": f"${{{v}}} not found in survey Q Name",
                            "severity": "high",
                            "excel_row": excel_row,
                        })

        if not issues:
            return pl.DataFrame(schema=EMPTY)
        return pl.DataFrame(issues).unique(
            subset=["issue_type", "Q Name", "field", "current", "reference"], keep="first"
        )
    ```

### `_module_rows_from_survey` {#fn--module-rows-from-survey-3252}

**Pipeline stage:** `Step 7 -- Relevant validation (KoBO skip logic)`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3252`

**Signature**

```python
def _module_rows_from_survey(survey_df: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 7 -- Relevant validation (KoBO skip logic)` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `survey_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def _module_rows_from_survey(survey_df: pl.DataFrame) -> pl.DataFrame:
        schema = {
            "module_key_norm": pl.Utf8,
            "module_key": pl.Utf8,
            "module": pl.Utf8,
            "module_en": pl.Utf8,
            "excel_row": pl.Int64,
        }
        if (
            survey_df is None
            or survey_df.height == 0
            or "module_key" not in survey_df.columns
            or "module" not in survey_df.columns
        ):
            return pl.DataFrame(schema=schema)

        has_module_en = "module_en" in survey_df.columns
        select_cols = ["module_key_norm", "module_key", "module", "excel_row"]
        if has_module_en:
            select_cols = ["module_key_norm", "module_key", "module", "module_en", "excel_row"]

        rows = (
            survey_df
            .with_columns(_normalized_module_expr("module_key").alias("module_key_norm"))
            .filter(pl.col("module_key_norm") != "")
            .with_columns(
                pl.when(pl.col("module").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
                .then(pl.col("module").cast(pl.Utf8))
                .otherwise(pl.col("module_key").cast(pl.Utf8))
                .alias("module")
            )
            .select(select_cols)
        )
        if rows.height == 0:
            return pl.DataFrame(schema=schema)

        agg_exprs = [
            pl.col("module_key").first().alias("module_key"),
            pl.col("module").first().alias("module"),
            pl.col("excel_row").min().alias("excel_row"),
        ]
        if has_module_en:
            agg_exprs.append(pl.col("module_en").first().alias("module_en"))

        result = (
            rows
            .sort(["module_key_norm", "excel_row"])
            .group_by("module_key_norm")
            .agg(agg_exprs)
        )
        if "module_en" not in result.columns:
            result = result.with_columns(pl.lit("").alias("module_en"))
        return result
    ```

### `validate_module_presence` {#fn-validate-module-presence-3307}

**Pipeline stage:** `Step 7 -- Relevant validation (KoBO skip logic)`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3307`

**Signature**

```python
def validate_module_presence(current_survey: pl.DataFrame, reference_survey: pl.DataFrame, template_survey: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Module integrity checks:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_survey` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_survey` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `template_survey` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def validate_module_presence(
        current_survey: pl.DataFrame,
        reference_survey: pl.DataFrame,
        template_survey: pl.DataFrame,
    ) -> pl.DataFrame:
        """
        Module integrity checks:
        - module_removed (high): template module missing in current (always enforced)
        - module_added (info): current module absent from selected reference
        """
        schema = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "module": pl.Utf8, "module_en": pl.Utf8, "field": pl.Utf8,
            "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }

        cur_mod = _module_rows_from_survey(current_survey)
        ref_mod = _module_rows_from_survey(reference_survey)
        tpl_mod = _module_rows_from_survey(template_survey)

        cur_keys = set(cur_mod["module_key_norm"].to_list()) if cur_mod.height > 0 else set()
        ref_keys = set(ref_mod["module_key_norm"].to_list()) if ref_mod.height > 0 else set()
        tpl_keys = set(tpl_mod["module_key_norm"].to_list()) if tpl_mod.height > 0 else set()

        cur_map = {r["module_key_norm"]: r for r in cur_mod.to_dicts()} if cur_mod.height > 0 else {}
        ref_map = {r["module_key_norm"]: r for r in ref_mod.to_dicts()} if ref_mod.height > 0 else {}
        tpl_map = {r["module_key_norm"]: r for r in tpl_mod.to_dicts()} if tpl_mod.height > 0 else {}

        rows: list[dict] = []

        for key in sorted(tpl_keys - cur_keys):
            src = tpl_map.get(key, {})
            module_label = str(src.get("module") or src.get("module_key") or key)
            module_label_en = str(src.get("module_en") or module_label)
            module_key = str(src.get("module_key") or key)
            rows.append({
                "issue_type": "module_removed",
                "set_name": "questionnaire_structure",
                "Q Name": "",
                "module": module_label,
                "module_en": module_label_en,
                "field": "module",
                "current": "missing_in_current",
                "reference": f"Required by template: {module_key}",
                "severity": "high",
                "excel_row": src.get("excel_row"),
            })

        for key in sorted(cur_keys - ref_keys):
            src = cur_map.get(key, {})
            module_label = str(src.get("module") or src.get("module_key") or key)
            module_label_en = str(src.get("module_en") or module_label)
            module_key = str(src.get("module_key") or key)
            rows.append({
                "issue_type": "module_added",
                "set_name": "questionnaire_structure",
                "Q Name": "",
                "module": module_label,
                "module_en": module_label_en,
                "field": "module",
                "current": f"present: {module_key}",
                "reference": "missing_in_reference",
                "severity": "info",
                "excel_row": src.get("excel_row"),
            })

        return pl.DataFrame(rows, schema=schema) if rows else pl.DataFrame(schema=schema)
    ```

### `_attach_module_column_to_issues` {#fn--attach-module-column-to-issues-3377}

**Pipeline stage:** `Step 7 -- Relevant validation (KoBO skip logic)`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3377`

**Signature**

```python
def _attach_module_column_to_issues(issues_df: pl.DataFrame, current_survey: pl.DataFrame, reference_survey: pl.DataFrame, template_survey: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Populate per-row module label from question name lookup.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `issues_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 7 -- Relevant validation (KoBO skip logic)` stage. |
| `current_survey` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_survey` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `template_survey` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def _attach_module_column_to_issues(
        issues_df: pl.DataFrame,
        current_survey: pl.DataFrame,
        reference_survey: pl.DataFrame,
        template_survey: pl.DataFrame,
    ) -> pl.DataFrame:
        """
        Populate per-row module label from question name lookup.
        Existing non-empty module values (e.g. module-level issues) are preserved.
        """
        if issues_df is None or issues_df.height == 0:
            if issues_df is None:
                return pl.DataFrame(schema={"module": pl.Utf8})
            if "module" not in issues_df.columns:
                return issues_df.with_columns(pl.lit("").alias("module"))
            return issues_df

        def _lookup_part(df: pl.DataFrame, priority: int) -> pl.DataFrame:
            if df is None or df.height == 0 or "Q Name" not in df.columns or "module" not in df.columns:
                return pl.DataFrame(schema={"Q Name": pl.Utf8, "_module_from_qname": pl.Utf8, "_p": pl.Int64})
            return (
                df
                .select(["Q Name", "module"])
                .with_columns([
                    pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Q Name"),
                    pl.col("module").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_module_from_qname"),
                    pl.lit(priority).alias("_p"),
                ])
                .filter((pl.col("Q Name") != "") & (pl.col("_module_from_qname") != ""))
                .select(["Q Name", "_module_from_qname", "_p"])
            )

        def _lookup_part_en(df: pl.DataFrame, priority: int) -> pl.DataFrame:
            if df is None or df.height == 0 or "Q Name" not in df.columns or "module_en" not in df.columns:
                return pl.DataFrame(schema={"Q Name": pl.Utf8, "_module_en_from_qname": pl.Utf8, "_p": pl.Int64})
            return (
                df
                .select(["Q Name", "module_en"])
                .with_columns([
                    pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Q Name"),
                    pl.col("module_en").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_module_en_from_qname"),
                    pl.lit(priority).alias("_p"),
                ])
                .filter((pl.col("Q Name") != "") & (pl.col("_module_en_from_qname") != ""))
                .select(["Q Name", "_module_en_from_qname", "_p"])
            )

        module_lookup = (
            pl.concat([
                _lookup_part(current_survey, 2),
                _lookup_part(reference_survey, 1),
                _lookup_part(template_survey, 0),
            ], how="vertical")
            .sort(["Q Name", "_p"])
            .group_by("Q Name")
            .agg(pl.col("_module_from_qname").last().alias("_module_from_qname"))
        )

        module_en_lookup = (
            pl.concat([
                _lookup_part_en(current_survey, 2),
                _lookup_part_en(reference_survey, 1),
                _lookup_part_en(template_survey, 0),
            ], how="vertical")
            .sort(["Q Name", "_p"])
            .group_by("Q Name")
            .agg(pl.col("_module_en_from_qname").last().alias("_module_en_from_qname"))
        )

        out = issues_df
        if "module" not in out.columns:
            out = out.with_columns(pl.lit("").alias("module"))
        if "module_en" not in out.columns:
            out = out.with_columns(pl.lit("").alias("module_en"))

        out = out.join(module_lookup, on="Q Name", how="left")
        out = out.with_columns(
            pl.when(pl.col("module").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
            .then(pl.col("module").cast(pl.Utf8))
            .otherwise(pl.col("_module_from_qname").cast(pl.Utf8).fill_null(""))
            .alias("module")
        ).drop("_module_from_qname")

        out = out.join(module_en_lookup, on="Q Name", how="left")
        out = out.with_columns(
            pl.when(pl.col("module_en").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
            .then(pl.col("module_en").cast(pl.Utf8))
            .otherwise(pl.col("_module_en_from_qname").cast(pl.Utf8).fill_null(""))
            .alias("module_en")
        ).drop("_module_en_from_qname")

        return out
    ```

### `_attach_module_column_to_issues._lookup_part` {#fn--lookup-part-3394}

**Pipeline stage:** `Step 7 -- Relevant validation (KoBO skip logic)`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3394`

**Signature**

```python
def _lookup_part(df: pl.DataFrame, priority: int) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 7 -- Relevant validation (KoBO skip logic)` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `priority` | positional_or_keyword | Yes | `-` | `int` | Input used by the `Step 7 -- Relevant validation (KoBO skip logic)` stage. |

??? note "Function source"

    ```python
    def _lookup_part(df: pl.DataFrame, priority: int) -> pl.DataFrame:
            if df is None or df.height == 0 or "Q Name" not in df.columns or "module" not in df.columns:
                return pl.DataFrame(schema={"Q Name": pl.Utf8, "_module_from_qname": pl.Utf8, "_p": pl.Int64})
            return (
                df
                .select(["Q Name", "module"])
                .with_columns([
                    pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Q Name"),
                    pl.col("module").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_module_from_qname"),
                    pl.lit(priority).alias("_p"),
                ])
                .filter((pl.col("Q Name") != "") & (pl.col("_module_from_qname") != ""))
                .select(["Q Name", "_module_from_qname", "_p"])
            )
    ```

### `_attach_module_column_to_issues._lookup_part_en` {#fn--lookup-part-en-3409}

**Pipeline stage:** `Step 7 -- Relevant validation (KoBO skip logic)`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3409`

**Signature**

```python
def _lookup_part_en(df: pl.DataFrame, priority: int) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 7 -- Relevant validation (KoBO skip logic)` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `priority` | positional_or_keyword | Yes | `-` | `int` | Input used by the `Step 7 -- Relevant validation (KoBO skip logic)` stage. |

??? note "Function source"

    ```python
    def _lookup_part_en(df: pl.DataFrame, priority: int) -> pl.DataFrame:
            if df is None or df.height == 0 or "Q Name" not in df.columns or "module_en" not in df.columns:
                return pl.DataFrame(schema={"Q Name": pl.Utf8, "_module_en_from_qname": pl.Utf8, "_p": pl.Int64})
            return (
                df
                .select(["Q Name", "module_en"])
                .with_columns([
                    pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Q Name"),
                    pl.col("module_en").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_module_en_from_qname"),
                    pl.lit(priority).alias("_p"),
                ])
                .filter((pl.col("Q Name") != "") & (pl.col("_module_en_from_qname") != ""))
                .select(["Q Name", "_module_en_from_qname", "_p"])
            )
    ```

### `validate_critical_sets` {#fn-validate-critical-sets-3490}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3490`

**Signature**

```python
def validate_critical_sets(questions_df, exact_sets):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 8 -- Critical sets` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `-` | Questionnaire structure table used by comparison and checks. |
| `exact_sets` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 -- Critical sets` stage. |

??? note "Function source"

    ```python
    def validate_critical_sets(questions_df, exact_sets):
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if not exact_sets:
            return pl.DataFrame(schema=EMPTY)

        # KoBO uses mandatory_category (already normalised); add Mandatory alias for compat
        if "Mandatory" not in questions_df.columns and "mandatory_category" in questions_df.columns:
            questions_df = questions_df.with_columns(
                pl.col("mandatory_category").alias("Mandatory")
            )
        # Mandatory_norm: map to yes/no for comparison with yaml expected values
        questions_df = questions_df.with_columns(
            pl.when(pl.col("Mandatory").is_in(["mandatory", "yes"])).then(pl.lit("yes"))
            .when(pl.col("Mandatory").is_in(["mandatory-panel"])).then(pl.lit("yes"))
            .when(pl.col("Mandatory").is_in(["optional", "no"])).then(pl.lit("no"))
            .otherwise(pl.lit("")).alias("Mandatory_norm")
        )

        present_qnames = set(questions_df["Q Name"].to_list())

        def _wealth_optional_variants(q_name: str) -> list[str]:
            q = str(q_name or "").strip()
            return _custom_variants(q) if q.startswith("hh_wealth_") else []

        issues = []
        for set_name, set_rules in exact_sets.items():
            for rule in set_rules:
                q_name   = rule["q_name"]
                expected = rule.get("expected_mandatory", "")
                required = rule.get("required", True)
                alt_q_names = _wealth_optional_variants(q_name)
                alt_q_name = " / ".join(alt_q_names)
                matched_q_name = q_name if q_name in present_qnames else next((a for a in alt_q_names if a in present_qnames), "")
                if not matched_q_name:
                    issues.append({
                        "issue_type": "missing_critical_question" if required else "advisory_question",
                        "set_name": set_name, "Q Name": q_name,
                        "field": "Q Name", "current": "",
                        "reference": (f"present (or optional variant: {alt_q_name})" if alt_q_name else "present"),
                        "severity": "high" if required else "medium", "excel_row": None,
                    })
                    continue
                if not expected:
                    continue
                # If a wealth optional variant is accepted as substitute, treat it as pass
                # and avoid forcing mandatory parity on the alternate form.
                if matched_q_name != q_name:
                    continue
                row = questions_df.filter(pl.col("Q Name") == matched_q_name).select(
                    ["Q Name", "Mandatory", "Mandatory_norm", "excel_row"]
                ).to_dicts()
                if not row:
                    continue
                row = row[0]
                if row["Mandatory_norm"] != expected:
                    issues.append({
                        "issue_type": "critical_mandatory_mismatch", "set_name": set_name,
                        "Q Name": q_name, "field": "Mandatory",
                        "current": row["Mandatory"], "reference": expected,
                        "severity": "high", "excel_row": row.get("excel_row"),
                    })

        if not issues:
            return pl.DataFrame(schema=EMPTY)
        return pl.DataFrame(issues)
    ```

### `validate_critical_sets._wealth_optional_variants` {#fn--wealth-optional-variants-3514}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3514`

**Signature**

```python
def _wealth_optional_variants(q_name: str) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 8 -- Critical sets` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `q_name` | positional_or_keyword | Yes | `-` | `str` | Question identifier used to join or compare records. |

??? note "Function source"

    ```python
    def _wealth_optional_variants(q_name: str) -> list[str]:
            q = str(q_name or "").strip()
            return _custom_variants(q) if q.startswith("hh_wealth_") else []
    ```

### `validate_prefix_counts` {#fn-validate-prefix-counts-3561}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3561`

**Signature**

```python
def validate_prefix_counts(questions_df, min_count_sets):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 8 -- Critical sets` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `-` | Questionnaire structure table used by comparison and checks. |
| `min_count_sets` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 -- Critical sets` stage. |

??? note "Function source"

    ```python
    def validate_prefix_counts(questions_df, min_count_sets):
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if not min_count_sets:
            return pl.DataFrame(schema=EMPTY)
        all_qnames = questions_df["Q Name"].to_list()
        issues = []
        for set_name, rule in min_count_sets.items():
            prefix    = rule.get("prefix", "")
            min_count = rule.get("min_count", 1)
            desc      = rule.get("description", f"At least {min_count} '{prefix}*' questions required")
            prefix_alts = tuple(_custom_variants(prefix)) if str(prefix) == "hh_wealth_" or str(set_name).upper() == "WEALTH" else ()
            matched = sorted(
                q for q in all_qnames
                if (prefix and q.startswith(prefix)) or (prefix_alts and q.startswith(prefix_alts))
            )
            if len(matched) < min_count:
                found_str = f"{len(matched)} found" + (f": {', '.join(matched)}" if matched else " (none)")
                issues.append({
                    "issue_type": "missing_critical_question", "set_name": set_name, "Q Name": "",
                    "field": "count", "current": found_str, "reference": desc,
                    "severity": "high", "excel_row": None,
                })
        if not issues:
            return pl.DataFrame(schema=EMPTY)
        return pl.DataFrame(issues)
    ```

### `validate_crop_harvest` {#fn-validate-crop-harvest-3592}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3592`

**Signature**

```python
def validate_crop_harvest(survey: pl.DataFrame, crop_harvest_cfg: dict) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** PASS if only the minimal set is present (no extra full-set questions), OR

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `survey` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `crop_harvest_cfg` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 8 -- Critical sets` stage. |

??? note "Function source"

    ```python
    def validate_crop_harvest(survey: pl.DataFrame, crop_harvest_cfg: dict) -> pl.DataFrame:
        """
        PASS if only the minimal set is present (no extra full-set questions), OR
        if the full set is completely present (extra questions beyond full are fine).
        FAIL for any partial overlap.
        Returns a DataFrame with ISSUE_SCHEMA columns.
        """
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if not crop_harvest_cfg:
            return pl.DataFrame(schema=EMPTY)

        minimal = set(crop_harvest_cfg.get("minimal", []))
        full    = set(crop_harvest_cfg.get("full", []))
        present = set(survey["Q Name"].to_list())

        if full.issubset(present):
            return pl.DataFrame(schema=EMPTY)

        extra_full = (full - minimal) & present
        if (minimal & present) == minimal and not extra_full:
            return pl.DataFrame(schema=EMPTY)

        missing_from_full = full - present
        partial_found     = (full - minimal) & present
        detail_parts = []
        if missing_from_full:
            detail_parts.append(f"missing from full set: {sorted(missing_from_full)}")
        if partial_found:
            detail_parts.append(f"partial full-set Qs present: {sorted(partial_found)}")
        detail = "; ".join(detail_parts) or "partial crop-harvest set"
        ref    = f"minimal={sorted(minimal)}, full={sorted(full)}"

        return pl.DataFrame([{
            "issue_type": "crop_harvest_violation",
            "set_name":   "CRP_HARV",
            "Q Name":     "crp_harv_*",
            "field":      "",
            "current":    detail,
            "reference":  ref,
            "severity":   "high",
            "excel_row":  -1,
        }], schema=EMPTY)
    ```

### `_rule_issues_df` {#fn--rule-issues-df-3647}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3647`

**Signature**

```python
def _rule_issues_df(rows: list[dict]) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 8 -- Critical sets` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `rows` | positional_or_keyword | Yes | `-` | `list[dict]` | Input used by the `Step 8 -- Critical sets` stage. |

??? note "Function source"

    ```python
    def _rule_issues_df(rows: list[dict]) -> pl.DataFrame:
        return pl.DataFrame(rows, schema=_RULE_ISSUE_SCHEMA) if rows else pl.DataFrame(schema=_RULE_ISSUE_SCHEMA)
    ```

### `_indicator_present` {#fn--indicator-present-3651}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3651`

**Signature**

```python
def _indicator_present(qnames: set[str], indicator_cfg: dict) -> bool:
```

**Returns:** `bool`

**What it does:** Returns True if the indicator has at least one question in the questionnaire.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 8 -- Critical sets` stage. |
| `indicator_cfg` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 8 -- Critical sets` stage. |

??? note "Function source"

    ```python
    def _indicator_present(qnames: set[str], indicator_cfg: dict) -> bool:
        """Returns True if the indicator has at least one question in the questionnaire."""
        prefix = indicator_cfg.get("anchor_prefix")
        qname  = indicator_cfg.get("anchor_qname")
        if prefix and any(q.startswith(prefix) for q in qnames):
            return True
        if qname and qname in qnames:
            return True
        return False
    ```

### `validate_fs_indicators` {#fn-validate-fs-indicators-3662}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3662`

**Signature**

```python
def validate_fs_indicators(current_questions: pl.DataFrame, rules: dict, modality: str='capi') -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Food Security indicator presence and CAPI ceiling (fs_indicators block in

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `rules` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 8 -- Critical sets` stage. |
| `modality` | positional_or_keyword | No | `'capi'` | `str` | Input used by the `Step 8 -- Critical sets` stage. |

??? note "Function source"

    ```python
    def validate_fs_indicators(
        current_questions: pl.DataFrame,
        rules: dict,
        modality: str = "capi",
    ) -> pl.DataFrame:
        """
        Food Security indicator presence and CAPI ceiling (fs_indicators block in
        critical_sets.yaml), same rule as the GeoPoll validator:
          - each mandatory indicator (FIES, FCS, LCSI) needs at least one question
          - when modality='capi', mandatory + optional indicators found must not
            exceed capi_max
        """
        fs_rules = rules.get("fs_indicators", {})
        if not fs_rules:
            return _rule_issues_df([])

        qnames: set[str] = set(current_questions["Q Name"].to_list())
        capi_max = int(fs_rules.get("capi_max", 4))
        rows: list[dict] = []

        found_mandatory: list[str] = []
        for name, ind_cfg in fs_rules.get("mandatory", {}).items():
            if _indicator_present(qnames, ind_cfg):
                found_mandatory.append(name)
            else:
                rows.append({
                    "issue_type": "fs_indicator_missing",
                    "set_name": "FS_INDICATORS", "Q Name": "",
                    "field": name, "current": "not found",
                    "reference": f"mandatory indicator -- expected prefix/qname: "
                                 f"{ind_cfg.get('anchor_prefix') or ind_cfg.get('anchor_qname')}",
                    "severity": "high", "excel_row": None,
                })
        found_optional = [
            name for name, ind_cfg in fs_rules.get("optional", {}).items()
            if _indicator_present(qnames, ind_cfg)
        ]

        if modality == "capi":
            total = len(found_mandatory) + len(found_optional)
            if total > capi_max:
                rows.append({
                    "issue_type": "fs_indicator_capi_excess",
                    "set_name": "FS_INDICATORS", "Q Name": "",
                    "field": "indicator count",
                    "current": f"{total} indicators present: {', '.join(found_mandatory + found_optional)}",
                    "reference": f"max {capi_max} for CAPI modality",
                    "severity": "high", "excel_row": None,
                })
        return _rule_issues_df(rows)
    ```

### `_agri_signal_patterns_kobo` {#fn--agri-signal-patterns-kobo-3714}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3714`

**Signature**

```python
def _agri_signal_patterns_kobo(agri_signals: list[dict]) -> list[re.Pattern]:
```

**Returns:** `list[re.Pattern]`

**What it does:** Regexes matching an agri signal in KoBo `relevant` syntax:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `agri_signals` | positional_or_keyword | Yes | `-` | `list[dict]` | Input used by the `Step 8 -- Critical sets` stage. |

??? note "Function source"

    ```python
    def _agri_signal_patterns_kobo(agri_signals: list[dict]) -> list[re.Pattern]:
        """
        Regexes matching an agri signal in KoBo `relevant` syntax:
        ${var} = 'v' / ${var}='v' / selected(${var}, 'v'). Matches both
        `kobo_values` (current KoBo choice names, e.g. hh_agricactivity =
        crp/ls/fish) and `values` (numeric codes used by earlier KoBo templates).
        """
        patterns: list[re.Pattern] = []
        for sig in agri_signals:
            var = re.escape(str(sig.get("variable", "")))
            vals = list(sig.get("kobo_values") or []) + list(sig.get("values") or [])
            val_pat = "|".join(re.escape(str(v)) for v in vals)
            if not var or not val_pat:
                continue
            patterns.append(re.compile(
                rf"\$\{{{var}\}}\s*=\s*['\"]?(?:{val_pat})['\"]?(?![\w])"
                rf"|selected\(\s*\$\{{{var}\}}\s*,\s*['\"](?:{val_pat})['\"]\s*\)",
                re.IGNORECASE,
            ))
        return patterns
    ```

### `validate_agri_cs_count` {#fn-validate-agri-cs-count-3736}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3736`

**Signature**

```python
def validate_agri_cs_count(current_questions: pl.DataFrame, rules: dict) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Counts coping strategy questions (cs_prefixes) whose `relevant` references

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `rules` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 8 -- Critical sets` stage. |

??? note "Function source"

    ```python
    def validate_agri_cs_count(
        current_questions: pl.DataFrame,
        rules: dict,
    ) -> pl.DataFrame:
        """
        Counts coping strategy questions (cs_prefixes) whose `relevant` references
        an agricultural signal (agri_cs_check in critical_sets.yaml). Fewer than
        min_agri_cs raises a high-severity issue. KoBo counterpart of the GeoPoll
        check, which reads the Conditional column instead.
        """
        agri_cfg = rules.get("agri_cs_check", {})
        if not agri_cfg or "relevant" not in current_questions.columns:
            return _rule_issues_df([])

        cs_prefixes = list(agri_cfg.get("cs_prefixes", []))
        min_agri_cs = int(agri_cfg.get("min_agri_cs", 4))
        patterns = _agri_signal_patterns_kobo(agri_cfg.get("agri_signals", []))
        if not cs_prefixes or not patterns:
            return _rule_issues_df([])

        cs_df = current_questions.filter(
            pl.any_horizontal([_core_qname_expr("Q Name").str.starts_with(p) for p in cs_prefixes])
        ).select(["Q Name", pl.col("relevant").cast(pl.Utf8).fill_null("")])

        agri_cs = sorted(
            q for q, rel in cs_df.iter_rows()
            if any(pat.search(rel) for pat in patterns)
        )
        if len(agri_cs) >= min_agri_cs:
            return _rule_issues_df([])
        return _rule_issues_df([{
            "issue_type": "agri_cs_count_insufficient",
            "set_name": "AGRI_CS", "Q Name": "",
            "field": "agri-related CS count",
            "current": f"{len(agri_cs)} found" + (f": {', '.join(agri_cs)}" if agri_cs else ""),
            "reference": f"minimum {min_agri_cs} agriculture-related CS required",
            "severity": "high", "excel_row": None,
        }])
    ```

### `validate_variable_pairs` {#fn-validate-variable-pairs-3776}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3776`

**Signature**

```python
def validate_variable_pairs(current_questions: pl.DataFrame, rules: dict) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** If either question of a pair (variable_pairs in critical_sets.yaml) is present, both must be.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `rules` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 8 -- Critical sets` stage. |

??? note "Function source"

    ```python
    def validate_variable_pairs(
        current_questions: pl.DataFrame,
        rules: dict,
    ) -> pl.DataFrame:
        """If either question of a pair (variable_pairs in critical_sets.yaml) is present, both must be."""
        pairs_cfg: list[dict] = rules.get("variable_pairs", [])
        if not pairs_cfg:
            return _rule_issues_df([])

        qnames: set[str] = set(current_questions["Q Name"].to_list())
        rows: list[dict] = []
        for pair in pairs_cfg:
            a, b, label = pair.get("a", ""), pair.get("b", ""), pair.get("label", "")
            a_present, b_present = a in qnames, b in qnames
            if a_present == b_present:
                continue
            present, missing = (a, b) if a_present else (b, a)
            rows.append({
                "issue_type": "variable_pair_incomplete",
                "set_name": "VAR_PAIRS", "Q Name": present,
                "field": label,
                "current": f"'{present}' present but '{missing}' absent",
                "reference": "both variables required when either is included",
                "severity": "medium", "excel_row": None,
            })
        return _rule_issues_df(rows)
    ```

### `_code_sort_key` {#fn--code-sort-key-3804}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3804`

**Signature**

```python
def _code_sort_key(value: str) -> tuple:
```

**Returns:** `tuple`

**What it does:** Implements logic in the `Step 8 -- Critical sets` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 -- Critical sets` stage. |

??? note "Function source"

    ```python
    def _code_sort_key(value: str) -> tuple:
        return (0, int(value), value) if value.lstrip("-").isdigit() else (1, 0, value)
    ```

### `validate_fixed_option_codes` {#fn-validate-fixed-option-codes-3808}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3808`

**Signature**

```python
def validate_fixed_option_codes(current_options: pl.DataFrame | None, rules: dict) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Questions whose choice names must be exactly a fixed code set

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |
| `rules` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 8 -- Critical sets` stage. |

??? note "Function source"

    ```python
    def validate_fixed_option_codes(
        current_options: pl.DataFrame | None,
        rules: dict,
    ) -> pl.DataFrame:
        """
        Questions whose choice names must be exactly a fixed code set
        (fixed_option_codes in critical_sets.yaml; `kobo_codes` when given, else
        `codes`), e.g. ls_main_confirm = the 8 livestock types.
        Questions absent from the questionnaire are skipped.
        """
        rules_cfg: list[dict] = rules.get("fixed_option_codes") or []
        if not rules_cfg or current_options is None or current_options.height == 0:
            return _rule_issues_df([])

        codes_by_q = {
            row["Q Name"]: {str(c).strip() for c in row["codes"] if c is not None and str(c).strip()}
            for row in (
                current_options
                .group_by("Q Name")
                .agg(pl.col("option_name").cast(pl.Utf8).alias("codes"))
                .iter_rows(named=True)
            )
        }
        rows: list[dict] = []
        for rule in rules_cfg:
            q = str(rule.get("q_name") or "").strip()
            expected = {str(c).strip() for c in (rule.get("kobo_codes") or rule.get("codes") or [])}
            if not q or not expected or q not in codes_by_q:
                continue
            found = codes_by_q[q]
            if found == expected:
                continue
            missing = sorted(expected - found, key=_code_sort_key)
            extra = sorted(found - expected, key=_code_sort_key)
            rows.append({
                "issue_type": "fixed_codes_mismatch",
                "set_name": "FIXED_CODES", "Q Name": q,
                "field": str(rule.get("description") or "fixed answer codes"),
                "current": f"codes {sorted(found, key=_code_sort_key)}; missing {missing or '-'}; unexpected {extra or '-'}",
                "reference": f"codes must be exactly {sorted(expected, key=_code_sort_key)}",
                "severity": str(rule.get("severity") or "high"), "excel_row": None,
            })
        return _rule_issues_df(rows)
    ```

### `read_tlu_weights` {#fn-read-tlu-weights-3853}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3853`

**Signature**

```python
def read_tlu_weights(path: str, section_marker: str) -> pl.DataFrame | None:
```

**Returns:** `pl.DataFrame | None`

**What it does:** Tropical Livestock Unit weights from the Additional information sheet

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |
| `section_marker` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 -- Critical sets` stage. |

??? note "Function source"

    ```python
    def read_tlu_weights(path: str, section_marker: str) -> pl.DataFrame | None:
        """
        Tropical Livestock Unit weights from the Additional information sheet
        (20261007 template on). The section banner sits left of the 'Original'
        column on the first row of the section; every following row belongs to
        it until the next banner. Returns species + one 'Replacement (xx)' column
        per language, or None when the sheet is absent.
        """
        try:
            wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
            if "Additional information" not in wb.sheetnames:
                wb.close()
                return None
            rows = list(wb["Additional information"].iter_rows(values_only=True))
            wb.close()
        except Exception:
            return None
        if len(rows) < 2 or not section_marker:
            return pl.DataFrame(schema={"species": pl.Utf8})

        headers = [str(h).strip() if h is not None else "" for h in rows[1]]
        orig_idx = next((i for i, h in enumerate(headers) if _normalize_additional_info_header(h).startswith("original")), None)
        if orig_idx is None:
            return pl.DataFrame(schema={"species": pl.Utf8})
        weight_idx = {headers[i]: i for i in _additional_info_replacement_indexes(headers).values() if i is not None}

        records: list[dict] = []
        section = ""
        for row in rows[2:]:
            banner = next((str(c).strip() for c in row[:orig_idx] if c is not None and str(c).strip()), "")
            if banner:
                section = banner
            species = str(row[orig_idx]).strip() if orig_idx < len(row) and row[orig_idx] is not None else ""
            if not species or section_marker.upper() not in section.upper():
                continue
            rec = {"species": species}
            for col, i in weight_idx.items():
                v = row[i] if i < len(row) else None
                rec[col] = "" if v is None else str(v).strip()
            records.append(rec)
        schema = {"species": pl.Utf8, **{c: pl.Utf8 for c in weight_idx}}
        return pl.DataFrame(records, schema=schema) if records else pl.DataFrame(schema=schema)
    ```

### `validate_tlu_weights` {#fn-validate-tlu-weights-3897}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3897`

**Signature**

```python
def validate_tlu_weights(tlu_df: pl.DataFrame | None, rules: dict) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Every species in tlu_weights (critical_sets.yaml) needs a numeric weight

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `tlu_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame | None` | Input used by the `Step 8 -- Critical sets` stage. |
| `rules` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 8 -- Critical sets` stage. |

??? note "Function source"

    ```python
    def validate_tlu_weights(tlu_df: pl.DataFrame | None, rules: dict) -> pl.DataFrame:
        """
        Every species in tlu_weights (critical_sets.yaml) needs a numeric weight
        > 0, identical in every filled language column. Skipped when the
        Additional information sheet is absent (tlu_df is None).
          - tlu_weight_missing (high), tlu_weight_invalid (high),
            tlu_weight_inconsistent (medium)
        """
        cfg = rules.get("tlu_weights") or {}
        species_cfg = [str(x).strip() for x in (cfg.get("species") or []) if str(x or "").strip()]
        if not species_cfg or tlu_df is None:
            return _rule_issues_df([])

        weight_cols = [c for c in tlu_df.columns if c != "species"]
        by_species: dict[str, dict] = {}
        for row in tlu_df.iter_rows(named=True):
            by_species.setdefault(str(row["species"]).strip().lower(), row)

        def _issue(issue_type, species, current, reference, severity):
            return {
                "issue_type": issue_type, "set_name": "TLU", "Q Name": "",
                "field": f"TLU weight: {species}", "current": current,
                "reference": reference, "severity": severity, "excel_row": None,
            }

        rows: list[dict] = []
        for species in species_cfg:
            row = by_species.get(species.lower())
            filled = {c: str(row.get(c) or "").strip() for c in weight_cols} if row else {}
            filled = {c: v for c, v in filled.items() if v}
            if not filled:
                rows.append(_issue("tlu_weight_missing", species, "blank / row missing",
                                   "weight required in Additional information (TLU section)", "high"))
                continue
            parsed: dict[str, float | None] = {}
            for c, v in filled.items():
                try:
                    parsed[c] = float(v.replace(",", "."))
                except ValueError:
                    parsed[c] = None
            bad = {c: filled[c] for c, v in parsed.items() if v is None or v <= 0}
            if bad:
                rows.append(_issue("tlu_weight_invalid", species,
                                   "; ".join(f"{c}={v}" for c, v in bad.items()),
                                   "weight must be a number > 0", "high"))
                continue
            if len({round(v, 6) for v in parsed.values()}) > 1:
                rows.append(_issue("tlu_weight_inconsistent", species,
                                   "; ".join(f"{c}={v}" for c, v in filled.items()),
                                   "same weight expected in every language column", "medium"))
        return _rule_issues_df(rows)
    ```

### `validate_tlu_weights._issue` {#fn--issue-3915}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3915`

**Signature**

```python
def _issue(issue_type, species, current, reference, severity):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 8 -- Critical sets` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `issue_type` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 -- Critical sets` stage. |
| `species` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 -- Critical sets` stage. |
| `current` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 -- Critical sets` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 -- Critical sets` stage. |
| `severity` | positional_or_keyword | Yes | `-` | `-` | Severity label used for final issue classification. |

??? note "Function source"

    ```python
    def _issue(issue_type, species, current, reference, severity):
            return {
                "issue_type": issue_type, "set_name": "TLU", "Q Name": "",
                "field": f"TLU weight: {species}", "current": current,
                "reference": reference, "severity": severity, "excel_row": None,
            }
    ```

### `validate_qname_length` {#fn-validate-qname-length-3950}

**Pipeline stage:** `Step 8 -- Critical sets`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3950`

**Signature**

```python
def validate_qname_length(current_questions: pl.DataFrame, max_qname_length: int) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Question names longer than max_qname_length (kobo_options) -> medium.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `max_qname_length` | positional_or_keyword | Yes | `-` | `int` | Input used by the `Step 8 -- Critical sets` stage. |

??? note "Function source"

    ```python
    def validate_qname_length(current_questions: pl.DataFrame, max_qname_length: int) -> pl.DataFrame:
        """Question names longer than max_qname_length (kobo_options) -> medium."""
        if max_qname_length <= 0:
            return _rule_issues_df([])
        cols = ["Q Name"] + (["excel_row"] if "excel_row" in current_questions.columns else [])
        long_q = (
            current_questions.select(cols)
            .filter(pl.col("Q Name").cast(pl.Utf8).str.len_chars() > max_qname_length)
        )
        return _rule_issues_df([
            {
                "issue_type": "qname_too_long", "set_name": "", "Q Name": r["Q Name"],
                "field": "Q Name", "current": f"{len(r['Q Name'])} characters",
                "reference": f"max {max_qname_length} characters",
                "severity": "medium", "excel_row": r.get("excel_row"),
            }
            for r in long_q.iter_rows(named=True)
        ])
    ```

### `make_presence_issues` {#fn-make-presence-issues-3974}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:3974`

**Signature**

```python
def make_presence_issues(added, removed, reference_survey=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `added` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `removed` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `reference_survey` | positional_or_keyword | No | `None` | `-` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def make_presence_issues(added, removed, reference_survey=None):
        added_base = added

        # Build optional counterpart lookup from added questions: core -> c_<core> / o_<core>
        # Example: removed "confl_yn" + added "c_confl_yn" => mandatory_to_optional
        added_opt_lookup = (
            added
            .with_columns([
                pl.col("Q Name").cast(pl.Utf8).str.strip_chars().alias("_q"),
                _core_qname_expr("Q Name").alias("_core"),
            ])
            .filter(_custom_qname_expr("_q"))
            .select(["_core", pl.col("Q Name").alias("_optional_qname")])
            .unique(subset=["_core"], keep="first")
        )

        # Severity: mandatory / mandatory-panel -> high; non-mandatory / optional -> info
        if reference_survey is not None and "mandatory_category" in reference_survey.columns:
            removed_aug = (
                removed.join(
                    reference_survey.select(["Q Name", "mandatory_category"]),
                    on="Q Name", how="left"
                )
                .with_columns(
                    _core_qname_expr("Q Name").alias("_core")
                )
            )
            severity_expr = (
                pl.when(pl.col("mandatory_category").is_in(["mandatory", "mandatory-panel"]))
                .then(pl.lit("high"))
                .otherwise(pl.lit("info"))
                .alias("severity")
            )

            moved_to_optional = (
                removed_aug
                .join(added_opt_lookup, on="_core", how="inner")
                .filter(pl.col("mandatory_category").is_in(["mandatory", "mandatory-panel"]))
            )
        else:
            removed_aug = removed.with_columns([
                pl.lit("").alias("mandatory_category"),
                _core_qname_expr("Q Name").alias("_core"),
            ])
            severity_expr = (
                pl.when(pl.col("is_optional")).then(pl.lit("info")).otherwise(pl.lit("high"))
                .alias("severity")
            )
            moved_to_optional = pl.DataFrame(schema={
                "Q Name": pl.Utf8, "is_optional": pl.Boolean, "mandatory_category": pl.Utf8,
                "_core": pl.Utf8, "_optional_qname": pl.Utf8,
            })

        moved_i = (
            moved_to_optional.with_columns([
                pl.lit("mandatory_to_optional").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("Q Name").alias("field"),
                pl.col("_optional_qname").alias("current"),
                pl.lit("present (mandatory in reference)").alias("reference"),
                pl.lit("high").alias("severity"),
                pl.lit(None).cast(pl.Int64).alias("excel_row"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )

        added_base = (
            added.join(moved_to_optional.select(pl.col("_optional_qname").alias("Q Name")), on="Q Name", how="anti")
            if moved_to_optional.height > 0 else added
        )
        added_i = added_base.with_columns([
            pl.lit("added_question").alias("issue_type"),
            pl.lit("").alias("set_name"),
            pl.lit("Q Name").alias("field"),
            pl.lit("present").alias("current"),
            pl.lit("missing_in_reference").alias("reference"),
            pl.lit("info").alias("severity"),
            pl.lit(None).cast(pl.Int64).alias("excel_row"),
        ]).select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])

        removed_base = (
            removed_aug.join(moved_to_optional.select(["Q Name"]), on="Q Name", how="anti")
            if moved_to_optional.height > 0 else removed_aug
        )

        removed_i = (
            removed_base.with_columns([
                pl.lit("removed_question").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("Q Name").alias("field"),
                pl.lit("missing_in_current").alias("current"),
                pl.lit("present").alias("reference"),
                severity_expr,
                pl.lit(None).cast(pl.Int64).alias("excel_row"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )

        return pl.concat([added_i, removed_i, moved_i], how="vertical")
    ```

### `make_mandatory_issues` {#fn-make-mandatory-issues-4075}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4075`

**Signature**

```python
def make_mandatory_issues(mandatory_diff):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `mandatory_diff` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def make_mandatory_issues(mandatory_diff):
        return (
            mandatory_diff
            .with_columns([
                pl.lit("").alias("set_name"),
                pl.col("Mandatory").alias("current"),
                pl.col("Mandatory_ref").alias("reference"),
                pl.lit("high").alias("severity"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `make_option_issues` {#fn-make-option-issues-4088}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4088`

**Signature**

```python
def make_option_issues(option_diff):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `option_diff` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def make_option_issues(option_diff):
        return (
            option_diff
            .with_columns([
                pl.lit("").alias("set_name"),
                pl.col("option_label").alias("current"),
                pl.col("option_label_ref").alias("reference"),
                pl.lit("medium").alias("severity"),
            ])
            .select(["issue_type", "set_name", "Q Name", "list_name", "option_name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `make_option_presence_issues` {#fn-make-option-presence-issues-4101}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4101`

**Signature**

```python
def make_option_presence_issues(added_opts, removed_opts):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `added_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `removed_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def make_option_presence_issues(added_opts, removed_opts):
        added_i = added_opts.with_columns([
            pl.lit("").alias("set_name"),
            pl.col("option_label").alias("current"),
            pl.lit(_not_in_reference_text()).alias("reference"),
            pl.lit("high").alias("severity"),
            pl.lit(None).cast(pl.Int64).alias("excel_row"),
        ]).select(["issue_type", "set_name", "Q Name", "list_name", "option_name", "field", "current", "reference", "severity", "excel_row"])

        removed_i = removed_opts.with_columns([
            pl.lit("").alias("set_name"),
            pl.lit("(removed)").alias("current"),
            pl.col("option_label").alias("reference"),
            pl.lit("high").alias("severity"),
            pl.lit(None).cast(pl.Int64).alias("excel_row"),
        ]).select(["issue_type", "set_name", "Q Name", "list_name", "option_name", "field", "current", "reference", "severity", "excel_row"])

        return pl.concat([added_i, removed_i], how="vertical")
    ```

### `make_option_name_renumber_issues` {#fn-make-option-name-renumber-issues-4121}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4121`

**Signature**

```python
def make_option_name_renumber_issues(renumbered_opts):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `renumbered_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def make_option_name_renumber_issues(renumbered_opts):
        return (
            renumbered_opts
            .with_columns([
                pl.lit("").alias("set_name"),
                pl.col("new_option_name").cast(pl.Utf8).alias("current"),
                pl.col("old_option_name").cast(pl.Utf8).alias("reference"),
                pl.lit("high").alias("severity"),
                pl.lit(None).cast(pl.Int64).alias("excel_row"),
            ])
            .select(["issue_type", "set_name", "Q Name", "list_name", "option_name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `merge_option_issue_views_en_target` {#fn-merge-option-issue-views-en-target-4135}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4135`

**Signature**

```python
def merge_option_issue_views_en_target(en_df: pl.DataFrame, tgt_df: pl.DataFrame, target_lang: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** For non-EN runs, keep EN in current/reference and add target-language

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `en_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `tgt_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `target_lang` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def merge_option_issue_views_en_target(
        en_df: pl.DataFrame,
        tgt_df: pl.DataFrame,
        target_lang: str,
    ) -> pl.DataFrame:
        """
        For non-EN runs, keep EN in current/reference and add target-language
        columns as current_lang/reference_lang.
        """
        if str(target_lang or "").strip().lower() == "en":
            return en_df
        if en_df.height == 0 and tgt_df.height == 0:
            return en_df

        keys = [k for k in ["issue_type", "set_name", "Q Name", "list_name", "option_name", "field"] if k in en_df.columns and k in tgt_df.columns]

        en_view = en_df.rename({
            "current": "current_en",
            "reference": "reference_en",
            "severity": "severity_en",
            "excel_row": "excel_row_en",
        })
        tgt_view = tgt_df.rename({
            "current": "current_tgt",
            "reference": "reference_tgt",
            "severity": "severity_tgt",
            "excel_row": "excel_row_tgt",
        })

        out = en_view.join(tgt_view, on=keys, how="full", suffix="_t")

        return (
            out
            .with_columns([
                pl.coalesce([pl.col("issue_type"), pl.col("issue_type_t")]).alias("issue_type"),
                pl.coalesce([pl.col("set_name"), pl.col("set_name_t"), pl.lit("")]).alias("set_name"),
                pl.coalesce([pl.col("Q Name"), pl.col("Q Name_t"), pl.lit("")]).alias("Q Name"),
                pl.coalesce([pl.col("list_name"), pl.col("list_name_t"), pl.lit("")]).alias("list_name"),
                pl.coalesce([pl.col("option_name"), pl.col("option_name_t"), pl.lit("")]).alias("option_name"),
                pl.coalesce([pl.col("field"), pl.col("field_t"), pl.lit("")]).alias("field"),
                pl.coalesce([pl.col("current_en"), pl.lit("")]).alias("current"),
                pl.coalesce([pl.col("reference_en"), pl.lit("")]).alias("reference"),
                pl.coalesce([pl.col("current_tgt"), pl.lit("")]).alias("current_lang"),
                pl.coalesce([pl.col("reference_tgt"), pl.lit("")]).alias("reference_lang"),
                pl.when(pl.col("severity_tgt") == "high").then(pl.lit("high"))
                .when(pl.col("severity_en") == "high").then(pl.lit("high"))
                .when(pl.col("severity_tgt") == "medium").then(pl.lit("medium"))
                .when(pl.col("severity_en") == "medium").then(pl.lit("medium"))
                .otherwise(pl.lit("info")).alias("severity"),
                pl.coalesce([pl.col("excel_row_tgt"), pl.col("excel_row_en")]).alias("excel_row"),
            ])
            .select([
                "issue_type", "set_name", "Q Name", "list_name", "option_name", "field",
                "current", "reference", "current_lang", "reference_lang", "severity", "excel_row",
            ])
        )
    ```

### `classify_choice_name_root_causes` {#fn-classify-choice-name-root-causes-4193}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4193`

**Signature**

```python
def classify_choice_name_root_causes(current_opts: pl.DataFrame, reference_opts: pl.DataFrame, option_presence_issues: pl.DataFrame, option_renumber_issues: pl.DataFrame, current_opts_en: pl.DataFrame | None=None, reference_opts_en: pl.DataFrame | None=None, target_lang: str='en') -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
```

**Returns:** `tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]`

**What it does:** Label-first classifier for choice name issues.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_opts` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `reference_opts` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `option_presence_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `option_renumber_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `current_opts_en` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `reference_opts_en` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `target_lang` | positional_or_keyword | No | `'en'` | `str` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def classify_choice_name_root_causes(
        current_opts: pl.DataFrame,
        reference_opts: pl.DataFrame,
        option_presence_issues: pl.DataFrame,
        option_renumber_issues: pl.DataFrame,
        current_opts_en: pl.DataFrame | None = None,
        reference_opts_en: pl.DataFrame | None = None,
        target_lang: str = "en",
    ) -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
        """
        Label-first classifier for choice name issues.
        Emits one primary root-cause row per (Q Name, list_name):
          - option_name_dictionary_replaced
          - removed_option_causes_index_drift
        and suppresses redundant subordinate rows to avoid double-reporting.
        """
        dual_lang = (
            str(target_lang or "").strip().lower() != "en"
            and current_opts_en is not None
            and reference_opts_en is not None
        )

        issue_schema = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "list_name": pl.Utf8, "option_name": pl.Utf8, "field": pl.Utf8,
            "current": pl.Utf8, "reference": pl.Utf8, "severity": pl.Utf8,
            "excel_row": pl.Int64,
        }
        if dual_lang:
            issue_schema["current_lang"] = pl.Utf8
            issue_schema["reference_lang"] = pl.Utf8
        empty_df = pl.DataFrame(schema=issue_schema)
        if option_presence_issues.height == 0 or option_renumber_issues.height == 0:
            return option_presence_issues, option_renumber_issues, empty_df

        presence_keys = (
            option_presence_issues
            .filter(pl.col("issue_type").is_in(["removed_choice", "added_choice"]))
            .select(["Q Name", "list_name"])
            .unique()
        )
        renumber_keys = option_renumber_issues.select(["Q Name", "list_name"]).unique()
        candidate_keys = presence_keys.join(renumber_keys, on=["Q Name", "list_name"], how="inner")
        if candidate_keys.height == 0:
            return option_presence_issues, option_renumber_issues, empty_df

        cur_norm = (
            current_opts
            .with_columns([
                pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase().alias("_qk"),
                _normalized_list_expr("list_name").alias("_lkst"),
                normalize_text_expr("option_label").alias("_lblk"),
                _canonical_option_key_expr("option_name").alias("_namek"),
                pl.col("option_name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_name_raw"),
                pl.col("option_label").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_label_raw"),
            ])
            .filter(
                (pl.col("_qk") != "")
                & (pl.col("_lkst") != "")
                & (pl.col("_lblk") != "")
                & (pl.col("_namek") != "")
            )
            .select(["_qk", "_lkst", "_lblk", "_namek", "_name_raw", "_label_raw"])
        )
        ref_norm = (
            reference_opts
            .with_columns([
                pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase().alias("_qk"),
                _normalized_list_expr("list_name").alias("_lkst"),
                normalize_text_expr("option_label").alias("_lblk"),
                _canonical_option_key_expr("option_name").alias("_namek"),
                pl.col("option_name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_name_raw"),
                pl.col("option_label").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_label_raw"),
            ])
            .filter(
                (pl.col("_qk") != "")
                & (pl.col("_lkst") != "")
                & (pl.col("_lblk") != "")
                & (pl.col("_namek") != "")
            )
            .select(["_qk", "_lkst", "_lblk", "_namek", "_name_raw", "_label_raw"])
        )

        cur_norm_en = None
        ref_norm_en = None
        if dual_lang:
            cur_norm_en = (
                current_opts_en
                .with_columns([
                    pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase().alias("_qk"),
                    _normalized_list_expr("list_name").alias("_lkst"),
                    normalize_text_expr("option_label").alias("_lblk"),
                    _canonical_option_key_expr("option_name").alias("_namek"),
                    pl.col("option_name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_name_raw"),
                    pl.col("option_label").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_label_raw"),
                ])
                .filter(
                    (pl.col("_qk") != "")
                    & (pl.col("_lkst") != "")
                    & (pl.col("_lblk") != "")
                    & (pl.col("_namek") != "")
                )
                .select(["_qk", "_lkst", "_lblk", "_namek", "_name_raw", "_label_raw"])
            )
            ref_norm_en = (
                reference_opts_en
                .with_columns([
                    pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase().alias("_qk"),
                    _normalized_list_expr("list_name").alias("_lkst"),
                    normalize_text_expr("option_label").alias("_lblk"),
                    _canonical_option_key_expr("option_name").alias("_namek"),
                    pl.col("option_name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_name_raw"),
                    pl.col("option_label").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_label_raw"),
                ])
                .filter(
                    (pl.col("_qk") != "")
                    & (pl.col("_lkst") != "")
                    & (pl.col("_lblk") != "")
                    & (pl.col("_namek") != "")
                )
                .select(["_qk", "_lkst", "_lblk", "_namek", "_name_raw", "_label_raw"])
            )

        def _is_numeric_name(token) -> bool:
            return bool(re.fullmatch(r"\d+(?:\.0+)?", str(token or "").strip()))

        def _name_sort_key(token: str):
            txt = str(token or "").strip()
            if re.fullmatch(r"\d+(?:\.0+)?", txt):
                return (0, float(txt))
            return (1, txt.lower())

        def _uniq(seq):
            seen = set()
            out = []
            for raw in seq:
                token = str(raw or "").strip()
                if not token or token in seen:
                    continue
                seen.add(token)
                out.append(token)
            return out

        def _join_limited(items, limit=12):
            if not items:
                return "(none)"
            vals = _uniq(items)
            if len(vals) <= limit:
                return ", ".join(vals)
            return ", ".join(vals[:limit]) + f", ... (+{len(vals) - limit} more)"

        def _join_names(items, limit=12):
            vals = _uniq(items)
            vals = sorted(vals, key=_name_sort_key)
            if not vals:
                return "(none)"
            if len(vals) <= limit:
                return ", ".join(vals)
            return ", ".join(vals[:limit]) + f", ... (+{len(vals) - limit} more)"

        def _format_choice_list(rows: list[dict]) -> str:
            ordered = sorted(rows, key=lambda r: _name_sort_key(r.get("_name_raw")))
            lines = []
            for r in ordered:
                nm = str(r.get("_name_raw") or "").strip()
                lb = str(r.get("_label_raw") or "").strip()
                if not nm and not lb:
                    continue
                lines.append(f"{nm} | {lb}" if lb else nm)
            return "\n".join(lines) if lines else "(none)"

        classified = []
        root_rows = []
        for key in candidate_keys.to_dicts():
            q_name = str(key.get("Q Name") or "")
            list_name = str(key.get("list_name") or "")
            qk = q_name.strip().lower()
            lkst = _normalize_list_token(list_name)
            if not qk or not lkst:
                continue

            cur_rows = cur_norm.filter((pl.col("_qk") == qk) & (pl.col("_lkst") == lkst)).to_dicts()
            ref_rows = ref_norm.filter((pl.col("_qk") == qk) & (pl.col("_lkst") == lkst)).to_dicts()
            if not cur_rows or not ref_rows:
                continue

            cur_by_label = {}
            ref_by_label = {}
            cur_label_counts = {}
            ref_label_counts = {}

            for r in cur_rows:
                lbl = r.get("_lblk")
                if not lbl:
                    continue
                cur_label_counts[lbl] = cur_label_counts.get(lbl, 0) + 1
                cur_by_label.setdefault(lbl, r)
            for r in ref_rows:
                lbl = r.get("_lblk")
                if not lbl:
                    continue
                ref_label_counts[lbl] = ref_label_counts.get(lbl, 0) + 1
                ref_by_label.setdefault(lbl, r)

            cur_labels = set(cur_by_label.keys())
            ref_labels = set(ref_by_label.keys())
            common_labels = sorted(cur_labels & ref_labels)
            missing_entries = [
                {
                    "label_raw": ref_by_label[lbl].get("_label_raw"),
                    "name_raw": str(ref_by_label[lbl].get("_name_raw") or "").strip(),
                    "name_key": str(ref_by_label[lbl].get("_namek") or "").strip(),
                }
                for lbl in sorted(ref_labels - cur_labels)
            ]
            missing_labels = [e.get("label_raw") for e in missing_entries]
            added_entries = [
                {
                    "label_raw": cur_by_label[lbl].get("_label_raw"),
                    "name_raw": str(cur_by_label[lbl].get("_name_raw") or "").strip(),
                    "name_key": str(cur_by_label[lbl].get("_namek") or "").strip(),
                }
                for lbl in sorted(cur_labels - ref_labels)
            ]
            added_labels = [e.get("label_raw") for e in added_entries]

            mapped_pairs = []
            changed_pairs = []
            for lbl in common_labels:
                if cur_label_counts.get(lbl, 0) != 1 or ref_label_counts.get(lbl, 0) != 1:
                    continue
                old_raw = str(ref_by_label[lbl].get("_name_raw") or "").strip()
                new_raw = str(cur_by_label[lbl].get("_name_raw") or "").strip()
                old_key = str(ref_by_label[lbl].get("_namek") or "").strip()
                new_key = str(cur_by_label[lbl].get("_namek") or "").strip()
                label_raw = str(ref_by_label[lbl].get("_label_raw") or cur_by_label[lbl].get("_label_raw") or "").strip()
                if not old_key or not new_key:
                    continue
                pair = {"label": label_raw, "old_raw": old_raw, "new_raw": new_raw, "old_key": old_key, "new_key": new_key}
                mapped_pairs.append(pair)
                if old_key != new_key:
                    changed_pairs.append(pair)

            mapped_n = len(mapped_pairs)
            changed_n = len(changed_pairs)
            missing_n = len(_uniq(missing_labels))
            added_n = len(_uniq(added_labels))
            changed_ratio = (changed_n / mapped_n) if mapped_n else 0.0

            old_num_share = (sum(1 for p in mapped_pairs if _is_numeric_name(p["old_raw"])) / mapped_n) if mapped_n else 0.0
            new_num_share = (sum(1 for p in mapped_pairs if _is_numeric_name(p["new_raw"])) / mapped_n) if mapped_n else 0.0

            is_dictionary = (
                (missing_n == 0)
                and (added_n == 0)
                and (mapped_n >= 3)
                and (changed_n >= 3)
                and (changed_ratio >= 0.8)
                and (old_num_share <= 0.5)
                and (new_num_share >= 0.8)
            )
            is_removed_cascade = (
                (missing_n >= 1)
                and (changed_n >= 1)
                and (mapped_n >= 2)
                and (not is_dictionary)
            )
            is_added_cascade = (
                (missing_n == 0)
                and (added_n >= 1)
                and (changed_n >= 1)
                and (mapped_n >= 2)
                and (not is_dictionary)
            )

            if not (is_dictionary or is_removed_cascade or is_added_cascade):
                continue

            if is_dictionary:
                cls = "option_name_dictionary_replaced"
                suppress_removed = True
                suppress_added = True
            elif is_removed_cascade:
                cls = "removed_option_causes_index_drift"
                suppress_removed = True
                suppress_added = True
            else:
                cls = "added_option_causes_index_drift"
                suppress_removed = False
                suppress_added = True
            classified.append({
                "Q Name": q_name,
                "list_name": list_name,
                "_root_issue": cls,
                "_suppress_removed": suppress_removed,
                "_suppress_added": suppress_added,
            })

            if dual_lang:
                cur_rows_en = cur_norm_en.filter((pl.col("_qk") == qk) & (pl.col("_lkst") == lkst)).to_dicts()
                ref_rows_en = ref_norm_en.filter((pl.col("_qk") == qk) & (pl.col("_lkst") == lkst)).to_dicts()
                ref_en_by_name = {}
                for rr in ref_rows_en:
                    nk = str(rr.get("_namek") or "").strip()
                    if nk and nk not in ref_en_by_name:
                        ref_en_by_name[nk] = str(rr.get("_label_raw") or "").strip()
            else:
                cur_rows_en = cur_rows
                ref_rows_en = ref_rows
                ref_en_by_name = {}

            current_list_tgt = _format_choice_list(cur_rows)
            reference_list_tgt = _format_choice_list(ref_rows)
            current_list_en = _format_choice_list(cur_rows_en)
            reference_list_en = _format_choice_list(ref_rows_en)
            cur_names = [str(r.get("_name_raw") or "").strip() for r in cur_rows]
            ref_names = [str(r.get("_name_raw") or "").strip() for r in ref_rows]
            names_detail = f"cur[{_join_names(cur_names)}] | ref[{_join_names(ref_names)}]"

            if is_dictionary:
                row = {
                    "issue_type": cls,
                    "set_name": "",
                    "Q Name": q_name,
                    "list_name": list_name,
                    "option_name": names_detail,
                    "field": f"option names replaced ({changed_n}/{mapped_n} changed)",
                    "current": "Current list (name | label):\n" + current_list_en,
                    "reference": "Reference list (name | label):\n" + reference_list_en,
                    "severity": "high",
                    "excel_row": None,
                }
                if dual_lang:
                    row["current_lang"] = "Current list (name | label):\n" + current_list_tgt
                    row["reference_lang"] = "Reference list (name | label):\n" + reference_list_tgt
                root_rows.append(row)
            elif is_removed_cascade:
                removed_desc_tgt = _join_limited([
                    f"{e.get('name_raw') or '?'} | {e.get('label_raw') or ''}"
                    for e in missing_entries
                ], limit=6)
                removed_desc_en = _join_limited([
                    f"{e.get('name_raw') or '?'} | {ref_en_by_name.get(e.get('name_key')) or e.get('label_raw') or ''}"
                    for e in missing_entries
                ], limit=6) if dual_lang else removed_desc_tgt

                row = {
                    "issue_type": cls,
                    "set_name": "",
                    "Q Name": q_name,
                    "list_name": list_name,
                    "option_name": names_detail,
                    "field": f"removed option(s) causing drift: {removed_desc_en}",
                    "current": "Current list (name | label):\n" + current_list_en,
                    "reference": "Reference list (name | label):\n" + reference_list_en,
                    "severity": "high",
                    "excel_row": None,
                }
                if dual_lang:
                    row["current_lang"] = "Current list (name | label):\n" + current_list_tgt
                    row["reference_lang"] = "Reference list (name | label):\n" + reference_list_tgt
                root_rows.append(row)
            else:
                added_desc_tgt = _join_limited([
                    f"{e.get('name_raw') or '?'} | {e.get('label_raw') or ''}"
                    for e in added_entries
                ], limit=6)
                added_desc_en = _join_limited([
                    f"{e.get('name_raw') or '?'} | {e.get('label_raw') or ''}"
                    for e in added_entries
                ], limit=6) if dual_lang else added_desc_tgt

                row = {
                    "issue_type": cls,
                    "set_name": "",
                    "Q Name": q_name,
                    "list_name": list_name,
                    "option_name": names_detail,
                    "field": f"added option(s) causing drift: {added_desc_en}",
                    "current": "Current list (name | label):\n" + current_list_en,
                    "reference": "Reference list (name | label):\n" + reference_list_en,
                    "severity": "high",
                    "excel_row": None,
                }
                if dual_lang:
                    row["current_lang"] = "Current list (name | label):\n" + current_list_tgt
                    row["reference_lang"] = "Reference list (name | label):\n" + reference_list_tgt
                root_rows.append(row)

        if not root_rows:
            return option_presence_issues, option_renumber_issues, empty_df

        cls_df = (
            pl.DataFrame(classified)
            .sort(["Q Name", "list_name"])
            .unique(subset=["Q Name", "list_name"], keep="last")
        )
        presence_clean = (
            option_presence_issues
            .join(cls_df, on=["Q Name", "list_name"], how="left")
            .filter(
                ~(
                    ((pl.col("_suppress_removed") == True) & (pl.col("issue_type") == "removed_choice"))
                    | (
                        (pl.col("_suppress_added") == True)
                        & (pl.col("issue_type") == "added_choice")
                    )
                    | (
                        (pl.col("_root_issue") == "option_name_dictionary_replaced")
                        & (pl.col("_suppress_added") == True)
                        & (pl.col("issue_type") == "removed_choice")
                    )
                )
            )
            .drop(["_root_issue", "_suppress_removed", "_suppress_added"])
        )
        renumber_clean = (
            option_renumber_issues
            .join(cls_df, on=["Q Name", "list_name"], how="left")
            .filter(pl.col("_root_issue").is_null())
            .drop(["_root_issue", "_suppress_removed", "_suppress_added"])
        )

        return presence_clean, renumber_clean, pl.DataFrame(root_rows, schema=issue_schema)
    ```

### `classify_choice_name_root_causes._is_numeric_name` {#fn--is-numeric-name-4316}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4316`

**Signature**

```python
def _is_numeric_name(token) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _is_numeric_name(token) -> bool:
            return bool(re.fullmatch(r"\d+(?:\.0+)?", str(token or "").strip()))
    ```

### `classify_choice_name_root_causes._name_sort_key` {#fn--name-sort-key-4319}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4319`

**Signature**

```python
def _name_sort_key(token: str):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _name_sort_key(token: str):
            txt = str(token or "").strip()
            if re.fullmatch(r"\d+(?:\.0+)?", txt):
                return (0, float(txt))
            return (1, txt.lower())
    ```

### `classify_choice_name_root_causes._uniq` {#fn--uniq-4325}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4325`

**Signature**

```python
def _uniq(seq):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `seq` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _uniq(seq):
            seen = set()
            out = []
            for raw in seq:
                token = str(raw or "").strip()
                if not token or token in seen:
                    continue
                seen.add(token)
                out.append(token)
            return out
    ```

### `classify_choice_name_root_causes._join_limited` {#fn--join-limited-4336}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4336`

**Signature**

```python
def _join_limited(items, limit=12):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `items` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `limit` | positional_or_keyword | No | `12` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _join_limited(items, limit=12):
            if not items:
                return "(none)"
            vals = _uniq(items)
            if len(vals) <= limit:
                return ", ".join(vals)
            return ", ".join(vals[:limit]) + f", ... (+{len(vals) - limit} more)"
    ```

### `classify_choice_name_root_causes._join_names` {#fn--join-names-4344}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4344`

**Signature**

```python
def _join_names(items, limit=12):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `items` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `limit` | positional_or_keyword | No | `12` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _join_names(items, limit=12):
            vals = _uniq(items)
            vals = sorted(vals, key=_name_sort_key)
            if not vals:
                return "(none)"
            if len(vals) <= limit:
                return ", ".join(vals)
            return ", ".join(vals[:limit]) + f", ... (+{len(vals) - limit} more)"
    ```

### `classify_choice_name_root_causes._format_choice_list` {#fn--format-choice-list-4353}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4353`

**Signature**

```python
def _format_choice_list(rows: list[dict]) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `rows` | positional_or_keyword | Yes | `-` | `list[dict]` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _format_choice_list(rows: list[dict]) -> str:
            ordered = sorted(rows, key=lambda r: _name_sort_key(r.get("_name_raw")))
            lines = []
            for r in ordered:
                nm = str(r.get("_name_raw") or "").strip()
                lb = str(r.get("_label_raw") or "").strip()
                if not nm and not lb:
                    continue
                lines.append(f"{nm} | {lb}" if lb else nm)
            return "\n".join(lines) if lines else "(none)"
    ```

### `classify_mandatory_choice_set_replaced` {#fn-classify-mandatory-choice-set-replaced-4619}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4619`

**Signature**

```python
def classify_mandatory_choice_set_replaced(current_opts: pl.DataFrame, reference_opts: pl.DataFrame, option_label_issues: pl.DataFrame, option_presence_issues: pl.DataFrame, option_renumber_issues: pl.DataFrame, option_root_cause_issues: pl.DataFrame, reference_survey: pl.DataFrame | None=None, current_survey: pl.DataFrame | None=None, current_opts_en: pl.DataFrame | None=None, reference_opts_en: pl.DataFrame | None=None, target_lang: str='en') -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame]:
```

**Returns:** `tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame]`

**What it does:** Strict detector for mandatory questions where the full choice-set meaning

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_opts` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `reference_opts` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `option_label_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `option_presence_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `option_renumber_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `option_root_cause_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `reference_survey` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |
| `current_survey` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |
| `current_opts_en` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `reference_opts_en` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `target_lang` | positional_or_keyword | No | `'en'` | `str` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def classify_mandatory_choice_set_replaced(
        current_opts: pl.DataFrame,
        reference_opts: pl.DataFrame,
        option_label_issues: pl.DataFrame,
        option_presence_issues: pl.DataFrame,
        option_renumber_issues: pl.DataFrame,
        option_root_cause_issues: pl.DataFrame,
        reference_survey: pl.DataFrame | None = None,
        current_survey: pl.DataFrame | None = None,
        current_opts_en: pl.DataFrame | None = None,
        reference_opts_en: pl.DataFrame | None = None,
        target_lang: str = "en",
    ) -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame]:
        """
        Strict detector for mandatory questions where the full choice-set meaning
        is replaced (zero normalized-label overlap between current and reference).

        Emits exactly one consolidated row per (Q Name, list_name):
          - mandatory_choice_set_replaced (high)
        and suppresses subordinate per-option rows for the same key.
        """
        dual_lang = (
            str(target_lang or "").strip().lower() != "en"
            and current_opts_en is not None
            and reference_opts_en is not None
        )

        issue_schema = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "list_name": pl.Utf8, "option_name": pl.Utf8, "field": pl.Utf8,
            "current": pl.Utf8, "reference": pl.Utf8, "severity": pl.Utf8,
            "excel_row": pl.Int64,
        }
        if dual_lang:
            issue_schema["current_lang"] = pl.Utf8
            issue_schema["reference_lang"] = pl.Utf8
        empty_df = pl.DataFrame(schema=issue_schema)

        if current_opts.height == 0 or reference_opts.height == 0:
            return option_label_issues, option_presence_issues, option_renumber_issues, option_root_cause_issues, empty_df

        # Mandatory lookup (reference + current; current takes precedence on duplicates).
        mand_src = []
        if reference_survey is not None and reference_survey.height > 0 and "mandatory_category" in reference_survey.columns:
            mand_src.append(
                reference_survey
                .select(["Q Name", "mandatory_category"])
                .with_columns(pl.lit(0).alias("_p"))
            )
        if current_survey is not None and current_survey.height > 0 and "mandatory_category" in current_survey.columns:
            mand_src.append(
                current_survey
                .select(["Q Name", "mandatory_category"])
                .with_columns(pl.lit(1).alias("_p"))
            )
        if not mand_src:
            return option_label_issues, option_presence_issues, option_renumber_issues, option_root_cause_issues, empty_df

        mand_lookup = (
            pl.concat(mand_src, how="vertical")
            .sort(["Q Name", "_p"])
            .group_by("Q Name")
            .agg(pl.col("mandatory_category").last().alias("mandatory_category"))
            .with_columns(
                pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase().alias("_qk"),
                pl.col("mandatory_category").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase().alias("_mand"),
            )
            .filter(pl.col("_mand").is_in(["mandatory", "mandatory-panel"]))
            .select(["_qk"])
            .unique()
        )
        if mand_lookup.height == 0:
            return option_label_issues, option_presence_issues, option_renumber_issues, option_root_cause_issues, empty_df

        cur_norm = (
            current_opts
            .with_columns([
                pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase().alias("_qk"),
                _normalized_list_expr("list_name").alias("_lkst"),
                normalize_text_expr("option_label").alias("_lblk"),
                _canonical_option_key_expr("option_name").alias("_namek"),
                pl.col("option_name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_name_raw"),
                pl.col("option_label").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_label_raw"),
            ])
            .filter((pl.col("_qk") != "") & (pl.col("_lkst") != "") & (pl.col("_lblk") != "") & (pl.col("_namek") != ""))
            .select(["_qk", "_lkst", "_lblk", "_namek", "_name_raw", "_label_raw", "Q Name", "list_name"])
        )
        ref_norm = (
            reference_opts
            .with_columns([
                pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase().alias("_qk"),
                _normalized_list_expr("list_name").alias("_lkst"),
                normalize_text_expr("option_label").alias("_lblk"),
                _canonical_option_key_expr("option_name").alias("_namek"),
                pl.col("option_name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_name_raw"),
                pl.col("option_label").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_label_raw"),
            ])
            .filter((pl.col("_qk") != "") & (pl.col("_lkst") != "") & (pl.col("_lblk") != "") & (pl.col("_namek") != ""))
            .select(["_qk", "_lkst", "_lblk", "_namek", "_name_raw", "_label_raw", "Q Name", "list_name"])
        )

        cur_norm_en = None
        ref_norm_en = None
        if dual_lang:
            cur_norm_en = (
                current_opts_en
                .with_columns([
                    pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase().alias("_qk"),
                    _normalized_list_expr("list_name").alias("_lkst"),
                    normalize_text_expr("option_label").alias("_lblk"),
                    _canonical_option_key_expr("option_name").alias("_namek"),
                    pl.col("option_name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_name_raw"),
                    pl.col("option_label").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_label_raw"),
                ])
                .filter((pl.col("_qk") != "") & (pl.col("_lkst") != "") & (pl.col("_lblk") != "") & (pl.col("_namek") != ""))
                .select(["_qk", "_lkst", "_lblk", "_namek", "_name_raw", "_label_raw", "Q Name", "list_name"])
            )
            ref_norm_en = (
                reference_opts_en
                .with_columns([
                    pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase().alias("_qk"),
                    _normalized_list_expr("list_name").alias("_lkst"),
                    normalize_text_expr("option_label").alias("_lblk"),
                    _canonical_option_key_expr("option_name").alias("_namek"),
                    pl.col("option_name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_name_raw"),
                    pl.col("option_label").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_label_raw"),
                ])
                .filter((pl.col("_qk") != "") & (pl.col("_lkst") != "") & (pl.col("_lblk") != "") & (pl.col("_namek") != ""))
                .select(["_qk", "_lkst", "_lblk", "_namek", "_name_raw", "_label_raw", "Q Name", "list_name"])
            )

        def _name_sort_key(token: str):
            txt = str(token or "").strip()
            if re.fullmatch(r"\d+(?:\.0+)?", txt):
                return (0, float(txt))
            return (1, txt.lower())

        def _uniq(seq):
            seen = set()
            out = []
            for raw in seq:
                token = str(raw or "").strip()
                if not token or token in seen:
                    continue
                seen.add(token)
                out.append(token)
            return out

        def _join_names(items, limit=12):
            vals = _uniq(items)
            vals = sorted(vals, key=_name_sort_key)
            if not vals:
                return "(none)"
            if len(vals) <= limit:
                return ", ".join(vals)
            return ", ".join(vals[:limit]) + f", ... (+{len(vals) - limit} more)"

        def _format_choice_list(rows: list[dict]) -> str:
            ordered = sorted(rows, key=lambda r: _name_sort_key(r.get("_name_raw")))
            lines = []
            for r in ordered:
                nm = str(r.get("_name_raw") or "").strip()
                lb = str(r.get("_label_raw") or "").strip()
                if not nm and not lb:
                    continue
                lines.append(f"{nm} | {lb}" if lb else nm)
            return "\n".join(lines) if lines else "(none)"

        candidate_keys = (
            cur_norm.select(["_qk", "_lkst", "Q Name", "list_name"]).unique()
            .join(ref_norm.select(["_qk", "_lkst"]).unique(), on=["_qk", "_lkst"], how="inner")
            .join(mand_lookup, on=["_qk"], how="inner")
        )
        if candidate_keys.height == 0:
            return option_label_issues, option_presence_issues, option_renumber_issues, option_root_cause_issues, empty_df

        root_rows = []
        matched_keys = []
        for key in candidate_keys.to_dicts():
            qk = str(key.get("_qk") or "")
            lkst = str(key.get("_lkst") or "")
            q_name = str(key.get("Q Name") or "")
            list_name = str(key.get("list_name") or "")
            if not qk or not lkst:
                continue

            cur_rows = cur_norm.filter((pl.col("_qk") == qk) & (pl.col("_lkst") == lkst)).to_dicts()
            ref_rows = ref_norm.filter((pl.col("_qk") == qk) & (pl.col("_lkst") == lkst)).to_dicts()
            if not cur_rows or not ref_rows:
                continue

            cur_labels = {str(r.get("_lblk") or "").strip() for r in cur_rows if str(r.get("_lblk") or "").strip()}
            ref_labels = {str(r.get("_lblk") or "").strip() for r in ref_rows if str(r.get("_lblk") or "").strip()}
            if not cur_labels or not ref_labels:
                continue

            # Strict mode: zero normalized-label overlap means complete semantic replacement.
            if cur_labels.intersection(ref_labels):
                continue

            if dual_lang:
                cur_rows_en = cur_norm_en.filter((pl.col("_qk") == qk) & (pl.col("_lkst") == lkst)).to_dicts()
                ref_rows_en = ref_norm_en.filter((pl.col("_qk") == qk) & (pl.col("_lkst") == lkst)).to_dicts()
            else:
                cur_rows_en = cur_rows
                ref_rows_en = ref_rows

            current_list_tgt = _format_choice_list(cur_rows)
            reference_list_tgt = _format_choice_list(ref_rows)
            current_list_en = _format_choice_list(cur_rows_en)
            reference_list_en = _format_choice_list(ref_rows_en)
            cur_names = [str(r.get("_name_raw") or "").strip() for r in cur_rows]
            ref_names = [str(r.get("_name_raw") or "").strip() for r in ref_rows]
            names_detail = f"cur[{_join_names(cur_names)}] | ref[{_join_names(ref_names)}]"

            row = {
                "issue_type": "mandatory_choice_set_replaced",
                "set_name": "",
                "Q Name": q_name,
                "list_name": list_name,
                "option_name": names_detail,
                "field": "complete choice-set replacement (strict: zero label overlap)",
                "current": "Current list (name | label):\n" + current_list_en,
                "reference": "Reference list (name | label):\n" + reference_list_en,
                "severity": "high",
                "excel_row": None,
            }
            if dual_lang:
                row["current_lang"] = "Current list (name | label):\n" + current_list_tgt
                row["reference_lang"] = "Reference list (name | label):\n" + reference_list_tgt
            root_rows.append(row)
            matched_keys.append({"Q Name": q_name, "list_name": list_name})

        if not root_rows:
            return option_label_issues, option_presence_issues, option_renumber_issues, option_root_cause_issues, empty_df

        keys_df = pl.DataFrame(matched_keys).unique(subset=["Q Name", "list_name"], keep="last")
        option_label_clean = option_label_issues.join(keys_df, on=["Q Name", "list_name"], how="anti")
        option_presence_clean = option_presence_issues.join(keys_df, on=["Q Name", "list_name"], how="anti")
        option_renumber_clean = option_renumber_issues.join(keys_df, on=["Q Name", "list_name"], how="anti")
        option_root_cause_clean = option_root_cause_issues.join(keys_df, on=["Q Name", "list_name"], how="anti")

        return (
            option_label_clean,
            option_presence_clean,
            option_renumber_clean,
            option_root_cause_clean,
            pl.DataFrame(root_rows, schema=issue_schema),
        )
    ```

### `classify_mandatory_choice_set_replaced._name_sort_key` {#fn--name-sort-key-4750}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4750`

**Signature**

```python
def _name_sort_key(token: str):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _name_sort_key(token: str):
            txt = str(token or "").strip()
            if re.fullmatch(r"\d+(?:\.0+)?", txt):
                return (0, float(txt))
            return (1, txt.lower())
    ```

### `classify_mandatory_choice_set_replaced._uniq` {#fn--uniq-4756}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4756`

**Signature**

```python
def _uniq(seq):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `seq` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _uniq(seq):
            seen = set()
            out = []
            for raw in seq:
                token = str(raw or "").strip()
                if not token or token in seen:
                    continue
                seen.add(token)
                out.append(token)
            return out
    ```

### `classify_mandatory_choice_set_replaced._join_names` {#fn--join-names-4767}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4767`

**Signature**

```python
def _join_names(items, limit=12):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `items` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `limit` | positional_or_keyword | No | `12` | `-` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _join_names(items, limit=12):
            vals = _uniq(items)
            vals = sorted(vals, key=_name_sort_key)
            if not vals:
                return "(none)"
            if len(vals) <= limit:
                return ", ".join(vals)
            return ", ".join(vals[:limit]) + f", ... (+{len(vals) - limit} more)"
    ```

### `classify_mandatory_choice_set_replaced._format_choice_list` {#fn--format-choice-list-4776}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4776`

**Signature**

```python
def _format_choice_list(rows: list[dict]) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `rows` | positional_or_keyword | Yes | `-` | `list[dict]` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _format_choice_list(rows: list[dict]) -> str:
            ordered = sorted(rows, key=lambda r: _name_sort_key(r.get("_name_raw")))
            lines = []
            for r in ordered:
                nm = str(r.get("_name_raw") or "").strip()
                lb = str(r.get("_label_raw") or "").strip()
                if not nm and not lb:
                    continue
                lines.append(f"{nm} | {lb}" if lb else nm)
            return "\n".join(lines) if lines else "(none)"
    ```

### `collapse_cluster_ea_option_changes` {#fn-collapse-cluster-ea-option-changes-4870}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4870`

**Signature**

```python
def collapse_cluster_ea_option_changes(option_label_issues: pl.DataFrame, option_presence_issues: pl.DataFrame, option_renumber_issues: pl.DataFrame) -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame]:
```

**Returns:** `tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame]`

**What it does:** Suppress noisy per-option diffs for KoBo cluster/ea lists and replace them

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `option_label_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `option_presence_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `option_renumber_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def collapse_cluster_ea_option_changes(
        option_label_issues: pl.DataFrame,
        option_presence_issues: pl.DataFrame,
        option_renumber_issues: pl.DataFrame,
    ) -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame]:
        """
        Suppress noisy per-option diffs for KoBo cluster/ea lists and replace them
        with a single informational summary row.
        """
        issue_schema = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "list_name": pl.Utf8, "option_name": pl.Utf8, "field": pl.Utf8,
            "current": pl.Utf8, "reference": pl.Utf8, "severity": pl.Utf8,
            "excel_row": pl.Int64,
        }

        q_expr = pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase()
        list_expr = pl.col("list_name").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase()
        ea_cluster_mask = (q_expr == "cluster") & (list_expr == "ea")

        modified_n = option_label_issues.filter(ea_cluster_mask).height if option_label_issues.height else 0
        added_n = option_presence_issues.filter(ea_cluster_mask & (pl.col("issue_type") == "added_choice")).height if option_presence_issues.height else 0
        removed_n = option_presence_issues.filter(ea_cluster_mask & (pl.col("issue_type") == "removed_choice")).height if option_presence_issues.height else 0
        renamed_n = option_renumber_issues.filter(ea_cluster_mask).height if option_renumber_issues.height else 0

        option_label_clean = option_label_issues.filter(~ea_cluster_mask) if option_label_issues.height else option_label_issues
        option_presence_clean = option_presence_issues.filter(~ea_cluster_mask) if option_presence_issues.height else option_presence_issues
        option_renumber_clean = option_renumber_issues.filter(~ea_cluster_mask) if option_renumber_issues.height else option_renumber_issues

        total = modified_n + added_n + removed_n + renamed_n
        if total == 0:
            return option_label_clean, option_presence_clean, option_renumber_clean, pl.DataFrame(schema=issue_schema)

        summary_row = pl.DataFrame([{
            "issue_type": "cluster_ea_choice_changes_summary",
            "set_name": "",
            "Q Name": "cluster",
            "list_name": "ea",
            "option_name": "",
            "field": "choices",
            "current": f"added={added_n}; removed={removed_n}; modified={modified_n}; renamed={renamed_n}",
            "reference": "Detailed cluster/ea per-option differences suppressed (expected round-to-round rotation)",
            "severity": "info",
            "excel_row": None,
        }], schema=issue_schema)

        return option_label_clean, option_presence_clean, option_renumber_clean, summary_row
    ```

### `_join_tokens_limited` {#fn--join-tokens-limited-4919}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4919`

**Signature**

```python
def _join_tokens_limited(tokens: list[str], limit: int=16) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `tokens` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `limit` | positional_or_keyword | No | `16` | `int` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _join_tokens_limited(tokens: list[str], limit: int = 16) -> str:
        seen = set()
        vals: list[str] = []
        for raw in tokens:
            t = str(raw or "").strip()
            if not t or t in seen:
                continue
            seen.add(t)
            vals.append(t)
        if not vals:
            return "(none)"
        if len(vals) <= limit:
            return ", ".join(vals)
        return ", ".join(vals[:limit]) + f", ... (+{len(vals) - limit} more)"
    ```

### `_format_collapsed_choice_side` {#fn--format-collapsed-choice-side-4935}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4935`

**Signature**

```python
def _format_collapsed_choice_side(rows: list[dict], value_key: str, header: str, empty_label: str='(empty)') -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `rows` | positional_or_keyword | Yes | `-` | `list[dict]` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `value_key` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `header` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `empty_label` | positional_or_keyword | No | `'(empty)'` | `str` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _format_collapsed_choice_side(
        rows: list[dict],
        value_key: str,
        header: str,
        empty_label: str = "(empty)",
    ) -> str:
        entries: list[tuple[str, str]] = []
        for r in rows or []:
            entries.append((
                str(r.get("option_name") or "").strip(),
                str(r.get(value_key) or "").strip(),
            ))
        return _format_choice_entries(entries, header, empty_label=empty_label)
    ```

### `_format_choice_entries` {#fn--format-choice-entries-4950}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4950`

**Signature**

```python
def _format_choice_entries(entries: list[tuple[str, str]], header: str, empty_label: str='(empty)') -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `header` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `empty_label` | positional_or_keyword | No | `'(empty)'` | `str` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _format_choice_entries(
        entries: list[tuple[str, str]],
        header: str,
        empty_label: str = "(empty)",
    ) -> str:
        if not entries:
            return f"{header}:\n{empty_label}"

        out_lines: list[str] = []
        seen: set[tuple[str, str]] = set()
        idx = 0
        for opt_raw, val_raw in entries:
            opt = str(opt_raw or "").strip()
            val = str(val_raw or "").strip()
            if not opt and not val:
                continue
            key = (opt, val)
            if key in seen:
                continue
            seen.add(key)
            idx += 1
            if opt:
                out_lines.append(f"{idx} | {opt} | {val or '(blank)'}")
            else:
                out_lines.append(f"{idx} | {val}")
        if not out_lines:
            return f"{header}:\n{empty_label}"
        return f"{header}:\n" + "\n".join(out_lines)
    ```

### `_build_choice_lookup` {#fn--build-choice-lookup-4980}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:4980`

**Signature**

```python
def _build_choice_lookup(options_df: pl.DataFrame | None) -> dict[tuple[str, str], list[tuple[str, str]]]:
```

**Returns:** `dict[tuple[str, str], list[tuple[str, str]]]`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `options_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def _build_choice_lookup(options_df: pl.DataFrame | None) -> dict[tuple[str, str], list[tuple[str, str]]]:
        out: dict[tuple[str, str], list[tuple[str, str]]] = {}
        if options_df is None or options_df.height == 0:
            return out
        if not {"Q Name", "list_name", "option_name", "option_label"}.issubset(set(options_df.columns)):
            return out

        seen_per_key: dict[tuple[str, str], set[str]] = {}
        for row in options_df.select(["Q Name", "list_name", "option_name", "option_label"]).iter_rows(named=True):
            qn_raw = str(row.get("Q Name") or "").strip()
            ln_raw = str(row.get("list_name") or "").strip()
            if not qn_raw or not ln_raw:
                continue
            key = (qn_raw.lower(), _normalize_list_token(ln_raw))
            if not key[1]:
                continue
            name_raw = str(row.get("option_name") or "").strip()
            label_raw = str(row.get("option_label") or "").strip()
            ckey = _canonical_option_name_token(name_raw)
            if not ckey:
                continue
            seen = seen_per_key.setdefault(key, set())
            if ckey in seen:
                continue
            seen.add(ckey)
            out.setdefault(key, []).append((name_raw, label_raw))
        return out
    ```

### `_collapsed_choice_detail` {#fn--collapsed-choice-detail-5009}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:5009`

**Signature**

```python
def _collapsed_choice_detail(issue_type: str, n_rows: int, current_total: int | None=None, reference_total: int | None=None) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `issue_type` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `n_rows` | positional_or_keyword | Yes | `-` | `int` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `current_total` | positional_or_keyword | No | `None` | `int | None` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `reference_total` | positional_or_keyword | No | `None` | `int | None` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _collapsed_choice_detail(
        issue_type: str,
        n_rows: int,
        current_total: int | None = None,
        reference_total: int | None = None,
    ) -> str:
        issue_map = {
            "added_choice": f"{n_rows} option(s) added vs reference",
            "removed_choice": f"{n_rows} option(s) removed vs reference",
            "choice_label_mismatch": f"{n_rows} option label(s) changed",
            "option_index_drift": f"{n_rows} option code/index drift case(s)",
        }
        head = issue_map.get(str(issue_type or "").strip(), f"{n_rows} choice change row(s)")
        if current_total is not None and reference_total is not None:
            return f"{head}; current total={current_total}, reference total={reference_total}"
        return f"{head}; grouped in one row for this question/list"
    ```

### `_ordered_unique_names` {#fn--ordered-unique-names-5027}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:5027`

**Signature**

```python
def _ordered_unique_names(rows: list[dict], field_name: str='option_name') -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `rows` | positional_or_keyword | Yes | `-` | `list[dict]` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `field_name` | positional_or_keyword | No | `'option_name'` | `str` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _ordered_unique_names(rows: list[dict], field_name: str = "option_name") -> list[str]:
        out: list[str] = []
        seen: set[str] = set()
        for r in rows:
            raw = str(r.get(field_name) or "").strip()
            key = _canonical_option_name_token(raw)
            if not key or key in seen:
                continue
            seen.add(key)
            out.append(raw)
        return out
    ```

### `_ordered_added_removed_names` {#fn--ordered-added-removed-names-5040}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:5040`

**Signature**

```python
def _ordered_added_removed_names(current_entries: list[tuple[str, str]], reference_entries: list[tuple[str, str]]) -> tuple[list[str], list[str]]:
```

**Returns:** `tuple[list[str], list[str]]`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `reference_entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _ordered_added_removed_names(
        current_entries: list[tuple[str, str]],
        reference_entries: list[tuple[str, str]],
    ) -> tuple[list[str], list[str]]:
        cur_norm_order: list[str] = []
        cur_name_raw: dict[str, str] = {}
        for nm, _lb in current_entries or []:
            raw = str(nm or "").strip()
            key = _canonical_option_name_token(raw)
            if not key or key in cur_name_raw:
                continue
            cur_name_raw[key] = raw
            cur_norm_order.append(key)

        ref_norm_order: list[str] = []
        ref_name_raw: dict[str, str] = {}
        for nm, _lb in reference_entries or []:
            raw = str(nm or "").strip()
            key = _canonical_option_name_token(raw)
            if not key or key in ref_name_raw:
                continue
            ref_name_raw[key] = raw
            ref_norm_order.append(key)

        ref_set = set(ref_norm_order)
        cur_set = set(cur_norm_order)

        added = [cur_name_raw[k] for k in cur_norm_order if k not in ref_set]
        removed = [ref_name_raw[k] for k in ref_norm_order if k not in cur_set]
        return added, removed
    ```

### `merge_added_removed_choice_rows` {#fn-merge-added-removed-choice-rows-5072}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:5072`

**Signature**

```python
def merge_added_removed_choice_rows(option_presence_issues: pl.DataFrame, current_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None=None, reference_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None=None, current_lang_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None=None, reference_lang_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** If a (Q Name, list_name) has both added_choice and removed_choice rows,

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `option_presence_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `current_lookup` | positional_or_keyword | No | `None` | `dict[tuple[str, str], list[tuple[str, str]]] | None` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `reference_lookup` | positional_or_keyword | No | `None` | `dict[tuple[str, str], list[tuple[str, str]]] | None` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `current_lang_lookup` | positional_or_keyword | No | `None` | `dict[tuple[str, str], list[tuple[str, str]]] | None` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `reference_lang_lookup` | positional_or_keyword | No | `None` | `dict[tuple[str, str], list[tuple[str, str]]] | None` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def merge_added_removed_choice_rows(
        option_presence_issues: pl.DataFrame,
        current_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None = None,
        reference_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None = None,
        current_lang_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None = None,
        reference_lang_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None = None,
    ) -> pl.DataFrame:
        """
        If a (Q Name, list_name) has both added_choice and removed_choice rows,
        replace them with one general consolidated row.
        """
        df = option_presence_issues
        if df is None or df.height == 0:
            return df
        if not {"issue_type", "Q Name", "list_name"}.issubset(set(df.columns)):
            return df

        target = df.filter(pl.col("issue_type").is_in(["added_choice", "removed_choice"]))
        if target.height == 0:
            return df

        keys = (
            target
            .group_by(["Q Name", "list_name"])
            .agg([
                (pl.col("issue_type") == "added_choice").any().alias("_has_added"),
                (pl.col("issue_type") == "removed_choice").any().alias("_has_removed"),
            ])
            .filter(pl.col("_has_added") & pl.col("_has_removed"))
            .select(["Q Name", "list_name"])
        )
        if keys.height == 0:
            return df

        has_cur_lang = "current_lang" in df.columns
        has_ref_lang = "reference_lang" in df.columns
        key_rows = keys.to_dicts()
        merged_rows: list[dict] = []
        for k in key_rows:
            qn = str(k.get("Q Name") or "")
            ln = str(k.get("list_name") or "")
            if not qn or not ln:
                continue
            key_norm = (qn.strip().lower(), _normalize_list_token(ln))

            sub = target.filter((pl.col("Q Name") == qn) & (pl.col("list_name") == ln))
            added_rows = sub.filter(pl.col("issue_type") == "added_choice").to_dicts()
            removed_rows = sub.filter(pl.col("issue_type") == "removed_choice").to_dicts()
            if not added_rows or not removed_rows:
                continue

            cur_entries = (current_lookup or {}).get(key_norm, [])
            ref_entries = (reference_lookup or {}).get(key_norm, [])
            cur_lang_entries = (current_lang_lookup or {}).get(key_norm, [])
            ref_lang_entries = (reference_lang_lookup or {}).get(key_norm, [])

            if cur_entries or ref_entries:
                added_names, removed_names = _ordered_added_removed_names(cur_entries, ref_entries)
            else:
                added_names = _ordered_unique_names(added_rows)
                removed_names = _ordered_unique_names(removed_rows)

            added_n = len(added_names)
            removed_n = len(removed_names)
            cur_total = len(cur_entries) if cur_entries else added_n + max(len(_ordered_unique_names(removed_rows)), 0)
            ref_total = len(ref_entries) if ref_entries else removed_n + max(len(_ordered_unique_names(added_rows)), 0)

            added_txt = _join_tokens_limited(added_names, limit=24)
            removed_txt = _join_tokens_limited(removed_names, limit=24)
            detail = (
                f"both added and removed options: added={added_n}, removed={removed_n}; "
                f"current total={cur_total}, reference total={ref_total} "
                f"(added: {added_txt}; removed: {removed_txt})"
            )

            severities = [str(r.get("severity") or "").strip().lower() for r in (added_rows + removed_rows)]
            sev = "info"
            if "high" in severities:
                sev = "high"
            elif "medium" in severities:
                sev = "medium"

            excel_rows = [r.get("excel_row") for r in (added_rows + removed_rows) if r.get("excel_row") is not None]

            merged = {
                "issue_type": "choice_changes_general",
                "set_name": "",
                "Q Name": qn,
                "list_name": ln,
                "option_name": f"added[{added_txt}] | removed[{removed_txt}]",
                "field": detail,
                "current": _format_choice_entries(cur_entries, "Current list (name | label)")
                if cur_entries else _format_collapsed_choice_side(added_rows + removed_rows, "current", "Current list (name | label)"),
                "reference": _format_choice_entries(ref_entries, "Reference list (name | label)")
                if ref_entries else _format_collapsed_choice_side(added_rows + removed_rows, "reference", "Reference list (name | label)"),
                "severity": sev,
                "excel_row": min(excel_rows) if excel_rows else None,
            }
            if has_cur_lang:
                merged["current_lang"] = (
                    _format_choice_entries(cur_lang_entries, "Current list (name | label)")
                    if cur_lang_entries
                    else ""
                )
            if has_ref_lang:
                merged["reference_lang"] = (
                    _format_choice_entries(ref_lang_entries, "Reference list (name | label)")
                    if ref_lang_entries
                    else ""
                )
            merged_rows.append(merged)

        if not merged_rows:
            return df

        merged_df = pl.DataFrame(merged_rows)
        for col in df.columns:
            if col not in merged_df.columns:
                merged_df = merged_df.with_columns(pl.lit(None).alias(col))
        merged_df = merged_df.select(df.columns)

        df_no_pairs = df.join(keys, on=["Q Name", "list_name"], how="anti")
        return pl.concat([df_no_pairs, merged_df], how="vertical")
    ```

### `collapse_choice_issue_rows_by_key` {#fn-collapse-choice-issue-rows-by-key-5197}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:5197`

**Signature**

```python
def collapse_choice_issue_rows_by_key(df: pl.DataFrame, issue_types: list[str], current_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None=None, reference_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None=None, current_lang_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None=None, reference_lang_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Reduce per-option noise by collapsing rows into one row per

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `issue_types` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `current_lookup` | positional_or_keyword | No | `None` | `dict[tuple[str, str], list[tuple[str, str]]] | None` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `reference_lookup` | positional_or_keyword | No | `None` | `dict[tuple[str, str], list[tuple[str, str]]] | None` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `current_lang_lookup` | positional_or_keyword | No | `None` | `dict[tuple[str, str], list[tuple[str, str]]] | None` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `reference_lang_lookup` | positional_or_keyword | No | `None` | `dict[tuple[str, str], list[tuple[str, str]]] | None` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def collapse_choice_issue_rows_by_key(
        df: pl.DataFrame,
        issue_types: list[str],
        current_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None = None,
        reference_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None = None,
        current_lang_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None = None,
        reference_lang_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None = None,
    ) -> pl.DataFrame:
        """
        Reduce per-option noise by collapsing rows into one row per
        (issue_type, Q Name, list_name), preserving issue semantics.
        """
        if df.height == 0:
            return df
        if not {"issue_type", "Q Name", "list_name"}.issubset(set(df.columns)):
            return df

        target = set(issue_types or [])
        if not target:
            return df

        mask = pl.col("issue_type").is_in(list(target))
        keep_df = df.filter(~mask)
        noisy_df = df.filter(mask)
        if noisy_df.height == 0:
            return df

        has_cur_lang = "current_lang" in noisy_df.columns
        has_ref_lang = "reference_lang" in noisy_df.columns

        def _filter_choice_entries_by_names(
            entries: list[tuple[str, str]],
            names_keep: set[str],
        ) -> list[tuple[str, str]]:
            if not entries or not names_keep:
                return []
            out: list[tuple[str, str]] = []
            seen: set[str] = set()
            for nm, lb in entries:
                nk = _canonical_option_name_token(nm)
                if not nk or nk in seen or nk not in names_keep:
                    continue
                seen.add(nk)
                out.append((str(nm or "").strip(), str(lb or "").strip()))
            return out

        grouped_rows: list[dict] = []
        for grp in noisy_df.group_by(["issue_type", "Q Name", "list_name"]).agg(pl.len().alias("_n")).to_dicts():
            it = str(grp.get("issue_type") or "")
            qn = str(grp.get("Q Name") or "")
            ln = str(grp.get("list_name") or "")
            key_norm = (qn.strip().lower(), _normalize_list_token(ln))
            sub = noisy_df.filter(
                (pl.col("issue_type") == it)
                & (pl.col("Q Name") == qn)
                & (pl.col("list_name") == ln)
            )
            rows = sub.to_dicts()
            n = len(rows)

            opt_names = [r.get("option_name") for r in rows]
            currents = [r.get("current") for r in rows]
            refs = [r.get("reference") for r in rows]
            severities = [str(r.get("severity") or "").strip().lower() for r in rows]
            excel_rows = [r.get("excel_row") for r in rows if r.get("excel_row") is not None]

            cur_lang_vals = [r.get("current_lang") for r in rows] if has_cur_lang else []
            ref_lang_vals = [r.get("reference_lang") for r in rows] if has_ref_lang else []

            sev = "info"
            if "high" in severities:
                sev = "high"
            elif "medium" in severities:
                sev = "medium"

            cur_entries = (current_lookup or {}).get(key_norm, [])
            ref_entries = (reference_lookup or {}).get(key_norm, [])
            cur_lang_entries = (current_lang_lookup or {}).get(key_norm, [])
            ref_lang_entries = (reference_lang_lookup or {}).get(key_norm, [])
            cur_total = len(cur_entries) if cur_entries else None
            ref_total = len(ref_entries) if ref_entries else None
            cur_total_for_detail = cur_total
            ref_total_for_detail = ref_total

            if it == "choice_label_mismatch" and (cur_entries or ref_entries):
                mismatch_name_keys = {
                    _canonical_option_name_token(r.get("option_name"))
                    for r in rows
                }
                mismatch_name_keys = {k for k in mismatch_name_keys if k}
                cur_entries_mm = _filter_choice_entries_by_names(cur_entries, mismatch_name_keys)
                ref_entries_mm = _filter_choice_entries_by_names(ref_entries, mismatch_name_keys)
                cur_total_for_detail = len(cur_entries_mm)
                ref_total_for_detail = len(ref_entries_mm)

                cur_txt = _format_choice_entries(cur_entries_mm, "Current list (name | label)")
                ref_txt = _format_choice_entries(ref_entries_mm, "Reference list (name | label)")
            else:
                cur_txt = (
                    _format_choice_entries(cur_entries, "Current list (name | label)")
                    if cur_entries or ref_entries
                    else _format_collapsed_choice_side(rows, "current", "Current list (name | label)")
                )
                ref_txt = (
                    _format_choice_entries(ref_entries, "Reference list (name | label)")
                    if cur_entries or ref_entries
                    else _format_collapsed_choice_side(rows, "reference", "Reference list (name | label)")
                )

            row = {
                "issue_type": it,
                "set_name": "",
                "Q Name": qn,
                "list_name": ln,
                "option_name": _join_tokens_limited(opt_names, limit=20),
                "field": _collapsed_choice_detail(it, n, current_total=cur_total_for_detail, reference_total=ref_total_for_detail),
                "current": cur_txt,
                "reference": ref_txt,
                "severity": sev,
                "excel_row": min(excel_rows) if excel_rows else None,
            }
            if has_cur_lang:
                if it == "choice_label_mismatch" and (cur_lang_entries or ref_lang_entries):
                    mismatch_name_keys = {
                        _canonical_option_name_token(r.get("option_name"))
                        for r in rows
                    }
                    mismatch_name_keys = {k for k in mismatch_name_keys if k}
                    row["current_lang"] = _format_choice_entries(
                        _filter_choice_entries_by_names(cur_lang_entries, mismatch_name_keys),
                        "Current list (name | label)",
                    )
                else:
                    row["current_lang"] = (
                        _format_choice_entries(cur_lang_entries, "Current list (name | label)")
                        if (cur_lang_entries or ref_lang_entries)
                        else (
                            _format_collapsed_choice_side(rows, "current_lang", "Current list (name | label)")
                            if any(str(v or "").strip() for v in cur_lang_vals)
                            else ""
                        )
                    )
            if has_ref_lang:
                if it == "choice_label_mismatch" and (cur_lang_entries or ref_lang_entries):
                    mismatch_name_keys = {
                        _canonical_option_name_token(r.get("option_name"))
                        for r in rows
                    }
                    mismatch_name_keys = {k for k in mismatch_name_keys if k}
                    row["reference_lang"] = _format_choice_entries(
                        _filter_choice_entries_by_names(ref_lang_entries, mismatch_name_keys),
                        "Reference list (name | label)",
                    )
                else:
                    row["reference_lang"] = (
                        _format_choice_entries(ref_lang_entries, "Reference list (name | label)")
                        if (cur_lang_entries or ref_lang_entries)
                        else (
                            _format_collapsed_choice_side(rows, "reference_lang", "Reference list (name | label)")
                            if any(str(v or "").strip() for v in ref_lang_vals)
                            else ""
                        )
                    )
            grouped_rows.append(row)

        collapsed_df = pl.DataFrame(grouped_rows) if grouped_rows else pl.DataFrame(schema=noisy_df.schema)
        for col in noisy_df.columns:
            if col not in collapsed_df.columns:
                collapsed_df = collapsed_df.with_columns(pl.lit(None).alias(col))
        collapsed_df = collapsed_df.select(noisy_df.columns)
        return pl.concat([keep_df, collapsed_df], how="vertical")
    ```

### `collapse_choice_issue_rows_by_key._filter_choice_entries_by_names` {#fn--filter-choice-entries-by-names-5227}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:5227`

**Signature**

```python
def _filter_choice_entries_by_names(entries: list[tuple[str, str]], names_keep: set[str]) -> list[tuple[str, str]]:
```

**Returns:** `list[tuple[str, str]]`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `names_keep` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _filter_choice_entries_by_names(
            entries: list[tuple[str, str]],
            names_keep: set[str],
        ) -> list[tuple[str, str]]:
            if not entries or not names_keep:
                return []
            out: list[tuple[str, str]] = []
            seen: set[str] = set()
            for nm, lb in entries:
                nk = _canonical_option_name_token(nm)
                if not nk or nk in seen or nk not in names_keep:
                    continue
                seen.add(nk)
                out.append((str(nm or "").strip(), str(lb or "").strip()))
            return out
    ```

### `suppress_enumerator_option_details` {#fn-suppress-enumerator-option-details-5370}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:5370`

**Signature**

```python
def suppress_enumerator_option_details(option_label_issues: pl.DataFrame, option_presence_issues: pl.DataFrame, option_renumber_issues: pl.DataFrame, option_root_cause_issues: pl.DataFrame, option_complete_replace_issues: pl.DataFrame, current_options_source: pl.DataFrame | None=None) -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame]:
```

**Returns:** `tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame]`

**What it does:** Suppress enumerator per-option change rows and return one informational summary row.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `option_label_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `option_presence_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `option_renumber_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `option_root_cause_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `option_complete_replace_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `current_options_source` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def suppress_enumerator_option_details(
        option_label_issues: pl.DataFrame,
        option_presence_issues: pl.DataFrame,
        option_renumber_issues: pl.DataFrame,
        option_root_cause_issues: pl.DataFrame,
        option_complete_replace_issues: pl.DataFrame,
        current_options_source: pl.DataFrame | None = None,
    ) -> tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame, pl.DataFrame]:
        """
        Suppress enumerator per-option change rows and return one informational summary row.
        """
        issue_schema = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "list_name": pl.Utf8, "option_name": pl.Utf8, "field": pl.Utf8,
            "current": pl.Utf8, "reference": pl.Utf8, "severity": pl.Utf8,
            "excel_row": pl.Int64,
        }

        q_expr = pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase()
        enum_mask = q_expr == "enumerator"

        def _split(df: pl.DataFrame) -> tuple[pl.DataFrame, int]:
            if df.height == 0:
                return df, 0
            n = df.filter(enum_mask).height
            return df.filter(~enum_mask), n

        option_label_clean, n_lbl = _split(option_label_issues)
        option_presence_clean, n_pres = _split(option_presence_issues)
        option_renumber_clean, n_ren = _split(option_renumber_issues)
        option_root_clean, n_root = _split(option_root_cause_issues)
        option_complete_clean, n_comp = _split(option_complete_replace_issues)

        enum_count = 0
        if current_options_source is not None and current_options_source.height > 0:
            enum_rows = (
                current_options_source
                .filter(
                    pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase() == "enumerator"
                )
                .with_columns(_canonical_option_key_expr("option_name").alias("_ok"))
                .filter(pl.col("_ok") != "")
                .select(["_ok"])
                .unique()
            )
            enum_count = enum_rows.height

        suppressed_total = n_lbl + n_pres + n_ren + n_root + n_comp
        if suppressed_total == 0 and enum_count == 0:
            return (
                option_label_clean,
                option_presence_clean,
                option_renumber_clean,
                option_root_clean,
                option_complete_clean,
                pl.DataFrame(schema=issue_schema),
            )

        summary_row = pl.DataFrame([{
            "issue_type": "enumerator_choice_changes_summary",
            "set_name": "",
            "Q Name": "enumerator",
            "list_name": "enumerator",
            "option_name": "",
            "field": "choices",
            "current": f"Enumerator choices present in current: {enum_count}",
            "reference": f"Detailed enumerator option differences suppressed ({suppressed_total} row(s))",
            "severity": "info",
            "excel_row": None,
        }], schema=issue_schema)

        return (
            option_label_clean,
            option_presence_clean,
            option_renumber_clean,
            option_root_clean,
            option_complete_clean,
            summary_row,
        )
    ```

### `suppress_enumerator_option_details._split` {#fn--split-5391}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:5391`

**Signature**

```python
def _split(df: pl.DataFrame) -> tuple[pl.DataFrame, int]:
```

**Returns:** `tuple[pl.DataFrame, int]`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _split(df: pl.DataFrame) -> tuple[pl.DataFrame, int]:
            if df.height == 0:
                return df, 0
            n = df.filter(enum_mask).height
            return df.filter(~enum_mask), n
    ```

### `suppress_structural_choice_label_noise` {#fn-suppress-structural-choice-label-noise-5451}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:5451`

**Signature**

```python
def suppress_structural_choice_label_noise(option_label_issues: pl.DataFrame, option_presence_issues: pl.DataFrame, option_renumber_issues: pl.DataFrame, current_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None=None, reference_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Remove only *derived* choice_label_mismatch rows caused by structural add/remove

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `option_label_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `option_presence_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `option_renumber_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `current_lookup` | positional_or_keyword | No | `None` | `dict[tuple[str, str], list[tuple[str, str]]] | None` | Input used by the `Step 9 -- Issue unifiers` stage. |
| `reference_lookup` | positional_or_keyword | No | `None` | `dict[tuple[str, str], list[tuple[str, str]]] | None` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def suppress_structural_choice_label_noise(
        option_label_issues: pl.DataFrame,
        option_presence_issues: pl.DataFrame,
        option_renumber_issues: pl.DataFrame,
        current_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None = None,
        reference_lookup: dict[tuple[str, str], list[tuple[str, str]]] | None = None,
    ) -> pl.DataFrame:
        """
        Remove only *derived* choice_label_mismatch rows caused by structural add/remove
        or renumber drift, while keeping genuine label edits for unchanged names.
        """
        if option_label_issues is None or option_label_issues.height == 0:
            return option_label_issues
        if not {"issue_type", "Q Name", "list_name", "option_name"}.issubset(set(option_label_issues.columns)):
            return option_label_issues

        if option_presence_issues is None or option_presence_issues.height == 0:
            return option_label_issues
        if not {"issue_type", "Q Name", "list_name"}.issubset(set(option_presence_issues.columns)):
            return option_label_issues

        structural_keys_df = (
            option_presence_issues
            .filter(pl.col("issue_type").is_in(["added_choice", "removed_choice", "choice_changes_general"]))
            .select(["Q Name", "list_name"])
            .unique()
        )
        if structural_keys_df.height == 0:
            return option_label_issues

        structural_keys = {
            (str(r.get("Q Name") or "").strip().lower(), _normalize_list_token(r.get("list_name")))
            for r in structural_keys_df.to_dicts()
        }

        renumber_triples: set[tuple[str, str, str]] = set()
        if (
            option_renumber_issues is not None
            and option_renumber_issues.height > 0
            and {"Q Name", "list_name", "option_name"}.issubset(set(option_renumber_issues.columns))
        ):
            for r in option_renumber_issues.to_dicts():
                qk = str(r.get("Q Name") or "").strip().lower()
                lk = _normalize_list_token(r.get("list_name"))
                nk = _canonical_option_name_token(r.get("option_name"))
                if qk and lk and nk:
                    renumber_triples.add((qk, lk, nk))

        def _norm_lbl(x: str) -> str:
            return re.sub(r"\s+", " ", str(x or "").strip().lower())

        def _name_to_label(entries: list[tuple[str, str]]) -> dict[str, str]:
            out: dict[str, str] = {}
            for nm, lb in entries or []:
                nk = _canonical_option_name_token(nm)
                if not nk or nk in out:
                    continue
                out[nk] = _norm_lbl(lb)
            return out

        kept_rows: list[dict] = []
        for row in option_label_issues.to_dicts():
            if str(row.get("issue_type") or "") != "choice_label_mismatch":
                kept_rows.append(row)
                continue

            qk = str(row.get("Q Name") or "").strip().lower()
            lk = _normalize_list_token(row.get("list_name"))
            nk = _canonical_option_name_token(row.get("option_name"))
            key = (qk, lk)

            # If this question/list has no structural add/remove, always keep.
            if key not in structural_keys:
                kept_rows.append(row)
                continue

            # Direct renumber for this option name => derived noise, suppress.
            if qk and lk and nk and (qk, lk, nk) in renumber_triples:
                continue

            cur_map = _name_to_label((current_lookup or {}).get(key, []))
            ref_map = _name_to_label((reference_lookup or {}).get(key, []))
            if not nk or nk not in cur_map or nk not in ref_map:
                # If we cannot prove drift for this row, keep it.
                kept_rows.append(row)
                continue

            cur_lbl = cur_map.get(nk, "")
            ref_lbl = ref_map.get(nk, "")
            if not cur_lbl or not ref_lbl:
                kept_rows.append(row)
                continue

            # Shift-like mismatch: this option appears to have inherited another option's label
            # or vice versa after structural changes.
            is_shift_like = False
            common_names = set(cur_map.keys()) & set(ref_map.keys())
            if nk in common_names:
                common_names.remove(nk)
            for ok in common_names:
                if cur_lbl == ref_map.get(ok, "") or ref_lbl == cur_map.get(ok, ""):
                    is_shift_like = True
                    break

            if is_shift_like:
                continue
            kept_rows.append(row)

        if not kept_rows:
            return pl.DataFrame(schema=option_label_issues.schema)
        out = pl.DataFrame(kept_rows)
        for col in option_label_issues.columns:
            if col not in out.columns:
                out = out.with_columns(pl.lit(None).alias(col))
        return out.select(option_label_issues.columns)
    ```

### `suppress_structural_choice_label_noise._norm_lbl` {#fn--norm-lbl-5499}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:5499`

**Signature**

```python
def _norm_lbl(x: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `x` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _norm_lbl(x: str) -> str:
            return re.sub(r"\s+", " ", str(x or "").strip().lower())
    ```

### `suppress_structural_choice_label_noise._name_to_label` {#fn--name-to-label-5502}

**Pipeline stage:** `Step 9 -- Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:5502`

**Signature**

```python
def _name_to_label(entries: list[tuple[str, str]]) -> dict[str, str]:
```

**Returns:** `dict[str, str]`

**What it does:** Implements logic in the `Step 9 -- Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 9 -- Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _name_to_label(entries: list[tuple[str, str]]) -> dict[str, str]:
            out: dict[str, str] = {}
            for nm, lb in entries or []:
                nk = _canonical_option_name_token(nm)
                if not nk or nk in out:
                    continue
                out[nk] = _norm_lbl(lb)
            return out
    ```

### `_dedupe_questions_for_compare` {#fn--dedupe-questions-for-compare-5576}

**Pipeline stage:** `Step 10 -- Run pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:5576`

**Signature**

```python
def _dedupe_questions_for_compare(df: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Keep one deterministic row per Q Name for pairwise comparisons.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _dedupe_questions_for_compare(df: pl.DataFrame) -> pl.DataFrame:
        """
        Keep one deterministic row per Q Name for pairwise comparisons.
        Duplicate Q Names are handled separately by structure checks.
        """
        if df.is_empty() or "Q Name" not in df.columns:
            return df
        order_cols = [c for c in ["Q Name", "excel_row"] if c in df.columns]
        base = df.sort(order_cols) if order_cols else df
        return base.unique(subset=["Q Name"], keep="first")
    ```

### `_with_choice_cols` {#fn--with-choice-cols-5940}

**Pipeline stage:** `Step 10 -- Run pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:5940`

**Signature**

```python
def _with_choice_cols(df: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 10 -- Run pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _with_choice_cols(df: pl.DataFrame) -> pl.DataFrame:
        out = df
        if "list_name" not in out.columns:
            out = out.with_columns(pl.lit("").alias("list_name"))
        if "option_name" not in out.columns:
            out = out.with_columns(pl.lit("").alias("option_name"))
        return out
    ```

### `_hdr` {#fn--hdr-6264}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6264`

**Signature**

```python
def _hdr(ws, row, vals):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `vals` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _hdr(ws, row, vals):
        for c, v in enumerate(vals, 1):
            cell = ws.cell(row=row, column=c, value=v)
            cell.fill = FILL_HEADER; cell.font = FONT_HDR
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.row_dimensions[row].height = 18
    ```

### `_sect` {#fn--sect-6271}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6271`

**Signature**

```python
def _sect(ws, row, title, n):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `title` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `n` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _sect(ws, row, title, n):
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=n)
        c = ws.cell(row=row, column=1, value=title)
        c.fill = FILL_SECT; c.font = FONT_SECT
        c.alignment = Alignment(horizontal="left", vertical="center")
        ws.row_dimensions[row].height = 20
    ```

### `_style_row` {#fn--style-row-6278}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6278`

**Signature**

```python
def _style_row(ws, row, n, severity=''):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `n` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `severity` | positional_or_keyword | No | `''` | `-` | Severity label used for final issue classification. |

??? note "Function source"

    ```python
    def _style_row(ws, row, n, severity=""):
        fill = SEV_FILL.get(severity)
        for c in range(1, n + 1):
            cell = ws.cell(row=row, column=c)
            cell.font = FONT_NORM; cell.border = THIN_BORDER
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            if fill: cell.fill = fill
    ```

### `_autofit` {#fn--autofit-6286}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6286`

**Signature**

```python
def _autofit(ws, mn=12, mx=60):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `mn` | positional_or_keyword | No | `12` | `-` | Input used by the `Step 11 -- Export` stage. |
| `mx` | positional_or_keyword | No | `60` | `-` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _autofit(ws, mn=12, mx=60):
        for col_cells in ws.columns:
            w = max((len(str(c.value)) if c.value else 0) for c in col_cells)
            ws.column_dimensions[get_column_letter(col_cells[0].column)].width = min(max(w+2, mn), mx)
    ```

### `_ensure_column_widths_from_header` {#fn--ensure-column-widths-from-header-6292}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6292`

**Signature**

```python
def _ensure_column_widths_from_header(ws, header_row: int, min_widths: dict[str, float]):
```

**Returns:** `None or implicit return`

**What it does:** Widen specific report columns after autofit when their content is intentionally verbose.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `header_row` | positional_or_keyword | Yes | `-` | `int` | Input used by the `Step 11 -- Export` stage. |
| `min_widths` | positional_or_keyword | Yes | `-` | `dict[str, float]` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _ensure_column_widths_from_header(ws, header_row: int, min_widths: dict[str, float]):
        """Widen specific report columns after autofit when their content is intentionally verbose."""
        if not min_widths:
            return
        for cell in ws[header_row]:
            header = str(cell.value or "").strip()
            target_width = min_widths.get(header)
            if target_width is None:
                continue
            col_letter = get_column_letter(cell.column)
            current_width = ws.column_dimensions[col_letter].width or 0
            ws.column_dimensions[col_letter].width = max(current_width, target_width)
    ```

### `_action_for_issue_type` {#fn--action-for-issue-type-6368}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6368`

**Signature**

```python
def _action_for_issue_type(issue_type: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `issue_type` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _action_for_issue_type(issue_type: str) -> str:
        key = str(issue_type or "").strip()
        if key.startswith("additional_information_replacement_change"):
            return "Review replacement-driven text change (Additional info / crop / AGOL)"
        return ISSUE_ACTION_MAP.get(key, "Review issue details")
    ```

### `_col_map_with_field_header` {#fn--col-map-with-field-header-6400}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6400`

**Signature**

```python
def _col_map_with_field_header(field_header: str) -> list[tuple[str, str]]:
```

**Returns:** `list[tuple[str, str]]`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `field_header` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _col_map_with_field_header(field_header: str) -> list[tuple[str, str]]:
        return [(src, field_header if src == "field" else disp) for src, disp in COL_MAP]
    ```

### `_prepare_table_df` {#fn--prepare-table-df-6412}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6412`

**Signature**

```python
def _prepare_table_df(df: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _prepare_table_df(df: pl.DataFrame) -> pl.DataFrame:
        if "issue_type" in df.columns and "action" not in df.columns:
            return df.with_columns(
                pl.col("issue_type")
                .map_elements(_action_for_issue_type, return_dtype=pl.Utf8)
                .alias("action")
            )
        return df
    ```

### `_resolve_table_cols` {#fn--resolve-table-cols-6422}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6422`

**Signature**

```python
def _resolve_table_cols(df: pl.DataFrame, col_map=None) -> list[tuple[str, str]]:
```

**Returns:** `list[tuple[str, str]]`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `col_map` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _resolve_table_cols(df: pl.DataFrame, col_map=None) -> list[tuple[str, str]]:
        cmap = col_map or COL_MAP
        cols = []
        for s, d in cmap:
            if s not in df.columns:
                continue
            if s == "lang_scope" and df.height > 0:
                has_vals = (
                    df.select(
                        (
                            pl.col(s).cast(pl.Utf8).fill_null("").str.strip_chars() != ""
                        ).any().alias("_has")
                    )
                    .item()
                )
                if not has_vals:
                    continue
            if s in {"current_lang", "reference_lang"} and df.height > 0:
                has_vals = (
                    df.select(
                        (
                            pl.col(s).cast(pl.Utf8).fill_null("").str.strip_chars() != ""
                        ).any().alias("_has")
                    )
                    .item()
                )
                if not has_vals:
                    continue
            cols.append((s, d))
        return cols
    ```

### `_table` {#fn--table-6454}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6454`

**Signature**

```python
def _table(ws, start_row, df, apply_view=True, col_map=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `start_row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `df` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `apply_view` | positional_or_keyword | No | `True` | `-` | Input used by the `Step 11 -- Export` stage. |
| `col_map` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _table(ws, start_row, df, apply_view=True, col_map=None):
        df = _prepare_table_df(df)
        cols = _resolve_table_cols(df, col_map=col_map)
        qname_col = next((i for i, (src, _) in enumerate(cols, start=1) if src == "Q Name"), None)
        _hdr(ws, start_row, [d for _, d in cols])
        r = start_row + 1
        if df.height == 0:
            ws.cell(row=r, column=1, value="No issues in this category").font = Font(bold=True, color="274E13", size=10)
            return r + 2
        for rd in df.to_dicts():
            for c, (src, _) in enumerate(cols, 1):
                ws.cell(row=r, column=c, value=rd.get(src))
            _style_row(ws, r, len(cols), rd.get("severity", ""))
            if qname_col:
                ws.cell(row=r, column=qname_col).font = Font(bold=True, size=10)
            r += 1
        if apply_view:
            ws.freeze_panes = f"A{start_row+1}"
            ws.auto_filter.ref = f"A{start_row}:{get_column_letter(len(cols))}{start_row}"
        return r + 1
    ```

### `_tokenize_for_word_diff` {#fn--tokenize-for-word-diff-6476}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6476`

**Signature**

```python
def _tokenize_for_word_diff(text: str):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _tokenize_for_word_diff(text: str):
        # Tokenize into non-space chunks and attach following spaces to the same token.
        # This reduces rich-text run fragmentation and avoids visual space-loss artifacts.
        raw = re.findall(r"\s+|\S+", text)
        out = []
        for tok in raw:
            if tok.isspace() and out:
                out[-1] = out[-1] + tok
            else:
                out.append(tok)
        return out
    ```

### `_coalesce_segments` {#fn--coalesce-segments-6489}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6489`

**Signature**

```python
def _coalesce_segments(parts):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `parts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _coalesce_segments(parts):
        merged = []
        for txt, is_equal in parts:
            if not txt:
                continue
            if merged and merged[-1][1] == is_equal:
                merged[-1] = (merged[-1][0] + txt, is_equal)
            else:
                merged.append((txt, is_equal))
        return merged
    ```

### `_build_diff_segments` {#fn--build-diff-segments-6501}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6501`

**Signature**

```python
def _build_diff_segments(current_text: str, reference_text: str):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 11 -- Export` stage. |
| `reference_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _build_diff_segments(current_text: str, reference_text: str):
        a = _tokenize_for_word_diff(current_text)
        b = _tokenize_for_word_diff(reference_text)
        sm = difflib.SequenceMatcher(a=a, b=b)
        current_parts, reference_parts = [], []
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                current_parts.append(("".join(a[i1:i2]), True))
                reference_parts.append(("".join(b[j1:j2]), True))
            elif tag == "replace":
                current_parts.append(("".join(a[i1:i2]), False))
                reference_parts.append(("".join(b[j1:j2]), False))
            elif tag == "delete":
                current_parts.append(("".join(a[i1:i2]), False))
            elif tag == "insert":
                reference_parts.append(("".join(b[j1:j2]), False))
        return _coalesce_segments(current_parts), _coalesce_segments(reference_parts)
    ```

### `_set_rich_text` {#fn--set-rich-text-6520}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6520`

**Signature**

```python
def _set_rich_text(cell, full_text: str, parts):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cell` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `full_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 11 -- Export` stage. |
| `parts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _set_rich_text(cell, full_text: str, parts):
        if not _RICH_TEXT_AVAILABLE:
            cell.value = full_text
            return
        blocks = []
        for txt, is_equal in parts:
            if not txt:
                continue
            color = "FF000000" if is_equal else "FFFF0000"
            blocks.append(TextBlock(InlineFont(color=color), txt))
        if not blocks:
            cell.value = full_text
            return
        cell.value = CellRichText(*blocks)
    ```

### `_set_rich_text_with_bold_tokens` {#fn--set-rich-text-with-bold-tokens-6536}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6536`

**Signature**

```python
def _set_rich_text_with_bold_tokens(cell, full_text: str, tokens: list[str]):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cell` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `full_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 11 -- Export` stage. |
| `tokens` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _set_rich_text_with_bold_tokens(cell, full_text: str, tokens: list[str]):
        if not _RICH_TEXT_AVAILABLE or not full_text:
            cell.value = full_text
            return
        txt = str(full_text)
        lower = txt.lower()
        spans: list[tuple[int, int]] = []
        for tok in tokens or []:
            t = str(tok or "").strip().lower()
            if not t:
                continue
            for m in re.finditer(re.escape(t), lower):
                spans.append((m.start(), m.end()))
        if not spans:
            cell.value = full_text
            return

        spans.sort()
        merged: list[tuple[int, int]] = []
        for s, e in spans:
            if not merged or s > merged[-1][1]:
                merged.append((s, e))
            else:
                merged[-1] = (merged[-1][0], max(merged[-1][1], e))

        blocks = []
        pos = 0
        for s, e in merged:
            if s > pos:
                blocks.append(TextBlock(InlineFont(color="FF000000", b=False), txt[pos:s]))
            blocks.append(TextBlock(InlineFont(color="FF000000", b=True), txt[s:e]))
            pos = e
        if pos < len(txt):
            blocks.append(TextBlock(InlineFont(color="FF000000", b=False), txt[pos:]))

        cell.value = CellRichText(*blocks) if blocks else full_text
    ```

### `_apply_inline_diff_for_issue` {#fn--apply-inline-diff-for-issue-6574}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6574`

**Signature**

```python
def _apply_inline_diff_for_issue(ws, start_row, df, cols, issue_types):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `start_row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `df` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `cols` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `issue_types` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _apply_inline_diff_for_issue(ws, start_row, df, cols, issue_types):
        if df.height == 0:
            return
        cidx = {src: i for i, (src, _) in enumerate(cols, start=1)}
        issue_col = cidx.get("issue_type")
        cur_col = cidx.get("current")
        ref_col = cidx.get("reference")
        cur_lang_col = cidx.get("current_lang")
        ref_lang_col = cidx.get("reference_lang")
        if not issue_col or not cur_col or not ref_col:
            return

        _allowed = set(issue_types or [])

        def _match_issue(issue_val: str) -> bool:
            for allowed in _allowed:
                if isinstance(allowed, str) and allowed.endswith("*"):
                    if issue_val.startswith(allowed[:-1]):
                        return True
                elif issue_val == allowed:
                    return True
            return False

        for offset, rd in enumerate(df.to_dicts(), start=1):
            _issue_val = str(rd.get("issue_type") or "")
            if not _match_issue(_issue_val):
                continue
            cur_txt = str(rd.get("current") or "")
            ref_txt = str(rd.get("reference") or "")
            cur_parts, ref_parts = _build_diff_segments(cur_txt, ref_txt)
            _set_rich_text(ws.cell(row=start_row + offset, column=cur_col), cur_txt, cur_parts)
            _set_rich_text(ws.cell(row=start_row + offset, column=ref_col), ref_txt, ref_parts)
            if cur_lang_col and ref_lang_col:
                cur_lang_txt = str(rd.get("current_lang") or "")
                ref_lang_txt = str(rd.get("reference_lang") or "")
                if cur_lang_txt or ref_lang_txt:
                    cur_lang_parts, ref_lang_parts = _build_diff_segments(cur_lang_txt, ref_lang_txt)
                    _set_rich_text(ws.cell(row=start_row + offset, column=cur_lang_col), cur_lang_txt, cur_lang_parts)
                    _set_rich_text(ws.cell(row=start_row + offset, column=ref_lang_col), ref_lang_txt, ref_lang_parts)
    ```

### `_apply_inline_diff_for_issue._match_issue` {#fn--match-issue-6588}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6588`

**Signature**

```python
def _match_issue(issue_val: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `issue_val` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _match_issue(issue_val: str) -> bool:
            for allowed in _allowed:
                if isinstance(allowed, str) and allowed.endswith("*"):
                    if issue_val.startswith(allowed[:-1]):
                        return True
                elif issue_val == allowed:
                    return True
            return False
    ```

### `_apply_choice_detail_highlights` {#fn--apply-choice-detail-highlights-6615}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6615`

**Signature**

```python
def _apply_choice_detail_highlights(ws, start_row, df, cols):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `start_row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `df` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `cols` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _apply_choice_detail_highlights(ws, start_row, df, cols):
        if df.height == 0:
            return
        cidx = {src: i for i, (src, _) in enumerate(cols, start=1)}
        issue_col = cidx.get("issue_type")
        detail_col = cidx.get("field")
        if not issue_col or not detail_col:
            return

        prefixes = {
            "removed_option_causes_index_drift": "removed option(s) causing drift: ",
            "added_option_causes_index_drift": "added option(s) causing drift: ",
        }
        bold_tokens_map = {
            "added_choice": ["added"],
            "removed_choice": ["removed"],
            "choice_changes_general": ["both added and removed", "added", "removed"],
        }

        for offset, rd in enumerate(df.to_dicts(), start=1):
            issue_val = str(rd.get("issue_type") or "")
            detail_txt = str(rd.get("field") or "")
            if not detail_txt:
                continue

            _bold_tokens = bold_tokens_map.get(issue_val)
            if _bold_tokens:
                _set_rich_text_with_bold_tokens(
                    ws.cell(row=start_row + offset, column=detail_col),
                    detail_txt,
                    _bold_tokens,
                )
                continue

            prefix = prefixes.get(issue_val)
            if not prefix:
                continue

            lower_txt = detail_txt.lower()
            lower_prefix = prefix.lower()
            if not lower_txt.startswith(lower_prefix):
                continue

            head = detail_txt[:len(prefix)]
            tail = detail_txt[len(prefix):]
            _set_rich_text(
                ws.cell(row=start_row + offset, column=detail_col),
                detail_txt,
                [(head, True), (tail, False)],
            )
    ```

### `_with_lang_scope_tag` {#fn--with-lang-scope-tag-6667}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6667`

**Signature**

```python
def _with_lang_scope_tag(df: pl.DataFrame, target_lang_label: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Adds a compact per-row language scope tag for dual-language option comparisons:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `target_lang_label` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _with_lang_scope_tag(df: pl.DataFrame, target_lang_label: str) -> pl.DataFrame:
        """
        Adds a compact per-row language scope tag for dual-language option comparisons:
          - EN only
          - <LANG> only
          - EN + <LANG>
        """
        if "lang_scope" in df.columns:
            return df
        if df.height == 0:
            return df.with_columns(pl.lit("").alias("lang_scope"))
        if not {"current", "reference", "current_lang", "reference_lang"}.issubset(set(df.columns)):
            return df.with_columns(pl.lit("").alias("lang_scope"))

        _tgt = (str(target_lang_label or "").upper().strip() or "LANG")
        _cur = pl.col("current").cast(pl.Utf8).fill_null("").str.strip_chars()
        _ref = pl.col("reference").cast(pl.Utf8).fill_null("").str.strip_chars()
        _cur_t = pl.col("current_lang").cast(pl.Utf8).fill_null("").str.strip_chars()
        _ref_t = pl.col("reference_lang").cast(pl.Utf8).fill_null("").str.strip_chars()

        _en_has = (_cur != "") | (_ref != "")
        _en_diff = _en_has & (_cur != _ref)
        _t_has = (_cur_t != "") | (_ref_t != "")
        _t_diff = _t_has & (_cur_t != _ref_t)

        return df.with_columns(
            pl.when(_en_diff & _t_diff).then(pl.lit(f"EN + {_tgt}"))
            .when(_en_diff & ~_t_diff & _t_has).then(pl.lit("EN only"))
            .when(_t_diff & ~_en_diff).then(pl.lit(f"{_tgt} only"))
            .otherwise(pl.lit(""))
            .alias("lang_scope")
        )
    ```

### `_question_change_expr` {#fn--question-change-expr-6741}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6741`

**Signature**

```python
def _question_change_expr():
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

No parameters.

??? note "Function source"

    ```python
    def _question_change_expr():
        return pl.col("issue_type").is_in(list(QUESTION_CHANGE_TYPES))
    ```

### `_ensure_question_field_detail` {#fn--ensure-question-field-detail-6745}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6745`

**Signature**

```python
def _ensure_question_field_detail(df: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Preserve actionable row-level column context for Question Changes.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _ensure_question_field_detail(df: pl.DataFrame) -> pl.DataFrame:
        """
        Preserve actionable row-level column context for Question Changes.
        If field is blank after transforms, backfill from issue_type.
        """
        if df.height == 0:
            return df

        if "field" not in df.columns:
            return df.with_columns(pl.lit("").alias("field"))

        fallback_field = (
            pl.when(pl.col("issue_type") == "added_question").then(pl.lit("Q Name"))
            .when(pl.col("issue_type") == "removed_question").then(pl.lit("Q Name"))
            .when(pl.col("issue_type") == "mandatory_to_optional").then(pl.lit("Q Name"))
            .when(pl.col("issue_type") == "mandatory_column_mismatch").then(pl.lit("mandatory_category"))
            .when(pl.col("issue_type") == "label_mismatch").then(pl.lit("label"))
            .when(pl.col("issue_type") == "choices_list_changed").then(pl.lit("type (list_name)"))
            .when(pl.col("issue_type") == "required_modified").then(pl.lit("required"))
            .when(pl.col("issue_type") == "choice_filter_modified").then(pl.lit("choice_filter"))
            .when(pl.col("issue_type") == "appearance_modified").then(pl.lit("appearance"))
            .when(pl.col("issue_type") == "calculation_modified").then(pl.lit("calculation"))
            .when(pl.col("issue_type") == "constraint_modified").then(pl.lit("constraint"))
            .when(pl.col("issue_type") == "constraint_removed_mandatory").then(pl.lit("constraint"))
            .when(pl.col("issue_type") == "hint_changed").then(pl.lit("hint"))
            .otherwise(pl.lit(""))
        )

        field_txt = pl.col("field").cast(pl.Utf8).fill_null("").str.strip_chars()
        return df.with_columns(
            pl.when(field_txt == "").then(fallback_field).otherwise(pl.col("field").cast(pl.Utf8)).alias("field")
        )
    ```

### `_normalise_qtype_for_summary` {#fn--normalise-qtype-for-summary-6779}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6779`

**Signature**

```python
def _normalise_qtype_for_summary(df):
```

**Returns:** `None or implicit return`

**What it does:** Fill missing/blank mandatory_cat for summary tables.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _normalise_qtype_for_summary(df):
        """Fill missing/blank mandatory_cat for summary tables.

        Rule:
          - keep valid mandatory_cat values as-is
          - if blank and Q Name starts with o_ -> optional
          - otherwise -> non-mandatory
        """
        if df.height == 0:
            return df
        if "mandatory_cat" not in df.columns:
            return df.with_columns(pl.lit("non-mandatory").alias("mandatory_cat"))

        _valid = ["mandatory", "mandatory-panel", "non-mandatory", "optional"]
        _mand = pl.col("mandatory_cat").cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase()
        _qnm = (
            pl.when(pl.col("Q Name").is_null()).then(pl.lit(""))
            .otherwise(pl.col("Q Name").cast(pl.Utf8))
            .str.strip_chars()
            .str.to_lowercase()
        )
        return df.with_columns(
            pl.when(_mand.is_in(_valid)).then(_mand)
            .when(_qnm.str.contains(_CUSTOM_QNAME_RE)).then(pl.lit("optional"))
            .otherwise(pl.lit("non-mandatory"))
            .alias("mandatory_cat")
        )
    ```

### `_grouped_table` {#fn--grouped-table-6808}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6808`

**Signature**

```python
def _grouped_table(ws, r, df):
```

**Returns:** `None or implicit return`

**What it does:** Render (issue_type, mandatory_cat, severity) -> count grouped summary table.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `r` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `df` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _grouped_table(ws, r, df):
        """Render (issue_type, mandatory_cat, severity) -> count grouped summary table."""
        _hdr(ws, r, ["Issue type", "Q type", "Count", "Severity"]); r += 1
        if df.height == 0:
            ws.cell(row=r, column=1, value="No issues").font = Font(bold=True, color="274E13", size=10)
            return r + 2

        df = _normalise_qtype_for_summary(df)

        grouped = (
            df
            .group_by(["issue_type", "mandatory_cat", "severity"])
            .agg(pl.len().alias("count"))
            .with_columns(
                pl.when(pl.col("severity") == "high").then(pl.lit(0))
                .when(pl.col("severity") == "medium").then(pl.lit(1))
                .otherwise(pl.lit(2))
                .alias("_s"),
                pl.when(pl.col("mandatory_cat") == "mandatory").then(pl.lit(0))
                .when(pl.col("mandatory_cat") == "mandatory-panel").then(pl.lit(1))
                .when(pl.col("mandatory_cat") == "non-mandatory").then(pl.lit(2))
                .when(pl.col("mandatory_cat") == "optional").then(pl.lit(3))
                .otherwise(pl.lit(4))
                .alias("_q")
            )
            .sort(["_s", "issue_type", "_q"])
            .drop(["_s", "_q"])
        )
        for rd in grouped.to_dicts():
            ws.cell(row=r, column=1, value=_ISSUE_LABELS.get(rd["issue_type"], rd["issue_type"]))
            ws.cell(row=r, column=2, value=rd["mandatory_cat"] or "")
            ws.cell(row=r, column=3, value=rd["count"])
            ws.cell(row=r, column=4, value=rd["severity"])
            _style_row(ws, r, 4, rd["severity"])
            r += 1
        return r + 1
    ```

### `write_summary_sheet` {#fn-write-summary-sheet-6846}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6846`

**Signature**

```python
def write_summary_sheet(wb, all_issues, rules=None, critical_issues=None, count_issues=None, found_info=None, replacement_status=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `rules` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 11 -- Export` stage. |
| `critical_issues` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 11 -- Export` stage. |
| `count_issues` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 11 -- Export` stage. |
| `found_info` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 11 -- Export` stage. |
| `replacement_status` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def write_summary_sheet(wb, all_issues, rules=None, critical_issues=None,
                            count_issues=None, found_info=None, replacement_status=None):
        ws = wb.create_sheet("Summary")
        ws.sheet_view.showGridLines = False
        for col, w in zip("ABCD", [38, 20, 42, 12]):
            ws.column_dimensions[col].width = w

        # Title
        ws.merge_cells("A1:D1")
        ws["A1"] = "KoBO Questionnaire Validation Report"
        ws["A1"].font = FONT_TITLE
        ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
        ws.row_dimensions[1].height = 26

        _curr_name = Path(run.get("questionnaire_path", "")).name
        _curr_iso = str(run.get("iso3", "") or "").upper()
        _curr_round = _extract_round_token_kobo(_curr_name) or "R?"
        _tpl_name = Path(run.get("template_path", "")).name if run.get("template_path") else "N/A"
        _summary_info_lines = [
            f"Comparison basis: {_reference_scope_label()}",
            f"Current questionnaire: {_curr_iso} {_curr_round} | {_curr_name}",
            f"Checked against: {_reference_descriptor_kobo()}",
            f"Language scope: {_language_scope_descriptor_kobo()}",
            f"Template used for placeholder mapping: {_tpl_name}",
        ]

        _mod_ignore_line = str(globals().get("_module_ignore_scope_summary") or "").strip()
        _mod_skip_line = str(globals().get("_module_skip_scope_summary") or "").strip()
        _mod_ignore_unres = str(globals().get("_module_ignore_unresolved_summary") or "").strip()
        _mod_skip_unres = str(globals().get("_module_skip_unresolved_summary") or "").strip()
        if _mod_ignore_line and _mod_ignore_line != "(none)":
            _summary_info_lines.append(f"Modules ignored from comparison: {_mod_ignore_line}")
        if _mod_skip_line and _mod_skip_line != "(none)":
            _summary_info_lines.append(f"Modules skipped from validated output: {_mod_skip_line}")
        if _mod_ignore_unres:
            _summary_info_lines.append(f"Unresolved ignored-module entries: {_mod_ignore_unres}")
        if _mod_skip_unres:
            _summary_info_lines.append(f"Unresolved skipped-module entries: {_mod_skip_unres}")

        for _i, _line in enumerate(_summary_info_lines, start=2):
            ws.merge_cells(f"A{_i}:D{_i}")
            ws[f"A{_i}"] = _line
            ws[f"A{_i}"].font = Font(
                size=10,
                color="274E13" if _i == 2 else "1F4E78",
                italic=True,
            )
            ws[f"A{_i}"].alignment = Alignment(horizontal="left", vertical="center")

        r = len(_summary_info_lines) + 2
        _rules = rules or {}
        _crit  = (critical_issues if critical_issues is not None
                  else pl.DataFrame(schema={"set_name": pl.Utf8, "issue_type": pl.Utf8, "Q Name": pl.Utf8}))
        _cnt   = (count_issues if count_issues is not None
                  else pl.DataFrame(schema={"set_name": pl.Utf8, "issue_type": pl.Utf8}))
        _found = found_info or {}

        # -- Critical Sets Status -------------------------------------------------
        _sect(ws, r, "CRITICAL SETS STATUS", 4); r += 1
        _hdr(ws, r, ["Critical set", "Status", "Details", ""]); r += 1

        def _set_row(ws, r, name, passed, details):
            ws.cell(row=r, column=1, value=name)
            ws.cell(row=r, column=2, value="PASS" if passed else "FAIL")
            ws.cell(row=r, column=3, value=details)
            _style_row(ws, r, 4, "pass" if passed else "high")
            ws.cell(row=r, column=2).font = Font(bold=True, size=10,
                                                  color="274E13" if passed else "CC0000")

        _EXACT_FAIL_TYPES = ["missing_critical_question", "critical_mandatory_mismatch"]
        for set_name, set_rules in _rules.get("exact_sets", {}).items():
            required_qs = [r.get("q_name", "") for r in set_rules if r.get("required", True)]
            advisory_qs = [r.get("q_name", "") for r in set_rules if not r.get("required", True)]
            found_exact = set(_found.get(set_name, []))
            missing_required = [q for q in required_qs if q and q not in found_exact]

            set_fail = all_issues.filter(
                (pl.col("set_name") == set_name) & pl.col("issue_type").is_in(_EXACT_FAIL_TYPES)
            )
            set_warn = all_issues.filter(
                (pl.col("set_name") == set_name) & (pl.col("issue_type") == "advisory_question")
            )

            # Fallback to rule-based presence check so status stays correct
            # even if issue tagging is affected by execution order.
            passed = (set_fail.height == 0) and (len(missing_required) == 0)

            if passed and set_warn.height == 0:
                details = "All required questions present"
            elif passed:
                warn_qs = [q for q in advisory_qs if q and q not in found_exact]
                if not warn_qs:
                    warn_qs = [q for q in set_warn["Q Name"].to_list() if q]
                details = (f"Required OK  (advisory missing: {', '.join(warn_qs)})"
                           if warn_qs else "All required questions present")
            else:
                missing = list(dict.fromkeys(missing_required + [q for q in set_fail["Q Name"].to_list() if q]))
                details = f"Missing: {', '.join(missing)}" if missing else "Issues found"
            _set_row(ws, r, set_name, passed, details); r += 1
        for set_name, rule in _rules.get("min_count_sets", {}).items():
            min_count = rule.get("min_count", 1)
            prefix    = rule.get("prefix", "")
            found_qs  = _found.get(set_name, [])
            failed    = _cnt.filter(pl.col("set_name") == set_name).height > 0
            if not failed:
                details = f">={min_count} {prefix}* confirmed  ({len(found_qs)} found)"
            else:
                details = f"{len(found_qs)} found -- need >={min_count} {prefix}* questions"
            _set_row(ws, r, set_name, not failed, details); r += 1

        # Crop harvest row
        if _rules.get("crop_harvest"):
            _harv_fail = all_issues.filter(pl.col("issue_type") == "crop_harvest_violation").height > 0
            _harv_det = ("Partial crop-harvest set -- see issues" if _harv_fail
                         else "Crop harvest rule satisfied")
            _set_row(ws, r, "CRP_HARV", not _harv_fail, _harv_det); r += 1

        # Rule-based sets shared with GeoPoll (fs_indicators, agri_cs_check, ...)
        _rule_rows = [
            ("fs_indicators", "FS_INDICATORS", "FIES / FCS / LCSI present"
             + (" (CAPI ceiling respected)" if _cfg_modality == "capi" else "")),
            ("agri_cs_check", "AGRI_CS", "Enough agriculture-related coping strategies"),
            ("variable_pairs", "VAR_PAIRS", "All variable pairs complete"),
            ("fixed_option_codes", "FIXED_CODES", "Fixed answer codes intact"),
            ("tlu_weights", "TLU", "TLU weights filled and consistent"),
        ]
        for _key, _set, _ok_det in _rule_rows:
            if not _rules.get(_key):
                continue
            _n = all_issues.filter(pl.col("set_name") == _set).height
            _set_row(ws, r, _set, _n == 0, _ok_det if _n == 0 else f"{_n} issue(s) -- see Critical Sets"); r += 1

        if not _rules.get("exact_sets") and not _rules.get("min_count_sets"):
            ws.cell(row=r, column=1, value="No critical sets defined")
            _style_row(ws, r, 4, "info"); r += 1

        r += 1

        # -- Questionnaire Structure Checks --------------------------------------
        _sect(ws, r, "QUESTIONNAIRE STRUCTURE CHECKS", 4); r += 1
        _hdr(ws, r, ["Check", "Status", "Details", ""]); r += 1

        def _check_row(ws, r, name, passed, details):
            ws.cell(row=r, column=1, value=name)
            ws.cell(row=r, column=2, value="PASS" if passed else "FAIL")
            ws.cell(row=r, column=3, value=details)
            _style_row(ws, r, 4, "pass" if passed else "high")
            ws.cell(row=r, column=2).font = Font(bold=True, size=10,
                                                  color="274E13" if passed else "CC0000")

        _broken   = all_issues.filter(pl.col("issue_type").is_in(["broken_relevant_reference", "relevant_inexact_reference"])).height
        _modified = all_issues.filter(pl.col("issue_type") == "relevant_modified").height
        skip_ok = _broken == 0
        skip_det = (f"{_broken} broken reference(s); {_modified} modified" if not skip_ok
                    else f"No broken references  ({_modified} modified)")
        _check_row(ws, r, "Skip logic references (relevant)", skip_ok, skip_det); r += 1

        _struct_df   = all_issues.filter(pl.col("issue_type").is_in(list(STRUCTURE_ISSUE_TYPES)))
        _struct_all  = _struct_df.height
        _dup_q       = _struct_df.filter(pl.col("issue_type") == "duplicate_qname").height
        _dup_choice  = _struct_df.filter(pl.col("issue_type") == "duplicate_choice_name").height
        _qtype       = _struct_df.filter(pl.col("issue_type") == "type_changed").height
        _module_removed = _struct_df.filter(pl.col("issue_type") == "module_removed").height
        _module_added = _struct_df.filter(pl.col("issue_type") == "module_added").height
        _base_struct_df = _struct_df.filter(~pl.col("issue_type").is_in(["module_removed", "module_added"]))
        _base_struct_all = _base_struct_df.height
        _other_struct = _base_struct_all - _dup_q - _dup_choice - _qtype
        _struct_ok   = _base_struct_all == 0
        _struct_det  = (
            f"{_base_struct_all} issue(s): Q type integrity={_qtype}; duplicate Q Name={_dup_q}; "
            f"duplicate choice name={_dup_choice}; other structure checks={_other_struct}"
            if not _struct_ok else
            "No issues in Q type integrity, duplicates, or other structure checks"
        )
        _check_row(ws, r, "Q type integrity, duplicates and KoBo references", _struct_ok, _struct_det); r += 1
        _module_ok = _module_removed == 0
        _module_det = (
            f"template modules missing={_module_removed}; modules added={_module_added}"
            if not _module_ok else
            f"No template module missing (modules added={_module_added})"
        )
        _check_row(ws, r, "Module presence (template-required)", _module_ok, _module_det); r += 1

        _mand_typo_n = all_issues.filter(pl.col("issue_type") == "mandatory_category_unrecognized").height
        _mand_typo_ok = _mand_typo_n == 0
        _mand_typo_det = (
            f"{_mand_typo_n} unrecognized Mandatory value(s)" if not _mand_typo_ok
            else "All Mandatory values match a known category"
        )
        _check_row(ws, r, "Mandatory category values", _mand_typo_ok, _mand_typo_det); r += 1

        r += 1

        # -- Replacement Status ---------------------------------------------------
        _sect(ws, r, "REPLACEMENT STATUS  (validated questionnaire output)", 4); r += 1
        _hdr(ws, r, ["Check", "Status", "Details", ""]); r += 1

        _repl_rows = (replacement_status or {}).get("rows", [])
        if not _repl_rows:
            ws.cell(row=r, column=1, value="Validated questionnaire step not run yet")
            ws.cell(row=r, column=2, value="INFO")
            ws.cell(row=r, column=3, value="Run Step 12, then rerun export to include replacement checks.")
            _style_row(ws, r, 4, "info"); r += 1
        else:
            for rd in _repl_rows:
                sev = rd.get("severity", "info")
                st  = rd.get("status", "INFO")
                ws.cell(row=r, column=1, value=rd.get("check", ""))
                ws.cell(row=r, column=2, value=st)
                ws.cell(row=r, column=3, value=rd.get("details", ""))
                _style_row(ws, r, 4, sev)
                if st == "PASS":
                    ws.cell(row=r, column=2).font = Font(bold=True, size=10, color="274E13")
                elif st == "WARN":
                    ws.cell(row=r, column=2).font = Font(bold=True, size=10, color="B45F06")
                elif st == "SKIP":
                    ws.cell(row=r, column=2).font = Font(bold=True, size=10, color="1F4E78")
                else:
                    ws.cell(row=r, column=2).font = Font(bold=True, size=10, color="CC0000")
                r += 1

        _repl_notes = (replacement_status or {}).get("notes", [])
        if _repl_notes:
            r += 1
            _sect(ws, r, "VALIDATED OUTPUT UPDATE NOTES", 4); r += 1
            _hdr(ws, r, ["Note", "", "", ""]); r += 1
            for note in _repl_notes:
                ws.cell(row=r, column=1, value=note)
                _style_row(ws, r, 4, "info")
                r += 1

        r += 1

        # -- Question Changes (Core) ----------------------------------------------
        _question_df = _ensure_question_field_detail(all_issues.filter(_question_change_expr()))

        _sect(ws, r, "QUESTION CHANGES (CORE)", 4); r += 1
        r = _grouped_table(
            ws,
            r,
            _question_df.filter(pl.col("issue_type").is_in(list(CORE_QUESTION_CHANGE_ISSUE_TYPES))),
        )
        r += 1

        # -- Question Changes (Additional fields) ---------------------------------
        _sect(ws, r, "QUESTION CHANGES (ADDITIONAL FIELDS)", 4); r += 1
        r = _grouped_table(
            ws,
            r,
            _question_df.filter(pl.col("issue_type").is_in(list(ADDITIONAL_QUESTION_FIELD_ISSUE_TYPES))),
        )
        r += 1

        # -- Choice Changes -------------------------------------------------------
        _sect(ws, r, "CHOICE CHANGES  (questions present in both files)", 4); r += 1
        r = _grouped_table(ws, r,
                           all_issues.filter(pl.col("issue_type").is_in(
                               ["removed_choice", "added_choice", "choice_changes_general", "choice_label_mismatch", "option_index_drift", "option_name_dictionary_replaced", "removed_option_causes_index_drift", "added_option_causes_index_drift", "mandatory_choice_set_replaced", "cluster_ea_choice_changes_summary", "enumerator_choice_changes_summary"])))
    ```

### `write_summary_sheet._set_row` {#fn--set-row-6907}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6907`

**Signature**

```python
def _set_row(ws, r, name, passed, details):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `r` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `name` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `passed` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `details` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _set_row(ws, r, name, passed, details):
            ws.cell(row=r, column=1, value=name)
            ws.cell(row=r, column=2, value="PASS" if passed else "FAIL")
            ws.cell(row=r, column=3, value=details)
            _style_row(ws, r, 4, "pass" if passed else "high")
            ws.cell(row=r, column=2).font = Font(bold=True, size=10,
                                                  color="274E13" if passed else "CC0000")
    ```

### `write_summary_sheet._check_row` {#fn--check-row-6988}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:6988`

**Signature**

```python
def _check_row(ws, r, name, passed, details):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `r` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `name` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `passed` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |
| `details` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def _check_row(ws, r, name, passed, details):
            ws.cell(row=r, column=1, value=name)
            ws.cell(row=r, column=2, value="PASS" if passed else "FAIL")
            ws.cell(row=r, column=3, value=details)
            _style_row(ws, r, 4, "pass" if passed else "high")
            ws.cell(row=r, column=2).font = Font(bold=True, size=10,
                                                  color="274E13" if passed else "CC0000")
    ```

### `write_critical_sets_sheet` {#fn-write-critical-sets-sheet-7106}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7106`

**Signature**

```python
def write_critical_sets_sheet(wb, all_issues, found_info=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `found_info` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def write_critical_sets_sheet(wb, all_issues, found_info=None):
        ws = wb.create_sheet("Critical Sets")
        ws.sheet_view.showGridLines = False

        df = all_issues.filter(
            pl.col("issue_type").is_in(list(CRITICAL_ISSUE_TYPES))
        ).sort(["set_name", "severity", "Q Name"])
        _sect(ws, 1, "CRITICAL SETS  Structural validation issues", 8)
        next_row = _table(ws, 2, df, apply_view=False, col_map=_COL_MAP_FIELD)

        if found_info:
            next_row += 1
            _sect(ws, next_row, "QUESTIONS FOUND IN CURRENT QUESTIONNAIRE", 3)
            next_row += 1
            _hdr(ws, next_row, ["Set", "Count found", "Questions"])
            next_row += 1
            for set_name, questions in found_info.items():
                ws.cell(row=next_row, column=1, value=set_name)
                ws.cell(row=next_row, column=2, value=len(questions))
                ws.cell(row=next_row, column=3, value=", ".join(questions) if questions else "none found")
                _style_row(ws, next_row, 3, "info" if questions else "high")
                next_row += 1
        ws.freeze_panes = "A1"
        _autofit(ws)
    ```

### `write_questionnaire_structure_sheet` {#fn-write-questionnaire-structure-sheet-7132}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7132`

**Signature**

```python
def write_questionnaire_structure_sheet(wb, all_issues):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def write_questionnaire_structure_sheet(wb, all_issues):
        ws = wb.create_sheet("Questionnaire Structure")
        ws.sheet_view.showGridLines = False
        row = 1
        relevant_widths = {"Current value": 110, "Reference / rule": 110}

        # Box 1: legacy relevant checks
        rel_df = all_issues.filter(
            pl.col("issue_type").is_in(list(RELEVANT_ISSUE_TYPES))
        ).sort(["severity", "Q Name"])
        rel_df_view = _prepare_table_df(rel_df)
        rel_cols = _resolve_table_cols(rel_df_view, col_map=_COL_MAP_STRUCT)
        _sect(ws, row, "QUESTIONNAIRE STRUCTURE CHECKS  Skip logic references (relevant)", 8)
        _rel_start = row + 1
        row = _table(ws, _rel_start, rel_df_view, apply_view=False, col_map=_COL_MAP_STRUCT)
        _apply_inline_diff_for_issue(
            ws,
            _rel_start,
            rel_df_view,
            rel_cols,
            {"relevant_modified"},
        )

        # Box 2: Q Type integrity
        row += 1
        qtype_df = all_issues.filter(
            pl.col("issue_type") == "type_changed"
        ).sort(["severity", "Q Name", "field"])
        _sect(ws, row, "Q TYPE INTEGRITY ISSUES", 8)
        row = _table(ws, row + 1, qtype_df, apply_view=False, col_map=_COL_MAP_STRUCT)

        # Box 3: duplicate/token syntax checks
        row += 1
        struct_df = all_issues.filter(
            pl.col("issue_type").is_in([
                "duplicate_qname", "duplicate_choice_name",
                "choice_missing_bilingual_label",
                "kobo_ref_loose_syntax", "kobo_ref_malformed_syntax", "kobo_ref_missing_variable",
                "module_removed", "module_added",
            ])
        ).sort(["severity", "Q Name", "field"])
        _sect(ws, row, "QUESTIONNAIRE STRUCTURE CHECKS  (Duplicates, KoBO references, modules)", 8)
        row = _table(ws, row + 1, struct_df, apply_view=False, col_map=_COL_MAP_STRUCT)

        # Box 4: authoring consistency checks (current questionnaire only, no reference comparison)
        row += 1
        authoring_df = all_issues.filter(
            pl.col("issue_type").is_in(list(KOBO_AUTHORING_CONSISTENCY_ISSUE_TYPES))
        ).sort(["severity", "Q Name", "field"])
        _sect(ws, row, "AUTHORING CONSISTENCY CHECKS", 8)
        _table(ws, row + 1, authoring_df, apply_view=False, col_map=_COL_MAP_STRUCT)

        # Avoid frozen panes in multi-box sheets (this was causing navigation/display issues).
        ws.freeze_panes = "A1"
        _autofit(ws)
        _ensure_column_widths_from_header(ws, _rel_start, relevant_widths)
    ```

### `write_replacement_issues_sheet` {#fn-write-replacement-issues-sheet-7190}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7190`

**Signature**

```python
def write_replacement_issues_sheet(wb, all_issues):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def write_replacement_issues_sheet(wb, all_issues):
        ws = wb.create_sheet("Replacement Issues")
        ws.sheet_view.showGridLines = False
        df = all_issues.filter(pl.col("issue_type").is_in(list(REPLACEMENT_ISSUE_TYPES))).sort(["severity", "Q Name", "field"])
        df_view = _prepare_table_df(df)
        _sect(ws, 1, "REPLACEMENT ISSUES  Placeholder and Additional information checks", 8)
        next_row = _table(ws, 2, df_view, apply_view=False, col_map=_COL_MAP_STRUCT)

        rp_df = (
            all_issues
            .filter(pl.col("issue_type").cast(pl.Utf8).str.starts_with("additional_information_replacement_change ("))
            .sort(["severity", "issue_type", "Q Name"])
        )
        rp_df_view = _prepare_table_df(rp_df)
        rp_cols = _resolve_table_cols(rp_df_view, col_map=_COL_MAP_STRUCT)
        next_row += 1
        _sect(ws, next_row, "ADDITIONAL INFORMATION REPLACEMENT CHANGES  (previous_round informational)", 8)
        rp_start = next_row + 1
        _table(ws, rp_start, rp_df_view, apply_view=False, col_map=_COL_MAP_STRUCT)
        _apply_inline_diff_for_issue(
            ws,
            rp_start,
            rp_df_view,
            rp_cols,
            {"additional_information_replacement_change*"},
        )

        ws.freeze_panes = "A1"
        _autofit(ws)
    ```

### `write_relevant_sheet` {#fn-write-relevant-sheet-7221}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7221`

**Signature**

```python
def write_relevant_sheet(wb, all_issues):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def write_relevant_sheet(wb, all_issues):
        ws = wb.create_sheet("Relevant Changes")
        ws.sheet_view.showGridLines = False
        df = all_issues.filter(pl.col("issue_type").is_in(list(RELEVANT_ISSUE_TYPES)))
        _sect(ws, 1, "RELEVANT CHANGES  KoBO skip-logic (relevant column)", 8)
        _table(ws, 2, df, col_map=_COL_MAP_FIELD)
        _autofit(ws)
        _ensure_column_widths_from_header(ws, 2, {"Current value": 110, "Reference / rule": 110})
    ```

### `write_question_changes_sheet` {#fn-write-question-changes-sheet-7231}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7231`

**Signature**

```python
def write_question_changes_sheet(wb, all_issues):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def write_question_changes_sheet(wb, all_issues):
        ws = wb.create_sheet("Question Changes")
        ws.sheet_view.showGridLines = False

        df = _ensure_question_field_detail(all_issues.filter(_question_change_expr()))
        if df.height > 0:
            df = (
                df
                .with_columns(
                    pl.when(pl.col("severity") == "high").then(pl.lit(0))
                    .when(pl.col("severity") == "medium").then(pl.lit(1))
                    .otherwise(pl.lit(2))
                    .alias("_s")
                )
                .sort(["_s", "issue_type", "Q Name"])
                .drop("_s")
            )

        core_df = df.filter(pl.col("issue_type").is_in(list(CORE_QUESTION_CHANGE_ISSUE_TYPES)))
        additional_df = df.filter(pl.col("issue_type").is_in(list(ADDITIONAL_QUESTION_FIELD_ISSUE_TYPES)))
        col_map = [c for c in _COL_MAP_FIELD if c[0] not in {"set_name", "list_name", "option_name"}]

        core_view = _prepare_table_df(core_df)
        core_cols = _resolve_table_cols(core_view, col_map=col_map)
        _sect(ws, 1, "QUESTION CHANGES (CORE)  Presence, mandatory, labels", 8)
        next_row = _table(ws, 2, core_view, col_map=col_map, apply_view=False)
        _apply_inline_diff_for_issue(
            ws,
            2,
            core_view,
            core_cols,
            {"label_mismatch", "constraint_removed_mandatory"},
        )

        additional_view = _prepare_table_df(additional_df)
        additional_cols = _resolve_table_cols(additional_view, col_map=col_map)
        _sect(
            ws,
            next_row,
            "QUESTION CHANGES (ADDITIONAL FIELDS)  hint, required, choice_filter, appearance, calculation, constraint, choices list",
            8,
        )
        _table(ws, next_row + 1, additional_view, col_map=col_map, apply_view=False)
        _apply_inline_diff_for_issue(
            ws,
            next_row + 1,
            additional_view,
            additional_cols,
            set(ADDITIONAL_QUESTION_FIELD_ISSUE_TYPES),
        )
        ws.freeze_panes = "A3"
        _autofit(ws)
    ```

### `write_option_changes_sheet` {#fn-write-option-changes-sheet-7285}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7285`

**Signature**

```python
def write_option_changes_sheet(wb, all_issues):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def write_option_changes_sheet(wb, all_issues):
        ws = wb.create_sheet("Choice Changes")
        ws.sheet_view.showGridLines = False
        df = all_issues.filter(pl.col("issue_type").is_in([
            "removed_choice", "added_choice", "choice_changes_general", "choice_label_mismatch", "option_index_drift", "option_name_dictionary_replaced", "removed_option_causes_index_drift", "added_option_causes_index_drift", "mandatory_choice_set_replaced", "cluster_ea_choice_changes_summary", "enumerator_choice_changes_summary",
        ]))
        df = _with_lang_scope_tag(df, _kobo_report_lang)
        col_map = [c for c in _COL_MAP_DETAIL if c[0] != "set_name"]
        df_view = _prepare_table_df(df)
        cols = _resolve_table_cols(df_view, col_map=col_map)
        _sect(ws, 1, "CHOICE CHANGES  Answer choices for questions in both files", 8)
        _table(ws, 2, df_view, col_map=col_map)
        _apply_inline_diff_for_issue(
            ws,
            2,
            df_view,
            cols,
            {"added_choice", "removed_choice", "choice_changes_general", "choice_label_mismatch", "option_index_drift", "option_name_dictionary_replaced", "removed_option_causes_index_drift", "added_option_causes_index_drift", "mandatory_choice_set_replaced"},
        )
        _apply_choice_detail_highlights(ws, 2, df_view, cols)
        _autofit(ws)
    ```

### `export_report` {#fn-export-report-7308}

**Pipeline stage:** `Step 11 -- Export`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7308`

**Signature**

```python
def export_report(all_issues, result_file, found_info=None, rules=None, critical_issues=None, count_issues=None, replacement_status=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 11 -- Export` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `result_file` | positional_or_keyword | Yes | `-` | `-` | Filesystem path used for reading inputs or writing outputs. |
| `found_info` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 11 -- Export` stage. |
| `rules` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 11 -- Export` stage. |
| `critical_issues` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 11 -- Export` stage. |
| `count_issues` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 11 -- Export` stage. |
| `replacement_status` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 11 -- Export` stage. |

??? note "Function source"

    ```python
    def export_report(all_issues, result_file, found_info=None,
                      rules=None, critical_issues=None, count_issues=None,
                      replacement_status=None):
        wb = Workbook()
        wb.remove(wb.active)
        write_summary_sheet(wb, all_issues, rules=rules,
                            critical_issues=critical_issues, count_issues=count_issues,
                            found_info=found_info, replacement_status=replacement_status)
        write_critical_sets_sheet(wb, all_issues, found_info=found_info)
        write_questionnaire_structure_sheet(wb, all_issues)
        write_replacement_issues_sheet(wb, all_issues)
        write_question_changes_sheet(wb, all_issues)
        write_option_changes_sheet(wb, all_issues)
        wb.save(result_file)
        print(f"Report saved: {result_file}")
        print(f"Sheets: {wb.sheetnames}")
    ```

### `_crop_label_idx` {#fn--crop-label-idx-7373}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7373`

**Signature**

```python
def _crop_label_idx(headers: list[str], language: str) -> int | None:
```

**Returns:** `int | None`

**What it does:** Locate Crop list label column index for a language token (EN/FR/AR/...).

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `headers` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _crop_label_idx(headers: list[str], language: str) -> int | None:
        """Locate Crop list label column index for a language token (EN/FR/AR/...)."""
        lu = str(language or "").strip().upper()
        if not lu:
            return None
        for i, h in enumerate(headers):
            hu = str(h or "").strip().upper()
            if "LABEL" not in hu:
                continue
            if f"({lu})" in hu or hu.endswith(f" {lu}") or hu.endswith(lu):
                return i
        return None
    ```

### `_read_crop_choices` {#fn--read-crop-choices-7387}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7387`

**Signature**

```python
def _read_crop_choices(src_path: str, language: str, strict_language: bool=False) -> tuple[dict[str, list[tuple]], dict]:
```

**Returns:** `tuple[dict[str, list[tuple]], dict]`

**What it does:** Read 'Crop list' sheet -> {list_name: [(code, label), ...]} for crop/crop2/crop3.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `src_path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `strict_language` | positional_or_keyword | No | `False` | `bool` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _read_crop_choices(
        src_path: str,
        language: str,
        strict_language: bool = False,
    ) -> tuple[dict[str, list[tuple]], dict]:
        """
        Read 'Crop list' sheet -> {list_name: [(code, label), ...]} for crop/crop2/crop3.
        Also returns crop-selection diagnostics for reporting (expected exactly 10 selected).
        """
        status = {
            "expected_selected": 10,
            "selected_count": 0,
            "candidate_count": 0,
            "status": "FAIL",
            "severity": "high",
            "message": "Crop list sheet not found",
        }

        wb = openpyxl.load_workbook(src_path, data_only=True, read_only=True)
        if "Crop list" not in wb.sheetnames:
            wb.close()
            return {}, status
        rows = list(wb["Crop list"].iter_rows(values_only=True))
        wb.close()

        # Layout: row 1 = title, row 2 = empty/sub-title, row 3 = header  (skiprows=2)
        if len(rows) < 3:
            status["message"] = "Crop list sheet has no crop rows"
            return {}, status

        headers  = [str(h).strip() if h is not None else "" for h in rows[2]]
        sel_idx  = next((i for i, h in enumerate(headers) if "Select top" in h), None)
        code_idx = next((i for i, h in enumerate(headers) if "Dataset code" in h), None)
        req_lbl_idx = _crop_label_idx(headers, language)
        en_lbl_idx = _crop_label_idx(headers, "en")
        lbl_idx = req_lbl_idx if req_lbl_idx is not None else en_lbl_idx

        if code_idx is None or lbl_idx is None:
            status["message"] = "Crop list headers missing Dataset code / language label"
            return {}, status
        if strict_language and req_lbl_idx is None:
            status["message"] = f"Crop list header missing label column for language '{language}'"
            return {}, status

        selected, unselected = [], []
        for row in rows[3:]:
            code = row[code_idx] if code_idx < len(row) else None
            lbl  = row[lbl_idx]  if lbl_idx  < len(row) else None
            sel  = row[sel_idx]  if sel_idx is not None and sel_idx < len(row) else None
            if code is None or str(code).strip() in ("", "nan"):
                continue
            entry = (str(code).strip(), str(lbl or "").strip())
            (selected if sel is not None and str(sel).strip() else unselected).append(entry)

        selected.sort(key=lambda x: x[0])
        unselected.sort(key=lambda x: x[0])
        combined = selected + unselected

        selected_count = len(selected)
        candidate_count = len(combined)
        status["selected_count"] = selected_count
        status["candidate_count"] = candidate_count

        if selected_count == 10:
            status["status"] = "PASS"
            status["severity"] = "pass"
            status["message"] = f"10 crops selected (OK) out of {candidate_count} candidates"
        elif selected_count == 0:
            status["status"] = "FAIL"
            status["severity"] = "high"
            status["message"] = f"No crops selected (0/10) out of {candidate_count} candidates"
        elif selected_count < 10:
            status["status"] = "WARN"
            status["severity"] = "medium"
            status["message"] = f"Only {selected_count}/10 crops selected out of {candidate_count} candidates"
        else:
            status["status"] = "WARN"
            status["severity"] = "medium"
            status["message"] = f"{selected_count}/10 crops selected (more than expected) out of {candidate_count} candidates"

        return ({name: combined + specials for name, specials in _CROP_SPECIALS.items()}, status)
    ```

### `_merge_crop_rows_for_multilang` {#fn--merge-crop-rows-for-multilang-7470}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7470`

**Signature**

```python
def _merge_crop_rows_for_multilang(crop_rows_en: dict[str, list[tuple]], crop_rows_target: dict[str, list[tuple]], target_language: str) -> dict[str, list[tuple]]:
```

**Returns:** `dict[str, list[tuple]]`

**What it does:** Build crop rows as (code, label_en, label_target) per list for writing both label columns.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_rows_en` | positional_or_keyword | Yes | `-` | `dict[str, list[tuple]]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `crop_rows_target` | positional_or_keyword | Yes | `-` | `dict[str, list[tuple]]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `target_language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _merge_crop_rows_for_multilang(
        crop_rows_en: dict[str, list[tuple]],
        crop_rows_target: dict[str, list[tuple]],
        target_language: str,
    ) -> dict[str, list[tuple]]:
        """
        Build crop rows as (code, label_en, label_target) per list for writing both label columns.
        Falls back safely if one language view is missing.
        """
        out: dict[str, list[tuple]] = {}
        tgt_lang = str(target_language or "").strip().lower()
        for ln in _CROP_SPECIALS.keys():
            en_entries = list(crop_rows_en.get(ln, []))
            tgt_entries = list(crop_rows_target.get(ln, []))

            en_by_code: dict[str, str] = {}
            tgt_by_code: dict[str, str] = {}
            first_code_seen: dict[str, str] = {}

            for code, lbl in en_entries:
                key = _normalize_choice_text_token(code)
                if not key:
                    continue
                first_code_seen.setdefault(key, str(code or "").strip())
                en_by_code[key] = str(lbl or "").strip()
            for code, lbl in tgt_entries:
                key = _normalize_choice_text_token(code)
                if not key:
                    continue
                first_code_seen.setdefault(key, str(code or "").strip())
                tgt_by_code[key] = str(lbl or "").strip()

            # Prefer EN ordering when available; otherwise keep target ordering.
            base_entries = en_entries if en_entries else tgt_entries
            merged: list[tuple] = []
            seen: set[str] = set()
            for code, _ in base_entries:
                key = _normalize_choice_text_token(code)
                if not key or key in seen:
                    continue
                code_txt = first_code_seen.get(key, str(code or "").strip())
                en_txt = en_by_code.get(key, "")
                if tgt_lang == "en":
                    tgt_txt = en_txt
                else:
                    tgt_txt = tgt_by_code.get(key, "")
                merged.append((code_txt, en_txt, tgt_txt))
                seen.add(key)

            # Defensive: include codes present in only one language map.
            for key, code_txt in first_code_seen.items():
                if key in seen:
                    continue
                en_txt = en_by_code.get(key, "")
                if tgt_lang == "en":
                    tgt_txt = en_txt
                else:
                    tgt_txt = tgt_by_code.get(key, "")
                merged.append((code_txt, en_txt, tgt_txt))

            out[ln] = merged
        return out
    ```

### `_fetch_admin_choices` {#fn--fetch-admin-choices-7534}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7534`

**Signature**

```python
def _fetch_admin_choices(iso3: str) -> dict[str, list[tuple]]:
```

**Returns:** `dict[str, list[tuple]]`

**What it does:** Fetch adm1 and adm2 from public FAO AGOL REST service (no credentials needed).

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `iso3` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _fetch_admin_choices(iso3: str) -> dict[str, list[tuple]]:
        """
        Fetch adm1 and adm2 from public FAO AGOL REST service (no credentials needed).
        Returns:
          admin1: [(adm1_pcode, adm1_name), ...]
          admin2: [(adm2_pcode, adm2_name, adm1_pcode), ...]  <- adm1_pcode for choice_filter (col 5)
        """
        _BASE = ("https://services5.arcgis.com/sjP4Ugu5s0dZWLjd/arcgis/rest/services"
                 "/Administrative_Boundaries_Reference_(view_layer)/FeatureServer")

        def _get(layer, fields):
            url = (f"{_BASE}/{layer}/query"
                   f"?where=adm0_ISO3+%3D+%27{iso3}%27"
                   f"&outFields={fields}&returnGeometry=false&outSR=4326&f=json")
            with _urlreq.urlopen(url, timeout=30) as r:
                return _json.loads(r.read().decode())["features"]

        adm1 = sorted(
            [(f["attributes"]["adm1_pcode"], f["attributes"]["adm1_name"])
             for f in _get(1, "adm1_name,adm1_pcode")],
            key=lambda x: x[0],
        )
        adm2 = sorted(
            [(f["attributes"]["adm2_pcode"], f["attributes"]["adm2_name"], f["attributes"]["adm1_pcode"])
             for f in _get(0, "adm2_name,adm2_pcode,adm1_pcode")],
            key=lambda x: x[0],
        )
        print(f"  AGOL  adm1: {len(adm1)} rows   adm2: {len(adm2)} rows")
        return {"admin1": adm1, "admin2": adm2}
    ```

### `_fetch_admin_choices._get` {#fn--get-7544}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7544`

**Signature**

```python
def _get(layer, fields):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `layer` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `fields` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _get(layer, fields):
            url = (f"{_BASE}/{layer}/query"
                   f"?where=adm0_ISO3+%3D+%27{iso3}%27"
                   f"&outFields={fields}&returnGeometry=false&outSR=4326&f=json")
            with _urlreq.urlopen(url, timeout=30) as r:
                return _json.loads(r.read().decode())["features"]
    ```

### `_fetch_admin3_choices` {#fn--fetch-admin3-choices-7565}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7565`

**Signature**

```python
def _fetch_admin3_choices(iso3: str) -> list[tuple]:
```

**Returns:** `list[tuple]`

**What it does:** Fetch adm3 from public FAO AGOL REST service.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `iso3` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _fetch_admin3_choices(iso3: str) -> list[tuple]:
        """
        Fetch adm3 from public FAO AGOL REST service.
        Returns:
          admin3 rows as [(adm3_pcode, adm3_name, adm2_pcode), ...]
        """
        _BASE = ("https://services5.arcgis.com/sjP4Ugu5s0dZWLjd/arcgis/rest/services"
                 "/Reference_Admin_3_(view_layer)/FeatureServer")
        url = (f"{_BASE}/0/query"
               f"?where=adm0_ISO3+%3D+%27{iso3}%27"
               f"&outFields=adm3_name,adm3_pcode,adm2_pcode"
               f"&returnGeometry=false&outSR=4326&f=json")
        with _urlreq.urlopen(url, timeout=30) as r:
            features = _json.loads(r.read().decode())["features"]
        adm3 = sorted(
            [(f["attributes"]["adm3_pcode"], f["attributes"]["adm3_name"], f["attributes"]["adm2_pcode"])
             for f in features],
            key=lambda x: x[0],
        )
        print(f"  AGOL  adm3: {len(adm3)} rows")
        return adm3
    ```

### `_rebuild_choices_sheet` {#fn--rebuild-choices-sheet-7588}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7588`

**Signature**

```python
def _rebuild_choices_sheet(wb, country_rows: dict[str, list[tuple]], target_language: str='en', template_headers: list[str] | None=None) -> dict:
```

**Returns:** `dict`

**What it does:** Replace all rows belonging to country_rows list_names with fresh data.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `country_rows` | positional_or_keyword | Yes | `-` | `dict[str, list[tuple]]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `target_language` | positional_or_keyword | No | `'en'` | `str` | Language selector used for language-specific text columns. |
| `template_headers` | positional_or_keyword | No | `None` | `list[str] | None` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _rebuild_choices_sheet(
        wb,
        country_rows: dict[str, list[tuple]],
        target_language: str = "en",
        template_headers: list[str] | None = None,
    ) -> dict:
        """
        Replace all rows belonging to country_rows list_names with fresh data.
        Non-country rows and empty separator rows are preserved in their original order.
        New country blocks are appended at the end, each preceded by an empty separator row.
        The output choices header row is aligned to the template header layout when provided.
        """
        ws = wb["choices"]
        all_rows_cells = list(ws.iter_rows(min_row=1, max_row=ws.max_row, max_col=ws.max_column))
        if not all_rows_cells:
            return {
                "used_template_headers": False,
                "template_header_count": 0,
                "source_only_headers_appended": 0,
                "extra_admin_rows": {},
                "extra_admin_rows_total": 0,
                "final_headers": [],
                "original_admin_counts": {},
                "written_admin_counts": {},
            }

        src_n_cols = ws.max_column or 5

        def _row_values(cells):
            vals = [c.value for c in cells]
            if len(vals) < src_n_cols:
                vals.extend([None] * (src_n_cols - len(vals)))
            return vals[:src_n_cols]

        def _row_styles(cells):
            styles = []
            for i in range(src_n_cols):
                if i < len(cells):
                    styles.append(_style_copy(cells[i]._style))
                else:
                    styles.append(None)
            return styles

        header_vals = _row_values(all_rows_cells[0])
        header_styles = _row_styles(all_rows_cells[0])
        source_headers = [str(h).strip() if h is not None else "" for h in header_vals]
        output_headers = _resolve_choices_output_headers(source_headers, template_headers)
        n_cols = max(len(output_headers), 5)
        if len(output_headers) < n_cols:
            output_headers.extend([""] * (n_cols - len(output_headers)))
        output_col_idx = {h: i for i, h in enumerate(output_headers)}
        col_idx = {h: i for i, h in enumerate(source_headers)}
        skip = set(country_rows.keys())

        list_col = col_idx.get("list_name", 0)
        name_col = col_idx.get("name", 1)
        en_label_col = col_idx.get(LANG_LABEL_COL.get("en", "label::English (en)"))
        tgt_label_name = LANG_LABEL_COL.get(str(target_language or "").lower(), f"label::{target_language}")
        tgt_label_col = col_idx.get(tgt_label_name)
        fallback_label_name = _find_label_col(source_headers, str(target_language or "en"))
        fallback_label_col = col_idx.get(fallback_label_name) if fallback_label_name else None

        admin_filter_col = None
        for c in ("my_filter_admin", "choice_filter", "filter", "tema", "team"):
            if c in col_idx:
                admin_filter_col = col_idx[c]
                break
        if admin_filter_col is None and n_cols >= 5:
            admin_filter_col = 4
        sample_filter_col = col_idx.get("my_filter_sample")

        def _norm_key(v):
            return str(v).strip().lower() if v is not None else ""

        def _is_empty(v):
            return v is None or str(v).strip() == ""

        preserved_sample_by_code: dict[tuple[str, str], object] = {}
        preserved_sample_by_label: dict[tuple[str, str], object] = {}
        preserved_sample_by_label_parent: dict[tuple[str, str, str], object] = {}

        def _remember_sample(list_name, code_val, label_val, parent_val, sample_val):
            if sample_filter_col is None or _is_empty(sample_val):
                return
            list_key = _norm_key(list_name)
            code_key = _norm_key(code_val)
            label_key = _norm_key(label_val)
            parent_key = _norm_key(parent_val)

            if code_key:
                preserved_sample_by_code.setdefault((list_key, code_key), sample_val)
            if label_key:
                preserved_sample_by_label.setdefault((list_key, label_key), sample_val)
            if label_key and parent_key:
                preserved_sample_by_label_parent.setdefault((list_key, label_key, parent_key), sample_val)

        def _is_blank(values):
            return all(v is None or str(v).strip() == "" for v in values)

        original_admin_counts = {"admin1": 0, "admin2": 0, "admin3": 0}

        # Keep non-country rows (with styles) and capture style templates for replaced lists.
        kept_rows: list[tuple[list, list, bool]] = []
        style_by_list: dict[str, list] = {}
        blank_style = None
        generic_style = _row_styles(all_rows_cells[1]) if len(all_rows_cells) > 1 else header_styles
        _, header_styles_out = _remap_choices_row_to_headers(
            header_vals,
            header_styles,
            source_headers,
            output_headers,
            fallback_styles=header_styles,
        )
        _, generic_style_out = _remap_choices_row_to_headers(
            header_vals,
            generic_style,
            source_headers,
            output_headers,
            fallback_styles=generic_style,
        )

        for cells in all_rows_cells[1:]:
            vals = _row_values(cells)
            styles = _row_styles(cells)
            list_val = vals[list_col] if list_col < len(vals) else None
            list_txt = str(list_val).strip() if list_val is not None else ""
            list_txt_norm = list_txt.lower()
            remapped_vals, remapped_styles = _remap_choices_row_to_headers(
                vals,
                styles,
                source_headers,
                output_headers,
                fallback_styles=generic_style_out,
            )

            if list_txt_norm in original_admin_counts and not _is_blank(vals):
                original_admin_counts[list_txt_norm] += 1

            if list_txt_norm in skip:
                style_by_list.setdefault(list_txt_norm, remapped_styles)
                if blank_style is None and _is_blank(vals):
                    blank_style = remapped_styles
                if sample_filter_col is not None and sample_filter_col < len(vals):
                    old_code = vals[name_col] if name_col < len(vals) else None
                    if fallback_label_col is not None and fallback_label_col < len(vals):
                        old_label = vals[fallback_label_col]
                    elif en_label_col is not None and en_label_col < len(vals):
                        old_label = vals[en_label_col]
                    elif tgt_label_col is not None and tgt_label_col < len(vals):
                        old_label = vals[tgt_label_col]
                    else:
                        old_label = None
                    old_parent = vals[admin_filter_col] if admin_filter_col is not None and admin_filter_col < len(vals) else None
                    _remember_sample(list_txt, old_code, old_label, old_parent, vals[sample_filter_col])
                continue

            if blank_style is None and _is_blank(vals):
                blank_style = remapped_styles
            kept_rows.append((remapped_vals, remapped_styles, False))

        if blank_style is None:
            blank_style = generic_style_out

        # Build new country blocks, each preceded by an empty separator row.
        new_rows: list[tuple[list, list, bool]] = []
        final_list_col = output_col_idx.get("list_name", 0)
        final_name_col = output_col_idx.get("name", 1)
        final_en_label_col = output_col_idx.get(LANG_LABEL_COL.get("en", "label::English (en)"))
        final_tgt_label_col = output_col_idx.get(tgt_label_name)
        final_fallback_label_name = _find_label_col(output_headers, str(target_language or "en"))
        final_fallback_label_col = output_col_idx.get(final_fallback_label_name) if final_fallback_label_name else None
        final_admin_filter_col = None
        for c in ("my_filter_admin", "choice_filter", "filter", "tema", "team"):
            if c in output_col_idx:
                final_admin_filter_col = output_col_idx[c]
                break
        if final_admin_filter_col is None and n_cols >= 5:
            final_admin_filter_col = 4
        final_sample_filter_col = output_col_idx.get("my_filter_sample")
        extra_admin_rows: dict[str, int] = {}
        written_admin_counts: dict[str, int] = {}

        for list_name, entries in country_rows.items():
            new_rows.append(([None] * n_cols, blank_style, False))
            row_style = style_by_list.get(str(list_name), generic_style_out)
            written_n = 0
            for entry_idx, entry in enumerate(entries, start=1):
                row = [None] * n_cols
                row[final_list_col] = list_name
                row[final_name_col] = entry[0] if len(entry) > 0 else ""

                if list_name in _CROP_SPECIALS:
                    en_lbl = str(entry[1] if len(entry) > 1 else "").strip()
                    tgt_lbl = str(entry[2] if len(entry) > 2 else en_lbl).strip()
                    if final_en_label_col is not None:
                        row[final_en_label_col] = en_lbl
                    if final_tgt_label_col is not None:
                        row[final_tgt_label_col] = tgt_lbl
                    if final_en_label_col is None and final_tgt_label_col is None and final_fallback_label_col is not None:
                        row[final_fallback_label_col] = tgt_lbl
                else:
                    admin_lbl = str(entry[1] if len(entry) > 1 else "").strip()
                    if final_fallback_label_col is not None:
                        row[final_fallback_label_col] = admin_lbl
                    elif final_en_label_col is not None:
                        row[final_en_label_col] = admin_lbl
                    if len(entry) > 2 and final_admin_filter_col is not None:
                        row[final_admin_filter_col] = entry[2]
                    # Preserve existing sample filters for matching admin rows.
                    if (
                        final_sample_filter_col is not None
                        and final_sample_filter_col < n_cols
                        and _norm_key(list_name) in {"admin1", "admin2", "admin3"}
                    ):
                        list_key = _norm_key(list_name)
                        code_key = _norm_key(entry[0] if len(entry) > 0 else "")
                        label_key = _norm_key(admin_lbl)
                        parent_key = _norm_key(entry[2] if len(entry) > 2 else "")
                        preserved_sample = None
                        if code_key:
                            preserved_sample = preserved_sample_by_code.get((list_key, code_key))
                        if preserved_sample is None and label_key and parent_key:
                            preserved_sample = preserved_sample_by_label_parent.get((list_key, label_key, parent_key))
                        if preserved_sample is None and label_key:
                            preserved_sample = preserved_sample_by_label.get((list_key, label_key))
                        if preserved_sample is not None:
                            row[final_sample_filter_col] = preserved_sample

                written_n += 1
                highlight_extra = (
                    _norm_key(list_name) in {"admin1", "admin2", "admin3"}
                    and entry_idx > original_admin_counts.get(_norm_key(list_name), 0)
                )
                if highlight_extra:
                    extra_admin_rows[_norm_key(list_name)] = extra_admin_rows.get(_norm_key(list_name), 0) + 1
                new_rows.append((row, row_style, highlight_extra))
            if _norm_key(list_name) in {"admin1", "admin2", "admin3"}:
                written_admin_counts[_norm_key(list_name)] = written_n

        # Rewrite choices with preserved styles.
        payload = [(output_headers, header_styles_out, False)] + kept_rows + new_rows
        ws.delete_rows(1, ws.max_row)
        for r_idx, (vals, styles, highlight_extra) in enumerate(payload, start=1):
            for c_idx in range(1, n_cols + 1):
                cell = ws.cell(row=r_idx, column=c_idx, value=vals[c_idx - 1] if c_idx - 1 < len(vals) else None)
                if c_idx - 1 < len(styles) and styles[c_idx - 1] is not None:
                    cell._style = _style_copy(styles[c_idx - 1])
                if highlight_extra:
                    cell.fill = FILL_HIGHLIGHT_YELLOW

        template_header_count = len([h for h in (template_headers or []) if str(h or "").strip() != ""])
        appended_headers = max(0, len([h for h in output_headers if str(h or "").strip() != ""]) - template_header_count)
        return {
            "used_template_headers": bool(template_headers),
            "template_header_count": template_header_count,
            "source_only_headers_appended": appended_headers if template_headers else 0,
            "extra_admin_rows": extra_admin_rows,
            "extra_admin_rows_total": sum(extra_admin_rows.values()),
            "final_headers": output_headers,
            "original_admin_counts": original_admin_counts,
            "written_admin_counts": written_admin_counts,
        }
    ```

### `_rebuild_choices_sheet._row_values` {#fn--row-values-7616}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7616`

**Signature**

```python
def _row_values(cells):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cells` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _row_values(cells):
            vals = [c.value for c in cells]
            if len(vals) < src_n_cols:
                vals.extend([None] * (src_n_cols - len(vals)))
            return vals[:src_n_cols]
    ```

### `_rebuild_choices_sheet._row_styles` {#fn--row-styles-7622}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7622`

**Signature**

```python
def _row_styles(cells):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cells` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _row_styles(cells):
            styles = []
            for i in range(src_n_cols):
                if i < len(cells):
                    styles.append(_style_copy(cells[i]._style))
                else:
                    styles.append(None)
            return styles
    ```

### `_rebuild_choices_sheet._norm_key` {#fn--norm-key-7659}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7659`

**Signature**

```python
def _norm_key(v):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `v` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _norm_key(v):
            return str(v).strip().lower() if v is not None else ""
    ```

### `_rebuild_choices_sheet._is_empty` {#fn--is-empty-7662}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7662`

**Signature**

```python
def _is_empty(v):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `v` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _is_empty(v):
            return v is None or str(v).strip() == ""
    ```

### `_rebuild_choices_sheet._remember_sample` {#fn--remember-sample-7669}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7669`

**Signature**

```python
def _remember_sample(list_name, code_val, label_val, parent_val, sample_val):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `list_name` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `code_val` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `label_val` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `parent_val` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `sample_val` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _remember_sample(list_name, code_val, label_val, parent_val, sample_val):
            if sample_filter_col is None or _is_empty(sample_val):
                return
            list_key = _norm_key(list_name)
            code_key = _norm_key(code_val)
            label_key = _norm_key(label_val)
            parent_key = _norm_key(parent_val)

            if code_key:
                preserved_sample_by_code.setdefault((list_key, code_key), sample_val)
            if label_key:
                preserved_sample_by_label.setdefault((list_key, label_key), sample_val)
            if label_key and parent_key:
                preserved_sample_by_label_parent.setdefault((list_key, label_key, parent_key), sample_val)
    ```

### `_rebuild_choices_sheet._is_blank` {#fn--is-blank-7684}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7684`

**Signature**

```python
def _is_blank(values):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `values` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _is_blank(values):
            return all(v is None or str(v).strip() == "" for v in values)
    ```

### `_strip_skipped_module_blocks_from_survey_sheet` {#fn--strip-skipped-module-blocks-from-survey-sheet-7852}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7852`

**Signature**

```python
def _strip_skipped_module_blocks_from_survey_sheet(wb, skip_module_keys: set[str], skip_qnames: set[str] | None=None) -> dict[str, int]:
```

**Returns:** `dict[str, int]`

**What it does:** Remove entire skipped-module blocks from survey sheet, including begin/end rows.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `skip_module_keys` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `skip_qnames` | positional_or_keyword | No | `None` | `set[str] | None` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _strip_skipped_module_blocks_from_survey_sheet(
        wb,
        skip_module_keys: set[str],
        skip_qnames: set[str] | None = None,
    ) -> dict[str, int]:
        """
        Remove entire skipped-module blocks from survey sheet, including begin/end rows.
        Also removes any explicitly listed question names as a safety fallback.
        """
        stats = {
            "removed_rows": 0,
            "removed_question_rows": 0,
            "removed_group_rows": 0,
            "removed_module_blocks": 0,
        }
        if "survey" not in wb.sheetnames:
            return stats

        ws = wb["survey"]
        all_rows = list(ws.iter_rows(values_only=True))
        if not all_rows:
            return stats

        n_cols = max((len(r) for r in all_rows), default=0)
        _hdr_idx = _find_xlsform_header_row_idx(all_rows)
        headers = [str(h).strip() if h is not None else "" for h in all_rows[_hdr_idx]]
        col_idx = {h: i for i, h in enumerate(headers)}
        type_col = col_idx.get("type")
        name_col = col_idx.get("name")
        if type_col is None and name_col is None:
            return stats

        skip_keys_norm = {
            _normalize_module_token(v)
            for v in (skip_module_keys or set())
            if _normalize_module_token(v)
        }
        skip_q = {str(v).strip() for v in (skip_qnames or set()) if str(v or "").strip()}
        if not skip_keys_norm and not skip_q:
            return stats

        def _cell(row, idx):
            if row is None or idx is None or idx >= len(row):
                return None
            return row[idx]

        kept = list(all_rows[:_hdr_idx + 1])
        stack: list[dict[str, object]] = []

        for row in all_rows[_hdr_idx + 1:]:
            q_type_raw = str(_cell(row, type_col) or "").strip()
            q_name = str(_cell(row, name_col) or "").strip()
            type_norm = _normalize_survey_type_token(q_type_raw)

            inside_removed = bool(stack[-1]["remove"]) if stack else False

            if any(type_norm.startswith(t) for t in _GROUP_BEGIN_TYPES):
                key_norm = _normalize_module_token(q_name)
                self_match = key_norm in skip_keys_norm if key_norm else False
                remove_here = inside_removed or self_match
                stack.append({"remove": remove_here, "module_key_norm": key_norm})
                if self_match and not inside_removed:
                    stats["removed_module_blocks"] += 1
                if remove_here:
                    stats["removed_rows"] += 1
                    stats["removed_group_rows"] += 1
                else:
                    kept.append(row)
                continue

            if any(type_norm.startswith(t) for t in _GROUP_END_TYPES):
                remove_here = bool(stack[-1]["remove"]) if stack else False
                if stack:
                    stack.pop()
                if remove_here:
                    stats["removed_rows"] += 1
                    stats["removed_group_rows"] += 1
                else:
                    kept.append(row)
                continue

            remove_here = inside_removed or (q_name in skip_q if q_name else False)
            if remove_here:
                stats["removed_rows"] += 1
                stats["removed_question_rows"] += 1
            else:
                kept.append(row)

        if stats["removed_rows"] == 0:
            return stats

        ws.delete_rows(1, ws.max_row)
        for r in kept:
            padded = list(r) + [None] * max(0, n_cols - len(r))
            ws.append(padded[:n_cols] if n_cols > 0 else list(r))
        return stats
    ```

### `_strip_skipped_module_blocks_from_survey_sheet._cell` {#fn--cell-7893}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7893`

**Signature**

```python
def _cell(row, idx):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `idx` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _cell(row, idx):
            if row is None or idx is None or idx >= len(row):
                return None
            return row[idx]
    ```

### `_remove_choices_lists_rows` {#fn--remove-choices-lists-rows-7950}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7950`

**Signature**

```python
def _remove_choices_lists_rows(wb, list_names: set[str]) -> int:
```

**Returns:** `int`

**What it does:** Remove all choices rows whose list_name is in list_names (normalized compare).

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `list_names` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _remove_choices_lists_rows(wb, list_names: set[str]) -> int:
        """Remove all choices rows whose list_name is in list_names (normalized compare)."""
        if "choices" not in wb.sheetnames or not list_names:
            return 0

        ws = wb["choices"]
        all_rows = list(ws.iter_rows(values_only=True))
        if not all_rows:
            return 0

        n_cols = max((len(r) for r in all_rows), default=0)
        headers = [str(h).strip() if h is not None else "" for h in all_rows[0]]
        col_idx = {h: i for i, h in enumerate(headers)}
        list_col = col_idx.get("list_name", 0)
        wanted = {
            _normalize_list_token(v)
            for v in list_names
            if _normalize_list_token(v)
        }
        if not wanted:
            return 0

        def _cell(row, idx):
            if row is None or idx is None or idx >= len(row):
                return None
            return row[idx]

        kept = [all_rows[0]]
        removed = 0
        for row in all_rows[1:]:
            ln = str(_cell(row, list_col) or "").strip()
            if ln and _normalize_list_token(ln) in wanted:
                removed += 1
                continue
            kept.append(row)

        if removed == 0:
            return 0

        ws.delete_rows(1, ws.max_row)
        for r in kept:
            padded = list(r) + [None] * max(0, n_cols - len(r))
            ws.append(padded[:n_cols] if n_cols > 0 else list(r))
        return removed
    ```

### `_remove_choices_lists_rows._cell` {#fn--cell-7972}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7972`

**Signature**

```python
def _cell(row, idx):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `idx` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _cell(row, idx):
            if row is None or idx is None or idx >= len(row):
                return None
            return row[idx]
    ```

### `_detect_kobo_header_language` {#fn--detect-kobo-header-language-7996}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:7996`

**Signature**

```python
def _detect_kobo_header_language(header_value: object) -> str | None:
```

**Returns:** `str | None`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `header_value` | positional_or_keyword | Yes | `-` | `object` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _detect_kobo_header_language(header_value: object) -> str | None:
        header = str(header_value or "").strip().lower()
        if not header:
            return None

        for lang, canonical in LANG_LABEL_COL.items():
            if header == canonical.lower():
                return lang

        match = re.search(r"\((en|fr|ar|es)\)\s*$", header)
        if match:
            return match.group(1).lower()

        if "::english" in header or header.endswith("_english"):
            return "en"
        if "::french" in header or header.endswith("_french"):
            return "fr"
        if "::arabic" in header or header.endswith("_arabic"):
            return "ar"
        if "::spanish" in header or header.endswith("_spanish"):
            return "es"
        return None
    ```

### `_apply_replacements_to_wb` {#fn--apply-replacements-to-wb-8020}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8020`

**Signature**

```python
def _apply_replacements_to_wb(wb, replacement_pairs: dict, replacement_pairs_by_language: dict[str, dict[str, str]] | None=None, target_language: str='en') -> None:
```

**Returns:** `None`

**What it does:** Apply #placeholder# -> value to workbook text, respecting per-language columns.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `replacement_pairs` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `replacement_pairs_by_language` | positional_or_keyword | No | `None` | `dict[str, dict[str, str]] | None` | Language selector used for language-specific text columns. |
| `target_language` | positional_or_keyword | No | `'en'` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _apply_replacements_to_wb(
        wb,
        replacement_pairs: dict,
        replacement_pairs_by_language: dict[str, dict[str, str]] | None = None,
        target_language: str = "en",
    ) -> None:
        """Apply #placeholder# -> value to workbook text, respecting per-language columns."""
        if not replacement_pairs and not any((replacement_pairs_by_language or {}).values()):
            return
        for sheet_name in ("survey", "choices"):
            if sheet_name not in wb.sheetnames:
                continue
            ws = wb[sheet_name]
            _hdr_row_1 = _find_ws_header_row_1based(ws) if sheet_name == "survey" else 1
            headers = [cell.value for cell in next(ws.iter_rows(min_row=_hdr_row_1, max_row=_hdr_row_1), [])]
            for row_idx, row in enumerate(ws.iter_rows(), start=1):
                for cell in row:
                    if isinstance(cell.value, str) and "#" in cell.value:
                        col_header = headers[cell.column - 1] if cell.column - 1 < len(headers) else None
                        col_lang = _detect_kobo_header_language(col_header)
                        if row_idx <= _hdr_row_1:
                            col_lang = None
                        active_pairs = replacement_pairs
                        if col_lang and replacement_pairs_by_language and replacement_pairs_by_language.get(col_lang):
                            active_pairs = replacement_pairs_by_language[col_lang]
                        elif not col_lang and replacement_pairs_by_language:
                            tgt_pairs = replacement_pairs_by_language.get(str(target_language or "en").lower(), {})
                            if tgt_pairs:
                                active_pairs = tgt_pairs
                        if not active_pairs:
                            continue
                        v = cell.value
                        for key, val in sorted(active_pairs.items(), key=lambda x: len(x[0]), reverse=True):
                            if key in v:
                                v = v.replace(key, str(val))
                        cell.value = v
    ```

### `_restore_placeholder_tokens_from_template` {#fn--restore-placeholder-tokens-from-template-8058}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8058`

**Signature**

```python
def _restore_placeholder_tokens_from_template(wb, template_path: str, replacement_pairs: dict[str, str] | None=None) -> dict:
```

**Returns:** `dict`

**What it does:** Restore placeholder-bearing cells from template into current workbook for:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `template_path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |
| `replacement_pairs` | positional_or_keyword | No | `None` | `dict[str, str] | None` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _restore_placeholder_tokens_from_template(
        wb,
        template_path: str,
        replacement_pairs: dict[str, str] | None = None,
    ) -> dict:
        """
        Restore placeholder-bearing cells from template into current workbook for:
          - survey sheet (key: name)
          - choices sheet (key: list_name + name)
        Only shared headers are considered; only template cells containing #...# are copied.
        """
        stats = {
            "survey_cells_restored": 0,
            "choices_cells_restored": 0,
            "survey_template_placeholder_cells": 0,
            "choices_template_placeholder_cells": 0,
            "survey_placeholder_cells_skipped_missing_replacement": 0,
            "choices_placeholder_cells_skipped_missing_replacement": 0,
            "survey_cells_already_vanilla": 0,
            "choices_cells_already_vanilla": 0,
            "survey_missing_key_rows": 0,
            "choices_missing_key_rows": 0,
            "survey_missing_qnames": [],
            "choices_missing_keys": [],
            "error": "",
        }

        def _norm_txt(v) -> str:
            return str(v or "").strip()

        _allow_tokens_exact: set[str] | None = None
        _allow_tokens_lower: set[str] | None = None
        if replacement_pairs is not None:
            _allow_tokens_exact = set(str(k) for k in replacement_pairs.keys())
            _allow_tokens_lower = {str(k).lower() for k in replacement_pairs.keys()}

        def _can_restore_template_value(v: str) -> bool:
            if _allow_tokens_exact is None or _allow_tokens_lower is None:
                return True
            toks = _PLACEHOLDER_RE.findall(v or "")
            if not toks:
                return True
            for t in toks:
                if t in _allow_tokens_exact:
                    continue
                if str(t).lower() in _allow_tokens_lower:
                    continue
                return False
            return True

        try:
            tpl_wb = openpyxl.load_workbook(template_path, data_only=False, read_only=True)
        except Exception as e:
            stats["error"] = f"could not open template for placeholder restore: {e}"
            return stats

        try:
            # -- survey --------------------------------------------------------------
            if "survey" in wb.sheetnames and "survey" in tpl_wb.sheetnames:
                ws_cur = wb["survey"]
                ws_tpl = tpl_wb["survey"]

                _cur_hdr_1 = _find_ws_header_row_1based(ws_cur)
                _tpl_hdr_1 = _find_ws_header_row_1based(ws_tpl)
                cur_hdr_vals = next(ws_cur.iter_rows(min_row=_cur_hdr_1, max_row=_cur_hdr_1, values_only=True), None) or []
                tpl_hdr_vals = next(ws_tpl.iter_rows(min_row=_tpl_hdr_1, max_row=_tpl_hdr_1, values_only=True), None) or []
                cur_headers = [str(h).strip() if h is not None else "" for h in cur_hdr_vals]
                tpl_headers = [str(h).strip() if h is not None else "" for h in tpl_hdr_vals]
                cur_idx = {h: i for i, h in enumerate(cur_headers) if h}
                tpl_idx = {h: i for i, h in enumerate(tpl_headers) if h}
                shared_headers = [h for h in tpl_idx.keys() if h in cur_idx]

                if "name" in cur_idx and "name" in tpl_idx and shared_headers:
                    cur_rows_by_name: dict[str, tuple] = {}
                    for row in ws_cur.iter_rows(min_row=_cur_hdr_1 + 1):
                        qn = _norm_txt(row[cur_idx["name"]].value if cur_idx["name"] < len(row) else "")
                        if qn and qn not in cur_rows_by_name:
                            cur_rows_by_name[qn] = row

                    for tpl_row in ws_tpl.iter_rows(min_row=_tpl_hdr_1 + 1, values_only=True):
                        qn = _norm_txt(tpl_row[tpl_idx["name"]] if tpl_idx["name"] < len(tpl_row) else "")
                        if not qn:
                            continue
                        _tpl_placeholder_cells: list[tuple[str, str]] = []
                        for h in shared_headers:
                            t_i = tpl_idx[h]
                            t_val = tpl_row[t_i] if t_i < len(tpl_row) else None
                            if isinstance(t_val, str) and "#" in t_val and _PLACEHOLDER_RE.search(t_val):
                                _tpl_placeholder_cells.append((h, t_val))
                        if not _tpl_placeholder_cells:
                            continue

                        stats["survey_template_placeholder_cells"] += len(_tpl_placeholder_cells)
                        cur_row = cur_rows_by_name.get(qn)
                        if cur_row is None:
                            stats["survey_missing_key_rows"] += 1
                            stats["survey_missing_qnames"].append(qn)
                            continue
                        for h, t_val in _tpl_placeholder_cells:
                            if not _can_restore_template_value(t_val):
                                stats["survey_placeholder_cells_skipped_missing_replacement"] += 1
                                continue
                            c_i = cur_idx[h]
                            cur_cell = cur_row[c_i] if c_i < len(cur_row) else None
                            if cur_cell is None:
                                continue
                            if cur_cell.value != t_val:
                                cur_cell.value = t_val
                                stats["survey_cells_restored"] += 1
                            else:
                                stats["survey_cells_already_vanilla"] += 1

            # -- choices -------------------------------------------------------------
            if "choices" in wb.sheetnames and "choices" in tpl_wb.sheetnames:
                ws_cur = wb["choices"]
                ws_tpl = tpl_wb["choices"]

                cur_hdr_vals = next(ws_cur.iter_rows(min_row=1, max_row=1, values_only=True), None) or []
                tpl_hdr_vals = next(ws_tpl.iter_rows(min_row=1, max_row=1, values_only=True), None) or []
                cur_headers = [str(h).strip() if h is not None else "" for h in cur_hdr_vals]
                tpl_headers = [str(h).strip() if h is not None else "" for h in tpl_hdr_vals]
                cur_idx = {h: i for i, h in enumerate(cur_headers) if h}
                tpl_idx = {h: i for i, h in enumerate(tpl_headers) if h}
                shared_headers = [h for h in tpl_idx.keys() if h in cur_idx]

                if {"list_name", "name"}.issubset(set(cur_idx.keys())) and {"list_name", "name"}.issubset(set(tpl_idx.keys())):
                    cur_rows_by_key: dict[tuple[str, str], tuple] = {}
                    for row in ws_cur.iter_rows(min_row=2):
                        ln = _normalize_list_token(row[cur_idx["list_name"]].value if cur_idx["list_name"] < len(row) else "")
                        nm = _canonical_option_name_token(row[cur_idx["name"]].value if cur_idx["name"] < len(row) else "")
                        if ln and nm and (ln, nm) not in cur_rows_by_key:
                            cur_rows_by_key[(ln, nm)] = row

                    for tpl_row in ws_tpl.iter_rows(min_row=2, values_only=True):
                        ln = _normalize_list_token(tpl_row[tpl_idx["list_name"]] if tpl_idx["list_name"] < len(tpl_row) else "")
                        nm = _canonical_option_name_token(tpl_row[tpl_idx["name"]] if tpl_idx["name"] < len(tpl_row) else "")
                        if not ln or not nm:
                            continue
                        _tpl_placeholder_cells: list[tuple[str, str]] = []
                        for h in shared_headers:
                            t_i = tpl_idx[h]
                            t_val = tpl_row[t_i] if t_i < len(tpl_row) else None
                            if isinstance(t_val, str) and "#" in t_val and _PLACEHOLDER_RE.search(t_val):
                                _tpl_placeholder_cells.append((h, t_val))
                        if not _tpl_placeholder_cells:
                            continue

                        stats["choices_template_placeholder_cells"] += len(_tpl_placeholder_cells)
                        cur_row = cur_rows_by_key.get((ln, nm))
                        if cur_row is None:
                            stats["choices_missing_key_rows"] += 1
                            stats["choices_missing_keys"].append(f"{ln}/{nm}")
                            continue
                        for h, t_val in _tpl_placeholder_cells:
                            if not _can_restore_template_value(t_val):
                                stats["choices_placeholder_cells_skipped_missing_replacement"] += 1
                                continue
                            c_i = cur_idx[h]
                            cur_cell = cur_row[c_i] if c_i < len(cur_row) else None
                            if cur_cell is None:
                                continue
                            if cur_cell.value != t_val:
                                cur_cell.value = t_val
                                stats["choices_cells_restored"] += 1
                            else:
                                stats["choices_cells_already_vanilla"] += 1
        finally:
            tpl_wb.close()

        return stats
    ```

### `_restore_placeholder_tokens_from_template._norm_txt` {#fn--norm-txt-8085}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8085`

**Signature**

```python
def _norm_txt(v) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `v` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _norm_txt(v) -> str:
            return str(v or "").strip()
    ```

### `_restore_placeholder_tokens_from_template._can_restore_template_value` {#fn--can-restore-template-value-8094}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8094`

**Signature**

```python
def _can_restore_template_value(v: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `v` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _can_restore_template_value(v: str) -> bool:
            if _allow_tokens_exact is None or _allow_tokens_lower is None:
                return True
            toks = _PLACEHOLDER_RE.findall(v or "")
            if not toks:
                return True
            for t in toks:
                if t in _allow_tokens_exact:
                    continue
                if str(t).lower() in _allow_tokens_lower:
                    continue
                return False
            return True
    ```

### `_count_choices_list_rows` {#fn--count-choices-list-rows-8230}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8230`

**Signature**

```python
def _count_choices_list_rows(wb, list_name: str) -> int:
```

**Returns:** `int`

**What it does:** Count rows in choices sheet belonging to a given list_name.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `list_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _count_choices_list_rows(wb, list_name: str) -> int:
        """Count rows in choices sheet belonging to a given list_name."""
        if "choices" not in wb.sheetnames:
            return 0
        ws = wb["choices"]
        return sum(
            1
            for r in ws.iter_rows(min_row=2, values_only=True)
            if str((r[0] if r and len(r) > 0 else "") or "").strip() == list_name
        )
    ```

### `_choices_header_index_map` {#fn--choices-header-index-map-8242}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8242`

**Signature**

```python
def _choices_header_index_map(wb) -> dict[str, int]:
```

**Returns:** `dict[str, int]`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |

??? note "Function source"

    ```python
    def _choices_header_index_map(wb) -> dict[str, int]:
        if "choices" not in wb.sheetnames:
            return {}
        ws = wb["choices"]
        row = next(ws.iter_rows(min_row=1, max_row=1, values_only=True), None)
        if not row:
            return {}
        headers = [str(h).strip() if h is not None else "" for h in row]
        return {h: i for i, h in enumerate(headers) if h}
    ```

### `_count_blank_labels_for_lists` {#fn--count-blank-labels-for-lists-8253}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8253`

**Signature**

```python
def _count_blank_labels_for_lists(wb, list_names: list[str], label_col: str) -> tuple[int, int]:
```

**Returns:** `tuple[int, int]`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `list_names` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `label_col` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _count_blank_labels_for_lists(wb, list_names: list[str], label_col: str) -> tuple[int, int]:
        hdr = _choices_header_index_map(wb)
        if not hdr:
            return 0, 0
        li = hdr.get("list_name", 0)
        ci = hdr.get(label_col)
        if ci is None:
            return 0, 0
        ws = wb["choices"]
        wanted = {str(v).strip() for v in list_names}
        total = 0
        blank = 0
        for row in ws.iter_rows(min_row=2, values_only=True):
            ln = str((row[li] if li < len(row) else "") or "").strip()
            if ln not in wanted:
                continue
            total += 1
            lbl = row[ci] if ci < len(row) else None
            if lbl is None or str(lbl).strip() == "":
                blank += 1
        return total, blank
    ```

### `_validate_admin_parent_links_in_choices_sheet` {#fn--validate-admin-parent-links-in-choices-sheet-8276}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8276`

**Signature**

```python
def _validate_admin_parent_links_in_choices_sheet(wb) -> dict:
```

**Returns:** `dict`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |

??? note "Function source"

    ```python
    def _validate_admin_parent_links_in_choices_sheet(wb) -> dict:
        stats = {
            "checked": {"admin2": 0, "admin3": 0},
            "issues": [],
            "parent_column": "",
            "header_present": False,
        }
        if "choices" not in wb.sheetnames:
            return stats

        ws = wb["choices"]
        row = next(ws.iter_rows(min_row=1, max_row=1, values_only=True), None)
        if not row:
            return stats

        headers = [str(h).strip() if h is not None else "" for h in row]
        idx = {h: i for i, h in enumerate(headers) if h}
        list_col = idx.get("list_name")
        name_col = idx.get("name")
        parent_col = None
        parent_header = ""
        for candidate in ("my_filter_admin", "choice_filter", "filter", "tema", "team"):
            if candidate in idx:
                parent_col = idx[candidate]
                parent_header = candidate
                break
        stats["parent_column"] = parent_header
        stats["header_present"] = parent_col is not None

        if list_col is None or name_col is None or parent_col is None:
            return stats

        names_by_list = {"admin1": set(), "admin2": set(), "admin3": set()}
        rows_by_list = {"admin2": [], "admin3": []}

        for excel_row, values in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
            list_name = _normalize_list_token(values[list_col] if list_col < len(values) else "")
            if list_name not in names_by_list:
                continue
            code = str((values[name_col] if name_col < len(values) else "") or "").strip()
            parent = str((values[parent_col] if parent_col < len(values) else "") or "").strip()
            if code:
                names_by_list[list_name].add(code)
            if list_name in rows_by_list and code:
                rows_by_list[list_name].append({
                    "excel_row": excel_row,
                    "list_name": list_name,
                    "code": code,
                    "parent": parent,
                })

        expectations = {
            "admin2": ("admin1", "admin1.name"),
            "admin3": ("admin2", "admin2.name"),
        }
        for list_name, rows in rows_by_list.items():
            parent_list, parent_ref = expectations[list_name]
            valid_parent_codes = names_by_list.get(parent_list, set())
            for row_info in rows:
                stats["checked"][list_name] += 1
                parent = row_info["parent"]
                if not parent:
                    stats["issues"].append({
                        "list_name": list_name,
                        "code": row_info["code"],
                        "parent": parent,
                        "expected_parent_list": parent_list,
                        "reference": parent_ref,
                        "excel_row": row_info["excel_row"],
                        "problem": "missing",
                    })
                elif parent not in valid_parent_codes:
                    stats["issues"].append({
                        "list_name": list_name,
                        "code": row_info["code"],
                        "parent": parent,
                        "expected_parent_list": parent_list,
                        "reference": parent_ref,
                        "excel_row": row_info["excel_row"],
                        "problem": "not_found",
                    })

        return stats
    ```

### `_highlight_admin_parent_issue_rows_in_choices_sheet` {#fn--highlight-admin-parent-issue-rows-in-choices-sheet-8361}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8361`

**Signature**

```python
def _highlight_admin_parent_issue_rows_in_choices_sheet(wb, issues: list[dict], target_lists: set[str] | None=None) -> int:
```

**Returns:** `int`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `issues` | positional_or_keyword | Yes | `-` | `list[dict]` | Polars DataFrame carrying records for this processing stage. |
| `target_lists` | positional_or_keyword | No | `None` | `set[str] | None` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _highlight_admin_parent_issue_rows_in_choices_sheet(
        wb,
        issues: list[dict],
        target_lists: set[str] | None = None,
    ) -> int:
        if "choices" not in wb.sheetnames or not issues:
            return 0

        wanted = {
            _normalize_list_token(v)
            for v in (target_lists or {"admin3"})
            if _normalize_list_token(v)
        }
        if not wanted:
            return 0

        ws = wb["choices"]
        rows_to_highlight = sorted({
            int(rr.get("excel_row"))
            for rr in issues
            if isinstance(rr.get("excel_row"), int)
            and _normalize_list_token(rr.get("list_name")) in wanted
            and int(rr.get("excel_row")) >= 2
        })
        if not rows_to_highlight:
            return 0

        for excel_row in rows_to_highlight:
            for cell in ws[excel_row]:
                cell.fill = FILL_MEDIUM
        return len(rows_to_highlight)
    ```

### `_write_admin_parent_mismatch_text_report` {#fn--write-admin-parent-mismatch-text-report-8394}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8394`

**Signature**

```python
def _write_admin_parent_mismatch_text_report(out_file: Path, issues: list[dict], label: str='admin3') -> Path:
```

**Returns:** `Path`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `out_file` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `issues` | positional_or_keyword | Yes | `-` | `list[dict]` | Polars DataFrame carrying records for this processing stage. |
| `label` | positional_or_keyword | No | `'admin3'` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _write_admin_parent_mismatch_text_report(
        out_file: Path,
        issues: list[dict],
        label: str = "admin3",
    ) -> Path:
        wanted = _normalize_list_token(label)
        filtered = [
            rr for rr in (issues or [])
            if _normalize_list_token(rr.get("list_name")) == wanted
        ]

        lines = [
            "Admin parent mismatch report",
            f"List: {label}",
            f"Count: {len(filtered)}",
            "",
        ]

        if not filtered:
            lines.append("No invalid admin parent references found.")
        else:
            lines.append("excel_row\tcode\tparent\tproblem\texpected_parent_list\treference")
            for rr in filtered:
                lines.append(
                    "\t".join([
                        str(rr.get("excel_row") or ""),
                        str(rr.get("code") or ""),
                        str(rr.get("parent") or ""),
                        str(rr.get("problem") or ""),
                        str(rr.get("expected_parent_list") or ""),
                        str(rr.get("reference") or ""),
                    ])
                )

        out_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return out_file
    ```

### `_choices_has_language_col` {#fn--choices-has-language-col-8432}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8432`

**Signature**

```python
def _choices_has_language_col(path: str, language: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _choices_has_language_col(path: str, language: str) -> bool:
        target = LANG_LABEL_COL.get(str(language or "").lower(), f"label::{language}")
        try:
            wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
        except Exception:
            return False
        try:
            if "choices" not in wb.sheetnames:
                return False
            row = next(wb["choices"].iter_rows(min_row=1, max_row=1, values_only=True), None)
            if not row:
                return False
            headers = {str(h).strip() for h in row if h is not None}
            return target in headers
        finally:
            wb.close()
    ```

### `_crop_list_has_language_col` {#fn--crop-list-has-language-col-8450}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8450`

**Signature**

```python
def _crop_list_has_language_col(path: str, language: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _crop_list_has_language_col(path: str, language: str) -> bool:
        try:
            wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
        except Exception:
            return False
        try:
            if "Crop list" not in wb.sheetnames:
                return False
            rows = list(wb["Crop list"].iter_rows(min_row=3, max_row=3, values_only=True))
            if not rows:
                return False
            headers = [str(h).strip() if h is not None else "" for h in rows[0]]
            return _crop_label_idx(headers, language) is not None
        finally:
            wb.close()
    ```

### `_normalize_choice_text_token` {#fn--normalize-choice-text-token-8467}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8467`

**Signature**

```python
def _normalize_choice_text_token(value) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _normalize_choice_text_token(value) -> str:
        txt = unicodedata.normalize("NFKC", str(value or ""))
        txt = txt.translate(_INVISIBLE_TOKEN_CHARS).replace("\u00a0", " ")
        txt = _re.sub(r"\s+", " ", txt).strip()
        return txt
    ```

### `_choice_pair_set_by_list` {#fn--choice-pair-set-by-list-8474}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8474`

**Signature**

```python
def _choice_pair_set_by_list(df: pl.DataFrame, list_names: list[str]) -> dict[str, set[tuple[str, str]]]:
```

**Returns:** `dict[str, set[tuple[str, str]]]`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `list_names` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _choice_pair_set_by_list(df: pl.DataFrame, list_names: list[str]) -> dict[str, set[tuple[str, str]]]:
        out: dict[str, set[tuple[str, str]]] = {ln: set() for ln in list_names}
        if df is None or df.height == 0:
            return out
        for row in df.select(["list_name", "option_name", "option_label"]).iter_rows(named=True):
            ln = _normalize_list_token(row.get("list_name"))
            if ln not in out:
                continue
            code = _normalize_choice_text_token(row.get("option_name"))
            lbl = _normalize_choice_text_token(row.get("option_label"))
            if not code:
                continue
            out[ln].add((code, lbl))
        return out
    ```

### `_choice_pair_set_from_rows` {#fn--choice-pair-set-from-rows-8490}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8490`

**Signature**

```python
def _choice_pair_set_from_rows(rows_by_list: dict[str, list[tuple]], list_names: list[str]) -> dict[str, set[tuple[str, str]]]:
```

**Returns:** `dict[str, set[tuple[str, str]]]`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `rows_by_list` | positional_or_keyword | Yes | `-` | `dict[str, list[tuple]]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `list_names` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _choice_pair_set_from_rows(rows_by_list: dict[str, list[tuple]], list_names: list[str]) -> dict[str, set[tuple[str, str]]]:
        out: dict[str, set[tuple[str, str]]] = {ln: set() for ln in list_names}
        if not rows_by_list:
            return out
        for ln in list_names:
            for entry in rows_by_list.get(ln, []):
                code = _normalize_choice_text_token(entry[0] if len(entry) > 0 else "")
                lbl = _normalize_choice_text_token(entry[1] if len(entry) > 1 else "")
                if not code:
                    continue
                out[ln].add((code, lbl))
        return out
    ```

### `_choice_code_set_by_list` {#fn--choice-code-set-by-list-8504}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8504`

**Signature**

```python
def _choice_code_set_by_list(df: pl.DataFrame, list_names: list[str]) -> dict[str, set[str]]:
```

**Returns:** `dict[str, set[str]]`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `list_names` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _choice_code_set_by_list(df: pl.DataFrame, list_names: list[str]) -> dict[str, set[str]]:
        out: dict[str, set[str]] = {ln: set() for ln in list_names}
        if df is None or df.height == 0:
            return out
        for row in df.select(["list_name", "option_name"]).iter_rows(named=True):
            ln = _normalize_list_token(row.get("list_name"))
            if ln not in out:
                continue
            code = _normalize_choice_text_token(row.get("option_name"))
            if code:
                out[ln].add(code)
        return out
    ```

### `_choice_code_set_from_rows` {#fn--choice-code-set-from-rows-8518}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8518`

**Signature**

```python
def _choice_code_set_from_rows(rows_by_list: dict[str, list[tuple]], list_names: list[str]) -> dict[str, set[str]]:
```

**Returns:** `dict[str, set[str]]`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `rows_by_list` | positional_or_keyword | Yes | `-` | `dict[str, list[tuple]]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `list_names` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _choice_code_set_from_rows(rows_by_list: dict[str, list[tuple]], list_names: list[str]) -> dict[str, set[str]]:
        out: dict[str, set[str]] = {ln: set() for ln in list_names}
        if not rows_by_list:
            return out
        for ln in list_names:
            for entry in rows_by_list.get(ln, []):
                code = _normalize_choice_text_token(entry[0] if len(entry) > 0 else "")
                if code:
                    out[ln].add(code)
        return out
    ```

### `_fmt_choice_pairs` {#fn--fmt-choice-pairs-8530}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8530`

**Signature**

```python
def _fmt_choice_pairs(items: set[tuple[str, str]], limit: int=12) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `items` | positional_or_keyword | Yes | `-` | `set[tuple[str, str]]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `limit` | positional_or_keyword | No | `12` | `int` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _fmt_choice_pairs(items: set[tuple[str, str]], limit: int = 12) -> str:
        def _sort_key(code: str):
            t = str(code or "").strip()
            if _re.fullmatch(r"\d+(?:\.0+)?", t):
                return (0, float(t))
            return (1, t.lower())

        vals = sorted(items, key=lambda x: (_sort_key(x[0]), str(x[1] or "").lower()))
        if not vals:
            return "(none)"
        txts = [f"{c} | {l}" for c, l in vals]
        if len(txts) <= limit:
            return ", ".join(txts)
        return ", ".join(txts[:limit]) + f", ... (+{len(txts) - limit} more)"
    ```

### `_fmt_choice_pairs._sort_key` {#fn--sort-key-8531}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8531`

**Signature**

```python
def _sort_key(code: str):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `code` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _sort_key(code: str):
            t = str(code or "").strip()
            if _re.fullmatch(r"\d+(?:\.0+)?", t):
                return (0, float(t))
            return (1, t.lower())
    ```

### `_fmt_choice_codes` {#fn--fmt-choice-codes-8546}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8546`

**Signature**

```python
def _fmt_choice_codes(items: set[str], limit: int=12) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `items` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `limit` | positional_or_keyword | No | `12` | `int` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _fmt_choice_codes(items: set[str], limit: int = 12) -> str:
        vals = sorted(items, key=lambda x: x.lower())
        if not vals:
            return "(none)"
        if len(vals) <= limit:
            return ", ".join(vals)
        return ", ".join(vals[:limit]) + f", ... (+{len(vals) - limit} more)"
    ```

### `_column_language` {#fn--column-language-8560}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8560`

**Signature**

```python
def _column_language(header: str) -> str:
```

**Returns:** `str`

**What it does:** Language code of a 'label::French (fr)'-style header, '' for non-language columns.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `header` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _column_language(header: str) -> str:
        """Language code of a 'label::French (fr)'-style header, '' for non-language columns."""
        h = str(header or "").strip()
        if "::" not in h:
            return ""
        m = _COLUMN_LANG_RE.search(h)
        return m.group(1).lower() if m else ""
    ```

### `_column_in_scope` {#fn--column-in-scope-8569}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8569`

**Signature**

```python
def _column_in_scope(header: str, languages_in_scope: list[str] | None) -> bool:
```

**Returns:** `bool`

**What it does:** False only for a language column whose language is not in languages_in_scope (empty = all).

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `header` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `languages_in_scope` | positional_or_keyword | Yes | `-` | `list[str] | None` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _column_in_scope(header: str, languages_in_scope: list[str] | None) -> bool:
        """False only for a language column whose language is not in languages_in_scope (empty = all)."""
        if not languages_in_scope:
            return True
        lang = _column_language(header)
        return not lang or lang in languages_in_scope
    ```

### `_sheet_scope_mask` {#fn--sheet-scope-mask-8577}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8577`

**Signature**

```python
def _sheet_scope_mask(ws, languages_in_scope: list[str] | None) -> list[bool]:
```

**Returns:** `list[bool]`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `languages_in_scope` | positional_or_keyword | Yes | `-` | `list[str] | None` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _sheet_scope_mask(ws, languages_in_scope: list[str] | None) -> list[bool]:
        hdr_row = next(ws.iter_rows(min_row=1, max_row=1, values_only=True), None)
        return [_column_in_scope(h, languages_in_scope) for h in (hdr_row or [])]
    ```

### `read_additional_info_keys` {#fn-read-additional-info-keys-8582}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8582`

**Signature**

```python
def read_additional_info_keys(country_path: str) -> set[str]:
```

**Returns:** `set[str]`

**What it does:** Every 'Original' key in the Additional information sheet, lowercased -- including rows with blank replacements.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `country_path` | positional_or_keyword | Yes | `-` | `str` | Filesystem path used for reading inputs or writing outputs. |

??? note "Function source"

    ```python
    def read_additional_info_keys(country_path: str) -> set[str]:
        """Every 'Original' key in the Additional information sheet, lowercased -- including rows with blank replacements."""
        try:
            wb = openpyxl.load_workbook(country_path, data_only=True, read_only=True)
            if "Additional information" not in wb.sheetnames:
                wb.close()
                return set()
            rows = list(wb["Additional information"].iter_rows(values_only=True))
            wb.close()
        except Exception:
            return set()
        if len(rows) < 2:
            return set()
        headers = [str(h).strip() if h is not None else "" for h in rows[1]]
        orig_idx = next((i for i, h in enumerate(headers) if _normalize_additional_info_header(h).startswith("original")), None)
        if orig_idx is None:
            return set()
        return {
            alias.lower()
            for row in rows[2:]
            if orig_idx < len(row) and row[orig_idx] is not None and str(row[orig_idx]).strip()
            for alias in _placeholder_aliases(str(row[orig_idx]).strip())
        }
    ```

### `build_unresolved_placeholder_issues` {#fn-build-unresolved-placeholder-issues-8607}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8607`

**Signature**

```python
def build_unresolved_placeholder_issues(unresolved_rows: list[dict], additional_info_keys: set[str], pairs_by_language: dict[str, dict[str, str]], severity: str='high') -> list[dict]:
```

**Returns:** `list[dict]`

**What it does:** One issue per (placeholder token, cause) instead of one per cell, listing

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `unresolved_rows` | positional_or_keyword | Yes | `-` | `list[dict]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `additional_info_keys` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `pairs_by_language` | positional_or_keyword | Yes | `-` | `dict[str, dict[str, str]]` | Language selector used for language-specific text columns. |
| `severity` | positional_or_keyword | No | `'high'` | `str` | Severity label used for final issue classification. |

??? note "Function source"

    ```python
    def build_unresolved_placeholder_issues(
        unresolved_rows: list[dict],
        additional_info_keys: set[str],
        pairs_by_language: dict[str, dict[str, str]],
        severity: str = "high",
    ) -> list[dict]:
        """
        One issue per (placeholder token, cause) instead of one per cell, listing
        the questions and columns affected. Cause, per cell language:
          - not_in_additional_info: no Original row matches the token
          - language_not_filled: the whole Replacement column of that language is empty (medium)
          - blank_replacement: the row exists but its Replacement for that language is blank
          - not_applied: a value exists but the token was not replaced (spelling/case variant)
        """
        tok_re = _re.compile(r"#[^#\n]+#")
        filled_langs = {lang for lang, pairs in (pairs_by_language or {}).items() if pairs}
        groups: dict[tuple[str, str], dict] = {}
        for rr in unresolved_rows:
            lang = rr.get("language", "")
            for token in dict.fromkeys(tok_re.findall(str(rr.get("full_text") or rr.get("token_text") or ""))):
                core = token.strip("#").strip()
                in_ai = bool(_placeholder_aliases(core) & {k for k in additional_info_keys}) or core.lower() in additional_info_keys
                if not in_ai:
                    cause = "not_in_additional_info"
                elif lang and lang not in filled_langs:
                    cause = "language_not_filled"
                elif lang and token in (pairs_by_language or {}).get(lang, {}):
                    cause = "not_applied"
                else:
                    cause = "blank_replacement"
                g = groups.setdefault((token, cause), {"qnames": [], "cells": [], "columns": [], "langs": [], "row": rr})
                label = (
                    f"{rr.get('list_name')}/{rr.get('option_name')}" if rr.get("sheet") == "choices" and rr.get("list_name")
                    else rr.get("q_name", "")
                )
                if label and label not in g["qnames"]:
                    g["qnames"].append(label)
                g["cells"].append(f"{rr.get('sheet')}!{rr.get('cell')}")
                col = str(rr.get("column") or "")
                if col and col not in g["columns"]:
                    g["columns"].append(col)
                if lang and lang not in g["langs"]:
                    g["langs"].append(lang)

        _reason = {
            "not_in_additional_info": "No matching 'Original' row in Additional information -- add the row, or align the token spelling with an existing key",
            "language_not_filled": "Replacement column for {langs} is empty for every key -- fill it, or leave the language out of languages_in_scope if it is not deployed",
            "blank_replacement": "Additional information row exists but its Replacement is blank for {langs} -- fill it (or drop the question/option using it)",
            "not_applied": "A replacement exists for {langs} but was not applied -- check spelling/case of the token vs the Original key",
        }
        out: list[dict] = []
        for (token, cause), g in sorted(groups.items(), key=lambda kv: (kv[0][1] == "language_not_filled", kv[0][0])):
            langs = ", ".join(l.upper() for l in g["langs"]) or "all languages"
            n_q = len(g["qnames"])
            out.append({
                "issue_type": "replacement_unresolved_placeholder",
                "q_name": ", ".join(g["qnames"]),
                "field": token,
                "current": (
                    f"{len(g['cells'])} cell(s) in {n_q} question/option(s); columns: {', '.join(g['columns']) or '-'}; "
                    f"cells: {', '.join(g['cells'][:12])}{' ...' if len(g['cells']) > 12 else ''}"
                ),
                "reference": _reason[cause].format(langs=langs),
                "severity": "medium" if cause == "language_not_filled" else severity,
                "excel_row": g["row"].get("excel_row") if len(g["cells"]) == 1 else None,
            })
        return out
    ```

### `_scan_unresolved_placeholders` {#fn--scan-unresolved-placeholders-8676}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8676`

**Signature**

```python
def _scan_unresolved_placeholders(wb, sheet_name: str, limit: int=5, languages_in_scope: list[str] | None=None) -> tuple[int, list[str]]:
```

**Returns:** `tuple[int, list[str]]`

**What it does:** Return (count, examples) of remaining #placeholder# tokens in a sheet (in-scope columns only).

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `sheet_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `limit` | positional_or_keyword | No | `5` | `int` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `languages_in_scope` | positional_or_keyword | No | `None` | `list[str] | None` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _scan_unresolved_placeholders(
        wb, sheet_name: str, limit: int = 5, languages_in_scope: list[str] | None = None,
    ) -> tuple[int, list[str]]:
        """Return (count, examples) of remaining #placeholder# tokens in a sheet (in-scope columns only)."""
        if sheet_name not in wb.sheetnames:
            return 0, []
        patt = _re.compile(r"#[^#]+#")
        ws = wb[sheet_name]
        scope = _sheet_scope_mask(ws, languages_in_scope)
        count = 0
        examples: list[str] = []
        for row in ws.iter_rows():
            for i, cell in enumerate(row):
                if i < len(scope) and not scope[i]:
                    continue
                v = cell.value
                if isinstance(v, str) and patt.search(v):
                    count += 1
                    if len(examples) < limit:
                        examples.append(f"{cell.coordinate}: {v[:90]}")
        return count, examples
    ```

### `_collect_unresolved_placeholder_cells` {#fn--collect-unresolved-placeholder-cells-8699}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8699`

**Signature**

```python
def _collect_unresolved_placeholder_cells(wb, languages_in_scope: list[str] | None=None) -> list[dict]:
```

**Returns:** `list[dict]`

**What it does:** Collect every unresolved #placeholder# cell from survey/choices with row context,

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `languages_in_scope` | positional_or_keyword | No | `None` | `list[str] | None` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _collect_unresolved_placeholder_cells(wb, languages_in_scope: list[str] | None = None) -> list[dict]:
        """
        Collect every unresolved #placeholder# cell from survey/choices with row context,
        skipping language columns outside languages_in_scope (empty = all).
        Returns rows with keys: sheet, cell, column, language, token_text, full_text,
        q_name, list_name, option_name, excel_row.
        """
        patt = _re.compile(r"#[^#]+#")
        out: list[dict] = []
        for sheet_name in ("survey", "choices"):
            if sheet_name not in wb.sheetnames:
                continue
            ws = wb[sheet_name]
            hdr_row = next(ws.iter_rows(min_row=1, max_row=1, values_only=True), None)
            headers = [str(h).strip() if h is not None else "" for h in (hdr_row or [])]
            col_idx = {h: i for i, h in enumerate(headers)}
            q_col = col_idx.get("name")
            list_col = col_idx.get("list_name")
            opt_col = col_idx.get("name") if sheet_name == "choices" else None

            for row in ws.iter_rows(min_row=2):
                vals = [c.value for c in row]
                q_name = str(vals[q_col]).strip() if q_col is not None and q_col < len(vals) and vals[q_col] is not None else ""
                list_name = str(vals[list_col]).strip() if list_col is not None and list_col < len(vals) and vals[list_col] is not None else ""
                opt_name = str(vals[opt_col]).strip() if opt_col is not None and opt_col < len(vals) and vals[opt_col] is not None else ""
                for i, cell in enumerate(row):
                    v = cell.value
                    header = headers[i] if i < len(headers) else ""
                    if not _column_in_scope(header, languages_in_scope):
                        continue
                    if isinstance(v, str) and patt.search(v):
                        out.append({
                            "sheet": sheet_name,
                            "cell": cell.coordinate,
                            "column": header,
                            "language": _column_language(header),
                            "token_text": v[:220],
                            "full_text": v,
                            "q_name": q_name,
                            "list_name": list_name,
                            "option_name": opt_name,
                            "excel_row": cell.row,
                        })
        return out
    ```

### `_scan_malformed_placeholder_syntax` {#fn--scan-malformed-placeholder-syntax-8745}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8745`

**Signature**

```python
def _scan_malformed_placeholder_syntax(wb, sheet_name: str, limit: int=5, languages_in_scope: list[str] | None=None) -> tuple[int, list[str]]:
```

**Returns:** `tuple[int, list[str]]`

**What it does:** Return (count, examples) of malformed placeholder/reference syntax in a sheet:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `sheet_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `limit` | positional_or_keyword | No | `5` | `int` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `languages_in_scope` | positional_or_keyword | No | `None` | `list[str] | None` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _scan_malformed_placeholder_syntax(
        wb, sheet_name: str, limit: int = 5, languages_in_scope: list[str] | None = None,
    ) -> tuple[int, list[str]]:
        """
        Return (count, examples) of malformed placeholder/reference syntax in a sheet:
          - malformed #...# tokens
          - malformed ${...} tokens
        """
        if sheet_name not in wb.sheetnames:
            return 0, []
        ws = wb[sheet_name]
        scope = _sheet_scope_mask(ws, languages_in_scope)
        count = 0
        examples: list[str] = []
        for row in ws.iter_rows():
            for i, cell in enumerate(row):
                if i < len(scope) and not scope[i]:
                    continue
                v = cell.value
                if not isinstance(v, str):
                    continue
                if _has_broken_hash_placeholder_token(v) or _has_malformed_kobo_ref_token(v):
                    count += 1
                    if len(examples) < limit:
                        examples.append(f"{sheet_name}!{cell.coordinate}: {v[:90]}")
        return count, examples
    ```

### `produce_validated_questionnaire` {#fn-produce-validated-questionnaire-8773}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8773`

**Signature**

```python
def produce_validated_questionnaire(cfg: dict, reference_survey: pl.DataFrame, replacement_pairs: dict, replacement_input_status: dict | None=None) -> tuple[str, dict, pl.DataFrame]:
```

**Returns:** `tuple[str, dict, pl.DataFrame]`

**What it does:** Build validated_questionnaire_kobo_<lang>_<iso3>_<date>.xlsx:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cfg` | positional_or_keyword | Yes | `-` | `dict` | Runtime configuration object for this validation run. |
| `reference_survey` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `replacement_pairs` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `replacement_input_status` | positional_or_keyword | No | `None` | `dict | None` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def produce_validated_questionnaire(
        cfg             : dict,
        reference_survey: pl.DataFrame,
        replacement_pairs: dict,
        replacement_input_status: dict | None = None,
    ) -> tuple[str, dict, pl.DataFrame]:
        """
        Build validated_questionnaire_kobo_<lang>_<iso3>_<date>.xlsx:
          1. Copy country questionnaire to output_dir
          2. Inject crop choices from 'Crop list' sheet
          3. Inject admin choices from AGOL
          4. Restore #placeholder# labels from template (then replace in step 5)
          5. Apply all #placeholder# replacements from Additional information sheet
        Returns (saved_file_path, replacement_status).
        """
        src  = cfg["questionnaire_path"]
        iso3 = cfg["iso3"]
        lang = cfg["language"]
        out  = Path(cfg.get("output_dir") or str(Path(src).parent))
        _round_kobo = _extract_round_token_kobo(Path(src).name)
        _rt_kobo = (f"_{_round_kobo}" if _round_kobo else "")
        dest = str(out / f"validated_questionnaire_kobo_{lang}_{iso3.upper()}{_rt_kobo}_{_date.today():%Y%m%d}.xlsx")

        replacement_status = {"rows": [], "notes": []}
        replacement_issue_rows: list[dict] = []
        _kobo_opt_local = cfg.get("kobo_options", {}) or {}
        _languages_in_scope = _normalize_languages_in_scope(cfg.get("languages_in_scope"))
        _include_admin3 = _as_bool(_kobo_opt_local.get("include_admin3", False), False)
        _skip_restore_and_replacement = _as_bool(_kobo_opt_local.get("skip_restore_and_replacement", False), False)
        _require_additional_info = _as_bool(_kobo_opt_local.get("require_additional_info", True), True)
        _require_crop_list = _as_bool(_kobo_opt_local.get("require_crop_list", True), True)

        def _add_row(check: str, status: str, details: str, severity: str):
            replacement_status["rows"].append({
                "check": check,
                "status": status,
                "details": details,
                "severity": severity,
            })

        def _add_issue(list_name: str, current: str, reference: str, severity: str = "high"):
            replacement_issue_rows.append({
                "issue_type": "replacement_crop_template_mismatch",
                "set_name": "",
                "Q Name": "",
                "list_name": list_name,
                "option_name": "",
                "field": "template crop code+label parity (order ignored)",
                "current": current,
                "reference": reference,
                "severity": severity,
                "excel_row": None,
            })

        def _add_issue_row(
            issue_type: str,
            field: str,
            current: str,
            reference: str,
            severity: str = "high",
            q_name: str = "",
            list_name: str = "",
            option_name: str = "",
            excel_row: int | None = None,
        ):
            replacement_issue_rows.append({
                "issue_type": issue_type,
                "set_name": "",
                "Q Name": q_name,
                "list_name": list_name,
                "option_name": option_name,
                "field": field,
                "current": current,
                "reference": reference,
                "severity": severity,
                "excel_row": excel_row,
            })

        print("Building validated questionnaire ...")
        print(f"  Source : {Path(src).name}")
        print(f"  Output : {dest}")

        _copy2(src, dest)
        wb = openpyxl.load_workbook(dest)
        _template_choices_path = ""
        if "run" in globals():
            _template_choices_path = str(run.get("template_path") or run.get("reference_path") or "")
        _template_choices_headers = _read_choices_headers_from_workbook(_template_choices_path) if _template_choices_path else []

        _crop_lists = ["crop", "crop2", "crop3"]
        _admin_lists = ["admin1", "admin2"] + (["admin3"] if _include_admin3 else [])

        _pre_status = replacement_input_status or {}
        _ai_status = _pre_status.get("additional_info", {}) if isinstance(_pre_status, dict) else {}
        _crop_probe = _pre_status.get("crop_list_probe", {}) if isinstance(_pre_status, dict) else {}

        if _skip_restore_and_replacement:
            _add_row(
                "Restore/replace process",
                "SKIP",
                "Skipped by config: kobo_options.skip_restore_and_replacement=true",
                "info",
            )
        else:
            if _require_additional_info:
                if not _ai_status.get("sheet_found"):
                    _det = _ai_status.get("message", "Additional information sheet not found")
                    _add_row("Additional information input", "FAIL", _det, "high")
                elif not _ai_status.get("headers_found"):
                    _det = _ai_status.get("message", "Original/Replacement headers not found")
                    _add_row("Additional information input", "FAIL", _det, "high")
                else:
                    _add_row(
                        "Additional information input",
                        _ai_status.get("status", "PASS"),
                        _ai_status.get("message", ""),
                        "pass" if _ai_status.get("status") == "PASS" else "medium",
                    )
                    for _mr in (_ai_status.get("missing_replacement_rows") or []):
                        _orig = str(_mr.get("original", "")).strip()
                        _erow = _mr.get("excel_row")
                        _add_issue_row(
                            "replacement_input_missing_additional_info",
                            "Additional information Replacement cell",
                            f"Original='{_orig}' has blank Replacement",
                            "Provide replacement value or remove unused placeholder key",
                            severity="medium",
                            q_name="",
                            list_name="",
                            option_name="",
                            excel_row=_erow if isinstance(_erow, int) else None,
                        )
            else:
                _add_row(
                    "Additional information input",
                    "SKIP",
                    "Requirement disabled (kobo_options.require_additional_info=false)",
                    "info",
                )

            if _require_crop_list:
                if not _crop_probe.get("sheet_found"):
                    _det = _crop_probe.get("message", "Crop list sheet not found")
                    _add_row("Crop list input", "FAIL", _det, "high")
                elif not _crop_probe.get("headers_found"):
                    _det = _crop_probe.get("message", "Crop list required headers missing")
                    _add_row("Crop list input", "FAIL", _det, "high")
                else:
                    _add_row(
                        "Crop list input",
                        _crop_probe.get("status", "PASS"),
                        _crop_probe.get("message", ""),
                        "pass" if _crop_probe.get("status") == "PASS" else "medium",
                    )
            else:
                _add_row(
                    "Crop list input",
                    "SKIP",
                    "Requirement disabled (kobo_options.require_crop_list=false)",
                    "info",
                )

        # -- 2. Crop choices --------------------------------------------------------
        if _skip_restore_and_replacement:
            crop_sel_status = {"status": "SKIP", "message": "Skipped by config"}
            crop_rows = {}
            _add_row(
                "Crop selection (top 10)",
                "SKIP",
                "Skipped by config: kobo_options.skip_restore_and_replacement=true",
                "info",
            )
        else:
            _, crop_sel_status = _read_crop_choices(src, lang)
            crop_rows_target, _ = _read_crop_choices(src, lang, strict_language=True)
            crop_rows_en, _ = _read_crop_choices(src, "en")
            crop_rows = _merge_crop_rows_for_multilang(crop_rows_en, crop_rows_target, lang)
            print(f"  Crop selection: {crop_sel_status['message']}")
            if crop_sel_status["status"] == "PASS":
                _add_row("Crop selection (top 10)", "PASS", crop_sel_status["message"], "pass")
            elif crop_sel_status["status"] == "WARN":
                _add_row("Crop selection (top 10)", "WARN", crop_sel_status["message"], "medium")
            else:
                _add_row("Crop selection (top 10)", "FAIL", crop_sel_status["message"], "high")

            if crop_rows:
                print(f"  Crops  : {sum(len(v) for v in crop_rows.values())} entries  "
                      f"({', '.join(crop_rows)})")

        # -- 3. Admin choices from AGOL ---------------------------------------------
        admin_rows: dict = {}
        agol_error = None
        admin3_error = None
        try:
            admin_rows = _fetch_admin_choices(iso3)
        except Exception as e:
            agol_error = str(e)
            print(f"  Warning: AGOL fetch failed -- admin choices not updated  ({e})")

        if _include_admin3 and not agol_error:
            try:
                admin_rows["admin3"] = _fetch_admin3_choices(iso3)
            except Exception as e:
                admin3_error = str(e)
                admin_rows["admin3"] = []
                print(f"  Warning: AGOL admin3 fetch failed -- admin3 choices not updated  ({e})")
        elif not _include_admin3:
            _add_row("AGOL fetch admin3", "SKIP", "Skipped by config (kobo_options.include_admin3=false)", "info")

        adm1_n = len(admin_rows.get("admin1", []))
        adm2_n = len(admin_rows.get("admin2", []))
        adm3_n = len(admin_rows.get("admin3", []))
        if agol_error:
            _add_row("AGOL fetch", "FAIL", f"Fetch failed: {agol_error}", "high")
        elif adm1_n > 0 and adm2_n > 0:
            _add_row("AGOL fetch", "PASS", f"admin1={adm1_n}, admin2={adm2_n}", "pass")
        else:
            _add_row("AGOL fetch", "WARN", f"admin1={adm1_n}, admin2={adm2_n}", "medium")
        if _include_admin3:
            if admin3_error:
                _add_row("AGOL fetch admin3", "FAIL", f"Fetch failed: {admin3_error}", "high")
            elif adm3_n > 0:
                _add_row("AGOL fetch admin3", "PASS", f"admin3={adm3_n}", "pass")
            else:
                _add_row("AGOL fetch admin3", "WARN", "admin3=0", "medium")

        country_rows = {**crop_rows, **admin_rows}
        _choices_rebuild_stats = _rebuild_choices_sheet(
            wb,
            country_rows,
            target_language=lang,
            template_headers=_template_choices_headers,
        )
        if _choices_rebuild_stats.get("used_template_headers"):
            _det = (
                f"Applied {_choices_rebuild_stats.get('template_header_count', 0)} template header(s)"
            )
            _extra_hdr = int(_choices_rebuild_stats.get("source_only_headers_appended", 0) or 0)
            if _extra_hdr > 0:
                _det += f"; appended {_extra_hdr} source-only header(s)"
            _add_row("Choices header alignment", "PASS", _det, "pass")
        else:
            _add_row(
                "Choices header alignment",
                "WARN",
                "Template choices headers unavailable; kept source header layout",
                "medium",
            )

        _extra_admin_rows = _choices_rebuild_stats.get("extra_admin_rows") or {}
        _extra_admin_total = int(_choices_rebuild_stats.get("extra_admin_rows_total", 0) or 0)
        if _extra_admin_total > 0:
            _parts = [f"{ln}={cnt}" for ln, cnt in sorted(_extra_admin_rows.items()) if cnt]
            _det = f"{_extra_admin_total} extra admin row(s) highlighted in yellow"
            if _parts:
                _det += f" ({', '.join(_parts)})"
            _add_row("Admin boundary additions", "WARN", _det, "medium")
            replacement_status["notes"].append(
                "Admin boundary updates: " + _det + "."
            )
        else:
            _add_row("Admin boundary additions", "PASS", "No extra admin rows beyond the original choices sheet", "pass")

        _admin_parent_stats = _validate_admin_parent_links_in_choices_sheet(wb)
        _admin_parent_issues = _admin_parent_stats.get("issues") or []
        _admin3_parent_issues = [
            rr for rr in _admin_parent_issues
            if _normalize_list_token(rr.get("list_name")) == "admin3"
        ]
        _admin3_parent_highlighted = 0
        _parent_header = _admin_parent_stats.get("parent_column") or "my_filter_admin"
        if not _admin_parent_stats.get("header_present"):
            _add_row(
                "Admin parent pcode integrity",
                "FAIL",
                "choices sheet does not contain a recognized admin parent column after header alignment",
                "high",
            )
        else:
            _checked_admin2 = int((_admin_parent_stats.get("checked") or {}).get("admin2", 0) or 0)
            _checked_admin3 = int((_admin_parent_stats.get("checked") or {}).get("admin3", 0) or 0)
            if not _admin_parent_issues:
                _add_row(
                    "Admin parent pcode integrity",
                    "PASS",
                    f"admin2 checked={_checked_admin2}; admin3 checked={_checked_admin3}",
                    "pass",
                )
            else:
                _examples = []
                for rr in _admin_parent_issues[:4]:
                    if rr.get("problem") == "missing":
                        _examples.append(f"{rr['list_name']}/{rr['code']}: missing parent")
                    else:
                        _examples.append(f"{rr['list_name']}/{rr['code']}: {rr['parent']} not in {rr['expected_parent_list']}")
                _det = (
                    f"{len(_admin_parent_issues)} invalid admin parent reference(s) "
                    f"(admin2 checked={_checked_admin2}; admin3 checked={_checked_admin3})"
                )
                if _examples:
                    _det += " | examples: " + "; ".join(_examples)
                _add_row("Admin parent pcode integrity", "FAIL", _det, "high")
                _missing_n = sum(1 for rr in _admin_parent_issues if rr.get("problem") == "missing")
                _not_found_n = len(_admin_parent_issues) - _missing_n
                _summary_current = (
                    f"{len(_admin_parent_issues)} invalid admin parent reference(s) in '{_parent_header}' "
                    f"(missing={_missing_n}, not found={_not_found_n}; "
                    f"admin2 checked={_checked_admin2}, admin3 checked={_checked_admin3})"
                )
                if _examples:
                    _summary_current += " | examples: " + "; ".join(_examples)
                _add_issue_row(
                    "replacement_admin_parent_mismatch",
                    _parent_header,
                    _summary_current,
                    "Use admin1 pcodes for admin2 rows and admin2 pcodes for admin3 rows in the validated choices output",
                    severity="high",
                    list_name="admin2/admin3",
                    option_name="",
                    excel_row=min(
                        (int(rr.get("excel_row")) for rr in _admin_parent_issues if isinstance(rr.get("excel_row"), int)),
                        default=None,
                    ),
                )
            _admin3_parent_highlighted = _highlight_admin_parent_issue_rows_in_choices_sheet(
                wb,
                _admin3_parent_issues,
                target_lists={"admin3"},
            )

        _admin3_parent_report = out / (
            f"admin3_parent_mismatches_kobo_{lang}_{iso3.upper()}{_rt_kobo}_{_date.today():%Y%m%d}.txt"
        )
        if _admin_parent_stats.get("header_present"):
            try:
                _write_admin_parent_mismatch_text_report(
                    _admin3_parent_report,
                    _admin_parent_issues,
                    label="admin3",
                )
                _report_name = _admin3_parent_report.name
                if _admin3_parent_issues:
                    _det = (
                        f"{len(_admin3_parent_issues)} admin3 mismatch row(s) exported to {_report_name}; "
                        f"{_admin3_parent_highlighted} row(s) highlighted in choices"
                    )
                    _add_row("Admin3 mismatch export", "WARN", _det, "medium")
                    replacement_status["notes"].append("Admin3 mismatch list: " + _report_name)
                else:
                    _add_row(
                        "Admin3 mismatch export",
                        "PASS",
                        f"No admin3 parent mismatches; wrote {_report_name}",
                        "pass",
                    )
                print(f"  Admin3 parent mismatch list: {_admin3_parent_report}")
            except Exception as e:
                _add_row("Admin3 mismatch export", "FAIL", f"Could not write mismatch list: {e}", "high")

        # Verify choices replacement counts in workbook
        if _skip_restore_and_replacement:
            for list_name in _crop_lists:
                _add_row(f"Choices replaced: {list_name}", "SKIP", "Skipped by config", "info")
        else:
            for list_name in _crop_lists:
                expected = len(crop_rows.get(list_name, []))
                actual = _count_choices_list_rows(wb, list_name)
                if expected > 0 and actual == expected:
                    _add_row(f"Choices replaced: {list_name}", "PASS", f"{actual} rows written", "pass")
                elif expected == 0:
                    _add_row(f"Choices replaced: {list_name}", "FAIL", "No rows prepared from Crop list", "high")
                else:
                    _add_row(f"Choices replaced: {list_name}", "FAIL", f"Expected {expected}, wrote {actual}", "high")

        for list_name in _admin_lists:
            expected = len(admin_rows.get(list_name, []))
            actual = _count_choices_list_rows(wb, list_name)
            if expected > 0 and actual == expected:
                _add_row(f"Choices replaced: {list_name}", "PASS", f"{actual} rows written", "pass")
            elif agol_error:
                _add_row(f"Choices replaced: {list_name}", "FAIL", "Skipped because AGOL fetch failed", "high")
            elif list_name == "admin3" and admin3_error:
                _add_row(f"Choices replaced: {list_name}", "FAIL", "Skipped because AGOL admin3 fetch failed", "high")
            elif expected == 0:
                _add_row(f"Choices replaced: {list_name}", "WARN", "No rows fetched from AGOL", "medium")
            else:
                _add_row(f"Choices replaced: {list_name}", "FAIL", f"Expected {expected}, wrote {actual}", "high")
        if not _include_admin3:
            _add_row("Choices replaced: admin3", "SKIP", "Skipped by config", "info")

        # -- 3b. Optional module skip from validated output -------------------------
        _skip_keys = set(globals().get("_skip_module_keys") or set())
        _skip_qnames = set(globals().get("_skip_module_qnames_for_validated_output") or set())
        _skip_choice_lists = set(globals().get("_skip_module_choice_lists_for_validated_output") or set())

        if _skip_keys or _skip_qnames:
            _survey_skip_stats = _strip_skipped_module_blocks_from_survey_sheet(
                wb,
                _skip_keys,
                _skip_qnames,
            )

            _protected_lists = {
                str(v).strip()
                for v in (cfg.get("kobo_options", {}).get("country_specific_list_names", []) or [])
                if str(v or "").strip()
            }
            _protected_lists.update(_crop_lists)
            _protected_lists.update({"admin1", "admin2"})
            if _include_admin3:
                _protected_lists.update({"admin3"})
            _protected_norm = {_normalize_list_token(v) for v in _protected_lists if _normalize_list_token(v)}

            _choice_lists_to_remove = {
                ln for ln in _skip_choice_lists
                if _normalize_list_token(ln) and _normalize_list_token(ln) not in _protected_norm
            }
            _choice_lists_protected = {
                ln for ln in _skip_choice_lists
                if _normalize_list_token(ln) and _normalize_list_token(ln) in _protected_norm
            }
            _removed_choice_rows = _remove_choices_lists_rows(wb, _choice_lists_to_remove)

            _removed_survey_rows = int(_survey_skip_stats.get("removed_rows", 0))
            _removed_modules = int(_survey_skip_stats.get("removed_module_blocks", 0))
            if _removed_survey_rows > 0 or _removed_choice_rows > 0:
                _det = (
                    f"removed module blocks={_removed_modules}; "
                    f"survey rows removed={_removed_survey_rows}; "
                    f"choices rows removed={_removed_choice_rows}"
                )
                if _choice_lists_to_remove:
                    _det += f"; choice lists removed={len(_choice_lists_to_remove)}"
                if _choice_lists_protected:
                    _det += (
                        f"; protected country lists kept={len(_choice_lists_protected)} "
                        f"({', '.join(sorted(_choice_lists_protected)[:8])}"
                    )
                    if len(_choice_lists_protected) > 8:
                        _det += ", ..."
                    _det += ")"
                _add_row("Module skip (validated output)", "PASS", _det, "pass")
                print(f"  Module skip applied: {_det}")
            else:
                _add_row(
                    "Module skip (validated output)",
                    "WARN",
                    "Configured, but no matching rows were removed in survey/choices",
                    "medium",
                )
                print("  Module skip configured, but no matching rows were removed.")

        # -- 4/5. Restore template placeholder-bearing cells + apply replacements ---
        #         Restore (step 4) always runs when not explicitly skipped: template
        #         #placeholder# cells are written back to the output so unresolved
        #         tokens surface even when no Additional information is available.
        #         Replacement (step 5) runs only when pairs were successfully loaded.
        _can_run_restore = not _skip_restore_and_replacement
        _can_run_replace = _can_run_restore and bool(replacement_pairs)

        if not _skip_restore_and_replacement and replacement_pairs:
            _add_row(
                "Placeholder replacement input pairs",
                "PASS",
                f"{len(replacement_pairs)} replacement token(s) loaded",
                "pass",
            )
        elif not _skip_restore_and_replacement:
            _sev = "high" if _require_additional_info else "medium"
            _st = "FAIL" if _require_additional_info else "WARN"
            _add_row(
                "Placeholder replacement input pairs",
                _st,
                "No replacement pairs loaded from Additional information",
                _sev,
            )

        if _can_run_restore:
            _tpl_restore_path = None
            if "run" in globals():
                _tpl_restore_path = run.get("template_path") or run.get("reference_path")
            if _tpl_restore_path:
                _replacement_pairs_for_restore = replacement_pairs
                if replacement_pairs_by_language:
                    _replacement_pairs_for_restore = {}
                    for _pairs in replacement_pairs_by_language.values():
                        _replacement_pairs_for_restore.update(_pairs or {})
                # Pass replacement_pairs only when we have pairs (filters restore to
                # known-replaceable tokens). Pass None when pairs are absent so ALL
                # template placeholder cells are restored, making them visible in output.
                _restore_stats = _restore_placeholder_tokens_from_template(
                    wb,
                    str(_tpl_restore_path),
                    replacement_pairs=_replacement_pairs_for_restore if _can_run_replace else None,
                )
                if _restore_stats.get("error"):
                    _add_row(
                        "Placeholder vanilla restore",
                        "FAIL",
                        str(_restore_stats.get("error")),
                        "high",
                    )
                else:
                    _n_s = int(_restore_stats.get("survey_cells_restored", 0))
                    _n_c = int(_restore_stats.get("choices_cells_restored", 0))
                    _tpl_s = int(_restore_stats.get("survey_template_placeholder_cells", 0))
                    _tpl_c = int(_restore_stats.get("choices_template_placeholder_cells", 0))
                    _skp_s = int(_restore_stats.get("survey_placeholder_cells_skipped_missing_replacement", 0))
                    _skp_c = int(_restore_stats.get("choices_placeholder_cells_skipped_missing_replacement", 0))
                    _van_s = int(_restore_stats.get("survey_cells_already_vanilla", 0))
                    _van_c = int(_restore_stats.get("choices_cells_already_vanilla", 0))
                    _miss_s = int(_restore_stats.get("survey_missing_key_rows", 0))
                    _miss_c = int(_restore_stats.get("choices_missing_key_rows", 0))
                    _det = (
                        f"Template placeholder cells survey={_tpl_s}, choices={_tpl_c}; "
                        f"restored survey={_n_s}, choices={_n_c}; "
                        f"skipped(no replacement) survey={_skp_s}, choices={_skp_c}; "
                        f"already-vanilla survey={_van_s}, choices={_van_c}; "
                        f"missing key rows survey={_miss_s}, choices={_miss_c}"
                    )

                    if (_miss_s + _miss_c) > 0:
                        _det += "; template rows absent from the questionnaire (removed by the country) need no restore"
                    if (_skp_s + _skp_c) > 0:
                        _sev = "medium"
                        _st = "WARN"
                    else:
                        _sev = "pass"
                        _st = "PASS"
                    _add_row(
                        "Placeholder vanilla restore",
                        _st,
                        _det,
                        _sev,
                    )

                    # Template rows carrying placeholders that the country dropped: nothing
                    # to restore. One info row per sheet; core removals are already
                    # reported in Question Changes.
                    _miss_q = [str(q) for q in (_restore_stats.get("survey_missing_qnames") or [])]
                    _miss_k = [str(k) for k in (_restore_stats.get("choices_missing_keys") or [])]
                    if _miss_q:
                        _add_issue_row(
                            "replacement_restore_missing_target_row",
                            "template survey rows",
                            f"{len(_miss_q)} template question(s) with placeholders are not in this questionnaire",
                            "Nothing to restore (question removed by the country); core removals are listed in Question Changes",
                            severity="info",
                            q_name=", ".join(_miss_q),
                        )
                    if _miss_k:
                        _add_issue_row(
                            "replacement_restore_missing_target_row",
                            "template choice rows",
                            f"{len(_miss_k)} template choice(s) with placeholders are not in this questionnaire: {', '.join(_miss_k)}",
                            "Nothing to restore (choice removed by the country)",
                            severity="info",
                        )
            else:
                _add_row(
                    "Placeholder vanilla restore",
                    "FAIL",
                    "Template path unavailable; cannot restore placeholder-bearing cells",
                    "high",
                )

            # -- 5. Apply #placeholder# -> actual values ----------------------------
            if _can_run_replace:
                _apply_replacements_to_wb(
                    wb,
                    replacement_pairs,
                    replacement_pairs_by_language=replacement_pairs_by_language,
                    target_language=run.get("language", "en"),
                )
                _add_row(
                    "Placeholder replacement",
                    "PASS",
                    f"Applied {len(replacement_pairs)} replacement pair(s) to survey and choices sheets",
                    "pass",
                )
            else:
                _add_row(
                    "Placeholder replacement",
                    "FAIL" if _require_additional_info else "WARN",
                    "No replacement pairs available; placeholders restored from template but not replaced",
                    "high" if _require_additional_info else "medium",
                )
        else:
            _add_row(
                "Placeholder restore/replacement",
                "SKIP",
                "Skipped by config: kobo_options.skip_restore_and_replacement=true",
                "info",
            )

        # Explicit choices-level replacement integrity check
        _ch_unresolved, _ch_examples = _scan_unresolved_placeholders(wb, "choices", languages_in_scope=_languages_in_scope)
        if _ch_unresolved == 0:
            _add_row(
                "Placeholder replacement in choices",
                "PASS",
                "No unresolved #placeholder# token remains in choices sheet",
                "pass",
            )
        else:
            _det = f"{_ch_unresolved} unresolved #placeholder# token(s) in choices"
            if _ch_examples:
                _det += " | examples: " + " ; ".join(_ch_examples)
            if _skip_restore_and_replacement:
                _add_row("Placeholder replacement in choices", "WARN", _det, "medium")
            else:
                _add_row("Placeholder replacement in choices", "FAIL", _det, "high")

        _unresolved_rows = _collect_unresolved_placeholder_cells(wb, languages_in_scope=_languages_in_scope)
        if _unresolved_rows:
            _sev = "medium" if _skip_restore_and_replacement else "high"
            for _iss in build_unresolved_placeholder_issues(
                _unresolved_rows,
                read_additional_info_keys(src),
                globals().get("replacement_pairs_by_language") or {},
                severity=_sev,
            ):
                _add_issue_row(
                    _iss["issue_type"],
                    _iss["field"],
                    _iss["current"],
                    _iss["reference"],
                    severity=_iss["severity"],
                    q_name=_iss["q_name"],
                    excel_row=_iss["excel_row"],
                )

        # Malformed placeholder/reference syntax check on final workbook text.
        _malformed_total = 0
        _malformed_examples: list[str] = []
        for _sheet_name in ("survey", "choices"):
            _cnt, _ex = _scan_malformed_placeholder_syntax(wb, _sheet_name, limit=3, languages_in_scope=_languages_in_scope)
            _malformed_total += _cnt
            if _ex:
                _malformed_examples.extend(_ex)
        if _malformed_total == 0:
            _add_row(
                "Placeholder/reference syntax integrity",
                "PASS",
                "No malformed #...# or ${...} token detected in survey/choices",
                "pass",
            )
        else:
            _det = f"{_malformed_total} malformed token cell(s) in survey/choices"
            if _malformed_examples:
                _det += " | examples: " + " ; ".join(_malformed_examples[:5])
            _add_row("Placeholder/reference syntax integrity", "FAIL", _det, "high")

        _lang_norm = str(lang or "").strip().lower()
        if _skip_restore_and_replacement:
            _add_row("Crop label placement (EN)", "SKIP", "Skipped by config", "info")
            if _lang_norm != "en":
                _add_row(f"Crop label placement ({_lang_norm.upper()})", "SKIP", "Skipped by config", "info")
        else:
            # Crop label placement integrity across language columns.
            _en_col = LANG_LABEL_COL.get("en", "label::English (en)")
            _total_en, _blank_en = _count_blank_labels_for_lists(wb, _crop_lists, _en_col)
            if _total_en == 0:
                _add_row(
                    "Crop label placement (EN)",
                    "WARN",
                    f"Column '{_en_col}' not found or no crop rows present",
                    "medium",
                )
            elif _blank_en == 0:
                _add_row("Crop label placement (EN)", "PASS", f"All {_total_en} crop rows have EN labels", "pass")
            else:
                _add_row(
                    "Crop label placement (EN)",
                    "FAIL",
                    f"{_blank_en}/{_total_en} crop rows have blank EN labels",
                    "high",
                )

            if _lang_norm != "en":
                _target_col = LANG_LABEL_COL.get(_lang_norm, f"label::{lang}")
                _total_tgt, _blank_tgt = _count_blank_labels_for_lists(wb, _crop_lists, _target_col)
                if _total_tgt == 0:
                    _add_row(
                        f"Crop label placement ({_lang_norm.upper()})",
                        "WARN",
                        f"Column '{_target_col}' not found or no crop rows present",
                        "medium",
                    )
                elif _blank_tgt == 0:
                    _add_row(
                        f"Crop label placement ({_lang_norm.upper()})",
                        "PASS",
                        f"All {_total_tgt} crop rows have {_lang_norm.upper()} labels",
                        "pass",
                    )
                else:
                    _add_row(
                        f"Crop label placement ({_lang_norm.upper()})",
                        "FAIL",
                        f"{_blank_tgt}/{_total_tgt} crop rows have blank {_lang_norm.upper()} labels",
                        "high",
                    )

        wb.save(dest)

        # -- 6. Crop parity vs template baseline -----------------------------------
        if _skip_restore_and_replacement:
            _add_row("Crop template parity", "SKIP", "Skipped by config", "info")
        else:
            _tmpl_path = None
            if "run" in globals():
                _tmpl_path = run.get("template_path") or run.get("reference_path")
            if not _tmpl_path:
                _add_row(
                    "Crop template parity",
                    "FAIL",
                    "Template path is unavailable; cannot verify crop code+label parity",
                    "high",
                )
                for _ln in _crop_lists:
                    _add_issue(
                        _ln,
                        "Parity check unavailable (template path missing)",
                        "Template crop baseline not accessible",
                        "high",
                    )
            else:
                try:
                    _lang_candidates = ["en"]
                    if _lang_norm and _lang_norm not in _lang_candidates:
                        _lang_candidates.append(_lang_norm)
                    _parity_langs = [
                        _lc
                        for _lc in _lang_candidates
                        if _choices_has_language_col(dest, _lc) and _crop_list_has_language_col(str(_tmpl_path), _lc)
                    ]

                    if _parity_langs:
                        for _plang in _parity_langs:
                            _actual_choices = read_kobo_choices(dest, _plang)
                            _template_crop_rows, _template_crop_status = _read_crop_choices(
                                str(_tmpl_path),
                                _plang,
                                strict_language=True,
                            )
                            if not _template_crop_rows:
                                raise ValueError(
                                    f"Template Crop list baseline is unavailable for language '{_plang}' "
                                    f"({_template_crop_status.get('message', 'unknown reason')})"
                                )
                            _actual_map = _choice_pair_set_by_list(_actual_choices, _crop_lists)
                            _template_map = _choice_pair_set_from_rows(_template_crop_rows, _crop_lists)

                            _tag = _plang.upper()
                            for _ln in _crop_lists:
                                _actual_set = _actual_map.get(_ln, set())
                                _template_set = _template_map.get(_ln, set())
                                _missing = _template_set - _actual_set
                                _extra = _actual_set - _template_set
                                if _missing or _extra:
                                    _det_parts = []
                                    if _missing:
                                        _det_parts.append(f"missing={len(_missing)} ({_fmt_choice_pairs(_missing, limit=8)})")
                                    if _extra:
                                        _det_parts.append(f"extra={len(_extra)} ({_fmt_choice_pairs(_extra, limit=8)})")
                                    _det = "; ".join(_det_parts)
                                    _add_row(f"Crop template parity ({_tag}): {_ln}", "FAIL", _det, "high")
                                    _add_issue(
                                        _ln,
                                        f"[{_tag}] extra in current: {_fmt_choice_pairs(_extra, limit=12)}",
                                        f"[{_tag}] missing vs template: {_fmt_choice_pairs(_missing, limit=12)}",
                                        "high",
                                    )
                                else:
                                    _add_row(
                                        f"Crop template parity ({_tag}): {_ln}",
                                        "PASS",
                                        f"All {_ln} code+label pairs match template baseline (order ignored)",
                                        "pass",
                                    )
                    else:
                        _add_row(
                            "Crop template parity language scope",
                            "WARN",
                            "No shared label column between choices and template Crop list; using code-only parity",
                            "medium",
                        )
                        _actual_choices = read_kobo_choices(dest, "en")
                        _template_crop_rows, _template_crop_status = _read_crop_choices(str(_tmpl_path), "en")
                        if not _template_crop_rows:
                            raise ValueError(
                                "Template Crop list baseline is unavailable "
                                f"({_template_crop_status.get('message', 'unknown reason')})"
                            )
                        _actual_codes = _choice_code_set_by_list(_actual_choices, _crop_lists)
                        _template_codes = _choice_code_set_from_rows(_template_crop_rows, _crop_lists)
                        for _ln in _crop_lists:
                            _actual_set = _actual_codes.get(_ln, set())
                            _template_set = _template_codes.get(_ln, set())
                            _missing = _template_set - _actual_set
                            _extra = _actual_set - _template_set
                            if _missing or _extra:
                                _det_parts = []
                                if _missing:
                                    _det_parts.append(f"missing={len(_missing)} ({_fmt_choice_codes(_missing, limit=8)})")
                                if _extra:
                                    _det_parts.append(f"extra={len(_extra)} ({_fmt_choice_codes(_extra, limit=8)})")
                                _det = "; ".join(_det_parts)
                                _add_row(f"Crop template parity (codes): {_ln}", "FAIL", _det, "high")
                                _add_issue(
                                    _ln,
                                    f"extra codes in current: {_fmt_choice_codes(_extra, limit=12)}",
                                    f"missing codes vs template: {_fmt_choice_codes(_missing, limit=12)}",
                                    "high",
                                )
                            else:
                                _add_row(
                                    f"Crop template parity (codes): {_ln}",
                                    "PASS",
                                    f"All {_ln} crop codes match template baseline",
                                    "pass",
                                )
                except Exception as e:
                    _add_row("Crop template parity", "FAIL", f"Comparison failed: {e}", "high")
                    for _ln in _crop_lists:
                        _add_issue(
                            _ln,
                            f"Parity check failed: {e}",
                            "Template crop baseline comparison could not be completed",
                            "high",
                        )

        print(f"  Saved  : {dest}")

        print("  Replacement checks:")
        for rr in replacement_status["rows"]:
            print(f"    - {rr['check']}: {rr['status']}  ({rr['details']})")

        if replacement_issue_rows:
            _replacement_issues_df = pl.DataFrame(replacement_issue_rows)
        else:
            _replacement_issues_df = pl.DataFrame(schema={
                "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
                "list_name": pl.Utf8, "option_name": pl.Utf8, "field": pl.Utf8,
                "current": pl.Utf8, "reference": pl.Utf8, "severity": pl.Utf8,
                "excel_row": pl.Int64,
            })
        return dest, replacement_status, _replacement_issues_df
    ```

### `produce_validated_questionnaire._add_row` {#fn--add-row-8805}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8805`

**Signature**

```python
def _add_row(check: str, status: str, details: str, severity: str):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `check` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `status` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `details` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `severity` | positional_or_keyword | Yes | `-` | `str` | Severity label used for final issue classification. |

??? note "Function source"

    ```python
    def _add_row(check: str, status: str, details: str, severity: str):
            replacement_status["rows"].append({
                "check": check,
                "status": status,
                "details": details,
                "severity": severity,
            })
    ```

### `produce_validated_questionnaire._add_issue` {#fn--add-issue-8813}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8813`

**Signature**

```python
def _add_issue(list_name: str, current: str, reference: str, severity: str='high'):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `list_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `current` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `severity` | positional_or_keyword | No | `'high'` | `str` | Severity label used for final issue classification. |

??? note "Function source"

    ```python
    def _add_issue(list_name: str, current: str, reference: str, severity: str = "high"):
            replacement_issue_rows.append({
                "issue_type": "replacement_crop_template_mismatch",
                "set_name": "",
                "Q Name": "",
                "list_name": list_name,
                "option_name": "",
                "field": "template crop code+label parity (order ignored)",
                "current": current,
                "reference": reference,
                "severity": severity,
                "excel_row": None,
            })
    ```

### `produce_validated_questionnaire._add_issue_row` {#fn--add-issue-row-8827}

**Pipeline stage:** `Step 12 -- Validated questionnaire output`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/kobo_validator.py:8827`

**Signature**

```python
def _add_issue_row(issue_type: str, field: str, current: str, reference: str, severity: str='high', q_name: str='', list_name: str='', option_name: str='', excel_row: int | None=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 12 -- Validated questionnaire output` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `issue_type` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `field` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `current` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `reference` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `severity` | positional_or_keyword | No | `'high'` | `str` | Severity label used for final issue classification. |
| `q_name` | positional_or_keyword | No | `''` | `str` | Question identifier used to join or compare records. |
| `list_name` | positional_or_keyword | No | `''` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `option_name` | positional_or_keyword | No | `''` | `str` | Input used by the `Step 12 -- Validated questionnaire output` stage. |
| `excel_row` | positional_or_keyword | No | `None` | `int | None` | Input used by the `Step 12 -- Validated questionnaire output` stage. |

??? note "Function source"

    ```python
    def _add_issue_row(
            issue_type: str,
            field: str,
            current: str,
            reference: str,
            severity: str = "high",
            q_name: str = "",
            list_name: str = "",
            option_name: str = "",
            excel_row: int | None = None,
        ):
            replacement_issue_rows.append({
                "issue_type": issue_type,
                "set_name": "",
                "Q Name": q_name,
                "list_name": list_name,
                "option_name": option_name,
                "field": field,
                "current": current,
                "reference": reference,
                "severity": severity,
                "excel_row": excel_row,
            })
    ```
