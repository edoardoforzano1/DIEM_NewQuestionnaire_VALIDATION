# FAQ

## Do I need to edit validator scripts each round?

No. Round-level setup should be done in `configuration/validation_config.yaml` and optional config profiles.

## Can I keep this docs site private?

For GitHub Free Pages hosting, repository visibility and plan constraints apply. For internal use without hosting, run docs locally with `mkdocs serve` or share the built `site/` folder.

## Can I keep README minimal and still have full details?

Yes. Keep README as operational quick start and maintain detailed explanations in this documentation site.

## Can this documentation be used offline?

Yes. Build with `mkdocs build` and open `site/index.html`, or ship the `site/` folder as a zip.

## Do I need to know Python or edit the configuration to validate a questionnaire?

No. Ask the agent in plain language (see [Working with the agent](agent/index.md)). It sets the configuration for each run through a temporary profile and restores `validation_config.yaml` afterwards.

## The agent says a point is still open but SMAR already agreed it. What do I do?

Tell the agent, with who decided: *"P04 is accepted, SMAR (email 22 Oct) agreed"*. The point is closed as accepted and listed in the final report as an agreed exception.

## Where are the files of a validation?

In `C:\Temp\DIEM_questionnaire_validation\`, split by tool: reports and validated questionnaires in `geopoll_output\` or `kobo_output\`, and one folder per country and round in `<tool>_outputalidation_cases\<ISO3>_<round>\`. Older reports are archived automatically; case folders are never deleted. See [Case folder and outputs](agent/case-folder.md).

## Which template was used?

The newest one in `Template/`, refreshed from the DIEM Toolbox before every run. The Summary sheet of the report names it ("Checked against"). See [Template and Previous Round](data-sources/template-and-previous-round.md).
