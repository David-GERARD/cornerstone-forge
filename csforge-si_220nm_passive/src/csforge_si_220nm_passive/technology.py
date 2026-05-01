"""This file contains the parametric technology definition for the SI 220nm passive PDK."""

import photonforge as pf
import tidy3d as td
from _extrusions import _masks, _media, _thicknesses
from _layers import _layer_specs


@pf.parametric_technology
def csforge_si_220nm_pdk(
    masks: dict[str, pf.MaskSpec] = _masks,
    media: dict[str, dict[str, td.Medium]] = _media,
    thicknesses: dict[str, float] = _thicknesses,
) -> pf.Technology:
    """Defines the parametric technology for Cornerstone's Si 220nm passive PDK."""
    layers = {k: v.copy() for k, v in _layer_specs.items()}

    extrusion_specs = [
        pf.ExtrusionSpec(
            mask_spec=masks["waveguide"],
            medium=media["si"],
            limits=(0, thicknesses["waveguide"]),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["rib_slab"],
            medium=media["si"],
            limits=(0, thicknesses["rib_slab"]),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["ebeam_gratings"],
            medium=media["si"],
            limits=(0, thicknesses["ebeam_gratings"]),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["duv_gratings"],
            medium=media["si"],
            limits=(0, thicknesses["duv_gratings"]),
            sidewall_angle=0.0,
        ),
        # TODO: Add heater and contact pads extrusions
    ]

    technology = pf.Technology(
        name="csforge_si_220nm_passive",
        version="0.1.0",
        layers=layers,
        extrusion_specs=extrusion_specs,
        ports={},
        background_medium=media["sio2"],
        connections={},
    )
    return technology


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # viewer = LiveViewer()
    c = pf.Component("test_component", technology=csforge_si_220nm_pdk())

    # Hole in waveguide test
    c.add(
        "wg_lf",
        pf.Rectangle((-2.5, -2), (-1.5, 2)),
        "wg_df",
        pf.Rectangle((-2.25, -2), (-1.75, 2)),
    )

    # Rib waveduide test
    c.add(
        "wg_lf",
        pf.Rectangle((-0.25, -2), (0.25, 2)),
        "rib_slab",
        pf.Rectangle((-0.5, -2), (0.5, 2)),
    )

    # Gratings test
    c.add(
        "wg_lf",
        pf.Rectangle((1.5, -2), (2.5, 2)),
        "rib_slab",
        pf.Rectangle((1, -2), (3, 2)),
        "grating_ebl",
        pf.Rectangle((1.25, -2), (1.75, 2)),
        "grating_duv",
        pf.Rectangle((2.25, -2), (2.75, 2)),
    )
    # viewer(c)
    ax1 = pf.tidy3d_plot(c, y=0)

    plt.show()
