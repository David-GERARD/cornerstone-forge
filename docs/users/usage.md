# Usage

!!! warning "Coming soon"
    Full usage documentation will be published alongside the PyPI release.

---

## Preview

Once installed, the packages are used as PhotonForge technology and component providers:

```python
import photonforge as pf
import csforge_si_220nm_passive as pdk

# Register the technology
tech = pdk.csforge_si_220nm_pdk()
pf.config.default_technology = tech

# Use a component from the catalogue
mmi = pdk.components["SOI220nm_1550nm_TE_STRIP_2x1_MMI"]
print(list(mmi.ports.keys()))   # ['o1', 'o2', 'o3']
```

For the full component catalogue and technology API, see the [PDK reference](../pdks/csforge-si_220nm_passive.md).
