# Build & Workflow Reference

Common day-to-day commands for working within the Cornerstone Forge workspace.

---

## Running tests

```bash
# All packages
uv run pytest

# Single package
uv run pytest csforge-si_220nm_passive/tests/

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

# Build static site to site/
uv run --group docs mkdocs build
```

The built site is written to `site/`. This directory is git-ignored.

---

## uv workspace cheatsheet

| Task | Command |
|------|---------|
| Install all deps (dev + docs) | `uv sync --group dev --group docs` |
| Add a runtime dep | `uv add <pkg>` |
| Add a dev dep | `uv add --group dev <pkg>` |
| Add a docs dep | `uv add --group docs <pkg>` |
| Remove a dep | `uv remove <pkg>` |
| Update all deps | `uv lock --upgrade` |
| Show installed packages | `uv pip list` |

---

## Adding a new PDK package

1. Create the package directory:

    ```bash
    mkdir csforge-<technology>
    cd csforge-<technology>
    uv init --lib
    ```

2. Register it as a workspace member in the root `pyproject.toml`:

    ```toml
    [tool.uv.workspace]
    members = [
        "csforge-si_220nm_active",
        "csforge-si_220nm_passive",
        "csforge-<technology>",   # add here
    ]

    [tool.uv.sources]
    csforge-<technology> = { workspace = true }
    ```

3. Re-sync the workspace:

    ```bash
    uv sync --group dev
    ```

4. Implement the package following the structure of `csforge-si_220nm_passive`:

    ```
    csforge-<technology>/
    ├── pyproject.toml
    ├── tests/
    └── src/csforge_<technology>/
        ├── __init__.py
        ├── technology.py
        ├── oband.py / cband.py
        ├── _layers.py
        ├── _ports.py
        ├── _extrusions.py
        ├── _media.py
        └── _utils.py
    ```

5. Add a documentation page under `docs/pdks/` and register it in `mkdocs.yml`.
