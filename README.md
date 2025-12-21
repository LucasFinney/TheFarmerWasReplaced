# The Farmer Was Replaced — Save workspace

This folder contains editable save files and user scripts for the game *The Farmer Was Replaced*.

- `Save0/` — a save folder with editable scripts (`main.py`), the API shim (`__builtins__.py`), and `save.json` (UI state).
- `.github/copilot-instructions.md` — guidance for AI agents editing scripts in this workspace.

Notes
- Edit scripts under `SaveX/` and use the game to run/test changes — the `__builtins__.py` file is a type-hint shim only.
- Avoid committing `save.json` (contains local UI state). It's listed in `.gitignore`.

## TO DO
- Automate crop selection based on player inventory? (IE. Check what's running low and adjust planting procedure accordingly)

Progress log

- Added `.github/copilot-instructions.md` to describe workspace-specific guidance for AI agents.
- Initialized a local Git repo in `Saves/`, added `.gitignore` and `README.md`, and created the initial commit.
- Created `experiment/auto-harvest` branch and pushed prototypes: `main_experiment.py` and `auto_carrot.py`.
- Implemented `Save0/auto_crt_bsh_grs.py` and `Save0/auto_crt_bsh_grs_tr.py` for mixed and alternate layouts; refactored to use `get_world_size()` and sense functions.
- Extracted reusable helpers into `Save0/field_lib.py` (idempotent helpers: `ensure_*`, `prepare_field`, `farm_pass`).
- Added and consolidated pumpkin support: `ensure_pumpkin`, `prepare_pumpkin_field`, `farm_pass_pumpkins`, then refactored to use a generic `primary_crop` parameter for `prepare_field` and `farm_pass`.
- Created `feat/pumpkins` branch, opened PR #2, and squash-merged it into `master` after testing (branch cleanup completed).

12/21/2025
- Implemented crop watering in `prepare_field` (or via a helper) so the system can support crops that need watering between planting and harvest.
- Generalized mixed-field configurations using lists
- Added a one-pass test helper (non-looping) to safely validate changes in-game before running continuous loops.  (Added: `field_lib.run_once`.)
- Add small docs/examples for how to run and test each script in the TFWR UI.
