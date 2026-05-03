"""This module defines the media used in the Si 220nm passive PDK.

Media:
    - Optical dispersive media for Si and SiO2 are loaded from PDK data.
    - Electrical media for Si and SiO2 are defined with typical permittivity values.
    - TiN media is defined for heaters, with properties taken from literature.
    - Aluminum media is defined for contact pads, using Tidy3D's material library.

"""

import tidy3d as td
from data.materials import _load_material_data

###############
# MEDIA
###############

# Waveguide and substrate media
medium_si, medium_sio2 = _load_material_data()
_media = {
    "sio2": {
        "optical": medium_sio2,
        "electrical": td.Medium(permittivity=4.2, name="sio2"),
    },
    "si": {"optical": medium_si, "electrical": td.Medium(permittivity=12.3, name="si")},
    "air": td.Medium(permittivity=1),
}

# Heaters media
# Taken from https://www.flexcompute.com/tidy3d/examples/notebooks/ThermallyTunedRingResonator/
TiN_k = 28e-6  # TiN thermal conductivity W/(um*K)
TiN_s = 598  # TiN specific heat capacity, J / (Kg * K)
TiN_sigma = 2.3  # Electric conductivity of TiN, S/um

# Taken from https://refractiveindex.info/?shelf=main&book=TiN&page=Shkondin
TiN_n_1550nm = 3.2303

_media["tin"] = td.MultiPhysicsMedium(
    optical=td.Medium(permittivity=TiN_n_1550nm**2, name="tin"),
    heat=td.SolidMedium(
        conductivity=TiN_k,
        capacity=TiN_s,
        name="tin",
    ),
)

# Contact pads media (Aluminum as in cspdk https://github.com/gdsfactory/cspdk/blob/main/cspdk/si220/cband/tech.py)
_media["al"] = td.material_library["Al"]["Rakic1995"]
