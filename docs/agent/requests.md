# Example requests

Plain language works. These examples show what the agent needs and what it
does with each request.

## Starting a validation

> Validate `C:\Users\…\Downloads\diem_household_questionnaire_geopoll_yemen_20261022.xlsx`, GeoPoll, latest template, Arabic. Yemen R1.

Everything the agent needs is there: file, tool, reference, languages
besides English, country and round. With less, it asks:

> Validate the Niger questionnaire in my Downloads.

The agent replies with what it found in the file (tool, languages filled,
proposed country and round) and asks only what is still open, in one
message.

Previous round instead of the template:

> Validate `…\diem_kobo_niger_R13.xlsx` against the previous round `…\validated_questionnaire_kobo_fr_NER_R12.xlsx`, French. Niger R13.

## After the first round

> New version of Yemen R1: `C:\…\diem_household_questionnaire_geopoll_yemen_20261023.xlsx`

The agent finds the case, re-validates with the same settings, and tells you
what was fixed, what is still open and what is new.

> What is still pending for Yemen?

It lists the open points of the case without running anything.

## History of a country

> What happened in the last Niger validation?

> Was the coping-strategies issue already there in Yemen R12? How was it solved?

The agent answers from the earlier case folders: each point once, with its
final outcome and the note on how it was solved.

## Decisions taken outside the file

> P04 is accepted: SMAR (Amira, email 22 Oct) said 3 agriculture coping strategies are fine for Yemen.

> Drop P07, the country does not do fishing.

> The country confirmed the airtime sentence was removed on purpose.

Always say **who** decided: it goes in the final report.

## Documents and emails

> Redo the Word document without the admin point.

> Draft the cover email in French.

> Give me only the list of template issues for SMAR, plain text.

## Closing

> Everything is solved, prepare the final version.

If points are still open, the agent lists them and asks how to close them.
Otherwise it builds the final validated questionnaire, the final report and
the final email.

## Understanding the results

> What does `option_position_drift` mean?

> Why is `module_removed` only info for migration?

> Explain the Critical Sets sheet of the last report.

## Documentation

> Open the documentation.

> Where is the template sync explained?

> Show me the page on the Replacement Issues sheet.

## Other forms and tools

> Check this KII form, there is no template for it.

The agent runs structural checks instead of the template comparison (see the
skill's "Forms without a template").

> Check the admin lists of the validated Yemen questionnaire against AGOL.

Runs `tool_admin_check`.

## Things the agent will not do on its own

- Edit or re-save files in SharePoint/OneDrive.
- Send emails or documents.
- Change the validator code or the tracked configuration without your OK.
- Close a point because the country *says* it is fixed: it re-validates.
