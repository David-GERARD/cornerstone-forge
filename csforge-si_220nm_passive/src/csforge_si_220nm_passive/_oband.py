"""O-band (1310 nm) component wrappers for the SI 220nm passive PDK."""

import photonforge as pf
from _utils import _import_component_with_ports

__all__ = [
    "SOI220nm_1310nm_TE_RIB_2x1_MMI",
    "SOI220nm_1310nm_TE_RIB_2x2_MMI",
    "SOI220nm_1310nm_TE_RIB_90_Degree_Bend",
    "SOI220nm_1310nm_TE_RIB_Grating_Coupler",
    "SOI220nm_1310nm_TE_RIB_Waveguide",
    "SOI220nm_1310nm_TE_RIB_Waveguide_Crossing",
    "SOI220nm_1310nm_TE_STRIP_2x1_MMI",
    "SOI220nm_1310nm_TE_STRIP_2x2_MMI",
    "SOI220nm_1310nm_TE_STRIP_90_Degree_Bend",
    "SOI220nm_1310nm_TE_STRIP_Grating_Coupler",
    "SOI220nm_1310nm_TE_STRIP_Waveguide",
    "SOI220nm_1310nm_TE_STRIP_Waveguide_Crossing",
]


def SOI220nm_1310nm_TE_RIB_2x1_MMI() -> pf.Component:
    """2x1 MMI splitter, TE RIB waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_RIB_2x1_MMI")


def SOI220nm_1310nm_TE_RIB_2x2_MMI() -> pf.Component:
    """2x2 MMI splitter, TE RIB waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_RIB_2x2_MMI")


def SOI220nm_1310nm_TE_RIB_90_Degree_Bend() -> pf.Component:
    """90-degree bend, TE RIB waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_RIB_90_Degree_Bend")


def SOI220nm_1310nm_TE_RIB_Grating_Coupler() -> pf.Component:
    """Grating coupler, TE RIB waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_RIB_Grating_Coupler")


def SOI220nm_1310nm_TE_RIB_Waveguide() -> pf.Component:
    """Straight waveguide, TE RIB, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_RIB_Waveguide")


def SOI220nm_1310nm_TE_RIB_Waveguide_Crossing() -> pf.Component:
    """Waveguide crossing, TE RIB, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_RIB_Waveguide_Crossing")


def SOI220nm_1310nm_TE_STRIP_2x1_MMI() -> pf.Component:
    """2x1 MMI splitter, TE STRIP waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_2x1_MMI")


def SOI220nm_1310nm_TE_STRIP_2x2_MMI() -> pf.Component:
    """2x2 MMI splitter, TE STRIP waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_2x2_MMI")


def SOI220nm_1310nm_TE_STRIP_90_Degree_Bend() -> pf.Component:
    """90-degree bend, TE STRIP waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_90_Degree_Bend")


def SOI220nm_1310nm_TE_STRIP_Grating_Coupler() -> pf.Component:
    """Grating coupler, TE STRIP waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_Grating_Coupler")


def SOI220nm_1310nm_TE_STRIP_Waveguide() -> pf.Component:
    """Straight waveguide, TE STRIP, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_Waveguide")


def SOI220nm_1310nm_TE_STRIP_Waveguide_Crossing() -> pf.Component:
    """Waveguide crossing, TE STRIP, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_Waveguide_Crossing")


if __name__ == "__main__":
    from photonforge.live_viewer import LiveViewer

    viewer = LiveViewer()

    comps = [
        SOI220nm_1310nm_TE_RIB_2x1_MMI(),
        SOI220nm_1310nm_TE_RIB_2x2_MMI(),
        SOI220nm_1310nm_TE_RIB_90_Degree_Bend(),
        SOI220nm_1310nm_TE_RIB_Grating_Coupler(),
        SOI220nm_1310nm_TE_RIB_Waveguide(),
        SOI220nm_1310nm_TE_RIB_Waveguide_Crossing(),
        SOI220nm_1310nm_TE_STRIP_2x1_MMI(),
        SOI220nm_1310nm_TE_STRIP_2x2_MMI(),
        SOI220nm_1310nm_TE_STRIP_90_Degree_Bend(),
        SOI220nm_1310nm_TE_STRIP_Grating_Coupler(),
        SOI220nm_1310nm_TE_STRIP_Waveguide(),
        SOI220nm_1310nm_TE_STRIP_Waveguide_Crossing(),
    ]

    for comp in comps:
        viewer(comp)
        input(f"Showing {comp.name!r} — press Enter for next...")
