"""O-band (1310 nm) component wrappers for the SI 220nm passive PDK."""

import photonforge as pf

from ._utils import _import_component_with_ports

components = {}


####################################################################
def SOI220nm_1310nm_TE_RIB_2x1_MMI(tech: pf.Technology) -> pf.Component:
    """2x1 MMI splitter, TE RIB waveguide, 1310 nm."""
    mmi = _import_component_with_ports("SOI220nm_1310nm_TE_RIB_2x1_MMI", tech)
    ports = list(mmi.ports.items())
    mmi.add_model(
        pf.Tidy3DModel(port_symmetries=[(ports[0], ports[1]), (ports[0], ports[2])]), "Tidy3D"
    )
    return mmi


components["SOI220nm_1310nm_TE_RIB_2x1_MMI"] = SOI220nm_1310nm_TE_RIB_2x1_MMI


####################################################################
def SOI220nm_1310nm_TE_RIB_2x2_MMI(tech: pf.Technology) -> pf.Component:
    """2x2 MMI splitter, TE RIB waveguide, 1310 nm."""
    mmi = _import_component_with_ports("SOI220nm_1310nm_TE_RIB_2x2_MMI", tech)
    ports = list(mmi.ports.items())
    mmi.add_model(
        pf.Tidy3DModel(
            port_symmetries=[
                (ports[0], ports[2]),
                (ports[0], ports[3]),
                (ports[1], ports[2]),
                (ports[1], ports[3]),
            ]
        ),
        "Tidy3D",
    )
    return mmi


components["SOI220nm_1310nm_TE_RIB_2x2_MMI"] = SOI220nm_1310nm_TE_RIB_2x2_MMI


####################################################################
def SOI220nm_1310nm_TE_RIB_90_Degree_Bend(tech: pf.Technology) -> pf.Component:
    """90-degree bend, TE RIB waveguide, 1310 nm."""
    bend = _import_component_with_ports("SOI220nm_1310nm_TE_RIB_90_Degree_Bend", tech)
    ports = list(bend.ports.items())
    bend.add_model(pf.Tidy3DModel(port_symmetries=[(ports[0], ports[1])]), "Tidy3D")
    return bend


components["SOI220nm_1310nm_TE_RIB_90_Degree_Bend"] = SOI220nm_1310nm_TE_RIB_90_Degree_Bend


####################################################################
def SOI220nm_1310nm_TE_RIB_Grating_Coupler(tech: pf.Technology) -> pf.Component:
    """Grating coupler, TE RIB waveguide, 1310 nm.

    Note:
        Model will be implemented when fiber ports are added to the component definition.

    """
    return _import_component_with_ports("SOI220nm_1310nm_TE_RIB_Grating_Coupler", tech)


components["SOI220nm_1310nm_TE_RIB_Grating_Coupler"] = SOI220nm_1310nm_TE_RIB_Grating_Coupler


####################################################################
def SOI220nm_1310nm_TE_RIB_Waveguide(tech: pf.Technology) -> pf.Component:
    """Straight waveguide, TE RIB, 1310 nm."""
    straight = _import_component_with_ports("SOI220nm_1310nm_TE_RIB_Waveguide", tech)
    ports = list(straight.ports.items())
    straight.add_model(pf.Tidy3DModel(port_symmetries=[(ports[0], ports[1])]), "Tidy3D")
    return straight


components["SOI220nm_1310nm_TE_RIB_Waveguide"] = SOI220nm_1310nm_TE_RIB_Waveguide


####################################################################
def SOI220nm_1310nm_TE_RIB_Waveguide_Crossing(tech: pf.Technology) -> pf.Component:
    """Waveguide crossing, TE RIB, 1310 nm."""
    crossing = _import_component_with_ports("SOI220nm_1310nm_TE_RIB_Waveguide_Crossing", tech)
    ports = list(crossing.ports.items())
    crossing.add_model(
        pf.Tidy3DModel(port_symmetries=[(ports[0], ports[2]), (ports[1], ports[3])]), "Tidy3D"
    )
    return crossing


components["SOI220nm_1310nm_TE_RIB_Waveguide_Crossing"] = SOI220nm_1310nm_TE_RIB_Waveguide_Crossing


