import photonforge as pf
import tidy3d as td
from _layers import _layer_specs
from data.materials import _load_material_data

# DEFAULT MEDIA
medium_si, medium_sio2 = _load_material_data()
_media = {
    "sio2": {
        "optical": medium_sio2,
        "electrical": td.Medium(permittivity=4.2, name="sio2"),
    },
    "si": {"optical": medium_si, "electrical": td.Medium(permittivity=12.3, name="si")},
}

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

# MASKS FOR EXTRUSIONS
_masks_layers = {
    "grating_ebl": pf.MaskSpec(_layer_specs["grating_ebl"].layer),
    "grating_duv": pf.MaskSpec(_layer_specs["grating_duv"].layer),
    "wg_lf": pf.MaskSpec(_layer_specs["wg_lf"].layer),
    "wg_df": pf.MaskSpec(_layer_specs["wg_df"].layer),
    "rib_slab": pf.MaskSpec(_layer_specs["rib_slab"].layer),
    "heater_fil": pf.MaskSpec(_layer_specs["heater_fil"].layer),
    "contact_pad": pf.MaskSpec(_layer_specs["contact_pad"].layer),
    "Label_Etch_DF": pf.MaskSpec(_layer_specs["Label_Etch_DF"].layer),
}

# _tolerances = {
#     "box": 0.0,
#     "waveguide": 0.02,
#     "rib_slab": 0.02,
#     "ebeam_gratings": 0.01,
#     "duv_gratings": 0.01,
#     "tox": 0.2,
#     "heater_fil": 0.01,
#     "contact_pad": 0.01,
# }


_masks = {
    "substrate": -pf.MaskSpec((0, 0)),
    "box": -pf.MaskSpec((0, 0)),
    "waveguide": (_masks_layers["wg_lf"] - _masks_layers["wg_df"])
    * (-_masks_layers["grating_ebl"] - _masks_layers["grating_duv"]),
    "rib_slab": _masks_layers["rib_slab"],
    "ebeam_gratings": (_masks_layers["wg_lf"] + -_masks_layers["wg_df"])
    * _masks_layers["grating_ebl"],
    "duv_gratings": (_masks_layers["wg_lf"] + -_masks_layers["wg_df"])
    * _masks_layers["grating_duv"],
}
_masks["heater_fil_waveguide"] = _masks_layers["heater_fil"] * _masks["waveguide"]
_masks["heater_fil_rib_slab"] = _masks_layers["heater_fil"] * _masks["rib_slab"]
_masks["heater_fil_ebeam_gratings"] = _masks_layers["heater_fil"] * _masks["ebeam_gratings"]
_masks["heater_fil_duv_gratings"] = _masks_layers["heater_fil"] * _masks["duv_gratings"]
_masks["heater_fil_box"] = _masks_layers["heater_fil"] - (
    _masks["heater_fil_waveguide"]
    + _masks["heater_fil_rib_slab"]
    + _masks["heater_fil_ebeam_gratings"]
    + _masks["heater_fil_duv_gratings"]
)

_thicknesses = {
    "box": 3.0,
    "waveguide": 0.22,
    "rib_slab": 0.1,
    "ebeam_gratings": 0.125,
    "duv_gratings": 0.15,
    "tox": 2.0,
    "heater_fil": 0.15,
    "contact_pad": 0.22,
}


if __name__ == "__main__":
    TiN_k = 28e-6  # TiN thermal conductivity W/(um*K)
    TiN_s = 598  # TiN specific heat capacity, J / (Kg * K)
    TiN_sigma = 2.3  # Electric conductivity of TiN, S/um
    tin = {
        "optical": td.material_library,
        "electrical": td.MultiPhysicsMedium(
            heat_spec=td.SolidSpec(
                conductivity=TiN_k,
                capacity=TiN_s,
            ),
            name="TiN",
        ),
    }
    print(type(tin["electrical"]))
