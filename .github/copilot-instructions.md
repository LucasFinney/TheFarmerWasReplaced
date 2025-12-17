# Copilot instructions for this workspace

Purpose
- Help AI agents be productive editing player scripts and helper files for the TFWR save files in this workspace.

Big picture
- This repository is a game save workspace containing user-editable scripts that are executed by the game engine. The scripting language is not full Python; `__builtins__.py` provides a Python-style shim that documents the game API available to scripts.
- Typical flow: agent edits a script (for example `Save0/main.py`) which uses game API functions and constants from `__builtins__.py`. The game reads the save folder (e.g., `Save0/`) to run the script.

Key files to inspect
- `Save0/main.py` — example user script that uses movement and world queries.
- `Save0/__builtins__.py` — authoritative list of available functions, constants, items, entities and unlocks. Treat this as the API reference.
- `Save0/save.json` — UI/save metadata (inventory, open files, positions). Avoid editing unless intentionally changing save state.

Coding conventions & patterns (project-specific)
- Scripts import the game API with `from __builtins__ import *` and then call functions like `move(North)`, `get_world_size()`, `can_harvest()`, etc. Follow the exact symbol names; they are case-sensitive and defined in `__builtins__.py`.
- Do not assume full Python semantics: `__builtins__.py` is a type-hint shim. Changes to runtime behavior must be done through the game, not by modifying this shim.
- Keep edits local to a `SaveX/` folder unless the user asks to migrate or refactor multiple saves.

Examples from the codebase
- Movement loop (from `Save0/main.py`):

```python
from __builtins__ import *
for i in range(2):
    for j in range(get_world_size()):
        move(North)
    move(East)
```

This demonstrates using the provided constants (`North`, `East`) and `get_world_size()` to control movement.

Guidance for AI edits
- Use only names and functions that appear in `__builtins__.py`. If you think a new helper is required, propose it to the user rather than inventing new engine APIs.
- Avoid editing `save.json` unintentionally — it stores UI state and inventory. If adjusting save state is intended, summarize the exact keys changed for user review.
- Prefer minimal, reversible changes: keep prior versions of user scripts and open a short diff in the PR or the patch.

Testing and running
- There is no repository-level build or test runner. To validate runtime behavior, the user must run the TFWR game environment and load the edited save. Ask the user for their local run steps if you need to automate testing.

When to modify `__builtins__.py`
- Only update this file to improve type hints or documentation of the existing API. Do NOT change it to simulate new runtime behavior; the shim does not control game logic.

When in doubt
- Ask the user whether they want the change to the live save state, a new save copy, or a one-off script to test in the game. Provide a short checklist of changed files and why.

Files referenced
- `Save0/main.py`
- `Save0/__builtins__.py`
- `Save0/save.json`

Please review and tell me if you want more detail (run steps, additional examples, or a stricter rule set for editing saves).
