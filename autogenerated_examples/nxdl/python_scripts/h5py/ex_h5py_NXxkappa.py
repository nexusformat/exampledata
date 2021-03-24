 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('h5py_NXxkappa.h5', 'w')
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('instrument')
root['/entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/instrument'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('detector')
root['/entry/instrument/detector'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('name')
root['/entry/name'].attrs['NX_class'] = 'NXdata'
root['/entry/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXxkappa
 
root['/entry'].create_dataset(name='definition', data='NXxkappa', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_FLOAT'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector'].create_dataset(name='polar_angle', data=[1.], maxshape=None, compression="gzip")
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='rotation_angle', data=[1.], maxshape=None, compression="gzip")
root['/entry/sample/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/rotation_angle'].attrs['axis'] = '1'
root['/entry/sample/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='kappa', data=[1.], maxshape=None, compression="gzip")
root['/entry/sample/kappa'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/kappa'].attrs['EX_required'] = 'true'
root['/entry/sample/kappa'].attrs['axis'] = '1'
root['/entry/sample/kappa'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='phi', data=[1.], maxshape=None, compression="gzip")
root['/entry/sample/phi'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/phi'].attrs['EX_required'] = 'true'
root['/entry/sample/phi'].attrs['axis'] = '1'
root['/entry/sample/phi'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='alpha', data=1.0, maxshape=None)
root['/entry/sample/alpha'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/alpha'].attrs['EX_required'] = 'true'
root['/entry/sample/alpha'].attrs['units'] = 'NX_ANGLE'
root['/entry/definition'].attrs['EX_doc'] = '     Official NeXus NXDL schema to which this file conforms    '
root['/entry/instrument/detector/polar_angle'].attrs['EX_doc'] = '       The polar_angle (two theta) at each scan point      '
root['/entry/sample/rotation_angle'].attrs['EX_doc'] = '      This is an array holding the sample rotation angle at each           scan point     '
root['/entry/sample/kappa'].attrs['EX_doc'] = '      This is an array holding the kappa angle at each scan point     '
root['/entry/sample/phi'].attrs['EX_doc'] = '      This is an array holding the phi angle at each scan point     '
root['/entry/sample/alpha'].attrs['EX_doc'] = '      This holds the inclination angle of the kappa arm.     '
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'name'
root.attrs['file_name'] = os.path.abspath('NXxkappa')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.close()

