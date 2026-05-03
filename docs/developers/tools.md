# Developer Tools

This page describes the tools used to develop, test, and document Cornerstone Forge.

---

## uv

[uv](https://docs.astral.sh/uv/) is an extremely fast Python package and project manager used for all dependency management in this project.

Cornerstone Forge is structured as a **uv workspace** — a single virtual environment shared across all sub-packages. The workspace root `pyproject.toml` declares the members and shared dependencies; each sub-package has its own `pyproject.toml` with package-specific metadata.

```
cornerstone-forge/       ← workspace root (pyproject.toml)
├── csforge-si_220nm_passive/   ← workspace member
└── csforge-si_220nm_active/    ← workspace member
```

Key commands:

| Command | Purpose |
|---------|---------|
| `uv sync` | Install all main dependencies |
| `uv sync --group dev` | Include development tools |
| `uv sync --group docs` | Include documentation tools |
| `uv sync --group dev --group docs` | Full contributor setup |
| `uv run <cmd>` | Run a command inside the workspace environment |
| `uv add --group dev <pkg>` | Add a dev dependency |

---

## pre-commit

[pre-commit](https://pre-commit.com/) runs automated checks before every `git commit`. The configuration lives in `.pre-commit-config.yaml` at the workspace root.

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

[ruff](https://docs.astral.sh/ruff/) is the project's linter and formatter, configured in the workspace `pyproject.toml` under `[tool.ruff]`.

Enabled rule sets include `D` (Google-style docstrings), `E`/`W` (pycodestyle), `F` (pyflakes), `B` (bugbear), `I` (isort), `UP` (pyupgrade), and several others.

```bash
uv run ruff check .          # lint
uv run ruff check --fix .    # lint and auto-fix
uv run ruff format .         # format
uv run ruff format --check . # check formatting without writing
```

---

## pytest

[pytest](https://docs.pytest.org/) is the test runner. Tests live in each package's `tests/` directory.

```bash
uv run pytest                              # run all tests
uv run pytest csforge-si_220nm_passive/tests/  # run one package's tests
uv run pytest -v                           # verbose output
```

Test files follow the `*_test.py` naming convention and are organised by topic:

| File | Covers |
|------|--------|
| `technology_test.py` | Technology definition, layers, thicknesses, port specs, extrusions |
| `components_test.py` | Component catalogue, port counts, port names, naming conventions |
| `package_test.py` | Package version matches `pyproject.toml` |

---

## MkDocs

[MkDocs](https://www.mkdocs.org/) with the [Material theme](https://squidfunk.github.io/mkdocs-material/) generates this documentation site from Markdown files in `docs/`.

```bash
uv run --group docs mkdocs serve   # live preview at http://127.0.0.1:8000
uv run --group docs mkdocs build   # build static site to site/
```

!!! tip
    If `mkdocs` is also installed in the `dev` group, you can omit `--group docs`.
