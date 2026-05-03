"""Mask specs used to construct the layer extrusions in the SI 220nm passive PDK.

Each ``_masks`` entry combines one or more raw layer masks with boolean operations to
produce the Boolean region that a given material occupies in 3-D (e.g. the waveguide
silicon, the rib slab, gratings, heater filaments, and contact pads at their respective
levels above or below the waveguide).
"""

import photonforge as pf

from ._layers import _layer_specs

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

_masks = {}

# Passive layers
_masks["substrate"] = -pf.MaskSpec((0, 0))
_masks["waveguide"] = (_masks_layers["wg_lf"] - _masks_layers["wg_df"]) * (
    -_masks_layers["grating_ebl"] - _masks_layers["grating_duv"]
)
_masks["ebeam_gratings"] = (_masks_layers["wg_lf"] + -_masks_layers["wg_df"]) * _masks_layers[
    "grating_ebl"
]
_masks["duv_gratings"] = (_masks_layers["wg_lf"] + -_masks_layers["wg_df"]) * _masks_layers[
    "grating_duv"
]
_masks["rib_slab"] = _masks_layers["rib_slab"] * -(
    _masks["waveguide"] + _masks["ebeam_gratings"] + _masks["duv_gratings"]
)
_masks["box"] = -(
    _masks["waveguide"] + _masks["rib_slab"] + _masks["ebeam_gratings"] + _masks["duv_gratings"]
)

# Heaters
_masks["heater_fil_waveguide"] = _masks_layers["heater_fil"] * _masks["waveguide"]
_masks["heater_fil_ebeam_gratings"] = _masks_layers["heater_fil"] * _masks["ebeam_gratings"]
_masks["heater_fil_duv_gratings"] = _masks_layers["heater_fil"] * _masks["duv_gratings"]
_masks["heater_fil_rib_slab"] = _masks_layers["heater_fil"] * _masks["rib_slab"]
_masks["heater_fil_box"] = _masks_layers["heater_fil"] * _masks["box"]

# Contact pads, no heaters
_masks["contact_pad_waveguide"] = (
    _masks_layers["contact_pad"] * _masks["waveguide"] * (-_masks_layers["heater_fil"])
)
_masks["contact_pad_rib_slab"] = (
    _masks_layers["contact_pad"] * _masks["rib_slab"] * (-_masks_layers["heater_fil"])
)
_masks["contact_pad_ebeam_gratings"] = (
    _masks_layers["contact_pad"] * _masks["ebeam_gratings"] * (-_masks_layers["heater_fil"])
)
_masks["contact_pad_duv_gratings"] = (
    _masks_layers["contact_pad"] * _masks["duv_gratings"] * (-_masks_layers["heater_fil"])
)
_masks["contact_pad_box"] = (
    _masks_layers["contact_pad"] * _masks["box"] * (-_masks_layers["heater_fil"])
)
mask_contact_pads_no_heaters = (
    _masks["contact_pad_waveguide"]
    + _masks["contact_pad_rib_slab"]
    + _masks["contact_pad_ebeam_gratings"]
    + _masks["contact_pad_duv_gratings"]
    + _masks["contact_pad_box"]
)

# Contact pads, heaters
_masks["contact_pad_heater_fil_waveguide"] = (
    _masks_layers["contact_pad"]
    * _masks["waveguide"]
    * _masks_layers["heater_fil"]
    * -mask_contact_pads_no_heaters
)
_masks["contact_pad_heater_fil_rib_slab"] = (
    _masks_layers["contact_pad"]
    * _masks["rib_slab"]
    * _masks_layers["heater_fil"]
    * -mask_contact_pads_no_heaters
)
_masks["contact_pad_heater_fil_ebeam_gratings"] = (
    _masks_layers["contact_pad"]
    * _masks["ebeam_gratings"]
    * _masks_layers["heater_fil"]
    * -mask_contact_pads_no_heaters
)
_masks["contact_pad_heater_fil_duv_gratings"] = (
    _masks_layers["contact_pad"]
    * _masks["duv_gratings"]
    * _masks_layers["heater_fil"]
    * -mask_contact_pads_no_heaters
)
_masks["contact_pad_heater_fil_box"] = (
    _masks_layers["contact_pad"] * _masks["box"] * -mask_contact_pads_no_heaters
)
