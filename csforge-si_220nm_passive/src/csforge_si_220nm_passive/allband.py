"""Band-agnostic component wrappers for the SI 220nm passive PDK."""

import photonforge as pf

from ._utils import _import_component_with_ports
from .parametric.floorplan import (
    floorplan,
    floorplan_5_5mm_x_4_9mm,
    floorplan_11_47mm_x_4_9mm,
)
from .technology import csforge_si_220nm_pdk

components = {
    "floorplan": floorplan(tech=csforge_si_220nm_pdk()),
    "floorplan_11_47mm_x_4_9mm": floorplan_11_47mm_x_4_9mm(tech=csforge_si_220nm_pdk()),
    "floorplan_5_5mm_x_4_9mm": floorplan_5_5mm_x_4_9mm(tech=csforge_si_220nm_pdk()),
}


####################################################################
def Cell0_SOI220_Full_1550nm_Packaging_Template() -> pf.Component:
    """2x1 MMI splitter, TE RIB waveguide, 1310 nm."""
    return _import_component_with_ports(
        "Cell0_SOI220_Full_1550nm_Packaging_Template", csforge_si_220nm_pdk()
    )


components["Cell0_SOI220_Full_1550nm_Packaging_Template"] = (
    Cell0_SOI220_Full_1550nm_Packaging_Template()
)

####################################################################
####################################################################
component_names = list(components.keys())
