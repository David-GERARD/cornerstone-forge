"""Tests for CSV-based DataModel loading and integration with PDK components.

These tests verify that:
- :func:`_load_data_model` correctly parses S-parameter CSV files.
- The resulting :class:`pf.DataModel` is registered on each applicable
  component as the ``"Data"`` model and is set as the active model.
- S-matrix data is physically consistent: reciprocity (S_ij = S_ji) holds
  across all frequencies, and 2x2 MMI components satisfy their expected
  structural symmetry (S_31 = S_42, S_41 = S_32).
"""

import csforge_si_220nm_passive as pdk
import numpy as np
import photonforge as pf
import pytest
from csforge_si_220nm_passive._utils import _load_data_model

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

_2PORT_NAMES = ["P1", "P2"]
_3PORT_NAMES = ["P1", "P2", "P3"]
_4PORT_NAMES = ["P1", "P2", "P3", "P4"]

# Components that have a matching S-parameter CSV and whose port count
# matches the CSV port count (grating couplers are excluded because the
# vertical_te port is filtered out of the component, leaving only 1 optical
# port while the CSV contains a 2-port model).
_COMPONENTS_WITH_DATA_MODEL = [
    # O-band RIB
    ("SOI220nm_1310nm_TE_RIB_2x1_MMI", _3PORT_NAMES),
    ("SOI220nm_1310nm_TE_RIB_2x2_MMI", _4PORT_NAMES),
    ("SOI220nm_1310nm_TE_RIB_90_Degree_Bend", _2PORT_NAMES),
    ("SOI220nm_1310nm_TE_RIB_Waveguide_Crossing", _4PORT_NAMES),
    # O-band STRIP
    ("SOI220nm_1310nm_TE_STRIP_2x1_MMI", _3PORT_NAMES),
    ("SOI220nm_1310nm_TE_STRIP_2x2_MMI", _4PORT_NAMES),
    ("SOI220nm_1310nm_TE_STRIP_90_Degree_Bend", _2PORT_NAMES),
    ("SOI220nm_1310nm_TE_STRIP_Waveguide_Crossing", _4PORT_NAMES),
    # C-band RIB
    ("SOI220nm_1550nm_TE_RIB_2x1_MMI", _3PORT_NAMES),
    ("SOI220nm_1550nm_TE_RIB_2x2_MMI", _4PORT_NAMES),
    ("SOI220nm_1550nm_TE_RIB_90_Degree_Bend", _2PORT_NAMES),
    ("SOI220nm_1550nm_TE_RIB_Waveguide_Crossing", _4PORT_NAMES),
    # C-band STRIP
    ("SOI220nm_1550nm_TE_STRIP_2x1_MMI", _3PORT_NAMES),
    ("SOI220nm_1550nm_TE_STRIP_2x2_MMI", _4PORT_NAMES),
    ("SOI220nm_1550nm_TE_STRIP_90_Degree_Bend", _2PORT_NAMES),
    ("SOI220nm_1550nm_TE_STRIP_Waveguide_Crossing", _4PORT_NAMES),
]

_2X2_MMI_NAMES = [name for name, _ in _COMPONENTS_WITH_DATA_MODEL if "2x2_MMI" in name]


@pytest.fixture(scope="module")
def tech() -> pf.Technology:
    """Build the PDK technology once per module and set it as default."""
    t = pdk.csforge_si_220nm_pdk()
    pf.config.default_technology = t
    return t


# ---------------------------------------------------------------------------
# _load_data_model unit tests
# ---------------------------------------------------------------------------


def test_load_data_model_missing_csv_raises():
    """FileNotFoundError is raised when the CSV does not exist."""
    with pytest.raises(FileNotFoundError, match="S-parameter CSV not found"):
        _load_data_model("nonexistent_component_xyz", _2PORT_NAMES)


@pytest.mark.parametrize("component_name,port_names", _COMPONENTS_WITH_DATA_MODEL)
def test_load_data_model_returns_data_model(component_name, port_names):
    """_load_data_model returns a pf.DataModel instance for every valid CSV."""
    dm = _load_data_model(component_name, port_names)
    assert isinstance(dm, pf.DataModel)


