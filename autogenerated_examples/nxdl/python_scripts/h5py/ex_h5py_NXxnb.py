 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('h5py_NXxnb.h5', 'w')
 
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
#	 NXxnb
 
root['/entry'].create_dataset(name='definition', data='NXxnb', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['units'] = ''
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector'].create_dataset(name='polar_angle', data=[1.], maxshape=None, compression="gzip")
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['units'] = ''
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/polar_angle'].attrs['axis'] = '1'
 
root['/entry/instrument/detector'].create_dataset(name='tilt_angle', data=[1.], maxshape=None, compression="gzip")
root['/entry/instrument/detector/tilt_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/tilt_angle'].attrs['units'] = ''
root['/entry/instrument/detector/tilt_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/tilt_angle'].attrs['axis'] = '1'
 
root['/entry/sample'].create_dataset(name='rotation_angle', data=[1.], maxshape=None, compression="gzip")
root['/entry/sample/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/rotation_angle'].attrs['units'] = ''
root['/entry/sample/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/rotation_angle'].attrs['axis'] = '1'
root['/entry/sample/rotation_angle'].attrs['primary'] = '1'
root['/entry/definition'].attrs['EX_doc'] = '     Official NeXus NXDL schema to which this file conforms    '
root['/entry/instrument/detector/polar_angle'].attrs['EX_doc'] = '       The polar_angle (gamma) of the detector for each scan point.      '
root['/entry/instrument/detector/tilt_angle'].attrs['EX_doc'] = '       The angle by which the detector has been tilted out of the             scattering plane.      '
root['/entry/sample/rotation_angle'].attrs['EX_doc'] = '      This is an array holding the sample rotation angle at each           scan point     '
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'name'
root.attrs['file_name'] = os.path.abspath('NXxnb')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.close()


