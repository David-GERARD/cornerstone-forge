"""This module declares the layers, media, and thicknesses for the Si_220nm_passive PDK.

Layers scpecs:
    - Source: https://github.com/cornerstone-uos/cornerstone-pdk/blob/main/Si_220nm_passive/process_overview.yaml
    - Alias is used as a key for the layer. with the full name in the description for clarity.
    - The layer number and datatype are defined in the layer tuple.
    - The description provides the layer full name and its purpose.
    - Colors from https://github.com/cornerstone-uos/cornerstone-pdk/blob/main/Si_220nm_passive/layers.lyp

Connections:
    - Heater filaments and contact pads are connected.

Thicknesses:
    - Source: https://github.com/cornerstone-uos/cornerstone-pdk/blob/main/Si_220nm_passive/process_overview.yaml

"""

import photonforge as pf

###############
# LAYER SPECS
###############
_layer_specs = {
    "grating_ebl": pf.LayerSpec(
        layer=(60, 0),
        description=(
            "[Si_Etch0_EBL_DF_94nm] EBL-defined grating couplers."
            "Dark-field: layer will be etched. For gaps > 0.35, there is no max feature size."
        ),
        color="#ff008050",
        pattern="",
    ),
    "grating_duv": pf.LayerSpec(
        layer=(6, 0),
        description=(
            "[Si_Etch1_DUV_DF_70nm] DUV-defined grating couplers. Dark-field: layer will be etched."
        ),
        color="#ffcc78ff",
        pattern="",
    ),
    "wg_lf": pf.LayerSpec(
        layer=(3, 0),
        description=(
            "[Si_Etch2_LF_120nm] Waveguide layer, defines both strip and rib. "
            "Light-field: layer will be protected."
        ),
        color="#ffff80a8",
        pattern="",
    ),
    "wg_df": pf.LayerSpec(
        layer=(4, 0),
        description=(
            "[Si_Etch2_DF_120nm] Waveguide layer, defines both strip and rib. "
            "Dark-field: layer will be etched."
        ),
        color="#ff8183ff",
        pattern="",
    ),
    "rib_slab": pf.LayerSpec(
        layer=(5, 0),
        description=(
            "[Si_Etch3_LF_100nm_to_BOX] Rib protect layer. Light-field: layer will be protected."
        ),
        color="#ff80a8ff",
        pattern="",
    ),
    "heater_fil": pf.LayerSpec(
        layer=(39, 0),
        description=(
            "[Heat_Fil_LF] Heater filaments (light). Light-field: layer will become metal."
        ),
        color="#ff9580ff",
        pattern="",
    ),
    "contact_pad": pf.LayerSpec(
        layer=(41, 0),
        description=(
            "[Heat_CP_LF] Heater contact pads (light). Light-field: layer will become metal."
        ),
        color="#ff80a8ff",
        pattern="",
    ),
    "FloorPlan": pf.LayerSpec(
        layer=(99, 0), description=("[FloorPlan] Cell outline"), color="#fff3ff80", pattern=""
    ),
    "Label_Etch_DF": pf.LayerSpec(
        layer=(100, 0),
        description=(
            "[Label_Etch_DF] Labels (dark), "
            "Dark-field: layer will be etched"
            "Will not be checked in DRC."
        ),
        color="#ff8000ff",
        pattern="",
    ),
}

###############
# ELECTRICAL CONNECTIONS
###############

_connections = [(_layer_specs["heater_fil"].layer, _layer_specs["contact_pad"].layer)]


###############
# LAYER THICKNESSES
###############
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
