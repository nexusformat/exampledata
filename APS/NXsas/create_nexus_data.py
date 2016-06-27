#!/usr/bin/env python

'''
create NeXus data file with the image data from these area detector data files

stores data according to the **NXsas** application definition

:deviation: **NXsas** describes a single frame raw 2-D SAS data image.
    We store a set of 2-D SAS images as a 3-D array.

:deviation: **NXsas** stores the counting time as a scalar: /entry/instrument/control/integral
    We store an array of count sample_times, one for each image frame.

:see: http://download.nexusformat.org/doc/html/classes/applications/NXsas.html
'''

import h5py
import os
import numpy
from spec2nexus import eznx


TARGET_FILE = 'nexus-example.hdf5'
FILE_SET = '''
/share1/USAXS_data/2016-06/06_23_IN625_775C_saxs/IN625AB_775C_3min_0378.hdf
/share1/USAXS_data/2016-06/06_23_IN625_775C_saxs/IN625AB_775C_30min_0383.hdf
/share1/USAXS_data/2016-06/06_23_IN625_775C_saxs/IN625AB_775C_58min_0388.hdf
/share1/USAXS_data/2016-06/06_23_IN625_775C_saxs/IN625AB_775C_86min_0393.hdf
/share1/USAXS_data/2016-06/06_23_IN625_775C_saxs/IN625AB_775C_112min_0398.hdf
/share1/USAXS_data/2016-06/06_23_IN625_775C_saxs/IN625AB_775C_140min_0403.hdf
/share1/USAXS_data/2016-06/06_23_IN625_775C_saxs/IN625AB_775C_168min_0408.hdf
/share1/USAXS_data/2016-06/06_23_IN625_775C_saxs/IN625AB_775C_196min_0413.hdf
/share1/USAXS_data/2016-06/06_23_IN625_775C_saxs/IN625AB_775C_223min_0418.hdf
/share1/USAXS_data/2016-06/06_23_IN625_775C_saxs/IN625AB_775C_240min_0421.hdf
'''.strip().split()
BLANK_FILE = '/share1/USAXS_data/2016-06/06_23_IN625_775C_saxs/HeaterBlank_30C_560min_0376.hdf'

frame_set, names, h5_files, monitor, sample_times = [], [], [], [], []
for fname in FILE_SET:
    h5 = h5py.File(fname, 'r')
    frame_set.append(h5['/entry/data/data'])
    monitor.append(h5['/entry/EPICS_PV_metadata/I0_cts_gated'][0])
    names.append(os.path.split(fname)[-1])
    sample_times.append(int(str(h5['/entry/sample/name'].value[0]).split('_')[-1][:-3]))
    # do not close the HDF5 files yet
    h5_files.append(h5)

h5_blank = h5py.File(BLANK_FILE, 'r')

# create file and group structure
root = eznx.makeFile(TARGET_FILE, default='entry')
nxentry = eznx.makeGroup(root, 'entry', 'NXentry', default='data')
nxdata = eznx.makeGroup(nxentry, 'data', 'NXdata', signal='frames', )
nxinstrument = eznx.makeGroup(nxentry, 'instrument', 'NXinstrument')
nxdetector = eznx.makeGroup(nxinstrument, 'detector', 'NXdetector')
nxsource = eznx.makeGroup(nxinstrument, 'source', 'NXsource')
nxmonochromator = eznx.makeGroup(nxinstrument, 'monochromator', 'NXmonochromator')
nxcollimator = eznx.makeGroup(nxinstrument, 'collimator', 'NXcollimator')
nxgeometry_slit = eznx.makeGroup(nxcollimator, 'geometry', 'NXgeometry')
nxshape_slit = eznx.makeGroup(nxgeometry_slit, 'shape', 'NXshape')
nxsample = eznx.makeGroup(nxinstrument, 'sample', 'NXsample')
nxmonitor = eznx.makeGroup(nxinstrument, 'control', 'NXmonitor')

