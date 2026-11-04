# Working with the agent

The validation can be run by talking to **Claude Code**, an AI agent that
works inside this repository. You describe what you need in plain language;
the agent runs the validator, reads the report, checks the validated
questionnaire, writes the documents for the country team, and remembers
what is still pending between versions.

You do not need to edit configuration files or run commands yourself. The
agent follows a fixed procedure, so every operator gets the same result.

## Opening the agent

=== "Claude desktop app"

    1. Open the Claude desktop app and go to the **Code** tab.
    2. Choose the folder `C:\git\DIEM_NewQuestionnaire_VALIDATION` (the
       folder of this repository) and start a session.
    3. Type your request in the message box.

=== "Terminal"

    ```powershell
    cd C:\git\DIEM_NewQuestionnaire_VALIDATION
    claude
    ```

The agent must be started **in the repository folder**: that is where it
finds the validator, the procedure and the documentation.

## What you can ask

| You want to… | Say something like |
|---|---|
| Validate a questionnaire | *Validate `C:\…\diem_household_questionnaire_geopoll_yemen_20261022.xlsx`, GeoPoll, latest template, Arabic. Yemen R1.* |
| Check a new version | *New version of Yemen R1: `C:\…\…_20261023.xlsx`* |
| Close a point agreed elsewhere | *P04 is accepted: SMAR said 3 agriculture coping strategies are fine.* |
| Understand an issue | *What does `skipPattern_invalid_qname` mean and what should the country do?* |
| Get the final package | *Everything is solved, prepare the final version.* |
| Read the documentation | *Open the documentation on the KoBo checks.* |

More examples: [Example requests](requests.md).

## What the agent always does

- **Explains the steps first.** At the start of a validation it tells you,
  in plain English, how the process will go: inputs → validation → points to
  fix or confirm → new versions from the country → final validated version.
- **Asks before guessing.** It needs four things to start: where the file is,
  KoBo or GeoPoll, latest template or previous round, and the languages to
  check besides English. Anything missing, it asks for.
- **Never changes the originals.** Files on SharePoint/OneDrive (templates
  and country questionnaires) are only copied; all work happens on copies.
- **Uses the latest template.** Before each run the templates are copied from
  the DIEM Toolbox (`03. Toolbox/02. Questionnaires`).
- **Keeps a case per country and round**, so a later session knows the open
  points. Everything is published in
  `C:\Temp\DIEM_questionnaire_validation\`, split into `geopoll_output` and
  `kobo_output`, with automatic archiving of older files. See
  [Case folder and outputs](case-folder.md).
- **Keeps the documentation current.** Any change it makes to the
  procedure, the checks or the configuration is reflected in these pages in
  the same piece of work.
- **Waits for you** after each round: it does not send anything to anyone.
  Emails and documents are drafts for you to send.
- **Asks before changing code.** If a run shows a problem in the validator
  itself, it proposes a fix and waits for your OK.

## The procedure in one line

Inputs → validation → summary, Word document and cover email → new version
from the country → re-validation against the open points → … → final
validated questionnaire and final report. Details:
[Standard procedure](standard-procedure.md).

## Asking for the documentation

Ask the agent: *"open the documentation"*, *"where are the GeoPoll critical
sets explained?"*, *"what does the TLU check do?"*. It either answers from the
documentation and tells you which page to read, or starts this site and
opens it in the browser panel, on the right page.

Without the agent, run `documentation` (or `.\documentation`) in a terminal
at the repository root with the `diem-validation` environment active; the
site opens at <http://127.0.0.1:8000/>.
