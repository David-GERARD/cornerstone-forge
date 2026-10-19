"""This module contains the implementation of Cornerstone's SI 220nm passive PDK."""

from .component import (
    allband_component_names,  # List of component names that are band-agnostic.
    allband_components,  # Dictionary of band-agnostic component factory functions.
    cband_component_names,  # List of component names specific to the C-band (1550 nm).
    cband_components,  # Dictionary of C-band component factory functions.
    component,  # This is the main entry point for users to access components by name.
    component_names,  # A list of all available component names in the library.
    components,  # A dictionary mapping component names to their factory functions.
    oband_component_names,  # List of component names specific to the O-band (1310 nm).
    oband_components,  # Dictionary of O-band component factory functions.
)
from .technology import si_220nm_passive_pdk, technology_version

__version__ = technology_version
__all__ = [
    "allband_component_names",
    "allband_components",
    "cband_component_names",
    "cband_components",
    "component",
    "component_names",
    "components",
    "oband_component_names",
    "oband_components",
    "si_220nm_passive_pdk",
]


def plot_cross_section(technology=None):
    """Plot the cross-section of the technology stack using Tidy3D."""
    import photonforge as pf  # noqa: PLC0415

    if technology is None:
        technology = si_220nm_passive_pdk()

    c = pf.Component("test_component", technology=technology)

    c.add(
        "wg_lf",
        pf.Rectangle((0.0, -2.0), (3.0, 2.0)),
        "grating_ebl",
        pf.Rectangle((0.2, -2.0), (0.4, 2.0)),
        pf.Rectangle((0.6, -2.0), (0.8, 2.0)),
        "grating_duv",
        pf.Rectangle((1.2, -2.0), (1.4, 2.0)),
        pf.Rectangle((1.6, -2.0), (1.8, 2.0)),
    )

    c.add(
        "wg_lf",
        pf.Rectangle((3.0, -2.0), (5.2, 2.0)),
        "wg_df",
        pf.Rectangle((3.2, -2.0), (4, 2.0)),
        pf.Rectangle((4.2, -2.0), (5.0, 2.0)),
        "heater_fil",
        pf.Rectangle((3.6, -2.0), (4.6, 2.0)),
        "contact_pad",
        pf.Rectangle((3.0, -2.0), (4.0, 2.0)),
        pf.Rectangle((4.2, -2.0), (5.2, 2.0)),
    )

    c.add(
        "rib_slab",
        pf.Rectangle((5.0, -2.0), (7.0, 2.0)),
        "wg_lf",
        pf.Rectangle((5.4, -2.0), (6.0, 2.0)),
        pf.Rectangle((6.4, -2.0), (7.0, 2.0)),
    )

    ax = pf.tidy3d_plot(c, y=0)

    return ax
