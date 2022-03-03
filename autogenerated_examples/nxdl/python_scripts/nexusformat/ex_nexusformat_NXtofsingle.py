 
import numpy as np
from nexusformat.nexus import *
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = NXroot()

# Create the GROUPS 
root['/entry'] = NXentry()
root['/entry'].attrs['EX_required'] = 'true'
root['/entry/user'] = NXuser()
root['/entry/user'].attrs['EX_required'] = 'true'
root['/entry/instrument'] = NXinstrument()
root['/entry/instrument'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector'] = NXdetector()
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
root['/entry/sample'] = NXsample()
root['/entry/sample'].attrs['EX_required'] = 'true'
root['/entry/monitor'] = NXmonitor()
root['/entry/monitor'].attrs['EX_required'] = 'true'
root['/entry/data'] = NXdata()
root['/entry/data'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
root['/entry/title'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry/start_time'] = NXfield('2022-03-03T14:34:16.763880')
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXtofsingle
 
root['/entry/definition'] = NXfield('NXtofsingle')
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/duration'] = NXfield(1.0)
root['/entry/duration'].attrs['type'] = 'NX_FLOAT'
root['/entry/duration'].attrs['EX_required'] = 'true'
 
root['/entry/pre_sample_flightpath'] = NXfield(1.0)
root['/entry/pre_sample_flightpath'].attrs['type'] = 'NX_FLOAT'
root['/entry/pre_sample_flightpath'].attrs['EX_required'] = 'true'
root['/entry/pre_sample_flightpath'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/user/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/user/name'].attrs['type'] = 'NX_CHAR'
root['/entry/user/name'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector/data'] = NXfield(1)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/entry/instrument/detector/distance'] = NXfield(1.0)
root['/entry/instrument/detector/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/distance'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/time_of_flight'] = NXfield(1.0)
root['/entry/instrument/detector/time_of_flight'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/time_of_flight'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/time_of_flight'].attrs['axis'] = '1'
root['/entry/instrument/detector/time_of_flight'].attrs['units'] = 'NX_TIME_OF_FLIGHT'
 
root['/entry/instrument/detector/polar_angle'] = NXfield(1.0)
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector/azimuthal_angle'] = NXfield(1.0)
root['/entry/instrument/detector/azimuthal_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/azimuthal_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/azimuthal_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/sample']['nature'] are: 
#	 powder
#	 liquid
#	 single crystal
 
root['/entry/sample/nature'] = NXfield('powder')
root['/entry/sample/nature'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/nature'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/monitor']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/monitor/mode'] = NXfield('monitor')
root['/entry/monitor/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/monitor/mode'].attrs['EX_required'] = 'true'
 
root['/entry/monitor/preset'] = NXfield(1.0)
root['/entry/monitor/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/monitor/preset'].attrs['EX_required'] = 'true'
 
root['/entry/monitor/distance'] = NXfield(1.0)
root['/entry/monitor/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/monitor/distance'].attrs['EX_required'] = 'true'
root['/entry/monitor/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/monitor/data'] = NXfield(1)
root['/entry/monitor/data'].attrs['type'] = 'NX_INT'
root['/entry/monitor/data'].attrs['EX_required'] = 'true'
root['/entry/monitor/data'].attrs['signal'] = '1'
 
root['/entry/monitor/time_of_flight'] = NXfield(1.0)
root['/entry/monitor/time_of_flight'].attrs['type'] = 'NX_FLOAT'
root['/entry/monitor/time_of_flight'].attrs['EX_required'] = 'true'
root['/entry/monitor/time_of_flight'].attrs['axis'] = '1'
root['/entry/monitor/time_of_flight'].attrs['units'] = 'NX_TIME_OF_FLIGHT'

# Create the LINKS 
root['/entry/data/data'] = NXlink(target='/entry/instrument/detector/data')

# Create the LINKS 
root['/entry/data/detector_number'] = NXlink(target='/entry/user/name')

# Create the LINKS 
root['/entry/data/time_of_flight'] = NXlink(target='/entry/instrument/detector/time_of_flight')

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms '
root['/entry/pre_sample_flightpath'].attrs['EX_doc'] = 'This is the flight path before the sample position. This can be determined by a chopper, by the moderator or the source itself. In other words: it the distance to the component which gives the T0 signal to the detector electronics. If another component in the NXinstrument hierarchy provides this information, this should be a link. '
root['/entry/instrument/detector/distance'].attrs['EX_doc'] = 'Distance to sample for the center of the detector '
root['/entry/instrument/detector/polar_angle'].attrs['EX_doc'] = 'polar angle for each detector element '
root['/entry/instrument/detector/azimuthal_angle'].attrs['EX_doc'] = 'azimuthal angle for each detector element '
root['/entry/sample/name'].attrs['EX_doc'] = 'Descriptive name of sample '
root['/entry/monitor/mode'].attrs['EX_doc'] = 'Count to a preset value based on either clock time (timer) or received monitor counts (monitor). '
root['/entry/monitor/preset'].attrs['EX_doc'] = 'preset value for time or monitor '
 

# Create the ATTRIBUTES 
root.attrs['default'] = 'entry'
root['/entry/data'].set_default()
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'

# Save the file
root.save('NXtofsingle.nxs', 'w')


