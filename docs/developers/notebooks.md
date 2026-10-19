# Notebooks

Example and analysis notebooks live in `notebooks/<technology>/` (e.g. `notebooks/si_220nm_passive/`).
They are written as [Quarto](https://quarto.org/) documents (`.qmd`): plain-text Markdown files with
executable ```` ```{python} ```` code chunks. Unlike `.ipynb` files, they don't store outputs, so
diffs stay small and reviewable.

---

## Setup

### 1 — Install the Quarto CLI

Quarto is a standalone command-line tool and is **not** installed by uv. Download the installer for
your platform from the [Quarto website](https://quarto.org/docs/get-started/) and check that it is on
your `PATH`:

```bash
quarto --version
```

### 2 — Install the notebook dependencies

The `notebooks` dependency group installs the Jupyter kernel (`ipykernel`) and the libraries Quarto
uses to execute Python chunks into the project's `.venv/`:

```bash
uv sync --group dev --group notebooks
```

!!! warning
    `uv sync` removes packages that aren't part of the groups you request. Running a plain
    `uv sync --group dev` afterwards uninstalls the notebook dependencies again; include
    `--group notebooks` whenever you sync.

Check that Quarto finds the project's Python and Jupyter:

```bash
uv run --group notebooks quarto check jupyter
```

The reported Python path must be `<repo>/.venv/bin/python3` (on Windows, `<repo>\.venv\Scripts\python.exe`).

### 3 — Install the VS Code extension

Install the [Quarto extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto)
for VS Code. To run code chunks interactively, you also need the
[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and
[Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions.

---

## Editing and running notebooks in VS Code

1. Open the repository root folder in VS Code.
2. Run `>Python: Select Interpreter` from the Command Palette and choose `./.venv/bin/python`.
   The Quarto extension and the Jupyter kernel both use this interpreter, so code runs against the
   editable `cornerstone_forge` install and the locked dependencies.
3. Open a `.qmd` file:
    - **>Run Cell** (above each chunk, or `Ctrl+Shift+Enter` / `Cmd+Shift+Enter`) runs a chunk
      in an interactive Jupyter window.
    - **Quarto: Preview** (`Ctrl+Shift+K` / `Cmd+Shift+K`) renders the whole document and opens
      a live preview that refreshes on save.

If the cells fail with `ModuleNotFoundError: No module named 'cornerstone_forge'`, the wrong
interpreter is selected: repeat step 2.

---

## Rendering from the command line

Run Quarto through `uv run` so that it uses the project's `.venv/`:

```bash
# Live preview in the browser, re-rendered on save
uv run --group notebooks quarto preview notebooks/si_220nm_passive/example-design.qmd

# Render to HTML once
uv run --group notebooks quarto render notebooks/si_220nm_passive/example-design.qmd
```

`uv run` puts `.venv/bin` first on the `PATH`, so Quarto picks up the project's Python. Outside
`uv run`, you can point Quarto at it explicitly with `export QUARTO_PYTHON=.venv/bin/python`.

Rendered files (`*.html`, `*_files/`, `.quarto/`) are git-ignored.

---

## Cloud simulations guardrail

Several notebooks can submit FDTD simulations, mode-solver batches or cost estimates to the Tidy3D
cloud, which consumes FlexCredits. Each notebook sets

```python
run_fdtd = False
```

in its setup chunk, and every chunk that talks to the cloud (or uses its results) is wrapped in
`if run_fdtd:`. Rendering or running a notebook end-to-end is therefore free by default. Set
`run_fdtd = True` only when you intend to run the simulations.

---

## Adding a notebook

Create a new `.qmd` file in `notebooks/<technology>/` with this front matter:

```yaml
---
title: My analysis
jupyter: python3
---
```

To convert an existing Jupyter notebook, run:

```bash
quarto convert my-notebook.ipynb
```

Then add the `run_fdtd` guardrail to any chunk that submits work to the Tidy3D cloud.
