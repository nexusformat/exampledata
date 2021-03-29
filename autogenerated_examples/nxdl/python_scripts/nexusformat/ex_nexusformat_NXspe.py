 
import numpy as np
from nexusformat.nexus import *
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = NXroot()

# Create the GROUPS 
root['/entry'] = NXentry()
root['/entry'].attrs['EX_required'] = 'true'
root['/entry/NXSPE_info'] = NXcollection()
root['/entry/NXSPE_info'].attrs['EX_required'] = 'true'
root['/entry/data'] = NXdata()
root['/entry/data'].attrs['EX_required'] = 'true'
root['/entry/instrument'] = NXinstrument()
root['/entry/instrument'].attrs['EX_required'] = 'true'
root['/entry/instrument/NXfermi_chopper'] = NXfermi_chopper()
root['/entry/instrument/NXfermi_chopper'].attrs['EX_required'] = 'true'
root['/entry/sample'] = NXsample()
root['/entry/sample'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
root['/entry/program_name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/program_name'].attrs['type'] = 'NX_CHAR'
root['/entry/program_name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXspe
 
root['/entry/definition'] = NXfield('NXspe')
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/NXSPE_info/fixed_energy'] = NXfield(1.0)
root['/entry/NXSPE_info/fixed_energy'].attrs['type'] = 'NX_FLOAT'
root['/entry/NXSPE_info/fixed_energy'].attrs['EX_required'] = 'true'
root['/entry/NXSPE_info/fixed_energy'].attrs['units'] = 'NX_ENERGY'
 
root['/entry/NXSPE_info/ki_over_kf_scaling'] = NXfield(np.int8(0))
root['/entry/NXSPE_info/ki_over_kf_scaling'].attrs['type'] = 'NX_BOOLEAN'
root['/entry/NXSPE_info/ki_over_kf_scaling'].attrs['EX_required'] = 'true'
 
root['/entry/NXSPE_info/psi'] = NXfield(1.0)
root['/entry/NXSPE_info/psi'].attrs['type'] = 'NX_FLOAT'
root['/entry/NXSPE_info/psi'].attrs['EX_required'] = 'true'
root['/entry/NXSPE_info/psi'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/data/azimuthal'] = NXfield(1.0)
root['/entry/data/azimuthal'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/azimuthal'].attrs['EX_required'] = 'true'
root['/entry/data/azimuthal'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/data/azimuthal_width'] = NXfield(1.0)
root['/entry/data/azimuthal_width'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/azimuthal_width'].attrs['EX_required'] = 'true'
root['/entry/data/azimuthal_width'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/data/polar'] = NXfield(1.0)
root['/entry/data/polar'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/polar'].attrs['EX_required'] = 'true'
root['/entry/data/polar'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/data/polar_width'] = NXfield(1.0)
root['/entry/data/polar_width'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/polar_width'].attrs['EX_required'] = 'true'
root['/entry/data/polar_width'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/data/distance'] = NXfield(1.0)
root['/entry/data/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/distance'].attrs['EX_required'] = 'true'
root['/entry/data/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/data/data'] = NXfield(1.0)
root['/entry/data/data'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/data'].attrs['EX_required'] = 'true'
 
root['/entry/data/error'] = NXfield(1.0)
root['/entry/data/error'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/error'].attrs['EX_required'] = 'true'
 
root['/entry/data/energy'] = NXfield(1.0)
root['/entry/data/energy'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/energy'].attrs['EX_required'] = 'true'
root['/entry/data/energy'].attrs['units'] = 'NX_ENERGY'
 
root['/entry/instrument/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/name'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/NXfermi_chopper/energy'] = NXfield(1.0)
root['/entry/instrument/NXfermi_chopper/energy'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/NXfermi_chopper/energy'].attrs['EX_required'] = 'true'
root['/entry/instrument/NXfermi_chopper/energy'].attrs['units'] = 'NX_ENERGY'
 
root['/entry/sample/rotation_angle'] = NXfield(1.0)
root['/entry/sample/rotation_angle'].attrs['type'] = 'NX_NUMBER'
root['/entry/sample/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample/seblock'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/seblock'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/seblock'].attrs['EX_required'] = 'true'
 
root['/entry/sample/temperature'] = NXfield(1.0)
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
root.attrs['default'] = 'entry'
root['/entry/data'].set_default()
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'

# Save the file
root.save('NXspe.nxs', 'w')


