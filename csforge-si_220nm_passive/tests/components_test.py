"""Tests for the csforge_si_220nm_passive component functions."""

import csforge_si_220nm_passive as pdk
import photonforge as pf
import pytest

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _port_names(component: pf.Component) -> list[str]:
    """Return sorted port names for *component*."""
    return sorted(component.ports.keys())


@pytest.fixture(scope="module")
def load_technology() -> None:
    """Load the technology once for all tests."""
    tech = pdk.csforge_si_220nm_pdk()
    pf.config.default_technology = tech


# ---------------------------------------------------------------------------
# Component catalogue
# ---------------------------------------------------------------------------


def test_components(load_technology):
    """Test that all components can be instantiated without errors."""
    for name in pdk.component_names:
        component = pdk.components[name]
        assert isinstance(component, pf.Component), f"{name} did not return a Component"


def test_oband_components(load_technology):
    """Test that all O-band components can be instantiated without errors."""
    for name in pdk.oband_component_names:
        component = pdk.components[name]
        assert isinstance(component, pf.Component), f"{name} did not return a Component"


def test_cband_components(load_technology):
    """Test that all C-band components can be instantiated without errors."""
    for name in pdk.cband_component_names:
        component = pdk.components[name]
        assert isinstance(component, pf.Component), f"{name} did not return a Component"


def test_allband_components(load_technology):
    """Test that all band-agnostic components can be instantiated without errors."""
    for name in pdk.allband_component_names:
        component = pdk.components[name]
        assert isinstance(component, pf.Component), f"{name} did not return a Component"


def test_component_names_non_empty(load_technology):
    """Test that the component catalogue contains at least one entry."""
    assert len(pdk.component_names) > 0, "component_names must not be empty"


def test_oband_and_cband_and_allband_disjoint(load_technology):
    """Test that O-band, C-band, and All-band catalogues share no component names."""
    overlap = (
        set(pdk.oband_component_names)
        & set(pdk.cband_component_names)
        & set(pdk.allband_component_names)
    )
    assert overlap == set(), f"Bands share component names: {overlap}"


def test_all_components_covered(load_technology):
    """Test that the combined catalogue equals oband + cband + allband."""
    combined = set(
        pdk.oband_component_names + pdk.cband_component_names + pdk.allband_component_names
    )
    assert combined == set(pdk.component_names)


# ---------------------------------------------------------------------------
# Naming convention
# ---------------------------------------------------------------------------

_OBAND_PREFIX = "SOI220nm_1310nm_"
_CBAND_PREFIX = "SOI220nm_1550nm_"


def test_oband_naming_convention(load_technology):
    """Test that all O-band names start with the 1310 nm prefix."""
    for name in pdk.oband_component_names:
        assert name.startswith(_OBAND_PREFIX), (
            f"O-band component '{name}' does not start with '{_OBAND_PREFIX}'"
        )


def test_cband_naming_convention(load_technology):
    """Test that all C-band names start with the 1550 nm prefix."""
    for name in pdk.cband_component_names:
        assert name.startswith(_CBAND_PREFIX), (
            f"C-band component '{name}' does not start with '{_CBAND_PREFIX}'"
        )


# ---------------------------------------------------------------------------
# Port counts per component type
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("name", [n for n in pdk.component_names if "2x1_MMI" in n])
def test_2x1_mmi_has_three_ports(name: str):
    """Test that every 2x1 MMI has exactly three optical ports."""
    component = pdk.components[name]
    assert len(component.ports) == 3, f"{name} expected 3 ports, got {len(component.ports)}"


@pytest.mark.parametrize("name", [n for n in pdk.component_names if "2x2_MMI" in n])
def test_2x2_mmi_has_four_ports(name: str):
    """Test that every 2x2 MMI has exactly four optical ports."""
    component = pdk.components[name]
    assert len(component.ports) == 4, f"{name} expected 4 ports, got {len(component.ports)}"


@pytest.mark.parametrize("name", [n for n in pdk.component_names if "90_Degree_Bend" in n])
def test_bend_has_two_ports(name: str):
    """Test that every 90-degree bend has exactly two ports."""
    component = pdk.components[name]
    assert len(component.ports) == 2, f"{name} expected 2 ports, got {len(component.ports)}"


@pytest.mark.parametrize("name", [n for n in pdk.component_names if "Waveguide_Crossing" in n])
def test_crossing_has_four_ports(name: str):
    """Test that every waveguide crossing has exactly four ports."""
    component = pdk.components[name]
    assert len(component.ports) == 4, f"{name} expected 4 ports, got {len(component.ports)}"


@pytest.mark.parametrize(
    "name",
    [n for n in pdk.component_names if "Waveguide" in n and "Crossing" not in n],
)
def test_waveguide_has_two_ports(name: str):
    """Test that every straight waveguide has exactly two ports."""
    component = pdk.components[name]
    assert len(component.ports) == 2, f"{name} expected 2 ports, got {len(component.ports)}"


@pytest.mark.parametrize("name", [n for n in pdk.component_names if "Grating_Coupler" in n])
def test_grating_coupler_has_one_port(name: str):
    """Test that every grating coupler has exactly one port."""
    component = pdk.components[name]
    assert len(component.ports) == 1, f"{name} expected 1 port, got {len(component.ports)}"
