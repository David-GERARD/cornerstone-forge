# Cornerstone Forge

[PhotonForge](https://docs.flexcompute.com/projects/photonforge/en/latest/) implementation of [Cornerstone's silicon photonics PDKs](https://github.com/cornerstone-uos/cornerstone-pdk).

Each package in this workspace provides a parametric `pf.Technology` definition and a pre-loaded component catalogue that plug directly into PhotonForge's simulation and layout environment.

---

## Available PDKs

| Package | Technology | Bands | Status |
|---------|-----------|-------|--------|
| `csforge-si_220nm_passive` | SOI 220 nm — passive | O-band (1310 nm), C-band (1550 nm) | Available |
| `csforge-si_220nm_active` | SOI 220 nm — PN modulators | C-band (1550 nm) | In development |

---

## Installation

> **Coming soon** — packages will be published to PyPI.

To use the PDKs today, install from source by following the [contributor setup](#contributor-setup) below.

---

## Quick start

```python
import photonforge as pf
import csforge_si_220nm_passive as pdk

# Register the technology globally
pf.config.default_technology = pdk.csforge_si_220nm_pdk()

# Pick a component from the catalogue
mmi = pdk.components["SOI220nm_1550nm_TE_STRIP_2x1_MMI"]
print(list(mmi.ports.keys()))  # ['o1', 'o2', 'o3']
```

---

## Contributor setup

### Prerequisites

- Python ≥ 3.10
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Git

### Steps

```bash
# 1. Clone (or fork then clone)
git clone https://github.com/<your-username>/cornerstone-forge
cd cornerstone-forge

# 2. Install all dependencies (workspace + dev tools)
uv sync --group dev

# 3. Install pre-commit hooks
uv run pre-commit install

# 4. Verify
uv run pytest
```

> **Note** — This project uses [uv workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/).
> A single `.venv/` at the root is shared across all sub-packages.

### Common commands

| Task | Command |
|------|---------|
| Run tests | `uv run pytest` |
| Lint | `uv run ruff check .` |
| Format | `uv run ruff format .` |
| Preview docs | `uv run --group docs mkdocs serve` |
| Build docs | `uv run --group docs mkdocs build` |

---

## Repository layout

```
cornerstone-forge/
├── pyproject.toml                  # uv workspace root & shared config
├── mkdocs.yml
├── docs/
├── csforge-si_220nm_passive/       # Passive PDK
│   ├── pyproject.toml
│   ├── README.md
│   └── src/csforge_si_220nm_passive/
└── csforge-si_220nm_active/        # Active PDK (in development)
    ├── pyproject.toml
    └── README.md
```

---

## Contributing

Contributions are welcome. Please ensure that:

- All tests pass: `uv run pytest`
- Code is lint-clean: `uv run pre-commit run --all-files`
- New public functions include Google-style docstrings
