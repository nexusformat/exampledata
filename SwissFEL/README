68 image lysozyme dataset recorded on the Jungfrau 16M detector at SwissFEL and formatted as a NeXus file.

Data provided by Meitian Wang at PSI.

Here, only the NeXus master file is provided. The full set of files, including pixel data and mask file, are available here: https://doi.org/10.5281/zenodo.3352357.  

To create a new NeXus master file, assuming DIALS is installed in the folder $DIALS, use this command:

libtbx.python $DIALS/modules/cctbx_project/xfel/swissfel/jf16m_cxigeom2nexus.py unassembled_file=lyso009a_0087.JF07T32V01.h5 geom_file=16M_bernina_backview_optimized_adu_quads.geom wavelength=1.368479 detector_distance=97.830 mask_file=lyso009a_0087.JF07T32V01.mask.h5

Geometry file is in CrystFEL format but has been realigned to group the modules hierarchically into quadrants.

View the data using DIALS: dials.image_viewer lyso009a_0087.JF07T32V01_master.h5

Process the data using DIALS, treating the images as stills, assuming 64 cores available on the system:
dials.stills_process mp.nproc=64 lyso009a_0087.JF07T32V01_master.h5 dispersion.gain=10 known_symmetry.space_group=P43212 known_symmetry.unit_cell=77,77,37,90,90,90 refinement_protocol.d_min_start=2.5

Download DIALS at dials.github.io.
