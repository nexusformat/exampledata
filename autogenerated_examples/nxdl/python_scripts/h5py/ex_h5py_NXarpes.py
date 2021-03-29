 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('NXarpes.h5', 'w')

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
root['/entry/instrument/monochromator'].attrs['NX_class'] = 'NXmonochromator'
root['/entry/instrument/monochromator'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('analyser')
root['/entry/instrument/analyser'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/analyser'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('data')
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
root['/entry'].create_dataset(name='title', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='start_time', data='2021-03-29T15:51:33.838489', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXarpes
 
root['/entry'].create_dataset(name='definition', data='NXarpes', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source'].create_dataset(name='type', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/type'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/type'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/source']['probe'] are: 
#	 x-ray
 
root['/entry/instrument/source'].create_dataset(name='probe', data='x-ray', maxshape=None)
root['/entry/instrument/source/probe'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/probe'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/monochromator'].create_dataset(name='energy', data=1.0, maxshape=None)
root['/entry/instrument/monochromator/energy'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/monochromator/energy'].attrs['EX_required'] = 'true'
root['/entry/instrument/monochromator/energy'].attrs['units'] = 'NX_ENERGY'
 
root['/entry/instrument/analyser'].create_dataset(name='data', data=1.0, maxshape=None)
root['/entry/instrument/analyser/data'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/analyser/data'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/analyser'].create_dataset(name='lens_mode', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/analyser/lens_mode'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/analyser/lens_mode'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/analyser']['acquisition_mode'] are: 
#	 swept
#	 fixed
 
root['/entry/instrument/analyser'].create_dataset(name='acquisition_mode', data='swept', maxshape=None)
root['/entry/instrument/analyser/acquisition_mode'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/analyser/acquisition_mode'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/analyser']['entrance_slit_shape'] are: 
#	 curved
#	 straight
 
root['/entry/instrument/analyser'].create_dataset(name='entrance_slit_shape', data='curved', maxshape=None)
root['/entry/instrument/analyser/entrance_slit_shape'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/analyser/entrance_slit_shape'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/analyser'].create_dataset(name='entrance_slit_setting', data=1.0, maxshape=None)
root['/entry/instrument/analyser/entrance_slit_setting'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/analyser/entrance_slit_setting'].attrs['EX_required'] = 'true'
root['/entry/instrument/analyser/entrance_slit_setting'].attrs['units'] = 'NX_ANY'
 
root['/entry/instrument/analyser'].create_dataset(name='entrance_slit_size', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/analyser/entrance_slit_size'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/analyser/entrance_slit_size'].attrs['units'] = 'NX_LENGTH'
root['/entry/instrument/analyser/entrance_slit_size'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/analyser'].create_dataset(name='pass_energy', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/analyser/pass_energy'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/analyser/pass_energy'].attrs['units'] = 'NX_ENERGY'
root['/entry/instrument/analyser/pass_energy'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/analyser'].create_dataset(name='time_per_channel', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/analyser/time_per_channel'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/analyser/time_per_channel'].attrs['units'] = 'NX_TIME'
root['/entry/instrument/analyser/time_per_channel'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/analyser'].create_dataset(name='angles', data=1.0, maxshape=None)
root['/entry/instrument/analyser/angles'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/analyser/angles'].attrs['EX_required'] = 'true'
root['/entry/instrument/analyser/angles'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/analyser'].create_dataset(name='energies', data=1.0, maxshape=None)
root['/entry/instrument/analyser/energies'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/analyser/energies'].attrs['EX_required'] = 'true'
root['/entry/instrument/analyser/energies'].attrs['units'] = 'NX_ENERGY'
 
root['/entry/instrument/analyser'].create_dataset(name='sensor_size', data=1, maxshape=None)
root['/entry/instrument/analyser/sensor_size'].attrs['type'] = 'NX_INT'
root['/entry/instrument/analyser/sensor_size'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/analyser'].create_dataset(name='region_origin', data=1, maxshape=None)
root['/entry/instrument/analyser/region_origin'].attrs['type'] = 'NX_INT'
root['/entry/instrument/analyser/region_origin'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/analyser'].create_dataset(name='region_size', data=1, maxshape=None)
root['/entry/instrument/analyser/region_size'].attrs['type'] = 'NX_INT'
root['/entry/instrument/analyser/region_size'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='temperature', data=1.0, maxshape=None)
root['/entry/sample/temperature'].attrs['type'] = 'NX_NUMBER'
root['/entry/sample/temperature'].attrs['EX_required'] = 'true'
root['/entry/sample/temperature'].attrs['units'] = 'NX_TEMPERATURE'

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms. '
root['/entry/instrument/analyser/lens_mode'].attrs['EX_doc'] = 'setting for the electron analyser lens '
root['/entry/instrument/analyser/entrance_slit_setting'].attrs['EX_doc'] = 'dial setting of the entrance slit '
root['/entry/instrument/analyser/entrance_slit_size'].attrs['EX_doc'] = 'size of the entrance slit '
root['/entry/instrument/analyser/pass_energy'].attrs['EX_doc'] = 'energy of the electrons on the mean path of the analyser '
root['/entry/instrument/analyser/time_per_channel'].attrs['EX_doc'] = 'todo: define more clearly '
root['/entry/instrument/analyser/angles'].attrs['EX_doc'] = 'Angular axis of the analyser data which dimension the axis applies to is defined using the normal NXdata methods. '
root['/entry/instrument/analyser/energies'].attrs['EX_doc'] = 'Energy axis of the analyser data which dimension the axis applies to is defined using the normal NXdata methods. '
root['/entry/instrument/analyser/sensor_size'].attrs['EX_doc'] = 'number of raw active elements in each dimension '
root['/entry/instrument/analyser/region_origin'].attrs['EX_doc'] = 'origin of rectangular region selected for readout '
root['/entry/instrument/analyser/region_size'].attrs['EX_doc'] = 'size of rectangular region selected for readout '
root['/entry/sample/name'].attrs['EX_doc'] = 'Descriptive name of sample '
 

# Create the ATTRIBUTES 
root['/entry'].attrs['entry'] = 'SAMPLE-CHAR-DATA'
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root.attrs['file_name'] = os.path.abspath('NXarpes')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version

# Close the file
root.close()