# various metadata
eznx.addAttributes(root, creator=h5.attrs['creator'] + ' and spec2nexus.eznx')
eznx.write_dataset(nxentry, 'title', 'NeXus NXsas example')
eznx.write_dataset(nxentry, 'definition', 'NXsas', URL='http://download.nexusformat.org/doc/html/classes/applications/NXsas.html')
eznx.write_dataset(nxentry, 'start_time', h5_files[0].attrs['file_time'])
eznx.write_dataset(nxentry, 'end_time', h5_files[-1].attrs['file_time'])
eznx.write_dataset(nxdetector, 'frame_files', '\n'.join(names))
eznx.write_dataset(nxinstrument, 'name', 'APS 9-ID-C USAXS pinSAXS')
eznx.write_dataset(nxsource, 'type', 'Synchrotron X-ray Source')
eznx.write_dataset(nxsource, 'name', 'Advanced Photon Source Undulator A, sector 9ID-C')
eznx.write_dataset(nxsource, 'probe', 'x-ray')
eznx.write_dataset(nxsource, 'current', h5['/entry/EPICS_PV_metadata/SRcurrent'], units='mA')
eznx.write_dataset(nxsource, 'energy', float(7), units='GeV')
eznx.write_dataset(nxmonochromator, 'energy', h5['/entry/instrument/monochromator/energy'], units='keV')
eznx.write_dataset(nxmonochromator, 'wavelength', h5['/entry/EPICS_PV_metadata/wavelength'], units='Angstroms')
eznx.write_dataset(nxmonochromator, 'wavelength_spread', h5['/entry/EPICS_PV_metadata/wavelength_spread'], units='Angstroms/Angstroms')
eznx.write_dataset(nxshape_slit, 'shape', 'nxbox')
# next four are not defined in the NXsas specification
eznx.write_dataset(nxshape_slit, 'size_x', h5['/entry/EPICS_PV_metadata/USAXSslitHap'], units='mm')
eznx.write_dataset(nxshape_slit, 'size_y', h5['/entry/EPICS_PV_metadata/USAXSslitVap'], units='mm')
eznx.write_dataset(nxshape_slit, 'center_x', h5['/entry/EPICS_PV_metadata/USAXSslitHpos'], units='mm')
eznx.write_dataset(nxshape_slit, 'center_y', h5['/entry/EPICS_PV_metadata/USAXSslitVpos'], units='mm')
eznx.write_dataset(nxdetector, 'distance', h5['/entry/EPICS_PV_metadata/SDD'], units='mm')
eznx.write_dataset(nxdetector, 'x_pixel_size', h5['/entry/EPICS_PV_metadata/pin_ccd_pixel_size_x'], units='mm')
eznx.write_dataset(nxdetector, 'y_pixel_size', h5['/entry/EPICS_PV_metadata/pin_ccd_pixel_size_y'], units='mm')
eznx.write_dataset(nxdetector, 'beam_center_x', h5['/entry/EPICS_PV_metadata/pin_ccd_center_x'], units='mm')
eznx.write_dataset(nxdetector, 'beam_center_y', h5['/entry/EPICS_PV_metadata/pin_ccd_center_y'], units='mm')
eznx.write_dataset(nxdetector, 'beam_center_x_pixel', h5['/entry/EPICS_PV_metadata/pin_ccd_center_x_pixel'])
eznx.write_dataset(nxdetector, 'beam_center_y_pixel', h5['/entry/EPICS_PV_metadata/pin_ccd_center_y_pixel'])
eznx.write_dataset(nxsample, 'name', h5['/entry/EPICS_PV_metadata/SampleTitle'])
eznx.write_dataset(nxmonitor, 'mode', 'time')
eznx.write_dataset(nxmonitor, 'preset', h5['/entry/EPICS_PV_metadata/PresetTime'], units='s')
# NXsas specifies a scaler, we have a frame set so we record a 1-D array here
eznx.write_dataset(nxmonitor, 'integral', monitor, units='clock', clock_per_s='100000')

