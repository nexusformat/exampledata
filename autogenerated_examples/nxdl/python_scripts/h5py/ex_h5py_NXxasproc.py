 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('h5py_NXxasproc.h5', 'w')
 
root.create_group('untitled_entry')
root['/untitled_entry'].attrs['NX_class'] = 'NXentry'
root['/untitled_entry'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/'].create_group('untitled_sample')
root['/untitled_entry/untitled_sample'].attrs['NX_class'] = 'NXsample'
root['/untitled_entry/untitled_sample'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/'].create_group('XAS_data_reduction')
root['/untitled_entry/XAS_data_reduction'].attrs['NX_class'] = 'NXprocess'
root['/untitled_entry/XAS_data_reduction'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/XAS_data_reduction/'].create_group('parameters')
root['/untitled_entry/XAS_data_reduction/parameters'].attrs['NX_class'] = 'NXparameters'
root['/untitled_entry/XAS_data_reduction/parameters'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/'].create_group('untitled_data')
root['/untitled_entry/untitled_data'].attrs['NX_class'] = 'NXdata'
root['/untitled_entry/untitled_data'].attrs['EX_required'] = 'true'
 
root['/untitled_entry'].create_dataset(name='title', data=1, maxshape=None)
root['/untitled_entry/title'].attrs['type'] = 'NX_INT'
root['/untitled_entry/title'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/untitled_entry']['definition'] are: 
#	 NXxasproc
 
root['/untitled_entry'].create_dataset(name='definition', data='NXxasproc', maxshape=None)
root['/untitled_entry/definition'].attrs['type'] = 'NX_INT'
root['/untitled_entry/definition'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/untitled_sample'].create_dataset(name='name', data=1, maxshape=None)
root['/untitled_entry/untitled_sample/name'].attrs['type'] = 'NX_INT'
root['/untitled_entry/untitled_sample/name'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/XAS_data_reduction'].create_dataset(name='program', data='!some char data!', maxshape=None)
root['/untitled_entry/XAS_data_reduction/program'].attrs['type'] = 'NX_CHAR'
root['/untitled_entry/XAS_data_reduction/program'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/XAS_data_reduction'].create_dataset(name='version', data='!some char data!', maxshape=None)
root['/untitled_entry/XAS_data_reduction/version'].attrs['type'] = 'NX_CHAR'
root['/untitled_entry/XAS_data_reduction/version'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/XAS_data_reduction'].create_dataset(name='date', data='2021-03-22T16:42:16.557707', maxshape=None)
root['/untitled_entry/XAS_data_reduction/date'].attrs['type'] = 'NX_DATE_TIME'
root['/untitled_entry/XAS_data_reduction/date'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/XAS_data_reduction/parameters'].create_dataset(name='raw_file', data='!some char data!', maxshape=None)
root['/untitled_entry/XAS_data_reduction/parameters/raw_file'].attrs['type'] = 'NX_CHAR'
root['/untitled_entry/XAS_data_reduction/parameters/raw_file'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/untitled_data']['energy'] = b"['!']"
root['/untitled_entry/untitled_data/energy'].attrs['type'] = 'NX_CHAR'
root['/untitled_entry/untitled_data/energy'].attrs['EX_required'] = 'true'
root['/untitled_entry/untitled_data/energy'].attrs['axis'] = '1'
 
root['/untitled_entry/untitled_data'].create_dataset(name='data', data=[1.], maxshape=None, compression="gzip")
root['/untitled_entry/untitled_data/data'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/untitled_data/data'].attrs['EX_required'] = 'true'
root['/untitled_entry/definition'].attrs['EX_doc'] = '     Official NeXus NXDL schema to which this file conforms    '
root['/untitled_entry/untitled_sample/name'].attrs['EX_doc'] = '      Descriptive name of sample     '
root['/untitled_entry/XAS_data_reduction/program'].attrs['EX_doc'] = '      Name of the program used for reconstruction     '
root['/untitled_entry/XAS_data_reduction/version'].attrs['EX_doc'] = '      Version of the program used     '
root['/untitled_entry/XAS_data_reduction/date'].attrs['EX_doc'] = '      Date and time of reconstruction processing.     '
root['/untitled_entry/XAS_data_reduction/parameters/raw_file'].attrs['EX_doc'] = '       Original raw data file this data was derived from      '
root['/untitled_entry/untitled_data/data'].attrs['EX_doc'] = '      This is corrected and calibrated I(incoming)/I(absorbed). So it is the absorption.                     Expect attribute  ``signal=1``     '
root['/untitled_entry'].attrs['entry'] = '!some char data!'
root['/'].attrs['default'] = 'untitled_entry'
root['/untitled_entry'].attrs['default'] = 'untitled_data'
root['/untitled_entry/untitled_data'].attrs['signal'] = 'data'
root['/untitled_entry/untitled_data/data'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXxasproc')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.close()

