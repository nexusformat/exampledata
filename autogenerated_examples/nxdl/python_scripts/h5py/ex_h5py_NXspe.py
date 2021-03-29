 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('NXspe.h5', 'w')

# Create the GROUPS 
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('NXSPE_info')
root['/entry/NXSPE_info'].attrs['NX_class'] = 'NXcollection'
root['/entry/NXSPE_info'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('data')
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('instrument')
root['/entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/instrument'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('NXfermi_chopper')
root['/entry/instrument/NXfermi_chopper'].attrs['NX_class'] = 'NXfermi_chopper'
root['/entry/instrument/NXfermi_chopper'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
root['/entry'].create_dataset(name='program_name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/program_name'].attrs['type'] = 'NX_CHAR'
root['/entry/program_name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXspe
 
root['/entry'].create_dataset(name='definition', data='NXspe', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/NXSPE_info'].create_dataset(name='fixed_energy', data=1.0, maxshape=None)
root['/entry/NXSPE_info/fixed_energy'].attrs['type'] = 'NX_FLOAT'
root['/entry/NXSPE_info/fixed_energy'].attrs['EX_required'] = 'true'
root['/entry/NXSPE_info/fixed_energy'].attrs['units'] = 'NX_ENERGY'
 
root['/entry/NXSPE_info'].create_dataset(name='ki_over_kf_scaling', data=np.int8(0), maxshape=None)
root['/entry/NXSPE_info/ki_over_kf_scaling'].attrs['type'] = 'NX_BOOLEAN'
root['/entry/NXSPE_info/ki_over_kf_scaling'].attrs['EX_required'] = 'true'
 
root['/entry/NXSPE_info'].create_dataset(name='psi', data=1.0, maxshape=None)
root['/entry/NXSPE_info/psi'].attrs['type'] = 'NX_FLOAT'
root['/entry/NXSPE_info/psi'].attrs['EX_required'] = 'true'
root['/entry/NXSPE_info/psi'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/data'].create_dataset(name='azimuthal', data=1.0, maxshape=None)
root['/entry/data/azimuthal'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/azimuthal'].attrs['EX_required'] = 'true'
root['/entry/data/azimuthal'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/data'].create_dataset(name='azimuthal_width', data=1.0, maxshape=None)
root['/entry/data/azimuthal_width'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/azimuthal_width'].attrs['EX_required'] = 'true'
root['/entry/data/azimuthal_width'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/data'].create_dataset(name='polar', data=1.0, maxshape=None)
root['/entry/data/polar'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/polar'].attrs['EX_required'] = 'true'
root['/entry/data/polar'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/data'].create_dataset(name='polar_width', data=1.0, maxshape=None)
root['/entry/data/polar_width'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/polar_width'].attrs['EX_required'] = 'true'
root['/entry/data/polar_width'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/data'].create_dataset(name='distance', data=1.0, maxshape=None)
root['/entry/data/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/distance'].attrs['EX_required'] = 'true'
root['/entry/data/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/data'].create_dataset(name='data', data=1.0, maxshape=None)
root['/entry/data/data'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/data'].attrs['EX_required'] = 'true'
 
root['/entry/data'].create_dataset(name='error', data=1.0, maxshape=None)
root['/entry/data/error'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/error'].attrs['EX_required'] = 'true'
 
root['/entry/data'].create_dataset(name='energy', data=1.0, maxshape=None)
root['/entry/data/energy'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/energy'].attrs['EX_required'] = 'true'
root['/entry/data/energy'].attrs['units'] = 'NX_ENERGY'
 
root['/entry/instrument'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/name'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/NXfermi_chopper'].create_dataset(name='energy', data=1.0, maxshape=None)
root['/entry/instrument/NXfermi_chopper/energy'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/NXfermi_chopper/energy'].attrs['EX_required'] = 'true'
root['/entry/instrument/NXfermi_chopper/energy'].attrs['units'] = 'NX_ENERGY'
 
root['/entry/sample'].create_dataset(name='rotation_angle', data=1.0, maxshape=None)
root['/entry/sample/rotation_angle'].attrs['type'] = 'NX_NUMBER'
root['/entry/sample/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='seblock', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/sample/seblock'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/seblock'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='temperature', data=1.0, maxshape=None)
root['/entry/sample/temperature'].attrs['type'] = 'NX_NUMBER'
root['/entry/sample/temperature'].attrs['EX_required'] = 'true'
root['/entry/sample/temperature'].attrs['units'] = 'NX_TEMPERATURE'

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = ' Official NeXus NXDL schema to which this file conforms. '
root['/entry/NXSPE_info/fixed_energy'].attrs['EX_doc'] = ' The fixed energy used for this file. '
root['/entry/NXSPE_info/ki_over_kf_scaling'].attrs['EX_doc'] = ' Indicates whether ki/kf scaling has been applied or not. '
root['/entry/NXSPE_info/psi'].attrs['EX_doc'] = ' Orientation angle as expected in DCS-MSlice '
 

# Create the ATTRIBUTES 
root['/entry/definition'].attrs['version'] = 'SAMPLE-CHAR-DATA'
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXspe')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version

# Close the file
root.close()


