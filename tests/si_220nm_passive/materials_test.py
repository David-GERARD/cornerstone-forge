"""Tests for the committed optical material fits."""

from pathlib import Path

import numpy as np
import pytest
import tidy3d as td

from cornerstone_forge.si_220nm_passive._material_fits import medium_si, medium_sio2

MATERIAL_DATA_DIR = Path(__file__).parents[2] / "tools" / "si_220nm_passive" / "material_data"
WAVELENGTH_RANGE_UM = (1.20036, 1.696618164)


@pytest.mark.parametrize(
    ("filename", "wavelength_scale", "medium"),
    (
        ("Si.csv", 1.0, medium_si),
        ("SiO2.csv", 1e-3, medium_sio2),
    ),
)
def test_material_fit(filename, wavelength_scale, medium):
    """Confirm that a committed model reproduces its source refractive indices."""
    data = np.loadtxt(MATERIAL_DATA_DIR / filename, skiprows=1, delimiter=",")
    wavelengths = data[:, 0] * wavelength_scale
    in_fit_range = (wavelengths >= WAVELENGTH_RANGE_UM[0]) & (wavelengths <= WAVELENGTH_RANGE_UM[1])

    fitted_n, _ = medium.nk_model(td.C_0 / wavelengths[in_fit_range])
    rms_error = np.sqrt(np.mean((fitted_n - data[in_fit_range, 1]) ** 2))

    assert rms_error < 1e-5
    assert medium.frequency_range == pytest.approx(
        (td.C_0 / WAVELENGTH_RANGE_UM[1], td.C_0 / WAVELENGTH_RANGE_UM[0])
    )
