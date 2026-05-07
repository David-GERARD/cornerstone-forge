"""Shared utilities for importing PDK components from GDS files."""

import pathlib
import warnings

import photonforge as pf
import yaml

_GDS_DIR = pathlib.Path(__file__).parent / "gds"


def _import_component_with_ports(component_name: str, tech: pf.Technology) -> pf.Component:
    """Import a PDK component from its GDS file and attach its ports from the YAML spec.

    Looks for ``<component_name>.gds`` and ``<component_name>.yaml`` in the
    ``gds/`` directory alongside this module.  Ports with ``port_type:
    vertical_te`` are ignored.  The port ``input_direction`` is derived from
    the YAML ``orientation`` field as ``(orientation + 180) % 360``, i.e. the
    direction power travels *into* the component, opposite to the outward port
    normal.

    Args:
        component_name: Name of the component, matching the GDS cell name and
            the stem of the ``.gds`` / ``.yaml`` files (e.g.
            ``"SOI220nm_1310nm_TE_RIB_2x1_MMI"``).
        tech: The technology to use for loading the GDS and interpreting the port specs.

    Returns:
        The loaded component with optical and electrical ports attached.

    Raises:
        FileNotFoundError: If the ``.gds`` file does not exist.

    Warns:
        UserWarning: If the ``.yaml`` port-spec file does not exist; the
            component is returned without ports in that case.
    """
    gds_path = _GDS_DIR / f"{component_name}.gds"
    yaml_path = _GDS_DIR / f"{component_name}.yaml"

    if not gds_path.exists():
        raise FileNotFoundError(f"GDS file not found: {gds_path}")

    components = pf.load_layout(str(gds_path), technology=tech)
    component = components[component_name]

    if not yaml_path.exists():
        warnings.warn(
            f"YAML port spec not found: {yaml_path}. No ports will be added.", stacklevel=2
        )
        return component

    with open(yaml_path) as f:
        spec = yaml.safe_load(f)

    for port_def in spec.get("ports", []):
        if port_def.get("port_type") == "vertical_te":
            continue

        # input_direction is the direction power travels into the component,
        # which is opposite to the outward orientation of the port face.
        input_direction = (port_def["orientation"] + 180) % 360
        port = pf.Port(
            center=port_def["center"],
            input_direction=input_direction,
            spec=tech.ports[port_def["cross_section"]],
        )
        component.add_port(port, f"P{port_def['name'][1:]}")

    return component
