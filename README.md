# DIEM Questionnaire Validation

Checks a country's DIEM household questionnaire (KoBo XLSForm or GeoPoll Excel)
against the latest template or the previous round. It produces:

- an **Excel report** listing every difference by severity (high / medium / info);
- a **validated questionnaire** ready to deploy, with crop list, admin lists
  (from AGOL) and placeholders filled in.

## Get it running

**1. Install** [Git](https://git-scm.com/downloads) and
[Miniconda or Anaconda](https://docs.conda.io/en/latest/miniconda.html).

**2. Clone the repository and create the environment** (in an Anaconda Prompt):

```powershell
git clone https://github.com/edoardoforzano1/DIEM_NewQuestionnaire_VALIDATION.git
cd DIEM_NewQuestionnaire_VALIDATION
conda env create -f environment.yml
conda activate diem-validation
```

To update an existing environment later, run `conda env update -f environment.yml --prune`.

**3. Set your paths** in `configuration/validation_config.yaml`. This is needed once:

| Key | What to put |
|---|---|
| `working_dir` | folder where you put the country questionnaire |
| `templates_dir` | the `Template` folder of this repository |
| `templates_source_dir` | your synced DIEM Toolbox folder (`…/03. Toolbox/02. Questionnaires`), so the latest templates are copied in automatically; leave it empty if you don't have access |
| `output_dir` | where results go, e.g. `C:/Temp/DIEM_questionnaire_validation` |

**4. Set up each run** in the same file:

| Key | Value |
|---|---|
| `tool` | `kobo` or `geopoll` |
| `questionnaire_file` | the country file name |
| `language` | the deployment language |
| `iso3` | the country code |
| `reference_mode` | `latest_template` or `previous_round` |

**5. Run** from the repository root:

```powershell
validate
```

The report and the validated questionnaire appear in `output_dir`, under
`kobo_output/` or `geopoll_output/`.

## Other commands

| Command | Does |
|---|---|
| `.\documentation` | opens the full documentation at http://127.0.0.1:8000/ |
| `tool_admin_check` / `tool_admin_sync` | check or rebuild the admin lists against AGOL (`configuration/admin_tools_config.yaml`) |
| `streamlit_ui` | optional browser interface over the same commands |
| `smoke_test` | quick end-to-end check after changing the code |

## Documentation

Everything else is in the documentation: how each check works, severities,
how to read the report, configuration keys, admin tools, and the standard
validation procedure. Start it with `.\documentation`, or read the pages
directly in [`docs/`](docs/).

- **Getting Started**: setup and every configuration key.
- **Validation Workflow**: the GeoPoll and KoBo logic, checks and severity.
- **Report Output**: the report sheets, column by column.
- **Working with the Agent**: running validations with Claude Code (the
  `diem-validate` skill). This covers the round-by-round procedure, the Word
  document for the country team and the final package.

## Rules

- The original files on SharePoint / OneDrive (Toolbox templates, country
  questionnaires) are only read or copied, never edited.
- `CLAUDE.md` describes the code structure and conventions for developers.
