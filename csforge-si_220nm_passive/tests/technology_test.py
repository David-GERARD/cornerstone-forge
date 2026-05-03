"""Tests for the csforge_si_220nm_passive technology definition."""

import csforge_si_220nm_passive as pdk
import photonforge as pf
import pytest
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


def test_strip_1310nm_port_spec():
    """Test that the strip_1310nm port spec has the expected parameters."""
    spec = _ports["strip_1310nm"]
    assert spec.width == pytest.approx(0.4)
    assert spec.num_modes == 2
    assert spec.target_neff == pytest.approx(2.52)


def test_rib_1310nm_port_spec():
    """Test that the rib_1310nm_TE port spec has the expected parameters."""
    spec = _ports["rib_1310nm_TE"]
    assert spec.width == pytest.approx(0.4)
    assert spec.num_modes == 1
    assert spec.target_neff == pytest.approx(2.52)
    assert spec.polarization == "TE"


def test_strip_1550nm_port_spec():
    """Test that the strip_1550nm port spec has the expected parameters."""
    spec = _ports["strip_1550nm"]
    assert spec.width == pytest.approx(0.45)
    assert spec.num_modes == 2
    assert spec.target_neff == pytest.approx(2.38)


def test_rib_1550nm_port_spec():
    """Test that the rib_1550nm_TE port spec has the expected parameters."""
    spec = _ports["rib_1550nm_TE"]
    assert spec.num_modes == 1
    assert spec.target_neff == pytest.approx(2.38)
    assert spec.polarization == "TE"


def test_dc_port_spec():
    """Test that the dc (electrical) port spec has zero default radius."""
    spec = _ports["dc"]
    assert spec.default_radius == 0
    assert spec.width == pytest.approx(80)


def test_all_port_specs_present():
    """Test that all required port spec keys are present in _ports."""
    required = {"strip_1310nm", "rib_1310nm_TE", "strip_1550nm", "rib_1550nm_TE", "dc"}
    assert required <= set(_ports.keys())


# ---------------------------------------------------------------------------
# Layer specs
# ---------------------------------------------------------------------------


def test_layer_specs_keys():
    """Test that all expected process layers are defined."""
    required = {
        "grating_ebl",
        "grating_duv",
        "wg_lf",
        "wg_df",
        "rib_slab",
        "heater_fil",
        "contact_pad",
        "FloorPlan",
        "Label_Etch_DF",
    }
    assert required <= set(_layer_specs.keys())


def test_layer_numbers_unique():
    """Test that no two layers share the same (layer, datatype) tuple."""
    seen: dict[tuple, str] = {}
    for name, spec in _layer_specs.items():
        key = tuple(spec.layer)
        assert key not in seen, f"Layer number {key} is used by both '{seen[key]}' and '{name}'"
        seen[key] = name


def test_wg_lf_layer_number():
    """Test that the main waveguide layer has the expected GDS layer number."""
    assert _layer_specs["wg_lf"].layer == (3, 0)


def test_rib_slab_layer_number():
    """Test that the rib slab layer has the expected GDS layer number."""
    assert _layer_specs["rib_slab"].layer == (5, 0)


def test_heater_fil_layer_number():
    """Test that the heater filament layer has the expected GDS layer number."""
    assert _layer_specs["heater_fil"].layer == (39, 0)


def test_contact_pad_layer_number():
    """Test that the contact pad layer has the expected GDS layer number."""
    assert _layer_specs["contact_pad"].layer == (41, 0)


# ---------------------------------------------------------------------------
# Layer thicknesses
# ---------------------------------------------------------------------------


def test_thicknesses_keys():
    """Test that all process layer thickness entries are present."""
    required = {
        "box",
        "waveguide",
        "rib_slab",
        "ebeam_gratings",
        "duv_gratings",
        "tox",
        "heater_fil",
        "contact_pad",
    }
    assert required <= set(_thicknesses.keys())


def test_waveguide_thickness():
    """Test that the waveguide thickness is 220 nm (0.22 µm)."""
    assert _thicknesses["waveguide"] == pytest.approx(0.22)


def test_box_thickness():
    """Test that the buried-oxide layer thickness is 3 µm."""
    assert _thicknesses["box"] == pytest.approx(3.0)


def test_tox_thickness():
    """Test that the top-oxide thickness is 2 µm."""
    assert _thicknesses["tox"] == pytest.approx(2.0)


def test_all_thicknesses_positive():
    """Test that all layer thicknesses are strictly positive."""
    for name, t in _thicknesses.items():
        assert t > 0, f"Thickness for '{name}' must be positive, got {t}"


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


def test_technology_version():
    """Test that the technology version string is set."""
    tech = csforge_si_220nm_pdk()
    assert tech.version == "0.1.0"


def test_technology_has_layers():
    """Test that the technology exposes all PDK layers."""
    tech = csforge_si_220nm_pdk()
    for layer_name in _layer_specs:
        assert layer_name in tech.layers, f"Layer '{layer_name}' missing from technology"


def test_technology_has_ports():
    """Test that the technology exposes all port specs."""
    tech = csforge_si_220nm_pdk()
    for port_name in _ports:
        assert port_name in tech.ports, f"Port spec '{port_name}' missing from technology"


def test_technology_without_substrate_extrusion_count():
    """Test that the default technology (no substrate) has the expected extrusion count."""
    tech_no_sub = csforge_si_220nm_pdk(include_substrate=False)
    tech_with_sub = csforge_si_220nm_pdk(include_substrate=True)
    assert len(tech_with_sub.extrusion_specs) == len(tech_no_sub.extrusion_specs) + 1


def test_technology_background_medium_is_air():
    """Test that the background simulation medium is air (permittivity ≈ 1)."""
    tech = csforge_si_220nm_pdk()
    bg = tech.background_medium
    # Air permittivity is 1.0
    assert bg.permittivity == pytest.approx(1.0)


def test_technology_export_roundtrip(tmp_path):
    """Test that the technology survives a write/load roundtrip without data loss."""
    tech = csforge_si_220nm_pdk()
    tech_file = tmp_path / "tech.phf"
    pf.write_phf(tech_file, tech)
    tech_loaded = pf.load_phf(tech_file)["technologies"][0]
    assert tech_loaded == tech
