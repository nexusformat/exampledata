 
import numpy as np
from nexusformat.nexus import *
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = NXroot()

# Create the GROUPS 
root['/entry_1'] = NXentry()
root['/entry_1'].attrs['EX_required'] = 'false'
root['/entry_1/instrument_1'] = NXinstrument()
root['/entry_1/instrument_1'].attrs['EX_required'] = 'true'
root['/entry_1/instrument_1/source_1'] = NXsource()
root['/entry_1/instrument_1/source_1'].attrs['EX_required'] = 'true'
root['/entry_1/instrument_1/beam_1'] = NXbeam()
root['/entry_1/instrument_1/beam_1'].attrs['EX_required'] = 'true'
root['/entry_1/instrument_1/detector_1'] = NXdetector()
root['/entry_1/instrument_1/detector_1'].attrs['EX_required'] = 'true'
root['/entry_1/instrument_1/detector_1/transformations'] = NXtransformations()
root['/entry_1/instrument_1/detector_1/transformations'].attrs['EX_required'] = 'false'
root['/entry_1/instrument_1/monitor'] = NXmonitor()
root['/entry_1/instrument_1/monitor'].attrs['EX_required'] = 'false'

# Create the FIELDS 
 
root['/entry_1/title'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry_1/title'].attrs['type'] = 'NX_CHAR'
root['/entry_1/title'].attrs['EX_required'] = 'false'
 
root['/entry_1/start_time'] = NXfield('2022-03-04T14:56:23.795988')
root['/entry_1/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry_1/start_time'].attrs['EX_required'] = 'false'
 
root['/entry_1/end_time'] = NXfield('2022-03-04T14:56:23.795988')
root['/entry_1/end_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry_1/end_time'].attrs['EX_required'] = 'false'
 
# Valid enumeration values for root['/entry_1']['definition'] are: 
#	 NXcxi_ptycho
 
root['/entry_1/definition'] = NXfield('NXcxi_ptycho')
root['/entry_1/definition'].attrs['type'] = 'NX_CHAR'
root['/entry_1/definition'].attrs['EX_required'] = 'true'
 
root['/entry_1/instrument_1/source_1/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry_1/instrument_1/source_1/name'].attrs['type'] = 'NX_CHAR'
root['/entry_1/instrument_1/source_1/name'].attrs['EX_required'] = 'true'
 
root['/entry_1/instrument_1/source_1/energy'] = NXfield(1.0)
root['/entry_1/instrument_1/source_1/energy'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/source_1/energy'].attrs['EX_required'] = 'true'
 
root['/entry_1/instrument_1/source_1/probe'] = NXfield(1.0)
root['/entry_1/instrument_1/source_1/probe'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/source_1/probe'].attrs['EX_required'] = 'true'
 
root['/entry_1/instrument_1/source_1/type'] = NXfield(1.0)
root['/entry_1/instrument_1/source_1/type'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/source_1/type'].attrs['EX_required'] = 'true'
 
root['/entry_1/instrument_1/beam_1/energy'] = NXfield(1.0)
root['/entry_1/instrument_1/beam_1/energy'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/beam_1/energy'].attrs['EX_required'] = 'true'
 
root['/entry_1/instrument_1/beam_1/extent'] = NXfield(1.0)
root['/entry_1/instrument_1/beam_1/extent'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/beam_1/extent'].attrs['EX_required'] = 'false'
 
root['/entry_1/instrument_1/beam_1/incident_beam_divergence'] = NXfield(1.0)
root['/entry_1/instrument_1/beam_1/incident_beam_divergence'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/beam_1/incident_beam_divergence'].attrs['EX_required'] = 'false'
 
root['/entry_1/instrument_1/beam_1/incident_beam_energy'] = NXfield(1.0)
root['/entry_1/instrument_1/beam_1/incident_beam_energy'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/beam_1/incident_beam_energy'].attrs['EX_required'] = 'true'
 
root['/entry_1/instrument_1/beam_1/incident_energy_spread'] = NXfield(1.0)
root['/entry_1/instrument_1/beam_1/incident_energy_spread'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/beam_1/incident_energy_spread'].attrs['EX_required'] = 'true'
 
root['/entry_1/instrument_1/detector_1/transformations/vector'] = NXfield(1.0)
root['/entry_1/instrument_1/detector_1/transformations/vector'].attrs['type'] = 'NX_NUMBER'
root['/entry_1/instrument_1/detector_1/transformations/vector'].attrs['EX_required'] = 'true'
 
root['/entry_1/instrument_1/detector_1/translation'] = NXfield(1.0)
root['/entry_1/instrument_1/detector_1/translation'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/detector_1/translation'].attrs['EX_required'] = 'true'
root['/entry_1/instrument_1/detector_1/translation'].attrs['units'] = 'NX_LENGTH'
 
root['/entry_1/instrument_1/detector_1/data'] = NXfield(1)
root['/entry_1/instrument_1/detector_1/data'].attrs['type'] = 'NX_INT'
root['/entry_1/instrument_1/detector_1/data'].attrs['EX_required'] = 'true'
root['/entry_1/instrument_1/detector_1/data'].attrs['signal'] = '1'
 
root['/entry_1/instrument_1/detector_1/x_pixel_size'] = NXfield(1.0)
root['/entry_1/instrument_1/detector_1/x_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/detector_1/x_pixel_size'].attrs['EX_required'] = 'true'
root['/entry_1/instrument_1/detector_1/x_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry_1/instrument_1/detector_1/y_pixel_size'] = NXfield(1.0)
root['/entry_1/instrument_1/detector_1/y_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/detector_1/y_pixel_size'].attrs['EX_required'] = 'true'
root['/entry_1/instrument_1/detector_1/y_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry_1/instrument_1/detector_1/distance'] = NXfield(1.0)
root['/entry_1/instrument_1/detector_1/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/detector_1/distance'].attrs['EX_required'] = 'true'
root['/entry_1/instrument_1/detector_1/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry_1/instrument_1/detector_1/beam_center_x'] = NXfield(1.0)
root['/entry_1/instrument_1/detector_1/beam_center_x'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/detector_1/beam_center_x'].attrs['EX_required'] = 'false'
root['/entry_1/instrument_1/detector_1/beam_center_x'].attrs['units'] = 'NX_LENGTH'
 
root['/entry_1/instrument_1/detector_1/beam_center_y'] = NXfield(1.0)
root['/entry_1/instrument_1/detector_1/beam_center_y'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/detector_1/beam_center_y'].attrs['EX_required'] = 'false'
root['/entry_1/instrument_1/detector_1/beam_center_y'].attrs['units'] = 'NX_LENGTH'
 
root['/entry_1/instrument_1/monitor/data'] = NXfield(1.0)
root['/entry_1/instrument_1/monitor/data'].attrs['type'] = 'NX_FLOAT'
root['/entry_1/instrument_1/monitor/data'].attrs['EX_required'] = 'false'

# Create the LINKS 
root['/entry_1/instrument_1/detector_1/data_1'] = NXlink(target='/entry_1/title')

# Create the DOC strings 
root['/entry_1/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms '
root['/entry_1/instrument_1/source_1/energy'].attrs['EX_doc'] = 'This is the energy of the machine, not the beamline. '
root['/entry_1/instrument_1/detector_1/translation'].attrs['EX_doc'] = 'This is an array of shape (npts_x*npts_y, 3) and can be a Virtual Dataset of x and y '
root['/entry_1/instrument_1/detector_1/data_1'].attrs['EX_doc'] = 'This data must always have shape (npts_x*npts_y, frame_size_x, frame_size_y) regardless   of the scan pattern. Use hdf5 virtual dataset to achieve this. '
root['/entry_1/instrument_1/detector_1/distance'].attrs['EX_doc'] = 'The distance between the detector and the sample '
 

# Create the ATTRIBUTES 
root['/entry_1/instrument_1/beam_1/energy'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry_1/instrument_1/beam_1/extent'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry_1/instrument_1/beam_1/incident_beam_divergence'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry_1/instrument_1/beam_1/incident_beam_energy'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry_1/instrument_1/beam_1/incident_energy_spread'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry_1/instrument_1/detector_1'].attrs['axes'] = 'SAMPLE-CHAR-DATA'
root['/entry_1/instrument_1/detector_1'].attrs['signal'] = 'SAMPLE-CHAR-DATA'
root['/entry_1/instrument_1/detector_1/translation'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry_1/instrument_1/detector_1/translation'].attrs['axes'] = 'SAMPLE-CHAR-DATA'
root['/entry_1/instrument_1/detector_1/translation'].attrs['interpretation'] = 'SAMPLE-CHAR-DATA'
root['/entry_1/instrument_1/detector_1/x_pixel_size'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry_1/instrument_1/detector_1/y_pixel_size'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry_1/instrument_1/detector_1/distance'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry_1/instrument_1/detector_1/beam_center_x'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry_1/instrument_1/detector_1/beam_center_y'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root.attrs['default'] = 'entry_1'

# Save the file
root.save('NXcxi_ptycho.nxs', 'w')


