# GeoPoll Validator (`C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py`)

This page is organized by the validator pipeline stages used in the script.
Use the stage map to navigate quickly, then open each function spec for parameters and full source.

Total functions documented: **212**

## Pipeline Function Map

### 1. Runtime and logger helpers

- [`_NullOutput.write`](#fn-write-17)
- [`_NullOutput.flush`](#fn-flush-18)
- [`_NullOutput.fileno`](#fn-fileno-19)
- [`_banner`](#fn--banner-25)
- [`_info`](#fn--info-37)
- [`_step`](#fn--step-41)
- [`_summary`](#fn--summary-50)

### 2. Step 1 Configuration

- [`_load_effective_config`](#fn--load-effective-config-139)
- [`_reference_scope_label`](#fn--reference-scope-label-204)
- [`_not_in_reference_text`](#fn--not-in-reference-text-211)

### 3. Step 2 Reference file resolution

- [`_normalize_header_name`](#fn--normalize-header-name-242)
- [`_header_tokens`](#fn--header-tokens-247)
- [`_is_language_candidate_header`](#fn--is-language-candidate-header-252)
- [`resolve_language_column`](#fn-resolve-language-column-264)
- [`detect_language_from_filename`](#fn-detect-language-from-filename-317)
- [`choose_target_language`](#fn-choose-target-language-324)
- [`extract_date_from_name`](#fn-extract-date-from-name-364)
- [`find_latest_template`](#fn-find-latest-template-373)
- [`resolve_reference_file`](#fn-resolve-reference-file-392)
- [`load_critical_sets`](#fn-load-critical-sets-403)
- [`prepare_run`](#fn-prepare-run-439)
- [`_write_config_snapshot_geopoll`](#fn--write-config-snapshot-geopoll-487)

### 4. Step 3 Reading and normalising the survey sheet

- [`_resolve_column_by_aliases`](#fn--resolve-column-by-aliases-616)
- [`_canonical_column_from_header`](#fn--canonical-column-from-header-624)
- [`_as_text_cell`](#fn--as-text-cell-633)
- [`_load_workbook_readonly`](#fn--load-workbook-readonly-646)
- [`_close_workbook`](#fn--close-workbook-677)
- [`read_survey_sheet`](#fn-read-survey-sheet-693)
- [`build_questions_df`](#fn-build-questions-df-776)
- [`_normalize_module_token`](#fn--normalize-module-token-829)
- [`_is_geopoll_module_row`](#fn--is-geopoll-module-row-835)
- [`split_geopoll_questions_and_modules`](#fn-split-geopoll-questions-and-modules-848)
- [`validate_module_column_integrity`](#fn-validate-module-column-integrity-902)
- [`_filter_questions_by_module_keys`](#fn--filter-questions-by-module-keys-938)
- [`_filter_module_rows_by_keys`](#fn--filter-module-rows-by-keys-951)
- [`_resolve_module_keys_from_tokens`](#fn--resolve-module-keys-from-tokens-957)
- [`_module_display_map`](#fn--module-display-map-991)
- [`_dedupe_keep_order`](#fn--dedupe-keep-order-1009)
- [`_format_module_scope_for_display`](#fn--format-module-scope-for-display-1024)
- [`_qnames_for_module_keys`](#fn--qnames-for-module-keys-1036)

### 5. Step 4 Exploding answer options

- [`_normalize_q_type`](#fn--normalize-q-type-1067)
- [`is_option_bearing_qtype`](#fn-is-option-bearing-qtype-1074)
- [`parse_options`](#fn-parse-options-1099)
- [`extract_question_stem`](#fn-extract-question-stem-1122)
- [`_split_stem_and_options`](#fn--split-stem-and-options-1134)
- [`explode_options`](#fn-explode-options-1148)
- [`parse_codes_cell`](#fn-parse-codes-cell-1196)
- [`explode_codes`](#fn-explode-codes-1214)
- [`_normalize_placeholder_token`](#fn--normalize-placeholder-token-1293)
- [`_is_crop_placeholder_token`](#fn--is-crop-placeholder-token-1302)
- [`_contains_crop_marker_text`](#fn--contains-crop-marker-text-1309)
- [`_clean_header`](#fn--clean-header-1316)
- [`_find_column`](#fn--find-column-1320)
- [`read_generic_sheet`](#fn-read-generic-sheet-1329)
- [`read_additional_information`](#fn-read-additional-information-1368)
- [`read_crop_list`](#fn-read-crop-list-1372)
- [`has_placeholder`](#fn-has-placeholder-1376)
- [`build_placeholder_restore_map`](#fn-build-placeholder-restore-map-1383)
- [`restore_placeholder_cells`](#fn-restore-placeholder-cells-1428)
- [`_normalize_placeholder_key`](#fn--normalize-placeholder-key-1483)
- [`_placeholder_lookup_aliases`](#fn--placeholder-lookup-aliases-1499)
- [`_build_placeholder_index`](#fn--build-placeholder-index-1526)
- [`_lookup_placeholder_replacement`](#fn--lookup-placeholder-replacement-1536)
- [`_language_code_for_text_column`](#fn--language-code-for-text-column-1545)
- [`_placeholder_token_explicit_lang`](#fn--placeholder-token-explicit-lang-1567)
- [`analyze_additional_info_substitutions`](#fn-analyze-additional-info-substitutions-1576)
- [`build_additional_info_replacements`](#fn-build-additional-info-replacements-1631)
- [`build_additional_info_replacements_by_language`](#fn-build-additional-info-replacements-by-language-1645)
- [`apply_text_replacements`](#fn-apply-text-replacements-1694)
- [`apply_text_replacements._lang_map`](#fn--lang-map-1708)
- [`apply_placeholder_conversions`](#fn-apply-placeholder-conversions-1744)
- [`extract_crop_metadata`](#fn-extract-crop-metadata-1785)
- [`find_crop_placeholder_questions`](#fn-find-crop-placeholder-questions-1810)
- [`_is_selected_crop_value`](#fn--is-selected-crop-value-1825)
- [`_build_sorted_crop_entries`](#fn--build-sorted-crop-entries-1829)
- [`build_crop_option_block`](#fn-build-crop-option-block-1856)
- [`build_crop_code_block`](#fn-build-crop-code-block-1871)
- [`rebuild_crop_questions_for_deployed_form`](#fn-rebuild-crop-questions-for-deployed-form-1886)

### 6. Step 6 Normalisation helpers

- [`normalize_text_expr`](#fn-normalize-text-expr-2178)
- [`normalize_code_token_expr`](#fn-normalize-code-token-expr-2197)
- [`normalize_mandatory_expr`](#fn-normalize-mandatory-expr-2209)

### 7. Step 7 Comparison and validation functions

- [`_normalize_skip_text`](#fn--normalize-skip-text-2244)
- [`_parse_skip_option_codes`](#fn--parse-skip-option-codes-2249)
- [`_extract_referenced_qnames`](#fn--extract-referenced-qnames-2298)
- [`_extract_qname_tokens`](#fn--extract-qname-tokens-2349)
- [`_extract_qname_like`](#fn--extract-qname-like-2354)
- [`_extract_codes_from_numeric_spec`](#fn--extract-codes-from-numeric-spec-2364)
- [`_extract_condition_codes`](#fn--extract-condition-codes-2397)
- [`_extract_skip_codes_for_target`](#fn--extract-skip-codes-for-target-2414)
- [`_extract_skip_codes_for_target._codes_from_spec`](#fn--codes-from-spec-2423)
- [`_parse_default_skip_rules`](#fn--parse-default-skip-rules-2458)
- [`_semantic_skip_signature`](#fn--semantic-skip-signature-2531)
- [`_skip_signatures_equivalent`](#fn--skip-signatures-equivalent-2564)
- [`_skip_signatures_equivalent._group`](#fn--group-2570)
- [`_check_skip_consistency`](#fn--check-skip-consistency-2594)
- [`validate_skip_patterns`](#fn-validate-skip-patterns-2721)

### 8. Step 8 Issue unifiers

- [`make_presence_issues`](#fn-make-presence-issues-2930)
- [`make_mandatory_issues`](#fn-make-mandatory-issues-3045)
- [`make_option_issues`](#fn-make-option-issues-3059)
- [`make_option_presence_issues`](#fn-make-option-presence-issues-3077)
- [`build_option_changes_view`](#fn-build-option-changes-view-3098)
- [`build_option_changes_view._scope_view`](#fn--scope-view-3118)
- [`collapse_removed_option_with_cascading_drift`](#fn-collapse-removed-option-with-cascading-drift-3220)
- [`collapse_removed_option_with_cascading_drift._norm_label`](#fn--norm-label-3243)
- [`collapse_removed_option_with_cascading_drift._infer_drift_from_lookups`](#fn--infer-drift-from-lookups-3248)
- [`_join_limited_tokens`](#fn--join-limited-tokens-3338)
- [`_option_code_sort_key`](#fn--option-code-sort-key-3354)
- [`_format_option_entries`](#fn--format-option-entries-3361)
- [`_build_option_lookup_by_qname`](#fn--build-option-lookup-by-qname-3393)
- [`_format_code_entries`](#fn--format-code-entries-3418)
- [`_build_codes_lookup_by_qname`](#fn--build-codes-lookup-by-qname-3442)
- [`enrich_codes_issue_lists`](#fn-enrich-codes-issue-lists-3476)
- [`enrich_codes_issue_lists._norm_pair`](#fn--norm-pair-3503)
- [`enrich_codes_issue_lists._format_code_entries_marked`](#fn--format-code-entries-marked-3506)
- [`_extract_option_codes_from_field`](#fn--extract-option-codes-from-field-3594)
- [`_combine_lang_scope`](#fn--combine-lang-scope-3611)
- [`_option_scope_flags`](#fn--option-scope-flags-3636)
- [`_option_label_delta_tokens`](#fn--option-label-delta-tokens-3646)
- [`merge_added_removed_option_rows`](#fn-merge-added-removed-option-rows-3662)
- [`collapse_option_issue_rows_by_qname`](#fn-collapse-option-issue-rows-by-qname-3776)
- [`collapse_option_issue_rows_by_qname._norm_label`](#fn--norm-label-3804)
- [`collapse_option_issue_rows_by_qname._delta_by_label`](#fn--delta-by-label-3809)
- [`collapse_option_issue_rows_by_qname._common_label_code_shift`](#fn--common-label-code-shift-3826)
- [`collapse_option_issue_rows_by_qname._token_set`](#fn--token-set-3840)
- [`collapse_option_issue_rows_by_qname._is_hard_replacement`](#fn--is-hard-replacement-3843)

### 9. Step 9 Run the full pipeline

- [`compare_question_presence`](#fn-compare-question-presence-4048)
- [`validate_module_presence`](#fn-validate-module-presence-4072)
- [`validate_module_presence._to_map`](#fn--to-map-4088)
- [`_attach_module_column_to_issues`](#fn--attach-module-column-to-issues-4139)
- [`_attach_module_column_to_issues._part`](#fn--part-4150)
- [`compare_mandatory`](#fn-compare-mandatory-4188)
- [`_mandatory_cat_expr`](#fn--mandatory-cat-expr-4263)
- [`_normalize_qtype_value`](#fn--normalize-qtype-value-4274)
- [`_qtype_mode`](#fn--qtype-mode-4288)
- [`_is_known_qtype_value`](#fn--is-known-qtype-value-4312)
- [`_qtype_change_severity`](#fn--qtype-change-severity-4327)
- [`compare_qtype_changes`](#fn-compare-qtype-changes-4383)
- [`compare_legacy_text_field_changes`](#fn-compare-legacy-text-field-changes-4485)
- [`validate_conditional_removed_for_mandatory`](#fn-validate-conditional-removed-for-mandatory-4547)
- [`compare_question_labels_single`](#fn-compare-question-labels-single-4601)
- [`build_question_changes_view`](#fn-build-question-changes-view-4667)
- [`build_question_changes_view._scope_view`](#fn--scope-view-4711)
- [`compare_option_labels_single`](#fn-compare-option-labels-single-4796)
- [`compare_option_presence_single`](#fn-compare-option-presence-single-4822)
- [`compare_option_code_renumber_single`](#fn-compare-option-code-renumber-single-4859)
- [`compare_codes_presence_single`](#fn-compare-codes-presence-single-4923)
- [`compare_codes_token_mismatch_single`](#fn-compare-codes-token-mismatch-single-4955)
- [`compare_codes_renumber_single`](#fn-compare-codes-renumber-single-5007)
- [`build_codes_changes_view`](#fn-build-codes-changes-view-5066)
- [`apply_codes_severity_by_mandatory`](#fn-apply-codes-severity-by-mandatory-5141)
- [`collapse_codes_issue_rows_by_qname`](#fn-collapse-codes-issue-rows-by-qname-5176)
- [`collapse_codes_issue_rows_by_qname._uniq`](#fn--uniq-5201)
- [`build_codes_not_comparable_rows`](#fn-build-codes-not-comparable-rows-5319)
- [`build_codes_option_count_mismatch_rows`](#fn-build-codes-option-count-mismatch-rows-5378)
- [`build_codes_option_count_mismatch_rows._parse_int_codes`](#fn--parse-int-codes-5400)
- [`build_codes_option_count_mismatch_rows._formatted_codes_with_option_alignment`](#fn--formatted-codes-with-option-alignment-5408)
- [`validate_critical_sets`](#fn-validate-critical-sets-5537)
- [`validate_critical_sets._wealth_optional_variant`](#fn--wealth-optional-variant-5564)
- [`validate_prefix_counts`](#fn-validate-prefix-counts-5624)
- [`validate_crop_harvest`](#fn-validate-crop-harvest-5665)
- [`validate_authoring_consistency`](#fn-validate-authoring-consistency-5712)
- [`_tick`](#fn--tick-5776)

### 10. Step 10 Export to Excel

- [`_header_row`](#fn--header-row-6447)
- [`_section_header`](#fn--section-header-6454)
- [`_data_row`](#fn--data-row-6461)
- [`_autofit`](#fn--autofit-6470)
- [`_action_for_issue_type`](#fn--action-for-issue-type-6531)
- [`_optional_counterparts_for_missing_skip_targets`](#fn--optional-counterparts-for-missing-skip-targets-6536)
- [`_action_for_issue_row`](#fn--action-for-issue-row-6570)
- [`_issues_col_map`](#fn--issues-col-map-6582)
- [`_issues_table`](#fn--issues-table-6605)
- [`_tokenize_for_word_diff`](#fn--tokenize-for-word-diff-6660)
- [`_coalesce_segments`](#fn--coalesce-segments-6671)
- [`_build_diff_segments`](#fn--build-diff-segments-6683)
- [`_set_rich_text`](#fn--set-rich-text-6702)
- [`_set_rich_text_with_bold_tokens`](#fn--set-rich-text-with-bold-tokens-6718)
- [`_apply_inline_diff_for_issue`](#fn--apply-inline-diff-for-issue-6762)
- [`_apply_inline_diff_for_issue._match_issue`](#fn--match-issue-6771)
- [`_apply_option_detail_highlights`](#fn--apply-option-detail-highlights-6801)
- [`_apply_codes_alignment_marker_highlights`](#fn--apply-codes-alignment-marker-highlights-6839)
- [`_set_status`](#fn--set-status-6882)
- [`_cat_counts`](#fn--cat-counts-6916)
- [`_extract_round_token`](#fn--extract-round-token-6924)
- [`_extract_iso3_token`](#fn--extract-iso3-token-6939)
- [`_reference_descriptor`](#fn--reference-descriptor-6967)
- [`_write_category_breakdown_block`](#fn--write-category-breakdown-block-6987)
- [`write_summary_sheet`](#fn-write-summary-sheet-7061)
- [`write_structure_skip_sheet`](#fn-write-structure-skip-sheet-7262)
- [`write_structure_skip_sheet._sorted`](#fn--sorted-7266)
- [`write_replacement_issues_sheet`](#fn-write-replacement-issues-sheet-7303)
- [`write_critical_sets_sheet`](#fn-write-critical-sets-sheet-7329)
- [`write_question_changes_sheet`](#fn-write-question-changes-sheet-7357)
- [`write_option_changes_sheet`](#fn-write-option-changes-sheet-7412)
- [`export_validation_report`](#fn-export-validation-report-7490)
- [`_resolve_survey_sheet`](#fn--resolve-survey-sheet-7513)
- [`_sheet_header_map`](#fn--sheet-header-map-7520)
- [`_count_selected_crops`](#fn--count-selected-crops-7534)
- [`_placeholder_scan_columns`](#fn--placeholder-scan-columns-7548)
- [`_extract_placeholder_tokens`](#fn--extract-placeholder-tokens-7555)
- [`_has_broken_placeholder_token`](#fn--has-broken-placeholder-token-7559)
- [`_count_unresolved_placeholders`](#fn--count-unresolved-placeholders-7567)
- [`_selected_crop_labels`](#fn--selected-crop-labels-7580)
- [`_selected_crop_entries`](#fn--selected-crop-entries-7598)
- [`_join_short`](#fn--join-short-7626)
- [`_build_crop_round_delta_issue_rows`](#fn--build-crop-round-delta-issue-rows-7634)
- [`_build_replacement_issue_rows`](#fn--build-replacement-issue-rows-7686)
- [`_build_replacement_issue_rows._effective_replacements_for_col`](#fn--effective-replacements-for-col-7751)
- [`_fetch_admin_reference`](#fn--fetch-admin-reference-7858)
- [`_write_table_sheet`](#fn--write-table-sheet-7908)
- [`_apply_admin_sheets`](#fn--apply-admin-sheets-7923)
- [`_build_replacement_status_rows`](#fn--build-replacement-status-rows-7966)
- [`write_validated_questionnaire`](#fn-write-validated-questionnaire-8075)

## Full Specifications

### `_NullOutput.write` {#fn-write-17}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:17`

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

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:18`

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

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:19`

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

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:25`

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

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:37`

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

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:41`

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

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:50`

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

### `_load_effective_config` {#fn--load-effective-config-139}

**Pipeline stage:** `Step 1 Configuration`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:139`

**Signature**

```python
def _load_effective_config(cfg_path: Path) -> tuple[dict, Path | None, Path]:
```

**Returns:** `tuple[dict, Path | None, Path]`

**What it does:** Implements logic in the `Step 1 Configuration` phase.

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

### `_reference_scope_label` {#fn--reference-scope-label-204}

**Pipeline stage:** `Step 1 Configuration`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:204`

**Signature**

```python
def _reference_scope_label() -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 1 Configuration` phase.

**Parameters**

No parameters.

??? note "Function source"

    ```python
    def _reference_scope_label() -> str:
        mode = str(getattr(globals().get("cfg", None), "reference_mode", "") or "").strip().lower()
        if mode == "previous_round":
            return "previous round"
        return "latest template"
    ```

### `_not_in_reference_text` {#fn--not-in-reference-text-211}

**Pipeline stage:** `Step 1 Configuration`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:211`

**Signature**

```python
def _not_in_reference_text(suffix: str='') -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 1 Configuration` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `suffix` | positional_or_keyword | No | `''` | `str` | Input used by the `Step 1 Configuration` stage. |

??? note "Function source"

    ```python
    def _not_in_reference_text(suffix: str = "") -> str:
        base = _reference_scope_label()
        if suffix:
            return f"(not in {base} {suffix})"
        return f"(not in {base})"
    ```

### `_normalize_header_name` {#fn--normalize-header-name-242}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:242`

**Signature**

```python
def _normalize_header_name(name: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 2 Reference file resolution` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 2 Reference file resolution` stage. |

??? note "Function source"

    ```python
    def _normalize_header_name(name: str) -> str:
        s = str(name or "").strip().lower()
        return re.sub(r"[^a-z0-9]+", "", s)
    ```

### `_header_tokens` {#fn--header-tokens-247}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:247`

**Signature**

```python
def _header_tokens(name: str) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 2 Reference file resolution` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 2 Reference file resolution` stage. |

??? note "Function source"

    ```python
    def _header_tokens(name: str) -> list[str]:
        s = str(name or "").strip().lower()
        return [t for t in re.split(r"[^a-z0-9]+", s) if t]
    ```

### `_is_language_candidate_header` {#fn--is-language-candidate-header-252}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:252`

**Signature**

```python
def _is_language_candidate_header(name: str) -> bool:
```

**Returns:** `bool`

**What it does:** Reject obvious non-language columns to avoid false alias matches.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 2 Reference file resolution` stage. |

??? note "Function source"

    ```python
    def _is_language_candidate_header(name: str) -> bool:
        """Reject obvious non-language columns to avoid false alias matches."""
        n = _normalize_header_name(name)
        blocked = {
            "qname", "suggestedqname", "qtype", "mandatory", "excelrow", "sourcefile",
            "length", "len", "codes", "additionalnotes",
            "defaultskippatternsconditional", "specifyskippatternvariablefrombluetext",
            "specifyskippatternvariable",
        }
        return n not in blocked
    ```

### `resolve_language_column` {#fn-resolve-language-column-264}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:264`

**Signature**

```python
def resolve_language_column(columns: list[str], language: str) -> str | None:
```

**Returns:** `str | None`

**What it does:** Resolves the best matching text column for a language, supporting variants

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `columns` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 2 Reference file resolution` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def resolve_language_column(columns: list[str], language: str) -> str | None:
        """
        Resolves the best matching text column for a language, supporting variants
        such as 'fr_French' while remaining deterministic.
        """
        lang = str(language or "EN").upper()
        preferred = LANGUAGE_COLUMN.get(lang, "English")
        if preferred in columns:
            return preferred

        preferred_norm = _normalize_header_name(preferred)
        for c in columns:
            if _normalize_header_name(c) == preferred_norm:
                return c

        aliases = [_normalize_header_name(a) for a in LANGUAGE_ALIASES.get(lang, [])]
        ranked: list[tuple[int, int, str]] = []
        for c in columns:
            if not _is_language_candidate_header(c):
                continue
            c_norm = _normalize_header_name(c)
            c_toks = set(_header_tokens(c))
            score = 0

            if preferred_norm and preferred_norm in c_norm:
                score += 6

            for a in aliases:
                if not a:
                    continue
                if len(a) <= 2:
                    # short language codes (fr/es/ar/pt/en): require token/prefix match,
                    # never generic substring match (prevents 'Codes' -> 'Spanish').
                    c_low = str(c or "").strip().lower()
                    if a in c_toks:
                        score += 5
                    if c_low.startswith(a + "_") or c_low.startswith(a + "-"):
                        score += 4
                else:
                    if a in c_norm:
                        score += 3
                    if a in c_toks:
                        score += 2

            if score > 0:
                ranked.append((score, -len(c), c))

        if not ranked:
            return None
        ranked.sort(reverse=True)
        return ranked[0][2]
    ```

### `detect_language_from_filename` {#fn-detect-language-from-filename-317}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:317`

**Signature**

```python
def detect_language_from_filename(path: Path | str) -> str | None:
```

**Returns:** `str | None`

**What it does:** Returns EN/FR/ES/AR/PT when filename contains a language token like _ar_.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path | str` | Filesystem path used for reading inputs or writing outputs. |

??? note "Function source"

    ```python
    def detect_language_from_filename(path: Path | str) -> str | None:
        """Returns EN/FR/ES/AR/PT when filename contains a language token like _ar_."""
        name = Path(path).name.lower()
        m = re.search(r"_(en|fr|es|ar|pt)(?=_|\.|$)", name)
        return m.group(1).upper() if m else None
    ```

### `choose_target_language` {#fn-choose-target-language-324}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:324`

**Signature**

```python
def choose_target_language(questionnaire_path: Path, questions_df: pl.DataFrame, preferred: str='EN') -> tuple[str, str]:
```

**Returns:** `tuple[str, str]`

**What it does:** Chooses the analysis language for text/option comparisons.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questionnaire_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `preferred` | positional_or_keyword | No | `'EN'` | `str` | Input used by the `Step 2 Reference file resolution` stage. |

??? note "Function source"

    ```python
    def choose_target_language(questionnaire_path: Path, questions_df: pl.DataFrame, preferred: str = "EN") -> tuple[str, str]:
        """
        Chooses the analysis language for text/option comparisons.
        Priority:
          1) language token in questionnaire filename (if non-EN and present in columns)
          2) config language (if non-EN and present in columns)
          3) best available non-EN column with most non-empty cells
          4) EN fallback
        """
        cols = questions_df.columns

        file_lang = detect_language_from_filename(questionnaire_path)
        if file_lang and file_lang != "EN" and resolve_language_column(cols, file_lang):
            return file_lang, "filename"

        pref = str(preferred or "EN").upper()
        if pref != "EN" and resolve_language_column(cols, pref):
            return pref, "config"

        scored: list[tuple[int, str]] = []
        for lang in ["AR", "FR", "ES", "PT"]:
            col = resolve_language_column(cols, lang)
            if not col:
                continue
            n_non_empty = (
                questions_df
                .select(pl.col(col).cast(pl.Utf8).fill_null("").str.strip_chars().alias("_v"))
                .filter(pl.col("_v") != "")
                .height
            )
            if n_non_empty > 0:
                scored.append((n_non_empty, lang))

        if scored:
            scored.sort(reverse=True)
            return scored[0][1], "auto_non_en"

        return "EN", "fallback_en"
    ```

### `extract_date_from_name` {#fn-extract-date-from-name-364}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:364`

**Signature**

```python
def extract_date_from_name(path: Path) -> int:
```

**Returns:** `int`

**What it does:** Pulls an 8-digit date out of a filename (e.g. _20260609_).

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |

??? note "Function source"

    ```python
    def extract_date_from_name(path: Path) -> int:
        """
        Pulls an 8-digit date out of a filename (e.g. _20260609_).
        Returns 0 if no date is found, so the file sorts last.
        """
        m = re.search(r"(\d{8})", path.name)
        return int(m.group(1)) if m else 0
    ```

### `find_latest_template` {#fn-find-latest-template-373}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:373`

**Signature**

```python
def find_latest_template(template_repo: Path, enumerator: str, language: str) -> Path:
```

**Returns:** `Path`

**What it does:** Scans the template repo folder and returns the most recent template

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `template_repo` | positional_or_keyword | Yes | `-` | `Path` | Input used by the `Step 2 Reference file resolution` stage. |
| `enumerator` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 2 Reference file resolution` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def find_latest_template(template_repo: Path, enumerator: str, language: str) -> Path:
        """
        Scans the template repo folder and returns the most recent template
        matching the given enumerator (geopoll/kobo) and language (EN/FR/etc.).
        Sorts by date in filename first, then by file modification time as fallback.
        """
        matches = [
            p for p in template_repo.glob("*.xlsx")
            if enumerator.lower() in p.name.lower()
            and f"_{language.lower()}_" in p.name.lower()
        ]
        if not matches:
            raise FileNotFoundError(
                f"No template found for enumerator='{enumerator}', language='{language}' in:\n  {template_repo}"
            )
        matches.sort(key=lambda p: (extract_date_from_name(p), p.stat().st_mtime), reverse=True)
        return matches[0]
    ```

### `resolve_reference_file` {#fn-resolve-reference-file-392}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:392`

**Signature**

```python
def resolve_reference_file(cfg: ValidationConfig) -> Path:
```

**Returns:** `Path`

**What it does:** Returns the path to the reference file based on reference_mode in the config.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cfg` | positional_or_keyword | Yes | `-` | `ValidationConfig` | Runtime configuration object for this validation run. |

??? note "Function source"

    ```python
    def resolve_reference_file(cfg: ValidationConfig) -> Path:
        """Returns the path to the reference file based on reference_mode in the config."""
        if cfg.reference_mode == "latest_template":
            return find_latest_template(cfg.template_repo, cfg.enumerator, cfg.language)
        if cfg.reference_mode == "previous_round":
            if not cfg.previous_round_file:
                raise ValueError("previous_round_file must be set when reference_mode='previous_round'")
            return cfg.working_dir / cfg.previous_round_file
        raise ValueError(f"Unknown reference_mode: '{cfg.reference_mode}'")
    ```

### `load_critical_sets` {#fn-load-critical-sets-403}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:403`

**Signature**

```python
def load_critical_sets(cfg: ValidationConfig) -> dict:
```

**Returns:** `dict`

**What it does:** Loads validation rules from critical_sets.yaml.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cfg` | positional_or_keyword | Yes | `-` | `ValidationConfig` | Runtime configuration object for this validation run. |

??? note "Function source"

    ```python
    def load_critical_sets(cfg: ValidationConfig) -> dict:
        """
        Loads validation rules from critical_sets.yaml.
        Search order:
          1. cfg.critical_sets_file (if set)
          2. critical_sets.yaml next to validation_config.yaml
          3. critical_sets.yaml in the parent folder of validation_config.yaml
          4. critical_sets.yaml in the current working directory
          5. critical_sets.yaml in a scripts/ subfolder of the current directory

        Returns a dict with keys: exact_sets, min_count_sets, crop_harvest.
        If the file is not found, structural validation is disabled (empty rules returned).
        """
        _cfg_dir = Path(__file__).parent.parent / "configuration"
        candidates = [
            Path(cfg.critical_sets_file) if cfg.critical_sets_file else None,
            _cfg_dir / "critical_sets.yaml",
            _cfg_dir.parent / "critical_sets.yaml",
            Path.cwd() / "critical_sets.yaml",
            Path.cwd() / "scripts" / "critical_sets.yaml",
        ]
        for path in candidates:
            if path is not None and path.exists():
                with open(path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                print(f"Rules loaded  : {path}")
                return {
                    "exact_sets"    : data.get("exact_sets", {}),
                    "min_count_sets": data.get("min_count_sets", {}),
                    "crop_harvest"  : data.get("crop_harvest", {}),
                }
        print("  critical_sets.yaml not found  structural validation disabled.")
        print(f"   Searched: {[str(p) for p in candidates if p is not None]}")
        return {"exact_sets": {}, "min_count_sets": {}, "crop_harvest": {}}
    ```

### `prepare_run` {#fn-prepare-run-439}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:439`

**Signature**

```python
def prepare_run(cfg: ValidationConfig) -> dict:
```

**Returns:** `dict`

**What it does:** Creates output directories and resolves all file paths.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cfg` | positional_or_keyword | Yes | `-` | `ValidationConfig` | Runtime configuration object for this validation run. |

??? note "Function source"

    ```python
    def prepare_run(cfg: ValidationConfig) -> dict:
        """
        Creates output directories and resolves all file paths.
        Returns a dict with the three paths the rest of the notebook needs.
        Prints a summary so you can confirm the right files were picked up.
        """
        cfg.working_dir.mkdir(parents=True, exist_ok=True)
        output_dir = (cfg.output_dir if cfg.output_dir else cfg.working_dir) / cfg.output_subfolder
        output_dir.mkdir(parents=True, exist_ok=True)

        questionnaire_path = cfg.working_dir / cfg.questionnaire_file
        reference_path     = resolve_reference_file(cfg)

        if not questionnaire_path.exists():
            raise FileNotFoundError(f"Questionnaire file not found:\n  {questionnaire_path}")
        if not reference_path.exists():
            raise FileNotFoundError(f"Reference file not found:\n  {reference_path}")

        _qname = questionnaire_path.name
        _round_tag = ""
        for _pat in [
            r"(?i)(?:^|[_\-\s])R(\d{1,3})(?=$|[_\-\s\.])",
            r"(?i)(?:^|[_\-\s])ROUND[_\-\s]*(\d{1,3})(?=$|[_\-\s\.])",
            r"(?i)R(?:OUND)?[_\-\s]*([0-9]{1,3})(?=(?:\.[A-Za-z0-9]+)?$)",
        ]:
            _m = re.search(_pat, _qname)
            if _m:
                _round_tag = f"_R{_m.group(1)}"
                break
        _rtag = _round_tag
        _dtag = _time.strftime("%Y%m%d")
        report_file = output_dir / f"report_geopoll_{cfg.language.lower()}_{cfg.iso3.upper()}{_rtag}_{_dtag}.xlsx"
        validated_questionnaire_file = output_dir / f"validated_questionnaire_geopoll_{cfg.language.lower()}_{cfg.iso3.upper()}{_rtag}_{_dtag}.xlsx"

        run = {
            "questionnaire_path" : questionnaire_path,
            "reference_path"     : reference_path,
            "report_file"        : report_file,
            "validated_questionnaire_file": validated_questionnaire_file,
        }

        print("Questionnaire :", questionnaire_path)
        print("Reference     :", reference_path)
        print("Report output :", report_file)
        print("Validated out :", validated_questionnaire_file)
        return run
    ```

### `_write_config_snapshot_geopoll` {#fn--write-config-snapshot-geopoll-487}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:487`

**Signature**

```python
def _write_config_snapshot_geopoll(cfg: ValidationConfig, run: dict, cfg_base_path: Path, cfg_active_path: Path, effective_cfg: dict) -> Path:
```

**Returns:** `Path`

**What it does:** Implements logic in the `Step 2 Reference file resolution` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cfg` | positional_or_keyword | Yes | `-` | `ValidationConfig` | Runtime configuration object for this validation run. |
| `run` | positional_or_keyword | Yes | `-` | `dict` | Runtime configuration object for this validation run. |
| `cfg_base_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `cfg_active_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `effective_cfg` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 2 Reference file resolution` stage. |

??? note "Function source"

    ```python
    def _write_config_snapshot_geopoll(
        cfg: ValidationConfig,
        run: dict,
        cfg_base_path: Path,
        cfg_active_path: Path,
        effective_cfg: dict,
    ) -> Path:
        logs_root = cfg.output_dir if cfg.output_dir else run["report_file"].parent.parent
        logs_dir = logs_root / "configuration"
        logs_dir.mkdir(parents=True, exist_ok=True)

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_file = logs_dir / f"config_geopoll_{cfg.language}_{cfg.iso3}_{ts}.yaml"

        payload = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "tool": cfg.enumerator,
            "active_config_file": str(cfg_active_path),
            "base_config_file": str(cfg_base_path.resolve()),
            "config_profile": str(effective_cfg.get("config_profile") or ""),
            "resolved_config": {
                "templates_dir": str(cfg.template_repo),
                "working_dir": str(cfg.working_dir),
                "questionnaire_file": cfg.questionnaire_file,
                "reference_mode": cfg.reference_mode,
                "language": cfg.language,
                "iso3": cfg.iso3,
                "output_dir": str(cfg.output_dir) if cfg.output_dir else "",
                "output_subfolder": cfg.output_subfolder,
                "previous_round_file": cfg.previous_round_file or "",
                "critical_sets_file": str(cfg.critical_sets_file) if cfg.critical_sets_file else "",
            },
            "resolved_run_paths": {k: str(v) for k, v in run.items()},
        }

        with out_file.open("w", encoding="utf-8") as f:
            yaml.safe_dump(payload, f, sort_keys=False, allow_unicode=True)
        return out_file
    ```

### `_resolve_column_by_aliases` {#fn--resolve-column-by-aliases-616}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:616`

**Signature**

```python
def _resolve_column_by_aliases(columns: list[str], aliases: list[str]) -> str | None:
```

**Returns:** `str | None`

**What it does:** Implements logic in the `Step 3 Reading and normalising the survey sheet` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `columns` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |
| `aliases` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def _resolve_column_by_aliases(columns: list[str], aliases: list[str]) -> str | None:
        alias_norm = {_normalize_header_name(a) for a in aliases}
        for c in columns:
            if _normalize_header_name(c) in alias_norm:
                return c
        return None
    ```

### `_canonical_column_from_header` {#fn--canonical-column-from-header-624}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:624`

**Signature**

```python
def _canonical_column_from_header(name: str) -> str | None:
```

**Returns:** `str | None`

**What it does:** Implements logic in the `Step 3 Reading and normalising the survey sheet` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def _canonical_column_from_header(name: str) -> str | None:
        n = _normalize_header_name(name)
        for canonical, aliases in COLUMN_ALIASES.items():
            alias_norm = {_normalize_header_name(canonical)} | {_normalize_header_name(a) for a in aliases}
            if n in alias_norm:
                return canonical
        return None
    ```

### `_as_text_cell` {#fn--as-text-cell-633}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:633`

**Signature**

```python
def _as_text_cell(value):
```

**Returns:** `None or implicit return`

**What it does:** Preserve cell content while forcing a stable string/None shape.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def _as_text_cell(value):
        """
        Preserve cell content while forcing a stable string/None shape.
        This avoids Polars schema crashes on mixed typed columns (e.g. '#REF!' strings
        appearing in otherwise numeric-looking columns).
        """
        if value is None:
            return None
        if isinstance(value, str):
            return value.strip()
        return str(value).strip()
    ```

### `_load_workbook_readonly` {#fn--load-workbook-readonly-646}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:646`

**Signature**

```python
def _load_workbook_readonly(path: Path, data_only: bool=True, read_only: bool=True):
```

**Returns:** `None or implicit return`

**What it does:** Best-effort workbook loader:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `data_only` | positional_or_keyword | No | `True` | `bool` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |
| `read_only` | positional_or_keyword | No | `True` | `bool` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def _load_workbook_readonly(path: Path, data_only: bool = True, read_only: bool = True):
        """
        Best-effort workbook loader:
        1) normal open
        2) if locked (PermissionError), try a temp copy and open the copy
        """
        p = Path(path)
        try:
            return openpyxl.load_workbook(p, data_only=data_only, read_only=read_only)
        except PermissionError as e:
            tmp_dir = Path(tempfile.gettempdir()) / "diem_qval_wb_cache"
            tmp_dir.mkdir(parents=True, exist_ok=True)
            tmp_path = tmp_dir / f"{uuid.uuid4().hex}_{p.name}"
            try:
                shutil.copy2(p, tmp_path)
                wb = openpyxl.load_workbook(tmp_path, data_only=data_only, read_only=read_only)
                setattr(wb, "_temp_copy_path", str(tmp_path))
                print(f"  Warning: workbook locked, reading temp copy: {p.name}")
                return wb
            except Exception as copy_err:
                try:
                    if tmp_path.exists():
                        tmp_path.unlink()
                except Exception:
                    pass
                raise PermissionError(
                    f"Cannot open workbook '{p}'. It may be locked by Excel/OneDrive sync. "
                    "Close the workbook (or disable Office co-authoring sync on this file) and retry."
                ) from copy_err
    ```

### `_close_workbook` {#fn--close-workbook-677}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:677`

**Signature**

```python
def _close_workbook(wb) -> None:
```

**Returns:** `None`

**What it does:** Implements logic in the `Step 3 Reading and normalising the survey sheet` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |

??? note "Function source"

    ```python
    def _close_workbook(wb) -> None:
        if wb is None:
            return
        tmp_copy = getattr(wb, "_temp_copy_path", "")
        try:
            wb.close()
        finally:
            if tmp_copy:
                try:
                    tmp_path = Path(tmp_copy)
                    if tmp_path.exists():
                        tmp_path.unlink()
                except Exception:
                    pass
    ```

### `read_survey_sheet` {#fn-read-survey-sheet-693}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:693`

**Signature**

```python
def read_survey_sheet(path: Path, sheet_name: str='survey', header_row: int=2, _wb=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Reads the survey sheet from an xlsx file into a Polars DataFrame.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `sheet_name` | positional_or_keyword | No | `'survey'` | `str` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |
| `header_row` | positional_or_keyword | No | `2` | `int` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def read_survey_sheet(path: Path, sheet_name: str = "survey", header_row: int = 2, _wb=None) -> pl.DataFrame:
        """
        Reads the survey sheet from an xlsx file into a Polars DataFrame.

        header_row=2 because the GeoPoll template has one title/banner row above
        the real column headers.

        Two columns are added automatically:
          excel_row    the actual row number in the Excel file (for tracing mismatches)
          source_file  the filename (tells you which file a row came from)

        Pass _wb to reuse an already-opened openpyxl workbook (avoids re-opening
        the same file multiple times).
        """
        owns_wb = _wb is None
        wb = _wb or _load_workbook_readonly(path, data_only=True, read_only=True)
        try:
            ws = next(
                (wb[n] for n in wb.sheetnames if n.strip().lower() == sheet_name.lower()),
                None
            )
            if ws is None:
                raise KeyError(f"Sheet '{sheet_name}' not found. Available sheets: {wb.sheetnames}")

            row_iter = ws.iter_rows(values_only=True)
            for _ in range(header_row - 1):
                next(row_iter, None)   # skip title rows safely

            raw_headers = next(row_iter, None)
            if raw_headers is None:
                raise ValueError(f"Header row {header_row} is missing in sheet '{sheet_name}' for file {path.name}")
            headers = [
                str(h).replace("\n", " ").strip() if h is not None else f"unnamed_{i}"
                for i, h in enumerate(raw_headers, 1)
            ]

            rows      = []
            excel_row = header_row + 1

            for values in row_iter:
                if all(v is None for v in values):
                    excel_row += 1
                    continue
                row_dict = {}
                for i in range(len(headers)):
                    raw_val = values[i] if i < len(values) else None
                    row_dict[headers[i]] = _as_text_cell(raw_val)
                row_dict["excel_row"]   = excel_row
                row_dict["source_file"] = Path(path).name
                rows.append(row_dict)
                excel_row += 1

            if rows:
                df = pl.DataFrame(rows, infer_schema_length=None)
            else:
                schema = {h: pl.Utf8 for h in headers}
                schema["excel_row"] = pl.Int64
                schema["source_file"] = pl.Utf8
                df = pl.DataFrame(schema=schema)

            # Canonicalize known alias columns before any strict presence checks.
            mapped_cols: list[tuple[str, str]] = []
            for canonical, aliases in COLUMN_ALIASES.items():
                if canonical in df.columns:
                    continue
                matched = _resolve_column_by_aliases(df.columns, [canonical] + aliases)
                if matched and matched != canonical:
                    df = df.with_columns(pl.col(matched).alias(canonical))
                    mapped_cols.append((matched, canonical))
            if mapped_cols:
                print(f"  Header aliases mapped in {path.name}: {mapped_cols}")

            if "Q Name" not in df.columns:
                raise KeyError(f"'Q Name' column not found after reading the sheet. Available columns: {df.columns}")

            return (
                df.with_columns(pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Q Name"))
                .filter(pl.col("Q Name") != "")
            )
        finally:
            if owns_wb:
                _close_workbook(wb)
    ```

### `build_questions_df` {#fn-build-questions-df-776}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:776`

**Signature**

```python
def build_questions_df(df: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Selects and cleans the core validation columns.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def build_questions_df(df: pl.DataFrame) -> pl.DataFrame:
        """
        Selects and cleans the core validation columns.
        Warns (does not crash) if an expected column is missing  silent drops
        would make mismatches invisible.
        """
        # Canonicalise language columns first (e.g. fr_French -> French)
        # so downstream logic can rely on stable names.
        mapped: list[tuple[str, str]] = []
        for lang_code, canonical in LANGUAGE_COLUMN.items():
            if canonical in df.columns:
                continue
            matched = resolve_language_column(df.columns, lang_code)
            if matched and matched != canonical:
                df = df.with_columns(pl.col(matched).alias(canonical))
                mapped.append((matched, canonical))
        if mapped:
            print(f"  Language columns mapped: {mapped}")

        # Canonicalise known non-language column variants (especially skip columns).
        mapped_cols: list[tuple[str, str]] = []
        for canonical, aliases in COLUMN_ALIASES.items():
            if canonical in df.columns:
                continue
            matched = _resolve_column_by_aliases(df.columns, aliases)
            if matched and matched != canonical:
                df = df.with_columns(pl.col(matched).alias(canonical))
                mapped_cols.append((matched, canonical))
        if mapped_cols:
            print(f"  Columns mapped: {mapped_cols}")

        # Mandatory may be absent in some operational files; keep pipeline running
        # by synthesizing a blank column so risk logic still applies deterministically.
        if "Mandatory" not in df.columns:
            df = df.with_columns(pl.lit("").alias("Mandatory"))
            print("  Column synthesized: Mandatory (blank default)")

        missing = [
            c for c in CORE_COLUMNS
            if c not in df.columns and c not in ("excel_row", "source_file")
        ]
        if missing:
            print(f"  Expected columns not found (will be skipped): {missing}")

        available = [c for c in CORE_COLUMNS if c in df.columns]
        out = df.select(available)

        out = out.with_columns(
            cs.exclude("excel_row").cast(pl.Utf8).fill_null("").str.strip_chars()
        )
        return out
    ```

### `_normalize_module_token` {#fn--normalize-module-token-829}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:829`

**Signature**

```python
def _normalize_module_token(value) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 3 Reading and normalising the survey sheet` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def _normalize_module_token(value) -> str:
        txt = str(value or "").strip().lower()
        txt = re.sub(r"\s+", " ", txt)
        return txt
    ```

### `_is_geopoll_module_row` {#fn--is-geopoll-module-row-835}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:835`

**Signature**

```python
def _is_geopoll_module_row(row: dict) -> bool:
```

**Returns:** `bool`

**What it does:** Detect GeoPoll module/section divider rows.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `row` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def _is_geopoll_module_row(row: dict) -> bool:
        """
        Detect GeoPoll module/section divider rows.
        The survey's own 'module' column is blank on divider rows (e.g. "E. LIVESTOCK
        MARKETING") and populated with the module code on every real question row.
        """
        q_name = str(row.get("Q Name") or "").strip()
        if not q_name:
            return False
        module_val = str(row.get("module") or "").strip()
        return module_val == ""
    ```

### `split_geopoll_questions_and_modules` {#fn-split-geopoll-questions-and-modules-848}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:848`

**Signature**

```python
def split_geopoll_questions_and_modules(df: pl.DataFrame) -> tuple[pl.DataFrame, pl.DataFrame]:
```

**Returns:** `tuple[pl.DataFrame, pl.DataFrame]`

**What it does:** Split questionnaire rows into:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def split_geopoll_questions_and_modules(df: pl.DataFrame) -> tuple[pl.DataFrame, pl.DataFrame]:
        """
        Split questionnaire rows into:
          1) question rows, with module_key/module set from the survey's own 'module' column
          2) module rows catalog (one entry per distinct module code)
        """
        q_schema = {
            **{c: df.schema[c] for c in df.columns},
            "module_key": pl.Utf8,
            "module": pl.Utf8,
        }
        m_schema = {
            "module_key_norm": pl.Utf8,
            "module_key": pl.Utf8,
            "module": pl.Utf8,
            "excel_row": pl.Int64,
            "source_file": pl.Utf8,
        }
        if df is None or df.height == 0:
            return pl.DataFrame(schema=q_schema), pl.DataFrame(schema=m_schema)

        q_rows: list[dict] = []
        seen_keys: dict[str, dict] = {}

        sort_cols = ["excel_row"] if "excel_row" in df.columns else None
        src_rows = df.sort(sort_cols).to_dicts() if sort_cols else df.to_dicts()
        for row in src_rows:
            if _is_geopoll_module_row(row):
                continue  # section divider row -- not a question

            module_code = str(row.get("module") or "").strip()
            out = dict(row)
            out["module_key"] = module_code
            out["module"] = module_code
            q_rows.append(out)

            key_norm = _normalize_module_token(module_code)
            if key_norm and key_norm not in seen_keys:
                seen_keys[key_norm] = {
                    "module_key_norm": key_norm,
                    "module_key": module_code,
                    "module": module_code,
                    "excel_row": row.get("excel_row"),
                    "source_file": str(row.get("source_file") or ""),
                }

        q_df = pl.DataFrame(q_rows, schema=q_schema) if q_rows else pl.DataFrame(schema=q_schema)
        m_df = (
            pl.DataFrame(list(seen_keys.values()), schema=m_schema).sort("excel_row")
            if seen_keys else pl.DataFrame(schema=m_schema)
        )
        return q_df, m_df
    ```

### `validate_module_column_integrity` {#fn-validate-module-column-integrity-902}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:902`

**Signature**

```python
def validate_module_column_integrity(questions_df: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Flags rows that look like real questions (Q Type populated) but have a

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def validate_module_column_integrity(questions_df: pl.DataFrame) -> pl.DataFrame:
        """
        Flags rows that look like real questions (Q Type populated) but have a
        blank 'module' cell. split_geopoll_questions_and_modules() treats a blank
        module as the signal for a section-divider row and silently drops it --
        if this fires, a genuine question is being lost from every downstream check.
        """
        schema = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if questions_df is None or questions_df.height == 0:
            return pl.DataFrame(schema=schema)
        if "Q Type" not in questions_df.columns or "module" not in questions_df.columns:
            return pl.DataFrame(schema=schema)

        flagged = questions_df.filter(
            (pl.col("Q Type").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
            & (pl.col("module").cast(pl.Utf8).fill_null("").str.strip_chars() == "")
        )
        if flagged.height == 0:
            return pl.DataFrame(schema=schema)

        return flagged.select([
            pl.lit("module_missing_for_question").alias("issue_type"),
            pl.lit("").alias("set_name"),
            pl.col("Q Name"),
            pl.lit("module").alias("field"),
            pl.lit("(blank)").alias("current"),
            pl.lit("module code expected -- row is being dropped from all checks").alias("reference"),
            pl.lit("high").alias("severity"),
            pl.col("excel_row").cast(pl.Int64),
        ])
    ```

### `_filter_questions_by_module_keys` {#fn--filter-questions-by-module-keys-938}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:938`

**Signature**

```python
def _filter_questions_by_module_keys(df: pl.DataFrame, excluded_module_keys: set[str]) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 3 Reading and normalising the survey sheet` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `excluded_module_keys` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def _filter_questions_by_module_keys(df: pl.DataFrame, excluded_module_keys: set[str]) -> pl.DataFrame:
        if df is None or df.height == 0 or not excluded_module_keys or "module_key" not in df.columns:
            return df
        return (
            df
            .with_columns(
                pl.col("module_key").cast(pl.Utf8).fill_null("").map_elements(_normalize_module_token, return_dtype=pl.Utf8).alias("_module_key_norm")
            )
            .filter(~pl.col("_module_key_norm").is_in(list(excluded_module_keys)))
            .drop("_module_key_norm")
        )
    ```

### `_filter_module_rows_by_keys` {#fn--filter-module-rows-by-keys-951}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:951`

**Signature**

```python
def _filter_module_rows_by_keys(df: pl.DataFrame, excluded_module_keys: set[str]) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 3 Reading and normalising the survey sheet` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `excluded_module_keys` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def _filter_module_rows_by_keys(df: pl.DataFrame, excluded_module_keys: set[str]) -> pl.DataFrame:
        if df is None or df.height == 0 or not excluded_module_keys or "module_key_norm" not in df.columns:
            return df
        return df.filter(~pl.col("module_key_norm").is_in(list(excluded_module_keys)))
    ```

### `_resolve_module_keys_from_tokens` {#fn--resolve-module-keys-from-tokens-957}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:957`

**Signature**

```python
def _resolve_module_keys_from_tokens(tokens: list[str], module_dfs: list[pl.DataFrame]) -> tuple[set[str], list[str]]:
```

**Returns:** `tuple[set[str], list[str]]`

**What it does:** Implements logic in the `Step 3 Reading and normalising the survey sheet` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `tokens` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |
| `module_dfs` | positional_or_keyword | Yes | `-` | `list[pl.DataFrame]` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def _resolve_module_keys_from_tokens(tokens: list[str], module_dfs: list[pl.DataFrame]) -> tuple[set[str], list[str]]:
        alias_to_key: dict[str, str] = {}
        for df in module_dfs:
            if df is None or df.height == 0:
                continue
            cols = set(df.columns)
            if not {"module_key_norm", "module_key", "module"}.issubset(cols):
                continue
            for row in df.select(["module_key_norm", "module_key", "module"]).iter_rows(named=True):
                key_norm = str(row.get("module_key_norm") or "").strip()
                if not key_norm:
                    continue
                alias_to_key.setdefault(key_norm, key_norm)
                mk = _normalize_module_token(row.get("module_key"))
                ml = _normalize_module_token(row.get("module"))
                if mk:
                    alias_to_key.setdefault(mk, key_norm)
                if ml:
                    alias_to_key.setdefault(ml, key_norm)

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

### `_module_display_map` {#fn--module-display-map-991}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:991`

**Signature**

```python
def _module_display_map(*module_dfs: pl.DataFrame) -> dict[str, str]:
```

**Returns:** `dict[str, str]`

**What it does:** Implements logic in the `Step 3 Reading and normalising the survey sheet` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `*module_dfs` | var_positional | Yes | `-` | `pl.DataFrame` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def _module_display_map(*module_dfs: pl.DataFrame) -> dict[str, str]:
        out: dict[str, str] = {}
        for df in module_dfs:
            if df is None or df.height == 0:
                continue
            cols = set(df.columns)
            if not {"module_key_norm", "module_key", "module"}.issubset(cols):
                continue
            for row in df.select(["module_key_norm", "module_key", "module"]).iter_rows(named=True):
                key = str(row.get("module_key_norm") or "").strip()
                if not key:
                    continue
                lbl = str(row.get("module") or row.get("module_key") or "").strip()
                if key not in out or (not out[key] and lbl):
                    out[key] = lbl or str(row.get("module_key") or key)
        return out
    ```

### `_dedupe_keep_order` {#fn--dedupe-keep-order-1009}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1009`

**Signature**

```python
def _dedupe_keep_order(items: list[str]) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 3 Reading and normalising the survey sheet` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `items` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

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

### `_format_module_scope_for_display` {#fn--format-module-scope-for-display-1024}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1024`

**Signature**

```python
def _format_module_scope_for_display(configured_tokens: list[str], resolved_keys: set[str], module_names: dict[str, str]) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 3 Reading and normalising the survey sheet` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `configured_tokens` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |
| `resolved_keys` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |
| `module_names` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def _format_module_scope_for_display(configured_tokens: list[str], resolved_keys: set[str], module_names: dict[str, str]) -> str:
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

### `_qnames_for_module_keys` {#fn--qnames-for-module-keys-1036}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1036`

**Signature**

```python
def _qnames_for_module_keys(questions_df: pl.DataFrame, module_keys: set[str]) -> set[str]:
```

**Returns:** `set[str]`

**What it does:** Implements logic in the `Step 3 Reading and normalising the survey sheet` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `module_keys` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def _qnames_for_module_keys(questions_df: pl.DataFrame, module_keys: set[str]) -> set[str]:
        if (
            questions_df is None
            or questions_df.height == 0
            or not module_keys
            or "module_key" not in questions_df.columns
            or "Q Name" not in questions_df.columns
        ):
            return set()
        out = (
            questions_df
            .with_columns(
                pl.col("module_key").cast(pl.Utf8).fill_null("").map_elements(_normalize_module_token, return_dtype=pl.Utf8).alias("_module_key_norm")
            )
            .filter(pl.col("_module_key_norm").is_in(list(module_keys)))
            .select("Q Name")
            .drop_nulls()
            .to_series()
            .to_list()
        )
        return {str(v).strip() for v in out if str(v or "").strip()}
    ```

### `_normalize_q_type` {#fn--normalize-q-type-1067}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1067`

**Signature**

```python
def _normalize_q_type(value: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _normalize_q_type(value: str) -> str:
        txt = str(value or "").strip().lower()
        txt = re.sub(r"[-_/]+", " ", txt)
        txt = re.sub(r"\s+", " ", txt)
        return txt
    ```

### `is_option_bearing_qtype` {#fn-is-option-bearing-qtype-1074}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1074`

**Signature**

```python
def is_option_bearing_qtype(value: str) -> bool:
```

**Returns:** `bool`

**What it does:** Robust Q Type classifier for option-bearing questions.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def is_option_bearing_qtype(value: str) -> bool:
        """
        Robust Q Type classifier for option-bearing questions.
        Handles spacing/punctuation variants (e.g. Open Ended vs Open-Ended).
        """
        t = _normalize_q_type(value)
        if not t:
            return False
        if t == "single choice":
            return True
        if "select all that apply" in t:
            return True
        if "single choice" in t and "open ended" in t:
            return True
        return False
    ```

### `parse_options` {#fn-parse-options-1099}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1099`

**Signature**

```python
def parse_options(text: str) -> list[tuple[int, str]]:
```

**Returns:** `list[tuple[int, str]]`

**What it does:** Parses numbered options from a question text cell.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def parse_options(text: str) -> list[tuple[int, str]]:
        """
        Parses numbered options from a question text cell.
        Returns a list of (option_code, option_label) tuples.

        Labels are whitespace-collapsed but otherwise kept raw 
    

        Example:
            input:  "What is your gender?\\n\\n1)Male\\n2)Female\\n3)DON'T want to answer"
            output: [(1, "Male"), (2, "Female"), (3, "DON'T want to answer")]
        """
        if not text or not isinstance(text, str):
            return []
        results = []
        for m in OPTION_PATTERN.finditer(text):
            code  = int(m.group(1))
            label = " ".join(m.group(2).split())   # collapse newlines/extra spaces
            if label:
                results.append((code, label))
        return results
    ```

### `extract_question_stem` {#fn-extract-question-stem-1122}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1122`

**Signature**

```python
def extract_question_stem(text: str) -> str:
```

**Returns:** `str`

**What it does:** Returns only the question/instruction part, removing numbered option blocks.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def extract_question_stem(text: str) -> str:
        """
        Returns only the question/instruction part, removing numbered option blocks.
        Used for Question Changes so option text is handled only in Option Changes.
        """
        if not text or not isinstance(text, str):
            return ""
        m = OPTION_PATTERN.search(text)
        stem = text[:m.start()] if m else text
        return stem.strip()
    ```

### `_split_stem_and_options` {#fn--split-stem-and-options-1134}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1134`

**Signature**

```python
def _split_stem_and_options(text: str) -> tuple[str, str]:
```

**Returns:** `tuple[str, str]`

**What it does:** Splits a question-text cell into (stem, options_block) at the first numbered

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _split_stem_and_options(text: str) -> tuple[str, str]:
        """
        Splits a question-text cell into (stem, options_block) at the first numbered
        option, losslessly (stem + options_block == text). Unlike extract_question_stem,
        this keeps the options block so callers can recombine pieces from different sources.
        """
        if not text or not isinstance(text, str):
            return (text or "", "")
        m = OPTION_PATTERN.search(text)
        if not m:
            return (text, "")
        return (text[:m.start()], text[m.start():])
    ```

### `explode_options` {#fn-explode-options-1148}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1148`

**Signature**

```python
def explode_options(questions_df: pl.DataFrame, text_col: str='English') -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Turns the questions DataFrame (one row per question) into an options

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `text_col` | positional_or_keyword | No | `'English'` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def explode_options(questions_df: pl.DataFrame, text_col: str = "English") -> pl.DataFrame:
        """
        Turns the questions DataFrame (one row per question) into an options
        DataFrame (one row per answer option).

        Output columns:
            Q Name, Q Type, option_code (Int64), option_label (Utf8),
            excel_row, source_file
        """
        EMPTY_SCHEMA = {
            "Q Name"      : pl.Utf8,
            "Q Type"      : pl.Utf8,
            "option_code" : pl.Int64,
            "option_label": pl.Utf8,
            "excel_row"   : pl.Int64,
            "source_file" : pl.Utf8,
        }

        if text_col not in questions_df.columns:
            print(f"  Column '{text_col}' not found  returning empty options frame.")
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        # IMPORTANT:
        # Do not gate option extraction on Q Type classification alone.
        # Q Type can be malformed/corrupted while option text remains valid; in that case
        # options should still compare independently and type issues are reported separately.
        df = questions_df

        carry_cols = [c for c in ["Q Name", "Q Type", "excel_row", "source_file"] if c in df.columns]
        rows = []

        for row in df.select(carry_cols + [text_col]).iter_rows(named=True):
            text = row.get(text_col) or ""
            for code, label in parse_options(text):
                out_row = {c: row.get(c) for c in carry_cols}
                out_row["option_code"]  = code
                out_row["option_label"] = label
                rows.append(out_row)

        if not rows:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        return pl.DataFrame(rows).with_columns(
            pl.col("option_code").cast(pl.Int64),
            pl.col("option_label").cast(pl.Utf8),
        )
    ```

### `parse_codes_cell` {#fn-parse-codes-cell-1196}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1196`

**Signature**

```python
def parse_codes_cell(text: str) -> list[tuple[int, str]]:
```

**Returns:** `list[tuple[int, str]]`

**What it does:** Parses numbered entries from the survey 'Codes' column, e.g.:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def parse_codes_cell(text: str) -> list[tuple[int, str]]:
        """
        Parses numbered entries from the survey 'Codes' column, e.g.:
          1)shock_none
          2)shock_flood
        Returns (code_num, code_token) rows.
        """
        if not text or not isinstance(text, str):
            return []
        out = []
        for m in OPTION_PATTERN.finditer(text):
            num = int(m.group(1))
            token = " ".join(m.group(2).split())
            if token:
                out.append((num, token))
        return out
    ```

### `explode_codes` {#fn-explode-codes-1214}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1214`

**Signature**

```python
def explode_codes(questions_df: pl.DataFrame, codes_col: str='Codes') -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Turns the survey 'Codes' column into one row per numbered code token.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `codes_col` | positional_or_keyword | No | `'Codes'` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def explode_codes(questions_df: pl.DataFrame, codes_col: str = "Codes") -> pl.DataFrame:
        """
        Turns the survey 'Codes' column into one row per numbered code token.
        Output columns: Q Name, code_num, code_token, excel_row, source_file
        """
        EMPTY_SCHEMA = {
            "Q Name": pl.Utf8,
            "code_num": pl.Int64,
            "code_token": pl.Utf8,
            "excel_row": pl.Int64,
            "source_file": pl.Utf8,
        }
        if codes_col not in questions_df.columns:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        carry_cols = [c for c in ["Q Name", "excel_row", "source_file"] if c in questions_df.columns]
        rows = []
        for row in questions_df.select(carry_cols + [codes_col]).iter_rows(named=True):
            for num, tok in parse_codes_cell(str(row.get(codes_col) or "")):
                rd = {c: row.get(c) for c in carry_cols}
                rd["code_num"] = num
                rd["code_token"] = tok
                rows.append(rd)
        if not rows:
            return pl.DataFrame(schema=EMPTY_SCHEMA)
        return pl.DataFrame(rows).with_columns([
            pl.col("code_num").cast(pl.Int64),
            pl.col("code_token").cast(pl.Utf8),
        ])
    ```

### `_normalize_placeholder_token` {#fn--normalize-placeholder-token-1293}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1293`

**Signature**

```python
def _normalize_placeholder_token(token: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _normalize_placeholder_token(token: str) -> str:
        s = str(token or "").strip()
        if s.startswith("$") and s.endswith("$") and len(s) >= 2:
            s = s[1:-1]
        s = re.sub(r"\s+", " ", s).strip().upper()
        s = re.sub(r" (EN|FR|ES|AR|PT)$", "", s)
        return s
    ```

### `_is_crop_placeholder_token` {#fn--is-crop-placeholder-token-1302}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1302`

**Signature**

```python
def _is_crop_placeholder_token(token: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _is_crop_placeholder_token(token: str) -> bool:
        norm = _normalize_placeholder_token(token)
        if norm.startswith("TEN MOST COMMON CROP"):
            return True
        return norm in {"CROPS SOLD", "CROP CODES", "CROP SOLD CODES"}
    ```

### `_contains_crop_marker_text` {#fn--contains-crop-marker-text-1309}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1309`

**Signature**

```python
def _contains_crop_marker_text(text: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _contains_crop_marker_text(text: str) -> bool:
        for tok in re.findall(r"\$[^$\r\n]+\$", str(text or "")):
            if _is_crop_placeholder_token(tok):
                return True
        return False
    ```

### `_clean_header` {#fn--clean-header-1316}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1316`

**Signature**

```python
def _clean_header(value) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _clean_header(value) -> str:
        return str(value or "").replace("\n", " ").strip()
    ```

### `_find_column` {#fn--find-column-1320}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1320`

**Signature**

```python
def _find_column(columns: list[str], *candidates: str) -> Optional[str]:
```

**Returns:** `Optional[str]`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `columns` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 4 Exploding answer options` stage. |
| `*candidates` | var_positional | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _find_column(columns: list[str], *candidates: str) -> Optional[str]:
        lookup = {_clean_header(c).lower(): c for c in columns}
        for candidate in candidates:
            match = lookup.get(_clean_header(candidate).lower())
            if match:
                return match
        return None
    ```

### `read_generic_sheet` {#fn-read-generic-sheet-1329}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1329`

**Signature**

```python
def read_generic_sheet(path: Path, sheet_name: str, header_row: int, _wb=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Reads any workbook sheet into Polars using the provided 1-based header row.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `sheet_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |
| `header_row` | positional_or_keyword | Yes | `-` | `int` | Input used by the `Step 4 Exploding answer options` stage. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def read_generic_sheet(path: Path, sheet_name: str, header_row: int, _wb=None) -> pl.DataFrame:
        """
        Reads any workbook sheet into Polars using the provided 1-based header row.
        Used for auxiliary sheets such as Crop list and Additional information.
        """
        owns_wb = _wb is None
        wb = _wb or _load_workbook_readonly(path, data_only=True, read_only=True)
        try:
            ws = next((wb[n] for n in wb.sheetnames if n.strip().lower() == sheet_name.lower()), None)
            if ws is None:
                raise KeyError(f"Sheet '{sheet_name}' not found in {path.name}. Available sheets: {wb.sheetnames}")

            row_iter = ws.iter_rows(values_only=True)
            for _ in range(header_row - 1):
                next(row_iter, None)

            raw_headers = next(row_iter, None)
            if raw_headers is None:
                raise ValueError(f"Header row {header_row} is missing in sheet '{sheet_name}' for file {path.name}")
            headers = [
                _clean_header(h) if h is not None else f"unnamed_{i}"
                for i, h in enumerate(raw_headers, 1)
            ]

            rows = []
            for values in row_iter:
                if all(v is None for v in values):
                    continue
                row = {}
                for i in range(len(headers)):
                    raw_val = values[i] if i < len(values) else None
                    row[headers[i]] = _as_text_cell(raw_val)
                rows.append(row)

            return pl.DataFrame(rows, infer_schema_length=None) if rows else pl.DataFrame(schema={h: pl.Utf8 for h in headers})
        finally:
            if owns_wb:
                _close_workbook(wb)
    ```

### `read_additional_information` {#fn-read-additional-information-1368}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1368`

**Signature**

```python
def read_additional_information(path: Path, _wb=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def read_additional_information(path: Path, _wb=None) -> pl.DataFrame:
        return read_generic_sheet(path, sheet_name="Additional information", header_row=2, _wb=_wb)
    ```

### `read_crop_list` {#fn-read-crop-list-1372}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1372`

**Signature**

```python
def read_crop_list(path: Path, _wb=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def read_crop_list(path: Path, _wb=None) -> pl.DataFrame:
        return read_generic_sheet(path, sheet_name="Crop list", header_row=3, _wb=_wb)
    ```

### `has_placeholder` {#fn-has-placeholder-1376}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1376`

**Signature**

```python
def has_placeholder(value) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def has_placeholder(value) -> bool:
        return bool(PLACEHOLDER_PATTERN.search(str(value or "")))
    ```

### `build_placeholder_restore_map` {#fn-build-placeholder-restore-map-1383}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1383`

**Signature**

```python
def build_placeholder_restore_map(current_questions: pl.DataFrame, reference_questions: pl.DataFrame, candidate_columns: Optional[list[str]]=None) -> dict[str, dict[str, str]]:
```

**Returns:** `dict[str, dict[str, str]]`

**What it does:** Returns a per-question map of columns whose template/reference cell still

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `candidate_columns` | positional_or_keyword | No | `None` | `Optional[list[str]]` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def build_placeholder_restore_map(
        current_questions: pl.DataFrame,
        reference_questions: pl.DataFrame,
        candidate_columns: Optional[list[str]] = None,
    ) -> dict[str, dict[str, str]]:
        """
        Returns a per-question map of columns whose template/reference cell still
        contains a $...$ placeholder. Those cells are restored to vanilla before
        comparison so country-specific placeholder fills don't appear as false
        text-change diffs.

        For columns that can hold numbered answer options (English/French/etc.),
        only the question stem is restored to the reference's vanilla text -- the
        numbered options block is kept exactly as it is in the current questionnaire,
        so a genuine option addition/removal still surfaces in Option Changes even
        when the question stem also contains an unresolved placeholder.
        """
        columns = [c for c in (candidate_columns or RESTORE_TEXT_COLUMNS) if c in reference_questions.columns]
        current_lookup = {
            row["Q Name"]: row
            for row in current_questions.select(
                ["Q Name"] + [c for c in columns if c in current_questions.columns]
            ).iter_rows(named=True)
        }
        restore_map: dict[str, dict[str, str]] = {}

        for row in reference_questions.select(["Q Name"] + columns).iter_rows(named=True):
            qname = row["Q Name"]
            hits: dict[str, str] = {}
            for col in columns:
                ref_val = str(row.get(col) or "")
                if not has_placeholder(ref_val):
                    continue
                if col in _OPTION_BEARING_RESTORE_COLUMNS:
                    ref_stem, _ = _split_stem_and_options(ref_val)
                    cur_val = str((current_lookup.get(qname) or {}).get(col) or "")
                    _, cur_options = _split_stem_and_options(cur_val)
                    hits[col] = ref_stem + cur_options
                else:
                    hits[col] = ref_val
            if hits:
                restore_map[qname] = hits
        return restore_map
    ```

### `restore_placeholder_cells` {#fn-restore-placeholder-cells-1428}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1428`

**Signature**

```python
def restore_placeholder_cells(current_questions: pl.DataFrame, reference_questions: pl.DataFrame, candidate_columns: Optional[list[str]]=None) -> tuple[pl.DataFrame, pl.DataFrame]:
```

**Returns:** `tuple[pl.DataFrame, pl.DataFrame]`

**What it does:** Restores current questionnaire cells to the template/reference version,

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `candidate_columns` | positional_or_keyword | No | `None` | `Optional[list[str]]` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def restore_placeholder_cells(
        current_questions: pl.DataFrame,
        reference_questions: pl.DataFrame,
        candidate_columns: Optional[list[str]] = None,
    ) -> tuple[pl.DataFrame, pl.DataFrame]:
        """
        Restores current questionnaire cells to the template/reference version,
        but only for cells where the reference still contains a $...$ placeholder.
        Returns (restored_questions, restore_log).
        """
        restore_map = build_placeholder_restore_map(current_questions, reference_questions, candidate_columns)
        if not restore_map:
            empty_log = pl.DataFrame(schema={"Q Name": pl.Utf8, "field": pl.Utf8, "restored_value": pl.Utf8})
            return current_questions.clone(), empty_log

        restore_log_rows = []
        for qname, hits in restore_map.items():
            for field, restored_value in hits.items():
                restore_log_rows.append({
                    "Q Name": qname,
                    "field": field,
                    "restored_value": restored_value,
                })

        if not restore_log_rows:
            empty_log = pl.DataFrame(schema={"Q Name": pl.Utf8, "field": pl.Utf8, "restored_value": pl.Utf8})
            return current_questions.clone(), empty_log

        restore_log = pl.DataFrame(restore_log_rows).select(["Q Name", "field", "restored_value"])
        restore_wide = restore_log.pivot(
            values="restored_value",
            index="Q Name",
            columns="field",
            aggregate_function="first",
        )

        joined = current_questions.join(restore_wide, on="Q Name", how="left", suffix="_restore")

        fields = sorted(set(restore_log["field"].to_list()))
        for field in fields:
            restore_col = f"{field}_restore"
            if field in current_questions.columns and restore_col in joined.columns:
                joined = (
                    joined
                    .with_columns(pl.coalesce([pl.col(restore_col), pl.col(field)]).alias(field))
                    .drop(restore_col)
                )

        leftover_restore_cols = [c for c in joined.columns if c.endswith("_restore")]
        if leftover_restore_cols:
            joined = joined.drop(leftover_restore_cols)

        restored = joined.select(current_questions.columns)
        return restored, restore_log
    ```

### `_normalize_placeholder_key` {#fn--normalize-placeholder-key-1483}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1483`

**Signature**

```python
def _normalize_placeholder_key(original_value: str) -> str:
```

**Returns:** `str`

**What it does:** Normalize an Additional information 'Original' key to a placeholder token.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `original_value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _normalize_placeholder_key(original_value: str) -> str:
        """
        Normalize an Additional information 'Original' key to a placeholder token.

        Accepts both strict "$...$" keys and plain labels like "currency".
        Plain labels are canonicalized to "$label$".
        """
        original = str(original_value or "").strip()
        if not original:
            return ""
        if has_placeholder(original):
            m = PLACEHOLDER_PATTERN.search(original)
            return m.group(0).strip() if m else ""
        return f"${original}$"
    ```

### `_placeholder_lookup_aliases` {#fn--placeholder-lookup-aliases-1499}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1499`

**Signature**

```python
def _placeholder_lookup_aliases(token: str) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Build normalized lookup aliases for placeholder tokens (e.g. $season FR$ -> $season$).

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _placeholder_lookup_aliases(token: str) -> list[str]:
        """Build normalized lookup aliases for placeholder tokens (e.g. $season FR$ -> $season$)."""
        raw = str(token or "").strip()
        if not raw:
            return []

        aliases = []
        if raw.startswith("$") and raw.endswith("$") and len(raw) >= 2:
            inner = re.sub(r"\s+", " ", raw[1:-1]).strip()
            if inner:
                aliases.append(f"${inner}$")
                base = re.sub(r"\s+(EN|FR|ES|AR|PT)$", "", inner, flags=re.IGNORECASE).strip()
                if base and base != inner:
                    aliases.append(f"${base}$")
        else:
            aliases.append(raw)

        out = []
        seen = set()
        for a in aliases:
            k = a.lower()
            if k and k not in seen:
                seen.add(k)
                out.append(k)
        return out
    ```

### `_build_placeholder_index` {#fn--build-placeholder-index-1526}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1526`

**Signature**

```python
def _build_placeholder_index(replacements: dict[str, str]) -> dict[str, str]:
```

**Returns:** `dict[str, str]`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `replacements` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _build_placeholder_index(replacements: dict[str, str]) -> dict[str, str]:
        idx = {}
        for k, v in (replacements or {}).items():
            if not v:
                continue
            for alias in _placeholder_lookup_aliases(k):
                idx.setdefault(alias, v)
        return idx
    ```

### `_lookup_placeholder_replacement` {#fn--lookup-placeholder-replacement-1536}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1536`

**Signature**

```python
def _lookup_placeholder_replacement(token: str, replacements: dict[str, str], idx: dict[str, str] | None=None) -> str | None:
```

**Returns:** `str | None`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |
| `replacements` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 4 Exploding answer options` stage. |
| `idx` | positional_or_keyword | No | `None` | `dict[str, str] | None` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _lookup_placeholder_replacement(token: str, replacements: dict[str, str], idx: dict[str, str] | None = None) -> str | None:
        mapping = idx if idx is not None else _build_placeholder_index(replacements)
        for alias in _placeholder_lookup_aliases(token):
            val = mapping.get(alias)
            if val is not None and str(val) != "":
                return val
        return None
    ```

### `_language_code_for_text_column` {#fn--language-code-for-text-column-1545}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1545`

**Signature**

```python
def _language_code_for_text_column(column_name: str) -> str | None:
```

**Returns:** `str | None`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `column_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _language_code_for_text_column(column_name: str) -> str | None:
        c = str(column_name or "")
        c_norm = _normalize_header_name(c)
        for lang in ["EN", "FR", "ES", "AR", "PT"]:
            canonical = LANGUAGE_COLUMN.get(lang, "")
            if canonical and c_norm == _normalize_header_name(canonical):
                return lang
            aliases = LANGUAGE_ALIASES.get(lang, [])
            toks = set(_header_tokens(c))
            for a in aliases:
                a_norm = _normalize_header_name(a)
                if not a_norm:
                    continue
                if len(a_norm) <= 2:
                    c_low = c.lower().strip()
                    if a.lower() in toks or c_low.startswith(a.lower() + "_") or c_low.startswith(a.lower() + "-"):
                        return lang
                elif a_norm in c_norm:
                    return lang
        return None
    ```

### `_placeholder_token_explicit_lang` {#fn--placeholder-token-explicit-lang-1567}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1567`

**Signature**

```python
def _placeholder_token_explicit_lang(token: str) -> str | None:
```

**Returns:** `str | None`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _placeholder_token_explicit_lang(token: str) -> str | None:
        raw = str(token or "").strip()
        if not (raw.startswith("$") and raw.endswith("$") and len(raw) >= 2):
            return None
        inner = re.sub(r"\s+", " ", raw[1:-1]).strip()
        m = re.search(r"\s+(EN|FR|ES|AR|PT)$", inner, flags=re.IGNORECASE)
        return m.group(1).upper() if m else None
    ```

### `analyze_additional_info_substitutions` {#fn-analyze-additional-info-substitutions-1576}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1576`

**Signature**

```python
def analyze_additional_info_substitutions(path: Path, language: str, _wb=None) -> dict:
```

**Returns:** `dict`

**What it does:** Return diagnostics about Additional information substitution readiness.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def analyze_additional_info_substitutions(path: Path, language: str, _wb=None) -> dict:
        """Return diagnostics about Additional information substitution readiness."""
        df = read_additional_information(path, _wb=_wb)
        out = {
            "has_sheet": True,
            "has_required_columns": True,
            "replacement_col": "",
            "original_col": "",
            "rows_with_any_data": 0,
            "rows_with_placeholder_style_original": 0,
            "rows_with_non_placeholder_original": 0,
            "loaded_keys": set(),
            "blank_value_keys": set(),
        }

        if df.height == 0:
            out["has_sheet"] = False
            return out

        replacement_col = _find_column(
            df.columns,
            f"Replacement ({language})",
            "Replacement",
            "Replacement (EN)",
        )
        original_col = _find_column(df.columns, "Original")
        out["replacement_col"] = replacement_col or ""
        out["original_col"] = original_col or ""
        if not replacement_col or not original_col:
            out["has_required_columns"] = False
            return out

        for row in df.iter_rows(named=True):
            original = str(row.get(original_col) or "").strip()
            replacement = str(row.get(replacement_col) or "").strip()
            if not original and not replacement:
                continue

            out["rows_with_any_data"] += 1
            if has_placeholder(original):
                out["rows_with_placeholder_style_original"] += 1
            elif original:
                out["rows_with_non_placeholder_original"] += 1

            key = _normalize_placeholder_key(original)
            if not key:
                continue
            if replacement:
                out["loaded_keys"].add(key)
            else:
                out["blank_value_keys"].add(key)

        return out
    ```

### `build_additional_info_replacements` {#fn-build-additional-info-replacements-1631}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1631`

**Signature**

```python
def build_additional_info_replacements(path: Path, language: str, _wb=None) -> dict[str, str]:
```

**Returns:** `dict[str, str]`

**What it does:** Backward-compatible single-language map from Additional information.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def build_additional_info_replacements(path: Path, language: str, _wb=None) -> dict[str, str]:
        """Backward-compatible single-language map from Additional information."""
        per_lang = build_additional_info_replacements_by_language(path, _wb=_wb)
        lang = str(language or "EN").upper()
        if per_lang.get(lang):
            return per_lang[lang]
        if per_lang.get("EN"):
            return per_lang["EN"]
        for m in per_lang.values():
            if m:
                return m
        return {}
    ```

### `build_additional_info_replacements_by_language` {#fn-build-additional-info-replacements-by-language-1645}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1645`

**Signature**

```python
def build_additional_info_replacements_by_language(path: Path, _wb=None) -> dict[str, dict[str, str]]:
```

**Returns:** `dict[str, dict[str, str]]`

**What it does:** Build per-language substitution maps from Additional information.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def build_additional_info_replacements_by_language(path: Path, _wb=None) -> dict[str, dict[str, str]]:
        """Build per-language substitution maps from Additional information."""
        df = read_additional_information(path, _wb=_wb)
        original_col = _find_column(df.columns, "Original")
        if not original_col or df.height == 0:
            return {lang: {} for lang in ["EN", "FR", "ES", "AR", "PT"]}

        generic_replacement_col = _find_column(df.columns, "Replacement")
        en_replacement_col = _find_column(df.columns, "Replacement (EN)", "Replacement EN")

        replacement_col_by_lang = {}
        for lang in ["EN", "FR", "ES", "AR", "PT"]:
            replacement_col_by_lang[lang] = _find_column(
                df.columns,
                f"Replacement ({lang})",
                f"Replacement {lang}",
            )

        out = {lang: {} for lang in ["EN", "FR", "ES", "AR", "PT"]}
        season_phase_by_lang = {lang: "" for lang in out.keys()}

        for row in df.iter_rows(named=True):
            key = _normalize_placeholder_key(str(row.get(original_col) or "").strip())
            if not key:
                continue

            for lang in out.keys():
                replacement = ""
                col = replacement_col_by_lang.get(lang)
                if col:
                    replacement = str(row.get(col) or "").strip()
                if not replacement and generic_replacement_col:
                    replacement = str(row.get(generic_replacement_col) or "").strip()
                if not replacement and lang != "EN" and en_replacement_col:
                    replacement = str(row.get(en_replacement_col) or "").strip()

                if replacement:
                    out[lang][key] = replacement
                    if key.lower() in {"$season phase$", "$season phase $"}:
                        season_phase_by_lang[lang] = replacement.lower()

        for lang, mapping in out.items():
            if "$expected or nothing$" in mapping:
                phase = season_phase_by_lang.get(lang, "")
                mapping["$expected or nothing$"] = "expected" if phase in SEASON_PHASE_EXPECTED_VALUES else ""

        return out
    ```

### `apply_text_replacements` {#fn-apply-text-replacements-1694}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1694`

**Signature**

```python
def apply_text_replacements(value, replacements: dict[str, str], replacements_by_language: Optional[dict[str, dict[str, str]]]=None) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 4 Exploding answer options` stage. |
| `replacements` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 4 Exploding answer options` stage. |
| `replacements_by_language` | positional_or_keyword | No | `None` | `Optional[dict[str, dict[str, str]]]` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def apply_text_replacements(
        value,
        replacements: dict[str, str],
        replacements_by_language: Optional[dict[str, dict[str, str]]] = None,
    ) -> str:
        text = str(value or "")
        has_lang_maps = any((replacements_by_language or {}).values())
        if not replacements and not has_lang_maps:
            return text

        default_map = replacements or {}
        default_idx = _build_placeholder_index(default_map)
        lang_idx_cache: dict[str, dict[str, str]] = {}

        def _lang_map(lang: str) -> dict[str, str]:
            if not replacements_by_language:
                return {}
            return replacements_by_language.get(lang, {}) or {}

        for token in sorted(set(re.findall(r"\$[^$\r\n]+\$", text)), key=len, reverse=True):
            replacement = None
            token_lang = _placeholder_token_explicit_lang(token)

            # If token explicitly carries a language suffix (e.g. $season FR$),
            # prioritize that language replacement column.
            if token_lang:
                token_lang_map = _lang_map(token_lang)
                if token_lang_map:
                    if token_lang not in lang_idx_cache:
                        lang_idx_cache[token_lang] = _build_placeholder_index(token_lang_map)
                    replacement = _lookup_placeholder_replacement(token, token_lang_map, lang_idx_cache[token_lang])

            # Fallback to the active column/default language map.
            if replacement is None and default_map:
                replacement = _lookup_placeholder_replacement(token, default_map, default_idx)

            # Final fallback: EN map if available (useful when EN is selected and
            # only English replacements are filled).
            if replacement is None:
                en_map = _lang_map("EN")
                if en_map:
                    if "EN" not in lang_idx_cache:
                        lang_idx_cache["EN"] = _build_placeholder_index(en_map)
                    replacement = _lookup_placeholder_replacement(token, en_map, lang_idx_cache["EN"])

            if replacement is not None:
                text = text.replace(token, replacement)
        return text
    ```

### `apply_text_replacements._lang_map` {#fn--lang-map-1708}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1708`

**Signature**

```python
def _lang_map(lang: str) -> dict[str, str]:
```

**Returns:** `dict[str, str]`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `lang` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _lang_map(lang: str) -> dict[str, str]:
            if not replacements_by_language:
                return {}
            return replacements_by_language.get(lang, {}) or {}
    ```

### `apply_placeholder_conversions` {#fn-apply-placeholder-conversions-1744}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1744`

**Signature**

```python
def apply_placeholder_conversions(questions_df: pl.DataFrame, replacements: dict[str, str], candidate_columns: Optional[list[str]]=None, replacements_by_language: Optional[dict[str, dict[str, str]]]=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Forward-applies placeholder replacements to text-bearing columns.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `replacements` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 4 Exploding answer options` stage. |
| `candidate_columns` | positional_or_keyword | No | `None` | `Optional[list[str]]` | Input used by the `Step 4 Exploding answer options` stage. |
| `replacements_by_language` | positional_or_keyword | No | `None` | `Optional[dict[str, dict[str, str]]]` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def apply_placeholder_conversions(
        questions_df: pl.DataFrame,
        replacements: dict[str, str],
        candidate_columns: Optional[list[str]] = None,
        replacements_by_language: Optional[dict[str, dict[str, str]]] = None,
    ) -> pl.DataFrame:
        """
        Forward-applies placeholder replacements to text-bearing columns.
        Language columns use language-specific replacement maps when available.
        """
        columns = [c for c in (candidate_columns or RESTORE_TEXT_COLUMNS) if c in questions_df.columns]
        if not columns:
            return questions_df.clone()

        default_replacements = replacements or {}
        has_lang_maps = any((replacements_by_language or {}).values())
        out = questions_df.clone()

        for col in columns:
            lang = _language_code_for_text_column(col)
            col_replacements = default_replacements
            if replacements_by_language and lang and replacements_by_language.get(lang):
                col_replacements = replacements_by_language[lang]

            if not col_replacements and not has_lang_maps:
                continue

            out = out.with_columns(
                pl.col(col)
                .cast(pl.Utf8)
                .fill_null("")
                .map_elements(
                    lambda v: apply_text_replacements(v, col_replacements, replacements_by_language=replacements_by_language),
                    return_dtype=pl.Utf8,
                )
                .alias(col)
            )

        return out
    ```

### `extract_crop_metadata` {#fn-extract-crop-metadata-1785}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1785`

**Signature**

```python
def extract_crop_metadata(crop_df: pl.DataFrame, language: str) -> dict:
```

**Returns:** `dict`

**What it does:** Pulls the key columns from the Crop list sheet in a language-aware way.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 4 Exploding answer options` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def extract_crop_metadata(crop_df: pl.DataFrame, language: str) -> dict:
        """
        Pulls the key columns from the Crop list sheet in a language-aware way.
        Returned labels include the full crop pool, not only the selected rows.
        """
        label_col = _find_column(crop_df.columns, f"Label ({language})", "Label (EN)")
        dataset_col = _find_column(crop_df.columns, "Dataset code")
        select_col = _find_column(crop_df.columns, "Select top 10 crops", "Select top 10 crops ")

        if not label_col:
            return {"label_col": None, "dataset_col": dataset_col, "select_col": select_col, "labels": []}

        labels = [
            str(v).strip()
            for v in crop_df.get_column(label_col).to_list()
            if str(v or "").strip()
        ]
        return {
            "label_col": label_col,
            "dataset_col": dataset_col,
            "select_col": select_col,
            "labels": labels,
        }
    ```

### `find_crop_placeholder_questions` {#fn-find-crop-placeholder-questions-1810}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1810`

**Signature**

```python
def find_crop_placeholder_questions(reference_questions: pl.DataFrame) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Identifies questions whose reference/template text carries a crop marker.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def find_crop_placeholder_questions(reference_questions: pl.DataFrame) -> list[str]:
        """
        Identifies questions whose reference/template text carries a crop marker.
        Those are the questions that need template-style restoration for comparison
        and deployed-style rebuilding for validated output.
        """
        text_columns = [c for c in RESTORE_TEXT_COLUMNS if c in reference_questions.columns]
        hits = []
        for row in reference_questions.select(["Q Name"] + text_columns).iter_rows(named=True):
            values = "\n".join(str(row.get(col) or "") for col in text_columns)
            if _contains_crop_marker_text(values):
                hits.append(row["Q Name"])
        return sorted(set(hits))
    ```

### `_is_selected_crop_value` {#fn--is-selected-crop-value-1825}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1825`

**Signature**

```python
def _is_selected_crop_value(value) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _is_selected_crop_value(value) -> bool:
        return str(value or "").strip().lower() not in {"", "0", "0.0", "none", "nan"}
    ```

### `_build_sorted_crop_entries` {#fn--build-sorted-crop-entries-1829}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1829`

**Signature**

```python
def _build_sorted_crop_entries(crop_df: pl.DataFrame, language: str) -> list[dict]:
```

**Returns:** `list[dict]`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 4 Exploding answer options` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _build_sorted_crop_entries(crop_df: pl.DataFrame, language: str) -> list[dict]:
        meta = extract_crop_metadata(crop_df, language)
        label_col = meta.get("label_col")
        dataset_col = meta.get("dataset_col")
        select_col = meta.get("select_col")
        if not label_col or label_col not in crop_df.columns:
            return []

        needed = [label_col]
        if dataset_col and dataset_col in crop_df.columns:
            needed.append(dataset_col)
        if select_col and select_col in crop_df.columns:
            needed.append(select_col)

        entries = []
        for idx, row in enumerate(crop_df.select(needed).iter_rows(named=True), start=1):
            label = str(row.get(label_col) or "").strip()
            code = str(row.get(dataset_col) or "").strip() if dataset_col and dataset_col in crop_df.columns else ""
            selected = _is_selected_crop_value(row.get(select_col)) if select_col and select_col in crop_df.columns else False
            if not label and not code:
                continue
            entries.append({"row_idx": idx, "label": label, "code": code, "selected": selected})

        entries.sort(key=lambda e: (0 if e["selected"] else 1, e["row_idx"]))
        return entries
    ```

### `build_crop_option_block` {#fn-build-crop-option-block-1856}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1856`

**Signature**

```python
def build_crop_option_block(crop_df: pl.DataFrame, language: str, include_no_crop: bool=True) -> str:
```

**Returns:** `str`

**What it does:** Builds a numbered crop label block: selected crops first, then others.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 4 Exploding answer options` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `include_no_crop` | positional_or_keyword | No | `True` | `bool` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def build_crop_option_block(crop_df: pl.DataFrame, language: str, include_no_crop: bool = True) -> str:
        """Builds a numbered crop label block: selected crops first, then others."""
        entries = _build_sorted_crop_entries(crop_df, language)
        labels = [e["label"] for e in entries if e["label"]]
        if not labels:
            return ""

        lines = [f"{idx}){label}" for idx, label in enumerate(labels, start=1)]
        if include_no_crop:
            lines.extend(["91)No crop production", "92)DON'T KNOW", "93)REFUSED"])
        else:
            lines.extend(["92)DON'T KNOW", "93)REFUSED"])
        return "\n".join(lines)
    ```

### `build_crop_code_block` {#fn-build-crop-code-block-1871}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1871`

**Signature**

```python
def build_crop_code_block(crop_df: pl.DataFrame, language: str, include_no_crop: bool=True) -> str:
```

**Returns:** `str`

**What it does:** Builds a numbered crop dataset-code block: selected crops first, then others.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 4 Exploding answer options` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `include_no_crop` | positional_or_keyword | No | `True` | `bool` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def build_crop_code_block(crop_df: pl.DataFrame, language: str, include_no_crop: bool = True) -> str:
        """Builds a numbered crop dataset-code block: selected crops first, then others."""
        entries = _build_sorted_crop_entries(crop_df, language)
        codes = [e["code"] for e in entries if e["code"]]
        if not codes:
            return ""

        lines = [f"{idx}){code}" for idx, code in enumerate(codes, start=1)]
        if include_no_crop:
            lines.extend(["91)No crop production", "92)DON'T KNOW", "93)REFUSED"])
        else:
            lines.extend(["92)DON'T KNOW", "93)REFUSED"])
        return "\n".join(lines)
    ```

### `rebuild_crop_questions_for_deployed_form` {#fn-rebuild-crop-questions-for-deployed-form-1886}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:1886`

**Signature**

```python
def rebuild_crop_questions_for_deployed_form(questions_df: pl.DataFrame, template_questions: pl.DataFrame, crop_df: pl.DataFrame, language: str, candidate_columns: Optional[list[str]]=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Replaces crop placeholders using the current questionnaire Crop list.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `template_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 4 Exploding answer options` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `candidate_columns` | positional_or_keyword | No | `None` | `Optional[list[str]]` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def rebuild_crop_questions_for_deployed_form(
        questions_df: pl.DataFrame,
        template_questions: pl.DataFrame,
        crop_df: pl.DataFrame,
        language: str,
        candidate_columns: Optional[list[str]] = None,
    ) -> pl.DataFrame:
        """
        Replaces crop placeholders using the current questionnaire Crop list.
        Handles label and code markers, singular/plural and language-suffixed forms.
        """
        crop_qnames = set(find_crop_placeholder_questions(template_questions))
        columns = [c for c in (candidate_columns or RESTORE_TEXT_COLUMNS) if c in questions_df.columns]
        if not crop_qnames or not columns:
            return questions_df.clone()

        main_block = build_crop_option_block(crop_df, language, include_no_crop=True)
        sold_block = build_crop_option_block(crop_df, language, include_no_crop=False)
        main_code_block = build_crop_code_block(crop_df, language, include_no_crop=True)
        sold_code_block = build_crop_code_block(crop_df, language, include_no_crop=False)
        if not main_block:
            return questions_df.clone()

        crop_qnames_list = sorted(crop_qnames)
        qname_lc = pl.col("Q Name").cast(pl.Utf8).str.to_lowercase()
        is_crop_q = pl.col("Q Name").is_in(crop_qnames_list)
        is_sales_q = qname_lc.str.contains("sales")

        exprs = []
        for col in columns:
            base = pl.col(col).cast(pl.Utf8).fill_null("")

            has_marker = (
                base.str.contains(CROP_LABEL_MARKER_PATTERN)
                | base.str.contains(CROP_SOLD_LABEL_MARKER_PATTERN)
                | base.str.contains(CROP_CODE_MARKER_PATTERN)
                | base.str.contains(CROP_SOLD_CODE_MARKER_PATTERN)
            )

            replaced_main = (
                base
                .str.replace_all(CROP_LABEL_MARKER_PATTERN, main_block)
                .str.replace_all(CROP_SOLD_LABEL_MARKER_PATTERN, sold_block)
                .str.replace_all(CROP_CODE_MARKER_PATTERN, main_code_block)
                .str.replace_all(CROP_SOLD_CODE_MARKER_PATTERN, sold_code_block)
            )

            replaced_sold = (
                base
                .str.replace_all(CROP_LABEL_MARKER_PATTERN, sold_block)
                .str.replace_all(CROP_SOLD_LABEL_MARKER_PATTERN, sold_block)
                .str.replace_all(CROP_CODE_MARKER_PATTERN, sold_code_block)
                .str.replace_all(CROP_SOLD_CODE_MARKER_PATTERN, sold_code_block)
            )

            exprs.append(
                pl.when(is_crop_q & has_marker)
                .then(
                    pl.when(is_sales_q).then(replaced_sold).otherwise(replaced_main)
                )
                .otherwise(base)
                .alias(col)
            )

        return questions_df.with_columns(exprs)
    ```

### `normalize_text_expr` {#fn-normalize-text-expr-2178}

**Pipeline stage:** `Step 6 Normalisation helpers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2178`

**Signature**

```python
def normalize_text_expr(col_name: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Polars expression that lowercases a string column, removes punctuation,

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 6 Normalisation helpers` stage. |

??? note "Function source"

    ```python
    def normalize_text_expr(col_name: str) -> pl.Expr:
        """
        Polars expression that lowercases a string column, removes punctuation,
        and collapses whitespace. Apply as an alias so the original column is preserved.

        Usage:
            df.with_columns(normalize_text_expr("option_label").alias("option_label_norm"))
        """
        return (
            pl.col(col_name)
            .cast(pl.Utf8)
            .fill_null("")
            .str.to_lowercase()
            .str.replace_all(r"[^\w\s]", "")   # remove punctuation
            .str.replace_all(r"\s+", " ")       # collapse multiple spaces
            .str.strip_chars()
        )
    ```

### `normalize_code_token_expr` {#fn-normalize-code-token-expr-2197}

**Pipeline stage:** `Step 6 Normalisation helpers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2197`

**Signature**

```python
def normalize_code_token_expr(col_name: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Normalizes code tokens from the 'Codes' column for stable comparisons.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 6 Normalisation helpers` stage. |

??? note "Function source"

    ```python
    def normalize_code_token_expr(col_name: str) -> pl.Expr:
        """Normalizes code tokens from the 'Codes' column for stable comparisons."""
        return (
            pl.col(col_name)
            .cast(pl.Utf8)
            .fill_null("")
            .str.to_lowercase()
            .str.replace_all(r"[^a-z0-9_]+", "")
            .str.strip_chars()
        )
    ```

### `normalize_mandatory_expr` {#fn-normalize-mandatory-expr-2209}

**Pipeline stage:** `Step 6 Normalisation helpers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2209`

**Signature**

```python
def normalize_mandatory_expr(col_name: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Polars expression that maps any common yes/no variant to canonical "yes"/"no"/""

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 6 Normalisation helpers` stage. |

??? note "Function source"

    ```python
    def normalize_mandatory_expr(col_name: str) -> pl.Expr:
        """
        Polars expression that maps any common yes/no variant to canonical "yes"/"no"/""
        so that "Yes", "YES", "y", "true", "1" are all treated as equivalent.

        Using when/then/otherwise keeps this inside the Polars execution engine
        (faster and parallelisable) vs a Python lambda with map_elements.
        """
        cleaned = (
            pl.col(col_name)
            .cast(pl.Utf8)
            .fill_null("")
            .str.to_lowercase()
            .str.strip_chars()
        )
        return (
            pl.when(cleaned.is_in(["yes", "y", "true", "1"])).then(pl.lit("yes"))
            .when(cleaned.is_in(["no",  "n", "false", "0"])).then(pl.lit("no"))
            .when(cleaned.str.starts_with("yes")).then(pl.lit("yes"))
            .when(cleaned.str.starts_with("no")).then(pl.lit("no"))
            .otherwise(pl.lit(""))
        )
    ```

### `_normalize_skip_text` {#fn--normalize-skip-text-2244}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2244`

**Signature**

```python
def _normalize_skip_text(value) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 7 Comparison and validation functions` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _normalize_skip_text(value) -> str:
        text = "" if value is None else str(value)
        return re.sub(r"\s+", " ", text).strip()
    ```

### `_parse_skip_option_codes` {#fn--parse-skip-option-codes-2249}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2249`

**Signature**

```python
def _parse_skip_option_codes(skip_text: str, max_range_span: int=200, max_total_codes: int=500) -> set[int]:
```

**Returns:** `set[int]`

**What it does:** Extracts numeric option codes from the left side of skip rules.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `skip_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `max_range_span` | positional_or_keyword | No | `200` | `int` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `max_total_codes` | positional_or_keyword | No | `500` | `int` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _parse_skip_option_codes(
        skip_text: str,
        max_range_span: int = 200,
        max_total_codes: int = 500,
    ) -> set[int]:
        """
        Extracts numeric option codes from the left side of skip rules.
        Examples handled: "1=...", "1-4 = ...", "1,3,5=...", "2 to 4 = ...".

        Safety guards:
          - do not fully expand very wide ranges,
          - cap total extracted codes to avoid pathological blowups.
        """
        if not skip_text:
            return set()

        codes = set()
        parts = [p.strip() for p in re.split(r"[\r\n;]+", str(skip_text)) if p.strip()]
        for part in parts:
            if len(codes) >= max_total_codes:
                break

            left = part.split("=", 1)[0] if "=" in part else part

            for a, b in re.findall(r"\b(\d+)\s*(?:-|to)\s*(\d+)\b", left, flags=re.IGNORECASE):
                start, end = int(a), int(b)
                lo, hi = sorted((start, end))
                span = hi - lo + 1

                if span <= max_range_span and (len(codes) + span) <= max_total_codes:
                    codes.update(range(lo, hi + 1))
                else:
                    # Keep endpoints so we still validate something without exploding runtime.
                    codes.add(lo)
                    codes.add(hi)
                    if len(codes) >= max_total_codes:
                        break

            if len(codes) >= max_total_codes:
                break

            left_no_ranges = re.sub(r"\b\d+\s*(?:-|to)\s*\d+\b", " ", left, flags=re.IGNORECASE)
            for n in re.findall(r"\b\d+\b", left_no_ranges):
                codes.add(int(n))
                if len(codes) >= max_total_codes:
                    break

        return codes
    ```

### `_extract_referenced_qnames` {#fn--extract-referenced-qnames-2298}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2298`

**Signature**

```python
def _extract_referenced_qnames(skip_text: str, source_q: str, ref_qnames: set[str], curr_qnames: set[str]) -> set[str]:
```

**Returns:** `set[str]`

**What it does:** Extract target question names from skip rules using a strict heuristic:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `skip_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `source_q` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `ref_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `curr_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _extract_referenced_qnames(skip_text: str, source_q: str, ref_qnames: set[str], curr_qnames: set[str]) -> set[str]:
        """
        Extract target question names from skip rules using a strict heuristic:
          - parse only RHS of '=' (or line/segment after '='),
          - take the first token as candidate target,
          - ignore common routing labels (ineligible, end, quota, etc.),
          - keep candidates that are known qnames OR look like qnames (underscore).
        """
        text = str(skip_text or "")
        if len(text) > 4000:
            text = text[:4000]

        stopwords = {
            "ineligible", "eligible", "end", "poll", "quota", "reached",
            "terminate", "terminated", "screenout", "screen_out",
            "refusal", "refused", "closeout", "close", "callback",
            "yes", "no", "na", "n_a", "none",
        }

        out = set()
        segments = [s.strip() for s in re.split(r"[\r\n;]+", text) if s.strip()]
        for seg in segments:
            if "=" not in seg:
                continue
            rhs = seg.split("=", 1)[1].strip()
            if not rhs:
                continue

            m = re.match(r"^\s*([A-Za-z_]\w*)", rhs)
            if not m:
                continue

            cand = m.group(1)
            cand_l = cand.lower()
            if cand == source_q or cand_l in stopwords:
                continue

            if cand in ref_qnames or cand in curr_qnames or ("_" in cand):
                out.add(cand)

        return out
    ```

### `_extract_qname_tokens` {#fn--extract-qname-tokens-2349}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2349`

**Signature**

```python
def _extract_qname_tokens(text: str, known_qnames: set[str]) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Return word tokens from text that are known Q Names.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `known_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _extract_qname_tokens(text: str, known_qnames: set[str]) -> list[str]:
        """Return word tokens from text that are known Q Names."""
        return [t for t in _QNAME_TOKEN_RE.findall(str(text or "")) if t in known_qnames]
    ```

### `_extract_qname_like` {#fn--extract-qname-like-2354}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2354`

**Signature**

```python
def _extract_qname_like(text: str, known_qnames: set[str]) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Return word tokens that are either known Q Names OR look like Q Names

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `known_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _extract_qname_like(text: str, known_qnames: set[str]) -> list[str]:
        """
        Return word tokens that are either known Q Names OR look like Q Names
        (contain an underscore).  This lets us detect references to Q Names
        that were renamed / removed from the current questionnaire.
        """
        return [t for t in _QNAME_TOKEN_RE.findall(str(text or ""))
                if t in known_qnames or "_" in t]
    ```

### `_extract_codes_from_numeric_spec` {#fn--extract-codes-from-numeric-spec-2364}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2364`

**Signature**

```python
def _extract_codes_from_numeric_spec(spec: str, max_range_span: int=200, max_total_codes: int=500) -> set[int]:
```

**Returns:** `set[int]`

**What it does:** Safely parse numeric code specs like "1-4, 7, 9 to 11".

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `spec` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `max_range_span` | positional_or_keyword | No | `200` | `int` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `max_total_codes` | positional_or_keyword | No | `500` | `int` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _extract_codes_from_numeric_spec(
        spec: str,
        max_range_span: int = 200,
        max_total_codes: int = 500,
    ) -> set[int]:
        """
        Safely parse numeric code specs like "1-4, 7, 9 to 11".
        Large ranges are truncated to endpoints to prevent memory blowups while still
        preserving strong validation signal.
        """
        out: set[int] = set()
        if not spec:
            return out

        for a, b in re.findall(r"\b(\d+)\s*(?:-|to)\s*(\d+)\b", spec, re.IGNORECASE):
            lo, hi = sorted((int(a), int(b)))
            span = hi - lo + 1
            if span <= max_range_span and (len(out) + span) <= max_total_codes:
                out.update(range(lo, hi + 1))
            else:
                out.add(lo)
                out.add(hi)
            if len(out) >= max_total_codes:
                return out

        clean = re.sub(r"\b\d+\s*(?:-|to)\s*\d+\b", " ", spec, flags=re.IGNORECASE)
        for n in re.findall(r"\b\d+\b", clean):
            out.add(int(n))
            if len(out) >= max_total_codes:
                break
        return out
    ```

### `_extract_condition_codes` {#fn--extract-condition-codes-2397}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2397`

**Signature**

```python
def _extract_condition_codes(stmt: str) -> set[int]:
```

**Returns:** `set[int]`

**What it does:** Extract option codes from a full Default-column rule statement by finding

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `stmt` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _extract_condition_codes(stmt: str) -> set[int]:
        """
        Extract option codes from a full Default-column rule statement by finding
        the range between '=' and 'go to', e.g.:
          "if hh_gender = 1-4, go to hh_education"  -> {1, 2, 3, 4}
          "For any response, go to X"               -> {} (any response = no range)
        Receives the FULL statement (not sliced) so that 'go to' can anchor the match.
        """
        match = re.search(
            r'=\s*([\d][^;=\n]*?)\s*,?\s*go\s+to',
            stmt, re.IGNORECASE,
        )
        if not match:
            return set()
        rng = match.group(1).strip()
        return _extract_codes_from_numeric_spec(rng)
    ```

### `_extract_skip_codes_for_target` {#fn--extract-skip-codes-for-target-2414}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2414`

**Signature**

```python
def _extract_skip_codes_for_target(skip_text: str, target: str) -> set[int]:
```

**Returns:** `set[int]`

**What it does:** Extract option codes from Skip-Pattern lines that send flow to *target*.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `skip_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `target` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _extract_skip_codes_for_target(skip_text: str, target: str) -> set[int]:
        """
        Extract option codes from Skip-Pattern lines that send flow to *target*.
        Handles both compact and verbose styles:
          "1-3 = hh_education"
          "if hh_gender = 1-3, go to hh_education"
          "1 = q_a 2-4 = q_b"
          "if q = 1, go to a if q = 2-4, go to b"
        """
        def _codes_from_spec(spec: str) -> set[int]:
            return _extract_codes_from_numeric_spec(spec)

        compact_re = re.compile(
            r'(\d+(?:\s*(?:-|to)\s*\d+)?(?:\s*,\s*\d+(?:\s*(?:-|to)\s*\d+)?)*)\s*=\s*(\[[^\]]+\]|[A-Za-z_]\w*)',
            re.IGNORECASE,
        )
        verbose_re = re.compile(
            r'if\s+[A-Za-z_]\w*\s*=\s*([^;]+?)\s*,?\s*go\s+to\s*(.+?)(?=(?:\s+if\s+[A-Za-z_]\w*\s*=)|$)',
            re.IGNORECASE,
        )

        codes: set[int] = set()
        for part in re.split(r'[\r\n;]+', str(skip_text or "")):
            if target not in part:
                continue

            # Compact style supports multiple mappings in one segment.
            for m in compact_re.finditer(part):
                code_spec = m.group(1)
                target_text = m.group(2)
                target_tokens = _extract_qname_like(target_text, {target})
                if target in target_tokens or target_text.strip('[] ') == target:
                    codes.update(_codes_from_spec(code_spec))

            # Verbose style supports multiple "if ... go to ..." clauses in one segment.
            for vm in verbose_re.finditer(part):
                code_spec = vm.group(1)
                target_text = vm.group(2).strip().strip('.')
                target_tokens = _extract_qname_like(target_text, {target})
                if target in target_tokens or target_text.strip('[] ') == target:
                    codes.update(_codes_from_spec(code_spec))

        return codes
    ```

### `_extract_skip_codes_for_target._codes_from_spec` {#fn--codes-from-spec-2423}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2423`

**Signature**

```python
def _codes_from_spec(spec: str) -> set[int]:
```

**Returns:** `set[int]`

**What it does:** Implements logic in the `Step 7 Comparison and validation functions` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `spec` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _codes_from_spec(spec: str) -> set[int]:
            return _extract_codes_from_numeric_spec(spec)
    ```

### `_parse_default_skip_rules` {#fn--parse-default-skip-rules-2458}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2458`

**Signature**

```python
def _parse_default_skip_rules(default_text: str, known_qnames: set[str]) -> list[dict]:
```

**Returns:** `list[dict]`

**What it does:** Parse "Default skip patterns & conditional" into structured rules.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `default_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `known_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _parse_default_skip_rules(default_text: str, known_qnames: set[str]) -> list[dict]:
        """
        Parse "Default skip patterns & conditional" into structured rules.
        Each rule: {targets, is_flexible, is_next_question, raw}

        Handles both compact and verbose styles, including multiple clauses in one line.
        """
        text = _normalize_skip_text(str(default_text or ""))
        if not text:
            return []

        rules = []

        # Verbose style, including chained clauses in one segment.
        verbose_re = re.compile(
            r'if\s+[A-Za-z_]\w*\s*=\s*([^;]+?)\s*,?\s*go\s+to\s*(.+?)(?=(?:\s+if\s+[A-Za-z_]\w*\s*=)|$)',
            re.IGNORECASE,
        )
        for vm in verbose_re.finditer(text):
            code_spec = vm.group(1)
            target_text = vm.group(2).strip().strip('.')
            is_next_question = bool(_NEXT_Q_RE.search(target_text))
            is_flexible = bool(_OPTIONAL_RE.search(target_text))
            targets = _extract_qname_like(target_text, known_qnames)
            option_codes = _extract_condition_codes(f"x = {code_spec}, go to y")
            if targets or is_next_question:
                rules.append({
                    "targets": targets,
                    "is_flexible": is_flexible,
                    "is_next_question": is_next_question,
                    "option_codes": option_codes,
                    "raw": vm.group(0),
                })

        # Compact form fallback (no "go to"): "1 = q1 2-4 = q2"
        # Keep full RHS clause so patterns like "OR optional question" are preserved.
        if not rules:
            compact_re = re.compile(
                r'(\d+(?:\s*(?:-|to)\s*\d+)?(?:\s*,\s*\d+(?:\s*(?:-|to)\s*\d+)?)*)\s*=\s*(.+?)(?=(?:\s+\d+(?:\s*(?:-|to)\s*\d+)?(?:\s*,\s*\d+(?:\s*(?:-|to)\s*\d+)?)*)\s*=|$)',
                re.IGNORECASE,
            )
            for m in compact_re.finditer(text):
                code_spec = m.group(1)
                target_text = m.group(2).strip().strip('.')
                targets = _extract_qname_like(target_text, known_qnames)
                if not targets:
                    continue
                rules.append({
                    "targets": targets,
                    "is_flexible": bool(_OPTIONAL_RE.search(target_text)),
                    "is_next_question": bool(_NEXT_Q_RE.search(target_text)),
                    "option_codes": _extract_condition_codes(f"x = {code_spec}, go to y"),
                    "raw": m.group(0),
                })

        # Minimal fallback for "For any response, go to target" when no numeric condition exists.
        if not rules:
            any_re = re.compile(r'for\s+any\s+response\s*,?\s*go\s+to\s*(.+)$', re.IGNORECASE)
            m = any_re.search(text)
            if m:
                target_text = m.group(1).strip().strip('.')
                targets = _extract_qname_like(target_text, known_qnames)
                if targets:
                    rules.append({
                        "targets": targets,
                        "is_flexible": bool(_OPTIONAL_RE.search(target_text)),
                        "is_next_question": bool(_NEXT_Q_RE.search(target_text)),
                        "option_codes": set(),
                        "raw": m.group(0),
                    })

        return rules
    ```

### `_semantic_skip_signature` {#fn--semantic-skip-signature-2531}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2531`

**Signature**

```python
def _semantic_skip_signature(skip_text: str, known_qnames: set[str]) -> tuple[set[tuple], bool]:
```

**Returns:** `tuple[set[tuple], bool]`

**What it does:** Build a semantic signature for skip logic text so phrasing differences

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `skip_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `known_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _semantic_skip_signature(skip_text: str, known_qnames: set[str]) -> tuple[set[tuple], bool]:
        """
        Build a semantic signature for skip logic text so phrasing differences
        can still compare as equal.

        Signature item:
          (target, sorted_codes_tuple, is_flexible, is_next_question)
        """
        text = _normalize_skip_text(skip_text)
        if not text:
            return set(), False

        rules = _parse_default_skip_rules(text, known_qnames)
        if not rules:
            return set(), False

        sig: set[tuple] = set()
        for rule in rules:
            codes = tuple(sorted(int(c) for c in (rule.get("option_codes") or set())))
            is_flexible = bool(rule.get("is_flexible"))
            is_next_question = bool(rule.get("is_next_question"))
            targets = sorted(set(rule.get("targets") or []))

            if not targets and is_next_question:
                sig.add(("__NEXT__", codes, is_flexible, is_next_question))
                continue

            for t in targets:
                sig.add((t, codes, is_flexible, is_next_question))

        return sig, True
    ```

### `_skip_signatures_equivalent` {#fn--skip-signatures-equivalent-2564}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2564`

**Signature**

```python
def _skip_signatures_equivalent(sig_a: set[tuple], sig_b: set[tuple]) -> bool:
```

**Returns:** `bool`

**What it does:** Semantic equivalence for skip signatures with permissive wildcard handling:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `sig_a` | positional_or_keyword | Yes | `-` | `set[tuple]` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `sig_b` | positional_or_keyword | Yes | `-` | `set[tuple]` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _skip_signatures_equivalent(sig_a: set[tuple], sig_b: set[tuple]) -> bool:
        """
        Semantic equivalence for skip signatures with permissive wildcard handling:
        - same routing keys (target/flex/next) are required
        - for a given key, empty code tuple () means "any response" and is treated as wildcard
        """
        def _group(sig: set[tuple]) -> dict[tuple, set[tuple]]:
            out: dict[tuple, set[tuple]] = {}
            for item in sig:
                # item = (target, codes_tuple, is_flexible, is_next_question)
                target, codes, is_flexible, is_next = item
                key = (target, is_flexible, is_next)
                out.setdefault(key, set()).add(tuple(codes))
            return out

        ga = _group(sig_a)
        gb = _group(sig_b)
        if set(ga.keys()) != set(gb.keys()):
            return False

        for key in ga.keys():
            ca = ga[key]
            cb = gb[key]
            if () in ca or () in cb:
                # one side says "any response" for this target route
                continue
            if ca != cb:
                return False
        return True
    ```

### `_skip_signatures_equivalent._group` {#fn--group-2570}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2570`

**Signature**

```python
def _group(sig: set[tuple]) -> dict[tuple, set[tuple]]:
```

**Returns:** `dict[tuple, set[tuple]]`

**What it does:** Implements logic in the `Step 7 Comparison and validation functions` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `sig` | positional_or_keyword | Yes | `-` | `set[tuple]` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _group(sig: set[tuple]) -> dict[tuple, set[tuple]]:
            out: dict[tuple, set[tuple]] = {}
            for item in sig:
                # item = (target, codes_tuple, is_flexible, is_next_question)
                target, codes, is_flexible, is_next = item
                key = (target, is_flexible, is_next)
                out.setdefault(key, set()).add(tuple(codes))
            return out
    ```

### `_check_skip_consistency` {#fn--check-skip-consistency-2594}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2594`

**Signature**

```python
def _check_skip_consistency(skip_text: str, rules: list[dict], q_mandatory_map: dict[str, str], curr_qnames: set[str], known_qnames: set[str], source_q: str, next_qname: str | None) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Returns a list of issue descriptions (empty = consistent).

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `skip_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `rules` | positional_or_keyword | Yes | `-` | `list[dict]` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `q_mandatory_map` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `curr_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `known_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `source_q` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `next_qname` | positional_or_keyword | Yes | `-` | `str | None` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _check_skip_consistency(
        skip_text      : str,
        rules          : list[dict],
        q_mandatory_map: dict[str, str],
        curr_qnames    : set[str],
        known_qnames   : set[str],
        source_q       : str,
        next_qname     : str | None,
    ) -> list[str]:
        """
        Returns a list of issue descriptions (empty = consistent).

        Rules:
        - Each required target Q Name must appear in skip_text.
        - If the rule is flexible ("OR optional question"), a non-mandatory Q Name
          in skip_text is also acceptable.
        - [next question] is treated as equivalent to the concrete next Q Name.
        - Any explicit RHS target that does not exist in current questionnaire
          is treated as a broken reference.

        Range-check policy:
        - Compare ranges only when a target has one unambiguous numeric mapping.
        - Skip range comparison for ambiguous authoring forms (e.g. "otherwise").
        """
        skip_text_s = str(skip_text or "")
        skip_present = set(_extract_qname_like(skip_text_s, curr_qnames))
        skip_mentions_next = bool(_NEXT_Q_RE.search(skip_text_s))
        issues = []

        # Broken target references must stay high severity:
        # RHS targets that do not exist in the current questionnaire.
        skip_targets = _extract_referenced_qnames(
            skip_text_s,
            source_q=source_q,
            ref_qnames=known_qnames,
            curr_qnames=curr_qnames,
        )
        invalid_targets = sorted(t for t in skip_targets if t not in curr_qnames)
        if invalid_targets:
            issues.append(
                f"target question(s) not found in current questionnaire: {invalid_targets}"
            )

        expected_codes_by_target: dict[str, set[int]] = {}
        range_skip_targets: set[str] = set()

        for rule in rules:
            targets = list(rule.get("targets") or [])
            is_flexible = bool(rule.get("is_flexible"))
            is_next_question = bool(rule.get("is_next_question"))
            expected_codes = set(rule.get("option_codes") or set())
            raw_l = str(rule.get("raw") or "").lower()

            # Resolve [next question] to concrete target when possible.
            if is_next_question and not targets and next_qname:
                targets = [next_qname]

            if not targets:
                continue

            found_targets = [t for t in targets if t in skip_present]

            # Equivalence: skip says [next question], rule says concrete next qname.
            if not found_targets and skip_mentions_next and next_qname and next_qname in targets:
                found_targets = [next_qname]

            # Equivalence: rule says [next question], skip says concrete next qname.
            if not found_targets and is_next_question and next_qname and next_qname in skip_present:
                found_targets = [next_qname]

            if not found_targets:
                if is_flexible:
                    non_mand = [
                        q for q in skip_present
                        if q_mandatory_map.get(q) not in ("mandatory", "mandatory-panel")
                    ]
                    if not non_mand:
                        mandatory_targets = sorted(
                            q for q in skip_present
                            if q_mandatory_map.get(q) in ("mandatory", "mandatory-panel")
                        )
                        if mandatory_targets:
                            issues.append(
                                "invalid qname category: "
                                f"expected optional/non-mandatory target; got mandatory target(s) {mandatory_targets}"
                            )
                            continue
                        issues.append(
                            f"expected {targets} (or non-mandatory alternative) not found in skip pattern"
                        )
                else:
                    if not skip_text_s.strip():
                        issues.append(
                            f"skip pattern is empty but default/spec says go to {targets}"
                        )
                    else:
                        issues.append(
                            f"expected {targets} in skip pattern; got: {skip_text_s[:80]}"
                        )

            ambiguous = (len(targets) != 1) or ("otherwise" in raw_l)
            if ambiguous or not expected_codes:
                for t in targets:
                    range_skip_targets.add(t)
            else:
                t = targets[0]
                expected_codes_by_target.setdefault(t, set()).update(expected_codes)

        # Range verification per target (single comparison per target).
        for t, expected in expected_codes_by_target.items():
            if t in range_skip_targets:
                continue

            # next-question equivalence may hide explicit target token in skip text.
            if t not in skip_present and not (skip_mentions_next and next_qname == t):
                continue

            actual_codes = _extract_skip_codes_for_target(skip_text_s, t)
            if actual_codes and actual_codes != expected:
                issues.append(
                    f"option range mismatch for target '{t}': "
                    f"default/spec says {sorted(expected)}, "
                    f"skip pattern has {sorted(actual_codes)}"
                )

        return issues
    ```

### `validate_skip_patterns` {#fn-validate-skip-patterns-2721}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2721`

**Signature**

```python
def validate_skip_patterns(current_questions: pl.DataFrame, reference_questions: pl.DataFrame, current_options_en: pl.DataFrame | None=None, reference_options_en: pl.DataFrame | None=None, q_mandatory_map: dict[str, str] | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Three-layer skip-pattern validation:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `current_options_en` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |
| `reference_options_en` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |
| `q_mandatory_map` | positional_or_keyword | No | `None` | `dict[str, str] | None` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def validate_skip_patterns(
        current_questions    : pl.DataFrame,
        reference_questions  : pl.DataFrame,
        current_options_en   : pl.DataFrame | None = None,
        reference_options_en : pl.DataFrame | None = None,
        q_mandatory_map      : dict[str, str] | None = None,
    ) -> pl.DataFrame:
        """
        Three-layer skip-pattern validation:

        1. Template consistency check (mostly medium): current effective skip rule
           should align with template effective rule. Broken references remain high.

        Effective rule selection per side:
           - Current (analyzed): use "Specify skip pattern variable (from blue text)"
             when filled; otherwise fall back to "Skip Pattern", then "Default".
           - Reference/template: use template "Specify" when filled; otherwise
             template "Skip Pattern", then template "Default".

        2. Option code validity (high): numeric codes referenced in Skip Pattern
           must actually exist in the question's answer options.

        3. Option code validity (high): numeric codes referenced in Skip Pattern
           must actually exist in the question's answer options.
        """
        EMPTY_SCHEMA = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field"     : pl.Utf8, "current" : pl.Utf8, "reference": pl.Utf8,
            "severity"  : pl.Utf8, "excel_row": pl.Int64,
        }

        DEF_COL  = "Default skip patterns & conditional "
        SPEC_COL = "Specify skip pattern variable (from blue text)"
        SKIP_COL = "Skip Pattern"

        has_def_cur  = DEF_COL  in current_questions.columns
        has_spec_cur = SPEC_COL in current_questions.columns
        has_skip_cur = SKIP_COL in current_questions.columns

        has_def_ref  = DEF_COL  in reference_questions.columns
        has_spec_ref = SPEC_COL in reference_questions.columns
        has_skip_ref = SKIP_COL in reference_questions.columns

        if not has_def_cur and not has_skip_cur and not has_spec_cur:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        curr_qnames = set(current_questions["Q Name"].to_list())
        ref_qnames  = set(reference_questions["Q Name"].to_list())
        known_qnames = curr_qnames | ref_qnames
        q_mandatory_map     = q_mandatory_map or {}

        # Option code lookup for validity check (layer 3)
        curr_opt_map: dict[str, set[int]] = {}
        if current_options_en is not None and current_options_en.height > 0:
            for row in current_options_en.select(["Q Name", "option_code"]).iter_rows(named=True):
                q, c = row.get("Q Name"), row.get("option_code")
                if q and c is not None:
                    curr_opt_map.setdefault(q, set()).add(int(c))

        # Minimal row maps from current + reference questionnaires
        cur_cols = ["Q Name"] + [c for c in [SKIP_COL, DEF_COL, SPEC_COL, "excel_row"]
                                 if c in current_questions.columns]
        ref_cols = ["Q Name"] + [c for c in [SKIP_COL, DEF_COL, SPEC_COL]
                                 if c in reference_questions.columns]
        cur_rows = {r["Q Name"]: r
                    for r in current_questions.select(cur_cols).iter_rows(named=True)}
        ref_rows = {r["Q Name"]: r
                    for r in reference_questions.select(ref_cols).iter_rows(named=True)}

        # Q Name ordering for "next question" resolution
        qname_list = current_questions["Q Name"].to_list()
        qname_next = {q: qname_list[i + 1]
                      for i, q in enumerate(qname_list) if i + 1 < len(qname_list)}

        issues = []

        for qname, cr in cur_rows.items():
            excel_row = cr.get("excel_row")
            skip_text = _normalize_skip_text(cr.get(SKIP_COL) or "")
            def_text  = _normalize_skip_text(cr.get(DEF_COL)  or "")
            spec_text = _normalize_skip_text(cr.get(SPEC_COL) or "")

            rr = ref_rows.get(qname, {})
            ref_skip_text = _normalize_skip_text(rr.get(SKIP_COL) or "") if has_skip_ref else ""
            ref_def_text  = _normalize_skip_text(rr.get(DEF_COL)  or "") if has_def_ref else ""
            ref_spec_text = _normalize_skip_text(rr.get(SPEC_COL) or "") if has_spec_ref else ""

            # Current effective rule: Specify > Skip Pattern > Default
            current_effective = spec_text if spec_text else (skip_text if skip_text else def_text)

            # Reference/template effective rule: Specify > Skip Pattern > Default
            reference_effective = ref_spec_text if ref_spec_text else (ref_skip_text if ref_skip_text else ref_def_text)

            # Current-file emptiness check:
            # Flag when default exists but both Specify and Skip Pattern are empty.
            if def_text and (not spec_text) and (not skip_text):
                issues.append({
                    "issue_type": "skip_pattern_empty",
                    "set_name": "",
                    "Q Name": qname,
                    "field": SKIP_COL,
                    "current": "Specify + Skip Pattern are empty",
                    "reference": f"default present: {def_text[:200]}",
                    "severity": "high",
                    "excel_row": excel_row,
                })

            # Current-file semantic warning:
            # If Specify is blank and both Skip Pattern + Default are present, flag only when
            # Skip Pattern is semantically inconsistent with the current Default rule.
            if (not spec_text) and skip_text and def_text:
                _def_rules = _parse_default_skip_rules(def_text, known_qnames)
                _default_consistency_issues = []
                if _def_rules:
                    _default_consistency_issues = _check_skip_consistency(
                        skip_text,
                        _def_rules,
                        q_mandatory_map,
                        curr_qnames,
                        known_qnames,
                        qname,
                        qname_next.get(qname),
                    )
                if _default_consistency_issues:
                    issues.append({
                        "issue_type": "default_skip_modified",
                        "set_name": "",
                        "Q Name": qname,
                        "field": SKIP_COL,
                        "current": skip_text[:220],
                        "reference": f"default: {def_text[:200]}",
                        "severity": "info",
                        "excel_row": excel_row,
                    })

            # Layer 1: Current effective rule must align with template effective rule.
            if reference_effective and current_effective:
                rules = _parse_default_skip_rules(reference_effective, known_qnames)
                for desc in _check_skip_consistency(
                    current_effective,
                    rules,
                    q_mandatory_map,
                    curr_qnames,
                    known_qnames,
                    qname,
                    qname_next.get(qname),
                ):
                    is_range = desc.startswith("option range mismatch")
                    is_broken_target = desc.startswith("target question(s) not found in current questionnaire")
                    is_invalid_category = desc.startswith("invalid qname category")
                    is_empty = desc.startswith("skip pattern is empty")
                    severity = "high" if (is_broken_target or is_invalid_category or is_empty) else "info"
                    if is_broken_target:
                        issue_type = "skipPattern_invalid_qname"
                    elif is_invalid_category:
                        issue_type = "skipPattern_invalid_qnameCategory"
                    elif is_range:
                        issue_type = "skipPattern_range_mismatch"
                    elif is_empty:
                        issue_type = "skip_pattern_empty"
                    else:
                        issue_type = "skipPattern_changes"
                    issues.append({
                        "issue_type": issue_type,
                        "set_name": "",
                        "Q Name": qname, "field": SKIP_COL,
                        "current": current_effective[:220], "reference": reference_effective[:220],
                        "severity": severity,
                        "excel_row": excel_row,
                    })

            # Layer 2: no additional override-only notes are emitted to avoid noise.

            # Layer 3: Option codes in effective current skip rule must exist in options
            if current_effective:
                mentioned = _parse_skip_option_codes(current_effective)
                available = curr_opt_map.get(qname, set())
                if mentioned and available:
                    invalid = sorted(c for c in mentioned if c not in available)
                    if invalid:
                        issues.append({
                            "issue_type": "skipPattern_range_invalid", "set_name": "",
                            "Q Name": qname, "field": SKIP_COL,
                            "current": f"invalid option code(s): {invalid}",
                            "reference": f"valid codes: {sorted(available)}",
                            "severity": "high", "excel_row": excel_row,
                        })

            # Speculative drift warnings are intentionally not emitted.
            # Option changes are already surfaced in Option Changes and should be reviewed there.

        if not issues:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        return (
            pl.DataFrame(issues)
            .unique(subset=["issue_type", "Q Name", "field", "current", "reference"], keep="first")
        )
    ```

### `make_presence_issues` {#fn-make-presence-issues-2930}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:2930`

**Signature**

```python
def make_presence_issues(added: pl.DataFrame, removed: pl.DataFrame, reference_questions: pl.DataFrame | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Converts added/removed question lists into the common issues schema.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `added` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |
| `removed` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |
| `reference_questions` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def make_presence_issues(
        added: pl.DataFrame,
        removed: pl.DataFrame,
        reference_questions: pl.DataFrame | None = None,
    ) -> pl.DataFrame:
        """
        Converts added/removed question lists into the common issues schema.

        Severity rules:
          - Optional questions (o_ prefix): 'info'   tracked but not a blocker
          - Non-optional added            : 'medium'  unexpected addition, review needed
          - Non-optional removed          : 'high'    mandatory question missing
        """
        added_opt_lookup = (
            added
            .with_columns([
                pl.col("Q Name").cast(pl.Utf8).str.strip_chars().alias("_q"),
                pl.when(pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.starts_with("o_"))
                .then(pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.slice(2))
                .otherwise(pl.col("Q Name").cast(pl.Utf8).str.strip_chars())
                .str.to_lowercase()
                .alias("_core"),
            ])
            .filter(pl.col("_q").str.starts_with("o_"))
            .select(["_core", pl.col("Q Name").alias("_optional_qname")])
            .unique(subset=["_core"], keep="first")
        )

        if reference_questions is not None and "Mandatory" in reference_questions.columns:
            removed_aug = (
                removed.join(
                    reference_questions.select(["Q Name", "Mandatory"]),
                    on="Q Name", how="left"
                )
                .with_columns(
                    pl.when(pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.starts_with("o_"))
                    .then(pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.slice(2))
                    .otherwise(pl.col("Q Name").cast(pl.Utf8).str.strip_chars())
                    .str.to_lowercase()
                    .alias("_core")
                )
            )
            severity_expr = (
                pl.when(normalize_mandatory_expr("Mandatory") == "yes")
                .then(pl.lit("high"))
                .otherwise(pl.lit("info"))
                .alias("severity")
            )
            moved_to_optional = (
                removed_aug
                .join(added_opt_lookup, on="_core", how="inner")
                .filter(normalize_mandatory_expr("Mandatory") == "yes")
            )
        else:
            removed_aug = removed.with_columns([
                pl.lit("").alias("Mandatory"),
                pl.when(pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.starts_with("o_"))
                .then(pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.slice(2))
                .otherwise(pl.col("Q Name").cast(pl.Utf8).str.strip_chars())
                .str.to_lowercase()
                .alias("_core"),
            ])
            severity_expr = (
                pl.when(pl.col("is_optional")).then(pl.lit("info")).otherwise(pl.lit("high"))
                .alias("severity")
            )
            moved_to_optional = pl.DataFrame(schema={
                "Q Name": pl.Utf8, "is_optional": pl.Boolean, "Mandatory": pl.Utf8,
                "_core": pl.Utf8, "_optional_qname": pl.Utf8,
            })

        moved_issues = (
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
        added_issues = added_base.with_columns([
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
        removed_issues = removed_base.with_columns([
            pl.lit("removed_question").alias("issue_type"),
            pl.lit("").alias("set_name"),
            pl.lit("Q Name").alias("field"),
            pl.lit("missing_in_current").alias("current"),
            pl.lit("present").alias("reference"),
            severity_expr,
            pl.lit(None).cast(pl.Int64).alias("excel_row"),
        ]).select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])

        return pl.concat([added_issues, removed_issues, moved_issues], how="vertical")
    ```

### `make_mandatory_issues` {#fn-make-mandatory-issues-3045}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3045`

**Signature**

```python
def make_mandatory_issues(mandatory_diff: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Converts mandatory mismatches into the common issues schema.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `mandatory_diff` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def make_mandatory_issues(mandatory_diff: pl.DataFrame) -> pl.DataFrame:
        """Converts mandatory mismatches into the common issues schema."""
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

### `make_option_issues` {#fn-make-option-issues-3059}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3059`

**Signature**

```python
def make_option_issues(option_diff: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Converts option label mismatches into the common issues schema.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `option_diff` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def make_option_issues(option_diff: pl.DataFrame) -> pl.DataFrame:
        """Converts option label mismatches into the common issues schema."""
        return (
            option_diff
            .with_columns([
                pl.lit("").alias("set_name"),
                pl.col("option_label").alias("current"),
                pl.col("option_label_ref").alias("reference"),
                pl.lit("medium").alias("severity"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `make_option_presence_issues` {#fn-make-option-presence-issues-3077}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3077`

**Signature**

```python
def make_option_presence_issues(added_options: pl.DataFrame, removed_options: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Converts added/removed options into the common issues schema.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `added_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `removed_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def make_option_presence_issues(added_options: pl.DataFrame, removed_options: pl.DataFrame) -> pl.DataFrame:
        """Converts added/removed options into the common issues schema."""
        added_issues = added_options.with_columns([
            pl.lit("").alias("set_name"),
            pl.col("option_label").alias("current"),
            pl.lit(_not_in_reference_text()).alias("reference"),
            pl.lit("medium").alias("severity"),
            pl.lit(None).cast(pl.Int64).alias("excel_row"),
        ]).select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])

        removed_issues = removed_options.with_columns([
            pl.lit("").alias("set_name"),
            pl.lit("(removed)").alias("current"),
            pl.col("option_label").alias("reference"),
            pl.lit("high").alias("severity"),
            pl.lit(None).cast(pl.Int64).alias("excel_row"),
        ]).select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])

        return pl.concat([added_issues, removed_issues], how="vertical")
    ```

### `build_option_changes_view` {#fn-build-option-changes-view-3098}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3098`

**Signature**

```python
def build_option_changes_view(en_option_diff: pl.DataFrame, en_added_options: pl.DataFrame, en_removed_options: pl.DataFrame, en_code_renumber: pl.DataFrame, tgt_option_diff: pl.DataFrame, tgt_added_options: pl.DataFrame, tgt_removed_options: pl.DataFrame, tgt_code_renumber: pl.DataFrame, target_lang: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Builds Option Changes rows with independent EN and target-language checks.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `en_option_diff` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |
| `en_added_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `en_removed_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `en_code_renumber` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |
| `tgt_option_diff` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |
| `tgt_added_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `tgt_removed_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `tgt_code_renumber` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |
| `target_lang` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def build_option_changes_view(
        en_option_diff: pl.DataFrame,
        en_added_options: pl.DataFrame,
        en_removed_options: pl.DataFrame,
        en_code_renumber: pl.DataFrame,
        tgt_option_diff: pl.DataFrame,
        tgt_added_options: pl.DataFrame,
        tgt_removed_options: pl.DataFrame,
        tgt_code_renumber: pl.DataFrame,
        target_lang: str,
    ) -> pl.DataFrame:
        """
        Builds Option Changes rows with independent EN and target-language checks.

        Layout policy:
        - Current value / Reference / rule are always EN baseline.
        - For non-EN runs, target language values are added in separate columns.
        """
        is_en = str(target_lang).upper() == "EN"

        def _scope_view(option_diff, added_opts, removed_opts, renumber_opts, scope):
            mismatch = option_diff.with_columns([
                pl.col("option_label").alias("current"),
                pl.col("option_label_ref").alias("reference"),
                pl.col("excel_row").cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            added = added_opts.with_columns([
                pl.col("option_label").alias("current"),
                pl.lit(_not_in_reference_text()).alias("reference"),
                pl.lit(None).cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            removed = removed_opts.with_columns([
                pl.lit("(removed)").alias("current"),
                pl.col("option_label").alias("reference"),
                pl.lit(None).cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            renumber = renumber_opts.with_columns([
                pl.concat_str([
                    pl.col("new_code").cast(pl.Utf8),
                    pl.lit(") "),
                    pl.col("option_label").cast(pl.Utf8),
                ]).alias("current"),
                pl.concat_str([
                    pl.col("old_code").cast(pl.Utf8),
                    pl.lit(") "),
                    pl.col("option_label_ref").cast(pl.Utf8),
                ]).alias("reference"),
                pl.col("excel_row").cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            base = pl.concat([mismatch, added, removed, renumber], how="vertical")
            return base.rename({
                "current": f"current_{scope.lower()}",
                "reference": f"reference_{scope.lower()}",
                "severity": f"severity_{scope.lower()}",
                "excel_row": f"excel_row_{scope.lower()}",
            })

        en_view = _scope_view(en_option_diff, en_added_options, en_removed_options, en_code_renumber, "EN")
        if is_en:
            return (
                en_view
                .with_columns([
                    pl.lit("").alias("set_name"),
                    pl.lit("EN").alias("lang_scope"),
                    pl.col("current_en").alias("current"),
                    pl.col("reference_en").alias("reference"),
                    pl.col("severity_en").alias("severity"),
                    pl.col("excel_row_en").alias("excel_row"),
                ])
                .select(["issue_type", "set_name", "Q Name", "field", "lang_scope", "current", "reference", "severity", "excel_row"])
            )

        tgt_view = _scope_view(tgt_option_diff, tgt_added_options, tgt_removed_options, tgt_code_renumber, "TGT")
        keys = ["issue_type", "Q Name", "field"]
        out = en_view.join(tgt_view, on=keys, how="full", suffix="_t")

        return (
            out
            .with_columns([
                pl.coalesce([pl.col("issue_type"), pl.col("issue_type_t")]).alias("issue_type"),
                pl.coalesce([pl.col("Q Name"), pl.col("Q Name_t")]).alias("Q Name"),
                pl.coalesce([pl.col("field"), pl.col("field_t")]).alias("field"),
                pl.lit("").alias("set_name"),
                pl.coalesce([pl.col("current_en"), pl.lit("")]).alias("current"),
                pl.coalesce([pl.col("reference_en"), pl.lit("")]).alias("reference"),
                pl.coalesce([pl.col("current_tgt"), pl.lit("")]).alias("current_lang"),
                pl.coalesce([pl.col("reference_tgt"), pl.lit("")]).alias("reference_lang"),
                pl.when(
                    ((pl.col("current_en").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
                     | (pl.col("reference_en").cast(pl.Utf8).fill_null("").str.strip_chars() != ""))
                    &
                    ((pl.col("current_tgt").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
                     | (pl.col("reference_tgt").cast(pl.Utf8).fill_null("").str.strip_chars() != ""))
                ).then(pl.lit(f"EN + {target_lang}"))
                .when(
                    (pl.col("current_en").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
                    | (pl.col("reference_en").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
                ).then(pl.lit("EN"))
                .when(
                    (pl.col("current_tgt").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
                    | (pl.col("reference_tgt").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
                ).then(pl.lit(target_lang))
                .otherwise(pl.lit("N/A"))
                .alias("lang_scope"),
                pl.when(pl.col("severity_tgt") == "high").then(pl.lit("high"))
                .when(pl.col("severity_en") == "high").then(pl.lit("high"))
                .when(pl.col("severity_tgt") == "medium").then(pl.lit("medium"))
                .when(pl.col("severity_en") == "medium").then(pl.lit("medium"))
                .otherwise(pl.lit("info")).alias("severity"),
                pl.coalesce([pl.col("excel_row_tgt"), pl.col("excel_row_en")]).alias("excel_row"),
            ])
            .select([
                "issue_type", "set_name", "Q Name", "field", "lang_scope", "current", "reference",
                "current_lang", "reference_lang", "severity", "excel_row",
            ])
        )
    ```

### `build_option_changes_view._scope_view` {#fn--scope-view-3118}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3118`

**Signature**

```python
def _scope_view(option_diff, added_opts, removed_opts, renumber_opts, scope):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `option_diff` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 Issue unifiers` stage. |
| `added_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 Issue unifiers` stage. |
| `removed_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 Issue unifiers` stage. |
| `renumber_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 Issue unifiers` stage. |
| `scope` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _scope_view(option_diff, added_opts, removed_opts, renumber_opts, scope):
            mismatch = option_diff.with_columns([
                pl.col("option_label").alias("current"),
                pl.col("option_label_ref").alias("reference"),
                pl.col("excel_row").cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            added = added_opts.with_columns([
                pl.col("option_label").alias("current"),
                pl.lit(_not_in_reference_text()).alias("reference"),
                pl.lit(None).cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            removed = removed_opts.with_columns([
                pl.lit("(removed)").alias("current"),
                pl.col("option_label").alias("reference"),
                pl.lit(None).cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            renumber = renumber_opts.with_columns([
                pl.concat_str([
                    pl.col("new_code").cast(pl.Utf8),
                    pl.lit(") "),
                    pl.col("option_label").cast(pl.Utf8),
                ]).alias("current"),
                pl.concat_str([
                    pl.col("old_code").cast(pl.Utf8),
                    pl.lit(") "),
                    pl.col("option_label_ref").cast(pl.Utf8),
                ]).alias("reference"),
                pl.col("excel_row").cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            base = pl.concat([mismatch, added, removed, renumber], how="vertical")
            return base.rename({
                "current": f"current_{scope.lower()}",
                "reference": f"reference_{scope.lower()}",
                "severity": f"severity_{scope.lower()}",
                "excel_row": f"excel_row_{scope.lower()}",
            })
    ```

### `collapse_removed_option_with_cascading_drift` {#fn-collapse-removed-option-with-cascading-drift-3220}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3220`

**Signature**

```python
def collapse_removed_option_with_cascading_drift(option_changes_view: pl.DataFrame, current_lookup_en: dict[str, list[tuple[str, str]]] | None=None, reference_lookup_en: dict[str, list[tuple[str, str]]] | None=None, current_lookup_tgt: dict[str, list[tuple[str, str]]] | None=None, reference_lookup_tgt: dict[str, list[tuple[str, str]]] | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Apply precedence between structural option changes and drift:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `option_changes_view` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `current_lookup_en` | positional_or_keyword | No | `None` | `dict[str, list[tuple[str, str]]] | None` | Input used by the `Step 8 Issue unifiers` stage. |
| `reference_lookup_en` | positional_or_keyword | No | `None` | `dict[str, list[tuple[str, str]]] | None` | Input used by the `Step 8 Issue unifiers` stage. |
| `current_lookup_tgt` | positional_or_keyword | No | `None` | `dict[str, list[tuple[str, str]]] | None` | Input used by the `Step 8 Issue unifiers` stage. |
| `reference_lookup_tgt` | positional_or_keyword | No | `None` | `dict[str, list[tuple[str, str]]] | None` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def collapse_removed_option_with_cascading_drift(
        option_changes_view: pl.DataFrame,
        current_lookup_en: dict[str, list[tuple[str, str]]] | None = None,
        reference_lookup_en: dict[str, list[tuple[str, str]]] | None = None,
        current_lookup_tgt: dict[str, list[tuple[str, str]]] | None = None,
        reference_lookup_tgt: dict[str, list[tuple[str, str]]] | None = None,
    ) -> pl.DataFrame:
        """
        Apply precedence between structural option changes and drift:
          - structural (add/remove) + drift => drift is reclassified as a combined
            causal issue and structural rows are suppressed for that question.
          - structural-only => keep structural rows.
          - drift-only => keep pure option_position_drift.
          - label mismatches are suppressed whenever structural changes exist for
            the same question (to avoid double-reporting replacements as relabels).
        """
        if option_changes_view.height == 0:
            return option_changes_view
        if not {"issue_type", "Q Name"}.issubset(set(option_changes_view.columns)):
            return option_changes_view

        structural_types = {"added_option", "removed_option", "added_removed_option"}

        def _norm_label(v: str) -> str:
            txt = str(v or "").strip().lower()
            txt = re.sub(r"\s+", " ", txt)
            return txt

        def _infer_drift_from_lookups(q_name: str) -> bool:
            qk = str(q_name or "").strip().lower()
            cur_en = (current_lookup_en or {}).get(qk, [])
            ref_en = (reference_lookup_en or {}).get(qk, [])
            cur_tgt = (current_lookup_tgt or {}).get(qk, [])
            ref_tgt = (reference_lookup_tgt or {}).get(qk, [])

            # Prefer EN baseline when available; fallback to target-language entries.
            cur_entries = cur_en if cur_en and ref_en else cur_tgt
            ref_entries = ref_en if cur_en and ref_en else ref_tgt
            if not cur_entries or not ref_entries:
                return False

            cur_map: dict[str, str] = {}
            ref_map: dict[str, str] = {}
            for code, label in cur_entries:
                k = _norm_label(label)
                if k and k not in cur_map:
                    cur_map[k] = str(code or "").strip()
            for code, label in ref_entries:
                k = _norm_label(label)
                if k and k not in ref_map:
                    ref_map[k] = str(code or "").strip()

            common = set(cur_map.keys()) & set(ref_map.keys())
            if not common:
                return False
            return any(cur_map[k] != ref_map[k] for k in common)
        rows = option_changes_view.to_dicts()
        by_q: dict[str, list[dict]] = {}
        for rd in rows:
            q = str(rd.get("Q Name") or "").strip()
            if not q:
                continue
            by_q.setdefault(q, []).append(rd)

        q_with_structural: set[str] = set()
        q_with_combined_drift: dict[str, str] = {}
        for q, items in by_q.items():
            types = {str(r.get("issue_type") or "").strip() for r in items}
            has_added = "added_option" in types
            has_removed = "removed_option" in types
            has_both_merged = "added_removed_option" in types
            has_structural = has_added or has_removed or has_both_merged
            has_drift = "option_position_drift" in types or _infer_drift_from_lookups(q)
            if has_structural:
                q_with_structural.add(q)
            if has_structural and has_drift:
                if has_both_merged or (has_added and has_removed):
                    q_with_combined_drift[q] = "added_removed_option_with_drift"
                elif has_added:
                    q_with_combined_drift[q] = "added_option_with_drift"
                else:
                    q_with_combined_drift[q] = "removed_option_with_drift"

        if not q_with_structural and not q_with_combined_drift:
            return option_changes_view

        out_rows: list[dict] = []
        for rd in rows:
            q = str(rd.get("Q Name") or "").strip()
            it = str(rd.get("issue_type") or "").strip()

            # If structural changes exist, label-mismatch rows are derivative noise.
            if q in q_with_structural and it == "option_label_mismatch":
                continue

            # For structural+drift questions, keep one combined drift-causal type.
            if q in q_with_combined_drift:
                if it == "option_position_drift":
                    nr = dict(rd)
                    nr["issue_type"] = q_with_combined_drift[q]
                    nr["severity"] = "high"
                    out_rows.append(nr)
                    continue
                if it in structural_types:
                    continue

            out_rows.append(rd)

        if not out_rows:
            return pl.DataFrame(schema=option_changes_view.schema)

        out_df = pl.DataFrame(out_rows)
        for col in option_changes_view.columns:
            if col not in out_df.columns:
                out_df = out_df.with_columns(pl.lit(None).alias(col))
        return out_df.select(option_changes_view.columns)
    ```

### `collapse_removed_option_with_cascading_drift._norm_label` {#fn--norm-label-3243}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3243`

**Signature**

```python
def _norm_label(v: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `v` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _norm_label(v: str) -> str:
            txt = str(v or "").strip().lower()
            txt = re.sub(r"\s+", " ", txt)
            return txt
    ```

### `collapse_removed_option_with_cascading_drift._infer_drift_from_lookups` {#fn--infer-drift-from-lookups-3248}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3248`

**Signature**

```python
def _infer_drift_from_lookups(q_name: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `q_name` | positional_or_keyword | Yes | `-` | `str` | Question identifier used to join or compare records. |

??? note "Function source"

    ```python
    def _infer_drift_from_lookups(q_name: str) -> bool:
            qk = str(q_name or "").strip().lower()
            cur_en = (current_lookup_en or {}).get(qk, [])
            ref_en = (reference_lookup_en or {}).get(qk, [])
            cur_tgt = (current_lookup_tgt or {}).get(qk, [])
            ref_tgt = (reference_lookup_tgt or {}).get(qk, [])

            # Prefer EN baseline when available; fallback to target-language entries.
            cur_entries = cur_en if cur_en and ref_en else cur_tgt
            ref_entries = ref_en if cur_en and ref_en else ref_tgt
            if not cur_entries or not ref_entries:
                return False

            cur_map: dict[str, str] = {}
            ref_map: dict[str, str] = {}
            for code, label in cur_entries:
                k = _norm_label(label)
                if k and k not in cur_map:
                    cur_map[k] = str(code or "").strip()
            for code, label in ref_entries:
                k = _norm_label(label)
                if k and k not in ref_map:
                    ref_map[k] = str(code or "").strip()

            common = set(cur_map.keys()) & set(ref_map.keys())
            if not common:
                return False
            return any(cur_map[k] != ref_map[k] for k in common)
    ```

### `_join_limited_tokens` {#fn--join-limited-tokens-3338}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3338`

**Signature**

```python
def _join_limited_tokens(items, limit=20):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `items` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 Issue unifiers` stage. |
| `limit` | positional_or_keyword | No | `20` | `-` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _join_limited_tokens(items, limit=20):
        vals = []
        seen = set()
        for raw in items or []:
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

### `_option_code_sort_key` {#fn--option-code-sort-key-3354}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3354`

**Signature**

```python
def _option_code_sort_key(raw):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `raw` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _option_code_sort_key(raw):
        txt = str(raw or "").strip()
        if re.fullmatch(r"\d+", txt):
            return (0, int(txt))
        return (1, txt.lower())
    ```

### `_format_option_entries` {#fn--format-option-entries-3361}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3361`

**Signature**

```python
def _format_option_entries(entries: list[tuple[str, str]], header: str, empty_label: str='(empty)', include_code: bool=False) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 8 Issue unifiers` stage. |
| `header` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |
| `empty_label` | positional_or_keyword | No | `'(empty)'` | `str` | Input used by the `Step 8 Issue unifiers` stage. |
| `include_code` | positional_or_keyword | No | `False` | `bool` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _format_option_entries(
        entries: list[tuple[str, str]],
        header: str,
        empty_label: str = "(empty)",
        include_code: bool = False,
    ) -> str:
        if not entries:
            return f"{header}:\n{empty_label}"
        out = []
        seen = set()
        idx = 0
        for code_raw, label_raw in entries:
            code = str(code_raw or "").strip()
            label = str(label_raw or "").strip()
            if not code and not label:
                continue
            key = (code, label)
            if key in seen:
                continue
            seen.add(key)
            idx += 1
            if include_code and code:
                out.append(f"{code} | {label or '(blank)'}")
            elif include_code:
                out.append(f"(blank) | {label or '(blank)'}")
            else:
                out.append(f"{idx} | {label or code or '(blank)'}")
        if not out:
            return f"{header}:\n{empty_label}"
        return f"{header}:\n" + "\n".join(out)
    ```

### `_build_option_lookup_by_qname` {#fn--build-option-lookup-by-qname-3393}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3393`

**Signature**

```python
def _build_option_lookup_by_qname(options_df: pl.DataFrame | None) -> dict[str, list[tuple[str, str]]]:
```

**Returns:** `dict[str, list[tuple[str, str]]]`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `options_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def _build_option_lookup_by_qname(options_df: pl.DataFrame | None) -> dict[str, list[tuple[str, str]]]:
        out: dict[str, list[tuple[str, str]]] = {}
        if options_df is None or options_df.height == 0:
            return out
        if not {"Q Name", "option_code", "option_label"}.issubset(set(options_df.columns)):
            return out
        seen_per_q = {}
        for row in options_df.select(["Q Name", "option_code", "option_label"]).iter_rows(named=True):
            q = str(row.get("Q Name") or "").strip()
            if not q:
                continue
            qk = q.lower()
            code = str(row.get("option_code") or "").strip()
            label = str(row.get("option_label") or "").strip()
            if not code and not label:
                continue
            ckey = (code.lower(), label.lower())
            seen = seen_per_q.setdefault(qk, set())
            if ckey in seen:
                continue
            seen.add(ckey)
            out.setdefault(qk, []).append((code, label))
        return out
    ```

### `_format_code_entries` {#fn--format-code-entries-3418}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3418`

**Signature**

```python
def _format_code_entries(entries: list[tuple[str, str]], header: str, empty_label: str='(empty)') -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 8 Issue unifiers` stage. |
| `header` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |
| `empty_label` | positional_or_keyword | No | `'(empty)'` | `str` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _format_code_entries(
        entries: list[tuple[str, str]],
        header: str,
        empty_label: str = "(empty)",
    ) -> str:
        if not entries:
            return f"{header}:\n{empty_label}"
        out = []
        seen = set()
        for code_raw, token_raw in entries:
            code = str(code_raw or "").strip()
            token = str(token_raw or "").strip()
            if not code and not token:
                continue
            key = (code, token)
            if key in seen:
                continue
            seen.add(key)
            out.append(f"{code or '(blank)'} | {token or '(blank)'}")
        if not out:
            return f"{header}:\n{empty_label}"
        return f"{header}:\n" + "\n".join(out)
    ```

### `_build_codes_lookup_by_qname` {#fn--build-codes-lookup-by-qname-3442}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3442`

**Signature**

```python
def _build_codes_lookup_by_qname(codes_df: pl.DataFrame | None) -> dict[str, list[tuple[str, str]]]:
```

**Returns:** `dict[str, list[tuple[str, str]]]`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `codes_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame | None` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _build_codes_lookup_by_qname(codes_df: pl.DataFrame | None) -> dict[str, list[tuple[str, str]]]:
        out: dict[str, list[tuple[str, str]]] = {}
        if codes_df is None or codes_df.height == 0:
            return out
        if not {"Q Name", "code_num", "code_token"}.issubset(set(codes_df.columns)):
            return out
        src = (
            codes_df
            .select([
                pl.col("Q Name").cast(pl.Utf8).fill_null(""),
                pl.col("code_num").cast(pl.Int64),
                pl.col("code_token").cast(pl.Utf8).fill_null(""),
            ])
            .sort(["Q Name", "code_num", "code_token"])
        )
        seen_per_q: dict[str, set[tuple[str, str]]] = {}
        for row in src.iter_rows(named=True):
            q = str(row.get("Q Name") or "").strip()
            if not q:
                continue
            qk = q.lower()
            num = str(row.get("code_num") or "").strip()
            tok = str(row.get("code_token") or "").strip()
            if not num and not tok:
                continue
            key_norm = (num.lower(), tok.lower())
            seen = seen_per_q.setdefault(qk, set())
            if key_norm in seen:
                continue
            seen.add(key_norm)
            out.setdefault(qk, []).append((num, tok))
        return out
    ```

### `enrich_codes_issue_lists` {#fn-enrich-codes-issue-lists-3476}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3476`

**Signature**

```python
def enrich_codes_issue_lists(codes_df: pl.DataFrame, current_codes: pl.DataFrame | None, reference_codes: pl.DataFrame | None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Ensure all code-related issue rows show full current/reference code lists.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `codes_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |
| `current_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame | None` | Input used by the `Step 8 Issue unifiers` stage. |
| `reference_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame | None` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def enrich_codes_issue_lists(
        codes_df: pl.DataFrame,
        current_codes: pl.DataFrame | None,
        reference_codes: pl.DataFrame | None,
    ) -> pl.DataFrame:
        """
        Ensure all code-related issue rows show full current/reference code lists.
        Keeps existing diagnostic text and appends formatted lists for readability.
        """
        if codes_df is None or codes_df.height == 0:
            return codes_df
        if not {"issue_type", "Q Name", "current", "reference"}.issubset(set(codes_df.columns)):
            return codes_df

        code_issue_types = {
            "codes_token_mismatch",
            "codes_removed",
            "codes_added",
            "codes_position_drift",
            "added_removed_codes",
            "added_codes_with_drift",
            "removed_codes_with_drift",
            "added_removed_codes_with_drift",
        }
        cur_lookup = _build_codes_lookup_by_qname(current_codes)
        ref_lookup = _build_codes_lookup_by_qname(reference_codes)

        def _norm_pair(code_raw: str, tok_raw: str) -> tuple[str, str]:
            return (str(code_raw or "").strip().lower(), str(tok_raw or "").strip().lower())

        def _format_code_entries_marked(
            entries: list[tuple[str, str]],
            header: str,
            mark_pairs: set[tuple[str, str]] | None = None,
            marker: str = "",
        ) -> str:
            if not entries:
                return f"{header}:\n(empty)"
            out = []
            seen = set()
            for code_raw, token_raw in entries:
                code = str(code_raw or "").strip()
                token = str(token_raw or "").strip()
                if not code and not token:
                    continue
                nk = _norm_pair(code, token)
                if nk in seen:
                    continue
                seen.add(nk)
                suffix = f" [{marker}]" if marker and mark_pairs and nk in mark_pairs else ""
                out.append(f"{code or '(blank)'} | {token or '(blank)'}{suffix}")
            if not out:
                return f"{header}:\n(empty)"
            return f"{header}:\n" + "\n".join(out)

        out_rows: list[dict] = []
        for rd in codes_df.to_dicts():
            issue_type = str(rd.get("issue_type") or "").strip()
            if issue_type not in code_issue_types:
                out_rows.append(rd)
                continue

            q = str(rd.get("Q Name") or "").strip()
            if not q or "," in q:
                out_rows.append(rd)
                continue

            qk = q.lower()
            cur_entries = cur_lookup.get(qk, [])
            ref_entries = ref_lookup.get(qk, [])
            if not cur_entries and not ref_entries:
                out_rows.append(rd)
                continue

            cur_pairs = {_norm_pair(c, t) for c, t in cur_entries}
            ref_pairs = {_norm_pair(c, t) for c, t in ref_entries}
            added_pairs = cur_pairs - ref_pairs
            removed_pairs = ref_pairs - cur_pairs

            mark_added_current = issue_type in {
                "codes_added",
                "added_codes_with_drift",
                "added_removed_codes",
                "added_removed_codes_with_drift",
            }
            mark_removed_reference = issue_type in {
                "codes_removed",
                "removed_codes_with_drift",
                "added_removed_codes",
                "added_removed_codes_with_drift",
            }

            cur_list = _format_code_entries_marked(
                cur_entries,
                "Current list (code | token)",
                mark_pairs=(added_pairs if mark_added_current else set()),
                marker="ADDED CODE",
            )
            ref_list = _format_code_entries_marked(
                ref_entries,
                "Reference list (code | token)",
                mark_pairs=(removed_pairs if mark_removed_reference else set()),
                marker="REMOVED CODE",
            )
            cur_diag = str(rd.get("current") or "").strip()
            ref_diag = str(rd.get("reference") or "").strip()

            rd["current"] = f"{cur_diag}\n\n{cur_list}" if cur_diag else cur_list
            rd["reference"] = f"{ref_diag}\n\n{ref_list}" if ref_diag else ref_list
            out_rows.append(rd)

        out = pl.DataFrame(out_rows) if out_rows else pl.DataFrame(schema=codes_df.schema)
        for col in codes_df.columns:
            if col not in out.columns:
                out = out.with_columns(pl.lit(None).alias(col))
        return out.select(codes_df.columns)
    ```

### `enrich_codes_issue_lists._norm_pair` {#fn--norm-pair-3503}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3503`

**Signature**

```python
def _norm_pair(code_raw: str, tok_raw: str) -> tuple[str, str]:
```

**Returns:** `tuple[str, str]`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `code_raw` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |
| `tok_raw` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _norm_pair(code_raw: str, tok_raw: str) -> tuple[str, str]:
            return (str(code_raw or "").strip().lower(), str(tok_raw or "").strip().lower())
    ```

### `enrich_codes_issue_lists._format_code_entries_marked` {#fn--format-code-entries-marked-3506}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3506`

**Signature**

```python
def _format_code_entries_marked(entries: list[tuple[str, str]], header: str, mark_pairs: set[tuple[str, str]] | None=None, marker: str='') -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 8 Issue unifiers` stage. |
| `header` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |
| `mark_pairs` | positional_or_keyword | No | `None` | `set[tuple[str, str]] | None` | Input used by the `Step 8 Issue unifiers` stage. |
| `marker` | positional_or_keyword | No | `''` | `str` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _format_code_entries_marked(
            entries: list[tuple[str, str]],
            header: str,
            mark_pairs: set[tuple[str, str]] | None = None,
            marker: str = "",
        ) -> str:
            if not entries:
                return f"{header}:\n(empty)"
            out = []
            seen = set()
            for code_raw, token_raw in entries:
                code = str(code_raw or "").strip()
                token = str(token_raw or "").strip()
                if not code and not token:
                    continue
                nk = _norm_pair(code, token)
                if nk in seen:
                    continue
                seen.add(nk)
                suffix = f" [{marker}]" if marker and mark_pairs and nk in mark_pairs else ""
                out.append(f"{code or '(blank)'} | {token or '(blank)'}{suffix}")
            if not out:
                return f"{header}:\n(empty)"
            return f"{header}:\n" + "\n".join(out)
    ```

### `_extract_option_codes_from_field` {#fn--extract-option-codes-from-field-3594}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3594`

**Signature**

```python
def _extract_option_codes_from_field(rows: list[dict]) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `rows` | positional_or_keyword | Yes | `-` | `list[dict]` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _extract_option_codes_from_field(rows: list[dict]) -> list[str]:
        out = []
        seen = set()
        for r in rows:
            fld = str(r.get("field") or "").strip()
            m = re.match(r"option_(.+)$", fld)
            token = m.group(1).strip() if m else fld
            if not token:
                continue
            key = token.lower()
            if key in seen:
                continue
            seen.add(key)
            out.append(token)
        return out
    ```

### `_combine_lang_scope` {#fn--combine-lang-scope-3611}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3611`

**Signature**

```python
def _combine_lang_scope(values: list[str], target_lang: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `values` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 8 Issue unifiers` stage. |
| `target_lang` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _combine_lang_scope(values: list[str], target_lang: str) -> str:
        tgt = str(target_lang or "").upper().strip()
        has_en = False
        has_tgt = False
        for raw in values or []:
            txt = str(raw or "").strip().upper().replace(" ", "")
            if not txt or txt == "N/A":
                continue
            if "EN+" in txt or "+EN" in txt:
                has_en = True
            if "EN" == txt:
                has_en = True
            if tgt and (f"+{tgt}" in txt or f"{tgt}+" in txt or txt == tgt):
                has_tgt = True
            if txt == "EN":
                has_en = True
        if has_en and has_tgt and tgt:
            return f"EN + {tgt}"
        if has_en:
            return "EN"
        if has_tgt and tgt:
            return tgt
        return "N/A"
    ```

### `_option_scope_flags` {#fn--option-scope-flags-3636}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3636`

**Signature**

```python
def _option_scope_flags(lang_scope: str, has_lang_cols: bool, target_lang: str) -> tuple[bool, bool]:
```

**Returns:** `tuple[bool, bool]`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `lang_scope` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `has_lang_cols` | positional_or_keyword | Yes | `-` | `bool` | Input used by the `Step 8 Issue unifiers` stage. |
| `target_lang` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _option_scope_flags(lang_scope: str, has_lang_cols: bool, target_lang: str) -> tuple[bool, bool]:
        txt = str(lang_scope or "").strip().upper().replace(" ", "")
        tgt = str(target_lang or "").upper().strip()
        show_en = ("EN" in txt) or (not has_lang_cols)
        show_tgt = bool(has_lang_cols and tgt and (txt == tgt or f"+{tgt}" in txt or f"{tgt}+" in txt))
        if has_lang_cols and not show_en and not show_tgt:
            show_en = True
        return show_en, show_tgt
    ```

### `_option_label_delta_tokens` {#fn--option-label-delta-tokens-3646}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3646`

**Signature**

```python
def _option_label_delta_tokens(current_entries: list[tuple[str, str]], reference_entries: list[tuple[str, str]], kind: str) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 8 Issue unifiers` stage. |
| `reference_entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 8 Issue unifiers` stage. |
| `kind` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _option_label_delta_tokens(
        current_entries: list[tuple[str, str]],
        reference_entries: list[tuple[str, str]],
        kind: str,
    ) -> list[str]:
        cur_map = {str(c or "").strip().lower(): str(l or "").strip() for c, l in current_entries if str(c or "").strip()}
        ref_map = {str(c or "").strip().lower(): str(l or "").strip() for c, l in reference_entries if str(c or "").strip()}
        if kind == "added":
            keys = [str(c or "").strip().lower() for c, _ in current_entries if str(c or "").strip()]
            return [cur_map[k] or k for k in keys if k not in ref_map]
        if kind == "removed":
            keys = [str(c or "").strip().lower() for c, _ in reference_entries if str(c or "").strip()]
            return [ref_map[k] or k for k in keys if k not in cur_map]
        return []
    ```

### `merge_added_removed_option_rows` {#fn-merge-added-removed-option-rows-3662}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3662`

**Signature**

```python
def merge_added_removed_option_rows(option_changes_view: pl.DataFrame, current_lookup_en: dict[str, list[tuple[str, str]]] | None=None, reference_lookup_en: dict[str, list[tuple[str, str]]] | None=None, current_lookup_tgt: dict[str, list[tuple[str, str]]] | None=None, reference_lookup_tgt: dict[str, list[tuple[str, str]]] | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Merge same-question added+removed option rows into one report-facing row.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `option_changes_view` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `current_lookup_en` | positional_or_keyword | No | `None` | `dict[str, list[tuple[str, str]]] | None` | Input used by the `Step 8 Issue unifiers` stage. |
| `reference_lookup_en` | positional_or_keyword | No | `None` | `dict[str, list[tuple[str, str]]] | None` | Input used by the `Step 8 Issue unifiers` stage. |
| `current_lookup_tgt` | positional_or_keyword | No | `None` | `dict[str, list[tuple[str, str]]] | None` | Input used by the `Step 8 Issue unifiers` stage. |
| `reference_lookup_tgt` | positional_or_keyword | No | `None` | `dict[str, list[tuple[str, str]]] | None` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def merge_added_removed_option_rows(
        option_changes_view: pl.DataFrame,
        current_lookup_en: dict[str, list[tuple[str, str]]] | None = None,
        reference_lookup_en: dict[str, list[tuple[str, str]]] | None = None,
        current_lookup_tgt: dict[str, list[tuple[str, str]]] | None = None,
        reference_lookup_tgt: dict[str, list[tuple[str, str]]] | None = None,
    ) -> pl.DataFrame:
        """
        Merge same-question added+removed option rows into one report-facing row.
        """
        df = option_changes_view
        if df is None or df.height == 0:
            return df
        if not {"issue_type", "Q Name", "field"}.issubset(set(df.columns)):
            return df

        target = df.filter(pl.col("issue_type").is_in(["added_option", "removed_option"]))
        if target.height == 0:
            return df

        keys = (
            target
            .group_by(["Q Name"])
            .agg([
                (pl.col("issue_type") == "added_option").any().alias("_has_added"),
                (pl.col("issue_type") == "removed_option").any().alias("_has_removed"),
            ])
            .filter(pl.col("_has_added") & pl.col("_has_removed"))
            .select(["Q Name"])
        )
        if keys.height == 0:
            return df

        has_lang_cols = "current_lang" in df.columns and "reference_lang" in df.columns
        target_lang = str(globals().get("target_lang", "")).upper().strip()
        merged_rows = []
        for k in keys.to_dicts():
            q = str(k.get("Q Name") or "")
            if not q:
                continue
            qk = q.lower()
            sub = target.filter(pl.col("Q Name") == q)
            added_rows = sub.filter(pl.col("issue_type") == "added_option").to_dicts()
            removed_rows = sub.filter(pl.col("issue_type") == "removed_option").to_dicts()
            if not added_rows or not removed_rows:
                continue

            cur_entries_en = (current_lookup_en or {}).get(qk, [])
            ref_entries_en = (reference_lookup_en or {}).get(qk, [])
            cur_entries_tgt = (current_lookup_tgt or {}).get(qk, [])
            ref_entries_tgt = (reference_lookup_tgt or {}).get(qk, [])

            severities = [str(r.get("severity") or "").strip().lower() for r in (added_rows + removed_rows)]
            sev = "info"
            if "high" in severities:
                sev = "high"
            elif "medium" in severities:
                sev = "medium"

            excel_rows = [r.get("excel_row") for r in (added_rows + removed_rows) if r.get("excel_row") is not None]
            lang_scopes = [str(r.get("lang_scope") or "").strip() for r in (added_rows + removed_rows)]
            lang_scope = _combine_lang_scope(lang_scopes, target_lang)
            show_en, show_tgt = _option_scope_flags(lang_scope, has_lang_cols, target_lang)

            cur_entries = cur_entries_en if show_en else cur_entries_tgt
            ref_entries = ref_entries_en if show_en else ref_entries_tgt
            added_labels = _option_label_delta_tokens(cur_entries, ref_entries, "added")
            removed_labels = _option_label_delta_tokens(cur_entries, ref_entries, "removed")
            if show_en and show_tgt:
                added_labels = _option_label_delta_tokens(cur_entries_en, ref_entries_en, "added") + _option_label_delta_tokens(cur_entries_tgt, ref_entries_tgt, "added")
                removed_labels = _option_label_delta_tokens(cur_entries_en, ref_entries_en, "removed") + _option_label_delta_tokens(cur_entries_tgt, ref_entries_tgt, "removed")
            if not added_labels:
                added_labels = _extract_option_codes_from_field(added_rows)
            if not removed_labels:
                removed_labels = _extract_option_codes_from_field(removed_rows)

            added_txt = _join_limited_tokens(added_labels, limit=30)
            removed_txt = _join_limited_tokens(removed_labels, limit=30)
            cur_total = len(cur_entries)
            ref_total = len(ref_entries)
            detail = (
                f"both added and removed options: added={len(added_rows)}, removed={len(removed_rows)}; "
                f"current total={cur_total}, reference total={ref_total} "
                f"(added: {added_txt}; removed: {removed_txt})"
            )

            row = {
                "issue_type": "added_removed_option",
                "set_name": "",
                "Q Name": q,
                "field": detail,
                "lang_scope": lang_scope,
                "current": _format_option_entries(cur_entries_en, "Current list (option label)") if show_en else "",
                "reference": _format_option_entries(ref_entries_en, "Reference list (option label)") if show_en else "",
                "severity": sev,
                "excel_row": min(excel_rows) if excel_rows else None,
            }
            if has_lang_cols:
                row["current_lang"] = _format_option_entries(cur_entries_tgt, "Current list (option label)") if show_tgt else ""
                row["reference_lang"] = _format_option_entries(ref_entries_tgt, "Reference list (option label)") if show_tgt else ""
            merged_rows.append(row)

        if not merged_rows:
            return df

        merged_df = pl.DataFrame(merged_rows)
        for col in df.columns:
            if col not in merged_df.columns:
                merged_df = merged_df.with_columns(pl.lit(None).alias(col))
        merged_df = merged_df.select(df.columns)
        keep = df.join(keys, on=["Q Name"], how="anti")
        return pl.concat([keep, merged_df], how="vertical")
    ```

### `collapse_option_issue_rows_by_qname` {#fn-collapse-option-issue-rows-by-qname-3776}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3776`

**Signature**

```python
def collapse_option_issue_rows_by_qname(df: pl.DataFrame, issue_types: list[str], current_lookup_en: dict[str, list[tuple[str, str]]] | None=None, reference_lookup_en: dict[str, list[tuple[str, str]]] | None=None, current_lookup_tgt: dict[str, list[tuple[str, str]]] | None=None, reference_lookup_tgt: dict[str, list[tuple[str, str]]] | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Collapse per-option rows into stable per-question issue rows with precedence:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `issue_types` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 8 Issue unifiers` stage. |
| `current_lookup_en` | positional_or_keyword | No | `None` | `dict[str, list[tuple[str, str]]] | None` | Input used by the `Step 8 Issue unifiers` stage. |
| `reference_lookup_en` | positional_or_keyword | No | `None` | `dict[str, list[tuple[str, str]]] | None` | Input used by the `Step 8 Issue unifiers` stage. |
| `current_lookup_tgt` | positional_or_keyword | No | `None` | `dict[str, list[tuple[str, str]]] | None` | Input used by the `Step 8 Issue unifiers` stage. |
| `reference_lookup_tgt` | positional_or_keyword | No | `None` | `dict[str, list[tuple[str, str]]] | None` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def collapse_option_issue_rows_by_qname(
        df: pl.DataFrame,
        issue_types: list[str],
        current_lookup_en: dict[str, list[tuple[str, str]]] | None = None,
        reference_lookup_en: dict[str, list[tuple[str, str]]] | None = None,
        current_lookup_tgt: dict[str, list[tuple[str, str]]] | None = None,
        reference_lookup_tgt: dict[str, list[tuple[str, str]]] | None = None,
    ) -> pl.DataFrame:
        """
        Collapse per-option rows into stable per-question issue rows with precedence:
        structural changes first, then drift context, then pure label/drift.
        """
        if df is None or df.height == 0:
            return df
        if not {"issue_type", "Q Name"}.issubset(set(df.columns)):
            return df
        target = set(issue_types or [])
        if not target:
            return df

        mask = pl.col("issue_type").is_in(list(target))
        keep_df = df.filter(~mask)
        noisy = df.filter(mask)
        if noisy.height == 0:
            return df

        has_lang_cols = "current_lang" in noisy.columns and "reference_lang" in noisy.columns
        target_lang = str(globals().get("target_lang", "")).upper().strip()
        def _norm_label(txt: str) -> str:
            out = str(txt or "").strip().lower()
            out = re.sub(r"\s+", " ", out)
            return out

        def _delta_by_label(cur_entries: list[tuple[str, str]], ref_entries: list[tuple[str, str]], kind: str) -> list[str]:
            cur = {}
            ref = {}
            for _, lbl in cur_entries or []:
                k = _norm_label(lbl)
                if k and k not in cur:
                    cur[k] = str(lbl or "").strip()
            for _, lbl in ref_entries or []:
                k = _norm_label(lbl)
                if k and k not in ref:
                    ref[k] = str(lbl or "").strip()
            if kind == "added":
                return [cur[k] for k in cur.keys() if k not in ref]
            if kind == "removed":
                return [ref[k] for k in ref.keys() if k not in cur]
            return []

        def _common_label_code_shift(cur_entries: list[tuple[str, str]], ref_entries: list[tuple[str, str]]) -> bool:
            cur = {}
            ref = {}
            for code, lbl in cur_entries or []:
                k = _norm_label(lbl)
                if k and k not in cur:
                    cur[k] = str(code or "").strip()
            for code, lbl in ref_entries or []:
                k = _norm_label(lbl)
                if k and k not in ref:
                    ref[k] = str(code or "").strip()
            common = set(cur.keys()) & set(ref.keys())
            return any(cur[k] != ref[k] for k in common)

        def _token_set(txt: str) -> set[str]:
            return {t for t in re.findall(r"[A-Za-z0-9\u0600-\u06FF]+", str(txt or "").lower()) if t}

        def _is_hard_replacement(curr_label: str, ref_label: str) -> bool:
            a = _token_set(curr_label)
            b = _token_set(ref_label)
            if not a or not b:
                return True
            inter = len(a & b)
            union = len(a | b)
            jacc = (inter / union) if union else 0.0
            return jacc < 0.30

        rows_out = []
        by_q: dict[str, list[dict]] = {}
        for rd in noisy.to_dicts():
            q = str(rd.get("Q Name") or "").strip()
            if not q:
                continue
            by_q.setdefault(q, []).append(rd)

        structural_types = {
            "added_option",
            "removed_option",
            "added_removed_option",
            "added_option_with_drift",
            "removed_option_with_drift",
            "added_removed_option_with_drift",
            "removed_option_cascading_drift",
        }
        drift_types = {
            "option_position_drift",
            "added_option_with_drift",
            "removed_option_with_drift",
            "added_removed_option_with_drift",
            "removed_option_cascading_drift",
        }

        for q, q_items in by_q.items():
            qk = q.lower()
            q_types = {str(r.get("issue_type") or "").strip() for r in q_items}

            cur_entries_en = (current_lookup_en or {}).get(qk, [])
            ref_entries_en = (reference_lookup_en or {}).get(qk, [])
            cur_entries_tgt = (current_lookup_tgt or {}).get(qk, [])
            ref_entries_tgt = (reference_lookup_tgt or {}).get(qk, [])

            lang_scope = _combine_lang_scope([str(r.get("lang_scope") or "").strip() for r in q_items], target_lang)
            show_en, show_tgt = _option_scope_flags(lang_scope, has_lang_cols, target_lang)
            cur_entries = cur_entries_en if show_en else cur_entries_tgt
            ref_entries = ref_entries_en if show_en else ref_entries_tgt

            # Base deltas: use EN baseline when available in scope; fallback to target.
            added_labels = _delta_by_label(cur_entries, ref_entries, "added")
            removed_labels = _delta_by_label(cur_entries, ref_entries, "removed")

            # Row-level structural evidence (more robust than pure set-delta in mixed edit cases).
            added_rows = [r for r in q_items if str(r.get("issue_type") or "") == "added_option"]
            removed_rows = [r for r in q_items if str(r.get("issue_type") or "") == "removed_option"]
            mismatch_rows = [r for r in q_items if str(r.get("issue_type") or "") == "option_label_mismatch"]

            added_from_rows = [str(r.get("current") or "").strip() for r in added_rows if str(r.get("current") or "").strip()]
            removed_from_rows = [str(r.get("reference") or "").strip() for r in removed_rows if str(r.get("reference") or "").strip()]

            # If structural changes exist, treat only hard label replacements as add+remove.
            if added_rows or removed_rows or ("added_removed_option" in q_types):
                for r in mismatch_rows:
                    cur_lbl = str(r.get("current") or "").strip()
                    ref_lbl = str(r.get("reference") or "").strip()
                    # Do not convert numbering-corrupted mismatch rows into structural
                    # add/remove; they are usually parser artifacts around drift/removal.
                    if removed_rows and re.search(r"\d+\)", cur_lbl):
                        continue
                    if cur_lbl and ref_lbl and _is_hard_replacement(cur_lbl, ref_lbl):
                        added_from_rows.append(cur_lbl)
                        removed_from_rows.append(ref_lbl)

            # Do not count labels as added/removed when they still exist on the opposite
            # side (typical drift/reindex of existing options).
            ref_label_norms = {_norm_label(lbl) for _, lbl in (ref_entries or []) if _norm_label(lbl)}
            cur_label_norms = {_norm_label(lbl) for _, lbl in (cur_entries or []) if _norm_label(lbl)}
            added_from_rows = [lbl for lbl in added_from_rows if _norm_label(lbl) and _norm_label(lbl) not in ref_label_norms]
            removed_from_rows = [lbl for lbl in removed_from_rows if _norm_label(lbl) and _norm_label(lbl) not in cur_label_norms]

            # Filter pseudo-added labels created by malformed numbering merges
            # (e.g. "... 6)Unusually high fuel prices ...") so they do not appear
            # as true structural additions.
            ref_norm_texts = [_norm_label(lbl) for _, lbl in (ref_entries or []) if _norm_label(lbl)]
            def _is_malformed_added_artifact(lbl: str) -> bool:
                raw = str(lbl or "")
                norm = _norm_label(raw)
                if not norm or not re.search(r"\d+\)", raw):
                    return False
                return any(t and len(t) >= 8 and t in norm for t in ref_norm_texts)
            added_from_rows = [lbl for lbl in added_from_rows if not _is_malformed_added_artifact(lbl)]

            if added_from_rows or removed_from_rows:
                added_labels = added_from_rows
                removed_labels = removed_from_rows

            added_n = len([v for v in added_labels if str(v or "").strip()])
            removed_n = len([v for v in removed_labels if str(v or "").strip()])

            explicit_drift = any(t in drift_types for t in q_types)
            common_labels_n = len(cur_label_norms & ref_label_norms)
            common_shift = _common_label_code_shift(cur_entries_en, ref_entries_en) or _common_label_code_shift(cur_entries_tgt, ref_entries_tgt)
            cur_total = len(cur_entries)
            ref_total = len(ref_entries)
            # Drift is meaningful only when at least one label persists across sides
            # AND that label's code actually differs between current and reference.
            # If no labels overlap, this is a full replacement (add/remove), not drift.
            inferred_drift = common_labels_n > 0 and (explicit_drift or common_shift)

            has_structural = any(t in structural_types for t in q_types) or (
                "option_label_mismatch" in q_types and any(t in {"added_option", "removed_option", "added_removed_option"} for t in q_types)
            )

            # Build one structural-precedence row per question when structural evidence exists.
            if has_structural:
                if added_n > 0 and removed_n > 0:
                    issue_type = "added_removed_option_with_drift" if inferred_drift else "added_removed_option"
                    sev = "high"
                    detail = (
                        f"{'added/removed options with cascading drift' if inferred_drift else 'both added and removed options'}: "
                        f"added={added_n}, removed={removed_n}; current total={cur_total}, reference total={ref_total} "
                        f"(added: {_join_limited_tokens(added_labels, 30)}; removed: {_join_limited_tokens(removed_labels, 30)})"
                    )
                elif removed_n > 0:
                    issue_type = "removed_option_with_drift" if inferred_drift else "removed_option"
                    sev = "high"
                    detail = (
                        f"{'removed options with cascading drift' if inferred_drift else 'removed options'}: {removed_n}; "
                        f"current total={cur_total}, reference total={ref_total} "
                        f"(removed: {_join_limited_tokens(removed_labels, 30)})"
                    )
                elif added_n > 0:
                    issue_type = "added_option_with_drift" if inferred_drift else "added_option"
                    sev = "high" if inferred_drift else "medium"
                    detail = (
                        f"{'added options with cascading drift' if inferred_drift else 'added options'}: {added_n}; "
                        f"current total={cur_total}, reference total={ref_total} "
                        f"(added: {_join_limited_tokens(added_labels, 30)})"
                    )
                else:
                    issue_type = "option_position_drift" if inferred_drift else "option_label_mismatch"
                    sev = "high" if issue_type == "option_position_drift" else "medium"
                    detail = (
                        f"{'option positions drifted' if issue_type == 'option_position_drift' else 'option labels changed'}: "
                        f"current total={cur_total}, reference total={ref_total}"
                    )
            else:
                # No structural change: keep pure type from observed rows.
                if "option_position_drift" in q_types:
                    issue_type = "option_position_drift"
                    sev = "high"
                    drift_n = len([r for r in q_items if str(r.get("issue_type") or "") == "option_position_drift"])
                    detail = f"option positions drifted: {drift_n}; current total={cur_total}, reference total={ref_total}"
                elif "option_label_mismatch" in q_types:
                    issue_type = "option_label_mismatch"
                    sev = "medium"
                    lab_n = len([r for r in q_items if str(r.get("issue_type") or "") == "option_label_mismatch"])
                    detail = f"option labels changed: {lab_n}; current total={cur_total}, reference total={ref_total}"
                elif "removed_option" in q_types:
                    issue_type = "removed_option"
                    sev = "high"
                    detail = f"removed options: {removed_n}; current total={cur_total}, reference total={ref_total} (removed: {_join_limited_tokens(removed_labels, 30)})"
                elif "added_option" in q_types:
                    issue_type = "added_option"
                    sev = "medium"
                    detail = f"added options: {added_n}; current total={cur_total}, reference total={ref_total} (added: {_join_limited_tokens(added_labels, 30)})"
                else:
                    # Fallback: keep first seen type for safety.
                    issue_type = str(q_items[0].get("issue_type") or "option_label_mismatch")
                    sev = str(q_items[0].get("severity") or "info")
                    detail = f"option changes: current total={cur_total}, reference total={ref_total}"

            excel_rows = [r.get("excel_row") for r in q_items if r.get("excel_row") is not None]
            row = {
                "issue_type": issue_type,
                "set_name": "",
                "Q Name": q,
                "field": detail,
                "lang_scope": lang_scope,
                "current": _format_option_entries(cur_entries_en, "Current list (option label)") if show_en else "",
                "reference": _format_option_entries(ref_entries_en, "Reference list (option label)") if show_en else "",
                "severity": sev,
                "excel_row": min(excel_rows) if excel_rows else None,
            }
            if has_lang_cols:
                row["current_lang"] = _format_option_entries(cur_entries_tgt, "Current list (option label)") if show_tgt else ""
                row["reference_lang"] = _format_option_entries(ref_entries_tgt, "Reference list (option label)") if show_tgt else ""
            rows_out.append(row)

        collapsed = pl.DataFrame(rows_out) if rows_out else pl.DataFrame(schema=noisy.schema)
        for col in noisy.columns:
            if col not in collapsed.columns:
                collapsed = collapsed.with_columns(pl.lit(None).alias(col))
        collapsed = collapsed.select(noisy.columns)
        return pl.concat([keep_df, collapsed], how="vertical")
    ```

### `collapse_option_issue_rows_by_qname._norm_label` {#fn--norm-label-3804}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3804`

**Signature**

```python
def _norm_label(txt: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `txt` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _norm_label(txt: str) -> str:
            out = str(txt or "").strip().lower()
            out = re.sub(r"\s+", " ", out)
            return out
    ```

### `collapse_option_issue_rows_by_qname._delta_by_label` {#fn--delta-by-label-3809}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3809`

**Signature**

```python
def _delta_by_label(cur_entries: list[tuple[str, str]], ref_entries: list[tuple[str, str]], kind: str) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cur_entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 8 Issue unifiers` stage. |
| `ref_entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 8 Issue unifiers` stage. |
| `kind` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _delta_by_label(cur_entries: list[tuple[str, str]], ref_entries: list[tuple[str, str]], kind: str) -> list[str]:
            cur = {}
            ref = {}
            for _, lbl in cur_entries or []:
                k = _norm_label(lbl)
                if k and k not in cur:
                    cur[k] = str(lbl or "").strip()
            for _, lbl in ref_entries or []:
                k = _norm_label(lbl)
                if k and k not in ref:
                    ref[k] = str(lbl or "").strip()
            if kind == "added":
                return [cur[k] for k in cur.keys() if k not in ref]
            if kind == "removed":
                return [ref[k] for k in ref.keys() if k not in cur]
            return []
    ```

### `collapse_option_issue_rows_by_qname._common_label_code_shift` {#fn--common-label-code-shift-3826}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3826`

**Signature**

```python
def _common_label_code_shift(cur_entries: list[tuple[str, str]], ref_entries: list[tuple[str, str]]) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cur_entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 8 Issue unifiers` stage. |
| `ref_entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _common_label_code_shift(cur_entries: list[tuple[str, str]], ref_entries: list[tuple[str, str]]) -> bool:
            cur = {}
            ref = {}
            for code, lbl in cur_entries or []:
                k = _norm_label(lbl)
                if k and k not in cur:
                    cur[k] = str(code or "").strip()
            for code, lbl in ref_entries or []:
                k = _norm_label(lbl)
                if k and k not in ref:
                    ref[k] = str(code or "").strip()
            common = set(cur.keys()) & set(ref.keys())
            return any(cur[k] != ref[k] for k in common)
    ```

### `collapse_option_issue_rows_by_qname._token_set` {#fn--token-set-3840}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3840`

**Signature**

```python
def _token_set(txt: str) -> set[str]:
```

**Returns:** `set[str]`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `txt` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _token_set(txt: str) -> set[str]:
            return {t for t in re.findall(r"[A-Za-z0-9\u0600-\u06FF]+", str(txt or "").lower()) if t}
    ```

### `collapse_option_issue_rows_by_qname._is_hard_replacement` {#fn--is-hard-replacement-3843}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:3843`

**Signature**

```python
def _is_hard_replacement(curr_label: str, ref_label: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `curr_label` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |
| `ref_label` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _is_hard_replacement(curr_label: str, ref_label: str) -> bool:
            a = _token_set(curr_label)
            b = _token_set(ref_label)
            if not a or not b:
                return True
            inter = len(a & b)
            union = len(a | b)
            jacc = (inter / union) if union else 0.0
            return jacc < 0.30
    ```

### `compare_question_presence` {#fn-compare-question-presence-4048}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4048`

**Signature**

```python
def compare_question_presence(current_questions: pl.DataFrame, reference_questions: pl.DataFrame) -> tuple[pl.DataFrame, pl.DataFrame]:
```

**Returns:** `tuple[pl.DataFrame, pl.DataFrame]`

**What it does:** Returns (added, removed). Each DataFrame includes `is_optional`.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def compare_question_presence(
        current_questions : pl.DataFrame,
        reference_questions: pl.DataFrame,
    ) -> tuple[pl.DataFrame, pl.DataFrame]:
        """
        Returns (added, removed). Each DataFrame includes `is_optional`.
        """
        key_col = "Q Name"

        added = (
            current_questions.select([key_col])
            .join(reference_questions.select([key_col]), on=key_col, how="anti")
            .with_columns(pl.col(key_col).str.starts_with("o_").alias("is_optional"))
        )

        removed = (
            reference_questions.select([key_col])
            .join(current_questions.select([key_col]), on=key_col, how="anti")
            .with_columns(pl.col(key_col).str.starts_with("o_").alias("is_optional"))
        )

        return added, removed
    ```

### `validate_module_presence` {#fn-validate-module-presence-4072}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4072`

**Signature**

```python
def validate_module_presence(current_modules: pl.DataFrame, reference_modules: pl.DataFrame, template_modules: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Module-level structure checks:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_modules` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `reference_modules` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `template_modules` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def validate_module_presence(
        current_modules: pl.DataFrame,
        reference_modules: pl.DataFrame,
        template_modules: pl.DataFrame,
    ) -> pl.DataFrame:
        """
        Module-level structure checks:
          - module_removed (high): template module missing in current (always enforced)
          - module_added (info): current module absent from selected reference
        """
        schema = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "module": pl.Utf8, "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }

        def _to_map(df: pl.DataFrame) -> dict[str, dict]:
            if df is None or df.height == 0:
                return {}
            out = {}
            for row in df.select(["module_key_norm", "module_key", "module", "excel_row"]).iter_rows(named=True):
                key = str(row.get("module_key_norm") or "").strip()
                if key:
                    out[key] = row
            return out

        cur_map = _to_map(current_modules)
        ref_map = _to_map(reference_modules)
        tpl_map = _to_map(template_modules)
        cur_keys = set(cur_map.keys())
        ref_keys = set(ref_map.keys())
        tpl_keys = set(tpl_map.keys())

        rows = []
        for key in sorted(tpl_keys - cur_keys):
            src = tpl_map.get(key, {})
            mod_label = str(src.get("module") or src.get("module_key") or key)
            rows.append({
                "issue_type": "module_removed",
                "set_name": "questionnaire_structure",
                "Q Name": "",
                "module": mod_label,
                "field": "module",
                "current": "missing_in_current",
                "reference": "present_in_template",
                "severity": "high",
                "excel_row": src.get("excel_row"),
            })

        for key in sorted(cur_keys - ref_keys):
            src = cur_map.get(key, {})
            mod_label = str(src.get("module") or src.get("module_key") or key)
            rows.append({
                "issue_type": "module_added",
                "set_name": "questionnaire_structure",
                "Q Name": "",
                "module": mod_label,
                "field": "module",
                "current": "present_in_current",
                "reference": "missing_in_reference",
                "severity": "info",
                "excel_row": src.get("excel_row"),
            })

        return pl.DataFrame(rows, schema=schema) if rows else pl.DataFrame(schema=schema)
    ```

### `validate_module_presence._to_map` {#fn--to-map-4088}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4088`

**Signature**

```python
def _to_map(df: pl.DataFrame) -> dict[str, dict]:
```

**Returns:** `dict[str, dict]`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _to_map(df: pl.DataFrame) -> dict[str, dict]:
            if df is None or df.height == 0:
                return {}
            out = {}
            for row in df.select(["module_key_norm", "module_key", "module", "excel_row"]).iter_rows(named=True):
                key = str(row.get("module_key_norm") or "").strip()
                if key:
                    out[key] = row
            return out
    ```

### `_attach_module_column_to_issues` {#fn--attach-module-column-to-issues-4139}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4139`

**Signature**

```python
def _attach_module_column_to_issues(issues_df: pl.DataFrame, current_questions: pl.DataFrame, reference_questions: pl.DataFrame, template_questions: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `issues_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `template_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def _attach_module_column_to_issues(
        issues_df: pl.DataFrame,
        current_questions: pl.DataFrame,
        reference_questions: pl.DataFrame,
        template_questions: pl.DataFrame,
    ) -> pl.DataFrame:
        if issues_df is None:
            return pl.DataFrame(schema={"module": pl.Utf8})
        if issues_df.height == 0:
            return issues_df if "module" in issues_df.columns else issues_df.with_columns(pl.lit("").alias("module"))

        def _part(df: pl.DataFrame, prio: int) -> pl.DataFrame:
            if df is None or df.height == 0 or "Q Name" not in df.columns or "module" not in df.columns:
                return pl.DataFrame(schema={"Q Name": pl.Utf8, "_module_from_qname": pl.Utf8, "_p": pl.Int64})
            return (
                df.select(["Q Name", "module"])
                .with_columns([
                    pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Q Name"),
                    pl.col("module").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_module_from_qname"),
                    pl.lit(prio).alias("_p"),
                ])
                .filter((pl.col("Q Name") != "") & (pl.col("_module_from_qname") != ""))
                .select(["Q Name", "_module_from_qname", "_p"])
            )

        lookup = (
            pl.concat([
                _part(current_questions, 2),
                _part(reference_questions, 1),
                _part(template_questions, 0),
            ], how="vertical")
            .sort(["Q Name", "_p"])
            .group_by("Q Name")
            .agg(pl.col("_module_from_qname").last().alias("_module_from_qname"))
        )

        out = issues_df
        if "module" not in out.columns:
            out = out.with_columns(pl.lit("").alias("module"))
        out = out.join(lookup, on="Q Name", how="left")
        out = out.with_columns(
            pl.when(pl.col("module").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
            .then(pl.col("module").cast(pl.Utf8))
            .otherwise(pl.col("_module_from_qname").cast(pl.Utf8).fill_null(""))
            .alias("module")
        ).drop("_module_from_qname")
        return out
    ```

### `_attach_module_column_to_issues._part` {#fn--part-4150}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4150`

**Signature**

```python
def _part(df: pl.DataFrame, prio: int) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |
| `prio` | positional_or_keyword | Yes | `-` | `int` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _part(df: pl.DataFrame, prio: int) -> pl.DataFrame:
            if df is None or df.height == 0 or "Q Name" not in df.columns or "module" not in df.columns:
                return pl.DataFrame(schema={"Q Name": pl.Utf8, "_module_from_qname": pl.Utf8, "_p": pl.Int64})
            return (
                df.select(["Q Name", "module"])
                .with_columns([
                    pl.col("Q Name").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Q Name"),
                    pl.col("module").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_module_from_qname"),
                    pl.lit(prio).alias("_p"),
                ])
                .filter((pl.col("Q Name") != "") & (pl.col("_module_from_qname") != ""))
                .select(["Q Name", "_module_from_qname", "_p"])
            )
    ```

### `compare_mandatory` {#fn-compare-mandatory-4188}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4188`

**Signature**

```python
def compare_mandatory(current_questions: pl.DataFrame, reference_questions: pl.DataFrame, treat_blank_as_no: bool=True) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Compares Mandatory column values by Q Name.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `treat_blank_as_no` | positional_or_keyword | No | `True` | `bool` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def compare_mandatory(
        current_questions : pl.DataFrame,
        reference_questions: pl.DataFrame,
        treat_blank_as_no: bool = True,
    ) -> pl.DataFrame:
        """
        Compares Mandatory column values by Q Name.
        """
        if "Mandatory" not in current_questions.columns or "Mandatory" not in reference_questions.columns:
            return pl.DataFrame(schema={
                "issue_type": pl.Utf8, "Q Name": pl.Utf8, "field": pl.Utf8,
                "Mandatory": pl.Utf8, "Mandatory_ref": pl.Utf8, "excel_row": pl.Int64,
            })

        curr_non_blank = (
            current_questions
            .select(pl.col("Mandatory").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_m"))
            .filter(pl.col("_m") != "")
            .height
        )
        ref_non_blank = (
            reference_questions
            .select(pl.col("Mandatory").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_m"))
            .filter(pl.col("_m") != "")
            .height
        )

        # If one side has no usable mandatory values at all, row-by-row mismatch output
        # becomes noisy and low-signal. Emit one structural issue instead.
        if curr_non_blank == 0 and ref_non_blank == 0:
            return pl.DataFrame(schema={
                "issue_type": pl.Utf8, "Q Name": pl.Utf8, "field": pl.Utf8,
                "Mandatory": pl.Utf8, "Mandatory_ref": pl.Utf8, "excel_row": pl.Int64,
            })
        if curr_non_blank == 0 or ref_non_blank == 0:
            return pl.DataFrame([
                {
                    "issue_type": "mandatory_source_missing",
                    "Q Name": "",
                    "field": "Mandatory",
                    "Mandatory": f"non_blank_values={curr_non_blank}",
                    "Mandatory_ref": f"non_blank_values={ref_non_blank}",
                    "excel_row": None,
                }
            ], schema={
                "issue_type": pl.Utf8, "Q Name": pl.Utf8, "field": pl.Utf8,
                "Mandatory": pl.Utf8, "Mandatory_ref": pl.Utf8, "excel_row": pl.Int64,
            })

        joined = (
            current_questions.select(["Q Name", "Mandatory", "excel_row"])
            .join(reference_questions.select(["Q Name", "Mandatory"]), on="Q Name", how="inner", suffix="_ref")
            .with_columns([
                pl.col("Mandatory").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Mandatory"),
                pl.col("Mandatory_ref").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Mandatory_ref"),
            ])
        )

        if treat_blank_as_no:
            joined = joined.with_columns([
                pl.when(pl.col("Mandatory") == "").then(pl.lit("No")).otherwise(pl.col("Mandatory")).alias("Mandatory"),
                pl.when(pl.col("Mandatory_ref") == "").then(pl.lit("No")).otherwise(pl.col("Mandatory_ref")).alias("Mandatory_ref"),
            ])

        return (
            joined
            .filter(normalize_text_expr("Mandatory") != normalize_text_expr("Mandatory_ref"))
            .with_columns([
                pl.lit("mandatory_column_mismatch").alias("issue_type"),
                pl.lit("Mandatory").alias("field"),
            ])
            .select(["issue_type", "Q Name", "field", "Mandatory", "Mandatory_ref", "excel_row"])
        )
    ```

### `_mandatory_cat_expr` {#fn--mandatory-cat-expr-4263}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4263`

**Signature**

```python
def _mandatory_cat_expr(qname_col: str, mandatory_col: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `qname_col` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `mandatory_col` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _mandatory_cat_expr(qname_col: str, mandatory_col: str) -> pl.Expr:
        qn = pl.col(qname_col).cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase()
        md = pl.col(mandatory_col).cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase()
        return (
            pl.when(qn.str.starts_with("o_")).then(pl.lit("optional"))
            .when(md.str.contains("panel")).then(pl.lit("mandatory-panel"))
            .when(md.is_in(["yes", "y", "true", "1"]) | md.str.starts_with("yes")).then(pl.lit("mandatory"))
            .otherwise(pl.lit("non-mandatory"))
        )
    ```

### `_normalize_qtype_value` {#fn--normalize-qtype-value-4274}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4274`

**Signature**

```python
def _normalize_qtype_value(value: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _normalize_qtype_value(value: str) -> str:
        s = str(value or "").strip().lower()
        if not s:
            return ""
        s = re.sub(r"[\\/_-]+", " ", s)
        s = re.sub(r"\s+", " ", s).strip()
        # Canonical families for stable comparisons.
        if "select all that apply" in s:
            return "select all that apply"
        if "single choice" in s:
            return "single choice"
        return s
    ```

### `_qtype_mode` {#fn--qtype-mode-4288}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4288`

**Signature**

```python
def _qtype_mode(value: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _qtype_mode(value: str) -> str:
        t = _normalize_qtype_value(value)
        if not t:
            return ""
        if "select all that apply" in t:
            return "multi_select"
        if "single choice" in t:
            return "single_select"
        if is_option_bearing_qtype(t):
            return "option_bearing"
        return "non_option"
    ```

### `_is_known_qtype_value` {#fn--is-known-qtype-value-4312}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4312`

**Signature**

```python
def _is_known_qtype_value(value: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _is_known_qtype_value(value: str) -> bool:
        t = _normalize_qtype_value(value)
        if not t:
            return False
        if t in {"single choice", "select all that apply"}:
            return True
        if is_option_bearing_qtype(t):
            return True
        if t in _GEOPOLL_KNOWN_NON_OPTION_QTYPES:
            return True
        if "open ended" in t:
            return True
        return False
    ```

### `_qtype_change_severity` {#fn--qtype-change-severity-4327}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4327`

**Signature**

```python
def _qtype_change_severity(curr_mode: str, ref_mode: str, curr_option_count: int, ref_option_count: int, curr_type_norm: str, ref_type_norm: str, curr_type_known: bool, ref_type_known: bool) -> str:
```

**Returns:** `str`

**What it does:** Severity policy:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `curr_mode` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `ref_mode` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `curr_option_count` | positional_or_keyword | Yes | `-` | `int` | Input used by the `Step 9 Run the full pipeline` stage. |
| `ref_option_count` | positional_or_keyword | Yes | `-` | `int` | Input used by the `Step 9 Run the full pipeline` stage. |
| `curr_type_norm` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `ref_type_norm` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `curr_type_known` | positional_or_keyword | Yes | `-` | `bool` | Input used by the `Step 9 Run the full pipeline` stage. |
| `ref_type_known` | positional_or_keyword | Yes | `-` | `bool` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _qtype_change_severity(
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
        Severity policy:
        - HIGH for incompatible/invalid transitions (including non-mandatory questions)
        - MEDIUM for valid type changes
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
        if "non_option" in modes and (("single_select" in modes) or ("multi_select" in modes) or ("option_bearing" in modes)):
            return "high"

        # Invalid option-count correctness checks:
        # option-bearing/select questions should normally have at least 2 options.
        curr_option_like = cm in {"single_select", "multi_select", "option_bearing"}
        ref_option_like = rm in {"single_select", "multi_select", "option_bearing"}
        if curr_option_like and int(curr_option_count or 0) <= 1:
            return "high"
        if ref_option_like and int(ref_option_count or 0) <= 1:
            return "high"
        if (cm == "non_option") and int(curr_option_count or 0) > 0:
            return "high"
        if (rm == "non_option") and int(ref_option_count or 0) > 0:
            return "high"

        # Changed but compatible/valid.
        return "medium"
    ```

### `compare_qtype_changes` {#fn-compare-qtype-changes-4383}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4383`

**Signature**

```python
def compare_qtype_changes(current_questions: pl.DataFrame, reference_questions: pl.DataFrame, current_options_en: pl.DataFrame | None=None, reference_options_en: pl.DataFrame | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Risk-based Q Type comparison:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `current_options_en` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |
| `reference_options_en` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def compare_qtype_changes(
        current_questions: pl.DataFrame,
        reference_questions: pl.DataFrame,
        current_options_en: pl.DataFrame | None = None,
        reference_options_en: pl.DataFrame | None = None,
    ) -> pl.DataFrame:
        """
        Risk-based Q Type comparison:
        - normalises wording to avoid cosmetic false positives
        - escalates severity for mandatory questions and option-bearing mode shifts
        """
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if "Q Type" not in current_questions.columns or "Q Type" not in reference_questions.columns:
            return pl.DataFrame(schema=EMPTY)

        # Option counts per Q Name (English options baseline).
        if current_options_en is not None and current_options_en.height > 0:
            _cur_opt_counts = (
                current_options_en
                .group_by("Q Name")
                .agg(pl.len().alias("_curr_opt_n"))
            )
        else:
            _cur_opt_counts = pl.DataFrame(schema={"Q Name": pl.Utf8, "_curr_opt_n": pl.Int64})

        if reference_options_en is not None and reference_options_en.height > 0:
            _ref_opt_counts = (
                reference_options_en
                .group_by("Q Name")
                .agg(pl.len().alias("_ref_opt_n"))
            )
        else:
            _ref_opt_counts = pl.DataFrame(schema={"Q Name": pl.Utf8, "_ref_opt_n": pl.Int64})

        joined = (
            current_questions
            .select(["Q Name", "Q Type", "Mandatory", "excel_row"])
            .join(
                reference_questions.select(["Q Name", "Q Type", "Mandatory"]),
                on="Q Name", how="inner", suffix="_ref",
            )
            .with_columns([
                pl.col("Q Type").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Q Type"),
                pl.col("Q Type_ref").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Q Type_ref"),
                pl.coalesce([pl.col("Mandatory"), pl.col("Mandatory_ref")]).alias("_mand_base"),
            ])
            .with_columns([
                pl.col("Q Type").map_elements(_normalize_qtype_value, return_dtype=pl.Utf8).alias("_type_norm"),
                pl.col("Q Type_ref").map_elements(_normalize_qtype_value, return_dtype=pl.Utf8).alias("_type_norm_ref"),
                pl.col("Q Type").map_elements(_qtype_mode, return_dtype=pl.Utf8).alias("_type_mode"),
                pl.col("Q Type_ref").map_elements(_qtype_mode, return_dtype=pl.Utf8).alias("_type_mode_ref"),
                pl.col("Q Type").map_elements(_is_known_qtype_value, return_dtype=pl.Boolean).alias("_type_known"),
                pl.col("Q Type_ref").map_elements(_is_known_qtype_value, return_dtype=pl.Boolean).alias("_type_known_ref"),
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
                    lambda r: _qtype_change_severity(
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
        )
        if joined.height == 0:
            return pl.DataFrame(schema=EMPTY)

        return (
            joined
            .with_columns([
                pl.lit("qtype_changed").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("Q Type").alias("field"),
                pl.col("Q Type").alias("current"),
                pl.col("Q Type_ref").alias("reference"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `compare_legacy_text_field_changes` {#fn-compare-legacy-text-field-changes-4485}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4485`

**Signature**

```python
def compare_legacy_text_field_changes(current_questions: pl.DataFrame, reference_questions: pl.DataFrame, column_name: str, issue_type: str, default_severity: str='medium', high_when_mandatory: bool=False) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Legacy column parity checks with normalization to avoid cosmetic false positives.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `column_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `issue_type` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `default_severity` | positional_or_keyword | No | `'medium'` | `str` | Severity label used for final issue classification. |
| `high_when_mandatory` | positional_or_keyword | No | `False` | `bool` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def compare_legacy_text_field_changes(
        current_questions: pl.DataFrame,
        reference_questions: pl.DataFrame,
        column_name: str,
        issue_type: str,
        default_severity: str = "medium",
        high_when_mandatory: bool = False,
    ) -> pl.DataFrame:
        """Legacy column parity checks with normalization to avoid cosmetic false positives."""
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if column_name not in current_questions.columns or column_name not in reference_questions.columns:
            return pl.DataFrame(schema=EMPTY)

        joined = (
            current_questions
            .select(["Q Name", column_name, "Mandatory", "excel_row"])
            .join(
                reference_questions.select(["Q Name", column_name, "Mandatory"]),
                on="Q Name", how="inner", suffix="_ref",
            )
            .with_columns([
                pl.col(column_name).cast(pl.Utf8).fill_null("").str.strip_chars().alias("_curr"),
                pl.col(f"{column_name}_ref").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_ref"),
                pl.coalesce([pl.col("Mandatory"), pl.col("Mandatory_ref")]).alias("_mand_base"),
            ])
            .with_columns([
                normalize_text_expr("_curr").alias("_curr_norm"),
                normalize_text_expr("_ref").alias("_ref_norm"),
                _mandatory_cat_expr("Q Name", "_mand_base").alias("_mandatory_cat"),
            ])
            .filter((pl.col("_curr_norm") != pl.col("_ref_norm")) & ((pl.col("_curr_norm") != "") | (pl.col("_ref_norm") != "")))
        )
        if joined.height == 0:
            return pl.DataFrame(schema=EMPTY)

        if high_when_mandatory:
            joined = joined.with_columns(
                pl.when(pl.col("_mandatory_cat").is_in(["mandatory", "mandatory-panel"]))
                .then(pl.lit("high"))
                .otherwise(pl.lit(default_severity))
                .alias("severity")
            )
        else:
            joined = joined.with_columns(pl.lit(default_severity).alias("severity"))

        return (
            joined
            .with_columns([
                pl.lit(issue_type).alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit(column_name).alias("field"),
                pl.col("_curr").alias("current"),
                pl.col("_ref").alias("reference"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `validate_conditional_removed_for_mandatory` {#fn-validate-conditional-removed-for-mandatory-4547}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4547`

**Signature**

```python
def validate_conditional_removed_for_mandatory(current_questions: pl.DataFrame, reference_questions: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** High-severity, narrow sibling of the generic 'Conditional' comparison:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def validate_conditional_removed_for_mandatory(
        current_questions: pl.DataFrame,
        reference_questions: pl.DataFrame,
    ) -> pl.DataFrame:
        """
        High-severity, narrow sibling of the generic 'Conditional' comparison:
        flags only the case where the reference has a constraint rule and the
        current questionnaire dropped it entirely on a mandatory/mandatory-panel
        question. Cosmetic rewording of Conditional is still handled separately
        by compare_legacy_text_field_changes() at info severity.
        """
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if "Conditional" not in current_questions.columns or "Conditional" not in reference_questions.columns:
            return pl.DataFrame(schema=EMPTY)

        joined = (
            current_questions
            .select(["Q Name", "Conditional", "Mandatory", "excel_row"])
            .join(
                reference_questions.select(["Q Name", "Conditional", "Mandatory"]),
                on="Q Name", how="inner", suffix="_ref",
            )
            .with_columns([
                pl.col("Conditional").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_curr"),
                pl.col("Conditional_ref").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_ref"),
                _mandatory_cat_expr("Q Name", "Mandatory").alias("_mandatory_cat"),
            ])
            .filter(
                (pl.col("_ref") != "")
                & (pl.col("_curr") == "")
                & pl.col("_mandatory_cat").is_in(["mandatory", "mandatory-panel"])
            )
        )
        if joined.height == 0:
            return pl.DataFrame(schema=EMPTY)

        return (
            joined
            .with_columns([
                pl.lit("conditional_removed_mandatory").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("Conditional").alias("field"),
                pl.lit("(blank)").alias("current"),
                pl.col("_ref").alias("reference"),
                pl.lit("high").alias("severity"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `compare_question_labels_single` {#fn-compare-question-labels-single-4601}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4601`

**Signature**

```python
def compare_question_labels_single(current_questions: pl.DataFrame, reference_questions: pl.DataFrame, current_text_col: str, reference_text_col: str, lang_scope: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Question stem (text label) changes for matching Q Name in one language scope.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `current_text_col` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `reference_text_col` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `lang_scope` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def compare_question_labels_single(
        current_questions : pl.DataFrame,
        reference_questions: pl.DataFrame,
        current_text_col: str,
        reference_text_col: str,
        lang_scope: str,
    ) -> pl.DataFrame:
        """
        Question stem (text label) changes for matching Q Name in one language scope.
        Numbered option blocks are removed so option labels are handled only in Option Changes.
        """
        if current_text_col not in current_questions.columns or reference_text_col not in reference_questions.columns:
            return pl.DataFrame(schema={
                "issue_type": pl.Utf8,
                "Q Name": pl.Utf8,
                "field": pl.Utf8,
                "current": pl.Utf8,
                "reference": pl.Utf8,
                "severity": pl.Utf8,
                "excel_row": pl.Int64,
                "lang_scope": pl.Utf8,
            })

        return (
            current_questions
            .select([
                "Q Name",
                "excel_row",
                pl.col(current_text_col).alias("_curr_text"),
            ])
            .join(
                reference_questions.select([
                    "Q Name",
                    pl.col(reference_text_col).alias("_ref_text"),
                ]),
                on="Q Name",
                how="inner",
            )
            .with_columns([
                pl.col("_curr_text")
                .map_elements(extract_question_stem, return_dtype=pl.Utf8)
                .fill_null("")
                .str.strip_chars()
                .alias("current"),
                pl.col("_ref_text")
                .map_elements(extract_question_stem, return_dtype=pl.Utf8)
                .fill_null("")
                .str.strip_chars()
                .alias("reference"),
            ])
            .with_columns([
                normalize_text_expr("current").alias("_current_norm"),
                normalize_text_expr("reference").alias("_reference_norm"),
            ])
            .filter(pl.col("_current_norm") != pl.col("_reference_norm"))
            .with_columns([
                pl.lit("question_label_mismatch").alias("issue_type"),
                pl.lit("label").alias("field"),
                pl.lit("medium").alias("severity"),
                pl.lit(lang_scope).alias("lang_scope"),
                pl.col("excel_row").cast(pl.Int64).alias("excel_row"),
            ])
            .select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row", "lang_scope"])
        )
    ```

### `build_question_changes_view` {#fn-build-question-changes-view-4667}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4667`

**Signature**

```python
def build_question_changes_view(core_question_issues: pl.DataFrame, en_label_diff: pl.DataFrame, tgt_label_diff: pl.DataFrame, target_lang: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Builds Question Changes rows with independent EN and target-language label checks.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `core_question_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `en_label_diff` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `tgt_label_diff` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `target_lang` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def build_question_changes_view(
        core_question_issues: pl.DataFrame,
        en_label_diff: pl.DataFrame,
        tgt_label_diff: pl.DataFrame,
        target_lang: str,
    ) -> pl.DataFrame:
        """
        Builds Question Changes rows with independent EN and target-language label checks.

        Layout policy:
        - Current value / Reference / rule are always EN baseline.
        - For non-EN runs, target language values are added in separate columns.
        """
        is_en = str(target_lang).upper() == "EN"

        if is_en:
            label_view = (
                en_label_diff
                .with_columns([
                    pl.lit("").alias("set_name"),
                    pl.lit("EN").alias("lang_scope"),
                    pl.col("current").cast(pl.Utf8).fill_null("").alias("current"),
                    pl.col("reference").cast(pl.Utf8).fill_null("").alias("reference"),
                    pl.col("severity").cast(pl.Utf8).fill_null("info").alias("severity"),
                    pl.col("excel_row").cast(pl.Int64).alias("excel_row"),
                ])
                .select(["issue_type", "set_name", "Q Name", "field", "lang_scope", "current", "reference", "severity", "excel_row"])
            )

            core_view = (
                core_question_issues
                .with_columns([
                    pl.col("set_name").cast(pl.Utf8).fill_null("").alias("set_name"),
                    pl.col("field").cast(pl.Utf8).fill_null("").alias("field"),
                    pl.lit("N/A").alias("lang_scope"),
                    pl.col("current").cast(pl.Utf8).fill_null("").alias("current"),
                    pl.col("reference").cast(pl.Utf8).fill_null("").alias("reference"),
                    pl.col("severity").cast(pl.Utf8).fill_null("info").alias("severity"),
                    pl.col("excel_row").cast(pl.Int64),
                ])
                .select(["issue_type", "set_name", "Q Name", "field", "lang_scope", "current", "reference", "severity", "excel_row"])
            )
            return pl.concat([core_view, label_view], how="vertical")

        def _scope_view(label_diff: pl.DataFrame, scope: str) -> pl.DataFrame:
            return (
                label_diff
                .rename({
                    "current": f"current_{scope.lower()}",
                    "reference": f"reference_{scope.lower()}",
                    "severity": f"severity_{scope.lower()}",
                    "excel_row": f"excel_row_{scope.lower()}",
                })
                .select([
                    "issue_type", "Q Name", "field",
                    f"current_{scope.lower()}", f"reference_{scope.lower()}",
                    f"severity_{scope.lower()}", f"excel_row_{scope.lower()}",
                ])
            )

        en_view = _scope_view(en_label_diff, "EN")
        tgt_view = _scope_view(tgt_label_diff, "TGT")
        keys = ["issue_type", "Q Name", "field"]
        out = en_view.join(tgt_view, on=keys, how="full", suffix="_t")
        label_view = (
            out
            .with_columns([
                pl.coalesce([pl.col("issue_type"), pl.col("issue_type_t")]).alias("issue_type"),
                pl.coalesce([pl.col("Q Name"), pl.col("Q Name_t")]).alias("Q Name"),
                pl.coalesce([pl.col("field"), pl.col("field_t")]).alias("field"),
                pl.lit("").alias("set_name"),
                # EN baseline in primary columns
                pl.coalesce([pl.col("current_en"), pl.lit("")]).alias("current"),
                pl.coalesce([pl.col("reference_en"), pl.lit("")]).alias("reference"),
                # Target language shown in dedicated columns
                pl.coalesce([pl.col("current_tgt"), pl.lit("")]).alias("current_lang"),
                pl.coalesce([pl.col("reference_tgt"), pl.lit("")]).alias("reference_lang"),
                pl.when(pl.col("severity_tgt") == "high").then(pl.lit("high"))
                .when(pl.col("severity_en") == "high").then(pl.lit("high"))
                .when(pl.col("severity_tgt") == "medium").then(pl.lit("medium"))
                .when(pl.col("severity_en") == "medium").then(pl.lit("medium"))
                .otherwise(pl.lit("info")).alias("severity"),
                pl.coalesce([pl.col("excel_row_tgt"), pl.col("excel_row_en")]).alias("excel_row"),
                pl.when(
                    ((pl.col("current_en").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
                     | (pl.col("reference_en").cast(pl.Utf8).fill_null("").str.strip_chars() != ""))
                    &
                    ((pl.col("current_tgt").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
                     | (pl.col("reference_tgt").cast(pl.Utf8).fill_null("").str.strip_chars() != ""))
                ).then(pl.lit(f"EN+{target_lang}"))
                .when(
                    (pl.col("current_en").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
                    | (pl.col("reference_en").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
                ).then(pl.lit("EN"))
                .when(
                    (pl.col("current_tgt").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
                    | (pl.col("reference_tgt").cast(pl.Utf8).fill_null("").str.strip_chars() != "")
                ).then(pl.lit(target_lang))
                .otherwise(pl.lit(target_lang))
                .alias("lang_scope"),
            ])
            .select([
                "issue_type", "set_name", "Q Name", "field", "lang_scope", "current", "reference",
                "current_lang", "reference_lang", "severity", "excel_row",
            ])
        )

        core_view = (
            core_question_issues
            .with_columns([
                pl.col("set_name").cast(pl.Utf8).fill_null("").alias("set_name"),
                pl.col("field").cast(pl.Utf8).fill_null("").alias("field"),
                pl.lit("N/A").alias("lang_scope"),
                pl.col("current").cast(pl.Utf8).fill_null("").alias("current"),
                pl.col("reference").cast(pl.Utf8).fill_null("").alias("reference"),
                pl.lit("").alias("current_lang"),
                pl.lit("").alias("reference_lang"),
                pl.col("severity").cast(pl.Utf8).fill_null("info").alias("severity"),
                pl.col("excel_row").cast(pl.Int64),
            ])
            .select([
                "issue_type", "set_name", "Q Name", "field", "lang_scope", "current", "reference",
                "current_lang", "reference_lang", "severity", "excel_row",
            ])
        )

        return pl.concat([core_view, label_view], how="vertical")
    ```

### `build_question_changes_view._scope_view` {#fn--scope-view-4711}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4711`

**Signature**

```python
def _scope_view(label_diff: pl.DataFrame, scope: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `label_diff` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `scope` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _scope_view(label_diff: pl.DataFrame, scope: str) -> pl.DataFrame:
            return (
                label_diff
                .rename({
                    "current": f"current_{scope.lower()}",
                    "reference": f"reference_{scope.lower()}",
                    "severity": f"severity_{scope.lower()}",
                    "excel_row": f"excel_row_{scope.lower()}",
                })
                .select([
                    "issue_type", "Q Name", "field",
                    f"current_{scope.lower()}", f"reference_{scope.lower()}",
                    f"severity_{scope.lower()}", f"excel_row_{scope.lower()}",
                ])
            )
    ```

### `compare_option_labels_single` {#fn-compare-option-labels-single-4796}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4796`

**Signature**

```python
def compare_option_labels_single(current_options: pl.DataFrame, reference_options: pl.DataFrame, lang_scope: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Option label changes for matching Q Name + option_code.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `lang_scope` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def compare_option_labels_single(
        current_options : pl.DataFrame,
        reference_options: pl.DataFrame,
        lang_scope: str,
    ) -> pl.DataFrame:
        """
        Option label changes for matching Q Name + option_code.
        """
        return (
            current_options
            .join(reference_options, on=["Q Name", "option_code"], how="inner", suffix="_ref")
            .with_columns([
                normalize_text_expr("option_label").alias("option_label_norm"),
                normalize_text_expr("option_label_ref").alias("option_label_ref_norm"),
            ])
            .filter(pl.col("option_label_norm") != pl.col("option_label_ref_norm"))
            .with_columns([
                pl.lit("option_label_mismatch").alias("issue_type"),
                pl.concat_str([pl.lit("option_"), pl.col("option_code").cast(pl.Utf8)]).alias("field"),
                pl.lit("medium").alias("severity"),
                pl.lit(lang_scope).alias("lang_scope"),
            ])
            .select(["issue_type", "Q Name", "field", "option_label", "option_label_ref", "severity", "excel_row", "lang_scope"])
        )
    ```

### `compare_option_presence_single` {#fn-compare-option-presence-single-4822}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4822`

**Signature**

```python
def compare_option_presence_single(current_options: pl.DataFrame, reference_options: pl.DataFrame, lang_scope: str) -> tuple[pl.DataFrame, pl.DataFrame]:
```

**Returns:** `tuple[pl.DataFrame, pl.DataFrame]`

**What it does:** Added/removed options for one language scope.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `lang_scope` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def compare_option_presence_single(
        current_options : pl.DataFrame,
        reference_options: pl.DataFrame,
        lang_scope: str,
    ) -> tuple[pl.DataFrame, pl.DataFrame]:
        """
        Added/removed options for one language scope.
        """
        key_cols = ["Q Name", "option_code"]

        removed_options = (
            reference_options.select(key_cols + ["option_label"])
            .join(current_options.select(key_cols), on=key_cols, how="anti")
            .with_columns([
                pl.lit("removed_option").alias("issue_type"),
                pl.concat_str([pl.lit("option_"), pl.col("option_code").cast(pl.Utf8)]).alias("field"),
                pl.lit("high").alias("severity"),
                pl.lit(lang_scope).alias("lang_scope"),
            ])
            .select(["issue_type", "Q Name", "field", "option_label", "severity", "lang_scope"])
        )

        added_options = (
            current_options.select(key_cols + ["option_label"])
            .join(reference_options.select(key_cols), on=key_cols, how="anti")
            .with_columns([
                pl.lit("added_option").alias("issue_type"),
                pl.concat_str([pl.lit("option_"), pl.col("option_code").cast(pl.Utf8)]).alias("field"),
                pl.lit("medium").alias("severity"),
                pl.lit(lang_scope).alias("lang_scope"),
            ])
            .select(["issue_type", "Q Name", "field", "option_label", "severity", "lang_scope"])
        )

        return added_options, removed_options
    ```

### `compare_option_code_renumber_single` {#fn-compare-option-code-renumber-single-4859}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4859`

**Signature**

```python
def compare_option_code_renumber_single(current_options: pl.DataFrame, reference_options: pl.DataFrame, lang_scope: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Detect explicit option-position renumbering for the same normalized label

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `lang_scope` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def compare_option_code_renumber_single(
        current_options: pl.DataFrame,
        reference_options: pl.DataFrame,
        lang_scope: str,
    ) -> pl.DataFrame:
        """
        Detect explicit option-position renumbering for the same normalized label
        within the same question: e.g., position 12 becomes 15.

        We only emit when label->code mapping is 1:1 on both sides to avoid
        ambiguous many-to-many matches.
        """
        cur = (
            current_options
            .with_columns(normalize_text_expr("option_label").alias("label_norm"))
            .filter(pl.col("label_norm") != "")
            .group_by(["Q Name", "label_norm"])
            .agg([
                pl.col("option_code").n_unique().alias("cur_n_codes"),
                pl.col("option_code").first().alias("new_code"),
                pl.col("option_label").first().alias("option_label"),
                pl.col("excel_row").min().alias("excel_row"),
            ])
        )

        ref = (
            reference_options
            .with_columns(normalize_text_expr("option_label").alias("label_norm"))
            .filter(pl.col("label_norm") != "")
            .group_by(["Q Name", "label_norm"])
            .agg([
                pl.col("option_code").n_unique().alias("ref_n_codes"),
                pl.col("option_code").first().alias("old_code"),
                pl.col("option_label").first().alias("option_label_ref"),
            ])
        )

        return (
            cur.join(ref, on=["Q Name", "label_norm"], how="inner")
            .filter(
                (pl.col("cur_n_codes") == 1)
                & (pl.col("ref_n_codes") == 1)
                & (pl.col("new_code") != pl.col("old_code"))
            )
            .with_columns([
                pl.lit("option_position_drift").alias("issue_type"),
                pl.concat_str([
                    pl.lit("position_"),
                    pl.col("old_code").cast(pl.Utf8),
                    pl.lit("_to_"),
                    pl.col("new_code").cast(pl.Utf8),
                ]).alias("field"),
                pl.lit("high").alias("severity"),
                pl.lit(lang_scope).alias("lang_scope"),
            ])
            .select([
                "issue_type", "Q Name", "field",
                "old_code", "new_code",
                "option_label", "option_label_ref",
                "severity", "excel_row", "lang_scope",
            ])
        )
    ```

### `compare_codes_presence_single` {#fn-compare-codes-presence-single-4923}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4923`

**Signature**

```python
def compare_codes_presence_single(current_codes: pl.DataFrame, reference_codes: pl.DataFrame) -> tuple[pl.DataFrame, pl.DataFrame]:
```

**Returns:** `tuple[pl.DataFrame, pl.DataFrame]`

**What it does:** Added/removed numeric code entries in the survey 'Codes' column.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `reference_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def compare_codes_presence_single(
        current_codes: pl.DataFrame,
        reference_codes: pl.DataFrame,
    ) -> tuple[pl.DataFrame, pl.DataFrame]:
        """Added/removed numeric code entries in the survey 'Codes' column."""
        key_cols = ["Q Name", "code_num"]

        removed_codes = (
            reference_codes.select(key_cols + ["code_token"])
            .join(current_codes.select(key_cols), on=key_cols, how="anti")
            .with_columns([
                pl.lit("codes_removed").alias("issue_type"),
                pl.concat_str([pl.lit("codes_"), pl.col("code_num").cast(pl.Utf8)]).alias("field"),
                pl.lit("high").alias("severity"),
            ])
            .select(["issue_type", "Q Name", "field", "code_num", "code_token", "severity"])
        )

        added_codes = (
            current_codes.select(key_cols + ["code_token", "excel_row"])
            .join(reference_codes.select(key_cols), on=key_cols, how="anti")
            .with_columns([
                pl.lit("codes_added").alias("issue_type"),
                pl.concat_str([pl.lit("codes_"), pl.col("code_num").cast(pl.Utf8)]).alias("field"),
                pl.lit("medium").alias("severity"),
            ])
            .select(["issue_type", "Q Name", "field", "code_num", "code_token", "severity", "excel_row"])
        )

        return added_codes, removed_codes
    ```

### `compare_codes_token_mismatch_single` {#fn-compare-codes-token-mismatch-single-4955}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:4955`

**Signature**

```python
def compare_codes_token_mismatch_single(current_codes: pl.DataFrame, reference_codes: pl.DataFrame, renumber_codes: pl.DataFrame | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Same code number exists in both, but token text differs in 'Codes' column.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `reference_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `renumber_codes` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def compare_codes_token_mismatch_single(
        current_codes: pl.DataFrame,
        reference_codes: pl.DataFrame,
        renumber_codes: pl.DataFrame | None = None,
    ) -> pl.DataFrame:
        """
        Same code number exists in both, but token text differs in 'Codes' column.

        Precedence rule:
        - If a code position is already explained by a same-token renumber event
          (old_code_num->new_code_num) for the same Q Name, suppress token-mismatch
          rows on those positions to avoid double-reporting reorder as rename.
        """
        mismatch = (
            current_codes
            .join(reference_codes, on=["Q Name", "code_num"], how="inner", suffix="_ref")
            .with_columns([
                normalize_code_token_expr("code_token").alias("code_token_norm"),
                normalize_code_token_expr("code_token_ref").alias("code_token_ref_norm"),
            ])
            .filter(pl.col("code_token_norm") != pl.col("code_token_ref_norm"))
            .with_columns([
                pl.lit("codes_token_mismatch").alias("issue_type"),
                pl.concat_str([pl.lit("codes_"), pl.col("code_num").cast(pl.Utf8)]).alias("field"),
                pl.lit("high").alias("severity"),
            ])
            .select([
                "issue_type", "Q Name", "field", "code_num",
                "code_token", "code_token_ref", "severity", "excel_row",
            ])
        )

        if renumber_codes is None or renumber_codes.height == 0:
            return mismatch

        renumber_positions = (
            pl.concat([
                renumber_codes.select([
                    pl.col("Q Name"),
                    pl.col("old_code_num").cast(pl.Int64).alias("code_num"),
                ]),
                renumber_codes.select([
                    pl.col("Q Name"),
                    pl.col("new_code_num").cast(pl.Int64).alias("code_num"),
                ]),
            ], how="vertical")
            .unique()
        )

        return mismatch.join(renumber_positions, on=["Q Name", "code_num"], how="anti")
    ```

### `compare_codes_renumber_single` {#fn-compare-codes-renumber-single-5007}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5007`

**Signature**

```python
def compare_codes_renumber_single(current_codes: pl.DataFrame, reference_codes: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Detect same normalized code token moved to a different number in 'Codes'.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `reference_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def compare_codes_renumber_single(
        current_codes: pl.DataFrame,
        reference_codes: pl.DataFrame,
    ) -> pl.DataFrame:
        """
        Detect same normalized code token moved to a different number in 'Codes'.
        Emits only 1:1 token->number mappings to avoid ambiguous many-to-many cases.
        """
        cur = (
            current_codes
            .with_columns(normalize_code_token_expr("code_token").alias("token_norm"))
            .filter(pl.col("token_norm") != "")
            .group_by(["Q Name", "token_norm"])
            .agg([
                pl.col("code_num").n_unique().alias("cur_n_nums"),
                pl.col("code_num").first().alias("new_code_num"),
                pl.col("code_token").first().alias("code_token"),
                pl.col("excel_row").min().alias("excel_row"),
            ])
        )

        ref = (
            reference_codes
            .with_columns(normalize_code_token_expr("code_token").alias("token_norm"))
            .filter(pl.col("token_norm") != "")
            .group_by(["Q Name", "token_norm"])
            .agg([
                pl.col("code_num").n_unique().alias("ref_n_nums"),
                pl.col("code_num").first().alias("old_code_num"),
                pl.col("code_token").first().alias("code_token_ref"),
            ])
        )

        return (
            cur.join(ref, on=["Q Name", "token_norm"], how="inner")
            .filter(
                (pl.col("cur_n_nums") == 1)
                & (pl.col("ref_n_nums") == 1)
                & (pl.col("new_code_num") != pl.col("old_code_num"))
            )
            .with_columns([
                pl.lit("codes_position_drift").alias("issue_type"),
                pl.concat_str([
                    pl.lit("codes_"),
                    pl.col("old_code_num").cast(pl.Utf8),
                    pl.lit("_to_"),
                    pl.col("new_code_num").cast(pl.Utf8),
                ]).alias("field"),
                pl.lit("high").alias("severity"),
            ])
            .select([
                "issue_type", "Q Name", "field",
                "old_code_num", "new_code_num",
                "code_token", "code_token_ref",
                "severity", "excel_row",
            ])
        )
    ```

### `build_codes_changes_view` {#fn-build-codes-changes-view-5066}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5066`

**Signature**

```python
def build_codes_changes_view(token_mismatch: pl.DataFrame, added_codes: pl.DataFrame, removed_codes: pl.DataFrame, renumber_codes: pl.DataFrame, target_lang: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Converts Codes-column checks to the common Option Changes view schema.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token_mismatch` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `added_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `removed_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `renumber_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `target_lang` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def build_codes_changes_view(
        token_mismatch: pl.DataFrame,
        added_codes: pl.DataFrame,
        removed_codes: pl.DataFrame,
        renumber_codes: pl.DataFrame,
        target_lang: str,
    ) -> pl.DataFrame:
        """Converts Codes-column checks to the common Option Changes view schema."""
        rows = []

        if token_mismatch.height > 0:
            rows.append(
                token_mismatch.with_columns([
                    pl.col("code_token").alias("current"),
                    pl.col("code_token_ref").alias("reference"),
                ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])
            )

        if added_codes.height > 0:
            rows.append(
                added_codes.with_columns([
                    pl.col("code_token").alias("current"),
                    pl.lit(_not_in_reference_text("Codes")).alias("reference"),
                ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])
            )

        if removed_codes.height > 0:
            rows.append(
                removed_codes.with_columns([
                    pl.lit("(removed from Codes)").alias("current"),
                    pl.col("code_token").alias("reference"),
                    pl.lit(None).cast(pl.Int64).alias("excel_row"),
                ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])
            )

        if renumber_codes.height > 0:
            rows.append(
                renumber_codes.with_columns([
                    pl.concat_str([
                        pl.col("new_code_num").cast(pl.Utf8), pl.lit(") "), pl.col("code_token")
                    ]).alias("current"),
                    pl.concat_str([
                        pl.col("old_code_num").cast(pl.Utf8), pl.lit(") "), pl.col("code_token_ref")
                    ]).alias("reference"),
                ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])
            )

        if rows:
            base = pl.concat(rows, how="vertical")
        else:
            base = pl.DataFrame(schema={
                "issue_type": pl.Utf8, "Q Name": pl.Utf8, "field": pl.Utf8,
                "current": pl.Utf8, "reference": pl.Utf8,
                "severity": pl.Utf8, "excel_row": pl.Int64,
            })

        if str(target_lang).upper() == "EN":
            return base.with_columns([
                pl.lit("").alias("set_name"),
                pl.lit("N/A").alias("lang_scope"),
            ]).select([
                "issue_type", "set_name", "Q Name", "field", "lang_scope", "current", "reference", "severity", "excel_row"
            ])

        return base.with_columns([
            pl.lit("").alias("set_name"),
            pl.lit("N/A").alias("lang_scope"),
            pl.lit("").alias("current_lang"),
            pl.lit("").alias("reference_lang"),
        ]).select([
            "issue_type", "set_name", "Q Name", "field", "lang_scope", "current", "reference",
            "current_lang", "reference_lang", "severity", "excel_row",
        ])
    ```

### `apply_codes_severity_by_mandatory` {#fn-apply-codes-severity-by-mandatory-5141}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5141`

**Signature**

```python
def apply_codes_severity_by_mandatory(codes_df: pl.DataFrame, q_mandatory_map: dict[str, str] | None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Keep codes logic intact while enforcing severity by question mandatory class.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `codes_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `q_mandatory_map` | positional_or_keyword | Yes | `-` | `dict[str, str] | None` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def apply_codes_severity_by_mandatory(
        codes_df: pl.DataFrame,
        q_mandatory_map: dict[str, str] | None,
    ) -> pl.DataFrame:
        """
        Keep codes logic intact while enforcing severity by question mandatory class.
        Mandatory / mandatory-panel code changes are always high.
        """
        if codes_df is None or codes_df.height == 0:
            return codes_df
        if "issue_type" not in codes_df.columns or "Q Name" not in codes_df.columns:
            return codes_df
        qmap = {str(k): str(v or "").strip().lower() for k, v in (q_mandatory_map or {}).items()}
        code_types = {
            "codes_added", "codes_removed", "codes_token_mismatch", "codes_position_drift",
        }
        return (
            codes_df
            .with_columns([
                pl.col("Q Name").cast(pl.Utf8).map_elements(lambda q: qmap.get(str(q), ""), return_dtype=pl.Utf8).alias("_mand_cat"),
            ])
            .with_columns([
                pl.when(pl.col("issue_type") == "codes_option_count_mismatch")
                .then(pl.lit("high"))
                .when(
                    pl.col("issue_type").is_in(list(code_types))
                    & pl.col("_mand_cat").is_in(["mandatory", "mandatory-panel"])
                ).then(pl.lit("high"))
                .otherwise(pl.col("severity").cast(pl.Utf8).fill_null("info"))
                .alias("severity")
            ])
            .drop("_mand_cat")
        )
    ```

### `collapse_codes_issue_rows_by_qname` {#fn-collapse-codes-issue-rows-by-qname-5176}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5176`

**Signature**

```python
def collapse_codes_issue_rows_by_qname(codes_df: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Consolidate per-code rows into one per-question structural code issue:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `codes_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def collapse_codes_issue_rows_by_qname(codes_df: pl.DataFrame) -> pl.DataFrame:
        """
        Consolidate per-code rows into one per-question structural code issue:
          - codes_added
          - codes_removed
          - added_removed_codes
          - added_codes_with_drift
          - removed_codes_with_drift
          - added_removed_codes_with_drift
          - codes_position_drift (pure drift only)
        Non-structural code issues (token mismatch, count mismatch, not comparable) are preserved.
        """
        if codes_df is None or codes_df.height == 0:
            return codes_df
        required = {"issue_type", "Q Name", "field", "current", "reference", "severity"}
        if not required.issubset(set(codes_df.columns)):
            return codes_df

        structural_types = {"codes_added", "codes_removed", "codes_position_drift"}
        mask = pl.col("issue_type").is_in(list(structural_types))
        keep_df = codes_df.filter(~mask)
        noisy = codes_df.filter(mask)
        if noisy.height == 0:
            return codes_df

        def _uniq(items: list[str]) -> list[str]:
            seen = set()
            out = []
            for raw in items or []:
                t = str(raw or "").strip()
                if not t:
                    continue
                k = t.lower()
                if k in seen:
                    continue
                seen.add(k)
                out.append(t)
            return out

        rows_out: list[dict] = []
        by_q: dict[str, list[dict]] = {}
        for rd in noisy.to_dicts():
            q = str(rd.get("Q Name") or "").strip()
            if not q:
                continue
            by_q.setdefault(q, []).append(rd)

        for q, items in by_q.items():
            added_rows = [r for r in items if str(r.get("issue_type") or "") == "codes_added"]
            removed_rows = [r for r in items if str(r.get("issue_type") or "") == "codes_removed"]
            drift_rows = [r for r in items if str(r.get("issue_type") or "") == "codes_position_drift"]

            has_added = len(added_rows) > 0
            has_removed = len(removed_rows) > 0
            has_drift = len(drift_rows) > 0

            added_vals = _uniq([str(r.get("current") or "").strip() for r in added_rows])
            removed_vals = _uniq([str(r.get("reference") or "").strip() for r in removed_rows])
            drift_from = _uniq([str(r.get("reference") or "").strip() for r in drift_rows])
            drift_to = _uniq([str(r.get("current") or "").strip() for r in drift_rows])

            if has_added and has_removed and has_drift:
                issue_type = "added_removed_codes_with_drift"
                severity = "high"
                detail = (
                    f"added/removed codes with cascading drift: added={len(added_rows)}, removed={len(removed_rows)}, drifted={len(drift_rows)}; "
                    f"(added: {_join_limited_tokens(added_vals, 30)}; removed: {_join_limited_tokens(removed_vals, 30)})"
                )
            elif has_added and has_removed:
                issue_type = "added_removed_codes"
                severity = "high"
                detail = (
                    f"both added and removed codes: added={len(added_rows)}, removed={len(removed_rows)}; "
                    f"(added: {_join_limited_tokens(added_vals, 30)}; removed: {_join_limited_tokens(removed_vals, 30)})"
                )
            elif has_added and has_drift:
                issue_type = "added_codes_with_drift"
                severity = "high"
                detail = (
                    f"added codes with cascading drift: added={len(added_rows)}, drifted={len(drift_rows)}; "
                    f"(added: {_join_limited_tokens(added_vals, 30)})"
                )
            elif has_removed and has_drift:
                issue_type = "removed_codes_with_drift"
                severity = "high"
                detail = (
                    f"removed codes with cascading drift: removed={len(removed_rows)}, drifted={len(drift_rows)}; "
                    f"(removed: {_join_limited_tokens(removed_vals, 30)})"
                )
            elif has_added:
                issue_type = "codes_added"
                severity = "medium"
                detail = f"added codes: {len(added_rows)} (added: {_join_limited_tokens(added_vals, 30)})"
            elif has_removed:
                issue_type = "codes_removed"
                severity = "high"
                detail = f"removed codes: {len(removed_rows)} (removed: {_join_limited_tokens(removed_vals, 30)})"
            else:
                issue_type = "codes_position_drift"
                severity = "high"
                detail = f"codes positions drifted: {len(drift_rows)}"

            sev_vals = [str(r.get("severity") or "").strip().lower() for r in items]
            if "high" in sev_vals:
                severity = "high"
            elif severity != "high" and "medium" in sev_vals:
                severity = "medium"

            excel_rows = [r.get("excel_row") for r in items if r.get("excel_row") is not None]
            base = items[0] if items else {}
            row = {
                "issue_type": issue_type,
                "set_name": str(base.get("set_name") or ""),
                "Q Name": q,
                "field": detail,
                "lang_scope": str(base.get("lang_scope") or "N/A"),
                "current": (
                    f"added codes: {_join_limited_tokens(added_vals, 30)}; "
                    f"drift now: {_join_limited_tokens(drift_to, 30)}"
                    if has_drift or has_added else ""
                ),
                "reference": (
                    f"removed codes: {_join_limited_tokens(removed_vals, 30)}; "
                    f"drift from: {_join_limited_tokens(drift_from, 30)}"
                    if has_drift or has_removed else ""
                ),
                "severity": severity,
                "excel_row": min(excel_rows) if excel_rows else None,
            }
            if "current_lang" in codes_df.columns:
                row["current_lang"] = ""
            if "reference_lang" in codes_df.columns:
                row["reference_lang"] = ""
            rows_out.append(row)

        collapsed = pl.DataFrame(rows_out) if rows_out else pl.DataFrame(schema=noisy.schema)
        for col in noisy.columns:
            if col not in collapsed.columns:
                collapsed = collapsed.with_columns(pl.lit(None).alias(col))
        collapsed = collapsed.select(noisy.columns)
        return pl.concat([keep_df, collapsed], how="vertical")
    ```

### `collapse_codes_issue_rows_by_qname._uniq` {#fn--uniq-5201}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5201`

**Signature**

```python
def _uniq(items: list[str]) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `items` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _uniq(items: list[str]) -> list[str]:
            seen = set()
            out = []
            for raw in items or []:
                t = str(raw or "").strip()
                if not t:
                    continue
                k = t.lower()
                if k in seen:
                    continue
                seen.add(k)
                out.append(t)
            return out
    ```

### `build_codes_not_comparable_rows` {#fn-build-codes-not-comparable-rows-5319}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5319`

**Signature**

```python
def build_codes_not_comparable_rows(current_codes: pl.DataFrame, reference_codes: pl.DataFrame, current_qnames: set[str], reference_qnames: set[str]) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Informational rows for code-bearing questions that cannot be compared because

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `reference_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `current_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 9 Run the full pipeline` stage. |
| `reference_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def build_codes_not_comparable_rows(
        current_codes: pl.DataFrame,
        reference_codes: pl.DataFrame,
        current_qnames: set[str],
        reference_qnames: set[str],
    ) -> pl.DataFrame:
        """
        Informational rows for code-bearing questions that cannot be compared because
        the parent question is present only in one file.
        """
        schema = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8, "field": pl.Utf8,
            "lang_scope": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "current_lang": pl.Utf8, "reference_lang": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if current_codes is None or reference_codes is None:
            return pl.DataFrame(schema=schema)

        cur_code_q = set(current_codes.get_column("Q Name").to_list()) if current_codes.height > 0 else set()
        ref_code_q = set(reference_codes.get_column("Q Name").to_list()) if reference_codes.height > 0 else set()

        cur_only = sorted(q for q in (cur_code_q - ref_code_q) if q in current_qnames and q not in reference_qnames)
        ref_only = sorted(q for q in (ref_code_q - cur_code_q) if q in reference_qnames and q not in current_qnames)

        rows = []
        if cur_only:
            rows.append({
                "issue_type": "codes_not_comparable",
                "set_name": "",
                "Q Name": ", ".join(cur_only[:40]) + (f", ... (+{len(cur_only)-40} more)" if len(cur_only) > 40 else ""),
                "field": f"codes present only in current for {len(cur_only)} question(s); comparison skipped",
                "lang_scope": "N/A",
                "current": ", ".join(cur_only[:40]) + (f", ... (+{len(cur_only)-40} more)" if len(cur_only) > 40 else ""),
                "reference": "(question(s) not present in reference)",
                "current_lang": "",
                "reference_lang": "",
                "severity": "info",
                "excel_row": None,
            })
        if ref_only:
            rows.append({
                "issue_type": "codes_not_comparable",
                "set_name": "",
                "Q Name": ", ".join(ref_only[:40]) + (f", ... (+{len(ref_only)-40} more)" if len(ref_only) > 40 else ""),
                "field": f"codes present only in reference for {len(ref_only)} question(s); comparison skipped",
                "lang_scope": "N/A",
                "current": "(question(s) not present in current)",
                "reference": ", ".join(ref_only[:40]) + (f", ... (+{len(ref_only)-40} more)" if len(ref_only) > 40 else ""),
                "current_lang": "",
                "reference_lang": "",
                "severity": "info",
                "excel_row": None,
            })
        if not rows:
            return pl.DataFrame(schema=schema)
        return pl.DataFrame(rows, schema=schema)
    ```

### `build_codes_option_count_mismatch_rows` {#fn-build-codes-option-count-mismatch-rows-5378}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5378`

**Signature**

```python
def build_codes_option_count_mismatch_rows(current_options_en: pl.DataFrame, current_codes: pl.DataFrame, reference_options_en: pl.DataFrame, reference_codes: pl.DataFrame, target_lang: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Internal consistency check (CURRENT questionnaire only):

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_options_en` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `current_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `reference_options_en` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `target_lang` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def build_codes_option_count_mismatch_rows(
        current_options_en: pl.DataFrame,
        current_codes: pl.DataFrame,
        reference_options_en: pl.DataFrame,
        reference_codes: pl.DataFrame,
        target_lang: str,
    ) -> pl.DataFrame:
        """
        Internal consistency check (CURRENT questionnaire only):
        flag questions where parsed option codes and parsed Codes entries are not aligned
        (count mismatch or code-number set mismatch).
        Reference columns are provided only as contextual baseline.
        """
        schema = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8, "field": pl.Utf8,
            "lang_scope": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "current_lang": pl.Utf8, "reference_lang": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if current_options_en is None or current_options_en.height == 0:
            return pl.DataFrame(schema=schema)

        def _parse_int_codes(entries: list[tuple[str, str]]) -> set[int]:
            out = set()
            for raw, _ in entries or []:
                s = str(raw or "").strip()
                if re.fullmatch(r"\d+", s):
                    out.add(int(s))
            return out

        def _formatted_codes_with_option_alignment(
            code_entries: list[tuple[str, str]],
            option_num_set: set[int],
            header: str,
        ) -> str:
            vals = []
            seen = set()
            for code_raw, token_raw in code_entries or []:
                code = str(code_raw or "").strip()
                token = str(token_raw or "").strip()
                if not code and not token:
                    continue
                key = (code.lower(), token.lower())
                if key in seen:
                    continue
                seen.add(key)
                note = ""
                if re.fullmatch(r"\d+", code) and int(code) not in option_num_set:
                    note = " [NO CORRESPONDING OPTION]"
                vals.append(f"{code or '(blank)'} | {token or '(blank)'}{note}")
            if not vals:
                return f"{header}:\n(empty)"
            return f"{header}:\n" + "\n".join(vals)

        opt_lookup_cur = _build_option_lookup_by_qname(current_options_en)
        code_lookup_cur = _build_codes_lookup_by_qname(current_codes)
        opt_lookup_ref = _build_option_lookup_by_qname(reference_options_en)
        code_lookup_ref = _build_codes_lookup_by_qname(reference_codes)

        excel_row_lookup: dict[str, int] = {}
        qname_lookup: dict[str, str] = {}
        for row in (
            current_options_en
            .group_by("Q Name")
            .agg(pl.col("excel_row").min().cast(pl.Int64).alias("excel_row"))
            .iter_rows(named=True)
        ):
            q_name_raw = str(row.get("Q Name") or "").strip()
            qk = q_name_raw.lower()
            if qk:
                excel_row_lookup[qk] = row.get("excel_row")
                qname_lookup[qk] = q_name_raw

        rows: list[dict] = []
        for qk, cur_opt_entries in opt_lookup_cur.items():
            cur_code_entries = code_lookup_cur.get(qk, [])
            ref_code_entries = code_lookup_ref.get(qk, [])
            # CURRENT-only consistency: evaluate when current has parsed codes.
            # If current has none, skip to avoid duplicating pure cross-file removals.
            if not cur_code_entries:
                continue

            cur_opt_nums = _parse_int_codes(cur_opt_entries)
            cur_code_nums = _parse_int_codes(cur_code_entries)
            if not cur_opt_nums and not cur_code_nums:
                continue

            missing_in_codes = sorted(cur_opt_nums - cur_code_nums)
            extra_in_codes = sorted(cur_code_nums - cur_opt_nums)
            count_mismatch = len(cur_opt_nums) != len(cur_code_nums)
            set_mismatch = bool(missing_in_codes or extra_in_codes)
            if not (count_mismatch or set_mismatch):
                continue

            ref_opt_entries = opt_lookup_ref.get(qk, [])
            ref_opt_nums = _parse_int_codes(ref_opt_entries)
            ref_code_nums = _parse_int_codes(ref_code_entries)
            ref_missing = sorted(ref_opt_nums - ref_code_nums)
            ref_extra = sorted(ref_code_nums - ref_opt_nums)

            missing_txt = ", ".join(str(v) for v in missing_in_codes) if missing_in_codes else "(none)"
            extra_txt = ", ".join(str(v) for v in extra_in_codes) if extra_in_codes else "(none)"
            ref_missing_txt = ", ".join(str(v) for v in ref_missing) if ref_missing else "(none)"
            ref_extra_txt = ", ".join(str(v) for v in ref_extra) if ref_extra else "(none)"

            q_name = qname_lookup.get(qk, qk)

            detail_text = (
                f"current options={len(cur_opt_nums)}, codes={len(cur_code_nums)}; "
                f"missing code(s) for option positions={missing_txt}; "
                f"code(s) without corresponding option={extra_txt} | "
                f"reference options={len(ref_opt_nums)}, codes={len(ref_code_nums)}; "
                f"missing code(s) for option positions={ref_missing_txt}; "
                f"code(s) without corresponding option={ref_extra_txt}"
            )
            current_block = _formatted_codes_with_option_alignment(
                cur_code_entries,
                cur_opt_nums,
                "Current codes (code | token)",
            )
            reference_block = _formatted_codes_with_option_alignment(
                ref_code_entries,
                ref_opt_nums,
                "Reference codes (code | token)",
            )

            rows.append({
                "issue_type": "codes_option_count_mismatch",
                "set_name": "",
                "Q Name": q_name,
                "field": detail_text,
                "lang_scope": "N/A",
                "current": current_block,
                "reference": reference_block,
                "severity": "high",
                "excel_row": excel_row_lookup.get(qk),
                "current_lang": "",
                "reference_lang": "",
            })

        if not rows:
            return pl.DataFrame(schema=schema)

        base = pl.DataFrame(rows, schema=schema)
        if str(target_lang).upper() == "EN":
            return base.select([
                "issue_type", "set_name", "Q Name", "field", "lang_scope",
                "current", "reference", "severity", "excel_row",
            ])
        return base.select([
            "issue_type", "set_name", "Q Name", "field", "lang_scope",
            "current", "reference", "current_lang", "reference_lang", "severity", "excel_row",
        ])
    ```

### `build_codes_option_count_mismatch_rows._parse_int_codes` {#fn--parse-int-codes-5400}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5400`

**Signature**

```python
def _parse_int_codes(entries: list[tuple[str, str]]) -> set[int]:
```

**Returns:** `set[int]`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _parse_int_codes(entries: list[tuple[str, str]]) -> set[int]:
            out = set()
            for raw, _ in entries or []:
                s = str(raw or "").strip()
                if re.fullmatch(r"\d+", s):
                    out.add(int(s))
            return out
    ```

### `build_codes_option_count_mismatch_rows._formatted_codes_with_option_alignment` {#fn--formatted-codes-with-option-alignment-5408}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5408`

**Signature**

```python
def _formatted_codes_with_option_alignment(code_entries: list[tuple[str, str]], option_num_set: set[int], header: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `code_entries` | positional_or_keyword | Yes | `-` | `list[tuple[str, str]]` | Input used by the `Step 9 Run the full pipeline` stage. |
| `option_num_set` | positional_or_keyword | Yes | `-` | `set[int]` | Input used by the `Step 9 Run the full pipeline` stage. |
| `header` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _formatted_codes_with_option_alignment(
            code_entries: list[tuple[str, str]],
            option_num_set: set[int],
            header: str,
        ) -> str:
            vals = []
            seen = set()
            for code_raw, token_raw in code_entries or []:
                code = str(code_raw or "").strip()
                token = str(token_raw or "").strip()
                if not code and not token:
                    continue
                key = (code.lower(), token.lower())
                if key in seen:
                    continue
                seen.add(key)
                note = ""
                if re.fullmatch(r"\d+", code) and int(code) not in option_num_set:
                    note = " [NO CORRESPONDING OPTION]"
                vals.append(f"{code or '(blank)'} | {token or '(blank)'}{note}")
            if not vals:
                return f"{header}:\n(empty)"
            return f"{header}:\n" + "\n".join(vals)
    ```

### `validate_critical_sets` {#fn-validate-critical-sets-5537}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5537`

**Signature**

```python
def validate_critical_sets(questions_df: pl.DataFrame, exact_sets: dict) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Checks that each critical question group is fully present with the expected

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `exact_sets` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def validate_critical_sets(
        questions_df: pl.DataFrame,
        exact_sets  : dict,
    ) -> pl.DataFrame:
        """
        Checks that each critical question group is fully present with the expected
        Mandatory value. Rules come from critical_sets.yaml -> exact_sets.

        required=true  -> missing = issue_type 'missing_critical_question', severity HIGH
        required=false -> missing = issue_type 'advisory_question',          severity MEDIUM
        """
        EMPTY_SCHEMA = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }

        if not exact_sets:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        if "Mandatory_norm" not in questions_df.columns:
            questions_df = questions_df.with_columns(
                normalize_mandatory_expr("Mandatory").alias("Mandatory_norm")
            )

        present_qnames = set(questions_df["Q Name"].to_list())

        def _wealth_optional_variant(q_name: str) -> str:
            q = str(q_name or "").strip()
            if q.startswith("hh_wealth_"):
                return "o_hh_wealth_" + q[len("hh_wealth_"):]
            return ""

        issues = []

        for set_name, rules in exact_sets.items():
            required_names   = [r["q_name"] for r in rules if r.get("required", True)]

            for rule in rules:
                q_name   = rule["q_name"]
                expected = rule.get("expected_mandatory", "")
                required = rule.get("required", True)
                alt_q_name = _wealth_optional_variant(q_name)
                matched_q_name = q_name if q_name in present_qnames else (alt_q_name if alt_q_name in present_qnames else "")

                if not matched_q_name:
                    issues.append({
                        "issue_type": "missing_critical_question" if required else "advisory_question",
                        "set_name"  : set_name, "Q Name": q_name,
                        "field"     : "Q Name", "current": "",
                        "reference" : (f"present (or optional variant: {alt_q_name})" if alt_q_name else "present"),
                        "severity"  : "high" if required else "medium",
                        "excel_row" : None,
                    })
                    continue

                if not expected:
                    continue

                # If a wealth optional variant is accepted as substitute, treat it as pass
                # and avoid forcing mandatory parity on the alternate form.
                if matched_q_name != q_name:
                    continue

                row = (
                    questions_df
                    .filter(pl.col("Q Name") == matched_q_name)
                    .select(["Q Name", "Mandatory", "Mandatory_norm", "excel_row"])
                    .to_dicts()
                )
                if not row:
                    continue
                row = row[0]
                if row["Mandatory_norm"] != expected:
                    issues.append({
                        "issue_type": "critical_mandatory_mismatch",
                        "set_name"  : set_name, "Q Name": q_name,
                        "field"     : "Mandatory",
                        "current"   : row["Mandatory"], "reference": expected,
                        "severity"  : "high", "excel_row": row.get("excel_row"),
                    })

        if not issues:
            return pl.DataFrame(schema=EMPTY_SCHEMA)
        return pl.DataFrame(issues)
    ```

### `validate_critical_sets._wealth_optional_variant` {#fn--wealth-optional-variant-5564}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5564`

**Signature**

```python
def _wealth_optional_variant(q_name: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `q_name` | positional_or_keyword | Yes | `-` | `str` | Question identifier used to join or compare records. |

??? note "Function source"

    ```python
    def _wealth_optional_variant(q_name: str) -> str:
            q = str(q_name or "").strip()
            if q.startswith("hh_wealth_"):
                return "o_hh_wealth_" + q[len("hh_wealth_"):]
            return ""
    ```

### `validate_prefix_counts` {#fn-validate-prefix-counts-5624}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5624`

**Signature**

```python
def validate_prefix_counts(current_questions: pl.DataFrame, min_count_sets: dict) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Checks that questions with a given prefix appear at least min_count times.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `min_count_sets` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def validate_prefix_counts(
        current_questions: pl.DataFrame,
        min_count_sets   : dict,
    ) -> pl.DataFrame:
        """
        Checks that questions with a given prefix appear at least min_count times.
        Covers CS groups (cs_stress_*, cs_crisis_*, cs_emergency_*) and HDDS count.
        Rules come from critical_sets.yaml -> min_count_sets.
        """
        EMPTY_SCHEMA = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if not min_count_sets:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        all_qnames = current_questions["Q Name"].to_list()
        issues = []
        for set_name, rule in min_count_sets.items():
            prefix    = rule.get("prefix", "")
            min_count = rule.get("min_count", 1)
            desc      = rule.get("description", f"At least {min_count} '{prefix}*' questions required")
            prefix_alt = "o_hh_wealth_" if str(prefix) == "hh_wealth_" or str(set_name).upper() == "WEALTH" else ""
            matched = sorted(
                q for q in all_qnames
                if (prefix and q.startswith(prefix)) or (prefix_alt and q.startswith(prefix_alt))
            )
            if len(matched) < min_count:
                found_str = f"{len(matched)} found" + (f": {', '.join(matched)}" if matched else " (none)")
                issues.append({
                    "issue_type": "missing_critical_question", "set_name": set_name, "Q Name": "",
                    "field": "count", "current": found_str, "reference": desc,
                    "severity": "high", "excel_row": None,
                })

        if not issues:
            return pl.DataFrame(schema=EMPTY_SCHEMA)
        return pl.DataFrame(issues)
    ```

### `validate_crop_harvest` {#fn-validate-crop-harvest-5665}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5665`

**Signature**

```python
def validate_crop_harvest(current_questions: pl.DataFrame, crop_rules: dict) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Questionnaire must contain EITHER only the minimal set OR all questions in

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `crop_rules` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def validate_crop_harvest(
        current_questions: pl.DataFrame,
        crop_rules       : dict,
    ) -> pl.DataFrame:
        """
        Questionnaire must contain EITHER only the minimal set OR all questions in
        the full set. Rules come from critical_sets.yaml -> crop_harvest.
        """
        EMPTY_SCHEMA = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if not crop_rules:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        minimal = set(crop_rules.get("minimal", []))
        full    = set(crop_rules.get("full", []))
        if not minimal and not full:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        all_qnames     = set(current_questions["Q Name"].to_list())
        relevant_found = {q for q in all_qnames if q in full or q in minimal}

        if relevant_found == minimal or full.issubset(all_qnames):
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        issues = [{
            "issue_type": "crop_harvest_violation", "set_name": "CRP_HARV", "Q Name": "",
            "field": "Q Name",
            "current"  : f"found: {', '.join(sorted(relevant_found)) or 'none'}",
            "reference": f"either only [{', '.join(sorted(minimal))}] OR all of [{', '.join(sorted(full))}]",
            "severity" : "high", "excel_row": None,
        }]
        return pl.DataFrame(issues)
    ```

### `validate_authoring_consistency` {#fn-validate-authoring-consistency-5712}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5712`

**Signature**

```python
def validate_authoring_consistency(current_questions: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Current-file-only authoring consistency checks (no reference comparison):

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def validate_authoring_consistency(current_questions: pl.DataFrame) -> pl.DataFrame:
        """
        Current-file-only authoring consistency checks (no reference comparison):
          - panel_targeting_mismatch: 'Mandatory' says panel-specific but the
            recent-panelist flag disagrees, or vice versa.
          - mandatory_category_unrecognized: 'Mandatory' value doesn't match any
            of the template's known categories (likely a typo).
        """
        schema = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if "Mandatory" not in current_questions.columns:
            return pl.DataFrame(schema=schema)

        rows: list[dict] = []
        has_panelist_col = PANELIST_RECENCY_COL in current_questions.columns
        select_cols = ["Q Name", "Mandatory", "excel_row"] + ([PANELIST_RECENCY_COL] if has_panelist_col else [])

        for r in current_questions.select(select_cols).iter_rows(named=True):
            qname = r.get("Q Name")
            mand_raw = str(r.get("Mandatory") or "").strip()
            mand_norm = mand_raw.lower()
            excel_row = r.get("excel_row")

            if mand_norm and mand_norm not in _KNOWN_MANDATORY_VALUES:
                rows.append({
                    "issue_type": "mandatory_category_unrecognized",
                    "set_name": "", "Q Name": qname, "field": "Mandatory",
                    "current": mand_raw,
                    "reference": "known categories: " + " | ".join(sorted(_KNOWN_MANDATORY_VALUES)),
                    "severity": "medium", "excel_row": excel_row,
                })

            if has_panelist_col:
                mand_says_panel = "panel" in mand_norm
                panel_flag = str(r.get(PANELIST_RECENCY_COL) or "").strip().lower()
                if mand_says_panel and panel_flag in ("", "no"):
                    rows.append({
                        "issue_type": "panel_targeting_mismatch",
                        "set_name": "", "Q Name": qname, "field": PANELIST_RECENCY_COL,
                        "current": f"Mandatory='{mand_raw}' but panelist flag='{panel_flag or '(blank)'}'",
                        "reference": "panelist flag should be 'yes' when Mandatory marks the question panel-specific",
                        "severity": "medium", "excel_row": excel_row,
                    })
                elif not mand_says_panel and panel_flag == "yes":
                    rows.append({
                        "issue_type": "panel_targeting_mismatch",
                        "set_name": "", "Q Name": qname, "field": PANELIST_RECENCY_COL,
                        "current": f"Mandatory='{mand_raw}' but panelist flag='yes'",
                        "reference": "Mandatory should mention 'panel' when the panelist flag is 'yes'",
                        "severity": "medium", "excel_row": excel_row,
                    })

        return pl.DataFrame(rows, schema=schema) if rows else pl.DataFrame(schema=schema)
    ```

### `_tick` {#fn--tick-5776}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:5776`

**Signature**

```python
def _tick(label: str):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `label` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _tick(label: str):
        global _t_prev
        _now = time.perf_counter()
        print(f"[timing] {label:<34} {_now - _t_prev:8.3f}s", flush=True)
        _t_prev = _now
    ```

### `_header_row` {#fn--header-row-6447}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6447`

**Signature**

```python
def _header_row(ws, row, values):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `values` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _header_row(ws, row, values):
        for col, val in enumerate(values, 1):
            c = ws.cell(row=row, column=col, value=val)
            c.fill = FILL_HEADER; c.font = FONT_HEADER
            c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.row_dimensions[row].height = 18
    ```

### `_section_header` {#fn--section-header-6454}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6454`

**Signature**

```python
def _section_header(ws, row, title, n_cols):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `title` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `n_cols` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _section_header(ws, row, title, n_cols):
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=n_cols)
        c = ws.cell(row=row, column=1, value=title)
        c.fill = FILL_SECTION; c.font = FONT_SECTION
        c.alignment = Alignment(horizontal="left", vertical="center")
        ws.row_dimensions[row].height = 20
    ```

### `_data_row` {#fn--data-row-6461}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6461`

**Signature**

```python
def _data_row(ws, row, n_cols, severity='', fill=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `n_cols` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `severity` | positional_or_keyword | No | `''` | `-` | Severity label used for final issue classification. |
| `fill` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _data_row(ws, row, n_cols, severity="", fill=None):
        use_fill = fill or SEVERITY_FILL.get(severity)
        for col in range(1, n_cols + 1):
            c = ws.cell(row=row, column=col)
            c.font = FONT_NORMAL; c.border = THIN_BORDER
            c.alignment = Alignment(vertical="top", wrap_text=True)
            if use_fill:
                c.fill = use_fill
    ```

### `_autofit` {#fn--autofit-6470}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6470`

**Signature**

```python
def _autofit(ws, mn=12, mx=55):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `mn` | positional_or_keyword | No | `12` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `mx` | positional_or_keyword | No | `55` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _autofit(ws, mn=12, mx=55):
        for col_cells in ws.columns:
            w = max((len(str(c.value)) if c.value else 0) for c in col_cells)
            ws.column_dimensions[get_column_letter(col_cells[0].column)].width = min(max(w + 2, mn), mx)
    ```

### `_action_for_issue_type` {#fn--action-for-issue-type-6531}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6531`

**Signature**

```python
def _action_for_issue_type(issue_type: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `issue_type` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _action_for_issue_type(issue_type: str) -> str:
        key = str(issue_type or "").strip()
        return ISSUE_ACTION_MAP.get(key, "Review issue details")
    ```

### `_optional_counterparts_for_missing_skip_targets` {#fn--optional-counterparts-for-missing-skip-targets-6536}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6536`

**Signature**

```python
def _optional_counterparts_for_missing_skip_targets(source_q: str, current_text: str) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** For skipPattern_invalid_qname rows, detect whether missing target(s) have

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `source_q` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |
| `current_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _optional_counterparts_for_missing_skip_targets(source_q: str, current_text: str) -> list[str]:
        """
        For skipPattern_invalid_qname rows, detect whether missing target(s) have
        optional counterparts (o_<target>) in the current questionnaire.
        """
        try:
            _curr_df = globals().get("current_questions", None)
            _ref_df = globals().get("reference_questions", None)
            curr_qnames = set(_curr_df.get_column("Q Name").drop_nulls().to_list()) if _curr_df is not None else set()
            ref_qnames = set(_ref_df.get_column("Q Name").drop_nulls().to_list()) if _ref_df is not None else set()
            if not curr_qnames:
                return []

            invalid_targets = sorted(
                t for t in _extract_referenced_qnames(
                    str(current_text or ""),
                    source_q=str(source_q or ""),
                    ref_qnames=ref_qnames,
                    curr_qnames=curr_qnames,
                )
                if t not in curr_qnames
            )
            hits = []
            for t in invalid_targets:
                if str(t).startswith("o_"):
                    continue
                cand = f"o_{t}"
                if cand in curr_qnames:
                    hits.append(cand)
            return sorted(set(hits))
        except Exception:
            return []
    ```

### `_action_for_issue_row` {#fn--action-for-issue-row-6570}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6570`

**Signature**

```python
def _action_for_issue_row(issue_type: str, q_name: str='', current_text: str='') -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `issue_type` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |
| `q_name` | positional_or_keyword | No | `''` | `str` | Question identifier used to join or compare records. |
| `current_text` | positional_or_keyword | No | `''` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _action_for_issue_row(issue_type: str, q_name: str = "", current_text: str = "") -> str:
        key = str(issue_type or "").strip()
        if key == "skipPattern_invalid_qname":
            opt_hits = _optional_counterparts_for_missing_skip_targets(q_name, current_text)
            if opt_hits:
                return (
                    "Fix Skip Pattern target question name (target does not exist). "
                    f"Optional counterpart found ({', '.join(opt_hits)}): verify compatibility before replacing."
                )
        return _action_for_issue_type(key)
    ```

### `_issues_col_map` {#fn--issues-col-map-6582}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6582`

**Signature**

```python
def _issues_col_map(field_label: str='Field'):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `field_label` | positional_or_keyword | No | `'Field'` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _issues_col_map(field_label: str = "Field"):
        lang_code = str(globals().get("target_lang", "")).upper().strip()
        lang_label = lang_code if (lang_code and lang_code != "EN") else "Language"
        return [
            ("issue_type",    "Issue type"),
            ("mandatory_cat", "Type"),
            ("set_name",      "Set"),
            ("Q Name",        "Q Name"),
            ("module",        "Module"),
            ("field",         field_label),
            ("lang_scope",    "Language scope"),
            ("current",       "Current value"),
            ("reference",     "Reference / rule"),
            ("current_lang",    f"Current value ({lang_label})"),
            ("reference_lang",  f"Reference / rule ({lang_label})"),
            ("current_en",    "Current value (EN)"),
            ("reference_en",  "Reference / rule (EN)"),
            ("action",        "Action"),
            ("severity",      "Severity"),
            ("excel_row",     "Excel row"),
        ]
    ```

### `_issues_table` {#fn--issues-table-6605}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6605`

**Signature**

```python
def _issues_table(ws, start_row, df, field_label: str='Field'):
```

**Returns:** `None or implicit return`

**What it does:** Renders a header + data table. Only columns present in df are shown.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `start_row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `df` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `field_label` | positional_or_keyword | No | `'Field'` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _issues_table(ws, start_row, df, field_label: str = "Field"):
        """Renders a header + data table. Only columns present in df are shown."""
        if "issue_type" in df.columns:
            _q_expr = pl.col("Q Name") if "Q Name" in df.columns else pl.lit("")
            _cur_expr = pl.col("current") if "current" in df.columns else pl.lit("")
            _action_expr = (
                pl.struct([
                    pl.col("issue_type").alias("_issue"),
                    _q_expr.alias("_q"),
                    _cur_expr.alias("_cur"),
                ])
                .map_elements(
                    lambda r: _action_for_issue_row(r.get("_issue"), r.get("_q"), r.get("_cur")),
                    return_dtype=pl.Utf8,
                )
                .alias("_action_default")
            )
            if "action" not in df.columns:
                df = df.with_columns(_action_expr).rename({"_action_default": "action"})
            else:
                df = df.with_columns([
                    _action_expr,
                    pl.coalesce([pl.col("action"), pl.col("_action_default")]).alias("action"),
                ]).drop("_action_default")
        cols = [(s, d) for s, d in _issues_col_map(field_label=field_label) if s in df.columns]
        qname_col = next((i for i, (src, _) in enumerate(cols, start=1) if src == "Q Name"), None)
        _header_row(ws, start_row, [d for _, d in cols])
        r = start_row + 1
        if df.height == 0:
            c = ws.cell(row=r, column=1, value="No issues in this category")
            c.font = Font(bold=True, color="274E13", size=10)
            return r + 2
        for row_data in df.to_dicts():
            for col, (src, _) in enumerate(cols, 1):
                ws.cell(row=r, column=col, value=row_data.get(src))
            _data_row(ws, r, len(cols), row_data.get("severity", ""))
            if qname_col:
                ws.cell(row=r, column=qname_col).font = Font(bold=True, size=10)
            r += 1
        ws.freeze_panes = f"A{start_row + 1}"
        ws.auto_filter.ref = f"A{start_row}:{get_column_letter(len(cols))}{start_row}"
        return r + 1
    ```

### `_tokenize_for_word_diff` {#fn--tokenize-for-word-diff-6660}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6660`

**Signature**

```python
def _tokenize_for_word_diff(text: str):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _tokenize_for_word_diff(text: str):
        raw = re.findall(r"\s+|\S+", text)
        out = []
        for tok in raw:
            if tok.isspace() and out:
                out[-1] = out[-1] + tok
            else:
                out.append(tok)
        return out
    ```

### `_coalesce_segments` {#fn--coalesce-segments-6671}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6671`

**Signature**

```python
def _coalesce_segments(parts):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `parts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |

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

### `_build_diff_segments` {#fn--build-diff-segments-6683}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6683`

**Signature**

```python
def _build_diff_segments(current_text: str, reference_text: str):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |
| `reference_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

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

### `_set_rich_text` {#fn--set-rich-text-6702}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6702`

**Signature**

```python
def _set_rich_text(cell, full_text: str, parts):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cell` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `full_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |
| `parts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |

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

### `_set_rich_text_with_bold_tokens` {#fn--set-rich-text-with-bold-tokens-6718}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6718`

**Signature**

```python
def _set_rich_text_with_bold_tokens(cell, full_text: str, tokens: list[str], color: str='FF000000', bold: bool=True):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cell` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `full_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |
| `tokens` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 10 Export to Excel` stage. |
| `color` | positional_or_keyword | No | `'FF000000'` | `str` | Input used by the `Step 10 Export to Excel` stage. |
| `bold` | positional_or_keyword | No | `True` | `bool` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _set_rich_text_with_bold_tokens(
        cell,
        full_text: str,
        tokens: list[str],
        color: str = "FF000000",
        bold: bool = True,
    ):
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
            blocks.append(TextBlock(InlineFont(color=color, b=bold), txt[s:e]))
            pos = e
        if pos < len(txt):
            blocks.append(TextBlock(InlineFont(color="FF000000", b=False), txt[pos:]))

        cell.value = CellRichText(*blocks) if blocks else full_text
    ```

### `_apply_inline_diff_for_issue` {#fn--apply-inline-diff-for-issue-6762}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6762`

**Signature**

```python
def _apply_inline_diff_for_issue(ws, start_row, df, issue_types):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `start_row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `df` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `issue_types` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _apply_inline_diff_for_issue(ws, start_row, df, issue_types):
        if df.height == 0:
            return

        cols = [(s, d) for s, d in _issues_col_map() if s in df.columns]
        cidx = {src: i for i, (src, _) in enumerate(cols, start=1)}

        _allowed = set(issue_types or [])

        def _match_issue(issue_val: str) -> bool:
            for allowed in _allowed:
                if isinstance(allowed, str) and allowed.endswith("*"):
                    if issue_val.startswith(allowed[:-1]):
                        return True
                elif issue_val == allowed:
                    return True
            return False

        compare_pairs = [("current", "reference")]
        if "current_lang" in cidx and "reference_lang" in cidx:
            compare_pairs.append(("current_lang", "reference_lang"))
        if "current_en" in cidx and "reference_en" in cidx:
            compare_pairs.append(("current_en", "reference_en"))

        for offset, rd in enumerate(df.to_dicts(), start=1):
            issue_val = str(rd.get("issue_type") or "")
            if not _match_issue(issue_val):
                continue

            for cur_key, ref_key in compare_pairs:
                cur_txt = str(rd.get(cur_key) or "")
                ref_txt = str(rd.get(ref_key) or "")
                if cur_txt == ref_txt:
                    continue
                cur_parts, ref_parts = _build_diff_segments(cur_txt, ref_txt)
                _set_rich_text(ws.cell(row=start_row + offset, column=cidx[cur_key]), cur_txt, cur_parts)
                _set_rich_text(ws.cell(row=start_row + offset, column=cidx[ref_key]), ref_txt, ref_parts)
    ```

### `_apply_inline_diff_for_issue._match_issue` {#fn--match-issue-6771}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6771`

**Signature**

```python
def _match_issue(issue_val: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `issue_val` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

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

### `_apply_option_detail_highlights` {#fn--apply-option-detail-highlights-6801}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6801`

**Signature**

```python
def _apply_option_detail_highlights(ws, start_row, df):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `start_row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `df` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _apply_option_detail_highlights(ws, start_row, df):
        if df.height == 0:
            return
        cols = [(s, d) for s, d in _issues_col_map() if s in df.columns]
        cidx = {src: i for i, (src, _) in enumerate(cols, start=1)}
        issue_col = cidx.get("issue_type")
        detail_col = cidx.get("field")
        if not issue_col or not detail_col:
            return

        bold_tokens_map = {
            "added_option": ["added"],
            "removed_option": ["removed"],
            "added_removed_option": ["both added and removed", "added", "removed"],
            "added_option_with_drift": ["added", "drift"],
            "removed_option_with_drift": ["removed", "drift"],
            "added_removed_option_with_drift": ["added", "removed", "drift"],
            "added_removed_codes": ["added", "removed"],
            "added_codes_with_drift": ["added", "drift"],
            "removed_codes_with_drift": ["removed", "drift"],
            "added_removed_codes_with_drift": ["added", "removed", "drift"],
        }

        for offset, rd in enumerate(df.to_dicts(), start=1):
            issue_val = str(rd.get("issue_type") or "")
            detail_txt = str(rd.get("field") or "")
            if not detail_txt:
                continue
            tokens = bold_tokens_map.get(issue_val)
            if not tokens:
                continue
            _set_rich_text_with_bold_tokens(
                ws.cell(row=start_row + offset, column=detail_col),
                detail_txt,
                tokens,
            )
    ```

### `_apply_codes_alignment_marker_highlights` {#fn--apply-codes-alignment-marker-highlights-6839}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6839`

**Signature**

```python
def _apply_codes_alignment_marker_highlights(ws, start_row, df):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `start_row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `df` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _apply_codes_alignment_marker_highlights(ws, start_row, df):
        if df.height == 0:
            return
        cols = [(s, d) for s, d in _issues_col_map() if s in df.columns]
        cidx = {src: i for i, (src, _) in enumerate(cols, start=1)}
        issue_col = cidx.get("issue_type")
        if not issue_col:
            return

        marker_tokens = ["NO CORRESPONDING OPTION", "ADDED CODE", "REMOVED CODE"]
        target_cols = [k for k in ["current", "reference"] if k in cidx]
        if not target_cols:
            return

        target_issue_types = {
            "codes_option_count_mismatch",
            "codes_added",
            "codes_removed",
            "added_removed_codes",
            "added_codes_with_drift",
            "removed_codes_with_drift",
            "added_removed_codes_with_drift",
        }

        for offset, rd in enumerate(df.to_dicts(), start=1):
            issue_val = str(rd.get("issue_type") or "")
            if issue_val not in target_issue_types:
                continue
            for col_key in target_cols:
                txt = str(rd.get(col_key) or "")
                if not txt:
                    continue
                _set_rich_text_with_bold_tokens(
                    ws.cell(row=start_row + offset, column=cidx[col_key]),
                    txt,
                    marker_tokens,
                    color="FFFF0000",
                    bold=True,
                )
    ```

### `_set_status` {#fn--set-status-6882}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6882`

**Signature**

```python
def _set_status(all_issues, rules):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `rules` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _set_status(all_issues, rules):
        results = []
        for set_name in rules.get("exact_sets", {}).keys():
            si   = all_issues.filter(pl.col("set_name") == set_name)
            high = si.filter(pl.col("severity") == "high").height
            med  = si.filter(pl.col("severity") == "medium").height
            if high > 0:
                status  = "FAIL"
                details = "; ".join(f"{r['Q Name'] or r['current']}" for r in si.filter(pl.col("severity") == "high").to_dicts())
            elif med > 0:
                status  = "WARNING"
                details = "; ".join(f"{r['Q Name'] or r['current']}" for r in si.to_dicts())
            else:
                status, details = "PASS", "All required questions present and correct"
            results.append({"set": set_name, "status": status, "details": details})
        for set_name, rule in rules.get("min_count_sets", {}).items():
            si = all_issues.filter(pl.col("set_name") == set_name)
            if si.filter(pl.col("severity").is_in(["high", "medium"])).height > 0:
                status, details = "FAIL", si["current"].to_list()[0]
            else:
                status  = "PASS"
                details = f">={rule.get('min_count',0)} {rule.get('prefix','')}* questions confirmed"
            results.append({"set": set_name, "status": status, "details": details})
        if rules.get("crop_harvest"):
            crp = all_issues.filter(pl.col("set_name") == "CRP_HARV")
            if crp.height > 0:
                status, details = "FAIL", crp["current"].to_list()[0]
            else:
                status, details = "PASS", "Crop harvest rule respected"
            results.append({"set": "CRP_HARV", "status": status, "details": details})

        return results
    ```

### `_cat_counts` {#fn--cat-counts-6916}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6916`

**Signature**

```python
def _cat_counts(df):
```

**Returns:** `None or implicit return`

**What it does:** Returns counts by mandatory_cat for the four standard categories.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _cat_counts(df):
        """Returns counts by mandatory_cat for the four standard categories."""
        cats = ["mandatory", "mandatory-panel", "non-mandatory", "optional"]
        if "mandatory_cat" not in df.columns or df.height == 0:
            return {c: 0 for c in cats}
        return {cat: df.filter(pl.col("mandatory_cat") == cat).height for cat in cats}
    ```

### `_extract_round_token` {#fn--extract-round-token-6924}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6924`

**Signature**

```python
def _extract_round_token(name: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _extract_round_token(name: str) -> str:
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

### `_extract_iso3_token` {#fn--extract-iso3-token-6939}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6939`

**Signature**

```python
def _extract_iso3_token(name: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _extract_iso3_token(name: str) -> str:
        txt = str(name or "").upper()
        cfg_iso = str(getattr(globals().get("cfg", None), "iso3", "") or "").upper().strip()
        if cfg_iso and re.search(rf"(?:^|[_\-\s]){re.escape(cfg_iso)}(?:$|[_\-\s])", txt):
            return cfg_iso

        # Handle common country-name tokens used in operational filenames.
        if "DRC" in txt or "CONGO" in txt:
            return "COD"
        if "YEMEN" in txt:
            return "YEM"
        if "MYANMAR" in txt:
            return "MMR"

        # Fallback: pick the first 3-letter token that is not a known boilerplate tag.
        banned = {
            "FAO", "WFP", "CATI", "VHF", "VFG", "VFF", "VFA", "ISO", "HHQ",
            "QNR", "EN", "AR", "FR", "ES", "PT",
        }
        tokens = re.findall(r"\b([A-Z]{3})\b", txt)
        for tok in tokens:
            if tok == "DRC":
                return "COD"
            if tok not in banned:
                return tok
        return ""
    ```

### `_reference_descriptor` {#fn--reference-descriptor-6967}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6967`

**Signature**

```python
def _reference_descriptor() -> str:
```

**Returns:** `str`

**What it does:** Human-readable reference descriptor for Summary header.

**Parameters**

No parameters.

??? note "Function source"

    ```python
    def _reference_descriptor() -> str:
        """
        Human-readable reference descriptor for Summary header.
        Example:
          previous_round | COD R8 | GeoPoll_FAO_DRC_Round_8_CATI_V4_copy.xlsx
          latest_template | EN template | household_questionnaire_geopoll_EN_template_20250708_ISO3.xlsx
        """
        _run = globals().get("run", {}) or {}
        _cfg = globals().get("cfg", None)
        mode = _reference_scope_label()
        ref_name = Path(_run.get("reference_path", "")).name if _run.get("reference_path") else ""
        lang = str(getattr(_cfg, "language", "") or "").upper()

        if mode == "previous round":
            iso = _extract_iso3_token(ref_name) or str(getattr(_cfg, "iso3", "") or "").upper()
            rnd = _extract_round_token(ref_name) or "R?"
            return f"{mode} | {iso} {rnd} | {ref_name}"
        return f"{mode} | {lang} template | {ref_name}"
    ```

### `_write_category_breakdown_block` {#fn--write-category-breakdown-block-6987}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:6987`

**Signature**

```python
def _write_category_breakdown_block(ws, r: int, title: str, categories: list[tuple], all_issues: pl.DataFrame) -> int:
```

**Returns:** `int`

**What it does:** Renders a category-count breakdown table (Total/Mandatory/M-Panel/Non-mand./

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `r` | positional_or_keyword | Yes | `-` | `int` | Input used by the `Step 10 Export to Excel` stage. |
| `title` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |
| `categories` | positional_or_keyword | Yes | `-` | `list[tuple]` | Input used by the `Step 10 Export to Excel` stage. |
| `all_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _write_category_breakdown_block(
        ws,
        r: int,
        title: str,
        categories: list[tuple],
        all_issues: pl.DataFrame,
    ) -> int:
        """
        Renders a category-count breakdown table (Total/Mandatory/M-Panel/Non-mand./
        Optional/Severity). Non-zero categories are shown first (grouped, if a group
        label is supplied); all-zero categories are folded into a single line instead
        of one row each, so the table stays scannable as more categories are added.

        Each entry in `categories` is (label, issue_type, severity_filter_or_None,
        display_severity[, group_label]).
        """
        _section_header(ws, r, title, 7); r += 1
        _header_row(ws, r, ["Category", "Total", "Mandatory", "M-Panel", "Non-mand.", "Optional", "Severity"]); r += 1

        computed = []
        for entry in categories:
            label, itype, sev_filter, disp_sev = entry[:4]
            group = entry[4] if len(entry) > 4 else None
            q = all_issues.filter(pl.col("issue_type") == itype)
            if sev_filter:
                q = q.filter(pl.col("severity") == sev_filter)
            computed.append({
                "label": label,
                "total": q.height,
                "counts": _cat_counts(q),
                "disp_sev": disp_sev if q.height > 0 else "none",
                "group": group,
            })

        nonzero = [c for c in computed if c["total"] > 0]
        zero = [c for c in computed if c["total"] == 0]

        total_line = f"{len(nonzero)} categor{'y' if len(nonzero) == 1 else 'ies'} with issues"
        if zero:
            total_line += f"  --  {len(zero)} clean"
        ws.cell(row=r, column=1, value=total_line).font = Font(bold=True, size=10, italic=True, color="1F4E78")
        r += 1

        seen_groups: list = []
        for c in nonzero:
            if c["group"] not in seen_groups:
                seen_groups.append(c["group"])

        for grp in seen_groups:
            if grp:
                ws.cell(row=r, column=1, value=grp).font = Font(bold=True, size=10, color="666666")
                r += 1
            for c in [x for x in nonzero if x["group"] == grp]:
                ws.cell(row=r, column=1, value=c["label"])
                ws.cell(row=r, column=2, value=c["total"])
                ws.cell(row=r, column=3, value=c["counts"]["mandatory"])
                ws.cell(row=r, column=4, value=c["counts"]["mandatory-panel"])
                ws.cell(row=r, column=5, value=c["counts"]["non-mandatory"])
                ws.cell(row=r, column=6, value=c["counts"]["optional"])
                ws.cell(row=r, column=7, value=c["disp_sev"])
                _data_row(ws, r, 7, c["disp_sev"])
                r += 1

        if zero:
            zero_text = "No issues: " + ", ".join(c["label"] for c in zero)
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
            ws.cell(row=r, column=1, value=zero_text)
            _data_row(ws, r, 7, fill=FILL_PASS)
            r += 1

        return r
    ```

### `write_summary_sheet` {#fn-write-summary-sheet-7061}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7061`

**Signature**

```python
def write_summary_sheet(wb, all_issues, rules, replacement_status=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `rules` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `replacement_status` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def write_summary_sheet(wb, all_issues, rules, replacement_status=None):
        ws = wb.create_sheet("Summary")
        ws.sheet_view.showGridLines = False
        # A=category/set  B=total/status  C=mandatory/details  D=m-panel  E=non-mand.  F=optional  G=severity
        for col, w in zip("ABCDEFG", [32, 8, 13, 10, 13, 10, 14]):
            ws.column_dimensions[col].width = w

        ws.merge_cells("A1:G1")
        ws["A1"] = "GeoPoll Questionnaire Validation Report"
        ws["A1"].font = FONT_TITLE
        ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
        ws.row_dimensions[1].height = 26

        _curr_name = Path((globals().get("run", {}) or {}).get("questionnaire_path", "")).name
        _curr_iso = str(getattr(globals().get("cfg", None), "iso3", "") or "").upper()
        _curr_round = _extract_round_token(_curr_name) or "R?"
        _cfg_lang = str(getattr(globals().get("cfg", None), "language", "") or "").upper()
        _effective_lang = str(globals().get("target_lang", "") or "").upper()
        _effective_src = str(globals().get("target_lang_source", "") or "").strip()
        _summary_info_lines = [
            f"Comparison basis: {_reference_scope_label()}",
            f"Current questionnaire: {_curr_iso} {_curr_round} | {_curr_name}",
            f"Checked against: {_reference_descriptor()}",
            f"Language scope: EN baseline + {_effective_lang or _cfg_lang} (configured={_cfg_lang or 'N/A'}; source={_effective_src or 'config'})",
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
            ws.merge_cells(f"A{_i}:G{_i}")
            ws[f"A{_i}"] = _line
            ws[f"A{_i}"].font = Font(
                size=10,
                color="274E13" if _i == 2 else "1F4E78",
                italic=True,
            )
            ws[f"A{_i}"].alignment = Alignment(horizontal="left", vertical="center")

        r = len(_summary_info_lines) + 2
        #  Critical sets 
        _section_header(ws, r, "CRITICAL SETS STATUS", 7); r += 1
        _header_row(ws, r, ["Critical set", "Status", "Details", "", "", "", ""]); r += 1
        for row_data in _set_status(all_issues, rules):
            fill = STATUS_FILL.get(row_data["status"])
            ws.cell(row=r, column=1, value=row_data["set"])
            ws.cell(row=r, column=2, value=row_data["status"])
            ws.cell(row=r, column=3, value=row_data["details"])
            _data_row(ws, r, 7, fill=fill); r += 1

        r += 1
        #  Structure checks (aligned with KoBo summary order)
        _section_header(ws, r, "QUESTIONNAIRE STRUCTURE CHECKS", 7); r += 1
        _header_row(ws, r, ["Check", "Status", "Details", "", "", "", ""]); r += 1

        _skip_df = all_issues.filter(pl.col("issue_type").is_in(list(SKIP_PATTERN_ISSUE_TYPES)))
        _skip_high = _skip_df.filter(pl.col("severity") == "high").height
        _skip_med = _skip_df.filter(pl.col("severity") == "medium").height
        _skip_info = _skip_df.filter(pl.col("severity") == "info").height

        ws.cell(row=r, column=1, value="Skip logic references")
        ws.cell(row=r, column=2, value="FAIL" if _skip_high > 0 else "PASS")
        ws.cell(row=r, column=3, value=(f"High severity issues: {_skip_high}" if _skip_high > 0 else "No high severity issues"))
        _data_row(ws, r, 7, fill=STATUS_FILL.get("FAIL" if _skip_high > 0 else "PASS")); r += 1

        _skip_warn_total = _skip_med + _skip_info
        ws.cell(row=r, column=1, value="Skip logic references")
        ws.cell(row=r, column=2, value="WARN" if _skip_warn_total > 0 else "PASS")
        ws.cell(row=r, column=3, value=(f"Medium severity issues: {_skip_med}; Info: {_skip_info}" if _skip_warn_total > 0 else "No medium/info issues"))
        _data_row(ws, r, 7, fill=STATUS_FILL.get("WARN" if _skip_warn_total > 0 else "PASS")); r += 1

        _dup_n = all_issues.filter(pl.col("issue_type") == "duplicate_qname").height
        _dup_st = "FAIL" if _dup_n > 0 else "PASS"
        ws.cell(row=r, column=1, value="Duplicate Q Names")
        ws.cell(row=r, column=2, value=_dup_st)
        ws.cell(row=r, column=3, value=f"{_dup_n} duplicate(s) found" if _dup_n else "No duplicates")
        _data_row(ws, r, 7, fill=STATUS_FILL.get(_dup_st)); r += 1

        _qt_df = all_issues.filter(pl.col("issue_type").is_in(list(QTYPE_ISSUE_TYPES)))
        _qt_high = _qt_df.filter(pl.col("severity") == "high").height
        _qt_med = _qt_df.filter(pl.col("severity") == "medium").height
        _qt_info = _qt_df.filter(pl.col("severity") == "info").height
        _qt_status = "FAIL" if _qt_high > 0 else ("WARN" if (_qt_med + _qt_info) > 0 else "PASS")
        ws.cell(row=r, column=1, value="Q Type integrity")
        ws.cell(row=r, column=2, value=_qt_status)
        ws.cell(row=r, column=3, value=f"High: {_qt_high}; Medium: {_qt_med}; Info: {_qt_info}")
        _data_row(ws, r, 7, fill=STATUS_FILL.get(_qt_status)); r += 1

        _mod_removed = all_issues.filter(pl.col("issue_type") == "module_removed").height
        _mod_added = all_issues.filter(pl.col("issue_type") == "module_added").height
        _mod_status = "FAIL" if _mod_removed > 0 else "PASS"
        ws.cell(row=r, column=1, value="Module presence (template-required)")
        ws.cell(row=r, column=2, value=_mod_status)
        ws.cell(
            row=r,
            column=3,
            value=(
                f"Template modules missing: {_mod_removed}; Modules added vs reference: {_mod_added}"
                if _mod_removed > 0 else
                f"No template module missing; Modules added vs reference: {_mod_added}"
            ),
        )
        _data_row(ws, r, 7, fill=STATUS_FILL.get(_mod_status)); r += 1

        r += 1
        #  Replacement status
        _section_header(ws, r, "REPLACEMENT STATUS (validated questionnaire output)", 7); r += 1
        _header_row(ws, r, ["Check", "Status", "Details", "", "", "", ""]); r += 1

        _repl_rows = (replacement_status or {}).get("rows", [])
        if not _repl_rows:
            ws.cell(row=r, column=1, value="Replacement step not run")
            ws.cell(row=r, column=2, value="INFO")
            ws.cell(row=r, column=3, value="No replacement diagnostics available for this run.")
            _data_row(ws, r, 7, "info"); r += 1
        else:
            for rd in _repl_rows:
                sev = rd.get("severity", "info")
                st = str(rd.get("status", "INFO") or "INFO").upper()
                ws.cell(row=r, column=1, value=rd.get("check", ""))
                ws.cell(row=r, column=2, value=st)
                ws.cell(row=r, column=3, value=rd.get("details", ""))
                row_fill = STATUS_FILL.get(st) or SEVERITY_FILL.get(sev)
                _data_row(ws, r, 7, fill=row_fill)
                if st == "PASS":
                    ws.cell(row=r, column=2).font = Font(bold=True, size=10, color="274E13")
                elif st in {"WARN", "WARNING"}:
                    ws.cell(row=r, column=2).font = Font(bold=True, size=10, color="B45F06")
                elif st == "FAIL":
                    ws.cell(row=r, column=2).font = Font(bold=True, size=10, color="CC0000")
                r += 1

        r += 1
        #  Core question changes (high/medium focus)
        r = _write_category_breakdown_block(
            ws, r, "QUESTION CHANGES (CORE)",
            [
                ("Mandatory source unavailable", "mandatory_source_missing", None, "high"),
                ("Mandatory flag changes",       "mandatory_column_mismatch", None, "high"),
                ("Mandatory to optional",        "mandatory_to_optional", None, "high"),
                ("Questions removed (high)",     "removed_question", "high", "high"),
                ("Questions removed (info)",     "removed_question", "info", "info"),
                ("Questions added (high)",       "added_question", "high", "high"),
                ("Questions added (info)",       "added_question", "info", "info"),
                ("Question labels changed",      "question_label_mismatch", None, "medium"),
            ],
            all_issues,
        )

        r += 1
        #  Additional control-field diffs
        r = _write_category_breakdown_block(
            ws, r, "QUESTION CHANGES (ADDITIONAL FIELDS)",
            [
                ("Conditional changed", "conditional_changed", None, "info"),
                ("Conditional removed (mandatory)", "conditional_removed_mandatory", None, "high"),
                ("Universe changed", "universe_changed", None, "medium"),
            ],
            all_issues,
        )

        r += 1
        #  Option changes (7 cols with mandatory breakdown)
        r = _write_category_breakdown_block(
            ws, r, "OPTION CHANGES (questions present in both files)",
            [
                ("Options added/removed",          "added_removed_option",                None, "high",   "OPTIONS"),
                ("Options removed",                 "removed_option",                     None, "high",   "OPTIONS"),
                ("Options added with drift",        "added_option_with_drift",            None, "high",   "OPTIONS"),
                ("Options removed with drift",      "removed_option_with_drift",          None, "high",   "OPTIONS"),
                ("Add/remove with drift",           "added_removed_option_with_drift",    None, "high",   "OPTIONS"),
                ("Removed + cascading drift",       "removed_option_cascading_drift",     None, "high",   "OPTIONS"),
                ("Options added",                   "added_option",                       None, "medium", "OPTIONS"),
                ("Option labels changed",           "option_label_mismatch",              None, "medium", "OPTIONS"),
                ("Option positions changed",        "option_position_drift",              None, "high",   "OPTIONS"),
                ("Codes token mismatch",            "codes_token_mismatch",               None, "high",   "CODES"),
                ("Codes removed",                   "codes_removed",                      None, "high",   "CODES"),
                ("Codes added",                     "codes_added",                        None, "high",   "CODES"),
                ("Codes added/removed",             "added_removed_codes",                None, "high",   "CODES"),
                ("Codes added with drift",          "added_codes_with_drift",             None, "high",   "CODES"),
                ("Codes removed with drift",        "removed_codes_with_drift",           None, "high",   "CODES"),
                ("Codes add/remove with drift",     "added_removed_codes_with_drift",     None, "high",   "CODES"),
                ("Codes renumbered (same token)",   "codes_position_drift",               None, "high",   "CODES"),
                ("Codes count vs options mismatch", "codes_option_count_mismatch",        None, "high",   "CODES"),
                ("Codes not comparable",            "codes_not_comparable",               None, "info",   "CODES"),
            ],
            all_issues,
        )
    ```

### `write_structure_skip_sheet` {#fn-write-structure-skip-sheet-7262}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7262`

**Signature**

```python
def write_structure_skip_sheet(wb, all_issues: pl.DataFrame):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def write_structure_skip_sheet(wb, all_issues: pl.DataFrame):
        ws = wb.create_sheet("Questionnaire Structure")
        ws.sheet_view.showGridLines = False

        def _sorted(df: pl.DataFrame) -> pl.DataFrame:
            if df.height == 0:
                return df
            return (
                df.with_columns(
                    pl.when(pl.col("severity") == "high").then(pl.lit(0))
                    .when(pl.col("severity") == "medium").then(pl.lit(1))
                    .otherwise(pl.lit(2))
                    .alias("_s")
                )
                .sort(["_s", "issue_type", "Q Name"])
                .drop("_s")
            )

        skip_df = _sorted(all_issues.filter(pl.col("issue_type").is_in(list(SKIP_PATTERN_ISSUE_TYPES))))
        qtype_df = _sorted(all_issues.filter(pl.col("issue_type").is_in(list(QTYPE_ISSUE_TYPES))))
        dup_df = _sorted(all_issues.filter(pl.col("issue_type") == "duplicate_qname"))
        module_df = _sorted(all_issues.filter(pl.col("issue_type").is_in(list(MODULE_ISSUE_TYPES))))
        dup_module_df = _sorted(pl.concat([dup_df, module_df], how="diagonal")) if (dup_df.height > 0 or module_df.height > 0) else dup_df
        authoring_df = _sorted(all_issues.filter(pl.col("issue_type").is_in(list(AUTHORING_CONSISTENCY_ISSUE_TYPES))))

        _section_header(ws, 1, "QUESTIONNAIRE STRUCTURE  Skip pattern issues", 8)
        next_row = _issues_table(ws, 2, skip_df)

        _section_header(ws, next_row, "Q TYPE INTEGRITY ISSUES", 8)
        next_row = _issues_table(ws, next_row + 1, qtype_df)

        _section_header(ws, next_row, "QUESTIONNAIRE STRUCTURE  (Duplicates, modules)", 8)
        next_row = _issues_table(ws, next_row + 1, dup_module_df)

        _section_header(ws, next_row, "AUTHORING CONSISTENCY CHECKS  (Mandatory / panel targeting)", 8)
        _issues_table(ws, next_row + 1, authoring_df)

        ws.freeze_panes = "A3"
        _autofit(ws)
    ```

### `write_structure_skip_sheet._sorted` {#fn--sorted-7266}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7266`

**Signature**

```python
def _sorted(df: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _sorted(df: pl.DataFrame) -> pl.DataFrame:
            if df.height == 0:
                return df
            return (
                df.with_columns(
                    pl.when(pl.col("severity") == "high").then(pl.lit(0))
                    .when(pl.col("severity") == "medium").then(pl.lit(1))
                    .otherwise(pl.lit(2))
                    .alias("_s")
                )
                .sort(["_s", "issue_type", "Q Name"])
                .drop("_s")
            )
    ```

### `write_replacement_issues_sheet` {#fn-write-replacement-issues-sheet-7303}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7303`

**Signature**

```python
def write_replacement_issues_sheet(wb, all_issues: pl.DataFrame):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def write_replacement_issues_sheet(wb, all_issues: pl.DataFrame):
        ws = wb.create_sheet("Replacement Issues")
        ws.sheet_view.showGridLines = False

        df = all_issues.filter(
            pl.col("issue_type").is_in(list(REPLACEMENT_ISSUE_TYPES))
        )
        if df.height > 0:
            df = (
                df.with_columns(
                    pl.when(pl.col("severity") == "high").then(pl.lit(0))
                    .when(pl.col("severity") == "medium").then(pl.lit(1))
                    .otherwise(pl.lit(2))
                    .alias("_s")
                )
                .sort(["_s", "issue_type", "Q Name"])
                .drop("_s")
            )

        _section_header(ws, 1, "REPLACEMENT ISSUES  Placeholder/additional-info diagnostics", 8)
        _issues_table(ws, 2, df)
        ws.freeze_panes = "A3"
        _autofit(ws)
    ```

### `write_critical_sets_sheet` {#fn-write-critical-sets-sheet-7329}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7329`

**Signature**

```python
def write_critical_sets_sheet(wb, all_issues, found_info=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `found_info` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def write_critical_sets_sheet(wb, all_issues, found_info=None):
        ws = wb.create_sheet("Critical Sets")
        ws.sheet_view.showGridLines = False

        df = all_issues.filter(
            pl.col("issue_type").is_in(list(CRITICAL_SET_ISSUE_TYPES))
        ).sort(["set_name", "severity", "Q Name"])

        _section_header(ws, 1, "CRITICAL SETS  Structural validation issues", 8)
        next_row = _issues_table(ws, 2, df)

        if found_info:
            next_row += 1
            _section_header(ws, next_row, "QUESTIONS FOUND IN CURRENT QUESTIONNAIRE", 3)
            next_row += 1
            _header_row(ws, next_row, ["Set", "Count found", "Questions"])
            next_row += 1
            for set_name, questions in found_info.items():
                ws.cell(row=next_row, column=1, value=set_name)
                ws.cell(row=next_row, column=2, value=len(questions))
                ws.cell(row=next_row, column=3, value=", ".join(questions) if questions else "none found")
                _data_row(ws, next_row, 3, "info" if questions else "high")
                next_row += 1

        _autofit(ws)
    ```

### `write_question_changes_sheet` {#fn-write-question-changes-sheet-7357}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7357`

**Signature**

```python
def write_question_changes_sheet(wb, question_changes_view):
```

**Returns:** `None or implicit return`

**What it does:** Question-level changes split into:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `question_changes_view` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def write_question_changes_sheet(wb, question_changes_view):
        """
        Question-level changes split into:
        1) core changes (presence/mandatory/label)
        2) additional informational control-field changes.
        """
        ws = wb.create_sheet("Question Changes")
        ws.sheet_view.showGridLines = False

        df = (
            question_changes_view
            .with_columns(
                pl.when(pl.col("severity") == "high").then(pl.lit(0))
                .when(pl.col("severity") == "medium").then(pl.lit(1))
                .otherwise(pl.lit(2))
                .alias("_s")
            )
            .sort(["_s", "issue_type", "Q Name"])
            .drop("_s")
        )
        if "set_name" in df.columns:
            df = df.drop("set_name")

        core_df = df.filter(pl.col("issue_type").is_in(list(CORE_QUESTION_CHANGE_ISSUE_TYPES)))
        additional_df = df.filter(pl.col("issue_type").is_in(list(ADDITIONAL_QUESTION_FIELD_ISSUE_TYPES)))
        additional_df = additional_df.with_columns(pl.lit("info").alias("severity"))

        _section_header(ws, 1, "QUESTION CHANGES (CORE)  Presence, mandatory, labels", 10)
        next_row = _issues_table(ws, 2, core_df)
        _apply_inline_diff_for_issue(
            ws,
            2,
            core_df,
            {"question_label_mismatch", "conditional_removed_mandatory", "universe_changed"},
        )

        _section_header(ws, next_row, "QUESTION CHANGES (ADDITIONAL FIELDS)", 10)
        _issues_table(ws, next_row + 1, additional_df)
        _apply_inline_diff_for_issue(
            ws,
            next_row + 1,
            additional_df,
            {"conditional_changed"},
        )
        # Keep navigation stable even with multiple tables in this sheet.
        # Without resetting here, the second table can push freeze panes far down.
        ws.freeze_panes = "A3"
        _cols = [(s, d) for s, d in _issues_col_map() if s in df.columns]
        if _cols:
            _n = len(_cols)
            ws.auto_filter.ref = f"A2:{get_column_letter(_n)}2"
        _autofit(ws)
    ```

### `write_option_changes_sheet` {#fn-write-option-changes-sheet-7412}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7412`

**Signature**

```python
def write_option_changes_sheet(wb, option_changes_view):
```

**Returns:** `None or implicit return`

**What it does:** Option-level changes for questions present in both files. The 'Field'

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `option_changes_view` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def write_option_changes_sheet(wb, option_changes_view):
        """
        Option-level changes for questions present in both files. The 'Field'
        column shows option_1 / option_2 /  so you know which answer choice is
        affected. The 'Type' column shows the mandatory category of the parent question.
        """
        ws = wb.create_sheet("Option Changes")
        ws.sheet_view.showGridLines = False

        df = option_changes_view
        if "set_name" in df.columns:
            df = df.drop("set_name")

        code_issue_types = {
            "codes_token_mismatch",
            "codes_removed",
            "codes_added",
            "codes_position_drift",
            "added_removed_codes",
            "added_codes_with_drift",
            "removed_codes_with_drift",
            "added_removed_codes_with_drift",
            "codes_option_count_mismatch",
            "codes_not_comparable",
        }
        option_df = df.filter(~pl.col("issue_type").is_in(list(code_issue_types)))
        codes_df = df.filter(pl.col("issue_type").is_in(list(code_issue_types)))

        _section_header(ws, 1, "OPTION CHANGES  Answer options for questions in both files", max(8, len(df.columns)))
        option_table_start = 2
        next_row = _issues_table(ws, option_table_start, option_df, field_label="Detail")
        _apply_inline_diff_for_issue(
            ws,
            option_table_start,
            option_df,
            {
                "option_label_mismatch",
                "option_position_drift",
                "added_option",
                "removed_option",
                "added_removed_option",
                "added_option_with_drift",
                "removed_option_with_drift",
                "added_removed_option_with_drift",
                "removed_option_cascading_drift",
            },
        )
        _apply_option_detail_highlights(ws, option_table_start, option_df)

        next_row += 1
        _section_header(ws, next_row, "CODES COLUMN CHECKS  Number/token consistency in 'Codes'", max(8, len(df.columns)))
        codes_table_start = next_row + 1
        _issues_table(ws, codes_table_start, codes_df, field_label="Detail")
        _apply_inline_diff_for_issue(
            ws,
            codes_table_start,
            codes_df,
            {
                "codes_token_mismatch",
                "codes_position_drift",
                "added_codes_with_drift",
                "removed_codes_with_drift",
                "added_removed_codes_with_drift",
            },
        )
        _apply_codes_alignment_marker_highlights(ws, codes_table_start, codes_df)

        # Keep sheet navigation usable: second table must not move freeze panes down.
        ws.freeze_panes = "A3"
        _cols = [(s, d) for s, d in _issues_col_map() if s in df.columns]
        if _cols:
            _n = len(_cols)
            _hdr = option_table_start if option_df.height > 0 else codes_table_start
            ws.auto_filter.ref = f"A{_hdr}:{get_column_letter(_n)}{_hdr}"
        _autofit(ws)
    ```

### `export_validation_report` {#fn-export-validation-report-7490}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7490`

**Signature**

```python
def export_validation_report(all_issues, question_changes_view, option_changes_view, result_file, rules, found_info=None, replacement_status=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `question_changes_view` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `option_changes_view` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `result_file` | positional_or_keyword | Yes | `-` | `-` | Filesystem path used for reading inputs or writing outputs. |
| `rules` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `found_info` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `replacement_status` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def export_validation_report(all_issues, question_changes_view, option_changes_view, result_file, rules, found_info=None, replacement_status=None):
        wb = Workbook()
        wb.remove(wb.active)
        write_summary_sheet(wb, all_issues, rules, replacement_status=replacement_status)
        write_critical_sets_sheet(wb, all_issues, found_info=found_info)
        write_structure_skip_sheet(wb, all_issues)
        write_replacement_issues_sheet(wb, all_issues)
        write_question_changes_sheet(wb, question_changes_view)
        write_option_changes_sheet(wb, option_changes_view)
        out_path = Path(result_file)
        try:
            wb.save(out_path)
        except PermissionError:
            alt_name = f"{out_path.stem}_{datetime.now().strftime('%H%M%S')}{out_path.suffix}"
            alt_path = out_path.with_name(alt_name)
            wb.save(alt_path)
            out_path = alt_path
            print(f"Warning: target report file was locked. Saved as: {out_path}")
        print(f"Report saved to: {out_path}")
        print(f"Sheets: {wb.sheetnames}")
        return out_path
    ```

### `_resolve_survey_sheet` {#fn--resolve-survey-sheet-7513}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7513`

**Signature**

```python
def _resolve_survey_sheet(workbook):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `workbook` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |

??? note "Function source"

    ```python
    def _resolve_survey_sheet(workbook):
        ws = next((workbook[n] for n in workbook.sheetnames if n.strip().lower() == "survey"), None)
        if ws is None:
            raise KeyError(f"Survey sheet not found. Available sheets: {workbook.sheetnames}")
        return ws
    ```

### `_sheet_header_map` {#fn--sheet-header-map-7520}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7520`

**Signature**

```python
def _sheet_header_map(ws, header_row: int=3) -> dict[str, int]:
```

**Returns:** `dict[str, int]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `header_row` | positional_or_keyword | No | `3` | `int` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _sheet_header_map(ws, header_row: int = 3) -> dict[str, int]:
        mapping = {}
        for col in range(1, ws.max_column + 1):
            value = ws.cell(row=header_row, column=col).value
            if value is None:
                continue
            header = str(value).strip()
            mapping[header] = col
            canonical = _canonical_column_from_header(header)
            if canonical and canonical not in mapping:
                mapping[canonical] = col
        return mapping
    ```

### `_count_selected_crops` {#fn--count-selected-crops-7534}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7534`

**Signature**

```python
def _count_selected_crops(crop_df: pl.DataFrame, language: str) -> tuple[int, int, str]:
```

**Returns:** `tuple[int, int, str]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 10 Export to Excel` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _count_selected_crops(crop_df: pl.DataFrame, language: str) -> tuple[int, int, str]:
        meta = extract_crop_metadata(crop_df, language)
        total_candidates = len(meta.get("labels", []))
        select_col = meta.get("select_col")
        if not select_col or select_col not in crop_df.columns:
            return 0, total_candidates, "missing_select_column"
        selected_values = crop_df.get_column(select_col).to_list()
        selected_count = sum(
            1 for v in selected_values
            if str(v or "").strip() not in {"", "0", "0.0", "none", "nan"}
        )
        return selected_count, total_candidates, "ok"
    ```

### `_placeholder_scan_columns` {#fn--placeholder-scan-columns-7548}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7548`

**Signature**

```python
def _placeholder_scan_columns(questions_df: pl.DataFrame, candidate_columns: Optional[list[str]]=None) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `candidate_columns` | positional_or_keyword | No | `None` | `Optional[list[str]]` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _placeholder_scan_columns(questions_df: pl.DataFrame, candidate_columns: Optional[list[str]] = None) -> list[str]:
        cols = [c for c in (candidate_columns or RESTORE_TEXT_COLUMNS) if c in questions_df.columns]
        if "Codes" in questions_df.columns and "Codes" not in cols:
            cols.append("Codes")
        return cols
    ```

### `_extract_placeholder_tokens` {#fn--extract-placeholder-tokens-7555}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7555`

**Signature**

```python
def _extract_placeholder_tokens(text: str) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _extract_placeholder_tokens(text: str) -> list[str]:
        return re.findall(r"\$[^$\r\n]+\$", str(text or ""))
    ```

### `_has_broken_placeholder_token` {#fn--has-broken-placeholder-token-7559}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7559`

**Signature**

```python
def _has_broken_placeholder_token(text: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _has_broken_placeholder_token(text: str) -> bool:
        txt = str(text or "")
        if "$" not in txt:
            return False
        stripped = re.sub(r"\$[^$\r\n]+\$", "", txt)
        return "$" in stripped
    ```

### `_count_unresolved_placeholders` {#fn--count-unresolved-placeholders-7567}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7567`

**Signature**

```python
def _count_unresolved_placeholders(questions_df: pl.DataFrame, candidate_columns: Optional[list[str]]=None) -> int:
```

**Returns:** `int`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `candidate_columns` | positional_or_keyword | No | `None` | `Optional[list[str]]` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _count_unresolved_placeholders(questions_df: pl.DataFrame, candidate_columns: Optional[list[str]] = None) -> int:
        cols = _placeholder_scan_columns(questions_df, candidate_columns)
        if not cols:
            return 0
        unresolved = 0
        for row in questions_df.select(cols).iter_rows(named=True):
            for col in cols:
                txt = str(row.get(col) or "")
                if _extract_placeholder_tokens(txt):
                    unresolved += 1
        return unresolved
    ```

### `_selected_crop_labels` {#fn--selected-crop-labels-7580}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7580`

**Signature**

```python
def _selected_crop_labels(crop_df: pl.DataFrame, language: str, limit: int=15) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 10 Export to Excel` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `limit` | positional_or_keyword | No | `15` | `int` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _selected_crop_labels(crop_df: pl.DataFrame, language: str, limit: int = 15) -> list[str]:
        meta = extract_crop_metadata(crop_df, language)
        label_col = meta.get("label_col")
        select_col = meta.get("select_col")
        if not label_col or not select_col or label_col not in crop_df.columns or select_col not in crop_df.columns:
            return []
        labels = []
        for row in crop_df.select([label_col, select_col]).iter_rows(named=True):
            sel = str(row.get(select_col) or "").strip().lower()
            if sel not in {"", "0", "0.0", "none", "nan"}:
                lbl = str(row.get(label_col) or "").strip()
                if lbl:
                    labels.append(lbl)
        if len(labels) > limit:
            return labels[:limit] + [f"... (+{len(labels) - limit} more)"]
        return labels
    ```

### `_selected_crop_entries` {#fn--selected-crop-entries-7598}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7598`

**Signature**

```python
def _selected_crop_entries(crop_df: pl.DataFrame, language: str) -> list[dict]:
```

**Returns:** `list[dict]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 10 Export to Excel` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _selected_crop_entries(crop_df: pl.DataFrame, language: str) -> list[dict]:
        if crop_df is None or crop_df.height == 0:
            return []
        meta = extract_crop_metadata(crop_df, language)
        label_col = meta.get("label_col")
        dataset_col = meta.get("dataset_col")
        select_col = meta.get("select_col")
        if not label_col or not select_col or label_col not in crop_df.columns or select_col not in crop_df.columns:
            return []

        cols = [label_col, select_col]
        if dataset_col and dataset_col in crop_df.columns:
            cols.append(dataset_col)

        out = []
        for row in crop_df.select(cols).iter_rows(named=True):
            if not _is_selected_crop_value(row.get(select_col)):
                continue
            label = str(row.get(label_col) or "").strip()
            code = str(row.get(dataset_col) or "").strip() if dataset_col and dataset_col in crop_df.columns else ""
            if not label and not code:
                continue
            key = code.lower() if code else label.lower()
            display = f"{code} - {label}" if code and label else (label or code)
            out.append({"key": key, "display": display})
        return out
    ```

### `_join_short` {#fn--join-short-7626}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7626`

**Signature**

```python
def _join_short(items: list[str], limit: int=12) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `items` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 10 Export to Excel` stage. |
| `limit` | positional_or_keyword | No | `12` | `int` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _join_short(items: list[str], limit: int = 12) -> str:
        if not items:
            return "none"
        if len(items) <= limit:
            return ", ".join(items)
        return ", ".join(items[:limit]) + f", ... (+{len(items) - limit} more)"
    ```

### `_build_crop_round_delta_issue_rows` {#fn--build-crop-round-delta-issue-rows-7634}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7634`

**Signature**

```python
def _build_crop_round_delta_issue_rows(current_crop_df: pl.DataFrame, reference_crop_df: pl.DataFrame, language: str, crop_qnames: Optional[list[str]]=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 10 Export to Excel` stage. |
| `reference_crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 10 Export to Excel` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `crop_qnames` | positional_or_keyword | No | `None` | `Optional[list[str]]` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _build_crop_round_delta_issue_rows(
        current_crop_df: pl.DataFrame,
        reference_crop_df: pl.DataFrame,
        language: str,
        crop_qnames: Optional[list[str]] = None,
    ) -> pl.DataFrame:
        schema = {
            "issue_type": pl.Utf8,
            "set_name": pl.Utf8,
            "Q Name": pl.Utf8,
            "field": pl.Utf8,
            "current": pl.Utf8,
            "reference": pl.Utf8,
            "severity": pl.Utf8,
            "excel_row": pl.Int64,
        }
        if reference_crop_df is None or reference_crop_df.height == 0:
            return pl.DataFrame(schema=schema)

        cur_entries = _selected_crop_entries(current_crop_df, language)
        ref_entries = _selected_crop_entries(reference_crop_df, language)
        if not cur_entries and not ref_entries:
            return pl.DataFrame(schema=schema)

        cur_map = {e["key"]: e["display"] for e in cur_entries}
        ref_map = {e["key"]: e["display"] for e in ref_entries}
        cur_keys = set(cur_map.keys())
        ref_keys = set(ref_map.keys())

        added = sorted(cur_map[k] for k in (cur_keys - ref_keys))
        removed = sorted(ref_map[k] for k in (ref_keys - cur_keys))
        qname_txt = ", ".join(crop_qnames) if crop_qnames else "crop placeholder question(s)"

        row = {
            "issue_type": "replacement_crop_round_delta",
            "set_name": "REPLACEMENT",
            "Q Name": qname_txt,
            "field": "Crop list (selected top 10)",
            "current": (
                f"Current selected ({len(cur_entries)}): {_join_short(sorted(cur_map.values()))} | "
                f"Added vs reference ({len(added)}): {_join_short(added)}"
            ),
            "reference": (
                f"Reference selected ({len(ref_entries)}): {_join_short(sorted(ref_map.values()))} | "
                f"Removed vs reference ({len(removed)}): {_join_short(removed)}"
            ),
            "severity": "info",
            "excel_row": None,
        }
        return pl.DataFrame([row], schema=schema)
    ```

### `_build_replacement_issue_rows` {#fn--build-replacement-issue-rows-7686}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7686`

**Signature**

```python
def _build_replacement_issue_rows(validated_questions: pl.DataFrame, replacements: dict[str, str], crop_df: pl.DataFrame, language: str, reference_questions: pl.DataFrame | None=None, additional_info_diag: dict | None=None, replacements_by_language: dict[str, dict[str, str]] | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `validated_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `replacements` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 10 Export to Excel` stage. |
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 10 Export to Excel` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `reference_questions` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |
| `additional_info_diag` | positional_or_keyword | No | `None` | `dict | None` | Input used by the `Step 10 Export to Excel` stage. |
| `replacements_by_language` | positional_or_keyword | No | `None` | `dict[str, dict[str, str]] | None` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _build_replacement_issue_rows(
        validated_questions: pl.DataFrame,
        replacements: dict[str, str],
        crop_df: pl.DataFrame,
        language: str,
        reference_questions: pl.DataFrame | None = None,
        additional_info_diag: dict | None = None,
        replacements_by_language: dict[str, dict[str, str]] | None = None,
    ) -> pl.DataFrame:
        schema = {
            "issue_type": pl.Utf8,
            "set_name": pl.Utf8,
            "Q Name": pl.Utf8,
            "field": pl.Utf8,
            "current": pl.Utf8,
            "reference": pl.Utf8,
            "severity": pl.Utf8,
            "excel_row": pl.Int64,
        }
        rows = []

        selected_count, total_candidates, crop_mode = _count_selected_crops(crop_df, language)
        if crop_mode == "missing_select_column":
            rows.append({
                "issue_type": "replacement_crop_selection_mismatch",
                "set_name": "REPLACEMENT",
                "Q Name": "",
                "field": "Crop list",
                "current": f"selection column missing ({total_candidates} candidate crops)",
                "reference": "Crop list should mark exactly 10 selected crops",
                "severity": "medium",
                "excel_row": None,
            })
        elif selected_count != 10:
            selected_labels = _selected_crop_labels(crop_df, language)
            rows.append({
                "issue_type": "replacement_crop_selection_mismatch",
                "set_name": "REPLACEMENT",
                "Q Name": "",
                "field": "Crop list",
                "current": f"{selected_count}/10 selected | {', '.join(selected_labels) if selected_labels else 'no selected labels'}",
                "reference": "Expected exactly 10 selected crops for $TEN MOST COMMON CROPS$ / $CROP CODES$ substitution",
                "severity": "medium",
                "excel_row": None,
            })

        if not replacements and not any((replacements_by_language or {}).values()):
            detail = "No replacement keys loaded"
            if additional_info_diag:
                detail = (
                    f"No replacement keys loaded | rows={additional_info_diag.get('rows_with_any_data', 0)} "
                    f"placeholder-style={additional_info_diag.get('rows_with_placeholder_style_original', 0)} "
                    f"plain-style={additional_info_diag.get('rows_with_non_placeholder_original', 0)}"
                )
            rows.append({
                "issue_type": "replacement_additional_info_missing",
                "set_name": "REPLACEMENT",
                "Q Name": "",
                "field": "Additional information",
                "current": detail,
                "reference": "Additional information must define all $...$ placeholders used in survey",
                "severity": "high",
                "excel_row": None,
            })

        def _effective_replacements_for_col(col_name: str) -> dict[str, str]:
            lang = _language_code_for_text_column(col_name)
            if replacements_by_language and lang and replacements_by_language.get(lang):
                return replacements_by_language[lang]
            return replacements or {}

        seen = set()
        missing_key_locs = set()

        if reference_questions is not None and reference_questions.height > 0:
            ref_cols = _placeholder_scan_columns(reference_questions)
            for row in reference_questions.select(["Q Name", "excel_row"] + ref_cols).iter_rows(named=True):
                qname = str(row.get("Q Name") or "")
                excel_row = row.get("excel_row")
                for col in ref_cols:
                    txt = str(row.get(col) or "")
                    if not txt:
                        continue
                    col_repl = _effective_replacements_for_col(col)
                    col_idx = _build_placeholder_index(col_repl)
                    for token in _extract_placeholder_tokens(txt):
                        if _is_crop_placeholder_token(token):
                            continue
                        if _lookup_placeholder_replacement(token, col_repl, col_idx) is not None:
                            continue
                        tok_norm = _normalize_placeholder_token(token)
                        key = ("replacement_missing_key", qname, col, token)
                        if key in seen:
                            continue
                        seen.add(key)
                        missing_key_locs.add((qname, col, tok_norm))
                        sev = "high"
                        rows.append({
                            "issue_type": "replacement_missing_key",
                            "set_name": "REPLACEMENT",
                            "Q Name": qname,
                            "field": col,
                            "current": token,
                            "reference": "Placeholder key missing/blank in Additional information",
                            "severity": sev,
                            "excel_row": excel_row,
                        })

        cols = _placeholder_scan_columns(validated_questions)
        for row in validated_questions.select(["Q Name", "excel_row"] + cols).iter_rows(named=True):
            qname = str(row.get("Q Name") or "")
            excel_row = row.get("excel_row")
            for col in cols:
                txt = str(row.get(col) or "")
                if not txt:
                    continue

                if _has_broken_placeholder_token(txt):
                    key = ("replacement_malformed_placeholder", qname, col, txt)
                    if key not in seen:
                        seen.add(key)
                        rows.append({
                            "issue_type": "replacement_malformed_placeholder",
                            "set_name": "REPLACEMENT",
                            "Q Name": qname,
                            "field": col,
                            "current": txt,
                            "reference": "Placeholder token should be balanced and closed (example: $season$)",
                            "severity": "medium",
                            "excel_row": excel_row,
                        })

                col_repl = _effective_replacements_for_col(col)
                col_idx = _build_placeholder_index(col_repl)
                for token in _extract_placeholder_tokens(txt):
                    tok_norm = _normalize_placeholder_token(token)
                    if _is_crop_placeholder_token(token):
                        issue_type = "replacement_unresolved_placeholder"
                        severity = "high"
                        reference = "Crop placeholders must be fully expanded in validated output"
                    elif _lookup_placeholder_replacement(token, col_repl, col_idx) is None:
                        issue_type = "replacement_missing_key"
                        severity = "high"
                        reference = "Placeholder key missing from Additional information"
                        missing_key_locs.add((qname, col, tok_norm))
                    else:
                        if (qname, col, tok_norm) in missing_key_locs:
                            continue
                        issue_type = "replacement_unresolved_placeholder"
                        severity = "medium"
                        reference = "Placeholder replacement exists but token remained unresolved"

                    key = (issue_type, qname, col, token)
                    if key in seen:
                        continue
                    seen.add(key)
                    rows.append({
                        "issue_type": issue_type,
                        "set_name": "REPLACEMENT",
                        "Q Name": qname,
                        "field": col,
                        "current": token,
                        "reference": reference,
                        "severity": severity,
                        "excel_row": excel_row,
                    })

        if not rows:
            return pl.DataFrame(schema=schema)
        return pl.DataFrame(rows, schema=schema)
    ```

### `_build_replacement_issue_rows._effective_replacements_for_col` {#fn--effective-replacements-for-col-7751}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7751`

**Signature**

```python
def _effective_replacements_for_col(col_name: str) -> dict[str, str]:
```

**Returns:** `dict[str, str]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _effective_replacements_for_col(col_name: str) -> dict[str, str]:
            lang = _language_code_for_text_column(col_name)
            if replacements_by_language and lang and replacements_by_language.get(lang):
                return replacements_by_language[lang]
            return replacements or {}
    ```

### `_fetch_admin_reference` {#fn--fetch-admin-reference-7858}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7858`

**Signature**

```python
def _fetch_admin_reference(admin_level: str, iso3: str) -> tuple[list[dict], str]:
```

**Returns:** `tuple[list[dict], str]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `admin_level` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |
| `iso3` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _fetch_admin_reference(admin_level: str, iso3: str) -> tuple[list[dict], str]:
        import urllib.request
        import json

        iso3 = str(iso3 or "").upper().strip()
        if not iso3:
            return [], "missing_iso3"

        urls = {
            "Admin 1": "https://services5.arcgis.com/sjP4Ugu5s0dZWLjd/arcgis/rest/services/Administrative_Boundaries_Reference_(view_layer)/FeatureServer/1/query?where=adm0_ISO3%20%3D%20'{iso3}'&outFields=adm1_name,adm1_name_local,adm1_pcode,adm0_name,adm0_ISO3&returnGeometry=false&outSR=4326&f=json",
            "Admin 2": "https://services5.arcgis.com/sjP4Ugu5s0dZWLjd/arcgis/rest/services/Administrative_Boundaries_Reference_(view_layer)/FeatureServer/0/query?where=adm0_ISO3%20%3D%20'{iso3}'&outFields=adm2_name,adm2_name_local,adm2_pcode,adm1_name,adm1_pcode,adm0_name,adm0_ISO3&returnGeometry=false&outSR=4326&f=json",
        }
        rename = {
            "Admin 1": {
                "adm1_name": "adm1_name",
                "adm1_name_local": "adm1_name_local",
                "adm1_pcode": "adm1_pcode",
                "adm0_name": "adm0_name",
                "adm0_ISO3": "adm0_ISO3",
            },
            "Admin 2": {
                "adm2_name": "adm2_name",
                "adm2_name_local": "adm2_name_local",
                "adm2_pcode": "adm2_pcode",
                "adm1_name": "adm1_name",
                "adm1_pcode": "adm1_pcode",
                "adm0_name": "adm0_name",
                "adm0_ISO3": "adm0_ISO3",
            },
        }

        if admin_level not in urls:
            return [], f"unsupported_admin_level:{admin_level}"

        url = urls[admin_level].format(iso3=iso3)
        try:
            with urllib.request.urlopen(url, timeout=25) as resp:
                data = json.loads(resp.read().decode())
        except Exception as e:
            return [], str(e)

        features = data.get("features", []) or []
        mapping = rename[admin_level]
        rows = []
        for feat in features:
            attrs = feat.get("attributes", {}) or {}
            rows.append({dst: attrs.get(src) for src, dst in mapping.items()})
        return rows, ""
    ```

### `_write_table_sheet` {#fn--write-table-sheet-7908}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7908`

**Signature**

```python
def _write_table_sheet(ws, rows: list[dict]):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `rows` | positional_or_keyword | Yes | `-` | `list[dict]` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _write_table_sheet(ws, rows: list[dict]):
        if not rows:
            ws.cell(row=1, column=1, value="No rows")
            return 0
        headers = list(rows[0].keys())
        for c, h in enumerate(headers, 1):
            ws.cell(row=1, column=c, value=h)
        r = 2
        for rd in rows:
            for c, h in enumerate(headers, 1):
                ws.cell(row=r, column=c, value=rd.get(h))
            r += 1
        return len(rows)
    ```

### `_apply_admin_sheets` {#fn--apply-admin-sheets-7923}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7923`

**Signature**

```python
def _apply_admin_sheets(output_questionnaire_path: Path, iso3: str) -> dict:
```

**Returns:** `dict`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `output_questionnaire_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `iso3` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _apply_admin_sheets(output_questionnaire_path: Path, iso3: str) -> dict:
        rows = []
        fetched = {}
        errors = {}
        for lvl in ["Admin 1", "Admin 2"]:
            data_rows, err = _fetch_admin_reference(lvl, iso3)
            if err:
                errors[lvl] = err
            else:
                fetched[lvl] = data_rows

        if fetched:
            details = ", ".join([
                f"admin1={len(fetched.get('Admin 1', []))}",
                f"admin2={len(fetched.get('Admin 2', []))}",
            ])
            rows.append({"check": "AGOL fetch", "status": "PASS" if not errors else "WARN", "details": details, "severity": "info" if not errors else "medium"})
        else:
            err_txt = "; ".join(f"{k}: {v}" for k, v in errors.items()) or "AGOL returned no data"
            rows.append({"check": "AGOL fetch", "status": "FAIL", "details": err_txt, "severity": "high"})
            return {"rows": rows}

        try:
            wb = openpyxl.load_workbook(output_questionnaire_path)
            for lvl, data_rows in fetched.items():
                sheet_name = f"{lvl} info"
                if sheet_name in wb.sheetnames:
                    del wb[sheet_name]
                ws = wb.create_sheet(sheet_name)
                n = _write_table_sheet(ws, data_rows)
                rows.append({
                    "check": f"Admin sheet added: {lvl.lower().replace(' ', '')}",
                    "status": "PASS",
                    "details": f"{n} rows written",
                    "severity": "info",
                })
            wb.save(output_questionnaire_path)
        except Exception as e:
            rows.append({"check": "Admin sheet write", "status": "FAIL", "details": str(e), "severity": "high"})

        return {"rows": rows}
    ```

### `_build_replacement_status_rows` {#fn--build-replacement-status-rows-7966}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:7966`

**Signature**

```python
def _build_replacement_status_rows(validated_questions: pl.DataFrame, crop_df: pl.DataFrame, replacements: dict[str, str], language: str, iso3: str, output_questionnaire_path: Optional[Path], write_status: dict, additional_info_diag: dict | None=None, replacement_issues: pl.DataFrame | None=None) -> dict:
```

**Returns:** `dict`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `validated_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 10 Export to Excel` stage. |
| `replacements` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 10 Export to Excel` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `iso3` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |
| `output_questionnaire_path` | positional_or_keyword | Yes | `-` | `Optional[Path]` | Filesystem path used for reading inputs or writing outputs. |
| `write_status` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 10 Export to Excel` stage. |
| `additional_info_diag` | positional_or_keyword | No | `None` | `dict | None` | Input used by the `Step 10 Export to Excel` stage. |
| `replacement_issues` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _build_replacement_status_rows(
        validated_questions: pl.DataFrame,
        crop_df: pl.DataFrame,
        replacements: dict[str, str],
        language: str,
        iso3: str,
        output_questionnaire_path: Optional[Path],
        write_status: dict,
        additional_info_diag: dict | None = None,
        replacement_issues: pl.DataFrame | None = None,
    ) -> dict:
        rows = []

        selected_count, total_candidates, crop_mode = _count_selected_crops(crop_df, language)
        if crop_mode == "missing_select_column":
            rows.append({
                "check": "Crop selection (top 10)",
                "status": "WARN",
                "details": f"selection column not found; {total_candidates} candidates detected",
                "severity": "medium",
            })
        else:
            crop_status = "PASS" if selected_count == 10 else "WARN"
            crop_sev = "info" if crop_status == "PASS" else "medium"
            rows.append({
                "check": "Crop selection (top 10)",
                "status": crop_status,
                "details": f"{selected_count}/10 selected ({total_candidates} candidates)",
                "severity": crop_sev,
            })

        repl_df = replacement_issues if replacement_issues is not None else pl.DataFrame(schema={"issue_type": pl.Utf8, "severity": pl.Utf8})
        miss_high = repl_df.filter((pl.col("issue_type") == "replacement_missing_key") & (pl.col("severity") == "high")).height if repl_df.height > 0 else 0
        miss_med = repl_df.filter((pl.col("issue_type") == "replacement_missing_key") & (pl.col("severity") == "medium")).height if repl_df.height > 0 else 0
        unresolved_high = repl_df.filter((pl.col("issue_type") == "replacement_unresolved_placeholder") & (pl.col("severity") == "high")).height if repl_df.height > 0 else 0
        unresolved_med = repl_df.filter((pl.col("issue_type") == "replacement_unresolved_placeholder") & (pl.col("severity") == "medium")).height if repl_df.height > 0 else 0
        malformed_n = repl_df.filter(pl.col("issue_type") == "replacement_malformed_placeholder").height if repl_df.height > 0 else 0

        key_load_ok = bool(replacements)
        key_load_details = f"{len(replacements)} placeholder key(s) loaded from Additional information"
        if not key_load_ok:
            if additional_info_diag:
                key_load_details = (
                    f"No replacement keys loaded | rows={additional_info_diag.get('rows_with_any_data', 0)} "
                    f"placeholder-style={additional_info_diag.get('rows_with_placeholder_style_original', 0)} "
                    f"plain-style={additional_info_diag.get('rows_with_non_placeholder_original', 0)}"
                )
            else:
                key_load_details = "No replacement keys loaded from Additional information"

        fail_parts = []
        if miss_high > 0:
            fail_parts.append(f"missing keys (high)={miss_high}")
        if unresolved_high > 0:
            fail_parts.append(f"unresolved placeholders (high)={unresolved_high}")

        warn_parts = []
        if miss_med > 0:
            warn_parts.append(f"missing keys (medium)={miss_med}")
        if unresolved_med > 0:
            warn_parts.append(f"unresolved placeholders (medium)={unresolved_med}")
        if malformed_n > 0:
            warn_parts.append(f"malformed placeholders={malformed_n}")

        check_statuses = []
        check_statuses.append("PASS" if key_load_ok else "FAIL")
        check_statuses.append("FAIL" if fail_parts else "PASS")
        check_statuses.append("WARN" if warn_parts else "PASS")

        fail_n = sum(1 for s in check_statuses if s == "FAIL")
        warn_n = sum(1 for s in check_statuses if s == "WARN")
        pass_n = sum(1 for s in check_statuses if s == "PASS")

        if fail_n > 0:
            summary_status = "FAIL"
            summary_sev = "high"
        elif warn_n > 0:
            summary_status = "WARN"
            summary_sev = "medium"
        else:
            summary_status = "PASS"
            summary_sev = "info"

        detail_parts = [f"{summary_status} (pass={pass_n}, warn={warn_n}, fail={fail_n})", key_load_details]
        if fail_parts:
            detail_parts.append("; ".join(fail_parts))
        if warn_parts:
            detail_parts.append("; ".join(warn_parts))

        rows.append({
            "check": "Additional info replacement",
            "status": summary_status,
            "details": " | ".join([p for p in detail_parts if p]),
            "severity": summary_sev,
        })

        if write_status.get("status") == "OK" and output_questionnaire_path is not None:
            rows.extend(_apply_admin_sheets(output_questionnaire_path, iso3).get("rows", []))
        else:
            rows.append({
                "check": "AGOL fetch",
                "status": "WARN",
                "details": "Skipped because validated questionnaire could not be written",
                "severity": "medium",
            })

        return {"rows": rows}
    ```

### `write_validated_questionnaire` {#fn-write-validated-questionnaire-8075}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `C:/git/DIEM_NewQuestionnaire_VALIDATION/scripts/geopoll_validator.py:8075`

**Signature**

```python
def write_validated_questionnaire(source_questionnaire_path: Path, output_questionnaire_path: Path, questions_df: pl.DataFrame, skip_module_keys: Optional[set[str]]=None, skip_qnames: Optional[set[str]]=None) -> dict:
```

**Returns:** `dict`

**What it does:** Creates a validated questionnaire workbook by copying the original file and

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `source_questionnaire_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `output_questionnaire_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `skip_module_keys` | positional_or_keyword | No | `None` | `Optional[set[str]]` | Input used by the `Step 10 Export to Excel` stage. |
| `skip_qnames` | positional_or_keyword | No | `None` | `Optional[set[str]]` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def write_validated_questionnaire(
        source_questionnaire_path: Path,
        output_questionnaire_path: Path,
        questions_df: pl.DataFrame,
        skip_module_keys: Optional[set[str]] = None,
        skip_qnames: Optional[set[str]] = None,
    ) -> dict:
        """
        Creates a validated questionnaire workbook by copying the original file and
        writing the converted survey values row-by-row using Q Name as key.
        Optionally removes skipped module blocks from the survey sheet.
        """
        copyfile(source_questionnaire_path, output_questionnaire_path)

        wb = openpyxl.load_workbook(output_questionnaire_path)
        ws = _resolve_survey_sheet(wb)
        header_map = _sheet_header_map(ws, header_row=2)

        q_col = header_map.get("Q Name")
        if not q_col:
            raise KeyError("Column 'Q Name' not found in survey header row.")

        qname_to_row = {}
        for row_idx in range(3, ws.max_row + 1):
            qname = ws.cell(row=row_idx, column=q_col).value
            key = str(qname).strip() if qname is not None else ""
            if key:
                qname_to_row[key] = row_idx

        writable_cols = [
            col for col in questions_df.columns
            if col not in {"Q Name", "excel_row", "source_file"} and col in header_map
        ]

        for row in questions_df.select(["Q Name"] + writable_cols).to_dicts():
            qname = str(row.get("Q Name") or "").strip()
            target_row = qname_to_row.get(qname)
            if not target_row:
                continue
            for col_name in writable_cols:
                cell = ws.cell(row=target_row, column=header_map[col_name])
                if not isinstance(cell, openpyxl.cell.cell.MergedCell):
                    cell.value = row.get(col_name)

        _skip_keys_norm = {
            _normalize_module_token(v)
            for v in (skip_module_keys or set())
            if _normalize_module_token(v)
        }
        _skip_q = {str(v).strip() for v in (skip_qnames or set()) if str(v or "").strip()}
        _module_skip_stats = {
            "removed_rows": 0,
            "removed_question_rows": 0,
            "removed_module_rows": 0,
            "removed_module_blocks": 0,
        }

        if _skip_keys_norm or _skip_q:
            rows_to_delete: list[int] = []
            module_col = header_map.get("module")

            # Each question row carries its own module code. Divider rows (blank
            # module cell) belong visually to the module that follows them, so
            # backfill blanks from the next populated row (look-ahead).
            row_module: dict[int, str] = {}
            for row_idx in range(3, ws.max_row + 1):
                module_val = str(ws.cell(row=row_idx, column=module_col).value or "").strip() if module_col else ""
                row_module[row_idx] = module_val

            next_code = ""
            for row_idx in range(ws.max_row, 2, -1):
                if row_module[row_idx]:
                    next_code = row_module[row_idx]
                else:
                    row_module[row_idx] = next_code

            for row_idx in range(3, ws.max_row + 1):
                q_name_val = ws.cell(row=row_idx, column=q_col).value
                q_name = str(q_name_val or "").strip()
                is_divider_row = module_col and not str(ws.cell(row=row_idx, column=module_col).value or "").strip() and q_name
                key_norm = _normalize_module_token(row_module.get(row_idx, ""))
                module_skip = key_norm in _skip_keys_norm if key_norm else False

                remove_here = module_skip or (q_name in _skip_q if q_name else False)
                if remove_here:
                    rows_to_delete.append(row_idx)
                    _module_skip_stats["removed_rows"] += 1
                    if is_divider_row:
                        _module_skip_stats["removed_module_rows"] += 1
                        if module_skip:
                            _module_skip_stats["removed_module_blocks"] += 1
                    else:
                        _module_skip_stats["removed_question_rows"] += 1

            for row_idx in sorted(set(rows_to_delete), reverse=True):
                ws.delete_rows(row_idx, 1)

        wb.save(output_questionnaire_path)
        print(f"Validated questionnaire saved to: {output_questionnaire_path}")
        return {"status": "OK", "path": str(output_questionnaire_path), "module_skip": _module_skip_stats}
    ```
