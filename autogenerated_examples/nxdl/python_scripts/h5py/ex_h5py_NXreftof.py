 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('h5py_NXreftof.h5', 'w')
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('instrument')
root['/entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/instrument'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('chopper')
root['/entry/instrument/chopper'].attrs['NX_class'] = 'NXdisk_chopper'
root['/entry/instrument/chopper'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('detector')
root['/entry/instrument/detector'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('control')
root['/entry/control'].attrs['NX_class'] = 'NXmonitor'
root['/entry/control'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('data')
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='title', data='!some char data!', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['units'] = ''
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='start_time', data='2021-03-22T14:00:27.721731', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['units'] = ''
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='end_time', data='2021-03-22T14:00:27.723730', maxshape=None)
root['/entry/end_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/end_time'].attrs['units'] = ''
root['/entry/end_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXreftof
 
root['/entry'].create_dataset(name='definition', data='NXreftof', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['units'] = ''
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument'].create_dataset(name='name', data='!some char data!', maxshape=None)
root['/entry/instrument/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/name'].attrs['units'] = ''
root['/entry/instrument/name'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/chopper'].create_dataset(name='distance', data=1.0, maxshape=None)
root['/entry/instrument/chopper/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/chopper/distance'].attrs['units'] = ''
root['/entry/instrument/chopper/distance'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector'].create_dataset(name='data', data=[np.array([[1]])], maxshape=None)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/data'].attrs['units'] = ''
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/entry/instrument/detector'].create_dataset(name='time_of_flight', data=[1.], maxshape=None, compression="gzip")
root['/entry/instrument/detector/time_of_flight'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/time_of_flight'].attrs['units'] = ''
root['/entry/instrument/detector/time_of_flight'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/time_of_flight'].attrs['axis'] = '3'
 
root['/entry/instrument/detector'].create_dataset(name='distance', data=1.0, maxshape=None)
root['/entry/instrument/detector/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/distance'].attrs['units'] = ''
root['/entry/instrument/detector/distance'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector'].create_dataset(name='polar_angle', data=1.0, maxshape=None)
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['units'] = ''
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector'].create_dataset(name='x_pixel_size', data=1.0, maxshape=None)
root['/entry/instrument/detector/x_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/x_pixel_size'].attrs['units'] = ''
root['/entry/instrument/detector/x_pixel_size'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector'].create_dataset(name='y_pixel_size', data=1.0, maxshape=None)
root['/entry/instrument/detector/y_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/y_pixel_size'].attrs['units'] = ''
root['/entry/instrument/detector/y_pixel_size'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='name', data='!some char data!', maxshape=None)
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['units'] = ''
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='rotation_angle', data=1.0, maxshape=None)
root['/entry/sample/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/rotation_angle'].attrs['units'] = ''
root['/entry/sample/rotation_angle'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/control']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/control'].create_dataset(name='mode', data='monitor', maxshape=None)
root['/entry/control/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/control/mode'].attrs['units'] = ''
root['/entry/control/mode'].attrs['EX_required'] = 'true'
 
root['/entry/control'].create_dataset(name='preset', data=1.0, maxshape=None)
root['/entry/control/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/preset'].attrs['units'] = ''
root['/entry/control/preset'].attrs['EX_required'] = 'true'
 
root['/entry/control'].create_dataset(name='integral', data=1, maxshape=None)
root['/entry/control/integral'].attrs['type'] = 'NX_INT'
root['/entry/control/integral'].attrs['units'] = ''
root['/entry/control/integral'].attrs['EX_required'] = 'true'
 
root['/entry/control'].create_dataset(name='time_of_flight', data=1.0, maxshape=None)
root['/entry/control/time_of_flight'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/time_of_flight'].attrs['units'] = ''
root['/entry/control/time_of_flight'].attrs['EX_required'] = 'true'
root['/entry/control/time_of_flight'].attrs['axis'] = '1'
 
root['/entry/control'].create_dataset(name='data', data=1, maxshape=None)
root['/entry/control/data'].attrs['type'] = 'NX_INT'
root['/entry/control/data'].attrs['units'] = ''
root['/entry/control/data'].attrs['EX_required'] = 'true'
root['/entry/control/data'].attrs['signal'] = '1'
root['/entry/definition'].attrs['EX_doc'] = '     Official NeXus NXDL schema to which this file conforms    '
root['/entry/instrument/chopper/distance'].attrs['EX_doc'] = '       Distance between chopper and sample      '
root['/entry/instrument/detector/time_of_flight'].attrs['EX_doc'] = '       Array of time values for each bin in a time-of-flight               measurement      '
root['/entry/sample/name'].attrs['EX_doc'] = '      Descriptive name of sample     '
root['/entry/control/mode'].attrs['EX_doc'] = '      Count to a preset value based on either clock time (timer)             or received monitor counts (monitor).     '
root['/entry/control/preset'].attrs['EX_doc'] = '      preset value for time or monitor     '
root['/entry/control/integral'].attrs['EX_doc'] = '      Total integral monitor counts     '
root['/entry/control/time_of_flight'].attrs['EX_doc'] = '      Time channels     '
root['/entry/control/data'].attrs['EX_doc'] = '      Monitor counts in each time channel     '
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root.attrs['file_name'] = os.path.abspath('NXreftof')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.close()


