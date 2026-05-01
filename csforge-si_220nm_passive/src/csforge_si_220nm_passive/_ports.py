"""Ports for csforge_si_220nm_passive technology.

Targets neff values were taken from cspdk.
"""

import photonforge as pf
from _layers import _layer_specs

_ports = {}

_ports["strip_1310nm"] = pf.PortSpec(
    description="Strip waveguide port, TE and TM polarization at 1310nm.",
    width=0.4,
    limits=(-1, 3),  # TODO: change to acount for thickness
    num_modes=2,
    default_radius=10,
    target_neff=2.52,
    path_profiles=[(0.4, 0, _layer_specs["wg_lf"].layer)],
)

_ports["rib_1310nm_TE"] = pf.PortSpec(
    description="Rib waveguide port, single mode at 1310nm, TE polarization.",
    width=0.4,
    limits=(-1, 3),  # TODO: change to acount for thickness
    num_modes=1,
    polarization="TE",
    default_radius=25,
    target_neff=2.52,
    path_profiles=[
        (0.4, 0, _layer_specs["wg_lf"].layer),
        (10.4, 0, _layer_specs["rib_slab"].layer),
    ],
)

_ports["strip_1550nm"] = pf.PortSpec(
    description="Strip waveguide port, TE and TM polarization at 1550nm.",
    width=0.45,
    limits=(-1, 3),  # TODO: change to acount for thickness
    num_modes=2,
    default_radius=10,
    target_neff=2.38,
    path_profiles=[(0.45, 0, _layer_specs["wg_lf"].layer)],
)

_ports["rib_1550nm_TE"] = pf.PortSpec(
    description="Rib waveguide port, single mode at 1550nm, TE polarization.",
    width=10.45,
    limits=(-1, 3),  # TODO: change to acount for thickness
    num_modes=1,
    polarization="TE",
    default_radius=25,
    target_neff=2.38,
    path_profiles=[
        (0.45, 0, _layer_specs["wg_lf"].layer),
        (10.45, 0, _layer_specs["rib_slab"].layer),
    ],
)

_ports["dc"] = pf.PortSpec(
    description="Electrical port for DC signals, used for heaters.",
    width=80,
    limits=(-1, 3),  # TODO: change to acount for thickness
    default_radius=0,
    path_profiles=[(80, 0, _layer_specs["contact_pad"].layer)],
    voltage_path=[],
    current_path=[],
)

if __name__ == "__main__":
    tech = pf.basic_technology()
    tech.ports = _ports
    print(tech.ports)
