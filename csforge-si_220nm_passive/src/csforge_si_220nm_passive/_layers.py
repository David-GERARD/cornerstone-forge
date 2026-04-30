"""This module defines the layers used in the csforge_si_220nm_passive process.

Layers info:
    - Source: https://github.com/cornerstone-uos/cornerstone-pdk/blob/main/Si_220nm_passive/process_overview.yaml
    - Alias is used as a key for the layer. with the full name in the description for clarity.
    - The layer number and datatype are defined in the layer tuple.
    - The description provides the layer full name and its purpose.

Layers colors:
    - Source: https://github.com/cornerstone-uos/cornerstone-pdk/blob/main/Si_220nm_passive/layers.lyp

"""
import photonforge as pf

_layers = {
    "grating_ebl": pf.LayerSpec(
        layer=(60, 0),
        description=(
            "[Si_Etch0_EBL_DF_94nm] EBL-defined grating couplers."
            "Layer will be etched. For gaps > 0.35, there is no max feature size."
        ),
        color="#ff008050",
        pattern=""
    ),
    "grating_duv": pf.LayerSpec(
        layer=(6, 0),
        description=(
            "[Si_Etch1_DUV_DF_70nm] DUV-defined grating couplers. "
            "Layer will be etched."
        ),
        color="#ffcc78ff",
        pattern=""
    ),
    "wg_lf": pf.LayerSpec(
        layer=(3, 0),
        description=(
            "[Si_Etch2_LF_120nm] Waveguide layer, defines both strip and rib. "
            "Layer will be protected."
        ),
        color="#ffff80a8",
        pattern=""
    ),
    "wg_df": pf.LayerSpec(
        layer=(4, 0),
        description=(
            "[Si_Etch2_DF_120nm] Waveguide layer, defines both strip and rib. "
            "Layer will be etched."
        ),
        color="#ff8183ff",
        pattern=""
    ),
    "rib_slab": pf.LayerSpec(
        layer=(5, 0),
        description=(
            "[Si_Etch3_LF_100nm_to_BOX] Rib protect layer. "
            "Layer will be protected."
        ),
        color="#ff80a8ff",
        pattern=""
    ),
    "heater_fil": pf.LayerSpec(
        layer=(39, 0),
        description=(
            "[Heat_Fil_LF] Heater filaments (light). "
            "Layer will become metal."
        ),
        color="#ff9580ff",
        pattern=""
    ),
    "contact_pad": pf.LayerSpec(
        layer=(41, 0),
        description=(
            "[Heat_CP_LF] Heater contact pads (light). "
            "Layer will become metal."
        ),
        color="#ff80a8ff",
        pattern=""
    ),
    "FloorPlan": pf.LayerSpec(
        layer=(99, 0),
        description=(
            "[FloorPlan] Cell outline"
        ),
        color="#fff3ff80",
        pattern=""
    ),
    "Label_Etch_DF": pf.LayerSpec(
        layer = (100, 0),
        description = (
            "[Label_Etch_DF] Labels (dark), will be etched, will not be checked in DRC."
        ),
        color = "#ff8000ff",
        pattern = ""
    ),
}

if __name__ == "__main__":
    print(pf.LayerTable(_layers))
