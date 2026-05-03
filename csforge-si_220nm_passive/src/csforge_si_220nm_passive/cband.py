"""C-band (1550 nm) component wrappers for the SI 220nm passive PDK."""

import photonforge as pf

from ._utils import _import_component_with_ports

components = {}


####################################################################
def SOI220nm_1550nm_TE_RIB_2x1_MMI() -> pf.Component:
    """2x1 MMI splitter, TE RIB waveguide, 1550 nm."""
    return _import_component_with_ports("SOI220nm_1550nm_TE_RIB_2x1_MMI")


components["SOI220nm_1550nm_TE_RIB_2x1_MMI"] = SOI220nm_1550nm_TE_RIB_2x1_MMI()


####################################################################
def SOI220nm_1550nm_TE_RIB_2x2_MMI() -> pf.Component:
    """2x2 MMI splitter, TE RIB waveguide, 1550 nm."""
    return _import_component_with_ports("SOI220nm_1550nm_TE_RIB_2x2_MMI")


components["SOI220nm_1550nm_TE_RIB_2x2_MMI"] = SOI220nm_1550nm_TE_RIB_2x2_MMI()


####################################################################
def SOI220nm_1550nm_TE_RIB_90_Degree_Bend() -> pf.Component:
    """90-degree bend, TE RIB waveguide, 1550 nm."""
    return _import_component_with_ports("SOI220nm_1550nm_TE_RIB_90_Degree_Bend")


components["SOI220nm_1550nm_TE_RIB_90_Degree_Bend"] = SOI220nm_1550nm_TE_RIB_90_Degree_Bend()


####################################################################
def SOI220nm_1550nm_TE_RIB_EBL_Apodised_Grating_Coupler() -> pf.Component:
    """EBL apodised grating coupler, TE RIB waveguide, 1550 nm."""
    return _import_component_with_ports("SOI220nm_1550nm_TE_RIB_EBL_Apodised_Grating_Coupler")


components["SOI220nm_1550nm_TE_RIB_EBL_Apodised_Grating_Coupler"] = (
    SOI220nm_1550nm_TE_RIB_EBL_Apodised_Grating_Coupler()
)


####################################################################
def SOI220nm_1550nm_TE_RIB_Grating_Coupler() -> pf.Component:
    """Grating coupler, TE RIB waveguide, 1550 nm."""
    return _import_component_with_ports("SOI220nm_1550nm_TE_RIB_Grating_Coupler")


components["SOI220nm_1550nm_TE_RIB_Grating_Coupler"] = SOI220nm_1550nm_TE_RIB_Grating_Coupler()


####################################################################
def SOI220nm_1550nm_TE_RIB_MZI() -> pf.Component:
    """Mach-Zehnder interferometer, TE RIB waveguide, 1550 nm."""
    return _import_component_with_ports("SOI220nm_1550nm_TE_RIB_MZI")


components["SOI220nm_1550nm_TE_RIB_MZI"] = SOI220nm_1550nm_TE_RIB_MZI()


####################################################################
def SOI220nm_1550nm_TE_RIB_Waveguide() -> pf.Component:
    """Straight waveguide, TE RIB, 1550 nm."""
    return _import_component_with_ports("SOI220nm_1550nm_TE_RIB_Waveguide")


components["SOI220nm_1550nm_TE_RIB_Waveguide"] = SOI220nm_1550nm_TE_RIB_Waveguide()


####################################################################
def SOI220nm_1550nm_TE_RIB_Waveguide_Crossing() -> pf.Component:
    """Waveguide crossing, TE RIB, 1550 nm."""
    return _import_component_with_ports("SOI220nm_1550nm_TE_RIB_Waveguide_Crossing")


components["SOI220nm_1550nm_TE_RIB_Waveguide_Crossing"] = (
    SOI220nm_1550nm_TE_RIB_Waveguide_Crossing()
)


####################################################################
def SOI220nm_1550nm_TE_STRIP_2x1_MMI() -> pf.Component:
    """2x1 MMI splitter, TE STRIP waveguide, 1550 nm."""
    return _import_component_with_ports("SOI220nm_1550nm_TE_STRIP_2x1_MMI")


