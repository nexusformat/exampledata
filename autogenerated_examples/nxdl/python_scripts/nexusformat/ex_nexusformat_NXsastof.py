from nexusformat.nexus import *
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = NXroot()
root['/entry'] = NXentry()
root['/entry'].attrs['EX_required'] = 'true'
root['/entry/instrument'] = NXinstrument()
root['/entry/instrument'].attrs['EX_required'] = 'true'
root['/entry/instrument/source'] = NXsource()
root['/entry/instrument/source'].attrs['EX_required'] = 'true'
root['/entry/instrument/collimator'] = NXcollimator()
root['/entry/instrument/collimator'].attrs['EX_required'] = 'true'
root['/entry/instrument/collimator/geometry'] = NXgeometry()
root['/entry/instrument/collimator/geometry'].attrs['EX_required'] = 'true'
root['/entry/instrument/collimator/geometry/shape'] = NXshape()
root['/entry/instrument/collimator/geometry/shape'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector'] = NXdetector()
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
root['/entry/sample'] = NXsample()
root['/entry/sample'].attrs['EX_required'] = 'true'
root['/entry/control'] = NXmonitor()
root['/entry/control'].attrs['EX_required'] = 'true'
root['/entry/data'] = NXdata()
root['/entry/data'].attrs['EX_required'] = 'true'
 
root['/entry/title'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry/start_time'] = NXfield('2021-03-29T13:50:55.488684')
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXsastof
 
root['/entry/definition'] = NXfield('NXsastof')
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source/type'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/source/type'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/type'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/source/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/source']['probe'] are: 
#	 neutron
#	 x-ray
 
root['/entry/instrument/source/probe'] = NXfield('neutron')
root['/entry/instrument/source/probe'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/probe'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/collimator/geometry/shape']['shape'] are: 
#	 nxcylinder
#	 nxbox
 
root['/entry/instrument/collimator/geometry/shape/shape'] = NXfield('nxcylinder')
root['/entry/instrument/collimator/geometry/shape/shape'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/collimator/geometry/shape/shape'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/collimator/geometry/shape/size'] = NXfield(1.0)
root['/entry/instrument/collimator/geometry/shape/size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/collimator/geometry/shape/size'].attrs['EX_required'] = 'true'
root['/entry/instrument/collimator/geometry/shape/size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/data'] = NXfield(1.0)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/entry/instrument/detector/time_of_flight'] = NXfield(1.0)
root['/entry/instrument/detector/time_of_flight'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/time_of_flight'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/time_of_flight'].attrs['units'] = 'NX_TIME_OF_FLIGHT'
 
root['/entry/instrument/detector/distance'] = NXfield(1.0)
root['/entry/instrument/detector/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/distance'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/x_pixel_size'] = NXfield(1.0)
root['/entry/instrument/detector/x_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/x_pixel_size'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/x_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/y_pixel_size'] = NXfield(1.0)
root['/entry/instrument/detector/y_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/y_pixel_size'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/y_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/polar_angle'] = NXfield(1.0)
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector/azimuthal_angle'] = NXfield(1.0)
root['/entry/instrument/detector/azimuthal_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/azimuthal_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/azimuthal_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector/rotation_angle'] = NXfield(1.0)
root['/entry/instrument/detector/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector/aequatorial_angle'] = NXfield(1.0)
root['/entry/instrument/detector/aequatorial_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/aequatorial_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/aequatorial_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector/beam_center_x'] = NXfield(1.0)
root['/entry/instrument/detector/beam_center_x'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/beam_center_x'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/beam_center_x'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/beam_center_y'] = NXfield(1.0)
root['/entry/instrument/detector/beam_center_y'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/beam_center_y'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/beam_center_y'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample/aequatorial_angle'] = NXfield(1.0)
root['/entry/sample/aequatorial_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/aequatorial_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/aequatorial_angle'].attrs['units'] = 'NX_ANGLE'
 
# Valid enumeration values for root['/entry/control']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/control/mode'] = NXfield('monitor')
root['/entry/control/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/control/mode'].attrs['EX_required'] = 'true'
 
root['/entry/control/preset'] = NXfield(1.0)
root['/entry/control/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/preset'].attrs['EX_required'] = 'true'
 
root['/entry/control/data'] = NXfield(1)
root['/entry/control/data'].attrs['type'] = 'NX_INT'
root['/entry/control/data'].attrs['EX_required'] = 'true'
root['/entry/control/data'].attrs['primary'] = '1'
root['/entry/control/data'].attrs['signal'] = '1'
 
root['/entry/control/time_of_flight'] = NXfield(1.0)
root['/entry/control/time_of_flight'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/time_of_flight'].attrs['EX_required'] = 'true'
root['/entry/control/time_of_flight'].attrs['units'] = 'NX_TIME_OF_FLIGHT'
 
# Create the soft links 
root['/entry/data/data'] = NXlink(target='/entry/instrument/detector/data')
 
# Create the soft links 
root['/entry/data/time_of_flight'] = NXlink(target='/entry/instrument/detector/time_of_flight')
 
# Assign all of the doc strings
root['/entry/definition'].attrs['EX_doc'] = ' Official NeXus NXDL schema to which this file conforms '
root['/entry/instrument/source/type'].attrs['EX_doc'] = ' type of radiation source '
root['/entry/instrument/source/name'].attrs['EX_doc'] = ' Name of the radiation source '
root['/entry/instrument/collimator/geometry/shape/size'].attrs['EX_doc'] = ' The collimation length '
root['/entry/instrument/detector/data'].attrs['EX_doc'] = ' This is area detector data, of number of x-pixel versus number of y-pixels. Since the beam center is to be determined as a step of data reduction, it is not necessary to document or assume the position of the beam center in acquired data. '
root['/entry/instrument/detector/distance'].attrs['EX_doc'] = ' The distance between detector and sample '
root['/entry/instrument/detector/x_pixel_size'].attrs['EX_doc'] = ' Physical size of a pixel in x-direction '
root['/entry/instrument/detector/y_pixel_size'].attrs['EX_doc'] = ' Size of a pixel in y direction '
root['/entry/instrument/detector/beam_center_x'].attrs['EX_doc'] = ' This is the x position where the direct beam would hit the detector. This is a   length, not a pixel position, and can be outside of the actual detector. '
root['/entry/instrument/detector/beam_center_y'].attrs['EX_doc'] = ' This is the y position where the direct beam would hit the detector. This is a   length, not a pixel position, and can be outside of the actual detector. '
root['/entry/instrument/name'].attrs['EX_doc'] = ' Name of the instrument actually used to perform the experiment '
root['/entry/sample/name'].attrs['EX_doc'] = ' Descriptive name of sample '
root['/entry/control/mode'].attrs['EX_doc'] = ' Count to a preset value based on either clock time (timer) or received monitor counts (monitor). '
root['/entry/control/preset'].attrs['EX_doc'] = ' preset value for time or monitor '
 
root['/entry'].attrs['entry'] = 'SAMPLE-CHAR-DATA'
root.attrs['default'] = 'entry'
root['/entry/data'].set_default()
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'
root.save('NXsastof.nxs', 'w')


