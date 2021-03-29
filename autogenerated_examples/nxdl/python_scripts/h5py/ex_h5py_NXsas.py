 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('h5py_NXsas.h5', 'w')
 
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
 
root['/entry/instrument/'].create_group('collimator')
root['/entry/instrument/collimator'].attrs['NX_class'] = 'NXcollimator'
root['/entry/instrument/collimator'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/collimator/'].create_group('geometry')
root['/entry/instrument/collimator/geometry'].attrs['NX_class'] = 'NXgeometry'
root['/entry/instrument/collimator/geometry'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/collimator/geometry/'].create_group('shape')
root['/entry/instrument/collimator/geometry/shape'].attrs['NX_class'] = 'NXshape'
root['/entry/instrument/collimator/geometry/shape'].attrs['EX_required'] = 'true'
 
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
 
root['/entry'].create_dataset(name='title', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='start_time', data='2021-03-26T13:07:54.100513', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='end_time', data='2021-03-26T13:07:54.103513', maxshape=None)
root['/entry/end_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/end_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXsas
 
root['/entry'].create_dataset(name='definition', data='NXsas', maxshape=None)
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
 
root['/entry/instrument/source'].create_dataset(name='probe', data='neutron', maxshape=None)
root['/entry/instrument/source/probe'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/probe'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/monochromator'].create_dataset(name='wavelength', data=1.0, maxshape=None)
root['/entry/instrument/monochromator/wavelength'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/monochromator/wavelength'].attrs['EX_required'] = 'true'
root['/entry/instrument/monochromator/wavelength'].attrs['units'] = 'NX_WAVELENGTH'
 
root['/entry/instrument/monochromator'].create_dataset(name='wavelength_spread', data=1.0, maxshape=None)
root['/entry/instrument/monochromator/wavelength_spread'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/monochromator/wavelength_spread'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/collimator/geometry/shape']['shape'] are: 
#	 nxcylinder
#	 nxbox
 
root['/entry/instrument/collimator/geometry/shape'].create_dataset(name='shape', data='nxcylinder', maxshape=None)
root['/entry/instrument/collimator/geometry/shape/shape'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/collimator/geometry/shape/shape'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/collimator/geometry/shape'].create_dataset(name='size', data=1.0, maxshape=None)
root['/entry/instrument/collimator/geometry/shape/size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/collimator/geometry/shape/size'].attrs['EX_required'] = 'true'
root['/entry/instrument/collimator/geometry/shape/size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='data', data=1.0, maxshape=None)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/entry/instrument/detector'].create_dataset(name='distance', data=1.0, maxshape=None)
root['/entry/instrument/detector/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/distance'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='x_pixel_size', data=1.0, maxshape=None)
root['/entry/instrument/detector/x_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/x_pixel_size'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/x_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='y_pixel_size', data=1.0, maxshape=None)
root['/entry/instrument/detector/y_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/y_pixel_size'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/y_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='polar_angle', data=1.0, maxshape=None)
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector'].create_dataset(name='azimuthal_angle', data=1.0, maxshape=None)
root['/entry/instrument/detector/azimuthal_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/azimuthal_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/azimuthal_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector'].create_dataset(name='rotation_angle', data=1.0, maxshape=None)
root['/entry/instrument/detector/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector'].create_dataset(name='aequatorial_angle', data=1.0, maxshape=None)
root['/entry/instrument/detector/aequatorial_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/aequatorial_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/aequatorial_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector'].create_dataset(name='beam_center_x', data=1.0, maxshape=None)
root['/entry/instrument/detector/beam_center_x'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/beam_center_x'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/beam_center_x'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='beam_center_y', data=1.0, maxshape=None)
root['/entry/instrument/detector/beam_center_y'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/beam_center_y'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/beam_center_y'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='aequatorial_angle', data=1.0, maxshape=None)
root['/entry/sample/aequatorial_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/aequatorial_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/aequatorial_angle'].attrs['units'] = 'NX_ANGLE'
 
# Valid enumeration values for root['/entry/control']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/control'].create_dataset(name='mode', data='monitor', maxshape=None)
root['/entry/control/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/control/mode'].attrs['EX_required'] = 'true'
 
root['/entry/control'].create_dataset(name='preset', data=1.0, maxshape=None)
root['/entry/control/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/preset'].attrs['EX_required'] = 'true'
 
root['/entry/control'].create_dataset(name='integral', data=1.0, maxshape=None)
root['/entry/control/integral'].attrs['type'] = 'NX_FLOAT'
root['/entry/control/integral'].attrs['EX_required'] = 'true'
root['/entry/control/integral'].attrs['units'] = 'NX_ANY'
 
 
root['/entry/data/data'] = h5py.SoftLink('/entry/instrument/detector/data')
root['/entry/data/data/'].attrs['target'] = '/entry/instrument/detector/data'
 
root['/entry'].attrs['entry'] = 'SAMPLE-CHAR-DATA'
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXsas')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.close()


