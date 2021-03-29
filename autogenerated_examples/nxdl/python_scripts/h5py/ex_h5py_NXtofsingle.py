 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('NXtofsingle.h5', 'w')

# Create the GROUPS 
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('user')
root['/entry/user'].attrs['NX_class'] = 'NXuser'
root['/entry/user'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('instrument')
root['/entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/instrument'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('detector')
root['/entry/instrument/detector'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('monitor')
root['/entry/monitor'].attrs['NX_class'] = 'NXmonitor'
root['/entry/monitor'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('data')
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
root['/entry'].create_dataset(name='title', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='start_time', data='2021-03-29T15:07:34.849178', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXtofsingle
 
root['/entry'].create_dataset(name='definition', data='NXtofsingle', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='duration', data=1.0, maxshape=None)
root['/entry/duration'].attrs['type'] = 'NX_FLOAT'
root['/entry/duration'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='pre_sample_flightpath', data=1.0, maxshape=None)
root['/entry/pre_sample_flightpath'].attrs['type'] = 'NX_FLOAT'
root['/entry/pre_sample_flightpath'].attrs['EX_required'] = 'true'
root['/entry/pre_sample_flightpath'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/user'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/user/name'].attrs['type'] = 'NX_CHAR'
root['/entry/user/name'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector'].create_dataset(name='data', data=1, maxshape=None)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/entry/instrument/detector'].create_dataset(name='distance', data=1.0, maxshape=None)
root['/entry/instrument/detector/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/distance'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='time_of_flight', data=1.0, maxshape=None)
root['/entry/instrument/detector/time_of_flight'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/time_of_flight'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/time_of_flight'].attrs['axis'] = '1'
root['/entry/instrument/detector/time_of_flight'].attrs['units'] = 'NX_TIME_OF_FLIGHT'
 
root['/entry/instrument/detector'].create_dataset(name='polar_angle', data=1.0, maxshape=None)
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector'].create_dataset(name='azimuthal_angle', data=1.0, maxshape=None)
root['/entry/instrument/detector/azimuthal_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/azimuthal_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/azimuthal_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/sample']['nature'] are: 
#	 powder
#	 liquid
#	 single crystal
 
root['/entry/sample'].create_dataset(name='nature', data='powder', maxshape=None)
root['/entry/sample/nature'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/nature'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/monitor']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/monitor'].create_dataset(name='mode', data='monitor', maxshape=None)
root['/entry/monitor/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/monitor/mode'].attrs['EX_required'] = 'true'
 
root['/entry/monitor'].create_dataset(name='preset', data=1.0, maxshape=None)
root['/entry/monitor/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/monitor/preset'].attrs['EX_required'] = 'true'
 
root['/entry/monitor'].create_dataset(name='distance', data=1.0, maxshape=None)
root['/entry/monitor/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/monitor/distance'].attrs['EX_required'] = 'true'
root['/entry/monitor/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/monitor'].create_dataset(name='data', data=1, maxshape=None)
root['/entry/monitor/data'].attrs['type'] = 'NX_INT'
root['/entry/monitor/data'].attrs['EX_required'] = 'true'
root['/entry/monitor/data'].attrs['signal'] = '1'
 
root['/entry/monitor'].create_dataset(name='time_of_flight', data=1.0, maxshape=None)
root['/entry/monitor/time_of_flight'].attrs['type'] = 'NX_FLOAT'
root['/entry/monitor/time_of_flight'].attrs['EX_required'] = 'true'
root['/entry/monitor/time_of_flight'].attrs['axis'] = '1'
root['/entry/monitor/time_of_flight'].attrs['units'] = 'NX_TIME_OF_FLIGHT'

# Create the LINKS 
root['/entry/data/data'] = h5py.SoftLink('/entry/instrument/detector/data')
root['/entry/data/data/'].attrs['target'] = '/entry/instrument/detector/data'

# Create the LINKS 
root['/entry/data/detector_number'] = h5py.SoftLink('/entry/user/name')
root['/entry/data/detector_number/'].attrs['target'] = '/entry/instrument/detector/detector_number'

# Create the LINKS 
root['/entry/data/time_of_flight'] = h5py.SoftLink('/entry/instrument/detector/time_of_flight')
root['/entry/data/time_of_flight/'].attrs['target'] = '/entry/instrument/detector/time_of_flight'

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = ' Official NeXus NXDL schema to which this file conforms '
root['/entry/pre_sample_flightpath'].attrs['EX_doc'] = ' This is the flight path before the sample position. This can be determined by a chopper, by the moderator or the source itself. In other words: it the distance to the component which gives the T0 signal to the detector electronics. If another component in the NXinstrument hierarchy provides this information, this should be a link. '
root['/entry/instrument/detector/distance'].attrs['EX_doc'] = ' Distance to sample for the center of the detector '
root['/entry/instrument/detector/polar_angle'].attrs['EX_doc'] = ' polar angle for each detector element '
root['/entry/instrument/detector/azimuthal_angle'].attrs['EX_doc'] = ' azimuthal angle for each detector element '
root['/entry/sample/name'].attrs['EX_doc'] = ' Descriptive name of sample '
root['/entry/monitor/mode'].attrs['EX_doc'] = ' Count to a preset value based on either clock time (timer) or received monitor counts (monitor). '
root['/entry/monitor/preset'].attrs['EX_doc'] = ' preset value for time or monitor '
 

# Create the ATTRIBUTES 
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXtofsingle')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version

# Close the file
root.close()


