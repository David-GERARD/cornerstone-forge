"""C-band (1550 nm) component wrappers for the SI 220nm passive PDK."""

import photonforge as pf

from ._utils import _import_component_with_ports, _load_data_model

components = {}


####################################################################
def SOI220nm_1550nm_TE_RIB_2x1_MMI(tech: pf.Technology) -> pf.Component:
    """2x1 MMI splitter, TE RIB waveguide, 1550 nm."""
    mmi = _import_component_with_ports("SOI220nm_1550nm_TE_RIB_2x1_MMI", tech)
    mmi.add_model(pf.Tidy3DModel(port_symmetries=[("P1", "P3", "P2")]), "Tidy3D")
    mmi.add_model(
        _load_data_model("SOI220nm_1550nm_TE_RIB_2x1_MMI", list(mmi.ports.keys())), "Data"
    )
    return mmi


components["SOI220nm_1550nm_TE_RIB_2x1_MMI"] = SOI220nm_1550nm_TE_RIB_2x1_MMI


####################################################################
def SOI220nm_1550nm_TE_RIB_2x2_MMI(tech: pf.Technology) -> pf.Component:
    """2x2 MMI splitter, TE RIB waveguide, 1550 nm."""
    mmi = _import_component_with_ports("SOI220nm_1550nm_TE_RIB_2x2_MMI", tech)
    mmi.add_model(
        pf.Tidy3DModel(
            port_symmetries=[
                ("P3", "P4", "P1", "P2"),
            ]
        ),
        "Tidy3D",
    )
    mmi.add_model(
        _load_data_model("SOI220nm_1550nm_TE_RIB_2x2_MMI", list(mmi.ports.keys())), "Data"
    )
    return mmi


components["SOI220nm_1550nm_TE_RIB_2x2_MMI"] = SOI220nm_1550nm_TE_RIB_2x2_MMI


####################################################################
def SOI220nm_1550nm_TE_RIB_90_Degree_Bend(tech: pf.Technology) -> pf.Component:
    """90-degree bend, TE RIB waveguide, 1550 nm."""
    bend = _import_component_with_ports("SOI220nm_1550nm_TE_RIB_90_Degree_Bend", tech)
    bend.add_model(pf.Tidy3DModel(port_symmetries=[("P2", "P1")]), "Tidy3D")
    bend.add_model(
        _load_data_model("SOI220nm_1550nm_TE_RIB_90_Degree_Bend", list(bend.ports.keys())), "Data"
    )
    return bend


components["SOI220nm_1550nm_TE_RIB_90_Degree_Bend"] = SOI220nm_1550nm_TE_RIB_90_Degree_Bend


####################################################################
def SOI220nm_1550nm_TE_RIB_EBL_Apodised_Grating_Coupler(tech: pf.Technology) -> pf.Component:
    """EBL apodised grating coupler, TE RIB waveguide, 1550 nm."""
    # TODO: Add port symmetries once fiber ports are added to the component definition
    return _import_component_with_ports("SOI220nm_1550nm_TE_RIB_EBL_Apodised_Grating_Coupler", tech)


components["SOI220nm_1550nm_TE_RIB_EBL_Apodised_Grating_Coupler"] = (
    SOI220nm_1550nm_TE_RIB_EBL_Apodised_Grating_Coupler
)


####################################################################
def SOI220nm_1550nm_TE_RIB_Grating_Coupler(tech: pf.Technology) -> pf.Component:
    """Grating coupler, TE RIB waveguide, 1550 nm.

    Note:
        Model will be implemented when fiber ports are added to the component definition.

    """
    return _import_component_with_ports("SOI220nm_1550nm_TE_RIB_Grating_Coupler", tech)


components["SOI220nm_1550nm_TE_RIB_Grating_Coupler"] = SOI220nm_1550nm_TE_RIB_Grating_Coupler


####################################################################
def SOI220nm_1550nm_TE_RIB_MZI(tech: pf.Technology) -> pf.Component:
    """Mach-Zehnder interferometer, TE RIB waveguide, 1550 nm.

    Note:
        This component only has electrical ports as its optical ports are
        routed to gratted couplers.

    """
    return _import_component_with_ports("SOI220nm_1550nm_TE_RIB_MZI", tech)


components["SOI220nm_1550nm_TE_RIB_MZI"] = SOI220nm_1550nm_TE_RIB_MZI


####################################################################
def SOI220nm_1550nm_TE_RIB_Waveguide(tech: pf.Technology) -> pf.Component:
    """Straight waveguide, TE RIB, 1550 nm."""
    straight = _import_component_with_ports("SOI220nm_1550nm_TE_RIB_Waveguide", tech)
    straight.add_model(pf.Tidy3DModel(port_symmetries=[("P2", "P1")]), "Tidy3D")
    return straight


components["SOI220nm_1550nm_TE_RIB_Waveguide"] = SOI220nm_1550nm_TE_RIB_Waveguide


####################################################################
def SOI220nm_1550nm_TE_RIB_Waveguide_Crossing(tech: pf.Technology) -> pf.Component:
    """Waveguide crossing, TE RIB, 1550 nm."""
    crossing = _import_component_with_ports("SOI220nm_1550nm_TE_RIB_Waveguide_Crossing", tech)
    crossing.add_model(pf.Tidy3DModel(port_symmetries=[("P2", "P1", "P4", "P3")]), "Tidy3D")
    crossing.add_model(
        _load_data_model("SOI220nm_1550nm_TE_RIB_Waveguide_Crossing", list(crossing.ports.keys())),
        "Data",
    )
    return crossing


