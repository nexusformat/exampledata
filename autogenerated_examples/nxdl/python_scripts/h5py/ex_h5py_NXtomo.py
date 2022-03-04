 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('NXtomo.h5', 'w')

# Create the GROUPS 
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('instrument')
root['/entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/instrument'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('source')
root['/entry/instrument/source'].attrs['NX_class'] = 'NXsource'
root['/entry/instrument/source'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/'].create_group('detector')
root['/entry/instrument/detector'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('control')
root['/entry/control'].attrs['NX_class'] = 'NXmonitor'
root['/entry/control'].attrs['EX_required'] = 'false'
 
root['/entry/'].create_group('data')
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
root['/entry'].create_dataset(name='title', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'false'
 
root['/entry'].create_dataset(name='start_time', data='2022-03-04T14:56:37.625713', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'false'
 
root['/entry'].create_dataset(name='end_time', data='2022-03-04T14:56:37.625713', maxshape=None)
root['/entry/end_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/end_time'].attrs['EX_required'] = 'false'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXtomo
 
root['/entry'].create_dataset(name='definition', data='NXtomo', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source'].create_dataset(name='type', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/type'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/type'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/source'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/name'].attrs['EX_required'] = 'false'
 
# Valid enumeration values for root['/entry/instrument/source']['probe'] are: 
#	 neutron
#	 x-ray
#	 electron
 
root['/entry/instrument/source'].create_dataset(name='probe', data='neutron', maxshape=None)
root['/entry/instrument/source/probe'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/probe'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector'].create_dataset(name='data', data=1, maxshape=None)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/entry/instrument/detector'].create_dataset(name='image_key', data=1, maxshape=None)
root['/entry/instrument/detector/image_key'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/image_key'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector'].create_dataset(name='x_pixel_size', data=1.0, maxshape=None)
root['/entry/instrument/detector/x_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/x_pixel_size'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/x_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='y_pixel_size', data=1.0, maxshape=None)
root['/entry/instrument/detector/y_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/y_pixel_size'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/y_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='distance', data=1.0, maxshape=None)
root['/entry/instrument/detector/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/distance'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='x_rotation_axis_pixel_position', data=1.0, maxshape=None)
root['/entry/instrument/detector/x_rotation_axis_pixel_position'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/x_rotation_axis_pixel_position'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector'].create_dataset(name='y_rotation_axis_pixel_position', data=1.0, maxshape=None)
root['/entry/instrument/detector/y_rotation_axis_pixel_position'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/y_rotation_axis_pixel_position'].attrs['EX_required'] = 'false'
 
root['/entry/sample'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='rotation_angle', data=1.0, maxshape=None)
root['/entry/sample/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/rotation_angle'].attrs['axis'] = '1'
root['/entry/sample/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='x_translation', data=1.0, maxshape=None)
root['/entry/sample/x_translation'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/x_translation'].attrs['EX_required'] = 'false'
root['/entry/sample/x_translation'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/sample'].create_dataset(name='y_translation', data=1.0, maxshape=None)
root['/entry/sample/y_translation'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/y_translation'].attrs['EX_required'] = 'false'
root['/entry/sample/y_translation'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/sample'].create_dataset(name='z_translation', data=1.0, maxshape=None)
root['/entry/sample/z_translation'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/z_translation'].attrs['EX_required'] = 'false'
root['/entry/sample/z_translation'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/control'].create_dataset(name='data', data=1.0, maxshape=None)
root['/entry/control/data'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/data'].attrs['EX_required'] = 'true'
root['/entry/control/data'].attrs['units'] = 'NX_ANY'

# Create the LINKS 
root['/entry/data/data'] = h5py.SoftLink('/entry/instrument/detector/data')
root['/entry/data/data/'].attrs['target'] = '/entry/instrument/detector/data'

# Create the LINKS 
root['/entry/data/rotation_angle'] = h5py.SoftLink('/entry/sample/rotation_angle')
root['/entry/data/rotation_angle/'].attrs['target'] = '/entry/sample/rotation_angle'

# Create the LINKS 
root['/entry/data/image_key'] = h5py.SoftLink('/entry/instrument/detector/image_key')
root['/entry/data/image_key/'].attrs['target'] = '/entry/instrument/detector/image_key'

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms '
root['/entry/instrument/detector/image_key'].attrs['EX_doc'] = 'In order    to distinguish between sample projections, dark and flat    images, a magic number is recorded per frame.    The key is as follows:    * projection = 0    * flat field = 1    * dark field = 2    * invalid = 3 '
root['/entry/instrument/detector/distance'].attrs['EX_doc'] = 'Distance between detector and sample '
root['/entry/sample/name'].attrs['EX_doc'] = 'Descriptive name of sample '
root['/entry/sample/rotation_angle'].attrs['EX_doc'] = 'In practice this axis is always aligned along one pixel direction on the detector and usually vertical.    There are experiments with horizontal rotation axes, so this would need to be indicated somehow.    For now the best way for that is an open question. '
root['/entry/control/data'].attrs['EX_doc'] = 'Total integral monitor counts for each measured frame. Allows a to correction for fluctuations in the beam between frames. '
 

# Create the ATTRIBUTES 
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXtomo')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version

# Close the file
root.close()


