"""Tests that package-level metadata matches the declared project configuration."""

import pathlib

import csforge_si_220nm_passive as pdk
import tomllib

# ---------------------------------------------------------------------------
# Version
# ---------------------------------------------------------------------------


def _pyproject_version() -> str:
    """Read the package version from csforge-si_220nm_passive/pyproject.toml."""
    pyproject_path = pathlib.Path(__file__).parents[1] / "pyproject.toml"
    with open(pyproject_path, "rb") as f:
        data = tomllib.load(f)
    return data["project"]["version"]


def test_package_version():
    """Test that pdk.__version__ matches the version declared in pyproject.toml."""
    assert pdk.__version__ == _pyproject_version()
