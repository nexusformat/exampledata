 
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
root['/entry/instrument/chopper'] = NXdisk_chopper()
root['/entry/instrument/chopper'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector'] = NXdetector()
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
root['/entry/sample'] = NXsample()
root['/entry/sample'].attrs['EX_required'] = 'true'
root['/entry/control'] = NXmonitor()
root['/entry/control'].attrs['EX_required'] = 'true'
root['/entry/data'] = NXdata()
root['/entry/data'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
root['/entry/title'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry/start_time'] = NXfield('2022-03-04T14:56:35.735539')
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
root['/entry/end_time'] = NXfield('2022-03-04T14:56:35.735539')
root['/entry/end_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/end_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXreftof
 
root['/entry/definition'] = NXfield('NXreftof')
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/name'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/chopper/distance'] = NXfield(1.0)
root['/entry/instrument/chopper/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/chopper/distance'].attrs['EX_required'] = 'true'
root['/entry/instrument/chopper/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/data'] = NXfield(1)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/entry/instrument/detector/time_of_flight'] = NXfield(1.0)
root['/entry/instrument/detector/time_of_flight'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/time_of_flight'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/time_of_flight'].attrs['axis'] = '3'
root['/entry/instrument/detector/time_of_flight'].attrs['units'] = 'NX_TIME_OF_FLIGHT'
 
root['/entry/instrument/detector/distance'] = NXfield(1.0)
root['/entry/instrument/detector/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/distance'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/polar_angle'] = NXfield(1.0)
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector/x_pixel_size'] = NXfield(1.0)
root['/entry/instrument/detector/x_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/x_pixel_size'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/x_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/y_pixel_size'] = NXfield(1.0)
root['/entry/instrument/detector/y_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/y_pixel_size'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/y_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/sample/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample/rotation_angle'] = NXfield(1.0)
root['/entry/sample/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
# Valid enumeration values for root['/entry/control']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/control/mode'] = NXfield('monitor')
root['/entry/control/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/control/mode'].attrs['EX_required'] = 'true'
 
root['/entry/control/preset'] = NXfield(1.0)
root['/entry/control/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/preset'].attrs['EX_required'] = 'true'
root['/entry/control/preset'].attrs['units'] = 'NX_ANY'
 
root['/entry/control/integral'] = NXfield(1)
root['/entry/control/integral'].attrs['type'] = 'NX_INT'
root['/entry/control/integral'].attrs['EX_required'] = 'true'
 
root['/entry/control/time_of_flight'] = NXfield(1.0)
root['/entry/control/time_of_flight'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/time_of_flight'].attrs['EX_required'] = 'true'
root['/entry/control/time_of_flight'].attrs['axis'] = '1'
root['/entry/control/time_of_flight'].attrs['units'] = 'NX_TIME_OF_FLIGHT'
 
root['/entry/control/data'] = NXfield(1)
root['/entry/control/data'].attrs['type'] = 'NX_INT'
root['/entry/control/data'].attrs['EX_required'] = 'true'
root['/entry/control/data'].attrs['signal'] = '1'

# Create the LINKS 
root['/entry/data/data'] = NXlink(target='/entry/instrument/detector/data')

# Create the LINKS 
root['/entry/data/time_binning'] = NXlink(target='/entry/title')

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms '
root['/entry/instrument/chopper/distance'].attrs['EX_doc'] = 'Distance between chopper and sample '
root['/entry/instrument/detector/time_of_flight'].attrs['EX_doc'] = 'Array of time values for each bin in a time-of-flight measurement '
root['/entry/sample/name'].attrs['EX_doc'] = 'Descriptive name of sample '
root['/entry/control/mode'].attrs['EX_doc'] = 'Count to a preset value based on either clock time (timer) or received monitor counts (monitor). '
root['/entry/control/preset'].attrs['EX_doc'] = 'preset value for time or monitor '
root['/entry/control/integral'].attrs['EX_doc'] = 'Total integral monitor counts '
root['/entry/control/time_of_flight'].attrs['EX_doc'] = 'Time channels '
root['/entry/control/data'].attrs['EX_doc'] = 'Monitor counts in each time channel '
 

# Create the ATTRIBUTES 
root.attrs['default'] = 'entry'
root['/entry/data'].set_default()
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'

# Save the file
root.save('NXreftof.nxs', 'w')


