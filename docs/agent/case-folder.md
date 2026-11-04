# Case folder and outputs

All results are published in the **DIEM questionnaire validation folder in
Temp** (`output_dir` in `configuration/validation_config.yaml`), split by
tool:

```
C:\Temp\DIEM_questionnaire_validation\
  geopoll_output\                     reports and validated questionnaires (GeoPoll)
    validation_cases\<ISO3>_<round>\  one folder per GeoPoll case
  kobo_output\                        reports and validated questionnaires (KoBo)
    validation_cases\<ISO3>_<round>\  one folder per KoBo case
  configuration\                      configuration snapshot of each run
  archive\<YYYY-MM>\                  older files moved out by housekeeping
  admin_tools_output\                 admin tools results
  _agent_runs\                        agent scratch files (deleted after 7 days)
```

Each validation is a **case**: one country, one tool (KoBo or GeoPoll), one
round, with its own folder, e.g.
`C:\Temp\DIEM_questionnaire_validation\geopoll_output\validation_cases\YEM_R1\`.

## Housekeeping and archiving

Housekeeping runs automatically before every validation (`housekeeping:` in
`validation_config.yaml`):

- **Reports and validated questionnaires**: the last 3 per tool, country,
  language and round stay in `geopoll_output` / `kobo_output`; older ones move
  to `archive\<YYYY-MM>\`. Files with a time suffix (saved while an older one
  was open in Excel) are handled the same way.
- **Archive**: files in `archive\` are deleted after 180 days.
- **Configuration snapshots**: the last 30 per group are kept.
- **Agent scratch files** (`_agent_runs\`: copies of the questionnaire made
  for a run, temporary configuration profiles, run logs): deleted after 7 days.
- **Case folders** (`validation_cases\`) are the record of each validation:
  housekeeping **never** archives or deletes them.

A file can be protected from housekeeping by creating an empty
`<filename>.keep` next to it.

## What the folder contains

| File | Made | Content |
|---|---|---|
| `case.json` | at the start, updated every round | inputs, validation rounds, points and their status |
| `iter<N>_output_check.md` | each round | checks on the validated questionnaire |
| `<ISO3>_<round>_<tool>_points_to_review_v<N>.docx` | each round | the Word document for the country team (open points only) |
| `<ISO3>_<round>_<tool>_validated_questionnaire_FINAL.xlsx` | at closing | the questionnaire to send to GeoPoll / deploy in KoBo |
| `<ISO3>_<round>_<tool>_final_validation_report.docx` | at closing | the final report |
| `final_report_spec.json` | at closing | the content of the final report, to adjust and rebuild |

The Excel **report** and the **validated questionnaire** of each run are in
`geopoll_output\` or `kobo_output\`, named
`report_<tool>_<lang>_<ISO3>_<date>.xlsx` and
`validated_questionnaire_<tool>_<lang>_<ISO3>_<date>.xlsx`. If an older one
is open in Excel, the new one gets a time suffix (`…_20261021_172244.xlsx`);
the agent always uses the file of the current run.

## Points and their status

Every item sent to the country (or to SMAR) is a **point** with an id
(`P01`, `P02`…) that stays the same across rounds, so you can refer to it in
emails and in requests to the agent.

| Status | Meaning | Set by |
|---|---|---|
| open | to be solved | agent, when the point is raised |
| fixed | no longer found in a later version | agent, after checking the new file |
| accepted | kept on purpose; the final report lists it as an agreed exception with who agreed it | you |
| dropped | not a real problem, or withdrawn | you |

| Type | Meaning |
|---|---|
| To fix | a difference from the template that must change |
| To confirm | a difference that may be intended: the country confirms or copies the template |
| Placeholder | a value the country must type in Additional information |
| Optional | cleanup with no effect on the data |
| Template side | a problem in the template itself, for SMAR; nothing for the country |

## Country history

The case files are also the **history of each country**. When a new round
starts, the agent reads every earlier case of that country (both tools) and
gets each earlier point **once**, with its final outcome and how it was
solved, for example:

```
R12 geopoll P01 [To fix] Food security — At least 4 agriculture-related coping strategies
    → fixed: country added back cs_stress_sold_more_animals with the template Conditional
R12 geopoll P02 [To confirm] Food security — cs_emergency_hh_migration renamed c_
    → accepted by Amira (SMAR): wording widened to in/out of country
```

Nothing is copied: the history is read from the case files when needed.
When an issue comes back, the agent says so in one short line, for example
*(also R12: fixed by adding back the template Conditional)*. For an
exception agreed last time it asks you whether it still holds this round;
it does not close it by itself. The Excel report and the Word document stay
as they are, without history sections.

So that the history is useful, close points with a short note that says
**how** the point was solved or **what** was agreed.

## The final report

Built from the case when no point is open:

- validation rounds (file, date, number of issues);
- questions by type in the questionnaire and in the reference: mandatory,
  optional recommended, optional low priority, customized, spiels;
- questions added and removed, grouped by type;
- admin levels and number of units (from AGOL in the validated
  questionnaire);
- selected crops;
- interview length (mandatory + recommended, and total);
- changes made during the validation, with the round each was raised and
  fixed;
- accepted exceptions, with who agreed them;
- template issues reported to SMAR.

## When something goes wrong

| Message or symptom | What it means | What to do |
|---|---|---|
| Template sync WARNING | the Toolbox folder could not be reached (OneDrive offline) | the run used the templates already copied; the agent tells you if they are older than the Toolbox. Sync OneDrive and run again |
| A file has a time suffix | the previous file of the same name is open in Excel | close it; nothing else to do |
| "points still open" at closing | some points are neither fixed nor closed | answer for each: fixed in a new version, accepted (who), or dropped |
| Permission denied on a SharePoint file | OneDrive placeholder file | the agent copies it instead of opening it; nothing to do |
| Dozens of unexpected issues | wrong reference or wrong languages | check the reference line of the summary; ask the agent to re-run with the right template or language list |