@pytest.mark.parametrize("component_name,port_names", _COMPONENTS_WITH_DATA_MODEL)
def test_data_model_key_count(component_name, port_names):
    """DataModel contains N² S-parameter keys for an N-port component."""
    dm = _load_data_model(component_name, port_names)
    n_ports = len(port_names)
    assert len(dm.keys) == n_ports**2, (
        f"{component_name}: expected {n_ports**2} keys, got {len(dm.keys)}"
    )


@pytest.mark.parametrize("component_name,port_names", _COMPONENTS_WITH_DATA_MODEL)
def test_data_model_port_keys_use_component_names(component_name, port_names):
    """All S-parameter keys reference the supplied component port names."""
    dm = _load_data_model(component_name, port_names)
    expected_port_strs = {f"{p}@0" for p in port_names}
    for in_port, out_port in dm.keys:
        assert in_port in expected_port_strs, (
            f"{component_name}: unexpected in-port key '{in_port}'"
        )
        assert out_port in expected_port_strs, (
            f"{component_name}: unexpected out-port key '{out_port}'"
        )


@pytest.mark.parametrize("component_name,port_names", _COMPONENTS_WITH_DATA_MODEL)
def test_data_model_reciprocity(component_name, port_names):
    """S_ij ≈ S_ji for all port pairs (reciprocity of passive optical device).

    Uses ``atol=2e-2`` to accommodate FDTD numerical noise: symmetric devices
    (2x2 MMI, bend, crossing) achieve exact reciprocity, while 2x1 MMI data
    can differ by up to ~1.3% between independent port-excitation runs.
    """
    dm = _load_data_model(component_name, port_names)
    s_arr = dm.s_array  # shape (N_params, N_freqs)
    keys = dm.keys  # (in_port, out_port) -> flat index

    for in_port, out_port in keys:
        s_ij = s_arr[keys[(in_port, out_port)], :]
        s_ji = s_arr[keys[(out_port, in_port)], :]
        assert np.allclose(s_ij, s_ji, atol=2e-2), (
            f"{component_name}: reciprocity violated for "
            f"({in_port!r}, {out_port!r}): max diff = "
            f"{np.max(np.abs(s_ij - s_ji)):.2e}"
        )


# ---------------------------------------------------------------------------
# 2x2 MMI structural symmetry tests
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("component_name", _2X2_MMI_NAMES)
def test_2x2_mmi_structural_symmetry(component_name):
    """2x2 MMI satisfies device mirror-symmetry: S_31=S_42 and S_41=S_32.

    A 2x2 MMI is symmetric about the axis along its length, so the
    transmission from port 1 to port 3 equals the transmission from port 2
    to port 4, and similarly for the cross-coupling paths.
    """
    dm = _load_data_model(component_name, _4PORT_NAMES)
    s_arr = dm.s_array
    keys = dm.keys

    # S_31: in=P1, out=P3  |  S_42: in=P2, out=P4
    s_31 = s_arr[keys[("P1@0", "P3@0")], :]
    s_42 = s_arr[keys[("P2@0", "P4@0")], :]
    assert np.allclose(s_31, s_42, atol=1e-4), (
        f"{component_name}: S_31 ≠ S_42 (max diff = {np.max(np.abs(s_31 - s_42)):.2e})"
    )

    # S_41: in=P1, out=P4  |  S_32: in=P2, out=P3
    s_41 = s_arr[keys[("P1@0", "P4@0")], :]
    s_32 = s_arr[keys[("P2@0", "P3@0")], :]
    assert np.allclose(s_41, s_32, atol=1e-4), (
        f"{component_name}: S_41 ≠ S_32 (max diff = {np.max(np.abs(s_41 - s_32)):.2e})"
    )


# ---------------------------------------------------------------------------
# Component integration tests
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("name", [name for name, _ in _COMPONENTS_WITH_DATA_MODEL])
def test_component_has_data_model(tech, name):
    """Each applicable component exposes a 'Data' model."""
    c = pdk.component(name, technology=tech)
    assert "Data" in c.models, f"{name}: 'Data' model not found in {list(c.models.keys())}"
    assert isinstance(c.models["Data"], pf.DataModel)


@pytest.mark.parametrize("name", [name for name, _ in _COMPONENTS_WITH_DATA_MODEL])
def test_data_model_is_active(tech, name):
    """The 'Data' model is the active model for each applicable component."""
    c = pdk.component(name, technology=tech)
    assert c.active_model.__class__.__name__ == "DataModel", (
        f"{name}: active model is {c.active_model.__class__.__name__!r}, expected 'DataModel'"
    )
