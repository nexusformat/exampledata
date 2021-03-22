 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('h5py_NXsas.h5', 'w')
 
root.create_group('untitled_entry')
root['/untitled_entry'].attrs['NX_class'] = 'NXentry'
root['/untitled_entry'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/'].create_group('instrument')
root['/untitled_entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/untitled_entry/instrument'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/instrument/'].create_group('source')
root['/untitled_entry/instrument/source'].attrs['NX_class'] = 'NXsource'
root['/untitled_entry/instrument/source'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/instrument/'].create_group('monochromator')
root['/untitled_entry/instrument/monochromator'].attrs['NX_class'] = 'NXmonochromator'
root['/untitled_entry/instrument/monochromator'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/instrument/'].create_group('collimator')
root['/untitled_entry/instrument/collimator'].attrs['NX_class'] = 'NXcollimator'
root['/untitled_entry/instrument/collimator'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/instrument/collimator/'].create_group('geometry')
root['/untitled_entry/instrument/collimator/geometry'].attrs['NX_class'] = 'NXgeometry'
root['/untitled_entry/instrument/collimator/geometry'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/instrument/collimator/geometry/'].create_group('shape')
root['/untitled_entry/instrument/collimator/geometry/shape'].attrs['NX_class'] = 'NXshape'
root['/untitled_entry/instrument/collimator/geometry/shape'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/instrument/'].create_group('detector')
root['/untitled_entry/instrument/detector'].attrs['NX_class'] = 'NXdetector'
root['/untitled_entry/instrument/detector'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/'].create_group('sample')
root['/untitled_entry/sample'].attrs['NX_class'] = 'NXsample'
root['/untitled_entry/sample'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/'].create_group('control')
root['/untitled_entry/control'].attrs['NX_class'] = 'NXmonitor'
root['/untitled_entry/control'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/'].create_group('data')
root['/untitled_entry/data'].attrs['NX_class'] = 'NXdata'
root['/untitled_entry/data'].attrs['EX_required'] = 'true'
 
root['/untitled_entry'].create_dataset(name='title', data=1, maxshape=None)
root['/untitled_entry/title'].attrs['type'] = 'NX_INT'
root['/untitled_entry/title'].attrs['EX_required'] = 'true'
 
root['/untitled_entry'].create_dataset(name='start_time', data='2021-03-22T16:42:15.944675', maxshape=None)
root['/untitled_entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/untitled_entry/start_time'].attrs['EX_required'] = 'true'
 
root['/untitled_entry'].create_dataset(name='end_time', data='2021-03-22T16:42:15.946665', maxshape=None)
root['/untitled_entry/end_time'].attrs['type'] = 'NX_DATE_TIME'
root['/untitled_entry/end_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/untitled_entry']['definition'] are: 
#	 NXsas
 
root['/untitled_entry'].create_dataset(name='definition', data='NXsas', maxshape=None)
root['/untitled_entry/definition'].attrs['type'] = 'NX_DATE_TIME'
root['/untitled_entry/definition'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/instrument/source'].create_dataset(name='type', data='2021-03-22T16:42:15.948687', maxshape=None)
root['/untitled_entry/instrument/source/type'].attrs['type'] = 'NX_DATE_TIME'
root['/untitled_entry/instrument/source/type'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/instrument/source'].create_dataset(name='name', data='2021-03-22T16:42:15.949687', maxshape=None)
root['/untitled_entry/instrument/source/name'].attrs['type'] = 'NX_DATE_TIME'
root['/untitled_entry/instrument/source/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/untitled_entry/instrument/source']['probe'] are: 
#	 neutron
#	 x-ray
 
root['/untitled_entry/instrument/source'].create_dataset(name='probe', data='neutron', maxshape=None)
root['/untitled_entry/instrument/source/probe'].attrs['type'] = 'NX_DATE_TIME'
root['/untitled_entry/instrument/source/probe'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/instrument/monochromator'].create_dataset(name='wavelength', data=1.0, maxshape=None)
root['/untitled_entry/instrument/monochromator/wavelength'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/instrument/monochromator/wavelength'].attrs['EX_required'] = 'true'
root['/untitled_entry/instrument/monochromator/wavelength'].attrs['units'] = 'NX_WAVELENGTH'
 
root['/untitled_entry/instrument/monochromator'].create_dataset(name='wavelength_spread', data=1.0, maxshape=None)
root['/untitled_entry/instrument/monochromator/wavelength_spread'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/instrument/monochromator/wavelength_spread'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/untitled_entry/instrument/collimator/geometry/shape']['shape'] are: 
#	 nxcylinder
#	 nxbox
 
root['/untitled_entry/instrument/collimator/geometry/shape'].create_dataset(name='shape', data='nxcylinder', maxshape=None)
root['/untitled_entry/instrument/collimator/geometry/shape/shape'].attrs['type'] = 'NX_CHAR'
root['/untitled_entry/instrument/collimator/geometry/shape/shape'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/instrument/collimator/geometry/shape'].create_dataset(name='size', data=1.0, maxshape=None)
root['/untitled_entry/instrument/collimator/geometry/shape/size'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/instrument/collimator/geometry/shape/size'].attrs['EX_required'] = 'true'
root['/untitled_entry/instrument/collimator/geometry/shape/size'].attrs['units'] = 'NX_LENGTH'
 
root['/untitled_entry/instrument/detector'].create_dataset(name='data', data=[[1]], maxshape=None, compression="gzip")
root['/untitled_entry/instrument/detector/data'].attrs['type'] = 'NX_NUMBER'
root['/untitled_entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/untitled_entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/untitled_entry/instrument/detector'].create_dataset(name='distance', data=1.0, maxshape=None)
root['/untitled_entry/instrument/detector/distance'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/instrument/detector/distance'].attrs['EX_required'] = 'true'
root['/untitled_entry/instrument/detector/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/untitled_entry/instrument/detector'].create_dataset(name='x_pixel_size', data=1.0, maxshape=None)
root['/untitled_entry/instrument/detector/x_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/instrument/detector/x_pixel_size'].attrs['EX_required'] = 'true'
root['/untitled_entry/instrument/detector/x_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/untitled_entry/instrument/detector'].create_dataset(name='y_pixel_size', data=1.0, maxshape=None)
root['/untitled_entry/instrument/detector/y_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/instrument/detector/y_pixel_size'].attrs['EX_required'] = 'true'
root['/untitled_entry/instrument/detector/y_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/untitled_entry/instrument/detector'].create_dataset(name='polar_angle', data=1.0, maxshape=None)
root['/untitled_entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/untitled_entry/instrument/detector/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/untitled_entry/instrument/detector'].create_dataset(name='azimuthal_angle', data=1.0, maxshape=None)
root['/untitled_entry/instrument/detector/azimuthal_angle'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/instrument/detector/azimuthal_angle'].attrs['EX_required'] = 'true'
root['/untitled_entry/instrument/detector/azimuthal_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/untitled_entry/instrument/detector'].create_dataset(name='rotation_angle', data=1.0, maxshape=None)
root['/untitled_entry/instrument/detector/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/instrument/detector/rotation_angle'].attrs['EX_required'] = 'true'
root['/untitled_entry/instrument/detector/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/untitled_entry/instrument/detector'].create_dataset(name='aequatorial_angle', data=1.0, maxshape=None)
root['/untitled_entry/instrument/detector/aequatorial_angle'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/instrument/detector/aequatorial_angle'].attrs['EX_required'] = 'true'
root['/untitled_entry/instrument/detector/aequatorial_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/untitled_entry/instrument/detector'].create_dataset(name='beam_center_x', data=1.0, maxshape=None)
root['/untitled_entry/instrument/detector/beam_center_x'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/instrument/detector/beam_center_x'].attrs['EX_required'] = 'true'
root['/untitled_entry/instrument/detector/beam_center_x'].attrs['units'] = 'NX_LENGTH'
 
root['/untitled_entry/instrument/detector'].create_dataset(name='beam_center_y', data=1.0, maxshape=None)
root['/untitled_entry/instrument/detector/beam_center_y'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/instrument/detector/beam_center_y'].attrs['EX_required'] = 'true'
root['/untitled_entry/instrument/detector/beam_center_y'].attrs['units'] = 'NX_LENGTH'
 
root['/untitled_entry/instrument'].create_dataset(name='name', data='!some char data!', maxshape=None)
root['/untitled_entry/instrument/name'].attrs['type'] = 'NX_CHAR'
root['/untitled_entry/instrument/name'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/sample'].create_dataset(name='name', data='!some char data!', maxshape=None)
root['/untitled_entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/untitled_entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/sample'].create_dataset(name='aequatorial_angle', data=1.0, maxshape=None)
root['/untitled_entry/sample/aequatorial_angle'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/sample/aequatorial_angle'].attrs['EX_required'] = 'true'
root['/untitled_entry/sample/aequatorial_angle'].attrs['units'] = 'NX_ANGLE'
 
# Valid enumeration values for root['/untitled_entry/control']['mode'] are: 
#	 monitor
#	 timer
 
root['/untitled_entry/control'].create_dataset(name='mode', data='monitor', maxshape=None)
root['/untitled_entry/control/mode'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/control/mode'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/control'].create_dataset(name='preset', data=1.0, maxshape=None)
root['/untitled_entry/control/preset'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/control/preset'].attrs['EX_required'] = 'true'
 
root['/untitled_entry/control'].create_dataset(name='integral', data=1.0, maxshape=None)
root['/untitled_entry/control/integral'].attrs['type'] = 'NX_FLOAT'
root['/untitled_entry/control/integral'].attrs['EX_required'] = 'true'
root['/untitled_entry/control/integral'].attrs['units'] = 'NX_ANY'
root['/untitled_entry/definition'].attrs['EX_doc'] = '     Official NeXus NXDL schema to which this file conforms    '
root['/untitled_entry/instrument/source/type'].attrs['EX_doc'] = '       type of radiation source      '
root['/untitled_entry/instrument/source/name'].attrs['EX_doc'] = '       Name of the radiation source      '
root['/untitled_entry/instrument/monochromator/wavelength'].attrs['EX_doc'] = '       The wavelength of the radiation      '
root['/untitled_entry/instrument/monochromator/wavelength_spread'].attrs['EX_doc'] = '       delta_lambda/lambda (:math:`\Delta\lambda/\lambda`):            Important for resolution calculations      '
root['/untitled_entry/instrument/collimator/geometry/shape/size'].attrs['EX_doc'] = '         The collimation length        '
root['/untitled_entry/instrument/detector/data'].attrs['EX_doc'] = '       This is area detector data, of number of x-pixel versus             number of y-pixels. Since the beam center is to be             determined as a step of data reduction, it is not necessary             to document or assume the position of the beam center in             acquired data.      '
root['/untitled_entry/instrument/detector/distance'].attrs['EX_doc'] = '       The distance between detector and sample      '
root['/untitled_entry/instrument/detector/x_pixel_size'].attrs['EX_doc'] = '       Physical size of a pixel in x-direction      '
root['/untitled_entry/instrument/detector/y_pixel_size'].attrs['EX_doc'] = '       Size of a pixel in y direction      '
root['/untitled_entry/instrument/detector/beam_center_x'].attrs['EX_doc'] = '       This is the x position where the direct beam would hit the detector. This is a     length, not a pixel position, and can be outside of the actual detector.      '
root['/untitled_entry/instrument/detector/beam_center_y'].attrs['EX_doc'] = '       This is the y position where the direct beam would hit the detector. This is a     length, not a pixel position, and can be outside of the actual detector.      '
root['/untitled_entry/instrument/name'].attrs['EX_doc'] = '      Name of the instrument actually used to perform the experiment     '
root['/untitled_entry/sample/name'].attrs['EX_doc'] = '      Descriptive name of sample     '
root['/untitled_entry/control/mode'].attrs['EX_doc'] = '      Count to a preset value based on either clock time     (timer) or received monitor counts (monitor).     '
root['/untitled_entry/control/preset'].attrs['EX_doc'] = '      preset value for time or monitor     '
root['/untitled_entry/control/integral'].attrs['EX_doc'] = '      Total integral monitor counts     '
root['/untitled_entry'].attrs['entry'] = '!some char data!'
root['/'].attrs['default'] = 'untitled_entry'
root['/untitled_entry'].attrs['default'] = 'data'
root.attrs['file_name'] = os.path.abspath('NXsas')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.close()


