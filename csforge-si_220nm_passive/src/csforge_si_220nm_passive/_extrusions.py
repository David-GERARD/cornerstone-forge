import photonforge as pf
from _layers import _layer_specs
from data.materials import _load_material_data

medium_si, medium_sio2 = _load_material_data()
_media = {"sio2": {"optical": medium_sio2}, "si": {"optical": medium_si}}

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
    "waveguide": (_masks_layers["wg_lf"] - _masks_layers["wg_df"])
    * (-_masks_layers["grating_ebl"] - _masks_layers["grating_duv"]),
    "rib_slab": _masks_layers["rib_slab"],
    "ebeam_gratings": (_masks_layers["wg_lf"] + -_masks_layers["wg_df"])
    * _masks_layers["grating_ebl"],
    "duv_gratings": (_masks_layers["wg_lf"] + -_masks_layers["wg_df"])
    * _masks_layers["grating_duv"],
    #   "heater_fil": _masks_layers["heater_fil"],
    #   "contact_pad": _masks_layers["contact_pad"],
}

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
