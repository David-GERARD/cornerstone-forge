# cornerstone-forge
PhotonForge implementation of [Cornerstone's PDK](https://github.com/cornerstone-uos/cornerstone-pdk).


## Setup (for developpers)

1. Clone the repository.
2. If required, install [`uv`](https://docs.astral.sh/uv/getting-started/installation/).
3. Run the following:
```bash
    uv sync --group dev # Install all main and development dependencies
    uv run pre-commit install # Setup pre-commit hooks to enforce code quality
```

[!TIP]
> This project uses [`uv` workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/) to jointly manage the dependencies of the different technology packages.

## Building the documentation locally

After setup, run:
```bash
    uv run mkdocs serve
```

In your web browser, enter [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) in the URL searchbar.