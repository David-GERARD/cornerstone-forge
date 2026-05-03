# csforge-si_220nm_passive

[PhotonForge](https://docs.flexcompute.com/projects/photonforge/en/latest/) PDK for **Cornerstone's SOI 220 nm passive process**.

Provides a parametric `pf.Technology` definition and a complete component catalogue covering O-band (1310 nm) and C-band (1550 nm), backed by Cornerstone GDS cells and YAML port specs.
Process data sourced from [cornerstone-uos/cornerstone-pdk](https://github.com/cornerstone-uos/cornerstone-pdk/tree/main/Si_220nm_passive).

---

## Quick start

```python
import photonforge as pf
import csforge_si_220nm_passive as pdk

# Build the technology and set it globally
tech = pdk.csforge_si_220nm_pdk()
pf.config.default_technology = tech

# List all available component names
print(pdk.component_names)

# Fetch and inspect a component
wg = pdk.components["SOI220nm_1550nm_TE_STRIP_Waveguide"]
print(list(wg.ports.keys()))  # ['o1', 'o2']
```

---

## Process overview

The SOI 220 nm passive process uses a standard Silicon-on-Insulator stack. Nominal layer thicknesses:

| Layer | Alias | Thickness (µm) | Material | Notes |
|-------|-------|---------------|----------|-------|
| Buried oxide (BOX) | `box` | 3.00 | SiO₂ | Below Si device layer |
| Strip waveguide | `strip` | 0.22 | Si | Full-etch — 220 nm |
| Rib slab | `rib_slab` | 0.10 | Si | Partial-etch slab |
| EBL gratings | `ebeam_gratings` | 0.125 | Si | Shallow e-beam etch |
| DUV gratings | `duv_gratings` | 0.150 | Si | Shallow DUV etch |
| Top oxide (TOX) | `tox` | 2.00 | SiO₂ | Upper cladding |
| Heater filament | `heater_fil` | 0.15 | TiN | Above TOX |
| Contact pad | `contact_pad` | 0.22 | Al | Electrically connected to heater |

---

## Layer map

| Alias | GDS Layer | Description |
|-------|-----------|-------------|
| `grating_ebl` | (60, 0) | EBL grating couplers — dark-field, 94 nm etch |
| `grating_duv` | (6, 0) | DUV grating couplers — dark-field, 70 nm etch |
| `wg_lf` | (3, 0) | Waveguide — light-field, 120 nm etch |
| `wg_df` | (4, 0) | Waveguide — dark-field, 120 nm etch |
| `rib_slab` | (5, 0) | Rib slab protect — light-field, 100 nm to BOX |
| `heater_fil` | (39, 0) | TiN heater filaments — light-field |
| `contact_pad` | (41, 0) | Al contact pads — light-field |
| `FloorPlan` | (99, 0) | Cell outline |
| `Label_Etch_DF` | (100, 0) | Labels — dark-field, not DRC-checked |

`heater_fil` and `contact_pad` are declared electrically shorted in the technology.

---

## Port specs

| Name | Waveguide | Band | Width (µm) | Modes | n_eff target | Default bend radius (µm) |
|------|-----------|------|-----------|-------|-------------|--------------------------|
| `strip_1310nm` | Strip | O (1310 nm) | 0.40 | 2 — TE + TM | 2.52 | 10 |
| `rib_1310nm_TE` | Rib | O (1310 nm) | 0.40 | 1 — TE only | 2.52 | 25 |
| `strip_1550nm` | Strip | C (1550 nm) | 0.45 | 2 — TE + TM | 2.38 | 10 |
| `rib_1550nm_TE` | Rib | C (1550 nm) | 0.45 | 1 — TE only | 2.38 | 25 |
| `dc` | — | — | 80.0 | — | — | 0 (electrical) |

---

## Technology API

### `csforge_si_220nm_pdk`

```python
from csforge_si_220nm_passive import csforge_si_220nm_pdk

tech = csforge_si_220nm_pdk()                          # process-nominal defaults
tech = csforge_si_220nm_pdk(waveguide_thickness=0.25)  # override a thickness
tech = csforge_si_220nm_pdk(include_substrate=True)    # add Si substrate
```

All parameters have process-nominal defaults and can be overridden individually:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `box_thickness` | 3.00 µm | BOX layer thickness |
| `waveguide_thickness` | 0.22 µm | Strip Si thickness |
| `rib_slab_thickness` | 0.10 µm | Rib slab thickness |
| `ebeam_gratings_thickness` | 0.125 µm | EBL grating etch depth |
| `duv_gratings_thickness` | 0.150 µm | DUV grating etch depth |
| `tox_thickness` | 2.00 µm | Top oxide thickness |
| `heater_fil_thickness` | 0.15 µm | TiN heater thickness |
| `contact_pad_thickness` | 0.22 µm | Al contact pad thickness |
| `sidewall_angle_si` | 5.0° | Sidewall angle for all Si extrusions |
| `sio2` | dispersive SiO₂ | SiO₂ optical/electrical medium |
| `si` | dispersive Si | Silicon optical/electrical medium |
| `tin` | TiN multi-physics | TiN optical + heat + electrical medium |
| `al` | Al (Rakic 1995) | Aluminium medium |
| `air` | ε = 1 | Background medium |
| `include_substrate` | `False` | Append a semi-infinite Si substrate below BOX |

---

## Component catalogue

### O-band — 1310 nm

| Component | Type | Waveguide | Ports | Port spec |
|-----------|------|-----------|-------|-----------|
| `SOI220nm_1310nm_TE_RIB_2x1_MMI` | 2×1 MMI | RIB | o1, o2, o3 | `rib_1310nm_TE` |
| `SOI220nm_1310nm_TE_RIB_2x2_MMI` | 2×2 MMI | RIB | o1, o2, o3, o4 | `rib_1310nm_TE` |
| `SOI220nm_1310nm_TE_RIB_90_Degree_Bend` | 90° bend | RIB | o1, o2 | `rib_1310nm_TE` |
| `SOI220nm_1310nm_TE_RIB_Grating_Coupler` | Grating coupler | RIB | o1 | `rib_1310nm_TE` |
| `SOI220nm_1310nm_TE_RIB_Waveguide` | Straight waveguide | RIB | o1, o2 | `rib_1310nm_TE` |
| `SOI220nm_1310nm_TE_RIB_Waveguide_Crossing` | Waveguide crossing | RIB | o1, o2, o3, o4 | `rib_1310nm_TE` |
| `SOI220nm_1310nm_TE_STRIP_2x1_MMI` | 2×1 MMI | STRIP | o1, o2, o3 | `strip_1310nm` |
| `SOI220nm_1310nm_TE_STRIP_2x2_MMI` | 2×2 MMI | STRIP | o1, o2, o3, o4 | `strip_1310nm` |
| `SOI220nm_1310nm_TE_STRIP_90_Degree_Bend` | 90° bend | STRIP | o1, o2 | `strip_1310nm` |
| `SOI220nm_1310nm_TE_STRIP_Grating_Coupler` | Grating coupler | STRIP | o1 | `strip_1310nm` |
| `SOI220nm_1310nm_TE_STRIP_Waveguide` | Straight waveguide | STRIP | o1, o2 | `strip_1310nm` |
| `SOI220nm_1310nm_TE_STRIP_Waveguide_Crossing` | Waveguide crossing | STRIP | o1, o2, o3, o4 | `strip_1310nm` |

### C-band — 1550 nm

| Component | Type | Waveguide | Ports | Port spec |
|-----------|------|-----------|-------|-----------|
| `SOI220nm_1550nm_TE_RIB_2x1_MMI` | 2×1 MMI | RIB | o1, o2, o3 | `rib_1550nm_TE` |
| `SOI220nm_1550nm_TE_RIB_2x2_MMI` | 2×2 MMI | RIB | o1, o2, o3, o4 | `rib_1550nm_TE` |
| `SOI220nm_1550nm_TE_RIB_90_Degree_Bend` | 90° bend | RIB | o1, o2 | `rib_1550nm_TE` |
| `SOI220nm_1550nm_TE_RIB_EBL_Apodised_Grating_Coupler` | Apodised GC (EBL) | RIB | o1 | `rib_1550nm_TE` |
| `SOI220nm_1550nm_TE_RIB_Grating_Coupler` | Grating coupler | RIB | o1 | `rib_1550nm_TE` |
| `SOI220nm_1550nm_TE_RIB_MZI` | MZI with heater | RIB | e1, e2 | `dc` |
| `SOI220nm_1550nm_TE_RIB_Waveguide` | Straight waveguide | RIB | o1, o2 | `rib_1550nm_TE` |
| `SOI220nm_1550nm_TE_RIB_Waveguide_Crossing` | Waveguide crossing | RIB | o1, o2, o3, o4 | `rib_1550nm_TE` |
| `SOI220nm_1550nm_TE_STRIP_2x1_MMI` | 2×1 MMI | STRIP | o1, o2, o3 | `strip_1550nm` |
| `SOI220nm_1550nm_TE_STRIP_2x2_MMI` | 2×2 MMI | STRIP | o1, o2, o3, o4 | `strip_1550nm` |
| `SOI220nm_1550nm_TE_STRIP_90_Degree_Bend` | 90° bend | STRIP | o1, o2 | `strip_1550nm` |
| `SOI220nm_1550nm_TE_STRIP_Grating_Coupler` | Grating coupler | STRIP | o1 | `strip_1550nm` |
| `SOI220nm_1550nm_TE_STRIP_MZI` | MZI with heater | STRIP | e1, e2 | `dc` |
| `SOI220nm_1550nm_TE_STRIP_Waveguide` | Straight waveguide | STRIP | o1, o2 | `strip_1550nm` |
| `SOI220nm_1550nm_TE_STRIP_Waveguide_Crossing` | Waveguide crossing | STRIP | o1, o2, o3, o4 | `strip_1550nm` |

**Note on MZI ports:** The MZI components expose electrical `dc` ports (`e1`, `e2`) for the integrated TiN heater. The waveguide input/output connections are internal to the GDS cell.

---

## Package API

```python
import csforge_si_220nm_passive as pdk

pdk.csforge_si_220nm_pdk    # parametric technology factory
pdk.components              # dict[str, pf.Component] — all components
pdk.component_names         # list[str] — all names (oband + cband)
pdk.oband_components        # dict — O-band components
pdk.oband_component_names   # list — O-band names
pdk.cband_components        # dict — C-band components
pdk.cband_component_names   # list — C-band names
pdk.__version__             # str — version from pyproject.toml
pdk.plot_cross_section()    # Tidy3D cross-section visualisation
```
