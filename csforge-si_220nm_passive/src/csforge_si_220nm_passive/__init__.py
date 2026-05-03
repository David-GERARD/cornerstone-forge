"""This module contains the implementation of Cornerstone's SI 220nm passive PDK."""

from cband import component_names as cband_component_names
from cband import components as cband_components
from oband import component_names as oband_component_names
from oband import components as oband_components
from technology import csforge_si_220nm_pdk

components = oband_components | cband_components
component_names = oband_component_names + cband_component_names

__version__ = "0.1.0"


def plot_cross_section(technology=None):
    """Plot the cross-section of the technology stack using Tidy3D."""
    import photonforge as pf  # noqa: PLC0415

    if technology is None:
        technology = csforge_si_220nm_pdk()

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
