"""Tests that package-level metadata matches the declared project configuration."""

import pathlib

import cornerstone_forge

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

# ---------------------------------------------------------------------------
# Version
# ---------------------------------------------------------------------------


def _pyproject_version() -> str:
    """Read the package version from the project's pyproject.toml."""
    pyproject_path = pathlib.Path(__file__).parents[2] / "pyproject.toml"
    with open(pyproject_path, "rb") as f:
        data = tomllib.load(f)
    return data["project"]["version"]


def test_package_version():
    """Test that cornerstone_forge.__version__ matches the version declared in pyproject.toml."""
    assert cornerstone_forge.__version__ == _pyproject_version()
