"""Imports and fits the pdk material data."""
import pathlib

import numpy as np
from tidy3d import PoleResidue
from tidy3d.plugins.dispersion import FastDispersionFitter

fname_si = pathlib.Path(__file__).parent / "Si.csv"
fname_sio2 = pathlib.Path(__file__).parent / "SiO2.csv"

def _load_material_data()-> tuple[PoleResidue, PoleResidue]:
    """Load and fits the material data for silicon and silicon dioxide."""
    # Load the data from the CSV files.
    data_si = np.loadtxt(fname_si, skiprows=1, delimiter=",")
    wvl_um_si = data_si[:, 0]
    n_si = data_si[:, 1]

    data_sio2 = np.loadtxt(fname_sio2, skiprows=1, delimiter=",")
    wvl_um_sio2 = data_sio2[:, 0]*1e-3 # Data is in nm, convert to um
    n_sio2 = data_sio2[:, 1]

    wvl_um_range = (max(wvl_um_si[0], wvl_um_sio2[0]), min(wvl_um_si[-1], wvl_um_sio2[-1]))
    print(f"Fitting range: {wvl_um_range[0]:.3f} um to {wvl_um_range[1]:.3f} um")

    # Create the fitters
    fitter_si = FastDispersionFitter(wvl_um=wvl_um_si, n_data=n_si, wvl_range=wvl_um_range)
    fitter_sio2 = FastDispersionFitter(wvl_um=wvl_um_sio2, n_data=n_sio2, wvl_range=wvl_um_range)

    # Fit the data
    medium_si, _ = fitter_si.fit(max_num_poles=3)
    medium_sio2, _ = fitter_sio2.fit(max_num_poles=3)

    return (medium_si, medium_sio2)
