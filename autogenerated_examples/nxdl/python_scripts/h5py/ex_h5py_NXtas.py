 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('NXtas.h5', 'w')

# Create the GROUPS 
 
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
root['/entry/instrument/monochromator'].attrs['NX_class'] = 'NXcrystal'
root['/entry/instrument/monochromator'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('analyser')
root['/entry/instrument/analyser'].attrs['NX_class'] = 'NXcrystal'
root['/entry/instrument/analyser'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('detector')
root['/entry/instrument/detector'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('monitor')
root['/entry/monitor'].attrs['NX_class'] = 'NXmonitor'
root['/entry/monitor'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('data')
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
root['/entry'].create_dataset(name='title', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='start_time', data='2022-03-03T14:34:16.263999', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXtas
 
root['/entry'].create_dataset(name='definition', data='NXtas', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/source']['probe'] are: 
#	 neutron
#	 x-ray
 
root['/entry/instrument/source'].create_dataset(name='probe', data='neutron', maxshape=None)
root['/entry/instrument/source/probe'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/probe'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/monochromator'].create_dataset(name='ei', data=1.0, maxshape=None)
root['/entry/instrument/monochromator/ei'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/monochromator/ei'].attrs['EX_required'] = 'true'
root['/entry/instrument/monochromator/ei'].attrs['axis'] = '1'
root['/entry/instrument/monochromator/ei'].attrs['units'] = 'NX_ENERGY'
 
root['/entry/instrument/monochromator'].create_dataset(name='rotation_angle', data=1.0, maxshape=None)
root['/entry/instrument/monochromator/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/monochromator/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/monochromator/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/analyser'].create_dataset(name='ef', data=1.0, maxshape=None)
root['/entry/instrument/analyser/ef'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/analyser/ef'].attrs['EX_required'] = 'true'
root['/entry/instrument/analyser/ef'].attrs['axis'] = '1'
root['/entry/instrument/analyser/ef'].attrs['units'] = 'NX_ENERGY'
 
root['/entry/instrument/analyser'].create_dataset(name='rotation_angle', data=1.0, maxshape=None)
root['/entry/instrument/analyser/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/analyser/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/analyser/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/analyser'].create_dataset(name='polar_angle', data=1.0, maxshape=None)
root['/entry/instrument/analyser/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/analyser/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/analyser/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector'].create_dataset(name='data', data=1, maxshape=None)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/entry/instrument/detector'].create_dataset(name='polar_angle', data=1.0, maxshape=None)
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='qh', data=1.0, maxshape=None)
root['/entry/sample/qh'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/qh'].attrs['EX_required'] = 'true'
root['/entry/sample/qh'].attrs['axis'] = '1'
root['/entry/sample/qh'].attrs['units'] = 'NX_DIMENSIONLESS'
 
root['/entry/sample'].create_dataset(name='qk', data=1.0, maxshape=None)
root['/entry/sample/qk'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/qk'].attrs['EX_required'] = 'true'
root['/entry/sample/qk'].attrs['axis'] = '1'
root['/entry/sample/qk'].attrs['units'] = 'NX_DIMENSIONLESS'
 
root['/entry/sample'].create_dataset(name='ql', data=1.0, maxshape=None)
root['/entry/sample/ql'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/ql'].attrs['EX_required'] = 'true'
root['/entry/sample/ql'].attrs['axis'] = '1'
root['/entry/sample/ql'].attrs['units'] = 'NX_DIMENSIONLESS'
 
root['/entry/sample'].create_dataset(name='en', data=1.0, maxshape=None)
root['/entry/sample/en'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/en'].attrs['EX_required'] = 'true'
root['/entry/sample/en'].attrs['axis'] = '1'
root['/entry/sample/en'].attrs['units'] = 'NX_ENERGY'
 
root['/entry/sample'].create_dataset(name='rotation_angle', data=1.0, maxshape=None)
root['/entry/sample/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='polar_angle', data=1.0, maxshape=None)
root['/entry/sample/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/polar_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='sgu', data=1.0, maxshape=None)
root['/entry/sample/sgu'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/sgu'].attrs['EX_required'] = 'true'
root['/entry/sample/sgu'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='sgl', data=1.0, maxshape=None)
root['/entry/sample/sgl'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/sgl'].attrs['EX_required'] = 'true'
root['/entry/sample/sgl'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='unit_cell', data=1.0, maxshape=None)
root['/entry/sample/unit_cell'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/unit_cell'].attrs['EX_required'] = 'true'
root['/entry/sample/unit_cell'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/sample'].create_dataset(name='orientation_matrix', data=1.0, maxshape=None)
root['/entry/sample/orientation_matrix'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/orientation_matrix'].attrs['EX_required'] = 'true'
root['/entry/sample/orientation_matrix'].attrs['units'] = 'NX_DIMENSIONLESS'
 
# Valid enumeration values for root['/entry/monitor']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/monitor'].create_dataset(name='mode', data='monitor', maxshape=None)
root['/entry/monitor/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/monitor/mode'].attrs['EX_required'] = 'true'
 
root['/entry/monitor'].create_dataset(name='preset', data=1.0, maxshape=None)
root['/entry/monitor/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/monitor/preset'].attrs['EX_required'] = 'true'
 
root['/entry/monitor'].create_dataset(name='data', data=1.0, maxshape=None)
root['/entry/monitor/data'].attrs['type'] = 'NX_FLOAT'
root['/entry/monitor/data'].attrs['EX_required'] = 'true'
root['/entry/monitor/data'].attrs['units'] = 'NX_ANY'

# Create the LINKS 
root['/entry/data/ei'] = h5py.SoftLink('/entry/instrument/monochromator/ei')
root['/entry/data/ei/'].attrs['target'] = '/entry/instrument/monochromator/ei'

# Create the LINKS 
root['/entry/data/ef'] = h5py.SoftLink('/entry/title')
root['/entry/data/ef/'].attrs['target'] = '/entry/instrument/analyzer/ef'

# Create the LINKS 
root['/entry/data/en'] = h5py.SoftLink('/entry/sample/en')
root['/entry/data/en/'].attrs['target'] = '/entry/sample/en'

# Create the LINKS 
root['/entry/data/qh'] = h5py.SoftLink('/entry/sample/qh')
root['/entry/data/qh/'].attrs['target'] = '/entry/sample/qh'

# Create the LINKS 
root['/entry/data/qk'] = h5py.SoftLink('/entry/sample/qk')
root['/entry/data/qk/'].attrs['target'] = '/entry/sample/qk'

# Create the LINKS 
root['/entry/data/ql'] = h5py.SoftLink('/entry/sample/ql')
root['/entry/data/ql/'].attrs['target'] = '/entry/sample/ql'

# Create the LINKS 
root['/entry/data/data'] = h5py.SoftLink('/entry/instrument/detector/data')
root['/entry/data/data/'].attrs['target'] = '/entry/instrument/detector/data'

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms '
root['/entry/sample/name'].attrs['EX_doc'] = 'Descriptive name of sample '
root['/entry/monitor/mode'].attrs['EX_doc'] = 'Count to a preset value based on either clock time (timer) or received monitor counts (monitor). '
root['/entry/monitor/preset'].attrs['EX_doc'] = 'preset value for time or monitor '
root['/entry/monitor/data'].attrs['EX_doc'] = 'Total integral monitor counts '
root['/entry/data'].attrs['EX_doc'] = 'One of the ei,ef,qh,qk,ql,en should get a primary=1 attribute to denote the main scan axis '
 

# Create the ATTRIBUTES 
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXtas')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version

# Close the file
root.close()


