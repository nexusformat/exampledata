 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('h5py_NXtomoproc.h5', 'w')
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('untitled_instrument')
root['/entry/untitled_instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/untitled_instrument'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/'].create_group('untitled_source')
root['/entry/untitled_instrument/untitled_source'].attrs['NX_class'] = 'NXsource'
root['/entry/untitled_instrument/untitled_source'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('untitled_sample')
root['/entry/untitled_sample'].attrs['NX_class'] = 'NXsample'
root['/entry/untitled_sample'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('reconstruction')
root['/entry/reconstruction'].attrs['NX_class'] = 'NXprocess'
root['/entry/reconstruction'].attrs['EX_required'] = 'true'
 
root['/entry/reconstruction/'].create_group('parameters')
root['/entry/reconstruction/parameters'].attrs['NX_class'] = 'NXparameters'
root['/entry/reconstruction/parameters'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('data')
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='title', data=1.0, maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_FLOAT'
root['/entry/title'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXtomoproc
 
root['/entry'].create_dataset(name='definition', data='NXtomoproc', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_FLOAT'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/untitled_source'].create_dataset(name='type', data=1.0, maxshape=None)
root['/entry/untitled_instrument/untitled_source/type'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_instrument/untitled_source/type'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/untitled_source'].create_dataset(name='name', data=1.0, maxshape=None)
root['/entry/untitled_instrument/untitled_source/name'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_instrument/untitled_source/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/untitled_instrument/untitled_source']['probe'] are: 
#	 neutron
#	 x-ray
#	 electron
 
root['/entry/untitled_instrument/untitled_source'].create_dataset(name='probe', data='neutron', maxshape=None)
root['/entry/untitled_instrument/untitled_source/probe'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_instrument/untitled_source/probe'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_sample'].create_dataset(name='name', data=1.0, maxshape=None)
root['/entry/untitled_sample/name'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/reconstruction'].create_dataset(name='program', data='!some char data!', maxshape=None)
root['/entry/reconstruction/program'].attrs['type'] = 'NX_CHAR'
root['/entry/reconstruction/program'].attrs['EX_required'] = 'true'
 
root['/entry/reconstruction'].create_dataset(name='version', data='!some char data!', maxshape=None)
root['/entry/reconstruction/version'].attrs['type'] = 'NX_CHAR'
root['/entry/reconstruction/version'].attrs['EX_required'] = 'true'
 
root['/entry/reconstruction'].create_dataset(name='date', data='2021-03-22T16:42:16.495348', maxshape=None)
root['/entry/reconstruction/date'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/reconstruction/date'].attrs['EX_required'] = 'true'
 
root['/entry/reconstruction/parameters'].create_dataset(name='raw_file', data='!some char data!', maxshape=None)
root['/entry/reconstruction/parameters/raw_file'].attrs['type'] = 'NX_CHAR'
root['/entry/reconstruction/parameters/raw_file'].attrs['EX_required'] = 'true'
 
root['/entry/data'].create_dataset(name='data', data=[np.array([[1]])], maxshape=None)
root['/entry/data/data'].attrs['type'] = 'NX_INT'
root['/entry/data/data'].attrs['EX_required'] = 'true'
root['/entry/data/data'].attrs['signal'] = '1'
 
root['/entry/data'].create_dataset(name='x', data=[1.], maxshape=None, compression="gzip")
root['/entry/data/x'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/x'].attrs['EX_required'] = 'true'
root['/entry/data/x'].attrs['axis'] = '1'
root['/entry/data/x'].attrs['units'] = 'NX_ANY'
 
root['/entry/data'].create_dataset(name='y', data=[1.], maxshape=None, compression="gzip")
root['/entry/data/y'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/y'].attrs['EX_required'] = 'true'
root['/entry/data/y'].attrs['axis'] = '2'
root['/entry/data/y'].attrs['units'] = 'NX_ANY'
 
root['/entry/data'].create_dataset(name='z', data=[1.], maxshape=None, compression="gzip")
root['/entry/data/z'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/z'].attrs['EX_required'] = 'true'
root['/entry/data/z'].attrs['axis'] = '3'
root['/entry/data/z'].attrs['units'] = 'NX_ANY'
root['/entry/definition'].attrs['EX_doc'] = '     Official NeXus NXDL schema to which this file conforms    '
root['/entry/untitled_sample/name'].attrs['EX_doc'] = '      Descriptive name of sample     '
root['/entry/reconstruction/program'].attrs['EX_doc'] = '      Name of the program used for reconstruction     '
root['/entry/reconstruction/version'].attrs['EX_doc'] = '      Version of the program used     '
root['/entry/reconstruction/date'].attrs['EX_doc'] = '      Date and time of reconstruction processing.     '
root['/entry/reconstruction/parameters/raw_file'].attrs['EX_doc'] = '       Original raw data file this data was derived from      '
root['/entry/data/data'].attrs['EX_doc'] = '      This is the reconstructed volume. This can be different             things. Please indicate in the unit attribute what physical             quantity this really is.     '
root['/entry/data/x'].attrs['EX_doc'] = '      This is an array holding the values to use for the x-axis of             data. The units must be appropriate for the measurement.     '
root['/entry/data/y'].attrs['EX_doc'] = '      This is an array holding the values to use for the y-axis of             data. The units must be appropriate for the measurement.     '
root['/entry/data/z'].attrs['EX_doc'] = '      This is an array holding the values to use for the z-axis of             data. The units must be appropriate for the measurement.     '
root['/entry/data/data'].attrs['transform'] = '!some char data!'
root['/entry/data/data'].attrs['offset'] = '!some char data!'
root['/entry/data/data'].attrs['scaling'] = '!some char data!'
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXtomoproc')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.close()


