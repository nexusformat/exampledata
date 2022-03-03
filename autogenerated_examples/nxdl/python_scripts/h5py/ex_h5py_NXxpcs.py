 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('NXxpcs.h5', 'w')

# Create the GROUPS 
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('data')
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('twotime')
root['/entry/twotime'].attrs['NX_class'] = 'NXdata'
root['/entry/twotime'].attrs['EX_required'] = 'false'
 
root['/entry/'].create_group('instrument')
root['/entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/instrument'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('incident_beam')
root['/entry/instrument/incident_beam'].attrs['NX_class'] = 'NXbeam'
root['/entry/instrument/incident_beam'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('detector')
root['/entry/instrument/detector'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/detector'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/'].create_group('masks')
root['/entry/instrument/masks'].attrs['NX_class'] = 'NXnote'
root['/entry/instrument/masks'].attrs['EX_required'] = 'false'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'false'
 
root['/entry/sample/'].create_group('position_x')
root['/entry/sample/position_x'].attrs['NX_class'] = 'NXpositioner'
root['/entry/sample/position_x'].attrs['EX_required'] = 'false'
 
root['/entry/sample/'].create_group('position_y')
root['/entry/sample/position_y'].attrs['NX_class'] = 'NXpositioner'
root['/entry/sample/position_y'].attrs['EX_required'] = 'false'
 
root['/entry/sample/'].create_group('position_z')
root['/entry/sample/position_z'].attrs['NX_class'] = 'NXpositioner'
root['/entry/sample/position_z'].attrs['EX_required'] = 'false'
 
root['/entry/'].create_group('ROI')
root['/entry/ROI'].attrs['NX_class'] = 'NXnote'
root['/entry/ROI'].attrs['EX_required'] = 'false'
 
root['/entry/'].create_group('NOTE')
root['/entry/NOTE'].attrs['NX_class'] = 'NXnote'
root['/entry/NOTE'].attrs['EX_required'] = 'false'

# Create the FIELDS 
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXxpcs
 
root['/entry'].create_dataset(name='definition', data='NXxpcs', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='entry_identifier', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/entry_identifier'].attrs['type'] = 'NX_CHAR'
root['/entry/entry_identifier'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='entry_identifier_uuid', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/entry_identifier_uuid'].attrs['type'] = 'NX_CHAR'
root['/entry/entry_identifier_uuid'].attrs['EX_required'] = 'false'
 
root['/entry'].create_dataset(name='scan_number', data=1, maxshape=None)
root['/entry/scan_number'].attrs['type'] = 'NX_INT'
root['/entry/scan_number'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='start_time', data='2022-03-03T14:34:24.295042', maxshape=None)
root['/entry/start_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/start_time'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='end_time', data='2022-03-03T14:34:24.295042', maxshape=None)
root['/entry/end_time'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/end_time'].attrs['EX_required'] = 'false'
 
root['/entry/data'].create_dataset(name='frame_sum', data=1.0, maxshape=None)
root['/entry/data/frame_sum'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/frame_sum'].attrs['EX_required'] = 'false'
root['/entry/data/frame_sum'].attrs['units'] = 'NX_COUNT'
 
root['/entry/data'].create_dataset(name='frame_average', data=1.0, maxshape=None)
root['/entry/data/frame_average'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/frame_average'].attrs['EX_required'] = 'false'
root['/entry/data/frame_average'].attrs['units'] = 'NX_COUNT'
 
root['/entry/data'].create_dataset(name='g2', data=1.0, maxshape=None)
root['/entry/data/g2'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/g2'].attrs['EX_required'] = 'false'
root['/entry/data/g2'].attrs['units'] = 'NX_ARBITRARY_UNITS'
 
root['/entry/data'].create_dataset(name='g2_derr', data=1.0, maxshape=None)
root['/entry/data/g2_derr'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/g2_derr'].attrs['EX_required'] = 'false'
root['/entry/data/g2_derr'].attrs['units'] = 'NX_ARBITRARY_UNITS'
 
root['/entry/data'].create_dataset(name='G2_unnormalized', data=1.0, maxshape=None)
root['/entry/data/G2_unnormalized'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/G2_unnormalized'].attrs['EX_required'] = 'false'
root['/entry/data/G2_unnormalized'].attrs['units'] = 'NX_ARBITRARY_UNITS'
 
root['/entry/data'].create_dataset(name='delay_difference', data=1, maxshape=None)
root['/entry/data/delay_difference'].attrs['type'] = 'NX_INT'
root['/entry/data/delay_difference'].attrs['EX_required'] = 'false'
root['/entry/data/delay_difference'].attrs['units'] = 'NX_INT'
 
root['/entry/twotime'].create_dataset(name='two_time_corr_func', data=1.0, maxshape=None)
root['/entry/twotime/two_time_corr_func'].attrs['type'] = 'NX_NUMBER'
root['/entry/twotime/two_time_corr_func'].attrs['EX_required'] = 'false'
root['/entry/twotime/two_time_corr_func'].attrs['units'] = 'NX_ANY'
 
root['/entry/twotime'].create_dataset(name='g2_from_two_time_corr_func', data=1.0, maxshape=None)
root['/entry/twotime/g2_from_two_time_corr_func'].attrs['type'] = 'NX_NUMBER'
root['/entry/twotime/g2_from_two_time_corr_func'].attrs['EX_required'] = 'false'
root['/entry/twotime/g2_from_two_time_corr_func'].attrs['units'] = 'NX_ARBITRARY_UNITS'
 
root['/entry/twotime'].create_dataset(name='g2_err_from_two_time_corr_func', data=1.0, maxshape=None)
root['/entry/twotime/g2_err_from_two_time_corr_func'].attrs['type'] = 'NX_NUMBER'
root['/entry/twotime/g2_err_from_two_time_corr_func'].attrs['EX_required'] = 'false'
root['/entry/twotime/g2_err_from_two_time_corr_func'].attrs['units'] = 'NX_ARBITRARY_UNITS'
 
root['/entry/twotime'].create_dataset(name='g2_from_two_time_corr_func_partials', data=1.0, maxshape=None)
root['/entry/twotime/g2_from_two_time_corr_func_partials'].attrs['type'] = 'NX_NUMBER'
root['/entry/twotime/g2_from_two_time_corr_func_partials'].attrs['EX_required'] = 'false'
root['/entry/twotime/g2_from_two_time_corr_func_partials'].attrs['units'] = 'NX_ARBITRARY_UNITS'
 
root['/entry/twotime'].create_dataset(name='g2_err_from_two_time_corr_func_partials', data=1.0, maxshape=None)
root['/entry/twotime/g2_err_from_two_time_corr_func_partials'].attrs['type'] = 'NX_NUMBER'
root['/entry/twotime/g2_err_from_two_time_corr_func_partials'].attrs['EX_required'] = 'false'
root['/entry/twotime/g2_err_from_two_time_corr_func_partials'].attrs['units'] = 'NX_ARBITRARY_UNITS'
 
root['/entry/instrument/incident_beam'].create_dataset(name='incident_energy', data=1.0, maxshape=None)
root['/entry/instrument/incident_beam/incident_energy'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/incident_beam/incident_energy'].attrs['EX_required'] = 'true'
root['/entry/instrument/incident_beam/incident_energy'].attrs['units'] = 'NX_ENERGY'
 
root['/entry/instrument/incident_beam'].create_dataset(name='incident_energy_spread', data=1.0, maxshape=None)
root['/entry/instrument/incident_beam/incident_energy_spread'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/incident_beam/incident_energy_spread'].attrs['EX_required'] = 'false'
root['/entry/instrument/incident_beam/incident_energy_spread'].attrs['units'] = 'NX_ENERGY'
 
root['/entry/instrument/incident_beam'].create_dataset(name='incident_polarization_type', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/incident_beam/incident_polarization_type'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/incident_beam/incident_polarization_type'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/incident_beam'].create_dataset(name='extent', data=1.0, maxshape=None)
root['/entry/instrument/incident_beam/extent'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/incident_beam/extent'].attrs['EX_required'] = 'false'
root['/entry/instrument/incident_beam/extent'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='description', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/detector/description'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/detector/description'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/detector'].create_dataset(name='distance', data=1.0, maxshape=None)
root['/entry/instrument/detector/distance'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/distance'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='count_time', data=1.0, maxshape=None)
root['/entry/instrument/detector/count_time'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/count_time'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/count_time'].attrs['units'] = 'NX_TIME'
 
root['/entry/instrument/detector'].create_dataset(name='frame_time', data=1.0, maxshape=None)
root['/entry/instrument/detector/frame_time'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/frame_time'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/frame_time'].attrs['units'] = 'NX_TIME'
 
root['/entry/instrument/detector'].create_dataset(name='beam_center_x', data=1.0, maxshape=None)
root['/entry/instrument/detector/beam_center_x'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/beam_center_x'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/beam_center_x'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='beam_center_y', data=1.0, maxshape=None)
root['/entry/instrument/detector/beam_center_y'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/beam_center_y'].attrs['EX_required'] = 'true'
root['/entry/instrument/detector/beam_center_y'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='x_pixel_size', data=1.0, maxshape=None)
root['/entry/instrument/detector/x_pixel_size'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/x_pixel_size'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/x_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='y_pixel_size', data=1.0, maxshape=None)
root['/entry/instrument/detector/y_pixel_size'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/y_pixel_size'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/y_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/masks'].create_dataset(name='dynamic_roi_map', data=1, maxshape=None)
root['/entry/instrument/masks/dynamic_roi_map'].attrs['type'] = 'NX_DIMENSIONLESS'
root['/entry/instrument/masks/dynamic_roi_map'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/masks'].create_dataset(name='dynamic_q_list', data=1.0, maxshape=None)
root['/entry/instrument/masks/dynamic_q_list'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/masks/dynamic_q_list'].attrs['EX_required'] = 'false'
root['/entry/instrument/masks/dynamic_q_list'].attrs['units'] = 'NX_PER_LENGTH'
 
root['/entry/instrument/masks'].create_dataset(name='dynamic_phi_list', data=1.0, maxshape=None)
root['/entry/instrument/masks/dynamic_phi_list'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/masks/dynamic_phi_list'].attrs['EX_required'] = 'false'
root['/entry/instrument/masks/dynamic_phi_list'].attrs['units'] = 'NX_PER_LENGTH'
 
root['/entry/instrument/masks'].create_dataset(name='static_roi_map', data=1, maxshape=None)
root['/entry/instrument/masks/static_roi_map'].attrs['type'] = 'NX_DIMENSIONLESS'
root['/entry/instrument/masks/static_roi_map'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/masks'].create_dataset(name='static_q_list', data=1.0, maxshape=None)
root['/entry/instrument/masks/static_q_list'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/masks/static_q_list'].attrs['EX_required'] = 'false'
root['/entry/instrument/masks/static_q_list'].attrs['units'] = 'NX_PER_LENGTH'
 
root['/entry/sample'].create_dataset(name='temperature_set', data=1.0, maxshape=None)
root['/entry/sample/temperature_set'].attrs['type'] = 'NX_NUMBER'
root['/entry/sample/temperature_set'].attrs['EX_required'] = 'false'
root['/entry/sample/temperature_set'].attrs['units'] = 'NX_TEMPERATURE'
 
root['/entry/sample'].create_dataset(name='temperature', data=1.0, maxshape=None)
root['/entry/sample/temperature'].attrs['type'] = 'NX_NUMBER'
root['/entry/sample/temperature'].attrs['EX_required'] = 'false'
root['/entry/sample/temperature'].attrs['units'] = 'NX_TEMPERATURE'

# Create the DOC strings 
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this file conforms '
root['/entry/entry_identifier'].attrs['EX_doc'] = 'Unique identifier for the experiment. '
root['/entry/entry_identifier_uuid'].attrs['EX_doc'] = '(optional) UUID identifier for this entry. '
root['/entry/scan_number'].attrs['EX_doc'] = 'Scan number (must be an integer). NOTE: Link to collection_identifier. '
root['/entry/start_time'].attrs['EX_doc'] = 'Starting time of experiment, such as "2021-02-11 11:22:33.445566Z". '
root['/entry/end_time'].attrs['EX_doc'] = 'Ending time of experiment, such as "2021-02-11 11:23:45Z". '
root['/entry/data'].attrs['EX_doc'] = 'The results data captured here are most commonly required for high throughput, equilibrium dynamics experiments. Data (results) describing on-equilibrium dynamics consume more memory resources so these data are separated. '
root['/entry/data/frame_sum'].attrs['EX_doc'] = 'Two-dimensional summation along the frames stack. sum of intensity v. time (in the units of "frames") '
root['/entry/data/frame_average'].attrs['EX_doc'] = 'Two-dimensional average along the frames stack. average intensity v. time (in the units of "frames") '
root['/entry/data/g2'].attrs['EX_doc'] = 'NXdata.html#nxdata '
root['/entry/data/g2_derr'].attrs['EX_doc'] = 'error values for the :math:`g_2` values. The derivation of the error is left up to the implemented code. Symmetric error will be expected (:math:`\pm` error). The data should be in the same format as ``g2``. '
root['/entry/data/G2_unnormalized'].attrs['EX_doc'] = 'unnormalized intensity auto-correlation function. Specifically, ``g2`` without the denominator. The data should be in the same format as ``g2``. '
root['/entry/data/delay_difference'].attrs['EX_doc'] = 'delay_difference (also known as delay or lag step) This is quantized difference so that the "step" between two consecutive frames is one frame (or step ``= dt = 1 frame``) It is the "quantized" delay time corresponding to the ``g2`` values. The unit of delay_differences is ``NX_INT`` for units of frames (i.e., integers) preferred, refer to :ref:`NXdetector` for conversion to time units. '
root['/entry/twotime'].attrs['EX_doc'] = 'The data (results) in this section are based on the two-time intensity correlation function derived from a time series of scattering images. '
root['/entry/twotime/two_time_corr_func'].attrs['EX_doc'] = 'two-time correlation of speckle intensity for a given q-bin or roi (represented by the nth roi_map value) See Fluerasu, Phys Rev E (2007), Eq 1 and Sutton, Optics Express (2003) for an early description applied to X-ray scattering: .. math:: C(\boldsymbol Q, t_1, t_2) = \frac{ \langle I(\boldsymbol Q, t_1)I(\boldsymbol Q, t_2)\rangle }{ \langle I(\boldsymbol Q,t_1)\rangle \langle I(\boldsymbol Q,t_2)\rangle } in which time is quantized by frames. In principle, any data format is acceptable if the data and its axes are self-describing as per NeXus recommendations. However, the data is preferred in one of the following two formats: * iterable list of linked files (or keys) for each q-bin called by the nth roi_map value. data for each bin is a 2D array * 3D array with shape (frames, frames, q) or (q, frames, frames), where :math:`q` is represented by the nth roi_map value, not the value `q` value The computation of this result can be customized. These customizations can affect subsequently derived results (below). The following attributes will be used to manage the customization. * Other normalization methods may be applied, but the method will not be specified in this definition. Some of these normalization methods result in a baseline value of ``0``, not ``1``. * The various software libraries use different programming languages. Therefore, we need to specify the ``time = 0`` origin location of the 2D array for each :math:`q`. * A method to reduce data storage needs is to only record half of the 2D array by populating array elements above or below the array diagonal. '
root['/entry/twotime/g2_from_two_time_corr_func'].attrs['EX_doc'] = 'g2" * iterable list of linked files for each :math:`g_2` with 1 file per :math:`q` * 2D array with shape (:math:`g_2`, :math:`q`) Note that delay_difference is not included here because it is derived from the shape of extracted :math:`g_2` because all frames are considered, which is not necessarily the case for :math:`g_2`. The computation of this result can be customized. The customization can affect the fitting required to extract quantitative results. The following attributes will be used to manage the customization. '
root['/entry/twotime/g2_err_from_two_time_corr_func'].attrs['EX_doc'] = 'error values for the :math:`g_2` values. The derivation of the error is left up to the implemented code. Symmetric error will be expected (:math:`\pm` error). '
root['/entry/twotime/g2_from_two_time_corr_func_partials'].attrs['EX_doc'] = 'subset of frame weighted average along the diagonal direction in ``two_time_corr_func`` Time slicing along the diagonal can be very sophisticated. This entry currently assumes equal frame-binning. The data formats are highly dependent on the implantation of various analysis libraries. In principle, any data format is acceptable if the data and its axes are self describing as per NeXus recommendations. However, the data is preferred in one of the following two formats: * iterable list of linked files (or keys) for each partial :math:`g_2` of each q-bin represented by the roi_map value * 3D array with shape (:math:`g_2`, :math:`q`, nth_partial) Note that delay_difference is not included here because it is derived from the shape of extracted :math:`g_2`. '
root['/entry/twotime/g2_err_from_two_time_corr_func_partials'].attrs['EX_doc'] = 'error values for the :math:`g_2` values. The derivation of the error is left up to the implemented code. Symmetric error will be expected (:math:`\pm` error). '
root['/entry/instrument'].attrs['EX_doc'] = 'instrument``). '
root['/entry/instrument/incident_beam/incident_energy'].attrs['EX_doc'] = 'Incident beam line energy (either keV or eV). '
root['/entry/instrument/incident_beam/incident_energy_spread'].attrs['EX_doc'] = 'Spread of incident beam line energy (either keV or eV). This quantity is otherwise known as the energy resolution, which is related to the longitudinal coherence length. '
root['/entry/instrument/incident_beam/incident_polarization_type'].attrs['EX_doc'] = 'Terse description of the incident beam polarization. The value can be plain text, such as ``vertical``, ``C+``, ``circular left``. '
root['/entry/instrument/incident_beam/extent'].attrs['EX_doc'] = 'Size (2-D) of the beam at this position. '
root['/entry/instrument/detector'].attrs['EX_doc'] = 'cxi.html '
root['/entry/instrument/detector/description'].attrs['EX_doc'] = 'Detector name. '
root['/entry/instrument/detector/distance'].attrs['EX_doc'] = 'Distance between sample and detector. '
root['/entry/instrument/detector/count_time'].attrs['EX_doc'] = 'Exposure time of frames, s. '
root['/entry/instrument/detector/frame_time'].attrs['EX_doc'] = 'Exposure period (time between frame starts) of frames, s '
root['/entry/instrument/detector/beam_center_x'].attrs['EX_doc'] = 'Position of beam center, x axis, in detector"s coordinates. '
root['/entry/instrument/detector/beam_center_y'].attrs['EX_doc'] = 'Position of beam center, y axis, in detector"s coordinates. '
root['/entry/instrument/detector/x_pixel_size'].attrs['EX_doc'] = 'Length of pixel in x direction. '
root['/entry/instrument/detector/y_pixel_size'].attrs['EX_doc'] = 'Length of pixel in y direction. '
root['/entry/instrument/masks'].attrs['EX_doc'] = 'two_time. "Static" refers to finer binning used for computation not strictly used for the final XPCS results. Implementation of _static_ binning is left for individual libraries to document. We encourage usage of :ref:`NXcanSAS` to represent standard SAXS results or development of new NeXus definitions for GI-SAXS or other reciprocal space intensity mapping. '
root['/entry/instrument/masks/dynamic_roi_map'].attrs['EX_doc'] = 'roi index array or labeled array The values of this mask index (or map to) the :math:`Q` value from the the ``dynamic_q_list`` field. Not that the value of ``0`` represents in-action. XPCS computations are performed on all pixels with a value > 0. The ``units`` attribute should be set to ``"au"`` indicating arbitrary units. '
root['/entry/instrument/masks/dynamic_q_list'].attrs['EX_doc'] = 'O is required by end user. The lists can be accessed as lists, arrays or via keys '
root['/entry/instrument/masks/dynamic_phi_list'].attrs['EX_doc'] = 'Array of :math:`\varphi` value for each pixel. List order is determined by the index value of the associated roi map starting at ``1``. '
root['/entry/instrument/masks/static_roi_map'].attrs['EX_doc'] = 'roi index array. The values of this mask index the :math:`|Q|` value from the the ``static_q_list`` field. The ``units`` attribute should be set to ``"au"`` indicating arbitrary units. '
root['/entry/instrument/masks/static_q_list'].attrs['EX_doc'] = '1-D list of :math:`|Q|` values, 1 for each roi. '
root['/entry/sample/temperature_set'].attrs['EX_doc'] = 'Sample temperature setpoint, (C or K). '
root['/entry/sample/temperature'].attrs['EX_doc'] = 'Sample temperature actual, (C or K). '
root['/entry/ROI'].attrs['EX_doc'] = '**THIS FIELD IS SCHEDULED FOR DELETION on or about March 1, 2022.** Contact abarbour@bnl.gov or jemian@anl.gov to object. Region(s) of interest. NAME: The NeXus convention, to use all upper case to indicate the name (here ``roi``), is left to the file writer. In our case, follow the suggested name pattern and sequence: roi_1, roi_2, roi_3, ... Start with ``roi_1`` if the first one, otherwise pick the next number in this sequence. '
root['/entry/NOTE'].attrs['EX_doc'] = 'Any other notes. NAME: The NeXus convention, to use all upper case to indicate the name (here ``NOTE``), is left to the file writer. In our case, follow the suggested name pattern and sequence: note_1, note_2, note_3, ... Start with ``note_1`` if the first one, otherwise pick the next number in this sequence. '
 

# Create the ATTRIBUTES 
root['/entry/data/g2'].attrs['storage_mode'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/g2_derr'].attrs['storage_mode'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/G2_unnormalized'].attrs['storage_mode'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/delay_difference'].attrs['storage_mode'] = 'SAMPLE-CHAR-DATA'
root['/entry/twotime/two_time_corr_func'].attrs['storage_mode'] = 'SAMPLE-CHAR-DATA'
root['/entry/twotime/two_time_corr_func'].attrs['baseline_reference'] = '1'
root['/entry/twotime/two_time_corr_func'].attrs['time_origin_location'] = 'SAMPLE-CHAR-DATA'
root['/entry/twotime/two_time_corr_func'].attrs['populated_elements'] = 'SAMPLE-CHAR-DATA'
root['/entry/twotime/g2_from_two_time_corr_func'].attrs['storage_mode'] = 'SAMPLE-CHAR-DATA'
root['/entry/twotime/g2_from_two_time_corr_func'].attrs['baseline_reference'] = '1'
root['/entry/twotime/g2_from_two_time_corr_func'].attrs['first_point_for_fit'] = '1'
root['/entry/twotime/g2_err_from_two_time_corr_func'].attrs['storage_mode'] = 'SAMPLE-CHAR-DATA'
root['/entry/twotime/g2_from_two_time_corr_func_partials'].attrs['storage_mode'] = 'SAMPLE-CHAR-DATA'
root['/entry/twotime/g2_from_two_time_corr_func_partials'].attrs['baseline_reference'] = '1'
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'data'
root['/entry/data'].attrs['signal'] = 'G2_unnormalized'
root['/entry/data/G2_unnormalized'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXxpcs')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version

# Close the file
root.close()

