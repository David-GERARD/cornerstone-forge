"""This file contains the parametric technology definition for the SI 220nm passive PDK."""

import photonforge as pf
import tidy3d as td
from _extrusions import _masks
from _layers import _connections, _layer_specs, _media, _thicknesses
from _ports import _ports


@pf.parametric_technology
def csforge_si_220nm_pdk(
    masks: dict[str, pf.MaskSpec] = _masks,
    media: dict[str, dict[str, td.Tidy3dBaseModel]] = _media,
    thicknesses: dict[str, float] = _thicknesses,
    include_substrate: bool = False,
) -> pf.Technology:
    """Defines the parametric technology for Cornerstone's Si 220nm passive PDK."""
    layers = {k: v.copy() for k, v in _layer_specs.items()}

    # Passive layers extrusions
    extrusion_specs = [
        pf.ExtrusionSpec(
            mask_spec=masks["waveguide"],
            medium=media["si"],
            limits=(0, thicknesses["waveguide"]),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["waveguide"],
            medium=media["sio2"],
            limits=(thicknesses["waveguide"], thicknesses["waveguide"] + thicknesses["tox"]),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["rib_slab"],
            medium=media["si"],
            limits=(0, thicknesses["rib_slab"]),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["rib_slab"],
            medium=media["sio2"],
            limits=(thicknesses["rib_slab"], thicknesses["rib_slab"] + thicknesses["tox"]),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["ebeam_gratings"],
            medium=media["si"],
            limits=(0, thicknesses["ebeam_gratings"]),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["ebeam_gratings"],
            medium=media["sio2"],
            limits=(
                thicknesses["ebeam_gratings"],
                thicknesses["ebeam_gratings"] + thicknesses["tox"],
            ),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["duv_gratings"],
            medium=media["si"],
            limits=(0, thicknesses["duv_gratings"]),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["duv_gratings"],
            medium=media["sio2"],
            limits=(thicknesses["duv_gratings"], thicknesses["duv_gratings"] + thicknesses["tox"]),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["box"],
            medium=media["sio2"],
            limits=(0, thicknesses["tox"]),
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["substrate"],
            medium=media["sio2"],
            limits=(-thicknesses["box"], 0),
            sidewall_angle=0.0,
        ),
    ]

    # Heater layer extrusions
    extrusion_specs += [
        pf.ExtrusionSpec(
            mask_spec=masks["heater_fil_waveguide"],
            medium=media["tin"],
            limits=(
                thicknesses["waveguide"] + thicknesses["tox"],
                thicknesses["waveguide"] + thicknesses["tox"] + thicknesses["heater_fil"],
            ),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["heater_fil_rib_slab"],
            medium=media["tin"],
            limits=(
                thicknesses["rib_slab"] + thicknesses["tox"],
                thicknesses["rib_slab"] + thicknesses["tox"] + thicknesses["heater_fil"],
            ),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["heater_fil_ebeam_gratings"],
            medium=media["tin"],
            limits=(
                thicknesses["ebeam_gratings"] + thicknesses["tox"],
                thicknesses["ebeam_gratings"] + thicknesses["tox"] + thicknesses["heater_fil"],
            ),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["heater_fil_duv_gratings"],
            medium=media["tin"],
            limits=(
                thicknesses["duv_gratings"] + thicknesses["tox"],
                thicknesses["duv_gratings"] + thicknesses["tox"] + thicknesses["heater_fil"],
            ),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["heater_fil_box"],
            medium=media["tin"],
            limits=(thicknesses["tox"], thicknesses["tox"] + thicknesses["heater_fil"]),
            sidewall_angle=0.0,
        ),
    ]

    # Contact pad extrusions (no heaters)
    extrusion_specs += [
        pf.ExtrusionSpec(
            mask_spec=masks["contact_pad_waveguide"],
            medium=media["al"],
            limits=(
                thicknesses["waveguide"] + thicknesses["tox"],
                thicknesses["waveguide"] + thicknesses["tox"] + thicknesses["contact_pad"],
            ),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["contact_pad_rib_slab"],
            medium=media["al"],
            limits=(
                thicknesses["rib_slab"] + thicknesses["tox"],
                thicknesses["rib_slab"] + thicknesses["tox"] + thicknesses["contact_pad"],
            ),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["contact_pad_ebeam_gratings"],
            medium=media["al"],
            limits=(
                thicknesses["ebeam_gratings"] + thicknesses["tox"],
                thicknesses["ebeam_gratings"] + thicknesses["tox"] + thicknesses["contact_pad"],
            ),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["contact_pad_duv_gratings"],
            medium=media["al"],
            limits=(
                thicknesses["duv_gratings"] + thicknesses["tox"],
                thicknesses["duv_gratings"] + thicknesses["tox"] + thicknesses["contact_pad"],
            ),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["contact_pad_box"],
            medium=media["al"],
            limits=(thicknesses["tox"], thicknesses["tox"] + thicknesses["contact_pad"]),
            sidewall_angle=0.0,
        ),
    ]
    # Contact pad extrusions (with heaters)
    extrusion_specs += [
        pf.ExtrusionSpec(
            mask_spec=masks["contact_pad_heater_fil_waveguide"],
            medium=media["al"],
            limits=(
                thicknesses["waveguide"] + thicknesses["tox"] + thicknesses["heater_fil"],
                thicknesses["waveguide"]
                + thicknesses["tox"]
                + thicknesses["heater_fil"]
                + thicknesses["contact_pad"],
            ),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["contact_pad_heater_fil_rib_slab"],
            medium=media["al"],
            limits=(
                thicknesses["rib_slab"] + thicknesses["tox"] + thicknesses["heater_fil"],
                thicknesses["rib_slab"]
                + thicknesses["tox"]
                + thicknesses["heater_fil"]
                + thicknesses["contact_pad"],
            ),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["contact_pad_heater_fil_ebeam_gratings"],
            medium=media["al"],
            limits=(
                thicknesses["ebeam_gratings"] + thicknesses["tox"] + thicknesses["heater_fil"],
                thicknesses["ebeam_gratings"]
                + thicknesses["tox"]
                + thicknesses["heater_fil"]
                + thicknesses["contact_pad"],
            ),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["contact_pad_heater_fil_duv_gratings"],
            medium=media["al"],
            limits=(
                thicknesses["duv_gratings"] + thicknesses["tox"] + thicknesses["heater_fil"],
                thicknesses["duv_gratings"]
                + thicknesses["tox"]
                + thicknesses["heater_fil"]
                + thicknesses["contact_pad"],
            ),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["contact_pad_heater_fil_box"],
            medium=media["al"],
            limits=(
                thicknesses["tox"] + thicknesses["heater_fil"],
                thicknesses["tox"] + thicknesses["heater_fil"] + thicknesses["contact_pad"],
            ),
            sidewall_angle=0.0,
        ),
    ]

    if include_substrate:
        extrusion_specs += [
            pf.ExtrusionSpec(
                mask_spec=masks["substrate"],
                medium=media["si"],
                limits=(-thicknesses["box"] * 2, -thicknesses["box"]),
                sidewall_angle=0.0,
            ),
        ]

    technology = pf.Technology(
        name="csforge_si_220nm_passive",
        version="0.1.0",
        layers=layers,
        extrusion_specs=extrusion_specs,
        ports=_ports,
        background_medium=media["air"],
        connections=_connections,
    )
    return technology


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    tech = csforge_si_220nm_pdk(include_substrate=True)
    pf.config.default_technology = tech
    # viewer = LiveViewer()
    c = pf.Component("test_component", technology=tech)

    # # Hole in waveguide test
    # c.add(
    #     "wg_lf",
    #     pf.Rectangle((-2.5, -2), (-1.5, 2)),
    #     "wg_df",
    #     pf.Rectangle((-2.25, -2), (-1.75, 2)),
    # )

    # # Rib waveduide test
    # c.add(
    #     "wg_lf",
    #     pf.Rectangle((-0.25, -2), (0.25, 2)),
    #     "rib_slab",
    #     pf.Rectangle((-0.5, -2), (0.5, 2)),
    # )

    # # Gratings test
    # c.add(
    #     "wg_lf",
    #     pf.Rectangle((1.5, -2), (2.5, 2)),
    #     "rib_slab",
    #     pf.Rectangle((1, -2), (3, 2)),
    #     "grating_ebl",
    #     pf.Rectangle((1.25, -2), (1.75, 2)),
    #     "grating_duv",
    #     pf.Rectangle((2.25, -2), (2.75, 2)),
    # )

    # # Heater and contact pad test
    # c.add(
    #     "heater_fil",
    #     pf.Rectangle((-2.5, -2), (0, 2)),
    #     pf.Rectangle((2, -2), (3, 2)),
    #     "contact_pad",
    #     pf.Rectangle((-2.5, -2), (3, 2)),
    # )

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

    # viewer(c)
    ax1 = pf.tidy3d_plot(c, y=0)

    plt.show()
    print(tech.ports)
    # pf.config.default_mesh_refinement = 30

    # freqs = [pf.C_0 / 1.55]

    # mode_solver = pf.port_modes("rib_1550nm_TE", freqs)
    # mode_solver.plot_field("E", mode_index=0, f=freqs[0], robust=False)

    # plt.show()

    # print(mode_solver.data.to_dataframe())
