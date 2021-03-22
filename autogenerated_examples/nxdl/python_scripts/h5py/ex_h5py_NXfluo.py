 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('h5py_NXfluo.h5', 'w')
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('untitled_instrument')
root['/entry/untitled_instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/untitled_instrument'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/'].create_group('untitled_source')
root['/entry/untitled_instrument/untitled_source'].attrs['NX_class'] = 'NXsource'
root['/entry/untitled_instrument/untitled_source'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/'].create_group('monochromator')
root['/entry/untitled_instrument/monochromator'].attrs['NX_class'] = 'NXmonochromator'
root['/entry/untitled_instrument/monochromator'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/'].create_group('fluorescence')
root['/entry/untitled_instrument/fluorescence'].attrs['NX_class'] = 'NXdetector'
root['/entry/untitled_instrument/fluorescence'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('untitled_sample')
root['/entry/untitled_sample'].attrs['NX_class'] = 'NXsample'
root['/entry/untitled_sample'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('untitled_monitor')
root['/entry/untitled_monitor'].attrs['NX_class'] = 'NXmonitor'
root['/entry/untitled_monitor'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('data')
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='title', data=1.0, maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_FLOAT'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='start_time', data='2021-03-22T16:42:15.565312', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXfluo
 
root['/entry'].create_dataset(name='definition', data='NXfluo', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/untitled_source'].create_dataset(name='type', data='2021-03-22T16:42:15.567312', maxshape=None)
root['/entry/untitled_instrument/untitled_source/type'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/untitled_instrument/untitled_source/type'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/untitled_source'].create_dataset(name='name', data='2021-03-22T16:42:15.568313', maxshape=None)
root['/entry/untitled_instrument/untitled_source/name'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/untitled_instrument/untitled_source/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/untitled_instrument/untitled_source']['probe'] are: 
#	 x-ray
 
root['/entry/untitled_instrument/untitled_source'].create_dataset(name='probe', data='x-ray', maxshape=None)
root['/entry/untitled_instrument/untitled_source/probe'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/untitled_instrument/untitled_source/probe'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/monochromator'].create_dataset(name='wavelength', data=1.0, maxshape=None)
root['/entry/untitled_instrument/monochromator/wavelength'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_instrument/monochromator/wavelength'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_instrument/fluorescence'].create_dataset(name='data', data=[1], maxshape=None)
root['/entry/untitled_instrument/fluorescence/data'].attrs['type'] = 'NX_INT'
root['/entry/untitled_instrument/fluorescence/data'].attrs['EX_required'] = 'true'
root['/entry/untitled_instrument/fluorescence/data'].attrs['axes'] = 'energy'
root['/entry/untitled_instrument/fluorescence/data'].attrs['signal'] = '1'
 
root['/entry/untitled_instrument/fluorescence'].create_dataset(name='energy', data=[1.], maxshape=None, compression="gzip")
root['/entry/untitled_instrument/fluorescence/energy'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_instrument/fluorescence/energy'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_sample'].create_dataset(name='name', data=1.0, maxshape=None)
root['/entry/untitled_sample/name'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_sample/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/untitled_monitor']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/untitled_monitor'].create_dataset(name='mode', data='monitor', maxshape=None)
root['/entry/untitled_monitor/mode'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_monitor/mode'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_monitor'].create_dataset(name='preset', data=1.0, maxshape=None)
root['/entry/untitled_monitor/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/untitled_monitor/preset'].attrs['EX_required'] = 'true'
 
root['/entry/untitled_monitor'].create_dataset(name='data', data=1, maxshape=None)
root['/entry/untitled_monitor/data'].attrs['type'] = 'NX_INT'
root['/entry/untitled_monitor/data'].attrs['EX_required'] = 'true'
root['/entry/definition'].attrs['EX_doc'] = '     Official NeXus NXDL schema to which this file conforms.    '
root['/entry/untitled_sample/name'].attrs['EX_doc'] = '      Descriptive name of sample     '
root['/entry/untitled_monitor/mode'].attrs['EX_doc'] = '      Count to a preset value based on either clock time (timer)             or received monitor counts (monitor).     '
root['/entry/untitled_monitor/preset'].attrs['EX_doc'] = '      preset value for time or monitor     '
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root.attrs['file_name'] = os.path.abspath('NXfluo')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.close()


