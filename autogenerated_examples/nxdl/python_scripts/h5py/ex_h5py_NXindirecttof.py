 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('h5py_NXindirecttof.h5', 'w')
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('untitled_instrument')
root['/entry/untitled_instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/untitled_instrument'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/'].create_group('analyser')
root['/entry/untitled_instrument/analyser'].attrs['NX_class'] = 'NXmonochromator'
root['/entry/untitled_instrument/analyser'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='title', data='!some char data!', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['units'] = ''
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='start_time', data='2021-03-22T14:00:27.101402', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['units'] = ''
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXindirecttof
 
root['/entry'].create_dataset(name='definition', data='NXindirecttof', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['units'] = ''
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/analyser'].create_dataset(name='energy', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_instrument/analyser/energy'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_instrument/analyser/energy'].attrs['units'] = ''
root['/entry/untitled_instrument/analyser/energy'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/analyser'].create_dataset(name='polar_angle', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_instrument/analyser/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_instrument/analyser/polar_angle'].attrs['units'] = ''
root['/entry/untitled_instrument/analyser/polar_angle'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/analyser'].create_dataset(name='distance', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_instrument/analyser/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_instrument/analyser/distance'].attrs['units'] = ''
root['/entry/untitled_instrument/analyser/distance'].attrs['EX_required'] = 'true'
root['/entry/definition'].attrs['EX_doc'] = '     Official NeXus NXDL schema to which this file conforms    '
root['/entry/untitled_instrument/analyser/energy'].attrs['EX_doc'] = '       analyzed energy      '
root['/entry/untitled_instrument/analyser/polar_angle'].attrs['EX_doc'] = '       polar angle towards sample      '
root['/entry/untitled_instrument/analyser/distance'].attrs['EX_doc'] = '       distance from sample      '
root['/'].attrs['default'] = 'entry'
root.attrs['file_name'] = os.path.abspath('NXindirecttof')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.close()