####################################################################
def SOI220nm_1310nm_TE_STRIP_2x1_MMI(tech: pf.Technology) -> pf.Component:
    """2x1 MMI splitter, TE STRIP waveguide, 1310 nm."""
    mmi = _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_2x1_MMI", tech)
    ports = list(mmi.ports.items())
    mmi.add_model(
        pf.Tidy3DModel(port_symmetries=[(ports[0], ports[1]), (ports[0], ports[2])]), "Tidy3D"
    )
    return mmi


components["SOI220nm_1310nm_TE_STRIP_2x1_MMI"] = SOI220nm_1310nm_TE_STRIP_2x1_MMI


####################################################################
def SOI220nm_1310nm_TE_STRIP_2x2_MMI(tech: pf.Technology) -> pf.Component:
    """2x2 MMI splitter, TE STRIP waveguide, 1310 nm."""
    mmi = _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_2x2_MMI", tech)
    ports = list(mmi.ports.items())
    mmi.add_model(
        pf.Tidy3DModel(
            port_symmetries=[
                (ports[0], ports[2]),
                (ports[0], ports[3]),
                (ports[1], ports[2]),
                (ports[1], ports[3]),
            ]
        ),
        "Tidy3D",
    )
    return mmi


components["SOI220nm_1310nm_TE_STRIP_2x2_MMI"] = SOI220nm_1310nm_TE_STRIP_2x2_MMI


####################################################################
def SOI220nm_1310nm_TE_STRIP_90_Degree_Bend(tech: pf.Technology) -> pf.Component:
    """90-degree bend, TE STRIP waveguide, 1310 nm."""
    bend = _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_90_Degree_Bend", tech)
    ports = list(bend.ports.items())
    bend.add_model(pf.Tidy3DModel(port_symmetries=[(ports[0], ports[1])]), "Tidy3D")
    return bend


components["SOI220nm_1310nm_TE_STRIP_90_Degree_Bend"] = SOI220nm_1310nm_TE_STRIP_90_Degree_Bend


####################################################################
def SOI220nm_1310nm_TE_STRIP_Grating_Coupler(tech: pf.Technology) -> pf.Component:
    """Grating coupler, TE STRIP waveguide, 1310 nm.

    Note:
        Model will be implemented when fiber ports are added to the component definition.

    """
    return _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_Grating_Coupler", tech)


components["SOI220nm_1310nm_TE_STRIP_Grating_Coupler"] = SOI220nm_1310nm_TE_STRIP_Grating_Coupler


####################################################################
def SOI220nm_1310nm_TE_STRIP_Waveguide(tech: pf.Technology) -> pf.Component:
    """Straight waveguide, TE STRIP, 1310 nm."""
    straight = _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_Waveguide", tech)
    ports = list(straight.ports.items())
    straight.add_model(pf.Tidy3DModel(port_symmetries=[(ports[0], ports[1])]), "Tidy3D")
    return straight


components["SOI220nm_1310nm_TE_STRIP_Waveguide"] = SOI220nm_1310nm_TE_STRIP_Waveguide


####################################################################
def SOI220nm_1310nm_TE_STRIP_Waveguide_Crossing(tech: pf.Technology) -> pf.Component:
    """Waveguide crossing, TE STRIP, 1310 nm."""
    crossing = _import_component_with_ports("SOI220nm_1310nm_TE_STRIP_Waveguide_Crossing", tech)
    ports = list(crossing.ports.items())
    crossing.add_model(
        pf.Tidy3DModel(port_symmetries=[(ports[0], ports[2]), (ports[1], ports[3])]), "Tidy3D"
    )
    return crossing


components["SOI220nm_1310nm_TE_STRIP_Waveguide_Crossing"] = (
    SOI220nm_1310nm_TE_STRIP_Waveguide_Crossing
)


####################################################################
####################################################################
component_names = list(components.keys())

if __name__ == "__main__":
    from .technology import csforge_si_220nm_pdk

    tech = csforge_si_220nm_pdk()
    pf.config.default_technology = tech

    for name in component_names:
        print(f"Component: {name}")
        c = components[name]
        print(f"  Ports: {list(c.ports.keys())}")
