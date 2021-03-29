from nexusformat.nexus import *
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = NXroot()
root['/entry'] = NXentry()
root['/entry'].attrs['EX_required'] = 'true'
root['/entry/instrument'] = NXinstrument()
root['/entry/instrument'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector'] = NXdetector()
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
root['/entry/sample'] = NXsample()
root['/entry/sample'].attrs['EX_required'] = 'true'
root['/entry/monitor'] = NXmonitor()
root['/entry/monitor'].attrs['EX_required'] = 'true'
root['/entry/data'] = NXdata()
root['/entry/data'].attrs['EX_required'] = 'true'
 
root['/entry/title'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry/start_time'] = NXfield('2021-03-29T13:50:55.693693')
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
root['/entry/end_time'] = NXfield('2021-03-29T13:50:55.695694')
root['/entry/end_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/end_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXscan
 
root['/entry/definition'] = NXfield('NXscan')
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector/data'] = NXfield(1)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/entry/sample/rotation_angle'] = NXfield(1.0)
root['/entry/sample/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/rotation_angle'].attrs['axis'] = '1'
 
root['/entry/monitor/data'] = NXfield(1)
root['/entry/monitor/data'].attrs['type'] = 'NX_INT'
root['/entry/monitor/data'].attrs['EX_required'] = 'true'
 
# Create the soft links 
root['/entry/data/data'] = NXlink(target='/entry/instrument/detector/data')
 
# Create the soft links 
root['/entry/data/rotation_angle'] = NXlink(target='/entry/sample/rotation_angle')
 
# Assign all of the doc strings
root['/entry/definition'].attrs['EX_doc'] = ' Official NeXus NXDL schema to which this file conforms '
 
root.attrs['default'] = 'entry'
root['/entry/data'].set_default()
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'
root.save('NXscan.nxs', 'w')


