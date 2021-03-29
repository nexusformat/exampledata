 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('h5py_NXiqproc.h5', 'w')
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('instrument')
root['/entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/instrument'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('source')
root['/entry/instrument/source'].attrs['NX_class'] = 'NXsource'
root['/entry/instrument/source'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('reduction')
root['/entry/reduction'].attrs['NX_class'] = 'NXprocess'
root['/entry/reduction'].attrs['EX_required'] = 'true'
 
root['/entry/reduction/'].create_group('input')
root['/entry/reduction/input'].attrs['NX_class'] = 'NXparameters'
root['/entry/reduction/input'].attrs['EX_required'] = 'true'
 
root['/entry/reduction/'].create_group('output')
root['/entry/reduction/output'].attrs['NX_class'] = 'NXparameters'
root['/entry/reduction/output'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('data')
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='title', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXiqproc
 
root['/entry'].create_dataset(name='definition', data='NXiqproc', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source'].create_dataset(name='type', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/type'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/type'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/source']['probe'] are: 
#	 neutron
#	 x-ray
#	 electron
 
root['/entry/instrument/source'].create_dataset(name='probe', data='neutron', maxshape=None)
root['/entry/instrument/source/probe'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/probe'].attrs['EX_required'] = 'true'
 
root['/entry/instrument'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/reduction'].create_dataset(name='program', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/reduction/program'].attrs['type'] = 'NX_CHAR'
root['/entry/reduction/program'].attrs['EX_required'] = 'true'
 
root['/entry/reduction'].create_dataset(name='version', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/reduction/version'].attrs['type'] = 'NX_CHAR'
root['/entry/reduction/version'].attrs['EX_required'] = 'true'
 
root['/entry/reduction/input'].create_dataset(name='filenames', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/reduction/input/filenames'].attrs['type'] = 'NX_CHAR'
root['/entry/reduction/input/filenames'].attrs['EX_required'] = 'true'
 
root['/entry/data'].create_dataset(name='data', data=1, maxshape=None)
root['/entry/data/data'].attrs['type'] = 'NX_INT'
root['/entry/data/data'].attrs['EX_required'] = 'true'
root['/entry/data/data'].attrs['signal'] = '1'
 
root['/entry/data'].create_dataset(name='variable', data=1.0, maxshape=None)
root['/entry/data/variable'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/variable'].attrs['EX_required'] = 'true'
root['/entry/data/variable'].attrs['axis'] = '1'
 
root['/entry/data'].create_dataset(name='qx', data=1.0, maxshape=None)
root['/entry/data/qx'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/qx'].attrs['EX_required'] = 'true'
root['/entry/data/qx'].attrs['axis'] = '2'
 
root['/entry/data'].create_dataset(name='qy', data=1.0, maxshape=None)
root['/entry/data/qy'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/qy'].attrs['EX_required'] = 'true'
root['/entry/data/qy'].attrs['axis'] = '3'
 
root['/entry'].attrs['entry'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/variable'].attrs['varied_variable'] = 'SAMPLE-CHAR-DATA'
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXiqproc')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.close()


