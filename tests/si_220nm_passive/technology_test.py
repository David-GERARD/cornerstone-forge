"""Tests for the cornerstone_forge.si_220nm_passive technology definition."""

import photonforge as pf
import pytest
from photonforge._live_viewer import pdks as live_viewer_pdks

from cornerstone_forge import si_220nm_passive as pdk
from cornerstone_forge.si_220nm_passive._layers import _connections, _layer_specs, _thicknesses
from cornerstone_forge.si_220nm_passive._ports import _ports
from cornerstone_forge.si_220nm_passive.technology import si_220nm_passive_pdk

# ---------------------------------------------------------------------------
# Load technology test
# ---------------------------------------------------------------------------


def test_load_technology():
    """Test that the technology can be loaded without errors."""
    tech = pdk.si_220nm_passive_pdk()
    pf.config.default_technology = tech
    print(
        f"Loaded technology '{tech.name}' version"
        f"{tech.version} with {len(tech.layers)} layers"
        f" and {len(tech.ports)} port specs."
    )


# ---------------------------------------------------------------------------
# LiveViewer test
# ---------------------------------------------------------------------------


def test_technology_loaded_in_liveviewer():
    """Test that the LiveViewer finds this PDK and loads its technology."""
    installed = {p["name"]: p for p in live_viewer_pdks.installed()}
    assert "cornerstone-forge" in installed, "PDK not discovered by the LiveViewer"
    pdk_info = installed["cornerstone-forge"]
    assert pdk_info["compatible"], pdk_info["reason"]

    result = live_viewer_pdks.load(pdk_info)
    assert "error" not in result, result.get("error")
    assert result["technology"] == si_220nm_passive_pdk().name


# ---------------------------------------------------------------------------
# Export test
# ---------------------------------------------------------------------------


def test_export(tmp_path):
    """Test that the technology can be exported and re-imported without loss of information."""
    tech = pdk.si_220nm_passive_pdk()
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
    """Test that the strip_1310nm port spec has the expected parameters.

    Note: spec.width is the port simulation area width, not the waveguide
    width, which instead comes from the first path_profiles entry.
    """
    spec = port_specs["strip_1310nm"]
    assert spec.width == pytest.approx(0.6804)
    assert spec.path_profiles[0][0] == pytest.approx(0.4)  # wg_lf (strip core) width
    assert spec.num_modes == 2
    assert spec.target_neff == pytest.approx(2.52)


def test_rib_1310nm_port_spec():
    """Test that the rib_1310nm_TE port spec has the expected parameters.

    Note: spec.width is the port simulation area width, not the waveguide
    width, which instead comes from the first path_profiles entry.
    """
    spec = port_specs["rib_1310nm_TE"]
    assert spec.width == pytest.approx(2.8556)
    assert spec.path_profiles[0][0] == pytest.approx(0.4)  # wg_lf (rib core) width
    assert spec.path_profiles[1][0] == pytest.approx(10.4)  # rib_slab width
    assert spec.num_modes == 1
    assert spec.target_neff == pytest.approx(2.52)
    assert spec.polarization == "TE"


def test_strip_1550nm_port_spec():
    """Test that the strip_1550nm port spec has the expected parameters.

    Note: spec.width is the port simulation area width, not the waveguide
    width, which instead comes from the first path_profiles entry.
    """
    spec = port_specs["strip_1550nm"]
    assert spec.width == pytest.approx(0.7937)
    assert spec.path_profiles[0][0] == pytest.approx(0.45)  # wg_lf (strip core) width
    assert spec.num_modes == 2
    assert spec.target_neff == pytest.approx(2.38)


def test_rib_1550nm_port_spec():
    """Test that the rib_1550nm_TE port spec has the expected parameters.

    Note: spec.width is the port simulation area width, not the waveguide
    width, which instead comes from the first path_profiles entry.
    """
    spec = port_specs["rib_1550nm_TE"]
    assert spec.width == pytest.approx(1.2999)
    assert spec.path_profiles[0][0] == pytest.approx(0.45)  # wg_lf (rib core) width
    assert spec.path_profiles[1][0] == pytest.approx(10.45)  # rib_slab width
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
    tech = si_220nm_passive_pdk()
    assert tech.name == "cornerstone-si_220nm_passive-forge"


def test_technology_version():
    """Test that the technology version string is set to the subpackage version."""
    tech = si_220nm_passive_pdk()
    assert tech.version == pdk.__version__


def test_technology_has_layers():
    """Test that the technology exposes all PDK layers."""
    tech = si_220nm_passive_pdk()
    for layer_name in _layer_specs:
        assert layer_name in tech.layers, f"Layer '{layer_name}' missing from technology"


def test_technology_has_ports():
    """Test that the technology exposes all port specs."""
    tech = si_220nm_passive_pdk()
    for port_name in port_specs:
        assert port_name in tech.ports, f"Port spec '{port_name}' missing from technology"


def test_technology_substrate_adds_two_extrusion():
    """Test that include_substrate=True adds exactly two extrusions to the stack."""
    tech_no_sub = si_220nm_passive_pdk(include_substrate=False)
    tech_with_sub = si_220nm_passive_pdk(include_substrate=True)
    assert len(tech_with_sub.extrusion_specs) == len(tech_no_sub.extrusion_specs) + 2


def test_technology_export_roundtrip(tmp_path):
    """Test that the technology survives a write/load roundtrip without data loss."""
    tech = si_220nm_passive_pdk()
    tech_file = tmp_path / "tech.phf"
    pf.write_phf(tech_file, tech)
    tech_loaded = pf.load_phf(tech_file)["technologies"][0]
    assert tech_loaded == tech


def test_area_outside_of_layout_is_air():
    """Test that the area outside of the layout is assigned the background medium."""
    # Test that the background is air
    tech = si_220nm_passive_pdk()
    assert tech.background_medium.permittivity == 1.0

    # Test that a point far outside the layout is assigned the background medium
    # Gaussian port will return an error if it intersects multiple media,
    # so we place it far from the layout to ensure it only intersects the background medium
    c2 = pf.Component("test_component_2", technology=tech)
    c2.add_reference(
        pf.parametric.straight(technology=tech, port_spec=tech.ports["rib_1550nm_TE"], length=5.0)
    )
    gaussian_port_x = pf.GaussianPort(
        center=(
            -5.0,
            0.0,
            0.0,
        ),
        input_vector=(1, 0, 0),
        waist_radius=2.0,
        polarization_angle=0,  # for TE mode, in this case
    )
    gaussian_port_y = pf.GaussianPort(
        center=(
            0.0,
            -10.0,
            0.0,
        ),
        input_vector=(0, 1, 0),
        waist_radius=2.0,
        polarization_angle=0,  # for TE mode, in this case
    )
    gaussian_port_z = pf.GaussianPort(
        center=(
            0.0,
            0.0,
            +5.0,
        ),
        input_vector=(0, 0, 1),
        waist_radius=2.0,
        polarization_angle=0,  # for TE mode, in this case
    )

    c2.add_port([gaussian_port_x, gaussian_port_y, gaussian_port_z])
    pf.tidy3d_plot(c2, x=0.2)
