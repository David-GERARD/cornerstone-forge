# Contributor Installation

Follow these steps to set up a local development environment for Cornerstone Forge.

---

## Prerequisites

| Tool | Minimum version | Install |
|------|----------------|---------|
| Python | 3.10 | [python.org](https://www.python.org/downloads/) |
| uv | latest | [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/) |
| Git | any | [git-scm.com](https://git-scm.com/) |

---

## 1 — Fork and clone

Fork the repository on GitHub, then clone your fork:

```bash
git clone https://github.com/<your-username>/cornerstone-forge
cd cornerstone-forge
```

---

## 2 — Install dependencies

Install all main and development dependencies using uv:

```bash
uv sync --group dev
```

This creates a `.venv/` at the repository root and installs:

- All shared dependencies (`photonforge`, etc.)
- `cornerstone-forge` itself in editable mode (all PDK subpackages)
- Development tools (pytest, ruff, pre-commit)

To also install documentation tools, or the Jupyter kernel used by the notebooks:

```bash
uv sync --group dev --group docs
uv sync --group dev --group notebooks
```

---

## 3 — Install pre-commit hooks

```bash
uv run pre-commit install
```

This registers the hooks so that `ruff check`, `ruff format`, and `isort` run automatically on every `git commit`.

---

## 4 — Verify the setup

Run the test suite to confirm everything is working:

```bash
uv run pytest
```

All tests should pass. You can also check that linting is clean:

```bash
uv run ruff check .
uv run ruff format --check .
```

---

## 5 — (Optional) Preview the documentation

```bash
uv run --group docs mkdocs serve
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Updating dependencies

To add a new runtime dependency:

```bash
uv add <package>                   # runtime dependency
uv add --group dev <package>       # dev group
uv add --group docs <package>      # docs group
uv add --group notebooks <package> # notebooks group
```

Always commit the updated `uv.lock` file alongside any `pyproject.toml` changes.
