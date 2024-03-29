 
import numpy as np
from nexusformat.nexus import *
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = NXroot()

# Create the GROUPS 
root['/entry'] = NXentry()
root['/entry'].attrs['EX_required'] = 'true'
root['/entry/user'] = NXuser()
root['/entry/user'].attrs['EX_required'] = 'true'
root['/entry/instrument'] = NXinstrument()
root['/entry/instrument'].attrs['EX_required'] = 'true'
root['/entry/instrument/source'] = NXsource()
root['/entry/instrument/source'].attrs['EX_required'] = 'true'
root['/entry/sample'] = NXsample()
root['/entry/sample'].attrs['EX_required'] = 'true'

# Create the FIELDS 
 
root['/entry/title'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry/experiment_identifier'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/experiment_identifier'].attrs['type'] = 'NX_CHAR'
root['/entry/experiment_identifier'].attrs['EX_required'] = 'true'
 
root['/entry/experiment_description'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/experiment_description'].attrs['type'] = 'NX_CHAR'
root['/entry/experiment_description'].attrs['EX_required'] = 'true'
 
root['/entry/collection_identifier'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/collection_identifier'].attrs['type'] = 'NX_CHAR'
root['/entry/collection_identifier'].attrs['EX_required'] = 'true'
 
root['/entry/collection_description'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/collection_description'].attrs['type'] = 'NX_CHAR'
root['/entry/collection_description'].attrs['EX_required'] = 'true'
 
root['/entry/entry_identifier'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/entry_identifier'].attrs['type'] = 'NX_CHAR'
root['/entry/entry_identifier'].attrs['EX_required'] = 'true'
 
root['/entry/start_time'] = NXfield('2021-03-29T15:51:33.227367')
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
root['/entry/end_time'] = NXfield('2021-03-29T15:51:33.233370')
root['/entry/end_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/end_time'].attrs['EX_required'] = 'true'
 
root['/entry/duration'] = NXfield(1.0)
root['/entry/duration'].attrs['type'] = 'NX_FLOAT'
root['/entry/duration'].attrs['EX_required'] = 'true'
root['/entry/duration'].attrs['units'] = 'NX_TIME'
 
root['/entry/collection_time'] = NXfield(1.0)
root['/entry/collection_time'].attrs['type'] = 'NX_FLOAT'
root['/entry/collection_time'].attrs['EX_required'] = 'true'
root['/entry/collection_time'].attrs['units'] = 'NX_TIME'
 
root['/entry/run_cycle'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/run_cycle'].attrs['type'] = 'NX_CHAR'
root['/entry/run_cycle'].attrs['EX_required'] = 'true'
 
root['/entry/revision'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/revision'].attrs['type'] = 'NX_CHAR'
root['/entry/revision'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXarchive
 
root['/entry/definition'] = NXfield('NXarchive')
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/program'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/program'].attrs['type'] = 'NX_CHAR'
root['/entry/program'].attrs['EX_required'] = 'true'
 
root['/entry/release_date'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/release_date'].attrs['type'] = 'NX_CHAR'
root['/entry/release_date'].attrs['EX_required'] = 'true'
root['/entry/release_date'].attrs['units'] = 'NX_TIME'
 
root['/entry/user/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/user/name'].attrs['type'] = 'NX_CHAR'
root['/entry/user/name'].attrs['EX_required'] = 'true'
 
root['/entry/user/role'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/user/role'].attrs['type'] = 'NX_CHAR'
root['/entry/user/role'].attrs['EX_required'] = 'true'
 
root['/entry/user/facility_user_id'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/user/facility_user_id'].attrs['type'] = 'NX_CHAR'
root['/entry/user/facility_user_id'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/source']['type'] are: 
#	 Spallation Neutron Source
#	 Pulsed Reactor Neutron Source
#	 Reactor Neutron Source
#	 Synchrotron X-Ray Source
#	 Pulsed Muon Source
#	 Rotating Anode X-Ray
#	 Fixed Tube X-Ray
 
root['/entry/instrument/source/type'] = NXfield('Spallation Neutron Source')
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
 
root['/entry/instrument/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/name'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/description'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/description'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/description'].attrs['EX_required'] = 'true'
 
root['/entry/sample/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample/sample_id'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/sample_id'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/sample_id'].attrs['EX_required'] = 'true'
 
root['/entry/sample/description'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/description'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/description'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/sample']['type'] are: 
#	 sample
#	 sample+can
#	 calibration sample
#	 normalisation sample
#	 simulated data
#	 none
#	 sample_environment
 
root['/entry/sample/type'] = NXfield('sample')
root['/entry/sample/type'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/type'].attrs['EX_required'] = 'true'
 
root['/entry/sample/chemical_formula'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/chemical_formula'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/chemical_formula'].attrs['EX_required'] = 'true'
 
root['/entry/sample/preparation_date'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/preparation_date'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/preparation_date'].attrs['EX_required'] = 'true'
root['/entry/sample/preparation_date'].attrs['units'] = 'NX_TIME'
 
root['/entry/sample/situation'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/situation'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/situation'].attrs['EX_required'] = 'true'
 
root['/entry/sample/temperature'] = NXfield(1.0)
root['/entry/sample/temperature'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/temperature'].attrs['EX_required'] = 'true'
root['/entry/sample/temperature'].attrs['units'] = 'NX_TEMPERATURE'
 
root['/entry/sample/magnetic_field'] = NXfield(1.0)
root['/entry/sample/magnetic_field'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/magnetic_field'].attrs['EX_required'] = 'true'
root['/entry/sample/magnetic_field'].attrs['units'] = 'NX_CURRENT'
 
root['/entry/sample/electric_field'] = NXfield(1.0)
root['/entry/sample/electric_field'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/electric_field'].attrs['EX_required'] = 'true'
root['/entry/sample/electric_field'].attrs['units'] = 'NX_VOLTAGE'
 
root['/entry/sample/stress_field'] = NXfield(1.0)
root['/entry/sample/stress_field'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/stress_field'].attrs['EX_required'] = 'true'
root['/entry/sample/stress_field'].attrs['units'] = 'NX_UNITLESS'
 
root['/entry/sample/pressure'] = NXfield(1.0)
root['/entry/sample/pressure'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/pressure'].attrs['EX_required'] = 'true'
root['/entry/sample/pressure'].attrs['units'] = 'NX_PRESSURE'

# Create the DOC strings 
root['/entry/experiment_identifier'].attrs['EX_doc'] = 'unique identifier for the experiment '
root['/entry/experiment_description'].attrs['EX_doc'] = 'Brief description of the experiment and its objectives '
root['/entry/collection_identifier'].attrs['EX_doc'] = 'ID of user or DAQ define group of data files '
root['/entry/collection_description'].attrs['EX_doc'] = 'Brief summary of the collection, including grouping criteria '
root['/entry/entry_identifier'].attrs['EX_doc'] = 'unique identifier for this measurement as provided by the facility '
root['/entry/duration'].attrs['EX_doc'] = 'TODO: needs documentation '
root['/entry/collection_time'].attrs['EX_doc'] = 'TODO: needs documentation '
root['/entry/run_cycle'].attrs['EX_doc'] = 'TODO: needs documentation '
root['/entry/revision'].attrs['EX_doc'] = 'revision ID of this file, may be after recalibration, reprocessing etc. '
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms '
root['/entry/program'].attrs['EX_doc'] = 'The program and version used for generating this file '
root['/entry/release_date'].attrs['EX_doc'] = 'when this file is to be released into PD '
root['/entry/user/role'].attrs['EX_doc'] = 'role of the user '
root['/entry/user/facility_user_id'].attrs['EX_doc'] = 'ID of the user in the facility burocracy database '
root['/entry/instrument/description'].attrs['EX_doc'] = 'Brief description of the instrument '
root['/entry/sample/name'].attrs['EX_doc'] = 'Descriptive name of sample '
root['/entry/sample/sample_id'].attrs['EX_doc'] = 'Unique database id of the sample '
root['/entry/sample/chemical_formula'].attrs['EX_doc'] = 'Chemical formula formatted according to CIF conventions '
root['/entry/sample/situation'].attrs['EX_doc'] = 'Description of the environment the sample is in:   air, vacuum, oxidizing atmosphere, dehydrated, etc. '
 

# Create the ATTRIBUTES 
root['/entry'].attrs['index'] = 'SAMPLE-CHAR-DATA'
root['/entry/program'].attrs['version'] = 'SAMPLE-CHAR-DATA'
root.attrs['default'] = 'entry'

# Save the file
root.save('NXarchive.nxs', 'w')


