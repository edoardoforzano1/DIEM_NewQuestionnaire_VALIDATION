# DIEM Questionnaire Validation

Internal documentation for the GeoPoll and KoBo questionnaire validation workflows.

## What this system does

Validates a questionnaire file against a reference (official template or previous round) and produces a structured Excel report. Every detected difference is classified by issue type and severity — HIGH blocks round launch, MEDIUM needs review, INFO is tracked for traceability. It also produces the **validated questionnaire**: placeholders replaced from the Additional information sheet, crop lists expanded and sorted, admin lists refreshed from AGOL.

## How to get started

**Operators — with the agent (recommended).** Open Claude Code in the
repository folder and ask, for example:

> Validate `C:\…\diem_household_questionnaire_geopoll_yemen_20261022.xlsx`, GeoPoll, latest template, Arabic. Yemen R1.

The agent runs the standard procedure: validation, a summary, a Word document
and an email for the country team, re-validation of each new version, and
the final validated questionnaire with its final report. Start with
[Working with the agent](agent/index.md).

**Manual route.**

1. Set up the environment: [Getting Started](getting-started.md).
2. Edit `configuration/validation_config.yaml` to point to your questionnaire file.
3. Run `validate` from the repository root.
4. Open the report in `<output_dir>/geopoll_output/` or `<output_dir>/kobo_output/`.

Documentation: run `.\documentation` from the repo root to open this site at
`http://127.0.0.1:8000/`, or ask the agent to open it.

## Documentation map

| Section | What it covers |
|---|---|
| [Working with the Agent](agent/index.md) | How operators run validations through the agent: standard procedure, example requests, case folder, final package |
| [Getting Started](getting-started.md) | Environment setup, configuration keys, manual run |
| [Process Overview](workflow/process-overview.md) | Full pipeline diagram — inputs, steps, outputs |
| [Reference Modes](workflow/reference-modes.md) | When to use `latest_template` vs `previous_round` |
| [Severity Reference](workflow/checks-and-severity.md) | Severity levels, dynamic severity logic, issue index by sheet |
| [GeoPoll Logic](workflow/geopoll-logic.md) | All GeoPoll sheets with issue cards and report screenshots |
| [KoBo Logic](workflow/kobo-logic.md) | All KoBo sheets with issue cards and report screenshots |
| [Template and Previous Round](data-sources/template-and-previous-round.md) | Where templates come from (DIEM Toolbox sync) and how the reference is chosen |
| [Admin Tools](tools/admin-tools.md) | Standalone tools for checking and updating admin boundary lists against AGOL |
