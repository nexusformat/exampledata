
**The following is output from running nxvalidate against each generated file**
```
########################################################################################################################

NXarchive.hdf5 passed validation

########################################################################################################################

definition=NXarpes.nxdl.xml message="Rank mismatch expected 1, found 0" nxdlPath=/NXentry/NXinstrument/NXdetector/sensor_size sev=error dataPath=/untitled_entry/untitled_instrument/analyser/sensor_size dataFile=NXarpes.hdf5
definition=NXarpes.nxdl.xml message="Rank mismatch expected 1, found 0" nxdlPath=/NXentry/NXinstrument/NXdetector/region_origin sev=error dataPath=/untitled_entry/untitled_instrument/analyser/region_origin dataFile=NXarpes.hdf5
definition=NXarpes.nxdl.xml message="Rank mismatch expected 1, found 0" nxdlPath=/NXentry/NXinstrument/NXdetector/region_size sev=error dataPath=/untitled_entry/untitled_instrument/analyser/region_size dataFile=NXarpes.hdf5
3 errors and 0 warnings found when validating NXarpes.hdf5

########################################################################################################################

NXcanSAS.hdf5 passed validation

########################################################################################################################

NXdirecttof.hdf5 passed validation

########################################################################################################################

message="Failed to open data file" sev=fatal dataFile=nxdlformat.xsl
0 errors and 0 warnings found when validating nxdlformat.xsl

########################################################################################################################

definition=NXfluo.nxdl.xml message="Required link energy missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/energy sev=error dataPath=/entry/data/energy dataFile=NXfluo.hdf5
definition=NXfluo.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/data/data dataFile=NXfluo.hdf5
2 errors and 0 warnings found when validating NXfluo.hdf5

########################################################################################################################

NXindirecttof.hdf5 passed validation

########################################################################################################################

NXiqproc.hdf5 passed validation

########################################################################################################################

definition=NXlauetof.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/name/data dataFile=NXlauetof.hdf5
definition=NXlauetof.nxdl.xml message="Required link time_of_flight missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/time_of_flight sev=error dataPath=/entry/name/time_of_flight dataFile=NXlauetof.hdf5
2 errors and 0 warnings found when validating NXlauetof.hdf5

########################################################################################################################

definition=NXmonopd.nxdl.xml message="Required link polar_angle missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/polar_angle sev=error dataPath=/entry/untitled_data/polar_angle dataFile=NXmonopd.hdf5
definition=NXmonopd.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/untitled_data/data dataFile=NXmonopd.hdf5
2 errors and 0 warnings found when validating NXmonopd.hdf5

########################################################################################################################

definition=NXmx.nxdl.xml message="Cannot even find the starting point of the depends_on chain, !some char data!" nxdlPath=/NXentry/NXsample/name sev=error dataPath=/untitled_entry/untitled_sample/depends_on dataFile=NXmx.hdf5
definition=NXmx.nxdl.xml message="Cannot even find the starting point of the depends_on chain, !some char data!" nxdlPath=/NXentry/NXinstrument/NXdetector sev=error dataPath=/untitled_entry/untitled_instrument/untitled_detector/depends_on dataFile=NXmx.hdf5
definition=NXmx.nxdl.xml message="Rank mismatch expected 4, found 3" nxdlPath=/NXentry/NXinstrument/NXdetector/angular_calibration sev=error dataPath=/untitled_entry/untitled_instrument/untitled_detector/angular_calibration dataFile=NXmx.hdf5
definition=NXmx.nxdl.xml message="Rank mismatch expected 4, found 3" nxdlPath=/NXentry/NXinstrument/NXdetector/flatfield sev=error dataPath=/untitled_entry/untitled_instrument/untitled_detector/flatfield dataFile=NXmx.hdf5
definition=NXmx.nxdl.xml message="Rank mismatch expected 4, found 3" nxdlPath=/NXentry/NXinstrument/NXdetector/flatfield_error sev=error dataPath=/untitled_entry/untitled_instrument/untitled_detector/flatfield_error dataFile=NXmx.hdf5
definition=NXmx.nxdl.xml message="Rank mismatch expected 4, found 3" nxdlPath=/NXentry/NXinstrument/NXdetector/flatfield_errors sev=error dataPath=/untitled_entry/untitled_instrument/untitled_detector/flatfield_errors dataFile=NXmx.hdf5
6 errors and 1 warnings found when validating NXmx.hdf5

########################################################################################################################

definition=NXrefscan.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/data/data dataFile=NXrefscan.hdf5
definition=NXrefscan.nxdl.xml message="Required link rotation_angle missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/rotation_angle sev=error dataPath=/entry/data/rotation_angle dataFile=NXrefscan.hdf5
definition=NXrefscan.nxdl.xml message="Required link polar_angle missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/polar_angle sev=error dataPath=/entry/data/polar_angle dataFile=NXrefscan.hdf5
3 errors and 0 warnings found when validating NXrefscan.hdf5

########################################################################################################################

definition=NXreftof.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/data/data dataFile=NXreftof.hdf5
definition=NXreftof.nxdl.xml message="Required link time_binning missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/time_binning sev=error dataPath=/entry/data/time_binning dataFile=NXreftof.hdf5
2 errors and 0 warnings found when validating NXreftof.hdf5

########################################################################################################################

definition=NXsas.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/untitled_entry/data/data dataFile=NXsas.hdf5
1 errors and 0 warnings found when validating NXsas.hdf5

########################################################################################################################

definition=NXsastof.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/untitled_entry/data/data dataFile=NXsastof.hdf5
definition=NXsastof.nxdl.xml message="Required link time_of_flight missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/time_of_flight sev=error dataPath=/untitled_entry/data/time_of_flight dataFile=NXsastof.hdf5
2 errors and 0 warnings found when validating NXsastof.hdf5

########################################################################################################################

definition=NXscan.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/untitled_entry/untitled_data/data dataFile=NXscan.hdf5
definition=NXscan.nxdl.xml message="Required link rotation_angle missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/rotation_angle sev=error dataPath=/untitled_entry/untitled_data/rotation_angle dataFile=NXscan.hdf5
2 errors and 0 warnings found when validating NXscan.hdf5

########################################################################################################################

NXspe.hdf5 passed validation

########################################################################################################################

NXsqom.hdf5 passed validation

########################################################################################################################

definition=NXstxm.nxdl.xml message="Invalid NXDL entry, missing rank on dimensions field" nxdlPath=/NXentry/NXinstrument/NXdetector/data sev=error dataPath=/untitled_entry/untitled_instrument/sample_x/data dataFile=NXstxm.hdf5
1 errors and 1 warnings found when validating NXstxm.hdf5

########################################################################################################################

definition=NXtas.nxdl.xml message="Required link ei missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/ei sev=error dataPath=/entry/untitled_data/ei dataFile=NXtas.hdf5
definition=NXtas.nxdl.xml message="Required link ef missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/ef sev=error dataPath=/entry/untitled_data/ef dataFile=NXtas.hdf5
definition=NXtas.nxdl.xml message="Required link en missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/en sev=error dataPath=/entry/untitled_data/en dataFile=NXtas.hdf5
definition=NXtas.nxdl.xml message="Required link qh missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/qh sev=error dataPath=/entry/untitled_data/qh dataFile=NXtas.hdf5
definition=NXtas.nxdl.xml message="Required link qk missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/qk sev=error dataPath=/entry/untitled_data/qk dataFile=NXtas.hdf5
definition=NXtas.nxdl.xml message="Required link ql missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/ql sev=error dataPath=/entry/untitled_data/ql dataFile=NXtas.hdf5
definition=NXtas.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/untitled_data/data dataFile=NXtas.hdf5
7 errors and 0 warnings found when validating NXtas.hdf5

########################################################################################################################

definition=NXtofnpd.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/data/data dataFile=NXtofnpd.hdf5
definition=NXtofnpd.nxdl.xml message="Required link detector_number missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/detector_number sev=error dataPath=/entry/data/detector_number dataFile=NXtofnpd.hdf5
definition=NXtofnpd.nxdl.xml message="Required link time_of_flight missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/time_of_flight sev=error dataPath=/entry/data/time_of_flight dataFile=NXtofnpd.hdf5
3 errors and 0 warnings found when validating NXtofnpd.hdf5

########################################################################################################################

definition=NXtofraw.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/data/data dataFile=NXtofraw.hdf5
definition=NXtofraw.nxdl.xml message="Required link detector_number missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/detector_number sev=error dataPath=/entry/data/detector_number dataFile=NXtofraw.hdf5
definition=NXtofraw.nxdl.xml message="Required link time_of_flight missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/time_of_flight sev=error dataPath=/entry/data/time_of_flight dataFile=NXtofraw.hdf5
3 errors and 0 warnings found when validating NXtofraw.hdf5

########################################################################################################################

definition=NXtofsingle.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/data/data dataFile=NXtofsingle.hdf5
definition=NXtofsingle.nxdl.xml message="Required link detector_number missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/detector_number sev=error dataPath=/entry/data/detector_number dataFile=NXtofsingle.hdf5
definition=NXtofsingle.nxdl.xml message="Required link time_of_flight missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/time_of_flight sev=error dataPath=/entry/data/time_of_flight dataFile=NXtofsingle.hdf5
3 errors and 0 warnings found when validating NXtofsingle.hdf5

########################################################################################################################

definition=NXtomo.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/data/data dataFile=NXtomo.hdf5
definition=NXtomo.nxdl.xml message="Required link rotation_angle missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/rotation_angle sev=error dataPath=/entry/data/rotation_angle dataFile=NXtomo.hdf5
definition=NXtomo.nxdl.xml message="Required link image_key missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/image_key sev=error dataPath=/entry/data/image_key dataFile=NXtomo.hdf5
3 errors and 0 warnings found when validating NXtomo.hdf5

########################################################################################################################

definition=NXtomophase.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/data/data dataFile=NXtomophase.hdf5
definition=NXtomophase.nxdl.xml message="Required link rotation_angle missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/rotation_angle sev=error dataPath=/entry/data/rotation_angle dataFile=NXtomophase.hdf5
2 errors and 0 warnings found when validating NXtomophase.hdf5

########################################################################################################################

NXtomoproc.hdf5 passed validation

########################################################################################################################

definition=NXxas.nxdl.xml message="Required link energy missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/energy sev=error dataPath=/untitled_entry/untitled_data/energy dataFile=NXxas.hdf5
definition=NXxas.nxdl.xml message="Required link absorbed_beam missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/absorbed_beam sev=error dataPath=/untitled_entry/untitled_data/absorbed_beam dataFile=NXxas.hdf5
2 errors and 0 warnings found when validating NXxas.hdf5

########################################################################################################################

NXxasproc.hdf5 passed validation

########################################################################################################################

definition=NXxbase.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/untitled_data/data dataFile=NXxbase.hdf5
1 errors and 0 warnings found when validating NXxbase.hdf5

########################################################################################################################

definition=NXxeuler.nxdl.xml message="Required link polar_angle missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/polar_angle sev=error dataPath=/entry/name/polar_angle dataFile=NXxeuler.hdf5
definition=NXxeuler.nxdl.xml message="Required link rotation_angle missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/rotation_angle sev=error dataPath=/entry/name/rotation_angle dataFile=NXxeuler.hdf5
definition=NXxeuler.nxdl.xml message="Required link chi missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/chi sev=error dataPath=/entry/name/chi dataFile=NXxeuler.hdf5
definition=NXxeuler.nxdl.xml message="Required link phi missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/phi sev=error dataPath=/entry/name/phi dataFile=NXxeuler.hdf5
definition=NXxeuler.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/name/data dataFile=NXxeuler.hdf5
5 errors and 0 warnings found when validating NXxeuler.hdf5

########################################################################################################################

definition=NXxkappa.nxdl.xml message="Required link polar_angle missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/polar_angle sev=error dataPath=/entry/name/polar_angle dataFile=NXxkappa.hdf5
definition=NXxkappa.nxdl.xml message="Required link rotation_angle missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/rotation_angle sev=error dataPath=/entry/name/rotation_angle dataFile=NXxkappa.hdf5
definition=NXxkappa.nxdl.xml message="Required link kappa missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/kappa sev=error dataPath=/entry/name/kappa dataFile=NXxkappa.hdf5
definition=NXxkappa.nxdl.xml message="Required link phi missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/phi sev=error dataPath=/entry/name/phi dataFile=NXxkappa.hdf5
definition=NXxkappa.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/name/data dataFile=NXxkappa.hdf5
5 errors and 0 warnings found when validating NXxkappa.hdf5

########################################################################################################################

NXxlaue.hdf5 passed validation

########################################################################################################################

NXxlaueplate.hdf5 passed validation

########################################################################################################################

definition=NXxnb.nxdl.xml message="Required link polar_angle missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/polar_angle sev=error dataPath=/entry/name/polar_angle dataFile=NXxnb.hdf5
definition=NXxnb.nxdl.xml message="Required link tilt missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/tilt sev=error dataPath=/entry/name/tilt dataFile=NXxnb.hdf5
definition=NXxnb.nxdl.xml message="Required link rotation_angle missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/rotation_angle sev=error dataPath=/entry/name/rotation_angle dataFile=NXxnb.hdf5
definition=NXxnb.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/name/data dataFile=NXxnb.hdf5
4 errors and 0 warnings found when validating NXxnb.hdf5

########################################################################################################################

definition=NXxrot.nxdl.xml message="Required link rotation_angle missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/rotation_angle sev=error dataPath=/entry/name/rotation_angle dataFile=NXxrot.hdf5
definition=NXxrot.nxdl.xml message="Required link data missing or not pointing to an HDF5 object" nxdlPath=/NXentry/NXdata/data sev=error dataPath=/entry/name/data dataFile=NXxrot.hdf5
2 errors and 0 warnings found when validating NXxrot.hdf5

########################################################################################################################
`