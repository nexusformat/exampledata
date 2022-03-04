 
import numpy as np
from nexusformat.nexus import *
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = NXroot()

# Create the GROUPS 
root['/entry'] = NXentry()
root['/entry'].attrs['EX_required'] = 'true'
root['/entry/instrument'] = NXinstrument()
root['/entry/instrument'].attrs['EX_required'] = 'true'
root['/entry/instrument/source'] = NXsource()
root['/entry/instrument/source'].attrs['EX_required'] = 'true'
root['/entry/instrument/monochromator'] = NXmonochromator()
root['/entry/instrument/monochromator'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector'] = NXdetector()
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
root['/entry/sample'] = NXsample()
root['/entry/sample'].attrs['EX_required'] = 'true'
root['/entry/control'] = NXmonitor()
root['/entry/control'].attrs['EX_required'] = 'true'
root['/entry/data'] = NXdata()
root['/entry/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/attenuator'] = NXattenuator()
root['/entry/instrument/attenuator'].attrs['EX_required'] = 'true'
root['/entry/name'] = NXdata()
root['/entry/name'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
root['/entry/title'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry/start_time'] = NXfield('2022-03-04T14:56:40.218872')
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXxbase
#	 NXxrot
 
root['/entry/definition'] = NXfield('NXxbase')
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
#	 electron
 
root['/entry/instrument/source/probe'] = NXfield('neutron')
root['/entry/instrument/source/probe'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/probe'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/monochromator/wavelength'] = NXfield(1.0)
root['/entry/instrument/monochromator/wavelength'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/monochromator/wavelength'].attrs['EX_required'] = 'true'
root['/entry/instrument/monochromator/wavelength'].attrs['units'] = 'NX_WAVELENGTH'
 
root['/entry/instrument/detector/data'] = NXfield(1)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/entry/instrument/detector/x_pixel_size'] = NXfield(1.0)
root['/entry/instrument/detector/x_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/x_pixel_size'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/x_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/y_pixel_size'] = NXfield(1.0)
root['/entry/instrument/detector/y_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/y_pixel_size'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/y_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/distance'] = NXfield(1.0)
root['/entry/instrument/detector/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/distance'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/frame_start_number'] = NXfield(1)
root['/entry/instrument/detector/frame_start_number'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/frame_start_number'].attrs['EX_required'] = 'true'
 
root['/entry/sample/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample/orientation_matrix'] = NXfield(1.0)
root['/entry/sample/orientation_matrix'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/orientation_matrix'].attrs['EX_required'] = 'true'
 
root['/entry/sample/unit_cell'] = NXfield(1.0)
root['/entry/sample/unit_cell'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/unit_cell'].attrs['EX_required'] = 'true'
 
root['/entry/sample/temperature'] = NXfield(1.0)
root['/entry/sample/temperature'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/temperature'].attrs['EX_required'] = 'true'
 
root['/entry/sample/x_translation'] = NXfield(1.0)
root['/entry/sample/x_translation'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/x_translation'].attrs['EX_required'] = 'true'
root['/entry/sample/x_translation'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/sample/y_translation'] = NXfield(1.0)
root['/entry/sample/y_translation'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/y_translation'].attrs['EX_required'] = 'true'
root['/entry/sample/y_translation'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/sample/distance'] = NXfield(1.0)
root['/entry/sample/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/distance'].attrs['EX_required'] = 'true'
root['/entry/sample/distance'].attrs['units'] = 'NX_LENGTH'
 
# Valid enumeration values for root['/entry/control']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/control/mode'] = NXfield('monitor')
root['/entry/control/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/control/mode'].attrs['EX_required'] = 'true'
 
root['/entry/control/preset'] = NXfield(1.0)
root['/entry/control/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/preset'].attrs['EX_required'] = 'true'
 
root['/entry/control/integral'] = NXfield(1.0)
root['/entry/control/integral'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/integral'].attrs['EX_required'] = 'true'
root['/entry/control/integral'].attrs['units'] = 'NX_ANY'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXxbase
#	 NXxrot
 
root['/entry/instrument/detector/polar_angle'] = NXfield(1.0)
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector/beam_center_x'] = NXfield(1.0)
root['/entry/instrument/detector/beam_center_x'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/beam_center_x'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/beam_center_x'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/beam_center_y'] = NXfield(1.0)
root['/entry/instrument/detector/beam_center_y'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/beam_center_y'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/beam_center_y'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/attenuator/attenuator_transmission'] = NXfield(1.0)
root['/entry/instrument/attenuator/attenuator_transmission'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/attenuator/attenuator_transmission'].attrs['EX_required'] = 'true'
root['/entry/instrument/attenuator/attenuator_transmission'].attrs['units'] = 'NX_ANY'
 
root['/entry/sample/rotation_angle'] = NXfield(1.0)
root['/entry/sample/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/rotation_angle'].attrs['axis'] = '1'
root['/entry/sample/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample/rotation_angle_step'] = NXfield(1.0)
root['/entry/sample/rotation_angle_step'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/rotation_angle_step'].attrs['EX_required'] = 'true'
root['/entry/sample/rotation_angle_step'].attrs['axis'] = '1'
root['/entry/sample/rotation_angle_step'].attrs['units'] = 'NX_ANGLE'

# Create the LINKS 
root['/entry/data/data'] = NXlink(target='/entry/instrument/detector/data')

# Create the LINKS 
root['/entry/name/rotation_angle'] = NXlink(target='/entry/sample/rotation_angle')

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms '
root['/entry/instrument/detector/data'].attrs['EX_doc'] = 'The area detector data, the first dimension is always the number of scan points, the second and third are the number of pixels in x and y. The origin is always assumed to be in the center of the detector. maxOccurs is limited to the the number of detectors on your instrument. '
root['/entry/instrument/detector'].attrs['EX_doc'] = 'The name of the group is detector if there is only one detector, if there are several, names have to be detector1, detector2, ...detectorn. '
root['/entry/instrument/detector/frame_start_number'].attrs['EX_doc'] = 'This is the start number of the first frame of a scan. In PX one often scans a couple of frames on a give sample, then does something else, then returns to the same sample and scans some more frames. Each time with a new data file. This number helps concatenating such measurements. '
root['/entry/sample/name'].attrs['EX_doc'] = 'Descriptive name of sample '
root['/entry/sample/orientation_matrix'].attrs['EX_doc'] = 'The orientation matrix according to Busing and Levy conventions. This is not strictly necessary as the UB can always be derived from the data. But let us bow to common usage which includes the UB nearly always. '
root['/entry/sample/unit_cell'].attrs['EX_doc'] = 'The unit cell, a, b, c, alpha, beta, gamma. Again, not strictly necessary, but normally written. '
root['/entry/sample/temperature'].attrs['EX_doc'] = 'The sample temperature or whatever sensor represents this value best '
root['/entry/sample/x_translation'].attrs['EX_doc'] = 'Translation of the sample along the X-direction of the laboratory coordinate system '
root['/entry/sample/y_translation'].attrs['EX_doc'] = 'Translation of the sample along the Y-direction of the laboratory coordinate system '
root['/entry/sample/distance'].attrs['EX_doc'] = 'Translation of the sample along the Z-direction of the laboratory coordinate system '
root['/entry/control/mode'].attrs['EX_doc'] = 'Count to a preset value based on either clock time (timer) or received monitor counts (monitor). '
root['/entry/control/preset'].attrs['EX_doc'] = 'preset value for time or monitor '
root['/entry/control/integral'].attrs['EX_doc'] = 'Total integral monitor counts '
root['/entry/data'].attrs['EX_doc'] = 'The name of this group id data if there is only one detector; if there are several the names will be data1, data2, data3 and will point to the corresponding detector groups in the instrument hierarchy. '
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms. '
root['/entry/instrument/detector/polar_angle'].attrs['EX_doc'] = 'The polar_angle (two theta) where the detector is placed. '
root['/entry/instrument/detector/beam_center_x'].attrs['EX_doc'] = 'This is the x position where the direct beam would hit the detector. This is a length, not a pixel position, and can be outside of the actual detector. '
root['/entry/instrument/detector/beam_center_y'].attrs['EX_doc'] = 'This is the y position where the direct beam would hit the detector. This is a length, not a pixel position, and can be outside of the actual detector. '
root['/entry/sample/rotation_angle'].attrs['EX_doc'] = 'This is an array holding the sample rotation start angle at each scan point '
root['/entry/sample/rotation_angle_step'].attrs['EX_doc'] = 'This is an array holding the step made for sample rotation angle at each scan point '
 

# Create the ATTRIBUTES 
 
# Valid enumeration values for root['/entry/instrument/detector/data']['signal'] are: 
#	 1
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
root.attrs['default'] = 'entry'
root['/entry/data'].set_default()
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'

# Save the file
root.save('NXxrot.nxs', 'w')


