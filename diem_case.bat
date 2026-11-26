@echo off
REM Standard DIEM validation procedure (same steps for every agent): see AGENTS.md
python "%~dp0.claude\skills\diem-validate\scripts\diem_case.py" %*