components["SOI220nm_1550nm_TE_STRIP_2x1_MMI"] = SOI220nm_1550nm_TE_STRIP_2x1_MMI()


####################################################################
def SOI220nm_1550nm_TE_STRIP_2x2_MMI() -> pf.Component:
    """2x2 MMI splitter, TE STRIP waveguide, 1550 nm."""
    return _import_component_with_ports("SOI220nm_1550nm_TE_STRIP_2x2_MMI")


components["SOI220nm_1550nm_TE_STRIP_2x2_MMI"] = SOI220nm_1550nm_TE_STRIP_2x2_MMI()


####################################################################
def SOI220nm_1550nm_TE_STRIP_90_Degree_Bend() -> pf.Component:
    """90-degree bend, TE STRIP waveguide, 1550 nm."""
    return _import_component_with_ports("SOI220nm_1550nm_TE_STRIP_90_Degree_Bend")


components["SOI220nm_1550nm_TE_STRIP_90_Degree_Bend"] = SOI220nm_1550nm_TE_STRIP_90_Degree_Bend()


####################################################################
def SOI220nm_1550nm_TE_STRIP_Grating_Coupler() -> pf.Component:
    """Grating coupler, TE STRIP waveguide, 1550 nm."""
    return _import_component_with_ports("SOI220nm_1550nm_TE_STRIP_Grating_Coupler")


components["SOI220nm_1550nm_TE_STRIP_Grating_Coupler"] = SOI220nm_1550nm_TE_STRIP_Grating_Coupler()


####################################################################
def SOI220nm_1550nm_TE_STRIP_MZI() -> pf.Component:
    """Mach-Zehnder interferometer, TE STRIP waveguide, 1550 nm."""
    return _import_component_with_ports("SOI220nm_1550nm_TE_STRIP_MZI")


components["SOI220nm_1550nm_TE_STRIP_MZI"] = SOI220nm_1550nm_TE_STRIP_MZI()


####################################################################
def SOI220nm_1550nm_TE_STRIP_Waveguide() -> pf.Component:
    """Straight waveguide, TE STRIP, 1550 nm."""
    return _import_component_with_ports("SOI220nm_1550nm_TE_STRIP_Waveguide")


components["SOI220nm_1550nm_TE_STRIP_Waveguide"] = SOI220nm_1550nm_TE_STRIP_Waveguide()


####################################################################
def SOI220nm_1550nm_TE_STRIP_Waveguide_Crossing() -> pf.Component:
    """Waveguide crossing, TE STRIP, 1550 nm."""
    crossing = _import_component_with_ports("SOI220nm_1550nm_TE_STRIP_Waveguide_Crossing")
    ports = list(crossing.ports.items())
    crossing.add_model(
        pf.Tidy3DModel(port_symmetries=[(ports[0], ports[2]), (ports[1], ports[3])]), "Tidy3D"
    )
    return crossing


components["SOI220nm_1550nm_TE_STRIP_Waveguide_Crossing"] = (
    SOI220nm_1550nm_TE_STRIP_Waveguide_Crossing()
)

###################################################################
###################################################################
component_names = list(components.keys())

if __name__ == "__main__":
    from .technology import csforge_si_220nm_pdk

    tech = csforge_si_220nm_pdk()
    pf.config.default_technology = tech

    for name in component_names:
        print(f"Component: {name}")
        c = components[name]
        print(f"  Ports: {list(c.ports.keys())}")

    # import matplotlib.pyplot as plt
    # import numpy as np

    # crossing = SOI220nm_1550nm_TE_STRIP_Waveguide_Crossing()
    # s_matrix = crossing.s_matrix(pf.C_0 / np.linspace(1.4, 1.6, 21))
    # _ = pf.plot_s_matrix(s_matrix)

    # plt.show()

    components["SOI220nm_1550nm_TE_STRIP_Waveguide_Crossing"].write_gds(
        "SOI220nm_1550nm_TE_STRIP_Waveguide_Crossing.gds"
    )
