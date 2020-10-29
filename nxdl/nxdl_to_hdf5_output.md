
**C:\Continuum\anaconda3\python.exe C:/controls/test/nexusformat/exampledata/nxdl_to_hdf5.py -d applications**
```
	Process this entire directory [applications]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXarchive.nxdl.xml]
	exporting: [NXarchive]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXarchive.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXarpes.nxdl.xml]
	exporting: [NXarpes]
		Error: Incorrect number of dim sections for this dimensions specification, should be at least [2] found [0]
		[/NXentry/NXinstrument/analyser/sensor_size/]
		Error: Incorrect number of dim sections for this dimensions specification, should be at least [2] found [0]
		[/NXentry/NXinstrument/analyser/region_origin/]
		Error: Incorrect number of dim sections for this dimensions specification, should be at least [2] found [0]
		[/NXentry/NXinstrument/analyser/region_size/]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXarpes.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXcanSAS.nxdl.xml]
	exporting: [NXcanSAS]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXcanSAS.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXdirecttof.nxdl.xml]
	exporting: [NXdirecttof]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXdirecttof.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXfluo.nxdl.xml]
	exporting: [NXfluo]
	-Symbol Warning: the symbol [nenergy] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/entry/data/energy/] specifies a link target that does not exist in the generated file [/entry/instrument/fluorescence/energy]
	-Link Error: This field [/entry/data/data/] specifies a link target that does not exist in the generated file [/entry/instrument/fluorescence/data]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXfluo.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXindirecttof.nxdl.xml]
	exporting: [NXindirecttof]
	-Symbol Warning: the symbol [nDet] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [ndet] is being used but has not been defined in the Symbols table, setting to default value of 1
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXindirecttof.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXiqproc.nxdl.xml]
	exporting: [NXiqproc]
	-Symbol Warning: the symbol [NE] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [NQX] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [NQY] is being used but has not been defined in the Symbols table, setting to default value of 1
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXiqproc.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXlauetof.nxdl.xml]
	exporting: [NXlauetof]
	-Symbol Warning: the symbol [nTOF] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Most likely this [number of x pixels] should be a symbol but has not been entered in the definition as one
	-Most likely this [number of y pixels] should be a symbol but has not been entered in the definition as one
	-Link Error: This field [/entry/name/data/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/data]
	-Link Error: This field [/entry/name/time_of_flight/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/time_of_flight]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXlauetof.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXmonopd.nxdl.xml]
	exporting: [NXmonopd]
	-Symbol Warning: the symbol [i] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [ndet] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/entry/NXdata/polar_angle/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/polar_angle]
	-Link Error: This field [/entry/NXdata/data/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/data]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXmonopd.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXmx.nxdl.xml]
	symbol [dataRank] was not defined and passed in in the usr_args, so it will be auto calculated at every occurance
	symbol [np] was not defined and passed in in the usr_args, so using default value of 1 for [np]
	symbol [i] was not defined and passed in in the usr_args, so using default value of 1 for [i]
	symbol [j] was not defined and passed in in the usr_args, so using default value of 1 for [j]
	symbol [k] was not defined and passed in in the usr_args, so using default value of 1 for [k]
	symbol [m] was not defined and passed in in the usr_args, so using default value of 1 for [m]
	exporting: [NXmx]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXmx.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXrefscan.nxdl.xml]
	exporting: [NXrefscan]
	-Symbol Warning: the symbol [NP] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/entry/data/data/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/data]
	-Link Error: This field [/entry/data/rotation_angle/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/rotation_angle]
	-Link Error: This field [/entry/data/polar_angle/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/polar_angle]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXrefscan.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXreftof.nxdl.xml]
	exporting: [NXreftof]
	-Symbol Warning: the symbol [xsize] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [ysize] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [nTOF] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/entry/data/data/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/data]
	-Link Error: This field [/entry/data/time_binning/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/time_binning]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXreftof.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXsas.nxdl.xml]
	exporting: [NXsas]
	-Symbol Warning: the symbol [nXPixel] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [nYPixel] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/NXentry/data/data/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/data]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXsas.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXsastof.nxdl.xml]
	exporting: [NXsastof]
	-Symbol Warning: the symbol [nXPixel] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [nYPixel] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [nTOF] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/NXentry/data/data/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/data]
	-Link Error: This field [/NXentry/data/time_of_flight/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/time_of_flight]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXsastof.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXscan.nxdl.xml]
	exporting: [NXscan]
	-Symbol Warning: the symbol [NP] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [xdim] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [ydim] is being used but has not been defined in the Symbols table, setting to default value of 1
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXscan.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXspe.nxdl.xml]
	exporting: [NXspe]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXspe.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXsqom.nxdl.xml]
	exporting: [NXsqom]
	-Symbol Warning: the symbol [NP] is being used but has not been defined in the Symbols table, setting to default value of 1
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXsqom.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXstxm.nxdl.xml]
	symbol [numP] was not defined and passed in in the usr_args, so using default value of 1 for [numP]
	symbol [numE] was not defined and passed in in the usr_args, so using default value of 1 for [numE]
	symbol [numY] was not defined and passed in in the usr_args, so using default value of 1 for [numY]
	symbol [numX] was not defined and passed in in the usr_args, so using default value of 1 for [numX]
	exporting: [NXstxm]
	-Symbol Warning: the symbol [NumP] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [NumE] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [NumY] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [NumX] is being used but has not been defined in the Symbols table, setting to default value of 1
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXstxm.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXtas.nxdl.xml]
	exporting: [NXtas]
	-Symbol Warning: the symbol [np] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/entry/NXdata/ei/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/monochromator:NXcrystal/ei]
	-Link Error: This field [/entry/NXdata/ef/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/analyzer:NXcrystal/ef]
	-Link Error: This field [/entry/NXdata/en/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/en]
	-Link Error: This field [/entry/NXdata/qh/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/qh]
	-Link Error: This field [/entry/NXdata/qk/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/qk]
	-Link Error: This field [/entry/NXdata/ql/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/ql]
	-Link Error: This field [/entry/NXdata/data/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/data]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXtas.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXtofnpd.nxdl.xml]
	exporting: [NXtofnpd]
	-Symbol Warning: the symbol [ndet] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [ntimechan] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/entry/data/data/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/data]
	-Link Error: This field [/entry/data/detector_number/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/detector_number]
	-Link Error: This field [/entry/data/time_of_flight/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/time_of_flight]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXtofnpd.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXtofraw.nxdl.xml]
	exporting: [NXtofraw]
	-Symbol Warning: the symbol [ndet] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [ntimechan] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/entry/data/data/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/data]
	-Link Error: This field [/entry/data/detector_number/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/detector_number]
	-Link Error: This field [/entry/data/time_of_flight/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/time_of_flight]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXtofraw.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXtofsingle.nxdl.xml]
	exporting: [NXtofsingle]
	-Symbol Warning: the symbol [xsize] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [ysize] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [ntimechan] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [ndet] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/entry/data/data/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/data]
	-Link Error: This field [/entry/data/detector_number/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/detector_number]
	-Link Error: This field [/entry/data/time_of_flight/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/time_of_flight]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXtofsingle.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXtomo.nxdl.xml]
	symbol [nFrames] was not defined and passed in in the usr_args, so using default value of 1 for [nFrames]
	symbol [xsize] was not defined and passed in in the usr_args, so using default value of 1 for [xsize]
	symbol [ysize] was not defined and passed in in the usr_args, so using default value of 1 for [ysize]
	exporting: [NXtomo]
	-Link Error: This field [/entry/data/data/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/detector:NXdetector/data]
	-Link Error: This field [/entry/data/rotation_angle/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/rotation_angle]
	-Link Error: This field [/entry/data/image_key/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/detector:NXdetector/image_key]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXtomo.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXtomophase.nxdl.xml]
	symbol [nBrightFrames] was not defined and passed in in the usr_args, so using default value of 1 for [nBrightFrames]
	symbol [nDarkFrames] was not defined and passed in in the usr_args, so using default value of 1 for [nDarkFrames]
	symbol [nSampleFrames] was not defined and passed in in the usr_args, so using default value of 1 for [nSampleFrames]
	symbol [nPhase] was not defined and passed in in the usr_args, so using default value of 1 for [nPhase]
	symbol [xsize] was not defined and passed in in the usr_args, so using default value of 1 for [xsize]
	symbol [ysize] was not defined and passed in in the usr_args, so using default value of 1 for [ysize]
	exporting: [NXtomophase]
	-Most likely this [nDarkFrames + nBrightFrames + nSampleFrame] should be a symbol but has not been entered in the definition as one
	-Link Error: This field [/entry/data/data/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/sample:NXdetector/data]
	-Link Error: This field [/entry/data/rotation_angle/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/rotation_angle]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXtomophase.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXtomoproc.nxdl.xml]
	symbol [nx] was not defined and passed in in the usr_args, so using default value of 1 for [nx]
	symbol [ny] was not defined and passed in in the usr_args, so using default value of 1 for [ny]
	symbol [nz] was not defined and passed in in the usr_args, so using default value of 1 for [nz]
	exporting: [NXtomoproc]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXtomoproc.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXxas.nxdl.xml]
	exporting: [NXxas]
	-Symbol Warning: the symbol [np] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/NXentry/NXdata/energy/] specifies a link target that does not exist in the generated file [/entry/instrument/monochromator/energy]
	-Link Error: This field [/NXentry/NXdata/absorbed_beam/] specifies a link target that does not exist in the generated file [/entry/instrument/absorbed_beam/data]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXxas.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXxasproc.nxdl.xml]
	exporting: [NXxasproc]
	-Symbol Warning: the symbol [np] is being used but has not been defined in the Symbols table, setting to default value of 1
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXxasproc.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXxbase.nxdl.xml]
	exporting: [NXxbase]
	-Symbol Warning: the symbol [np] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [NP] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Most likely this [number of x pixels] should be a symbol but has not been entered in the definition as one
	-Most likely this [number of y pixels] should be a symbol but has not been entered in the definition as one
	-Link Error: This field [/entry/NXdata/data/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/data]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXxbase.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXxeuler.nxdl.xml]
	exporting: [NXxeuler]
	-Symbol Warning: the symbol [np] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/entry/name/polar_angle/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/polar_angle]
	-Link Error: This field [/entry/name/rotation_angle/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/rotation_angle]
	-Link Error: This field [/entry/name/chi/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/chi]
	-Link Error: This field [/entry/name/phi/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/phi]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXxeuler.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXxkappa.nxdl.xml]
	exporting: [NXxkappa]
	-Symbol Warning: the symbol [np] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/entry/name/polar_angle/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/polar_angle]
	-Link Error: This field [/entry/name/rotation_angle/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/rotation_angle]
	-Link Error: This field [/entry/name/kappa/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/kappa]
	-Link Error: This field [/entry/name/phi/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/phi]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXxkappa.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXxlaue.nxdl.xml]
	exporting: [NXxlaue]
	-Symbol Warning: the symbol [ne] is being used but has not been defined in the Symbols table, setting to default value of 1
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXxlaue.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXxlaueplate.nxdl.xml]
	exporting: [NXxlaueplate]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXxlaueplate.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXxnb.nxdl.xml]
	exporting: [NXxnb]
	-Symbol Warning: the symbol [np] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/entry/name/polar_angle/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/polar_angle]
	-Link Error: This field [/entry/name/tilt/] specifies a link target that does not exist in the generated file [/NXentry/NXinstrument/NXdetector/tilt]
	-Link Error: This field [/entry/name/rotation_angle/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/rotation_angle]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXxnb.hdf5]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXxrot.nxdl.xml]
	exporting: [NXxrot]
	-Symbol Warning: the symbol [np] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Link Error: This field [/entry/name/rotation_angle/] specifies a link target that does not exist in the generated file [/NXentry/NXsample/rotation_angle]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXxrot.hdf5]
```
