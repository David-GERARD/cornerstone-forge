"""O-band (1310 nm) component wrappers for the SI 220nm passive PDK."""

import photonforge as pf
from _utils import _import_component_with_ports

components = {}


####################################################################
def SOI220nm_1310nm_TE_RIB_2x1_MMI() -> pf.Component:
    """2x1 MMI splitter, TE RIB waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_RIB_2x1_MMI")


components["SOI220nm_1310nm_TE_RIB_2x1_MMI"] = SOI220nm_1310nm_TE_RIB_2x1_MMI()


####################################################################
def SOI220nm_1310nm_TE_RIB_2x2_MMI() -> pf.Component:
    """2x2 MMI splitter, TE RIB waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_RIB_2x2_MMI")


components["SOI220nm_1310nm_TE_RIB_2x2_MMI"] = SOI220nm_1310nm_TE_RIB_2x2_MMI()


####################################################################
def SOI220nm_1310nm_TE_RIB_90_Degree_Bend() -> pf.Component:
    """90-degree bend, TE RIB waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_RIB_90_Degree_Bend")


components["SOI220nm_1310nm_TE_RIB_90_Degree_Bend"] = SOI220nm_1310nm_TE_RIB_90_Degree_Bend()


####################################################################
def SOI220nm_1310nm_TE_RIB_Grating_Coupler() -> pf.Component:
    """Grating coupler, TE RIB waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_RIB_Grating_Coupler")


components["SOI220nm_1310nm_TE_RIB_Grating_Coupler"] = SOI220nm_1310nm_TE_RIB_Grating_Coupler()


####################################################################
def SOI220nm_1310nm_TE_RIB_Waveguide() -> pf.Component:
    """Straight waveguide, TE RIB, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_RIB_Waveguide")


components["SOI220nm_1310nm_TE_RIB_Waveguide"] = SOI220nm_1310nm_TE_RIB_Waveguide()


####################################################################
def SOI220nm_1310nm_TE_RIB_Waveguide_Crossing() -> pf.Component:
    """Waveguide crossing, TE RIB, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_RIB_Waveguide_Crossing")


components["SOI220nm_1310nm_TE_RIB_Waveguide_Crossing"] = (
    SOI220nm_1310nm_TE_RIB_Waveguide_Crossing()
)


####################################################################
def SOI220nm_1310nm_TE_STRIP_2x1_MMI() -> pf.Component:
    """2x1 MMI splitter, TE STRIP waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_2x1_MMI")


components["SOI220nm_1310nm_TE_STRIP_2x1_MMI"] = SOI220nm_1310nm_TE_STRIP_2x1_MMI()


####################################################################
def SOI220nm_1310nm_TE_STRIP_2x2_MMI() -> pf.Component:
    """2x2 MMI splitter, TE STRIP waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_2x2_MMI")


components["SOI220nm_1310nm_TE_STRIP_2x2_MMI"] = SOI220nm_1310nm_TE_STRIP_2x2_MMI()


####################################################################
def SOI220nm_1310nm_TE_STRIP_90_Degree_Bend() -> pf.Component:
    """90-degree bend, TE STRIP waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_90_Degree_Bend")


components["SOI220nm_1310nm_TE_STRIP_90_Degree_Bend"] = SOI220nm_1310nm_TE_STRIP_90_Degree_Bend()


####################################################################
def SOI220nm_1310nm_TE_STRIP_Grating_Coupler() -> pf.Component:
    """Grating coupler, TE STRIP waveguide, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_Grating_Coupler")


components["SOI220nm_1310nm_TE_STRIP_Grating_Coupler"] = SOI220nm_1310nm_TE_STRIP_Grating_Coupler()


####################################################################
def SOI220nm_1310nm_TE_STRIP_Waveguide() -> pf.Component:
    """Straight waveguide, TE STRIP, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_Waveguide")


components["SOI220nm_1310nm_TE_STRIP_Waveguide"] = SOI220nm_1310nm_TE_STRIP_Waveguide()


####################################################################
def SOI220nm_1310nm_TE_STRIP_Waveguide_Crossing() -> pf.Component:
    """Waveguide crossing, TE STRIP, 1310 nm."""
    return _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_Waveguide_Crossing")


components["SOI220nm_1310nm_TE_STRIP_Waveguide_Crossing"] = (
    SOI220nm_1310nm_TE_STRIP_Waveguide_Crossing()
)


####################################################################
####################################################################
component_names = list(components.keys())

if __name__ == "__main__":
    from technology import csforge_si_220nm_pdk

    tech = csforge_si_220nm_pdk()
    pf.config.default_technology = tech

    for name in component_names:
        print(f"Component: {name}")
        c = components[name]
        print(f"  Ports: {list(c.ports.keys())}")
