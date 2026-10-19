"""Defines a function to load components from the default PDK library."""

import warnings

import photonforge as pf

from .allband import component_names as allband_component_names
from .allband import components as allband_components
from .cband import component_names as cband_component_names
from .cband import components as cband_components
from .oband import component_names as oband_component_names
from .oband import components as oband_components

components = oband_components | cband_components | allband_components
component_names = oband_component_names + cband_component_names + allband_component_names


def component(cell_name: str, technology: pf.Technology | None = None, **kwargs) -> pf.Component:
    """Load a component from the default PDK library.

    Args:
        cell_name (str): Name of the component to load.
        technology (Technology): Technology for the created component.
        **kwargs: Additional keyword arguments to pass to the component factory function.

    Returns:
        Component: Component loaded from the default PDK library.

    Note:
        The available component names are listed in the module-level tuple
        ``component_names``.
    """
    if technology is None:
        technology = pf.config.default_technology
        if "cornerstone-si_220nm_passive-forge" not in technology.name:
            warnings.warn(
                f"Current default technology {technology.name} does not seem compatible with the "
                f"cornerstone-si_220nm_passive-forge component library",
                RuntimeWarning,
                2,
            )

    if cell_name not in components:
        raise ValueError(
            f"Component '{cell_name}' not found in the library."
            f" Available components: {component_names}"
        )

    return components[cell_name](tech=technology, **kwargs)
