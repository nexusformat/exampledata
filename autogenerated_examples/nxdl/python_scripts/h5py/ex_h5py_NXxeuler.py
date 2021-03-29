 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('NXxeuler.h5', 'w')
 
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
 
root['/entry/'].create_group('name')
root['/entry/name'].attrs['NX_class'] = 'NXdata'
root['/entry/name'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='title', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='start_time', data='2021-03-29T13:51:00.374705', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXxbase
#	 NXxeuler
 
root['/entry'].create_dataset(name='definition', data='NXxbase', maxshape=None)
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
 
root['/entry/instrument/monochromator'].create_dataset(name='wavelength', data=1.0, maxshape=None)
root['/entry/instrument/monochromator/wavelength'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/monochromator/wavelength'].attrs['EX_required'] = 'true'
root['/entry/instrument/monochromator/wavelength'].attrs['units'] = 'NX_WAVELENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='data', data=1, maxshape=None)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/entry/instrument/detector'].create_dataset(name='x_pixel_size', data=1.0, maxshape=None)
root['/entry/instrument/detector/x_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/x_pixel_size'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/x_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='y_pixel_size', data=1.0, maxshape=None)
root['/entry/instrument/detector/y_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/y_pixel_size'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/y_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='distance', data=1.0, maxshape=None)
root['/entry/instrument/detector/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/distance'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='frame_start_number', data=1, maxshape=None)
root['/entry/instrument/detector/frame_start_number'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/frame_start_number'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='orientation_matrix', data=1.0, maxshape=None)
root['/entry/sample/orientation_matrix'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/orientation_matrix'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='unit_cell', data=1.0, maxshape=None)
root['/entry/sample/unit_cell'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/unit_cell'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='temperature', data=1.0, maxshape=None)
root['/entry/sample/temperature'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/temperature'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='x_translation', data=1.0, maxshape=None)
root['/entry/sample/x_translation'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/x_translation'].attrs['EX_required'] = 'true'
root['/entry/sample/x_translation'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/sample'].create_dataset(name='y_translation', data=1.0, maxshape=None)
root['/entry/sample/y_translation'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/y_translation'].attrs['EX_required'] = 'true'
root['/entry/sample/y_translation'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/sample'].create_dataset(name='distance', data=1.0, maxshape=None)
root['/entry/sample/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/distance'].attrs['EX_required'] = 'true'
root['/entry/sample/distance'].attrs['units'] = 'NX_LENGTH'
 
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
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXxbase
#	 NXxeuler
 
root['/entry/instrument/detector'].create_dataset(name='polar_angle', data=1.0, maxshape=None)
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/polar_angle'].attrs['axis'] = '1'
root['/entry/instrument/detector/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='rotation_angle', data=1.0, maxshape=None)
root['/entry/sample/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/rotation_angle'].attrs['axis'] = '1'
root['/entry/sample/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='chi', data=1.0, maxshape=None)
root['/entry/sample/chi'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/chi'].attrs['EX_required'] = 'true'
root['/entry/sample/chi'].attrs['axis'] = '1'
root['/entry/sample/chi'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='phi', data=1.0, maxshape=None)
root['/entry/sample/phi'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/phi'].attrs['EX_required'] = 'true'
root['/entry/sample/phi'].attrs['signal'] = '1'
root['/entry/sample/phi'].attrs['units'] = 'NX_ANGLE'
 
# Create the soft links 
root['/entry/data/data'] = h5py.SoftLink('/entry/instrument/detector/data')
root['/entry/data/data/'].attrs['target'] = '/entry/instrument/detector/data'
 
# Create the soft links 
root['/entry/name/polar_angle'] = h5py.SoftLink('/entry/instrument/detector/polar_angle')
root['/entry/name/polar_angle/'].attrs['target'] = '/entry/instrument/detector/polar_angle'
 
# Create the soft links 
root['/entry/name/rotation_angle'] = h5py.SoftLink('/entry/sample/rotation_angle')
root['/entry/name/rotation_angle/'].attrs['target'] = '/entry/sample/rotation_angle'
 
# Create the soft links 
root['/entry/name/chi'] = h5py.SoftLink('/entry/sample/chi')
root['/entry/name/chi/'].attrs['target'] = '/entry/sample/chi'
 
# Create the soft links 
root['/entry/name/phi'] = h5py.SoftLink('/entry/sample/phi')
root['/entry/name/phi/'].attrs['target'] = '/entry/sample/phi'
 
# Assign all of the doc strings
root['/entry/definition'].attrs['EX_doc'] = ' Official NeXus NXDL schema to which this file conforms '
root['/entry/instrument/detector/data'].attrs['EX_doc'] = ' The area detector data, the first dimension is always the number of scan points, the second and third are the number of pixels in x and y. The origin is always assumed to be in the center of the detector. maxOccurs is limited to the the number of detectors on your instrument. '
root['/entry/instrument/detector'].attrs['EX_doc'] = ' The name of the group is detector if there is only one detector, if there are several, names have to be detector1, detector2, ...detectorn. '
root['/entry/instrument/detector/frame_start_number'].attrs['EX_doc'] = ' This is the start number of the first frame of a scan. In PX one often scans a couple of frames on a give sample, then does something else, then returns to the same sample and scans some more frames. Each time with a new data file. This number helps concatenating such measurements. '
root['/entry/sample/name'].attrs['EX_doc'] = ' Descriptive name of sample '
root['/entry/sample/orientation_matrix'].attrs['EX_doc'] = ' The orientation matrix according to Busing and Levy conventions. This is not strictly necessary as the UB can always be derived from the data. But let us bow to common usage which includes the UB nearly always. '
root['/entry/sample/unit_cell'].attrs['EX_doc'] = ' The unit cell, a, b, c, alpha, beta, gamma. Again, not strictly necessary, but normally written. '
root['/entry/sample/temperature'].attrs['EX_doc'] = ' The sample temperature or whatever sensor represents this value best '
root['/entry/sample/x_translation'].attrs['EX_doc'] = ' Translation of the sample along the X-direction of the laboratory coordinate system '
root['/entry/sample/y_translation'].attrs['EX_doc'] = ' Translation of the sample along the Y-direction of the laboratory coordinate system '
root['/entry/sample/distance'].attrs['EX_doc'] = ' Translation of the sample along the Z-direction of the laboratory coordinate system '
root['/entry/control/mode'].attrs['EX_doc'] = ' Count to a preset value based on either clock time (timer) or received monitor counts (monitor). '
root['/entry/control/preset'].attrs['EX_doc'] = ' preset value for time or monitor '
root['/entry/control/integral'].attrs['EX_doc'] = ' Total integral monitor counts '
root['/entry/data'].attrs['EX_doc'] = ' The name of this group id data if there is only one detector; if there are several the names will be data1, data2, data3 and will point to the corresponding detector groups in the instrument hierarchy. '
root['/entry/definition'].attrs['EX_doc'] = ' Official NeXus NXDL schema to which this file conforms '
root['/entry/instrument/detector/polar_angle'].attrs['EX_doc'] = ' The polar_angle (two theta) where the detector is placed at each scan point. '
root['/entry/sample/rotation_angle'].attrs['EX_doc'] = ' This is an array holding the sample rotation angle at each scan point '
root['/entry/sample/chi'].attrs['EX_doc'] = ' This is an array holding the chi angle of the eulerian cradle at each scan point '
root['/entry/sample/phi'].attrs['EX_doc'] = ' This is an array holding the phi rotation of the eulerian cradle at each scan point '
 
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXxeuler')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.close()


