"""Tests for the csforge_si_220nm_passive technology definition."""

import pathlib

import csforge_si_220nm_passive as pdk
import photonforge as pf
import pytest
import tomllib
from csforge_si_220nm_passive._layers import _connections, _layer_specs, _thicknesses
from csforge_si_220nm_passive._ports import _ports
from csforge_si_220nm_passive.technology import csforge_si_220nm_pdk


def test_export(tmp_path):
    """Test that the technology can be exported and re-imported without loss of information."""
    tech = pdk.csforge_si_220nm_pdk()
    tech_file = tmp_path / "tech.phf"
    pf.write_phf(tech_file, tech)
    tech_loaded = pf.load_phf(tech_file)["technologies"][0]
    assert tech_loaded.name == tech.name
    assert tech_loaded.version == tech.version
    assert tech_loaded.layers == tech.layers
    assert tech_loaded.ports == tech.ports
    assert tech_loaded.extrusion_specs == tech.extrusion_specs
    assert tech_loaded.background_medium == tech.background_medium
    assert tech_loaded == tech


def test_demo():
    """Test that the demo script runs without errors."""
    _ = pdk.plot_cross_section()


# ---------------------------------------------------------------------------
# Port spec correctness
# ---------------------------------------------------------------------------

port_specs = _ports(_thicknesses)


def test_strip_1310nm_port_spec():
    """Test that the strip_1310nm port spec has the expected parameters."""
    spec = port_specs["strip_1310nm"]
    assert spec.width == pytest.approx(0.4)
    assert spec.num_modes == 2
    assert spec.target_neff == pytest.approx(2.52)


def test_rib_1310nm_port_spec():
    """Test that the rib_1310nm_TE port spec has the expected parameters."""
    spec = port_specs["rib_1310nm_TE"]
    assert spec.width == pytest.approx(0.4)
    assert spec.num_modes == 1
    assert spec.target_neff == pytest.approx(2.52)
    assert spec.polarization == "TE"


def test_strip_1550nm_port_spec():
    """Test that the strip_1550nm port spec has the expected parameters."""
    spec = port_specs["strip_1550nm"]
    assert spec.width == pytest.approx(0.45)
    assert spec.num_modes == 2
    assert spec.target_neff == pytest.approx(2.38)


def test_rib_1550nm_port_spec():
    """Test that the rib_1550nm_TE port spec has the expected parameters."""
    spec = port_specs["rib_1550nm_TE"]
    assert spec.num_modes == 1
    assert spec.target_neff == pytest.approx(2.38)
    assert spec.polarization == "TE"


def test_dc_port_spec():
    """Test that the dc (electrical) port spec has zero default radius."""
    spec = port_specs["dc"]
    assert spec.default_radius == 0
    assert spec.width == pytest.approx(80)


def test_all_port_specs_present():
    """Test that all required port spec keys are present in _ports."""
    required = {"strip_1310nm", "rib_1310nm_TE", "strip_1550nm", "rib_1550nm_TE", "dc"}
    assert required <= set(port_specs.keys())


# ---------------------------------------------------------------------------
# Layer specs
# ---------------------------------------------------------------------------


def test_layer_numbers_unique():
    """Test that no two layers share the same (layer, datatype) tuple."""
    seen: dict[tuple, str] = {}
    for name, spec in _layer_specs.items():
        key = tuple(spec.layer)
        assert key not in seen, f"Layer number {key} is used by both '{seen[key]}' and '{name}'"
        seen[key] = name


# ---------------------------------------------------------------------------
# Layer thicknesses
# ---------------------------------------------------------------------------


def test_thicknesses_keys():
    """Test that all process layer thickness entries are present."""
    required = {
        "box",
        "strip",
        "rib_slab",
        "ebeam_gratings",
        "duv_gratings",
        "tox",
        "heater_fil",
        "contact_pad",
    }
    assert required <= set(_thicknesses.keys())


# ---------------------------------------------------------------------------
# Electrical connections
# ---------------------------------------------------------------------------


def test_heater_contact_pad_connected():
    """Test that heater filaments and contact pads are electrically connected."""
    heater_layer = _layer_specs["heater_fil"].layer
    contact_layer = _layer_specs["contact_pad"].layer
    assert (heater_layer, contact_layer) in _connections


# ---------------------------------------------------------------------------
# Technology
# ---------------------------------------------------------------------------


def test_technology_name():
    """Test that the technology has the expected name."""
    tech = csforge_si_220nm_pdk()
    assert tech.name == "csforge_si_220nm_passive"


def _pyproject_version() -> str:
    """Read the package version from csforge-si_220nm_passive/pyproject.toml."""
    pyproject_path = pathlib.Path(__file__).parents[1] / "pyproject.toml"
    with open(pyproject_path, "rb") as f:
        data = tomllib.load(f)
    return data["project"]["version"]


def test_technology_version():
    """Test that the technology version string is set to the package version."""
    tech = csforge_si_220nm_pdk()
    assert tech.version == _pyproject_version()


def test_technology_has_layers():
    """Test that the technology exposes all PDK layers."""
    tech = csforge_si_220nm_pdk()
    for layer_name in _layer_specs:
        assert layer_name in tech.layers, f"Layer '{layer_name}' missing from technology"


def test_technology_has_ports():
    """Test that the technology exposes all port specs."""
    tech = csforge_si_220nm_pdk()
    for port_name in port_specs:
        assert port_name in tech.ports, f"Port spec '{port_name}' missing from technology"


def test_technology_substrate_adds_one_extrusion():
    """Test that include_substrate=True adds exactly one extrusion to the stack."""
    tech_no_sub = csforge_si_220nm_pdk(include_substrate=False)
    tech_with_sub = csforge_si_220nm_pdk(include_substrate=True)
    assert len(tech_with_sub.extrusion_specs) == len(tech_no_sub.extrusion_specs) + 1


def test_technology_export_roundtrip(tmp_path):
    """Test that the technology survives a write/load roundtrip without data loss."""
    tech = csforge_si_220nm_pdk()
    tech_file = tmp_path / "tech.phf"
    pf.write_phf(tech_file, tech)
    tech_loaded = pf.load_phf(tech_file)["technologies"][0]
    assert tech_loaded == tech
