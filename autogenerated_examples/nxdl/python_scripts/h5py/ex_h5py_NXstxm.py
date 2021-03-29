 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('h5py_NXstxm.h5', 'w')
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('instrument')
root['/entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/instrument'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('source')
root['/entry/instrument/source'].attrs['NX_class'] = 'NXsource'
root['/entry/instrument/source'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('monochromator')
root['/entry/instrument/monochromator'].attrs['NX_class'] = 'NXmonochromator'
root['/entry/instrument/monochromator'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('detector')
root['/entry/instrument/detector'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('sample_x')
root['/entry/instrument/sample_x'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/sample_x'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/'].create_group('sample_y')
root['/entry/instrument/sample_y'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/sample_y'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/'].create_group('sample_z')
root['/entry/instrument/sample_z'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/sample_z'].attrs['EX_required'] = 'false'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('data')
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('control')
root['/entry/control'].attrs['NX_class'] = 'NXmonitor'
root['/entry/control'].attrs['EX_required'] = 'false'
 
root['/entry'].create_dataset(name='title', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='start_time', data='2021-03-26T13:07:55.630585', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='end_time', data='2021-03-26T13:07:55.632583', maxshape=None)
root['/entry/end_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/end_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXstxm
 
root['/entry'].create_dataset(name='definition', data='NXstxm', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source'].create_dataset(name='type', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/type'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/type'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/name'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source'].create_dataset(name='probe', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/probe'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/probe'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/monochromator'].create_dataset(name='energy', data=1.0, maxshape=None)
root['/entry/instrument/monochromator/energy'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/monochromator/energy'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector'].create_dataset(name='data', data=1.0, maxshape=None)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/sample_x'].create_dataset(name='data', data=1.0, maxshape=None)
root['/entry/instrument/sample_x/data'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/sample_x/data'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/sample_y'].create_dataset(name='data', data=1.0, maxshape=None)
root['/entry/instrument/sample_y/data'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/sample_y/data'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/sample_z'].create_dataset(name='data', data=1.0, maxshape=None)
root['/entry/instrument/sample_z/data'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/sample_z/data'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='rotation_angle', data=1.0, maxshape=None)
root['/entry/sample/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/rotation_angle'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/data']['stxm_scan_type'] are: 
#	 sample point spectrum
#	 sample line spectrum
#	 sample image
#	 sample image stack
#	 sample focus
#	 osa image
#	 osa focus
#	 detector image
#	 generic scan
 
root['/entry/data'].create_dataset(name='stxm_scan_type', data='sample point spectrum', maxshape=None)
root['/entry/data/stxm_scan_type'].attrs['type'] = 'NX_CHAR'
root['/entry/data/stxm_scan_type'].attrs['EX_required'] = 'true'
 
root['/entry/data'].create_dataset(name='data', data=1.0, maxshape=None)
root['/entry/data/data'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/data'].attrs['EX_required'] = 'true'
root['/entry/data/data'].attrs['signal'] = '1'
 
root['/entry/data'].create_dataset(name='energy', data=1.0, maxshape=None)
root['/entry/data/energy'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/energy'].attrs['EX_required'] = 'true'
 
root['/entry/data'].create_dataset(name='sample_y', data=1.0, maxshape=None)
root['/entry/data/sample_y'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/sample_y'].attrs['EX_required'] = 'true'
 
root['/entry/data'].create_dataset(name='sample_x', data=1.0, maxshape=None)
root['/entry/data/sample_x'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/sample_x'].attrs['EX_required'] = 'true'
 
root['/entry/control'].create_dataset(name='data', data=1.0, maxshape=None)
root['/entry/control/data'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/data'].attrs['EX_required'] = 'true'
 
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXstxm')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.close()


