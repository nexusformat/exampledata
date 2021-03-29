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
root['/entry/data'] = NXdata()
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'
root['/entry/sample'] = NXsample()
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'true'
root['/entry/sample/transformations'] = NXtransformations()
root['/entry/sample/transformations'].attrs['NX_class'] = 'NXtransformations'
root['/entry/sample/transformations'].attrs['EX_required'] = 'false'
root['/entry/instrument'] = NXinstrument()
root['/entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/instrument'].attrs['EX_required'] = 'true'
root['/entry/instrument/attenuator'] = NXattenuator()
root['/entry/instrument/attenuator'].attrs['NX_class'] = 'NXattenuator'
root['/entry/instrument/attenuator'].attrs['EX_required'] = 'false'
root['/entry/instrument/NXdetector_group'] = NXdetector_group()
root['/entry/instrument/NXdetector_group'].attrs['NX_class'] = 'NXdetector_group'
root['/entry/instrument/NXdetector_group'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector'] = NXdetector()
root['/entry/instrument/detector'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/transformations'] = NXtransformations()
root['/entry/instrument/detector/transformations'].attrs['NX_class'] = 'NXtransformations'
root['/entry/instrument/detector/transformations'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/collection'] = NXcollection()
root['/entry/instrument/detector/collection'].attrs['NX_class'] = 'NXcollection'
root['/entry/instrument/detector/collection'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/NXdetector_module'] = NXdetector_module()
root['/entry/instrument/detector/NXdetector_module'].attrs['NX_class'] = 'NXdetector_module'
root['/entry/instrument/detector/NXdetector_module'].attrs['EX_required'] = 'true'
root['/entry/instrument/beam'] = NXbeam()
root['/entry/instrument/beam'].attrs['NX_class'] = 'NXbeam'
root['/entry/instrument/beam'].attrs['EX_required'] = 'true'
root['/entry/instrument/beam/incident_wavelength_spectrum'] = NXdata()
root['/entry/instrument/beam/incident_wavelength_spectrum'].attrs['NX_class'] = 'NXdata'
root['/entry/instrument/beam/incident_wavelength_spectrum'].attrs['EX_required'] = 'false'
root['/entry/source'] = NXsource()
root['/entry/source'].attrs['NX_class'] = 'NXsource'
root['/entry/source'].attrs['EX_required'] = 'true'
 
root['/entry/title'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'false'
 
root['/entry/start_time'] = NXfield('2021-03-26T13:07:53.060290')
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
root['/entry/end_time'] = NXfield('2021-03-26T13:07:53.063302')
root['/entry/end_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/end_time'].attrs['EX_required'] = 'false'
 
root['/entry/end_time_estimated'] = NXfield('2021-03-26T13:07:53.066303')
root['/entry/end_time_estimated'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/end_time_estimated'].attrs['EX_required'] = 'true'
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXmx
 
root['/entry/definition'] = NXfield('NXmx')
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/data/data'] = NXfield(1.0)
root['/entry/data/data'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/data'].attrs['EX_required'] = 'true'
 
root['/entry/sample/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample/depends_on'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/sample/depends_on'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/depends_on'].attrs['EX_required'] = 'true'
 
root['/entry/sample/temperature'] = NXfield(1.0)
root['/entry/sample/temperature'].attrs['type'] = 'NX_NUMBER'
root['/entry/sample/temperature'].attrs['EX_required'] = 'false'
root['/entry/sample/temperature'].attrs['units'] = 'NX_TEMPERATURE'
 
root['/entry/instrument/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/name'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/time_zone'] = NXfield('2021-03-26T13:07:53.092283')
root['/entry/instrument/time_zone'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/instrument/time_zone'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/attenuator/attenuator_transmission'] = NXfield(1.0)
root['/entry/instrument/attenuator/attenuator_transmission'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/attenuator/attenuator_transmission'].attrs['EX_required'] = 'false'
root['/entry/instrument/attenuator/attenuator_transmission'].attrs['units'] = 'NX_UNITLESS'
 
root['/entry/instrument/NXdetector_group/group_names'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/NXdetector_group/group_names'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/NXdetector_group/group_names'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/NXdetector_group/group_index'] = NXfield(1)
root['/entry/instrument/NXdetector_group/group_index'].attrs['type'] = 'NX_INT'
root['/entry/instrument/NXdetector_group/group_index'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/NXdetector_group/group_parent'] = NXfield(1)
root['/entry/instrument/NXdetector_group/group_parent'].attrs['type'] = 'NX_INT'
root['/entry/instrument/NXdetector_group/group_parent'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector/depends_on'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/detector/depends_on'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/detector/depends_on'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector/data'] = NXfield(1.0)
root['/entry/instrument/detector/data'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/data'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector/description'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/detector/description'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/detector/description'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector/time_per_channel'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/detector/time_per_channel'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/detector/time_per_channel'].attrs['units'] = 'NX_TIME'
root['/entry/instrument/detector/time_per_channel'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector/NXdetector_module/data_origin'] = NXfield(1)
root['/entry/instrument/detector/NXdetector_module/data_origin'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/NXdetector_module/data_origin'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector/NXdetector_module/data_size'] = NXfield(1)
root['/entry/instrument/detector/NXdetector_module/data_size'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/NXdetector_module/data_size'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector/NXdetector_module/data_stride'] = NXfield(1)
root['/entry/instrument/detector/NXdetector_module/data_stride'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/NXdetector_module/data_stride'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector/NXdetector_module/module_offset'] = NXfield(1.0)
root['/entry/instrument/detector/NXdetector_module/module_offset'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/NXdetector_module/module_offset'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/NXdetector_module/module_offset'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/NXdetector_module/fast_pixel_direction'] = NXfield(1.0)
root['/entry/instrument/detector/NXdetector_module/fast_pixel_direction'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/NXdetector_module/fast_pixel_direction'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/NXdetector_module/fast_pixel_direction'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/NXdetector_module/slow_pixel_direction'] = NXfield(1.0)
root['/entry/instrument/detector/NXdetector_module/slow_pixel_direction'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/NXdetector_module/slow_pixel_direction'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/NXdetector_module/slow_pixel_direction'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/distance'] = NXfield(1.0)
root['/entry/instrument/detector/distance'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/distance'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/distance_derived'] = NXfield(np.int8(0))
root['/entry/instrument/detector/distance_derived'].attrs['type'] = 'NX_BOOLEAN'
root['/entry/instrument/detector/distance_derived'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector/dead_time'] = NXfield(1.0)
root['/entry/instrument/detector/dead_time'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/dead_time'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/dead_time'].attrs['units'] = 'NX_TIME'
 
root['/entry/instrument/detector/count_time'] = NXfield(1.0)
root['/entry/instrument/detector/count_time'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/count_time'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/count_time'].attrs['units'] = 'NX_TIME'
 
root['/entry/instrument/detector/beam_center_derived'] = NXfield(np.int8(0))
root['/entry/instrument/detector/beam_center_derived'].attrs['type'] = 'NX_BOOLEAN'
root['/entry/instrument/detector/beam_center_derived'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector/beam_center_x'] = NXfield(1.0)
root['/entry/instrument/detector/beam_center_x'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/beam_center_x'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/beam_center_x'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/beam_center_y'] = NXfield(1.0)
root['/entry/instrument/detector/beam_center_y'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/beam_center_y'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/beam_center_y'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/angular_calibration_applied'] = NXfield(np.int8(0))
root['/entry/instrument/detector/angular_calibration_applied'].attrs['type'] = 'NX_BOOLEAN'
root['/entry/instrument/detector/angular_calibration_applied'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector/angular_calibration'] = NXfield(1.0)
root['/entry/instrument/detector/angular_calibration'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/angular_calibration'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector/flatfield_applied'] = NXfield(np.int8(0))
root['/entry/instrument/detector/flatfield_applied'].attrs['type'] = 'NX_BOOLEAN'
root['/entry/instrument/detector/flatfield_applied'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector/flatfield'] = NXfield(1.0)
root['/entry/instrument/detector/flatfield'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/flatfield'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector/flatfield_error'] = NXfield(1.0)
root['/entry/instrument/detector/flatfield_error'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/flatfield_error'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector/flatfield_errors'] = NXfield(1.0)
root['/entry/instrument/detector/flatfield_errors'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/flatfield_errors'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector/pixel_mask_applied'] = NXfield(np.int8(0))
root['/entry/instrument/detector/pixel_mask_applied'].attrs['type'] = 'NX_BOOLEAN'
root['/entry/instrument/detector/pixel_mask_applied'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector/pixel_mask'] = NXfield(1)
root['/entry/instrument/detector/pixel_mask'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/pixel_mask'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector/countrate_correction_applied'] = NXfield(np.int8(0))
root['/entry/instrument/detector/countrate_correction_applied'].attrs['type'] = 'NX_BOOLEAN'
root['/entry/instrument/detector/countrate_correction_applied'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector/bit_depth_readout'] = NXfield(1)
root['/entry/instrument/detector/bit_depth_readout'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/bit_depth_readout'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector/detector_readout_time'] = NXfield(1.0)
root['/entry/instrument/detector/detector_readout_time'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/detector_readout_time'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/detector_readout_time'].attrs['units'] = 'NX_TIME'
 
root['/entry/instrument/detector/frame_time'] = NXfield(1.0)
root['/entry/instrument/detector/frame_time'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/frame_time'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/frame_time'].attrs['units'] = 'NX_TIME'
 
root['/entry/instrument/detector/gain_setting'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/detector/gain_setting'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/detector/gain_setting'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector/saturation_value'] = NXfield(1)
root['/entry/instrument/detector/saturation_value'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/saturation_value'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector/underload_value'] = NXfield(1)
root['/entry/instrument/detector/underload_value'].attrs['type'] = 'NX_INT'
root['/entry/instrument/detector/underload_value'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector/sensor_material'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/detector/sensor_material'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/detector/sensor_material'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector/sensor_thickness'] = NXfield(1.0)
root['/entry/instrument/detector/sensor_thickness'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/sensor_thickness'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/sensor_thickness'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector/threshold_energy'] = NXfield(1.0)
root['/entry/instrument/detector/threshold_energy'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/threshold_energy'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/threshold_energy'].attrs['units'] = 'NX_ENERGY'
 
root['/entry/instrument/detector/type'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/detector/type'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/detector/type'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/beam/incident_wavelength'] = NXfield(1.0)
root['/entry/instrument/beam/incident_wavelength'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/beam/incident_wavelength'].attrs['EX_required'] = 'true'
root['/entry/instrument/beam/incident_wavelength'].attrs['units'] = 'NX_WAVELENGTH'
 
root['/entry/instrument/beam/incident_wavelength_weight'] = NXfield(1.0)
root['/entry/instrument/beam/incident_wavelength_weight'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/beam/incident_wavelength_weight'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/beam/incident_wavelength_weights'] = NXfield(1.0)
root['/entry/instrument/beam/incident_wavelength_weights'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/beam/incident_wavelength_weights'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/beam/incident_wavelength_spread'] = NXfield(1.0)
root['/entry/instrument/beam/incident_wavelength_spread'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/beam/incident_wavelength_spread'].attrs['EX_required'] = 'false'
root['/entry/instrument/beam/incident_wavelength_spread'].attrs['units'] = 'NX_WAVELENGTH'
 
root['/entry/instrument/beam/flux'] = NXfield(1.0)
root['/entry/instrument/beam/flux'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/beam/flux'].attrs['EX_required'] = 'false'
root['/entry/instrument/beam/flux'].attrs['units'] = 'NX_FLUX'
 
root['/entry/instrument/beam/total_flux'] = NXfield(1.0)
root['/entry/instrument/beam/total_flux'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/beam/total_flux'].attrs['EX_required'] = 'true'
root['/entry/instrument/beam/total_flux'].attrs['units'] = 'NX_FREQUENCY'
 
root['/entry/instrument/beam/incident_beam_size'] = NXfield(1.0)
root['/entry/instrument/beam/incident_beam_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/beam/incident_beam_size'].attrs['EX_required'] = 'true'
root['/entry/instrument/beam/incident_beam_size'].attrs['units'] = 'NX_LENGTH'
 
# Valid enumeration values for root['/entry/instrument/beam']['profile'] are: 
#	 Gaussian
#	 Airy
#	 top-hat
#	 rectangular
 
root['/entry/instrument/beam/profile'] = NXfield('Gaussian')
root['/entry/instrument/beam/profile'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/beam/profile'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/beam/incident_polarisation_stokes'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/instrument/beam/incident_polarisation_stokes'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/beam/incident_polarisation_stokes'].attrs['EX_required'] = 'true'
 
root['/entry/source/name'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/source/name'].attrs['type'] = 'NX_CHAR'
root['/entry/source/name'].attrs['EX_required'] = 'true'
 
root['/entry'].attrs['version'] = 'SAMPLE-CHAR-DATA'
root['/entry/instrument/name'].attrs['short_name'] = 'SAMPLE-CHAR-DATA'
root['/entry/instrument/detector/NXdetector_module/module_offset'].attrs['transformation_type'] = 'SAMPLE-CHAR-DATA'
root['/entry/instrument/detector/NXdetector_module/module_offset'].attrs['depends_on'] = 'SAMPLE-CHAR-DATA'
root['/entry/instrument/detector/NXdetector_module/fast_pixel_direction'].attrs['transformation_type'] = 'SAMPLE-CHAR-DATA'
root['/entry/instrument/detector/NXdetector_module/fast_pixel_direction'].attrs['depends_on'] = 'SAMPLE-CHAR-DATA'
root['/entry/instrument/detector/NXdetector_module/slow_pixel_direction'].attrs['transformation_type'] = 'SAMPLE-CHAR-DATA'
root['/entry/instrument/detector/NXdetector_module/slow_pixel_direction'].attrs['depends_on'] = 'SAMPLE-CHAR-DATA'
root['/entry/source/name'].attrs['short_name'] = 'SAMPLE-CHAR-DATA'
root.attrs['default'] = 'entry'
root['/entry/data'].set_default()
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXmx')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['nexusformat_version'] = nexusformat.__version__
root.attrs['HDF5_Version'] = h5py.version.hdf5_version
root.save('nexusformat_NXmx.h5', 'w')


