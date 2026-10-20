# Developer Tools

This page describes the tools used to develop, test, and document Cornerstone Forge.

---

## uv

[uv](https://docs.astral.sh/uv/) is an extremely fast Python package and project manager used for all dependency management in this project.

Cornerstone Forge is a single **uv project** that builds one distribution, `cornerstone-forge`. Each Cornerstone technology is a subpackage of `cornerstone_forge`, and the root `pyproject.toml` holds the package metadata, dependencies and tool configuration.

```
cornerstone-forge/              ← project root (pyproject.toml)
└── src/cornerstone_forge/
    ├── si_220nm_passive/       ← PDK subpackage
    └── si_220nm_active/        ← PDK subpackage
```

Key commands:

| Command | Purpose |
|---------|---------|
| `uv sync` | Install all main dependencies |
| `uv sync --group dev` | Include development tools |
| `uv sync --group docs` | Include documentation tools |
| `uv sync --group notebooks` | Include the Jupyter kernel and Quarto execution dependencies for the notebooks |
| `uv sync --group dev --group docs` | Full contributor setup |
| `uv run <cmd>` | Run a command inside the project environment |
| `uv add --group dev <pkg>` | Add a dev dependency |

---

## pre-commit

[pre-commit](https://pre-commit.com/) runs automated checks before every `git commit`. The configuration lives in `.pre-commit-config.yaml` at the repository root.

Active hooks:

| Hook | Tool | What it does |
|------|------|-------------|
| `isort` | isort 5 | Sorts import blocks (black-compatible profile) |
| `ruff-check` | ruff | Lints Python files and auto-fixes safe issues |
| `ruff-format` | ruff | Formats Python files |

Install the hooks after cloning:

```bash
uv run pre-commit install
```

Run manually against all files:

```bash
uv run pre-commit run --all-files
```

---

## ruff

[ruff](https://docs.astral.sh/ruff/) is the project's linter and formatter, configured in the root `pyproject.toml` under `[tool.ruff]`.

Enabled rule sets include `D` (Google-style docstrings), `E`/`W` (pycodestyle), `F` (pyflakes), `B` (bugbear), `I` (isort), `UP` (pyupgrade), and several others.

```bash
uv run ruff check .          # lint
uv run ruff check --fix .    # lint and auto-fix
uv run ruff format .         # format
uv run ruff format --check . # check formatting without writing
```

---

## pytest

[pytest](https://docs.pytest.org/) is the test runner. Tests live in `tests/`, with one directory per PDK subpackage (e.g. `tests/si_220nm_passive/`).

```bash
uv run pytest                          # run all tests
uv run pytest tests/si_220nm_passive/  # run one PDK's tests
uv run pytest -v                       # verbose output
```

Test files follow the `*_test.py` naming convention and are organised by topic:

| File | Covers |
|------|--------|
| `technology_test.py` | Technology definition, layers, thicknesses, port specs, extrusions |
| `components_test.py` | Component catalogue, port counts, port names, naming conventions |
| `package_test.py` | `cornerstone_forge.__version__` matches `pyproject.toml` |

---

## Quarto

[Quarto](https://quarto.org/) is used for the notebooks in `notebooks/<technology>/`, written as
`.qmd` files. The Quarto CLI is installed separately from the
[Quarto website](https://quarto.org/docs/get-started/); the Python side (Jupyter kernel) comes from
the `notebooks` dependency group. In VS Code, use the
[Quarto extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) with the
`.venv/` interpreter selected.

```bash
uv run --group notebooks quarto check jupyter                 # verify Quarto uses .venv/
uv run --group notebooks quarto preview <path/to/file>.qmd    # live preview
uv run --group notebooks quarto render <path/to/file>.qmd     # render to HTML
```

See [Notebooks](notebooks.md) for the full setup and workflow.

---

## MkDocs

[MkDocs](https://www.mkdocs.org/) with the [Material theme](https://squidfunk.github.io/mkdocs-material/) generates this documentation site from Markdown files in `docs/`.

```bash
uv run --group docs mkdocs serve   # live preview at http://127.0.0.1:8000
uv run --group docs mkdocs build   # build static site to build/
```

!!! tip
    If `mkdocs` is also installed in the `dev` group, you can omit `--group docs`.
