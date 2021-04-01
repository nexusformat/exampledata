 
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

# Create the FIELDS 
 
root['/entry/title'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry/start_time'] = NXfield('2021-03-29T15:51:40.531791')
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
root['/entry/end_time'] = NXfield('2021-03-29T15:51:40.534797')
root['/entry/end_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/end_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXrefscan
 
root['/entry/definition'] = NXfield('NXrefscan')
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
 
root['/entry/instrument/detector/polar_angle'] = NXfield(1.0)
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/polar_angle'].attrs['axis'] = '1'
root['/entry/instrument/detector/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
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
 
root['/entry/control/data'] = NXfield(1.0)
root['/entry/control/data'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/data'].attrs['EX_required'] = 'true'
root['/entry/control/data'].attrs['units'] = 'NX_ANY'

# Create the LINKS 
root['/entry/data/data'] = NXlink(target='/entry/instrument/detector/data')

# Create the LINKS 
root['/entry/data/rotation_angle'] = NXlink(target='/entry/sample/rotation_angle')

# Create the LINKS 
root['/entry/data/polar_angle'] = NXlink(target='/entry/instrument/detector/polar_angle')

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms '
root['/entry/sample/name'].attrs['EX_doc'] = 'Descriptive name of sample '
root['/entry/control/mode'].attrs['EX_doc'] = 'Count to a preset value based on either clock time (timer) or received monitor counts (monitor). '
root['/entry/control/preset'].attrs['EX_doc'] = 'preset value for time or monitor '
root['/entry/control/data'].attrs['EX_doc'] = 'Monitor counts for each step '
 

# Create the ATTRIBUTES 
root.attrs['default'] = 'entry'
root['/entry/data'].set_default()
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'

# Save the file
root.save('NXrefscan.nxs', 'w')


