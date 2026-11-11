"""Tests for the si_220nm_passive component catalogue and component() entry point."""

import photonforge as pf
import pytest

from cornerstone_forge import si_220nm_passive as pdk

# Old-convention cells emit a FutureWarning on every call; silence it outside the
# dedicated deprecation tests below (pytest.warns still captures it).
pytestmark = [
    pytest.mark.filterwarnings("ignore:PDK cell .* deprecated:FutureWarning"),
    pytest.mark.filterwarnings("ignore:PDK cell .* NOT an equivalent device:UserWarning"),
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def tech() -> pf.Technology:
    """Build the PDK technology once for the entire module and set it as default."""
    t = pdk.si_220nm_passive_pdk()
    pf.config.default_technology = t
    return t


# ---------------------------------------------------------------------------
# Component catalogue structure
# ---------------------------------------------------------------------------


def test_components_are_callable():
    """Test that every entry in the components dict is a callable factory."""
    for name, factory in pdk.components.items():
        assert callable(factory), f"components['{name}'] is not callable"


def test_component_names_non_empty():
    """Test that the component catalogue contains at least one entry."""
    assert len(pdk.component_names) > 0


def test_all_components_covered():
    """Test that component_names equals the union of all band catalogues."""
    combined = set(
        pdk.oband_component_names + pdk.cband_component_names + pdk.allband_component_names
    )
    assert combined == set(pdk.component_names)


def test_band_catalogues_are_pairwise_disjoint():
    """Test that no component name appears in more than one band catalogue."""
    oband = set(pdk.oband_component_names)
    cband = set(pdk.cband_component_names)
    allband = set(pdk.allband_component_names)
    overlaps = (oband & cband) | (oband & allband) | (cband & allband)
    assert overlaps == set(), f"Band catalogues share component names: {overlaps}"


# ---------------------------------------------------------------------------
# component() entry point
# ---------------------------------------------------------------------------


def test_component_unknown_name_raises(tech):
    """Test that requesting an unknown name raises ValueError."""
    with pytest.raises(ValueError, match="not found in the library"):
        pdk.component("does_not_exist", technology=tech)


def test_component_uses_explicit_technology(tech):
    """Test that component() accepts an explicit technology argument."""
    name = pdk.oband_component_names[0]
    c = pdk.component(name, technology=tech)
    assert isinstance(c, pf.Component)


def test_component_uses_default_technology(tech):
    """Test that component() falls back to pf.config.default_technology."""
    # tech fixture already set pf.config.default_technology
    name = pdk.oband_component_names[0]
    c = pdk.component(name)
    assert isinstance(c, pf.Component)


def test_component_warns_on_incompatible_technology():
    """Test that component() warns when the default technology name is not recognised.

    The warning is only issued when technology=None so the default is inspected.
    The subsequent component load raises KeyError (missing port specs), which is
    expected and suppressed here — only the warning is under test.
    """
    foreign_tech = pf.basic_technology()
    saved = pf.config.default_technology
    pf.config.default_technology = foreign_tech
    try:
        with pytest.warns(RuntimeWarning, match="does not seem compatible"):
            try:
                pdk.component(pdk.oband_component_names[0])
            except Exception:
                pass
    finally:
        pf.config.default_technology = saved


# ---------------------------------------------------------------------------
# Instantiation — all bands
# ---------------------------------------------------------------------------


def test_oband_components(tech):
    """Test that every O-band component instantiates as a pf.Component."""
    for name in pdk.oband_component_names:
        c = pdk.component(name, technology=tech)
        assert isinstance(c, pf.Component), f"{name} did not return a Component"


def test_cband_components(tech):
    """Test that every C-band component instantiates as a pf.Component."""
    for name in pdk.cband_component_names:
        c = pdk.component(name, technology=tech)
        assert isinstance(c, pf.Component), f"{name} did not return a Component"


def test_allband_components(tech):
    """Test that every band-agnostic component instantiates as a pf.Component."""
    for name in pdk.allband_component_names:
        c = pdk.component(name, technology=tech)
        assert isinstance(c, pf.Component), f"{name} did not return a Component"


# ---------------------------------------------------------------------------
# Naming conventions
# ---------------------------------------------------------------------------

_OBAND_PREFIXES = ("SOI220nm_1310nm_", "SOI220_1310nm_")  # (deprecated, SOI220P)
_CBAND_PREFIXES = ("SOI220nm_1550nm_", "SOI220_1550nm_")  # (deprecated, SOI220P)


def test_oband_naming_convention():
    """Test that all O-band names start with the 1310 nm prefix."""
    for name in pdk.oband_component_names:
        assert name.startswith(_OBAND_PREFIXES), (
            f"O-band component '{name}' does not start with any of {_OBAND_PREFIXES}"
        )


def test_cband_naming_convention():
    """Test that all C-band names start with the 1550 nm prefix."""
    for name in pdk.cband_component_names:
        assert name.startswith(_CBAND_PREFIXES), (
            f"C-band component '{name}' does not start with any of {_CBAND_PREFIXES}"
        )


# ---------------------------------------------------------------------------
# Port counts
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("name", [n for n in pdk.component_names if "2x1_MMI" in n])
def test_2x1_mmi_has_three_ports(tech, name: str):
    """Test that every 2x1 MMI has exactly three ports."""
    c = pdk.component(name, technology=tech)
    assert len(c.ports) == 3, f"{name}: expected 3 ports, got {len(c.ports)}"


@pytest.mark.parametrize("name", [n for n in pdk.component_names if "2x2_MMI" in n])
def test_2x2_mmi_has_four_ports(tech, name: str):
    """Test that every 2x2 MMI has exactly four ports."""
    c = pdk.component(name, technology=tech)
    assert len(c.ports) == 4, f"{name}: expected 4 ports, got {len(c.ports)}"


@pytest.mark.parametrize("name", [n for n in pdk.component_names if "90_Degree_Bend" in n])
def test_bend_has_two_ports(tech, name: str):
    """Test that every 90-degree bend has exactly two ports."""
    c = pdk.component(name, technology=tech)
    assert len(c.ports) == 2, f"{name}: expected 2 ports, got {len(c.ports)}"


@pytest.mark.parametrize("name", [n for n in pdk.component_names if "Waveguide_Crossing" in n])
def test_crossing_has_four_ports(tech, name: str):
    """Test that every waveguide crossing has exactly four ports."""
    c = pdk.component(name, technology=tech)
    assert len(c.ports) == 4, f"{name}: expected 4 ports, got {len(c.ports)}"


@pytest.mark.parametrize(
    "name",
    [n for n in pdk.component_names if "Waveguide" in n and "Crossing" not in n],
)
def test_waveguide_has_two_ports(tech, name: str):
    """Test that every straight waveguide has exactly two ports."""
    c = pdk.component(name, technology=tech)
    assert len(c.ports) == 2, f"{name}: expected 2 ports, got {len(c.ports)}"


@pytest.mark.parametrize(
    "name", [n for n in pdk.component_names if "Grating_Coupler" in n or "_GC" in n]
)
def test_grating_coupler_has_one_port(tech, name: str):
    """Test that every grating coupler has one waveguide port and one fiber port."""
    c = pdk.component(name, technology=tech)
    waveguide_ports = [p for p in c.ports if not p.startswith("FP")]
    fiber_ports = [p for p in c.ports if p.startswith("FP")]
    assert len(waveguide_ports) == 1, (
        f"{name}: expected 1 waveguide port, got {len(waveguide_ports)}"
    )
    assert len(fiber_ports) == 1, f"{name}: expected 1 fiber port, got {len(fiber_ports)}"


@pytest.mark.parametrize("name", [n for n in pdk.component_names if "_MZI" in n])
def test_mzi_has_two_electrical_ports(tech, name: str):
    """Test that every MZI exposes exactly two electrical ports named e1 and e2.

    Fiber ports (``FP*``, added for the vertical grating couplers used to
    probe the MZI arms) are excluded, since their count is device-specific.
    """
    c = pdk.component(name, technology=tech)
    non_fiber_ports = sorted(p for p in c.ports if not p.startswith("FP"))
    assert non_fiber_ports == ["P1", "P2"], f"{name}: expected ports P1, P2, got {non_fiber_ports}"


# ---------------------------------------------------------------------------
# Component models
# ---------------------------------------------------------------------------


def test_component_model_matches_optical_ports(tech):
    """Test that every component model's port symmetries match the component's optical ports."""
    for name in pdk.component_names:
        c = pdk.component(name, technology=tech)
        # Check if the component has a Tidy3D model
        if "Tidy3D" in c.models:
            model = c.models["Tidy3D"]
            # port_symmetries contains (name, Port) tuples from .items() — extract names only
            model_port_names = set()
            for pair in model.port_symmetries:
                for item in pair:
                    name_ = item[0] if isinstance(item, tuple) else item
                    model_port_names.add(name_)
            optical_ports = {p for p in c.ports if not p.startswith("e")}
            assert model_port_names == optical_ports, (
                f"{name}: Tidy3D model ports {model_port_names} != optical ports {optical_ports}"
            )


# ---------------------------------------------------------------------------
# Deprecation of the old Cornerstone naming convention (issue #23)
# ---------------------------------------------------------------------------

_NEW_GC = "SOI220_1550nm_TE_strip_apodized_GC_focusing_v1p0"
_DEPRECATED_NAMES = [
    n
    for n in pdk.component_names
    if n.startswith(("SOI220nm_", "Cell0_SOI220_Full_1550nm_Packaging_Template"))
]


def test_deprecated_names_non_empty():
    """Test that the old-convention cells are still available."""
    assert len(_DEPRECATED_NAMES) > 0


@pytest.mark.parametrize("name", _DEPRECATED_NAMES)
def test_old_naming_convention_cells_warn(tech, name: str):
    """Test that every cell using the old naming convention emits a deprecation warning."""
    with pytest.warns(FutureWarning, match="deprecated Cornerstone naming convention"):
        pdk.component(name, technology=tech)


def test_new_apodized_gc_is_registered():
    """Test that the new SOI220P apodized grating coupler is a C-band component."""
    assert _NEW_GC in pdk.cband_component_names


def test_new_apodized_gc_does_not_warn(tech, recwarn):
    """Test that the new SOI220P apodized grating coupler is not deprecated."""
    pdk.component(_NEW_GC, technology=tech)
    assert not [w for w in recwarn if issubclass(w.category, FutureWarning)]


def test_new_apodized_gc_ports_and_layers(tech):
    """Test the ports and layers of the new apodized grating coupler."""
    c = pdk.component(_NEW_GC, technology=tech)
    assert sorted(c.ports) == ["FPvertical_1", "P1"]
    assert isinstance(c.ports["FPvertical_1"], pf.FiberPort)
    assert c.ports["P1"].spec == tech.ports["strip_1550nm"]
    assert c.layers() == {(3, 0), (6, 0)}


# ---------------------------------------------------------------------------
# GDS layer 60 is now layer 6 (issue #23)
# ---------------------------------------------------------------------------


def test_no_component_uses_layer_60(tech):
    """Test that GDS layer 60 is remapped to layer 6 for every PDK component."""
    for name in pdk.component_names:
        c = pdk.component(name, technology=tech)
        assert (60, 0) not in c.layers(), f"{name} still has geometry on layer (60, 0)"


def test_ebl_grating_coupler_remapped_to_layer_6(tech):
    """Test that the legacy EBL grating coupler (layer 60 in its GDS) is loaded on layer 6."""
    c = pdk.component("SOI220nm_1550nm_TE_RIB_EBL_Apodised_Grating_Coupler", technology=tech)
    assert (6, 0) in c.layers()
    assert (60, 0) not in c.layers()


def test_layer_60_remap_warns_not_equivalent(tech):
    """Test that remapping layer 60 to layer 6 warns that the device is not equivalent."""
    with pytest.warns(UserWarning, match="NOT an equivalent device"):
        pdk.component("SOI220nm_1550nm_TE_RIB_EBL_Apodised_Grating_Coupler", technology=tech)


@pytest.mark.parametrize(
    "name",
    [n for n in pdk.component_names if n != "SOI220nm_1550nm_TE_RIB_EBL_Apodised_Grating_Coupler"],
)
def test_no_layer_remap_warning_without_layer_60(tech, recwarn, name: str):
    """Test that cells without layer-60 geometry do not emit the remap warning."""
    pdk.component(name, technology=tech)
    assert not [w for w in recwarn if "NOT an equivalent device" in str(w.message)]
