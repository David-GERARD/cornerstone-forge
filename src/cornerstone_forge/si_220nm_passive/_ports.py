"""Port specs for the SI 220nm passive PDK technology.

Defines optical port specs for strip and rib waveguides at 1310 nm and 1550 nm, plus
an electrical DC port spec for heater pads.  Target effective-index (neff) values are
taken from cspdk (https://github.com/gdsfactory/cspdk).

Limits and widths were optimized through an EME neff convergence study (see Notebook).
"""

import photonforge as pf

from ._layers import _layer_specs


def _ports(thicknesses: dict | None = None) -> dict:
    """Return the port specs for the SI 220nm passive PDK."""
    zlimits_heater = (
        thicknesses["tox"] - 1.5,
        thicknesses["tox"] + thicknesses["heater_fil"] + 1.5,
    )

    port_specs = {}

    port_specs["strip_1310nm"] = pf.PortSpec(
        description="Strip waveguide port, TE and TM polarization at 1310nm.",
        width=0.6804,
        limits=(-0.39, 0.61),
        num_modes=2,
        default_radius=10,
        target_neff=2.52,
        path_profiles=[(0.4, 0, _layer_specs["wg_lf"].layer)],
    )

    port_specs["rib_1310nm_TE"] = pf.PortSpec(
        description="Rib waveguide port, single mode at 1310nm, TE polarization.",
        width=2.8556,
        limits=(-0.14, 0.36),
        num_modes=1,
        polarization="TE",
        default_radius=25,
        target_neff=2.52,
        path_profiles=[
            (0.4, 0, _layer_specs["wg_lf"].layer),
            (10.4, 0, _layer_specs["rib_slab"].layer),
        ],
    )

    port_specs["strip_1550nm"] = pf.PortSpec(
        description="Strip waveguide port, TE and TM polarization at 1550nm.",
        width=0.7937,
        limits=(-0.14, 0.36),
        num_modes=2,
        default_radius=10,
        target_neff=2.38,
        path_profiles=[(0.45, 0, _layer_specs["wg_lf"].layer)],
    )

    port_specs["rib_1550nm_TE"] = pf.PortSpec(
        description="Rib waveguide port, single mode at 1550nm, TE polarization.",
        width=1.2999,
        limits=(-0.14, 0.36),
        num_modes=1,
        polarization="TE",
        default_radius=25,
        target_neff=2.38,
        path_profiles=[
            (0.45, 0, _layer_specs["wg_lf"].layer),
            (10.45, 0, _layer_specs["rib_slab"].layer),
        ],
    )

    port_specs["dc"] = pf.PortSpec(
        description="Electrical port for DC signals, used for heaters.",
        width=80,
        limits=zlimits_heater,
        default_radius=0,
        path_profiles=[(80, 0, _layer_specs["contact_pad"].layer)],
        voltage_path=[],
        current_path=[],
    )
    return port_specs


# TODO: fiber ports

if __name__ == "__main__":
    tech = pf.basic_technology()
    tech.ports = _ports
    print(tech.ports)
