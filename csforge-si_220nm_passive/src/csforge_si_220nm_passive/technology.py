"""Parametric technology definition for Cornerstone's SI 220nm passive PDK.

Exposes ``csforge_si_220nm_pdk``, a ``@pf.parametric_technology`` factory that assembles
layers, extrusion specs (waveguide, rib slab, EBL/DUV gratings, heater filaments, and
contact pads), port specs, and background medium into a ``pf.Technology`` object.

Every layer thickness, the silicon sidewall angle (default 5°), and each optical or
electrical medium can be overridden individually via keyword arguments.  Setting
``include_substrate=True`` appends a semi-infinite silicon substrate extrusion that
extends from ``-pf.Z_INF`` to the bottom of the BOX layer.
"""

from typing import Literal

import photonforge as pf
import photonforge.typing as pft

from ._extrusions import _masks
from ._layers import _connections, _layer_specs, _thicknesses
from ._media import _media
from ._ports import _ports

_MediumType = pft.Medium | dict[Literal["optical", "electrical"], pft.Medium]

technology_version = "0.2.9"


@pf.parametric_technology
def csforge_si_220nm_pdk(
    box_thickness: pft.PositiveDimension = _thicknesses["box"],
    waveguide_thickness: pft.PositiveDimension = _thicknesses["strip"],
    rib_slab_thickness: pft.PositiveDimension = _thicknesses["rib_slab"],
    ebeam_gratings_thickness: pft.PositiveDimension = _thicknesses["ebeam_gratings"],
    duv_gratings_thickness: pft.PositiveDimension = _thicknesses["duv_gratings"],
    tox_thickness: pft.PositiveDimension = _thicknesses["tox"],
    heater_fil_thickness: pft.PositiveDimension = _thicknesses["heater_fil"],
    contact_pad_thickness: pft.PositiveDimension = _thicknesses["contact_pad"],
    sidewall_angle_si: pft.Angle = 5.0,
    sidewall_angle_tin: pft.Angle = 5.0,
    sio2: _MediumType = _media["sio2"],
    si: _MediumType = _media["si"],
    tin: _MediumType = _media["tin"],
    al: _MediumType = _media["al"],
    air: _MediumType = _media["air"],
    include_substrate: bool = False,
) -> pf.Technology:
    """Defines the parametric technology for Cornerstone's Si 220nm passive PDK.

    Args:
        box_thickness: Thickness of the BOX layer in um.
        waveguide_thickness: Thickness of the strip waveguide layer in um.
        rib_slab_thickness: Thickness of the rib slab layer in um.
        ebeam_gratings_thickness: Thickness of the e-beam gratings layer in um.
        duv_gratings_thickness: Thickness of the DUV gratings layer in um.
        tox_thickness: Thickness of the top oxide SiO2 layer in um.
        heater_fil_thickness: Thickness of the heater filament layer in um.
        contact_pad_thickness: Thickness of the contact pad layer in um.
        sidewall_angle_si: Sidewall angle for silicon layers in degrees.
        sidewall_angle_tin: Sidewall angle for tin layers in degrees.
        sio2: Medium for SiO2.
        si: Medium for silicon.
        tin: Medium for tin.
        al: Medium for aluminum.
        air: Medium for air.
        include_substrate: Whether to include the silicon substrate below the BOX layer.

    Returns:
        A parametric technology object.

    """
    masks = _masks

    layers = {k: v.copy() for k, v in _layer_specs.items()}

    media = {
        "sio2": sio2,
        "si": si,
        "tin": tin,
        "al": al,
        "air": air,
    }

    thicknesses = {
        "box": box_thickness,
        "strip": waveguide_thickness,
        "rib_slab": rib_slab_thickness,
        "ebeam_gratings": ebeam_gratings_thickness,
        "duv_gratings": duv_gratings_thickness,
        "tox": tox_thickness,
        "heater_fil": heater_fil_thickness,
        "contact_pad": contact_pad_thickness,
    }

    extrusion_specs = []

    # Add extrusions for box and substrate
    extrusion_specs += [
        pf.ExtrusionSpec(
            mask_spec=masks["box"],
            medium=media["sio2"],
            limits=(0, thicknesses["tox"]),
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["box"],
            medium=media["sio2"],
            limits=(-1.0, 0),
            sidewall_angle=0.0,
        ),
    ]

    if include_substrate:
        extrusion_specs += [
            pf.ExtrusionSpec(
                mask_spec=masks["box"],
                medium=media["sio2"],
                limits=(-thicknesses["box"], 0),
                sidewall_angle=0.0,
            ),
            pf.ExtrusionSpec(
                mask_spec=masks["substrate"],
                medium=media["si"],
                limits=(-pf.Z_INF, -thicknesses["box"]),
                sidewall_angle=0.0,
            ),
        ]

    # Add extrusions for silicon layers (strip waveguide, rib slab, and gratings)

    extrusion_specs += [
        pf.ExtrusionSpec(
            mask_spec=masks["strip"],
            medium=media["si"],
            limits=(0, thicknesses["strip"]),
            sidewall_angle=sidewall_angle_si,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["rib_slab"],
            medium=media["si"],
            limits=(0, thicknesses["rib_slab"]),
            sidewall_angle=sidewall_angle_si,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["duv_gratings"],
            medium=media["si"],
            limits=(0, thicknesses["duv_gratings"]),
            sidewall_angle=sidewall_angle_si,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["ebeam_gratings"],
            medium=media["si"],
            limits=(0, thicknesses["ebeam_gratings"]),
            sidewall_angle=sidewall_angle_si,
        ),
    ]

    # Add extra extrusions to match the tox with the si layer
    extrusion_specs += [
        pf.ExtrusionSpec(
            mask_spec=masks["strip"],
            medium=media["sio2"],
            limits=(thicknesses["tox"], thicknesses["strip"] + thicknesses["tox"]),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["rib_slab"],
            medium=media["sio2"],
            limits=(thicknesses["tox"], thicknesses["rib_slab"] + thicknesses["tox"]),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["ebeam_gratings"],
            medium=media["sio2"],
            limits=(
                thicknesses["tox"],
                thicknesses["ebeam_gratings"] + thicknesses["tox"],
            ),
            sidewall_angle=0.0,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["duv_gratings"],
            medium=media["sio2"],
            limits=(thicknesses["tox"], thicknesses["duv_gratings"] + thicknesses["tox"]),
            sidewall_angle=0.0,
        ),
    ]

    # Add extrusions for contact pads
    # No heaters
    extrusion_specs += [
        pf.ExtrusionSpec(
            mask_spec=masks["contact_pad_waveguide"],
            medium=media["al"],
            limits=(
                thicknesses["strip"] + thicknesses["tox"],
                thicknesses["strip"] + thicknesses["tox"] + thicknesses["contact_pad"],
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
    # With heaters
    extrusion_specs += [
        pf.ExtrusionSpec(
            mask_spec=masks["contact_pad_heater_fil_waveguide"],
            medium=media["al"],
            limits=(
                thicknesses["strip"] + thicknesses["tox"],
                thicknesses["strip"]
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
                thicknesses["rib_slab"] + thicknesses["tox"],
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
                thicknesses["ebeam_gratings"] + thicknesses["tox"],
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
                thicknesses["duv_gratings"] + thicknesses["tox"],
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
                thicknesses["tox"],
                thicknesses["tox"] + thicknesses["heater_fil"] + thicknesses["contact_pad"],
            ),
            sidewall_angle=0.0,
        ),
    ]

    # Heater layer extrusions
    extrusion_specs += [
        pf.ExtrusionSpec(
            mask_spec=masks["heater_fil_waveguide"],
            medium=media["tin"],
            limits=(
                thicknesses["strip"] + thicknesses["tox"],
                thicknesses["strip"] + thicknesses["tox"] + thicknesses["heater_fil"],
            ),
            sidewall_angle=sidewall_angle_tin,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["heater_fil_rib_slab"],
            medium=media["tin"],
            limits=(
                thicknesses["rib_slab"] + thicknesses["tox"],
                thicknesses["rib_slab"] + thicknesses["tox"] + thicknesses["heater_fil"],
            ),
            sidewall_angle=sidewall_angle_tin,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["heater_fil_ebeam_gratings"],
            medium=media["tin"],
            limits=(
                thicknesses["ebeam_gratings"] + thicknesses["tox"],
                thicknesses["ebeam_gratings"] + thicknesses["tox"] + thicknesses["heater_fil"],
            ),
            sidewall_angle=sidewall_angle_tin,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["heater_fil_duv_gratings"],
            medium=media["tin"],
            limits=(
                thicknesses["duv_gratings"] + thicknesses["tox"],
                thicknesses["duv_gratings"] + thicknesses["tox"] + thicknesses["heater_fil"],
            ),
            sidewall_angle=sidewall_angle_tin,
        ),
        pf.ExtrusionSpec(
            mask_spec=masks["heater_fil_box"],
            medium=media["tin"],
            limits=(thicknesses["tox"], thicknesses["tox"] + thicknesses["heater_fil"]),
            sidewall_angle=sidewall_angle_tin,
        ),
    ]

    technology = pf.Technology(
        name="csforge_si_220nm_passive",
        version=technology_version,
        layers=layers,
        extrusion_specs=extrusion_specs,
        ports=_ports(thicknesses),
        background_medium=media["air"],
        connections=_connections,
    )
    return technology


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    tech = csforge_si_220nm_pdk(include_substrate=False)
    pf.config.default_technology = tech
    from photonforge.live_viewer import LiveViewer

    print(tech.ports)

    viewer = LiveViewer(port=59204)
    c = pf.Component("test_component", technology=tech)

    # c.add(
    #     "FloorPlan",
    #     pf.Rectangle((-0.5, -2.0), (7.5, 2.0)),
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
    c2 = pf.Component("test_component_2", technology=tech)
    straight_ref = c2.add_reference(
        pf.parametric.straight(technology=tech, port_spec=tech.ports["rib_1550nm_TE"], length=5.0)
    )
    gaussian_port = pf.GaussianPort(
        center=(-1.5, 0.0, _thicknesses["strip"] / 2),
        input_vector=(1, 0, 0),
        waist_radius=2.0,
        polarization_angle=0,  # for TE mode, in this case
    )
    c2.add_port(gaussian_port)
    viewer(c)
    ax1 = pf.tidy3d_plot(c, y=2.0)

    plt.show()
    # print(tech.ports)
    # pf.config.default_mesh_refinement = 30

    # freqs = [pf.C_0 / 1.55]

    # mode_solver = pf.port_modes("rib_1550nm_TE", freqs)
    # mode_solver.plot_field("E", mode_index=0, f=freqs[0], robust=False)

    # plt.show()

    # print(mode_solver.data.to_dataframe())
