"""This module defines floorplan components for the SI 220nm passive PDK."""

import photonforge as pf
import photonforge.typing as pft


@pf.parametric_component
def floorplan(
    x_width_mm: pft.PositiveFloat = 11.47,
    y_width_mm: pft.PositiveFloat = 4.9,
    position: pft.Coordinate = (0.0, 0.0),
    tech: pf.Technology | None = None,
) -> pf.Component:
    """Floorplan component for the SI 220nm passive PDK.

    Args:
        x_width_mm: Width of the floorplan in the x direction, in millimeters.
        y_width_mm: Width of the floorplan in the y direction, in millimeters.
        position: Position of the bottom-left corner of the floorplan, in microns.
        tech: The technology to use for the floorplan.

    Returns:
        A Component representing the floorplan.

    """
    layers = pf.config.default_technology.layers if tech is None else tech.layers

    if "FloorPlan" not in layers:
        raise ValueError("FloorPlan layer not found in technology layers.")

    c = pf.Component(technology=tech)
    c.add(
        "FloorPlan",
        pf.Rectangle(position, (x_width_mm * 1000, y_width_mm * 1000)),
    )
    return c


def floorplan_11_47mm_x_4_9mm(
    position: pft.Coordinate = (0.0, 0.0),
    tech: pf.Technology | None = None,
) -> pf.Component:
    """11.47mm x 4.9mm floorplan component for the SI 220nm passive PDK.

    Args:
        position: Position of the bottom-left corner of the floorplan, in microns.
        tech: The technology to use for the floorplan.

    Returns:
        A Component representing the floorplan.

    """
    return floorplan(x_width_mm=11.47, y_width_mm=4.9, position=position, tech=tech)


def floorplan_5_5mm_x_4_9mm(
    position: pft.Coordinate = (0.0, 0.0),
    tech: pf.Technology | None = None,
) -> pf.Component:
    """5.5mm x 4.9mm floorplan component for the SI 220nm passive PDK.

    Args:
        position: Position of the bottom-left corner of the floorplan, in microns.
        tech: The technology to use for the floorplan.

    Returns:
        A Component representing the floorplan.

    """
    return floorplan(x_width_mm=5.5, y_width_mm=4.9, position=position, tech=tech)
