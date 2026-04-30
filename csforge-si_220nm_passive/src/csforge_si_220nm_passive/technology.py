"""This file contains the parametric technology definition for the SI 220nm passive PDK."""

import photonforge as pf
from _layers import _layers


@pf.parametric_technology
def csforge_si_220nm_pdk()-> pf.Technology:
    """Defines the parametric technology for Cornerstone's Si 220nm passive PDK."""
    layers = {k: v.copy() for k, v in _layers.items()}

    technology = pf.Technology(
        name="csforge_si_220nm_passive",
        version="0.1.0",
        layers=layers,
        extrusion_specs={},
        ports={},
        background_medium={},
        connections={},
    )
    return technology

if __name__ == "__main__":
    tech = csforge_si_220nm_pdk()
    print(tech)
