# The Farmer Was Replaced — Save workspace

This folder contains editable save files and user scripts for the game *The Farmer Was Replaced*.

- `Save0/` — a save folder with editable scripts (`main.py`), the API shim (`__builtins__.py`), and `save.json` (UI state).
- `.github/copilot-instructions.md` — guidance for AI agents editing scripts in this workspace.

Notes
- Edit scripts under `SaveX/` and use the game to run/test changes — the `__builtins__.py` file is a type-hint shim only.
- Avoid committing `save.json` (contains local UI state). It's listed in `.gitignore`.
