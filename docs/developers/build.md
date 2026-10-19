# Build & Workflow Reference

Common day-to-day commands for working on Cornerstone Forge.

---

## Running tests

```bash
# All PDKs
uv run pytest

# Single PDK
uv run pytest tests/si_220nm_passive/

# Verbose with test names
uv run pytest -v

# Stop on first failure
uv run pytest -x
```

---

## Linting and formatting

```bash
# Check for lint issues
uv run ruff check .

# Auto-fix safe issues
uv run ruff check --fix .

# Format all files
uv run ruff format .

# Check formatting without writing changes
uv run ruff format --check .
```

Run both together (same as pre-commit):

```bash
uv run pre-commit run --all-files
```

---

## Building the documentation

```bash
# Live preview with hot-reload
uv run --group docs mkdocs serve

# Build static site to build/
uv run --group docs mkdocs build
```

The built site is written to `build/`. This directory is git-ignored.

---

## uv cheatsheet

| Task | Command |
|------|---------|
| Install all deps (dev + docs) | `uv sync --group dev --group docs` |
| Add a runtime dep | `uv add <pkg>` |
| Add a dev dep | `uv add --group dev <pkg>` |
| Add a docs dep | `uv add --group docs <pkg>` |
| Build the wheel and sdist | `uv build` |
| Remove a dep | `uv remove <pkg>` |
| Update all deps | `uv lock --upgrade` |
| Show installed packages | `uv pip list` |

---

## Adding a new PDK

Each PDK is a subpackage of `cornerstone_forge`; no packaging changes are needed.

1. Create the subpackage, following the structure of `si_220nm_passive`:

    ```
    src/cornerstone_forge/<technology>/
    ├── __init__.py
    ├── technology.py
    ├── oband.py / cband.py
    ├── _layers.py
    ├── _ports.py
    ├── _extrusions.py
    ├── _media.py
    └── _utils.py
    ```

    Users then import it with `from cornerstone_forge import <technology>`.

2. Add its tests under `tests/<technology>/`. Test module names may repeat those of other PDKs
   (e.g. `technology_test.py`) because pytest runs in `importlib` import mode.

3. Put example notebooks (Quarto `.qmd` files, see [Notebooks](notebooks.md)) under
   `notebooks/<technology>/`, and any development-only scripts or source data (not shipped in
   the wheel) under `tools/<technology>/`.

4. Add a documentation page at `docs/pdks/<technology>.md` and register it in `mkdocs.yml`.
