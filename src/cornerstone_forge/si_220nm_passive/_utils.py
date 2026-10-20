"""Shared utilities for importing PDK components from GDS files."""

import csv as _csv
import pathlib
import re as _re
import warnings

import photonforge as pf
import tidy3d as td
import yaml

_GDS_DIR = pathlib.Path(__file__).parent / "gds"
_DATA_DIR = pathlib.Path(__file__).parent / "data" / "sparams"

_SPARAM_COL_RE = _re.compile(r"^s_(\d+)@TE0_(\d+)@TE0_(re|im)$")


def _import_component_with_ports(component_name: str, tech: pf.Technology) -> pf.Component:
    """Import a PDK component from its GDS file and attach its ports from the YAML spec.

    Looks for ``<component_name>.gds`` and ``<component_name>.yaml`` in the
    ``gds/`` directory alongside this module.  Ports with ``port_type:
    vertical_te`` are attached as :class:`pf.FiberPort` instances, named
    ``FP<name>``; all other ports are attached as :class:`pf.Port` instances,
    named ``P<name[1:]>``.  The port ``input_direction`` is derived from
    the YAML ``orientation`` field as ``(orientation + 180) % 360``, i.e. the
    direction power travels *into* the component, opposite to the outward port
    normal.

    Args:
        component_name: Name of the component, matching the GDS cell name and
            the stem of the ``.gds`` / ``.yaml`` files (e.g.
            ``"SOI220nm_1310nm_TE_RIB_2x1_MMI"``).
        tech: The technology to use for loading the GDS and interpreting the port specs.

    Returns:
        The loaded component with optical, electrical, and fiber ports attached.

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
        # input_direction is the direction power travels into the component,
        # which is opposite to the outward orientation of the port face.
        input_direction = (port_def["orientation"] + 180) % 360
        if port_def.get("port_type") == "vertical_te":
            core = pf.Circle(port_def["width"] / 2)
            port = pf.FiberPort(
                center=(port_def["center"][0], port_def["center"][1], 0),
                input_vector=(1, 0, 0),
                size=(port_def["width"], port_def["width"]),
                extrusion_limits=(-50, 0.1),
                cross_section=[(core, td.Medium(permittivity=1.46**2))],
                num_modes=2,
                target_neff=2,
            )
            component.add_port(port, f"FP{port_def['name']}")
        else:
            port = pf.Port(
                center=port_def["center"],
                input_direction=input_direction,
                spec=tech.ports[port_def["cross_section"]],
            )
            component.add_port(port, f"P{port_def['name'][1:]}")

    return component


def _load_data_model(component_name: str, port_names: list[str]) -> pf.DataModel:
    """Load a :class:`pf.DataModel` from a CSV S-parameter file.

    Reads ``<component_name>.csv`` from the ``data/sparams/`` directory
    alongside this module.  Each row of the CSV corresponds to one wavelength
    point; columns are named ``s_<out>@TE0_<in>@TE0_re`` /
    ``s_<out>@TE0_<in>@TE0_im`` (1-based port indices) plus
    ``wavelength_μm``.

    Port indices in the CSV are positional: CSV port ``k`` (1-based)
    corresponds to ``port_names[k-1]``.  Wavelengths are converted to
    frequencies using ``pf.C_0 / wavelength_um`` (``pf.C_0`` is in µm/s,
    so the result is in Hz).

    The :class:`pf.SMatrix` ``elements`` keys follow the photonforge
    convention ``("in_port@mode", "out_port@mode")``.  Since all data
    are single-mode TE0, the mode suffix is ``@0`` (integer).

    Args:
        component_name: Component name that matches the CSV file stem (e.g.
            ``"SOI220nm_1550nm_TE_STRIP_2x2_MMI"``).
        port_names: Ordered list of component port names.  The i-th element
            corresponds to CSV port index ``i + 1`` (1-based).

    Returns:
        A :class:`pf.DataModel` populated from the CSV S-parameter data.

    Raises:
        FileNotFoundError: If the CSV file does not exist under
            ``data/sparams/``.
    """
    csv_path = _DATA_DIR / f"{component_name}.csv"
    if not csv_path.exists():
        raise FileNotFoundError(f"S-parameter CSV not found: {csv_path}")

    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = _csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)

    wavelengths_um = [float(row["wavelength_μm"]) for row in rows]
    # pf.C_0 is in µm/s; dividing by wavelength in µm gives frequency in Hz.
    frequencies = [pf.C_0 / wl for wl in wavelengths_um]

    re_cols: dict[tuple[int, int], list[float]] = {}
    im_cols: dict[tuple[int, int], list[float]] = {}
    for col in fieldnames:
        m = _SPARAM_COL_RE.match(col)
        if not m:
            continue
        out_1, in_1, part = int(m.group(1)), int(m.group(2)), m.group(3)
        values = [float(row[col]) for row in rows]
        if part == "re":
            re_cols[(out_1, in_1)] = values
        else:
            im_cols[(out_1, in_1)] = values

    n_freqs = len(frequencies)
    elements: dict[tuple[str, str], list[complex]] = {}
    for (out_1, in_1), re_vals in re_cols.items():
        in_port = port_names[in_1 - 1]
        out_port = port_names[out_1 - 1]
        im_vals = im_cols.get((out_1, in_1), [0.0] * n_freqs)
        elements[(f"{in_port}@0", f"{out_port}@0")] = [
            r + 1j * i for r, i in zip(re_vals, im_vals, strict=True)
        ]

    return pf.DataModel(s_matrix=pf.SMatrix(frequencies, elements))
