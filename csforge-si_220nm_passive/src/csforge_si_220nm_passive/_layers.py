"""Layer specs, electrical connections, and process thicknesses for the SI 220nm passive PDK.

Layer specs (``_layer_specs``):
    Each key is a short alias used throughout the package; the value is a
    ``pf.LayerSpec`` carrying the GDS (layer, datatype) tuple, a human-readable
    description, and a display colour.  Sourced from the Cornerstone PDK process
    overview and layer file:
    https://github.com/cornerstone-uos/cornerstone-pdk/blob/main/Si_220nm_passive/process_overview.yaml
    https://github.com/cornerstone-uos/cornerstone-pdk/blob/main/Si_220nm_passive/layers.lyp

Connections (``_connections``):
    List of (layer_a, layer_b) tuples that are electrically shorted.  Currently
    heater filaments (``heater_fil``) and contact pads (``contact_pad``) are connected.

Thicknesses (``_thicknesses``):
    Physical layer thicknesses in microns.  Sourced from:
    https://github.com/cornerstone-uos/cornerstone-pdk/blob/main/Si_220nm_passive/process_overview.yaml
"""

import photonforge as pf

###############
# LAYER SPECS
###############

# Klayout patterns
# Source: https://github.com/flexcompute/luxtelligence-forge/blob/main/lnoi400/layer_converter.py
patterns = {
    "I0": "solid",  # solid
    "I1": "hollow",  # hollow
    "I2": ":",  # dotted
    "I3": ".",  # coarsely dotted
    "I4": "\\\\",  # left-hatched
    "I5": "\\",  # lightly left-hatched
    "I6": "\\\\",  # strongly left-hatched dense
    "I7": "\\",  # strongly left-hatched sparse
    "I8": "//",  # right-hatched
    "I9": "/",  # lightly right-hatched
    "I10": "//",  # strongly right-hatched dense
    "I11": "/",  # strongly right-hatched sparse
    "I12": "xx",  # cross-hatched
    "I13": "x",  # lightly cross-hatched
    "I14": "+",  # checkerboard 2px
    "I15": "x",  # strongly cross-hatched sparse
    "I16": "xx",  # heavy checkerboard
    "I17": "x",  # hollow bubbles
    "I18": "x",  # solid bubbles
    "I19": "+",  # pyramids
    "I20": "+",  # turned pyramids
    "I21": "+",  # plus
    "I22": "-",  # minus
    "I23": "/",  # 22.5 degree down
    "I24": "\\",  # 22.5 degree up
    "I25": "//",  # 67.5 degree down
    "I26": "\\\\",  # 67.5 degree up
    "I27": "x",  # 22.5 cross hatched
    "I28": "x",  # zig zag
    "I29": "x",  # sine
    "I30": "+",  # special pattern for light heavy dithering
    "I31": "+",  # special pattern for light frame dithering
    "I32": "||",  # vertical dense
    "I33": "|",  # vertical
    "I34": "||",  # vertical thick
    "I35": "|",  # vertical sparse
    "I36": "|",  # vertical sparse, thick
    "I37": "=",  # horizontal dense
    "I38": "-",  # horizontal
    "I39": "=",  # horizontal thick
    "I40": "-",  # horizontal
    "I41": "-",  # horizontal
    "I42": "++",  # grid dense
    "I43": "+",  # grid
    "I44": "++",  # grid thick
    "I45": "+",  # grid sparse
    "I46": "+",  # grid sparse, thick
}

_layer_specs = {
    "grating_ebl": pf.LayerSpec(
        layer=(60, 0),
        description=(
            "[Si_Etch0_EBL_DF_94nm] EBL-defined grating couplers."
            "Dark-field: layer will be etched. For gaps > 0.35, there is no max feature size."
        ),
        color="#008050",
        pattern=patterns["I15"],
    ),
    "grating_duv": pf.LayerSpec(
        layer=(6, 0),
        description=(
            "[Si_Etch1_DUV_DF_70nm] DUV-defined grating couplers. Dark-field: layer will be etched."
        ),
        color="#cc78ff",
        pattern=patterns["I6"],
    ),
    "wg_lf": pf.LayerSpec(
        layer=(3, 0),
        description=(
            "[Si_Etch2_LF_120nm] Waveguide layer, defines both strip and rib. "
            "Light-field: layer will be protected."
        ),
        color="#ff80a8",
        pattern=patterns["I6"],
    ),
    "wg_df": pf.LayerSpec(
        layer=(4, 0),
        description=(
            "[Si_Etch2_DF_120nm] Waveguide layer, defines both strip and rib. "
            "Dark-field: layer will be etched."
        ),
        color="#8183ff",
        pattern=patterns["I6"],
    ),
    "rib_slab": pf.LayerSpec(
        layer=(5, 0),
        description=(
            "[Si_Etch3_LF_100nm_to_BOX] Rib protect layer. Light-field: layer will be protected."
        ),
        color="#80a8ff",
        pattern=patterns["I6"],
    ),
    "heater_fil": pf.LayerSpec(
        layer=(39, 0),
        description=(
            "[Heat_Fil_LF] Heater filaments (light). Light-field: layer will become metal."
        ),
        color="#9580ff",
        pattern=patterns["I9"],
    ),
    "contact_pad": pf.LayerSpec(
        layer=(41, 0),
        description=(
            "[Heat_CP_LF] Heater contact pads (light). Light-field: layer will become metal."
        ),
        color="#80a8ff",
        pattern=patterns["I10"],
    ),
    "FloorPlan": pf.LayerSpec(
        layer=(99, 0),
        description=("[FloorPlan] Cell outline"),
        color="#f3ff80",
        pattern=patterns["I1"],
    ),
    "Label_Etch_DF": pf.LayerSpec(
        layer=(100, 0),
        description=(
            "[Label_Etch_DF] Labels (dark), "
            "Dark-field: layer will be etched"
            "Will not be checked in DRC."
        ),
        color="#8000ff",
        pattern=patterns["I1"],
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
    "strip": 0.22,
    "rib_slab": 0.1,
    "ebeam_gratings": 0.125,
    "duv_gratings": 0.15,
    "tox": 2.0,
    "heater_fil": 0.15,
    "contact_pad": 0.22,
}

# _tolerances = {
#     "box": 0.0,
#     "strip": 0.02,
#     "rib_slab": 0.02,
#     "ebeam_gratings": 0.01,
#     "duv_gratings": 0.01,
#     "tox": 0.2,
#     "heater_fil": 0.01,
#     "contact_pad": 0.01,
# }