components["SOI220nm_1550nm_TE_RIB_Waveguide_Crossing"] = SOI220nm_1550nm_TE_RIB_Waveguide_Crossing


####################################################################
def SOI220nm_1550nm_TE_STRIP_2x1_MMI(tech: pf.Technology) -> pf.Component:
    """2x1 MMI splitter, TE STRIP waveguide, 1550 nm."""
    mmi = _import_component_with_ports("SOI220nm_1550nm_TE_STRIP_2x1_MMI", tech)
    mmi.add_model(pf.Tidy3DModel(port_symmetries=[("P1", "P3", "P2")]), "Tidy3D")
    mmi.add_model(
        _load_data_model("SOI220nm_1550nm_TE_STRIP_2x1_MMI", list(mmi.ports.keys())), "Data"
    )
    return mmi


components["SOI220nm_1550nm_TE_STRIP_2x1_MMI"] = SOI220nm_1550nm_TE_STRIP_2x1_MMI


####################################################################
def SOI220nm_1550nm_TE_STRIP_2x2_MMI(tech: pf.Technology) -> pf.Component:
    """2x2 MMI splitter, TE STRIP waveguide, 1550 nm."""
    mmi = _import_component_with_ports("SOI220nm_1550nm_TE_STRIP_2x2_MMI", tech)
    mmi.add_model(
        pf.Tidy3DModel(
            port_symmetries=[("P3", "P4", "P1", "P2")],
        ),
        "Tidy3D",
    )
    mmi.add_model(
        _load_data_model("SOI220nm_1550nm_TE_STRIP_2x2_MMI", list(mmi.ports.keys())), "Data"
    )
    return mmi


components["SOI220nm_1550nm_TE_STRIP_2x2_MMI"] = SOI220nm_1550nm_TE_STRIP_2x2_MMI


####################################################################
def SOI220nm_1550nm_TE_STRIP_90_Degree_Bend(tech: pf.Technology) -> pf.Component:
    """90-degree bend, TE STRIP waveguide, 1550 nm."""
    bend = _import_component_with_ports("SOI220nm_1550nm_TE_STRIP_90_Degree_Bend", tech)
    bend.add_model(pf.Tidy3DModel(port_symmetries=[("P2", "P1")]), "Tidy3D")
    bend.add_model(
        _load_data_model("SOI220nm_1550nm_TE_STRIP_90_Degree_Bend", list(bend.ports.keys())),
        "Data",
    )
    return bend


components["SOI220nm_1550nm_TE_STRIP_90_Degree_Bend"] = SOI220nm_1550nm_TE_STRIP_90_Degree_Bend


####################################################################
def SOI220nm_1550nm_TE_STRIP_Grating_Coupler(tech: pf.Technology) -> pf.Component:
    """Grating coupler, TE STRIP waveguide, 1550 nm.

    Note:
        Model will be implemented when fiber ports are added to the component definition.

    """
    # TODO: Add port symmetries once fiber ports are added to the component definition
    grating_coupler = _import_component_with_ports("SOI220nm_1550nm_TE_STRIP_Grating_Coupler", tech)
    grating_coupler.add_model(
        _load_data_model(
            "SOI220nm_1550nm_TE_STRIP_Grating_Coupler", list(grating_coupler.ports.keys())
        ),
        "Data",
    )
    return grating_coupler


components["SOI220nm_1550nm_TE_STRIP_Grating_Coupler"] = SOI220nm_1550nm_TE_STRIP_Grating_Coupler


####################################################################
def SOI220nm_1550nm_TE_STRIP_MZI(tech: pf.Technology) -> pf.Component:
    """Mach-Zehnder interferometer, TE STRIP waveguide, 1550 nm.

    Note:
        This component only has electrical ports as its optical ports are
        routed to gratted couplers.

    """
    return _import_component_with_ports("SOI220nm_1550nm_TE_STRIP_MZI", tech)


components["SOI220nm_1550nm_TE_STRIP_MZI"] = SOI220nm_1550nm_TE_STRIP_MZI


####################################################################
def SOI220nm_1550nm_TE_STRIP_Waveguide(tech: pf.Technology) -> pf.Component:
    """Straight waveguide, TE STRIP, 1550 nm."""
    straight = _import_component_with_ports("SOI220nm_1550nm_TE_STRIP_Waveguide", tech)
    straight.add_model(pf.Tidy3DModel(port_symmetries=[("P2", "P1")]), "Tidy3D")
    return straight


components["SOI220nm_1550nm_TE_STRIP_Waveguide"] = SOI220nm_1550nm_TE_STRIP_Waveguide


####################################################################
def SOI220nm_1550nm_TE_STRIP_Waveguide_Crossing(tech: pf.Technology) -> pf.Component:
    """Waveguide crossing, TE STRIP, 1550 nm."""
    crossing = _import_component_with_ports("SOI220nm_1550nm_TE_STRIP_Waveguide_Crossing", tech)
    crossing.add_model(pf.Tidy3DModel(port_symmetries=[("P2", "P1", "P4", "P3")]), "Tidy3D")
    crossing.add_model(
        _load_data_model(
            "SOI220nm_1550nm_TE_STRIP_Waveguide_Crossing", list(crossing.ports.keys())
        ),
        "Data",
    )
    return crossing


components["SOI220nm_1550nm_TE_STRIP_Waveguide_Crossing"] = (
    SOI220nm_1550nm_TE_STRIP_Waveguide_Crossing
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
