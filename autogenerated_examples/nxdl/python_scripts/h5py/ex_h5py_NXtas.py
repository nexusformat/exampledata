 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('h5py_NXtas.h5', 'w')
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('untitled_instrument')
root['/entry/untitled_instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/untitled_instrument'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/'].create_group('untitled_source')
root['/entry/untitled_instrument/untitled_source'].attrs['NX_class'] = 'NXsource'
root['/entry/untitled_instrument/untitled_source'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/'].create_group('monochromator')
root['/entry/untitled_instrument/monochromator'].attrs['NX_class'] = 'NXcrystal'
root['/entry/untitled_instrument/monochromator'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/'].create_group('analyser')
root['/entry/untitled_instrument/analyser'].attrs['NX_class'] = 'NXcrystal'
root['/entry/untitled_instrument/analyser'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/'].create_group('untitled_detector')
root['/entry/untitled_instrument/untitled_detector'].attrs['NX_class'] = 'NXdetector'
root['/entry/untitled_instrument/untitled_detector'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('untitled_sample')
root['/entry/untitled_sample'].attrs['NX_class'] = 'NXsample'
root['/entry/untitled_sample'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('untitled_monitor')
root['/entry/untitled_monitor'].attrs['NX_class'] = 'NXmonitor'
root['/entry/untitled_monitor'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('untitled_data')
root['/entry/untitled_data'].attrs['NX_class'] = 'NXdata'
root['/entry/untitled_data'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='title', data='!some char data!', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['units'] = ''
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='start_time', data='2021-03-22T14:00:28.311989', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['units'] = ''
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXtas
 
root['/entry'].create_dataset(name='definition', data='NXtas', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['units'] = ''
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/untitled_source'].create_dataset(name='name', data='!some char data!', maxshape=None)
root['/entry/untitled_instrument/untitled_source/name'].attrs['type'] = 'NX_CHAR'
root['/entry/untitled_instrument/untitled_source/name'].attrs['units'] = ''
root['/entry/untitled_instrument/untitled_source/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/untitled_instrument/untitled_source']['probe'] are: 
#	 neutron
#	 x-ray
 
root['/entry/untitled_instrument/untitled_source'].create_dataset(name='probe', data='neutron', maxshape=None)
root['/entry/untitled_instrument/untitled_source/probe'].attrs['type'] = 'NX_CHAR'
root['/entry/untitled_instrument/untitled_source/probe'].attrs['units'] = ''
root['/entry/untitled_instrument/untitled_source/probe'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/monochromator'].create_dataset(name='ei', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_instrument/monochromator/ei'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_instrument/monochromator/ei'].attrs['units'] = ''
root['/entry/untitled_instrument/monochromator/ei'].attrs['EX_required'] = 'true'
root['/entry/untitled_instrument/monochromator/ei'].attrs['axis'] = '1'
 
root['/entry/untitled_instrument/monochromator'].create_dataset(name='rotation_angle', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_instrument/monochromator/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_instrument/monochromator/rotation_angle'].attrs['units'] = ''
root['/entry/untitled_instrument/monochromator/rotation_angle'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/analyser'].create_dataset(name='ef', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_instrument/analyser/ef'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_instrument/analyser/ef'].attrs['units'] = ''
root['/entry/untitled_instrument/analyser/ef'].attrs['EX_required'] = 'true'
root['/entry/untitled_instrument/analyser/ef'].attrs['axis'] = '1'
 
root['/entry/untitled_instrument/analyser'].create_dataset(name='rotation_angle', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_instrument/analyser/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_instrument/analyser/rotation_angle'].attrs['units'] = ''
root['/entry/untitled_instrument/analyser/rotation_angle'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/analyser'].create_dataset(name='polar_angle', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_instrument/analyser/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_instrument/analyser/polar_angle'].attrs['units'] = ''
root['/entry/untitled_instrument/analyser/polar_angle'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/untitled_detector'].create_dataset(name='data', data=[1], maxshape=None)
root['/entry/untitled_instrument/untitled_detector/data'].attrs['type'] = 'NX_INT'
root['/entry/untitled_instrument/untitled_detector/data'].attrs['units'] = ''
root['/entry/untitled_instrument/untitled_detector/data'].attrs['EX_required'] = 'true'
root['/entry/untitled_instrument/untitled_detector/data'].attrs['signal'] = '1'
 
root['/entry/untitled_instrument/untitled_detector'].create_dataset(name='polar_angle', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_instrument/untitled_detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_instrument/untitled_detector/polar_angle'].attrs['units'] = ''
root['/entry/untitled_instrument/untitled_detector/polar_angle'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_sample'].create_dataset(name='name', data='!some char data!', maxshape=None)
root['/entry/untitled_sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/untitled_sample/name'].attrs['units'] = ''
root['/entry/untitled_sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_sample'].create_dataset(name='qh', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_sample/qh'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_sample/qh'].attrs['units'] = ''
root['/entry/untitled_sample/qh'].attrs['EX_required'] = 'true'
root['/entry/untitled_sample/qh'].attrs['axis'] = '1'
 
root['/entry/untitled_sample'].create_dataset(name='qk', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_sample/qk'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_sample/qk'].attrs['units'] = ''
root['/entry/untitled_sample/qk'].attrs['EX_required'] = 'true'
root['/entry/untitled_sample/qk'].attrs['axis'] = '1'
 
root['/entry/untitled_sample'].create_dataset(name='ql', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_sample/ql'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_sample/ql'].attrs['units'] = ''
root['/entry/untitled_sample/ql'].attrs['EX_required'] = 'true'
root['/entry/untitled_sample/ql'].attrs['axis'] = '1'
 
root['/entry/untitled_sample'].create_dataset(name='en', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_sample/en'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_sample/en'].attrs['units'] = ''
root['/entry/untitled_sample/en'].attrs['EX_required'] = 'true'
root['/entry/untitled_sample/en'].attrs['axis'] = '1'
 
root['/entry/untitled_sample'].create_dataset(name='rotation_angle', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_sample/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_sample/rotation_angle'].attrs['units'] = ''
root['/entry/untitled_sample/rotation_angle'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_sample'].create_dataset(name='polar_angle', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_sample/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_sample/polar_angle'].attrs['units'] = ''
root['/entry/untitled_sample/polar_angle'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_sample'].create_dataset(name='sgu', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_sample/sgu'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_sample/sgu'].attrs['units'] = ''
root['/entry/untitled_sample/sgu'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_sample'].create_dataset(name='sgl', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_sample/sgl'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_sample/sgl'].attrs['units'] = ''
root['/entry/untitled_sample/sgl'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_sample'].create_dataset(name='unit_cell', data=[1. , 1. , 1. , 1. , 1. , 1.], maxshape=None, compression="gzip")
root['/entry/untitled_sample/unit_cell'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_sample/unit_cell'].attrs['units'] = ''
root['/entry/untitled_sample/unit_cell'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_sample'].create_dataset(name='orientation_matrix', data=[1. , 1. , 1. , 1. , 1. , 1. , 1. , 1. , 1.], maxshape=None, compression="gzip")
root['/entry/untitled_sample/orientation_matrix'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_sample/orientation_matrix'].attrs['units'] = ''
root['/entry/untitled_sample/orientation_matrix'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/untitled_monitor']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/untitled_monitor'].create_dataset(name='mode', data='monitor', maxshape=None)
root['/entry/untitled_monitor/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/untitled_monitor/mode'].attrs['units'] = ''
root['/entry/untitled_monitor/mode'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_monitor'].create_dataset(name='preset', data=1.0, maxshape=None)
root['/entry/untitled_monitor/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_monitor/preset'].attrs['units'] = ''
root['/entry/untitled_monitor/preset'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_monitor'].create_dataset(name='data', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_monitor/data'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_monitor/data'].attrs['units'] = ''
root['/entry/untitled_monitor/data'].attrs['EX_required'] = 'true'
root['/entry/definition'].attrs['EX_doc'] = '     Official NeXus NXDL schema to which this file conforms    '
root['/entry/untitled_sample/name'].attrs['EX_doc'] = '      Descriptive name of sample     '
root['/entry/untitled_monitor/mode'].attrs['EX_doc'] = '      Count to a preset value based on either clock time (timer)             or received monitor counts (monitor).     '
root['/entry/untitled_monitor/preset'].attrs['EX_doc'] = '      preset value for time or monitor     '
root['/entry/untitled_monitor/data'].attrs['EX_doc'] = '      Total integral monitor counts     '
root['/entry/untitled_data'].attrs['EX_doc'] = '     One of the ei,ef,qh,qk,ql,en should get a primary=1 attribute to denote the main scan axis    '
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'untitled_data'
root.attrs['file_name'] = os.path.abspath('NXtas')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.close()