# the image data: a set of frames
# NXsas describes a 2-D single frame image, we are writing a 3-D multi-image frame set
# see: http://docs.h5py.org/en/latest/high/dataset.html#lossless-compression-filters
# full gzip compression (9) reduces THIS file size by ~50%
#ds = eznx.write_dataset(nxdetector, 'data', frame_set, units='counts')
ds = nxdetector.create_dataset('data', data=numpy.array(frame_set), compression='gzip', compression_opts=9)
eznx.addAttributes(ds, units='counts', compression='gzip', source_files='\n'.join(names))
eznx.makeLink(nxdata, ds, 'frames')
ds = eznx.write_dataset(nxsample, 'image_times', sample_times, units='minutes')
eznx.makeLink(nxdata, ds, 'sample_times')
ds = nxdetector.create_dataset('blank', data=h5_blank['/entry/data/data'], compression='gzip', compression_opts=9)
eznx.addAttributes(ds, units='counts')
eznx.addAttributes(ds, source_file=os.path.split(BLANK_FILE)[-1])
eznx.makeLink(nxdata, ds, 'blank')
eznx.write_dataset(nxdata, 'vertical', range(ds.shape[0]), units='pixels')
eznx.write_dataset(nxdata, 'horizontal', range(ds.shape[1]), units='pixels')
eznx.addAttributes(nxdata, axes='sample_times vertical horizontal'.split())
eznx.addAttributes(nxdata, sample_times_indices=[0,])
eznx.addAttributes(nxdata, vertical_indices=[1,])
eznx.addAttributes(nxdata, horizontal_indices=[2,])

# close the HDF5 output data file
root.close()

# Now, close the HDF5 source data files
[h5.close() for h5 in h5_files]
h5_blank.close()

##########################################################################

