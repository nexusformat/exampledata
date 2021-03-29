import os
import datetime
import numpy as np
import h5py
import nexusformat
from nexusformat.nexus import *
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = NXroot()
root['/entry'] = NXentry()
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
root['/entry/instrument'] = NXinstrument()
root['/entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/instrument'].attrs['EX_required'] = 'true'
root['/entry/instrument/source'] = NXsource()
root['/entry/instrument/source'].attrs['NX_class'] = 'NXsource'
root['/entry/instrument/source'].attrs['EX_required'] = 'true'
root['/entry/instrument/monochromator'] = NXmonochromator()
root['/entry/instrument/monochromator'].attrs['NX_class'] = 'NXmonochromator'
root['/entry/instrument/monochromator'].attrs['EX_required'] = 'true'
root['/entry/instrument/incoming_beam'] = NXdetector()
root['/entry/instrument/incoming_beam'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/incoming_beam'].attrs['EX_required'] = 'true'
root['/entry/instrument/absorbed_beam'] = NXdetector()
root['/entry/instrument/absorbed_beam'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/absorbed_beam'].attrs['EX_required'] = 'true'
root['/entry/sample'] = NXsample()
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'
root['/entry/monitor'] = NXmonitor()
root['/entry/monitor'].attrs['NX_class'] = 'NXmonitor'
root['/entry/monitor'].attrs['EX_required'] = 'true'
root['/entry/data'] = NXdata()
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'
 
root['/entry/title'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry/start_time'] = NXfield('2021-03-26T13:07:58.394929')
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXxas
 
root['/entry/definition'] = NXfield('NXxas')
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source/type'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/source/type'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/type'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/source/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/instrument/source']['probe'] are: 
#	 x-ray
 
root['/entry/instrument/source/probe'] = NXfield('x-ray')
root['/entry/instrument/source/probe'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/probe'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/monochromator/energy'] = NXfield(1.0)
root['/entry/instrument/monochromator/energy'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/monochromator/energy'].attrs['EX_required'] = 'true'
root['/entry/instrument/monochromator/energy'].attrs['axis'] = '1'
 
root['/entry/instrument/incoming_beam/data'] = NXfield(1)
root['/entry/instrument/incoming_beam/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/incoming_beam/data'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/absorbed_beam/data'] = NXfield(1)
root['/entry/instrument/absorbed_beam/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/absorbed_beam/data'].attrs['EX_required'] = 'true'
 
root['/entry/sample/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry/monitor']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/monitor/mode'] = NXfield('monitor')
root['/entry/monitor/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/monitor/mode'].attrs['EX_required'] = 'true'
 
root['/entry/monitor/preset'] = NXfield(1.0)
root['/entry/monitor/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/monitor/preset'].attrs['EX_required'] = 'true'
 
root['/entry/monitor/data'] = NXfield(1)
root['/entry/monitor/data'].attrs['type'] = 'NX_INT'
root['/entry/monitor/data'].attrs['EX_required'] = 'true'
 
root['/entry/data/energy'] = NXlink(target='/entry/instrument/monochromator/energy')
 
root['/entry/data/absorbed_beam'] = NXlink(target='/entry/instrument/absorbed_beam/data')
 
root['/entry'].attrs['entry'] = 'SAMPLE-CHAR-DATA'
root.attrs['default'] = 'entry'
root['/entry/data'].set_default()
root['/entry/data'].attrs['signal'] = 'absorbed_beam'
root['/entry/data/absorbed_beam'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXxas')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['nexusformat_version'] = nexusformat.__version__
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.save('nexusformat_NXxas.h5', 'w')


