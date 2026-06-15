# Process Overview

Use this page as the main map of the validation pipeline — inputs, steps, and outputs.

## End-to-End Pipeline

```mermaid
flowchart TD
    subgraph inputs ["Inputs"]
        A["<b>validation_config.yaml</b><br/>tool · mode · files · language"]
        B["<b>critical_sets.yaml</b><br/>structural rules"]
        C["<b>Questionnaire file</b><br/>current .xlsx to validate"]
        D["<b>Reference file</b><br/>template OR previous round"]
    end

    subgraph entry ["validate.py — Entrypoint"]
        E["Resolve tool + config profile<br/>Run output housekeeping<br/>Dispatch validator"]
    end

    subgraph pipeline ["Validation Pipeline"]
        F["1 · Load config + optional profile overlay"]
        G["2 · Resolve reference file<br/><i>latest_template</i> or <i>previous_round</i>"]
        H["3 · Read questionnaire<br/>survey structure · options/choices · codes"]
        I["4 · Normalize<br/>text · logic · placeholders · options"]
        J["5 · Run checks<br/>critical sets · structure · changes · replacements"]
        K["6 · Build issue records<br/>HIGH · MEDIUM · INFO · PASS"]
        L["7 · Export Excel report<br/>Summary + detail sheets"]
    end

    subgraph outputs ["Outputs"]
        M["<b>Validation report</b><br/>report_&lt;tool&gt;_&lt;lang&gt;_&lt;iso3&gt;_&lt;date&gt;.xlsx"]
        N["<b>Validated questionnaire</b><br/>KoBo and GeoPoll deployment copy"]
    end

    A --> E
    C --> H
    D --> G
    B --> J
    E --> F
    F --> G --> H --> I --> J --> K --> L
    L --> M
    L --> N
```

---

## Shared Pipeline Steps

Both GeoPoll and KoBo validators follow the same 7-step macro flow.

**Step 1 — Load config**
: Reads `validation_config.yaml`. If `config_profile` is set, merges the profile overlay on top. Before dispatch, `validate.py` also runs configured output housekeeping and reports the number of kept, archived, deleted, or planned files.

**Step 2 — Resolve reference file**
: Determines the baseline questionnaire for comparison. Mode `latest_template` uses the newest matching file in `templates_dir`; mode `previous_round` uses `previous_round_file` under `working_dir`. See [Reference Modes](reference-modes.md).

**Step 3 — Read questionnaire**
: Parses the current questionnaire Excel file. GeoPoll reads survey rows with language-aware column resolution and extracts numbered options and code tokens. KoBo reads `survey` and `choices` sheets.

**Step 4 — Normalize**
: Normalization is critical to avoid false positives from harmless formatting differences.

- **Text normalization**: trims, lowercases, and standardizes comparison text.
- **Logic normalization**: canonicalizes skip/relevant expressions where possible.
- **Placeholder normalization**: resolves template markers using Additional Information sheet replacements.
- **Option normalization**: aligns option structures before diffing labels and presence.

**Step 5 — Run checks**
: Executes all configured rule families. Results from `critical_sets.yaml` rules are applied here alongside code-level structure and comparison checks.

**Step 6 — Build issue records**
: Converts raw diffs and rule failures into standardized issue rows. Each row gets an `issue_type`, a `severity` (HIGH / MEDIUM / INFO / PASS), metadata columns, and an action recommendation.

**Step 7 — Export report**
: Writes the Excel workbook and a validated questionnaire output. The Summary sheet aggregates by severity and check group, while detail sheets carry the full issue rows.

---

## Tool-Specific Additions

=== "GeoPoll"

    - Language-aware column resolution (EN / FR / AR / ES / PT).
    - Option extraction from numbered text (`1) Label` format) and code-token parsing.
    - Skip-pattern consistency and option-code reference validation.
    - Crop/harvest structural completeness rule.
    - Report sheets: **Summary · Critical Sets · Questionnaire Structure · Replacement Issues · Question Changes · Option Changes**.

=== "KoBo"

    - `survey` and `choices` sheet parsing (XLSForm format).
    - `relevant` expression reference validation and modification tracking.
    - `${variable}` syntax and missing-reference checks.
    - Duplicate question and choice-name detection.
    - Report sheets: **Summary · Critical Sets · Questionnaire Structure · Replacement Issues · Question Changes · Choice Changes**.
    - Produces a validated questionnaire with crop/admin rebuilding and placeholder status checks.
    - Optional admin3 rebuilding is controlled by `kobo_options.include_admin3`.
    - Strict replacement input checks are controlled by `require_additional_info` and `require_crop_list`.
