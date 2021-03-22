 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('h5py_NXarchive.h5', 'w')
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('user')
root['/entry/user'].attrs['NX_class'] = 'NXuser'
root['/entry/user'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('instrument')
root['/entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/instrument'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('untitled_source')
root['/entry/instrument/untitled_source'].attrs['NX_class'] = 'NXsource'
root['/entry/instrument/untitled_source'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='title', data='!some char data!', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='experiment_identifier', data='!some char data!', maxshape=None)
root['/entry/experiment_identifier'].attrs['type'] = 'NX_CHAR'
root['/entry/experiment_identifier'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='experiment_description', data='!some char data!', maxshape=None)
root['/entry/experiment_description'].attrs['type'] = 'NX_CHAR'
root['/entry/experiment_description'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='collection_identifier', data='!some char data!', maxshape=None)
root['/entry/collection_identifier'].attrs['type'] = 'NX_CHAR'
root['/entry/collection_identifier'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='collection_description', data='!some char data!', maxshape=None)
root['/entry/collection_description'].attrs['type'] = 'NX_CHAR'
root['/entry/collection_description'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='entry_identifier', data='!some char data!', maxshape=None)
root['/entry/entry_identifier'].attrs['type'] = 'NX_CHAR'
root['/entry/entry_identifier'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='start_time', data='2021-03-22T16:42:15.218447', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='end_time', data='2021-03-22T16:42:15.219447', maxshape=None)
root['/entry/end_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/end_time'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='duration', data=1.0, maxshape=None)
root['/entry/duration'].attrs['type'] = 'NX_FLOAT'
root['/entry/duration'].attrs['EX_required'] = 'true'
root['/entry/duration'].attrs['units'] = 'NX_TIME'
 
root['/entry'].create_dataset(name='collection_time', data=1.0, maxshape=None)
root['/entry/collection_time'].attrs['type'] = 'NX_FLOAT'
root['/entry/collection_time'].attrs['EX_required'] = 'true'
root['/entry/collection_time'].attrs['units'] = 'NX_TIME'
 
root['/entry'].create_dataset(name='run_cycle', data='!some char data!', maxshape=None)
root['/entry/run_cycle'].attrs['type'] = 'NX_CHAR'
root['/entry/run_cycle'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='revision', data='!some char data!', maxshape=None)
root['/entry/revision'].attrs['type'] = 'NX_CHAR'
root['/entry/revision'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXarchive
 
root['/entry'].create_dataset(name='definition', data='NXarchive', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='program', data='!some char data!', maxshape=None)
root['/entry/program'].attrs['type'] = 'NX_CHAR'
root['/entry/program'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='release_date', data='!some char data!', maxshape=None)
root['/entry/release_date'].attrs['type'] = 'NX_CHAR'
root['/entry/release_date'].attrs['EX_required'] = 'true'
root['/entry/release_date'].attrs['units'] = 'NX_TIME'
 
root['/entry/user'].create_dataset(name='name', data='!some char data!', maxshape=None)
root['/entry/user/name'].attrs['type'] = 'NX_CHAR'
root['/entry/user/name'].attrs['EX_required'] = 'true'
 
root['/entry/user'].create_dataset(name='role', data='!some char data!', maxshape=None)
root['/entry/user/role'].attrs['type'] = 'NX_CHAR'
root['/entry/user/role'].attrs['EX_required'] = 'true'
 
root['/entry/user'].create_dataset(name='facility_user_id', data='!some char data!', maxshape=None)
root['/entry/user/facility_user_id'].attrs['type'] = 'NX_CHAR'
root['/entry/user/facility_user_id'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/untitled_source']['type'] are: 
#	 Spallation Neutron Source
#	 Pulsed Reactor Neutron Source
#	 Reactor Neutron Source
#	 Synchrotron X-Ray Source
#	 Pulsed Muon Source
#	 Rotating Anode X-Ray
#	 Fixed Tube X-Ray
 
root['/entry/instrument/untitled_source'].create_dataset(name='type', data='Spallation Neutron Source', maxshape=None)
root['/entry/instrument/untitled_source/type'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/untitled_source/type'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/untitled_source'].create_dataset(name='name', data='!some char data!', maxshape=None)
root['/entry/instrument/untitled_source/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/untitled_source/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/untitled_source']['probe'] are: 
#	 neutron
#	 x-ray
#	 electron
 
root['/entry/instrument/untitled_source'].create_dataset(name='probe', data='neutron', maxshape=None)
root['/entry/instrument/untitled_source/probe'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/untitled_source/probe'].attrs['EX_required'] = 'true'
 
root['/entry/instrument'].create_dataset(name='name', data='!some char data!', maxshape=None)
root['/entry/instrument/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/name'].attrs['EX_required'] = 'true'
 
root['/entry/instrument'].create_dataset(name='description', data='!some char data!', maxshape=None)
root['/entry/instrument/description'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/description'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='name', data='!some char data!', maxshape=None)
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='sample_id', data='!some char data!', maxshape=None)
root['/entry/sample/sample_id'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/sample_id'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='description', data='!some char data!', maxshape=None)
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
 
root['/entry/sample'].create_dataset(name='type', data='sample', maxshape=None)
root['/entry/sample/type'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/type'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='chemical_formula', data='!some char data!', maxshape=None)
root['/entry/sample/chemical_formula'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/chemical_formula'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='preparation_date', data='!some char data!', maxshape=None)
root['/entry/sample/preparation_date'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/preparation_date'].attrs['EX_required'] = 'true'
root['/entry/sample/preparation_date'].attrs['units'] = 'NX_TIME'
 
root['/entry/sample'].create_dataset(name='situation', data='!some char data!', maxshape=None)
root['/entry/sample/situation'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/situation'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='temperature', data=1.0, maxshape=None)
root['/entry/sample/temperature'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/temperature'].attrs['EX_required'] = 'true'
root['/entry/sample/temperature'].attrs['units'] = 'NX_TEMPERATURE'
 
root['/entry/sample'].create_dataset(name='magnetic_field', data=1.0, maxshape=None)
root['/entry/sample/magnetic_field'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/magnetic_field'].attrs['EX_required'] = 'true'
root['/entry/sample/magnetic_field'].attrs['units'] = 'NX_CURRENT'
 
root['/entry/sample'].create_dataset(name='electric_field', data=1.0, maxshape=None)
root['/entry/sample/electric_field'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/electric_field'].attrs['EX_required'] = 'true'
root['/entry/sample/electric_field'].attrs['units'] = 'NX_VOLTAGE'
 
root['/entry/sample'].create_dataset(name='stress_field', data=1.0, maxshape=None)
root['/entry/sample/stress_field'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/stress_field'].attrs['EX_required'] = 'true'
root['/entry/sample/stress_field'].attrs['units'] = 'NX_UNITLESS'
 
root['/entry/sample'].create_dataset(name='pressure', data=1.0, maxshape=None)
root['/entry/sample/pressure'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/pressure'].attrs['EX_required'] = 'true'
root['/entry/sample/pressure'].attrs['units'] = 'NX_PRESSURE'
root['/entry/experiment_identifier'].attrs['EX_doc'] = '     unique identifier for the experiment    '
root['/entry/experiment_description'].attrs['EX_doc'] = '     Brief description of the experiment and its objectives    '
root['/entry/collection_identifier'].attrs['EX_doc'] = '     ID of user or DAQ define group of data files    '
root['/entry/collection_description'].attrs['EX_doc'] = '     Brief summary of the collection, including grouping criteria    '
root['/entry/entry_identifier'].attrs['EX_doc'] = '     unique identifier for this measurement as provided by the facility    '
root['/entry/duration'].attrs['EX_doc'] = '     TODO: needs documentation    '
root['/entry/collection_time'].attrs['EX_doc'] = '     TODO: needs documentation    '
root['/entry/run_cycle'].attrs['EX_doc'] = '     TODO: needs documentation    '
root['/entry/revision'].attrs['EX_doc'] = '     revision ID of this file, may be after recalibration, reprocessing etc.    '
root['/entry/definition'].attrs['EX_doc'] = '     Official NeXus NXDL schema to which this file conforms    '
root['/entry/program'].attrs['EX_doc'] = '     The program and version used for generating this file    '
root['/entry/release_date'].attrs['EX_doc'] = '     when this file is to be released into PD    '
root['/entry/user/role'].attrs['EX_doc'] = '      role of the user     '
root['/entry/user/facility_user_id'].attrs['EX_doc'] = '      ID of the user in the facility burocracy database     '
root['/entry/instrument/description'].attrs['EX_doc'] = '      Brief description of the instrument     '
root['/entry/sample/name'].attrs['EX_doc'] = '      Descriptive name of sample     '
root['/entry/sample/sample_id'].attrs['EX_doc'] = '      Unique database id of the sample     '
root['/entry/sample/chemical_formula'].attrs['EX_doc'] = '      Chemical formula formatted according to CIF conventions     '
root['/entry/sample/situation'].attrs['EX_doc'] = '      Description of the environment the sample is in:             air, vacuum, oxidizing atmosphere, dehydrated, etc.     '
root['/entry'].attrs['index'] = '!some char data!'
root['/entry/program'].attrs['version'] = '!some char data!'
root['/'].attrs['default'] = 'entry'
root.attrs['file_name'] = os.path.abspath('NXarchive')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.close()