# structure of one of these files:
'''
IN625AB_775C_3min_0378.hdf
  @NeXus_version = 4.3.0
  @file_name = /mnt/share1/USAXS_data/2016-06/06_23_IN625_775C_saxs/IN625AB_775C_3min_0378.hdf
  @HDF5_Version = 1.8.13
  @file_time = 2016-06-23T12:02:31-06:00
  @creator = areaDetector NDFileNexus plugin v0.2
  @default = entry
  entry:NXentry
    @NX_class = NXentry
    @default = data
    @ADCoreVersion = 2.2.0
    AD_template_ID:char[66] = $Id: nexus_template_pilatus.xml 8473 2015-06-09 19:39:50Z jemian $
    definition:char[5] = NXsas
      @version = 1.0b
      @URL = http://download.nexusformat.org/doc/html/ClassDefinitions-Application.html#NXsas
    end_time:char[25] = Thu Jun 23 11:50:42 2016
    program_name:char[18] = NeXus areaDetector
    run_cycle:char[8] = 2016-02
    start_time:char[25] = Thu Jun 23 12:02:01 2016
    title:char[30] = pinSAXS for IN625AB_775C_3min
    EPICS_PV_metadata:NXcollection
      @NX_class = NXcollection
      @modified = 2015-06-09T14:31:00.450452
      APS_run_cycle:char[8] = 2016-02
        @pv = 9idcLAX:RunCycle
        @description = APS operating cycle
      EmptyFileName:char[13] = Unknown.hdf5
        @pv = 9idcLAX:USAXS_Pin:EmptyFileName
        @description = Name of file to use as empty scan
      EndTime:char[25] = Thu Jun 23 11:50:42 2016
        @pv = 9idcLAX:USAXS_Pin:EndExposureTime
        @description = image ending time
      GUPNumber:char[4] = PUP
        @pv = 9idcLAX:GUPNumber
        @description = GUP proposal number
      GuardslitHap:float64 = 0.9
        @pv = 9idcLAX:GSlit1H:size.VAL
        @description = Guard slit, horizontal aperture, mm
      GuardslitHpos:float64 = -1.06581410364e-14
        @pv = 9idcLAX:GSlit1H:center.VAL
        @description = Guard slit, horizontal position, mm
      GuardslitVap:float64 = 0.3
        @pv = 9idcLAX:GSlit1V:size.VAL
        @description = Guard slit, vertical aperture, mm
      GuardslitVpos:float64 = 2.22044604925e-16
        @pv = 9idcLAX:GSlit1V:center.VAL
        @description = Guard slit, vertical position, mm
      I000_cts:float64 = 0.0
        @pv = 9idb:scaler1_calc1.VAL
        @description = I000 counts
      I00_V:float64 = -0.0689697265625
        @pv = 9idcUSX:ath01:ana01:ai06
        @description = I00 voltage, V
      I00_cts:float64 = 1.0
        @pv = 9idcLAX:vsc:c0.S3
        @description = I00 counts
      I00_gain:float64 = 1000000000.0
        @pv = 9idcUSX:fem03:seq01:gain
        @description = I00 V/A gain
      I0_V:float64 = 0.946655273438
        @pv = 9idcUSX:ath01:ana01:ai05
        @description = I0 voltage, V
      I0_cts:float64 = 768876.0
        @pv = 9idcLAX:vsc:c0.S2
        @description = I0 counts
      I0_cts_gated:float64 = 2934680.0
        @pv = 9idcLAX:vsc:c1.S2
        @description = I0 counts gated
      I0_gain:float64 = 10000000.0
        @pv = 9idcUSX:fem02:seq01:gain
        @description = I0 V/A gain
      Linkam_ci94_temp:float64 = 775.0
        @pv = 9idcLAX:ci94:temp
        @description = Linkam_ci94_temp
      Linkam_ci94_temp2:float64 = 775.0
        @pv = 9idcLAX:ci94:temp2
        @description = Linkam_ci94_temp2
      PIN_Y:float64 = 12.8
        @pv = 9idcLAX:mxv:c0:m8.RBV
        @description = pinhole y stage position, mm
      PIN_Z:float64 = 12.998338
        @pv = 9idcLAX:mxv:c0:m2.RBV
        @description = pinhole z stage position, mm
      Pin_TrI0:float64 = 300072.0
        @pv = 9idcLAX:USAXS_Pin:Pin_TrI0
        @description = Pin_TrI0
      Pin_TrI0gain:float64 = 10000000.0
        @pv = 9idcLAX:USAXS_Pin:Pin_TrI0gain
        @description = Pin_TrI0gain
      Pin_TrPD:float64 = 2147763.0
        @pv = 9idcLAX:USAXS_Pin:Pin_TrPD
        @description = Pin_TrPD
      Pin_TrPDgain:float64 = 10000000.0
        @pv = 9idcLAX:USAXS_Pin:Pin_TrPDgain
        @description = Pin_TrPDgain
      PresetTime:float64 = 30.0
        @pv = usaxs_pilatus1:cam1:AcquireTime
        @description = specified time for this exposure, s
      SDD:float64 = 540.8
        @pv = 9idcLAX:USAXS_Pin:Distance
        @description = SDD: distance between sample and detector, mm
      SRcurrent:float64 = 101.91112448
        @pv = S:SRcurrentAI
        @description = Storage Ring Current, mA
      SampleTitle:char[30] = pinSAXS for IN625AB_775C_3min
        @pv = 9idcLAX:USAXS:sampleTitle
        @description = sample name
      ScanMacro:char[21] = 06_23_IN625_775C.dat
        @pv = 9idcLAX:SpecMacroFileName
        @description = name of SPEC macro file
      StartTime:char[25] = Thu Jun 23 12:02:01 2016
        @pv = 9idcLAX:USAXS_Pin:StartExposureTime
        @description = image starting time
      USAXS_Q:float64 = 9.28709817959e-06
        @pv = 9idcLAX:USAXS:Q
        @description = Q
      USAXSslitHap:float64 = 0.7998265
        @pv = 9idcLAX:m58:c2:m8
        @description = USAXS slit, horizontal aperture, mm
      USAXSslitHpos:float64 = 8.00000000112e-06
        @pv = 9idcLAX:m58:c2:m6
        @description = USAXS slit, horizontal position, mm
      USAXSslitVap:float64 = 0.2001505
        @pv = 9idcLAX:m58:c2:m7
        @description = USAXS slit, vertical aperture, mm
      USAXSslitVpos:float64 = 0.500036
        @pv = 9idcLAX:m58:c2:m5
        @description = USAXS slit, vertical position, mm
      UserName:char[19] = NIST, ANdrew Allen
        @pv = 9idcLAX:UserName
        @description = user name listed as GUP PI
      WAXS_X:float64 = 0.0
        @pv = 9idcLAX:m58:c0:m4.RBV
        @description = waxs x stage position, mm
      ccdProtection:int16 = 0
        @pv = 9idcLAX:ccdProtection
        @description = CCD protection bit
      filterAl:float64 = 0.0
        @pv = 9idcUSX:pf4:filterAl
        @description = Al filter, mm
      filterGlass:float64 = 0.0
        @pv = 9idcUSX:pf42:filterGlass
        @description = Glass filter, mm
      filterTi:float64 = 0.0
        @pv = 9idcUSX:pf4:filterTi
        @description = Ti filter, mm
      filterTrans:float64 = 1.0
        @pv = 9idcUSX:pf4:trans
        @description = filter transmission
      idE_ds:float64 = 21.1887254715
        @pv = ID09ds:Energy
        @description = ID energy, downstream, keV
      idE_us:float64 = 21.216753006
        @pv = ID09us:Energy
        @description = ID energy, upstream, keV
      is_2D_USAXS_scan:float64 = 0.0
        @pv = 9idcLAX:USAXS:is2DUSAXSscan
        @description = does this scan use 2D collimated geometry
      m2rp:float64 = 1.68
        @pv = 9idcUSX:pzt:m2
        @description = m2rp voltage, V
      monoE:float64 = 20.9999615757
        @pv = 9ida:BraggERdbkAO
        @description = monochromator energy, keV
      monoE_EGU:char[4] = keV
        @pv = 9ida:BraggERdbkAO.EGU
        @description = monochromator energy units
      mr_enc:float64 = 8.84545561142
        @pv = 9idcLAX:mr:encoder
        @description = mr readback, deg
      msrp:float64 = 5.005
        @pv = 9idcUSX:pzt:m4
        @description = msrp voltage, V
      mx:float64 = 23.0
        @pv = 9idcLAX:m58:c0:m2.RBV
        @description = mx stage position, mm
      my:float64 = 5.68434188608e-14
        @pv = 9idcLAX:m58:c0:m3.RBV
        @description = my stage position, mm
      pin_ccd_center_x:float64 = 17.1914
        @pv = 9idcLAX:USAXS_Pin:BeamCenterX:NXdetector
        @description = horizontal position of beam center on CCD, mm
      pin_ccd_center_x_pixel:float64 = 99.95
        @pv = 9idcLAX:USAXS_Pin:BeamCenterX
        @description = horizontal position of beam center on CCD, pixels
      pin_ccd_center_y:float64 = -0.9718
        @pv = 9idcLAX:USAXS_Pin:BeamCenterY:NXdetector
        @description = vertical position of beam center on CCD, mm
      pin_ccd_center_y_pixel:float64 = -5.65
        @pv = 9idcLAX:USAXS_Pin:BeamCenterY
        @description = vertical position of beam center on CCD, pixels
      pin_ccd_pixel_size_x:float64 = 0.172
        @pv = 9idcLAX:USAXS_Pin:PinPixSizeX
        @description = CCD pixel size, horizontal, mm
      pin_ccd_pixel_size_y:float64 = 0.172
        @pv = 9idcLAX:USAXS_Pin:PinPixSizeY
        @description = CCD pixel size, vertical, mm
      pin_ccd_tilt_x:float64 = 2.408
        @pv = 9idcLAX:USAXS_Pin:DetectorTiltX
        @description = CCD tilt, x direction, degrees
      pin_ccd_tilt_y:float64 = -7.879
        @pv = 9idcLAX:USAXS_Pin:DetectorTiltY
        @description = CCD tilt, y direction, degrees
      sa:float64 = -8.67896
        @pv = 9idcLAX:xps:c0:m7.RBV
        @description = sample azimuthal rotation, degrees
      scaler_freq:float64 = 10000000.0
        @pv = 9idcLAX:vsc:c0.FREQ
        @description = scaler frequency, Hz
      sthick:float64 = 0.033
        @pv = 9idcLAX:sampleThickness
        @description = sample thickness
      sx:float64 = -2.6
        @pv = 9idcLAX:m58:c2:m1.RBV
        @description = sample x stage position, mm
      sy:float64 = 0.1
        @pv = 9idcLAX:m58:c2:m2.RBV
        @description = sample y stage position, mm
      wavelength:float64 = 0.59040224218
        @pv = 9ida:BraggLambdaRdbkAO
        @description = monochromator wavelength, A
      wavelength_EGU:char[10] = Angstroms
        @pv = 9ida:BraggLambdaRdbkAO.EGU
        @description = monochromator wavelength units
      wavelength_spread:float64 = 8e-05
        @pv = 9idcLAX:WavelengthSpread
        @description = delta-lambda / lambda
    areaDetector_reduced_250:NXdata
      @NX_class = NXdata
      @timestamp = 2016-06-23 12:02:52
      @signal = R
      @axes = Q
      @Q_indices = 0
      Q:float64[249] = [0.021918980150849705, 0.028707726365588677, 0.035489034129379531, '...', 1.6798613941377709]
        @units = 1/A
      R:float64[249] = [1.8623465183045094e-05, 2.2082338884805095e-05, 0.0001484437904133914, '...', 0.0032147384021863532]
        @units = none
      dR:float64[249] = [1.7542873121017162e-06, 2.401995716943954e-06, 0.00042207664124416792, '...', 4.5081624461636254e-05]
        @units = none
    areaDetector_reduced_full:NXdata
      @NX_class = NXdata
      @timestamp = 2016-06-23 12:02:52
      @signal = R
      @axes = Q
      @Q_indices = 0
      Q:float64[993] = [0.019462155321490378, 0.021154511839111413, 0.022846867153066421, '...', 1.6823303208831488]
        @units = 1/A
      R:float64[993] = [2.0359971104174904e-05, 1.5901790541614984e-05, 2.0007048712052326e-05, '...', 0.0032690105905925008]
        @units = none
      x:float64[993] = [0.98899999999999988, 1.075, 1.1609999999999998, '...', 86.300999999999988]
        @units = mm
    control:NXmonitor
      @NX_class = NXmonitor
      integral:float64 = 768876.0
      mode:char[5] = timer
      preset:float64 = 30.0
    data:NXdata
      @NX_class = NXdata
      @signal = data
      data:int32[195,487] = __array
        __array = [
            [41, 38, 57, '...', 9820]
            [33, 43, 55, '...', 9367]
            [46, 34, 44, '...', 9159]
            ...
            [59, 43, 67, '...', 10831]
          ]
        @ImageCounter = 365
        @make = Dectris
        @model = Pilatus
        @maxSizeX = 487
        @maxSizeY = 195
        @USAXSmode = 06_23_IN625_775C.dat
      description:char[8] = Pilatus
        @make = Dectris
      local_name:char[12] = Pilatus 100K
      make:char[8] = Dectris
      model:char[8] = Pilatus
    instrument:NXinstrument
      @NX_class = NXinstrument
      name:char[5] = USAXS
      aperture:NXaperture
        @NX_class = NXaperture
        description:char[9] = USAXSslit
        hcenter:float64 = 8.00000000112e-06
        hsize:float64 = 0.7998265
        vcenter:float64 = 0.500036
        vsize:float64 = 0.2001505
      collimator:NXcollimator
        @NX_class = NXcollimator
        absorbing_material:char[8] = Tungsten
        geometry:NXgeometry
          @NX_class = NXgeometry
          shape:NXshape
            @NX_class = NXshape
            shape:char[5] = nxbox
            size:char[19] = see xsize and ysize
            xcenter:float64 = 8.00000000112e-06
            xsize:float64 = 0.7998265
            ycenter:float64 = 0.500036
            ysize:float64 = 0.2001505
      detector:NXdetector
        @NX_class = NXdetector
        beam_center_x:float64 = 17.1914
        beam_center_y:float64 = -0.9718
        distance:float64 = 540.8
        x_pixel_size:float64 = 0.172
        y_pixel_size:float64 = 0.172
      monochromator:NXmonochromator
        @NX_class = NXmonochromator
        energy:float64 = 20.9999615757
          @units = keV
        wavelength:float64 = 0.59040224218
          @units = Angstroms
        wavelength_spread:float64 = 8e-05
      source:NXsource
        @NX_class = NXsource
        facility_beamline:char[3] = 9ID
        facility_name:char[3] = APS
        facility_sector:char[7] = XSD/9ID
        facility_station:char[1] = C
        name:char[48] = Advanced Photon Source Undulator A, sector 9ID-C
        probe:char[5] = x-ray
        type:char[24] = Synchrotron X-ray Source
    link_rules:link_rules
      @NX_class = link_rules
      link --> /entry/instrument/detector/data
    sample:NXsample
      @NX_class = NXsample
      aequatorial_angle:float64 = -8.67896
        @units = degrees
      name:char[30] = pinSAXS for IN625AB_775C_3min
      thickness:float64 = 0.033
    user1:NXuser
      @NX_class = NXuser
      name:char[19] = NIST, ANdrew Allen
      proposal_number:char[4] = PUP
'''
