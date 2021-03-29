from nexusformat.nexus import *
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = NXroot()
root['/entry'] = NXentry()
root['/entry'].attrs['EX_required'] = 'true'
root['/entry/instrument'] = NXinstrument()
root['/entry/instrument'].attrs['EX_required'] = 'true'
root['/entry/instrument/source'] = NXsource()
root['/entry/instrument/source'].attrs['EX_required'] = 'true'
root['/entry/instrument/crystal'] = NXcrystal()
root['/entry/instrument/crystal'].attrs['EX_required'] = 'true'
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
 
root['/entry/start_time'] = NXfield('2021-03-29T13:50:52.538248')
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXmonopd
 
root['/entry/definition'] = NXfield('NXmonopd')
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
 
root['/entry/instrument/crystal/wavelength'] = NXfield(1.0)
root['/entry/instrument/crystal/wavelength'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/crystal/wavelength'].attrs['EX_required'] = 'true'
root['/entry/instrument/crystal/wavelength'].attrs['units'] = 'NX_WAVELENGTH'
 
root['/entry/instrument/detector/polar_angle'] = NXfield(1.0)
root['/entry/instrument/detector/polar_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/polar_angle'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/polar_angle'].attrs['axis'] = '1'
 
root['/entry/instrument/detector/data'] = NXfield(1)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/data'].attrs['signal'] = '1'
 
root['/entry/sample/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample/rotation_angle'] = NXfield(1.0)
root['/entry/sample/rotation_angle'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/rotation_angle'].attrs['EX_required'] = 'true'
root['/entry/sample/rotation_angle'].attrs['units'] = 'NX_ANGLE'
 
# Valid enumeration values for root['/entry/monitor']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/monitor/mode'] = NXfield('monitor')
root['/entry/monitor/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/monitor/mode'].attrs['EX_required'] = 'true'
 
root['/entry/monitor/preset'] = NXfield(1.0)
root['/entry/monitor/preset'].attrs['type'] = 'NX_FLOAT'
root['/entry/monitor/preset'].attrs['EX_required'] = 'true'
 
root['/entry/monitor/integral'] = NXfield(1.0)
root['/entry/monitor/integral'].attrs['type'] = 'NX_FLOAT'
root['/entry/monitor/integral'].attrs['EX_required'] = 'true'
root['/entry/monitor/integral'].attrs['units'] = 'NX_ANY'
 
# Create the soft links 
root['/entry/data/polar_angle'] = NXlink(target='/entry/instrument/detector/polar_angle')
 
# Create the soft links 
root['/entry/data/data'] = NXlink(target='/entry/instrument/detector/data')
 
# Assign all of the doc strings
root['/entry/definition'].attrs['EX_doc'] = ' Official NeXus NXDL schema to which this file conforms '
root['/entry/instrument/crystal/wavelength'].attrs['EX_doc'] = ' Optimum diffracted wavelength '
root['/entry/instrument/detector/data'].attrs['EX_doc'] = ' detector signal (usually counts) are already corrected for detector efficiency '
root['/entry/sample/name'].attrs['EX_doc'] = ' Descriptive name of sample '
root['/entry/sample/rotation_angle'].attrs['EX_doc'] = ' Optional rotation angle for the case when the powder diagram has been obtained through an omega-2theta scan like from a traditional single detector powder diffractometer '
root['/entry/monitor/mode'].attrs['EX_doc'] = ' Count to a preset value based on either clock time (timer) or received monitor counts (monitor). '
root['/entry/monitor/preset'].attrs['EX_doc'] = ' preset value for time or monitor '
root['/entry/monitor/integral'].attrs['EX_doc'] = ' Total integral monitor counts '
root['/entry/data/polar_angle'].attrs['EX_doc'] = ' Link to polar angle in /NXentry/NXinstrument/NXdetector '
root['/entry/data/data'].attrs['EX_doc'] = ' Link to data in /NXentry/NXinstrument/NXdetector '
 
root.attrs['default'] = 'entry'
root['/entry/data'].set_default()
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'
root.save('NXmonopd.nxs', 'w')


