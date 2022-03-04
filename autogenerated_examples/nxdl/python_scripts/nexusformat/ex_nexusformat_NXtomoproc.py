 
import numpy as np
from nexusformat.nexus import *
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = NXroot()

# Create the GROUPS 
root['/entry'] = NXentry()
root['/entry'].attrs['EX_required'] = 'true'
root['/entry/instrument'] = NXinstrument()
root['/entry/instrument'].attrs['EX_required'] = 'true'
root['/entry/instrument/source'] = NXsource()
root['/entry/instrument/source'].attrs['EX_required'] = 'true'
root['/entry/sample'] = NXsample()
root['/entry/sample'].attrs['EX_required'] = 'true'
root['/entry/reconstruction'] = NXprocess()
root['/entry/reconstruction'].attrs['EX_required'] = 'true'
root['/entry/reconstruction/parameters'] = NXparameters()
root['/entry/reconstruction/parameters'].attrs['EX_required'] = 'true'
root['/entry/data'] = NXdata()
root['/entry/data'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
root['/entry/title'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXtomoproc
 
root['/entry/definition'] = NXfield('NXtomoproc')
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source/type'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/source/type'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/type'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/source/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/source']['probe'] are: 
#	 neutron
#	 x-ray
#	 electron
 
root['/entry/instrument/source/probe'] = NXfield('neutron')
root['/entry/instrument/source/probe'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/probe'].attrs['EX_required'] = 'true'
 
root['/entry/sample/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/reconstruction/program'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/reconstruction/program'].attrs['type'] = 'NX_CHAR'
root['/entry/reconstruction/program'].attrs['EX_required'] = 'true'
 
root['/entry/reconstruction/version'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/reconstruction/version'].attrs['type'] = 'NX_CHAR'
root['/entry/reconstruction/version'].attrs['EX_required'] = 'true'
 
root['/entry/reconstruction/date'] = NXfield('2022-03-04T14:56:38.000624')
root['/entry/reconstruction/date'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/reconstruction/date'].attrs['EX_required'] = 'true'
 
root['/entry/reconstruction/parameters/raw_file'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/reconstruction/parameters/raw_file'].attrs['type'] = 'NX_CHAR'
root['/entry/reconstruction/parameters/raw_file'].attrs['EX_required'] = 'true'
 
root['/entry/data/data'] = NXfield(1)
root['/entry/data/data'].attrs['type'] = 'NX_INT'
root['/entry/data/data'].attrs['EX_required'] = 'true'
root['/entry/data/data'].attrs['signal'] = '1'
 
root['/entry/data/x'] = NXfield(1.0)
root['/entry/data/x'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/x'].attrs['EX_required'] = 'true'
root['/entry/data/x'].attrs['axis'] = '1'
root['/entry/data/x'].attrs['units'] = 'NX_ANY'
 
root['/entry/data/y'] = NXfield(1.0)
root['/entry/data/y'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/y'].attrs['EX_required'] = 'true'
root['/entry/data/y'].attrs['axis'] = '2'
root['/entry/data/y'].attrs['units'] = 'NX_ANY'
 
root['/entry/data/z'] = NXfield(1.0)
root['/entry/data/z'].attrs['type'] = 'NX_FLOAT'
root['/entry/data/z'].attrs['EX_required'] = 'true'
root['/entry/data/z'].attrs['axis'] = '3'
root['/entry/data/z'].attrs['units'] = 'NX_ANY'

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms '
root['/entry/sample/name'].attrs['EX_doc'] = 'Descriptive name of sample '
root['/entry/reconstruction/program'].attrs['EX_doc'] = 'Name of the program used for reconstruction '
root['/entry/reconstruction/version'].attrs['EX_doc'] = 'Version of the program used '
root['/entry/reconstruction/date'].attrs['EX_doc'] = 'Date and time of reconstruction processing. '
root['/entry/reconstruction/parameters/raw_file'].attrs['EX_doc'] = 'Original raw data file this data was derived from '
root['/entry/data/data'].attrs['EX_doc'] = 'This is the reconstructed volume. This can be different things. Please indicate in the unit attribute what physical quantity this really is. '
root['/entry/data/x'].attrs['EX_doc'] = 'This is an array holding the values to use for the x-axis of data. The units must be appropriate for the measurement. '
root['/entry/data/y'].attrs['EX_doc'] = 'This is an array holding the values to use for the y-axis of data. The units must be appropriate for the measurement. '
root['/entry/data/z'].attrs['EX_doc'] = 'This is an array holding the values to use for the z-axis of data. The units must be appropriate for the measurement. '
 

# Create the ATTRIBUTES 
root['/entry/data/data'].attrs['transform'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/data'].attrs['offset'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/data'].attrs['scaling'] = 'SAMPLE-CHAR-DATA'
root.attrs['default'] = 'entry'
root['/entry/data'].set_default()
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'

# Save the file
root.save('NXtomoproc.nxs', 'w')


