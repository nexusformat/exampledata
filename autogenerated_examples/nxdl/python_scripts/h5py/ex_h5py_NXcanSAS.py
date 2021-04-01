 
import numpy as np
import datetime
import h5py
import os
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = h5py.File('NXcanSAS.h5', 'w')

# Create the GROUPS 
 
root.create_group('entry')
root['/entry'].attrs['NX_class'] = 'NXentry'
root['/entry'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('data')
root['/entry/data'].attrs['NX_class'] = 'NXdata'
root['/entry/data'].attrs['EX_required'] = 'true'
 
root['/entry/'].create_group('instrument')
root['/entry/instrument'].attrs['NX_class'] = 'NXinstrument'
root['/entry/instrument'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/'].create_group('aperture')
root['/entry/instrument/aperture'].attrs['NX_class'] = 'NXaperture'
root['/entry/instrument/aperture'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/'].create_group('collimator')
root['/entry/instrument/collimator'].attrs['NX_class'] = 'NXcollimator'
root['/entry/instrument/collimator'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/'].create_group('detector')
root['/entry/instrument/detector'].attrs['NX_class'] = 'NXdetector'
root['/entry/instrument/detector'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/'].create_group('source')
root['/entry/instrument/source'].attrs['NX_class'] = 'NXsource'
root['/entry/instrument/source'].attrs['EX_required'] = 'false'
 
root['/entry/'].create_group('sample')
root['/entry/sample'].attrs['NX_class'] = 'NXsample'
root['/entry/sample'].attrs['EX_required'] = 'false'
 
root['/entry/'].create_group('process')
root['/entry/process'].attrs['NX_class'] = 'NXprocess'
root['/entry/process'].attrs['EX_required'] = 'false'
 
root['/entry/process/'].create_group('note')
root['/entry/process/note'].attrs['NX_class'] = 'NXnote'
root['/entry/process/note'].attrs['EX_required'] = 'false'
 
root['/entry/process/'].create_group('collection')
root['/entry/process/collection'].attrs['NX_class'] = 'NXcollection'
root['/entry/process/collection'].attrs['EX_required'] = 'false'
 
root['/entry/'].create_group('collection')
root['/entry/collection'].attrs['NX_class'] = 'NXcollection'
root['/entry/collection'].attrs['EX_required'] = 'false'
 
root['/entry/'].create_group('TRANSMISSION_SPECTRUM')
root['/entry/TRANSMISSION_SPECTRUM'].attrs['NX_class'] = 'NXdata'
root['/entry/TRANSMISSION_SPECTRUM'].attrs['EX_required'] = 'false'

# Create the FIELDS 
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXcanSAS
 
root['/entry'].create_dataset(name='definition', data='NXcanSAS', maxshape=None)
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'true'
 
root['/entry/data'].create_dataset(name='Q', data=1.0, maxshape=None)
root['/entry/data/Q'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/Q'].attrs['EX_required'] = 'true'
root['/entry/data/Q'].attrs['units'] = 'NX_PER_LENGTH'
 
root['/entry/data'].create_dataset(name='I', data=1.0, maxshape=None)
root['/entry/data/I'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/I'].attrs['EX_required'] = 'true'
 
root['/entry/data'].create_dataset(name='Idev', data=1.0, maxshape=None)
root['/entry/data/Idev'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/Idev'].attrs['EX_required'] = 'false'
 
root['/entry/data'].create_dataset(name='Qdev', data=1.0, maxshape=None)
root['/entry/data/Qdev'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/Qdev'].attrs['EX_required'] = 'false'
root['/entry/data/Qdev'].attrs['units'] = 'NX_PER_LENGTH'
 
root['/entry/data'].create_dataset(name='dQw', data=1.0, maxshape=None)
root['/entry/data/dQw'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/dQw'].attrs['EX_required'] = 'false'
root['/entry/data/dQw'].attrs['units'] = 'NX_PER_LENGTH'
 
root['/entry/data'].create_dataset(name='dQl', data=1.0, maxshape=None)
root['/entry/data/dQl'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/dQl'].attrs['EX_required'] = 'false'
root['/entry/data/dQl'].attrs['units'] = 'NX_PER_LENGTH'
 
root['/entry/data'].create_dataset(name='Qmean', data=1.0, maxshape=None)
root['/entry/data/Qmean'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/Qmean'].attrs['EX_required'] = 'false'
root['/entry/data/Qmean'].attrs['units'] = 'NX_PER_LENGTH'
 
root['/entry/data'].create_dataset(name='ShadowFactor', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/data/ShadowFactor'].attrs['type'] = 'NX_CHAR'
root['/entry/data/ShadowFactor'].attrs['units'] = 'NX_DIMENSIONLESS'
root['/entry/data/ShadowFactor'].attrs['EX_required'] = 'false'
 
root['/entry'].create_dataset(name='title', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'true'
 
root['/entry'].create_dataset(name='run', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/run'].attrs['type'] = 'NX_CHAR'
root['/entry/run'].attrs['EX_required'] = 'true'
root['/entry/run'].attrs['nameType'] = 'any'
 
root['/entry/instrument/aperture'].create_dataset(name='shape', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/aperture/shape'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/aperture/shape'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/aperture'].create_dataset(name='x_gap', data=1.0, maxshape=None)
root['/entry/instrument/aperture/x_gap'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/aperture/x_gap'].attrs['EX_required'] = 'false'
root['/entry/instrument/aperture/x_gap'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/aperture'].create_dataset(name='y_gap', data=1.0, maxshape=None)
root['/entry/instrument/aperture/y_gap'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/aperture/y_gap'].attrs['EX_required'] = 'false'
root['/entry/instrument/aperture/y_gap'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/collimator'].create_dataset(name='length', data=1.0, maxshape=None)
root['/entry/instrument/collimator/length'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/collimator/length'].attrs['EX_required'] = 'false'
root['/entry/instrument/collimator/length'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/collimator'].create_dataset(name='distance', data=1.0, maxshape=None)
root['/entry/instrument/collimator/distance'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/collimator/distance'].attrs['EX_required'] = 'false'
root['/entry/instrument/collimator/distance'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/detector/name'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/detector/name'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/detector'].create_dataset(name='SDD', data=1.0, maxshape=None)
root['/entry/instrument/detector/SDD'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/SDD'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/SDD'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='slit_length', data=1.0, maxshape=None)
root['/entry/instrument/detector/slit_length'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/slit_length'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/slit_length'].attrs['units'] = 'NX_PER_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='x_position', data=1.0, maxshape=None)
root['/entry/instrument/detector/x_position'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/x_position'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/x_position'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='y_position', data=1.0, maxshape=None)
root['/entry/instrument/detector/y_position'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/y_position'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/y_position'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='roll', data=1.0, maxshape=None)
root['/entry/instrument/detector/roll'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/roll'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/roll'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector'].create_dataset(name='pitch', data=1.0, maxshape=None)
root['/entry/instrument/detector/pitch'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/pitch'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/pitch'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector'].create_dataset(name='yaw', data=1.0, maxshape=None)
root['/entry/instrument/detector/yaw'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/detector/yaw'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/yaw'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/instrument/detector'].create_dataset(name='beam_center_x', data=1.0, maxshape=None)
root['/entry/instrument/detector/beam_center_x'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/beam_center_x'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/beam_center_x'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='beam_center_y', data=1.0, maxshape=None)
root['/entry/instrument/detector/beam_center_y'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/beam_center_y'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/beam_center_y'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='x_pixel_size', data=1.0, maxshape=None)
root['/entry/instrument/detector/x_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/x_pixel_size'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/x_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/detector'].create_dataset(name='y_pixel_size', data=1.0, maxshape=None)
root['/entry/instrument/detector/y_pixel_size'].attrs['type'] = 'NX_FLOAT'
root['/entry/instrument/detector/y_pixel_size'].attrs['EX_required'] = 'false'
root['/entry/instrument/detector/y_pixel_size'].attrs['units'] = 'NX_LENGTH'
 
# Valid enumeration values for root['/entry/instrument/source']['radiation'] are: 
#	 Spallation Neutron Source
#	 Pulsed Reactor Neutron Source
#	 Reactor Neutron Source
#	 Synchrotron X-ray Source
#	 Pulsed Muon Source
#	 Rotating Anode X-ray
#	 Fixed Tube X-ray
#	 UV Laser
#	 Free-Electron Laser
#	 Optical Laser
#	 Ion Source
#	 UV Plasma Source
#	 neutron
#	 x-ray
#	 muon
#	 electron
#	 ultraviolet
#	 visible light
#	 positron
#	 proton
 
root['/entry/instrument/source'].create_dataset(name='radiation', data='Spallation Neutron Source', maxshape=None)
root['/entry/instrument/source/radiation'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/radiation'].attrs['EX_required'] = 'true'
 
root['/entry/instrument/source'].create_dataset(name='beam_shape', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/instrument/source/beam_shape'].attrs['type'] = 'NX_CHAR'
root['/entry/instrument/source/beam_shape'].attrs['EX_required'] = 'false'
 
root['/entry/instrument/source'].create_dataset(name='incident_wavelength', data=1.0, maxshape=None)
root['/entry/instrument/source/incident_wavelength'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/source/incident_wavelength'].attrs['EX_required'] = 'false'
root['/entry/instrument/source/incident_wavelength'].attrs['units'] = 'NX_WAVELENGTH'
 
root['/entry/instrument/source'].create_dataset(name='wavelength_min', data=1.0, maxshape=None)
root['/entry/instrument/source/wavelength_min'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/source/wavelength_min'].attrs['EX_required'] = 'false'
root['/entry/instrument/source/wavelength_min'].attrs['units'] = 'NX_WAVELENGTH'
 
root['/entry/instrument/source'].create_dataset(name='wavelength_max', data=1.0, maxshape=None)
root['/entry/instrument/source/wavelength_max'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/source/wavelength_max'].attrs['EX_required'] = 'false'
root['/entry/instrument/source/wavelength_max'].attrs['units'] = 'NX_WAVELENGTH'
 
root['/entry/instrument/source'].create_dataset(name='incident_wavelength_spread', data=1.0, maxshape=None)
root['/entry/instrument/source/incident_wavelength_spread'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/source/incident_wavelength_spread'].attrs['EX_required'] = 'false'
root['/entry/instrument/source/incident_wavelength_spread'].attrs['units'] = 'NX_WAVELENGTH'
 
root['/entry/instrument/source'].create_dataset(name='beam_size_x', data=1.0, maxshape=None)
root['/entry/instrument/source/beam_size_x'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/source/beam_size_x'].attrs['EX_required'] = 'false'
root['/entry/instrument/source/beam_size_x'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/instrument/source'].create_dataset(name='beam_size_y', data=1.0, maxshape=None)
root['/entry/instrument/source/beam_size_y'].attrs['type'] = 'NX_NUMBER'
root['/entry/instrument/source/beam_size_y'].attrs['EX_required'] = 'false'
root['/entry/instrument/source/beam_size_y'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/sample'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/sample/name'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/name'].attrs['EX_required'] = 'true'
 
root['/entry/sample'].create_dataset(name='thickness', data=1.0, maxshape=None)
root['/entry/sample/thickness'].attrs['type'] = 'NX_FLOAT'
root['/entry/sample/thickness'].attrs['EX_required'] = 'false'
root['/entry/sample/thickness'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/sample'].create_dataset(name='transmission', data=1.0, maxshape=None)
root['/entry/sample/transmission'].attrs['type'] = 'NX_NUMBER'
root['/entry/sample/transmission'].attrs['EX_required'] = 'false'
root['/entry/sample/transmission'].attrs['units'] = 'NX_DIMENSIONLESS'
 
root['/entry/sample'].create_dataset(name='temperature', data=1.0, maxshape=None)
root['/entry/sample/temperature'].attrs['type'] = 'NX_NUMBER'
root['/entry/sample/temperature'].attrs['EX_required'] = 'false'
root['/entry/sample/temperature'].attrs['units'] = 'NX_TEMPERATURE'
 
root['/entry/sample'].create_dataset(name='details', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/sample/details'].attrs['type'] = 'NX_CHAR'
root['/entry/sample/details'].attrs['EX_required'] = 'false'
root['/entry/sample/details'].attrs['nameType'] = 'any'
 
root['/entry/sample'].create_dataset(name='x_position', data=1.0, maxshape=None)
root['/entry/sample/x_position'].attrs['type'] = 'NX_NUMBER'
root['/entry/sample/x_position'].attrs['EX_required'] = 'false'
root['/entry/sample/x_position'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/sample'].create_dataset(name='y_position', data=1.0, maxshape=None)
root['/entry/sample/y_position'].attrs['type'] = 'NX_NUMBER'
root['/entry/sample/y_position'].attrs['EX_required'] = 'false'
root['/entry/sample/y_position'].attrs['units'] = 'NX_LENGTH'
 
root['/entry/sample'].create_dataset(name='roll', data=1.0, maxshape=None)
root['/entry/sample/roll'].attrs['type'] = 'NX_NUMBER'
root['/entry/sample/roll'].attrs['EX_required'] = 'false'
root['/entry/sample/roll'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='pitch', data=1.0, maxshape=None)
root['/entry/sample/pitch'].attrs['type'] = 'NX_NUMBER'
root['/entry/sample/pitch'].attrs['EX_required'] = 'false'
root['/entry/sample/pitch'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/sample'].create_dataset(name='yaw', data=1.0, maxshape=None)
root['/entry/sample/yaw'].attrs['type'] = 'NX_NUMBER'
root['/entry/sample/yaw'].attrs['EX_required'] = 'false'
root['/entry/sample/yaw'].attrs['units'] = 'NX_ANGLE'
 
root['/entry/process'].create_dataset(name='name', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/process/name'].attrs['type'] = 'NX_CHAR'
root['/entry/process/name'].attrs['EX_required'] = 'false'
 
root['/entry/process'].create_dataset(name='date', data='2021-03-29T15:51:36.547895', maxshape=None)
root['/entry/process/date'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/process/date'].attrs['EX_required'] = 'false'
 
root['/entry/process'].create_dataset(name='description', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/process/description'].attrs['type'] = 'NX_CHAR'
root['/entry/process/description'].attrs['EX_required'] = 'false'
 
root['/entry/process'].create_dataset(name='term', data='SAMPLE-CHAR-DATA', maxshape=None)
root['/entry/process/term'].attrs['type'] = 'NX_CHAR'
root['/entry/process/term'].attrs['EX_required'] = 'false'
root['/entry/process/term'].attrs['nameType'] = 'any'
 
root['/entry/TRANSMISSION_SPECTRUM'].create_dataset(name='lambda', data=1.0, maxshape=None)
root['/entry/TRANSMISSION_SPECTRUM/lambda'].attrs['type'] = 'NX_NUMBER'
root['/entry/TRANSMISSION_SPECTRUM/lambda'].attrs['EX_required'] = 'true'
root['/entry/TRANSMISSION_SPECTRUM/lambda'].attrs['units'] = 'NX_WAVELENGTH'
 
root['/entry/TRANSMISSION_SPECTRUM'].create_dataset(name='T', data=1.0, maxshape=None)
root['/entry/TRANSMISSION_SPECTRUM/T'].attrs['type'] = 'NX_NUMBER'
root['/entry/TRANSMISSION_SPECTRUM/T'].attrs['EX_required'] = 'true'
root['/entry/TRANSMISSION_SPECTRUM/T'].attrs['units'] = 'NX_DIMENSIONLESS'
 
root['/entry/TRANSMISSION_SPECTRUM'].create_dataset(name='Tdev', data=1.0, maxshape=None)
root['/entry/TRANSMISSION_SPECTRUM/Tdev'].attrs['type'] = 'NX_NUMBER'
root['/entry/TRANSMISSION_SPECTRUM/Tdev'].attrs['EX_required'] = 'true'
root['/entry/TRANSMISSION_SPECTRUM/Tdev'].attrs['units'] = 'NX_DIMENSIONLESS'

# Create the DOC strings 
root['/entry'].attrs['EX_doc'] = '.. index:: NXcanSAS (applications); SASentry Place the canSAS ``SASentry`` group as a child of a NeXus ``NXentry`` group (when data from multiple techniques are being stored) or as a replacement for the ``NXentry`` group. Note: It is required for all numerical objects to provide a *units* attribute that describes the engineering units. Use the Unidata UDunits [#]_ specification as this is compatible with various community standards. .. [#] The UDunits specification also includes instructions for derived units. '
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this subentry conforms. '
root['/entry/data'].attrs['EX_doc'] = 'A *SASData* group contains a single reduced small-angle scattering data set that can be represented as :math:`I(\vec{Q})` or :math:`I(|\vec{Q}|)`. *Q* can be either a vector (:math:`\vec{Q}`) or a vector magnitude (:math:`|\vec{Q}|`) The name of each *SASdata* group must be unique within a SASentry group. Suggest using names such as ``sasdata01``. NOTE: For the first *SASdata* group, be sure to write the chosen name into the `SASentry/@default` attribute, as in:: SASentry/@default="sasdata01" A *SASdata* group has several attributes: * I_axes * Q_indices * Mask_indices To indicate the dependency relationships of other varied parameters, use attributes similar to ``@Mask_indices`` (such as ``@Temperature_indices`` or ``@Pressure_indices``). '
root['/entry/data/Q'].attrs['EX_doc'] = '.. index:: NXcanSAS (applications); Q     Array of :math:`Q` data to accompany :math:`I`. .. figure:: canSAS/Q-geometry.jpg  :width: 60%  The :math:`\vec{Q}` geometry.  (:download:`full image <canSAS/Q-geometry.jpg>`) :math:`Q` may be represented as either the three-dimensional scattering vector :math:`\vec{Q}` or the magnitude of the scattering vector, :math:`|\vec{Q}|`. .. math:: |\vec{Q}| = (4\pi/\lambda) sin(\theta) When we write :math:`Q`, we may refer to either or both of :math:`|\vec{Q}|` or :math:`\vec{Q}`, depending on the context. '
root['/entry/data/I'].attrs['EX_doc'] = '.. index:: NXcanSAS (applications); I     Array of intensity (:math:`I`) data. The intensity may be represented in one of these forms: **absolute units**: :math:`d\Sigma/d\Omega(Q)` differential cross-section per unit volume per unit solid angle (such as: 1/cm/sr or 1/m/sr) **absolute units**: :math:`d\sigma/d\Omega(Q)` differential cross-section per unit atom per unit solid angle (such as: cm^2 or m^2) **arbitrary units**: :math:`I(Q)` usually a ratio of two detectors but units are meaningless (such as: a.u. or counts) This presents a few problems for analysis software to sort out when reading the data. Fortunately, it is possible to analyze the *units* to determine which type of intensity is being reported and make choices at the time the file is read. But this is an area for consideration and possible improvement. One problem arises with software that automatically converts data into some canonical units used by that software. The software should not convert units between these different types of intensity indiscriminately. A second problem is that when arbitrary units are used, then the set of possible analytical results is restricted. With such units, no meaningful volume fraction or number density can be determined directly from :math:`I(Q)`. In some cases, it is possible to apply a factor to convert the arbitrary units to an absolute scale. This should be considered as a possibility of the analysis process. Where this documentation says *typical units*, it is possible that small-angle data may be presented in other units and still be consistent with NeXus. See the :ref:`design-units` section. '
root['/entry/data/Idev'].attrs['EX_doc'] = '.. index:: NXcanSAS (applications); Idev Estimated **uncertainty** (usually standard deviation) in :math:`I`. Must have the same units as :math:`I`. When present, the name of this field is also recorded in the *uncertainties* attribute of *I*, as in:: I/@uncertainties="Idev" '
root['/entry/data/Qdev'].attrs['EX_doc'] = '.. index:: NXcanSAS (applications); Qdev Estimated :math:`Q` **resolution** (usually standard deviation). Must have the same units as :math:`Q`. When present, the name of this field is also recorded in the *resolutions* attribute of *Q*, as in:: Q/@resolutions="Qdev" or:: Q/@resolutions="dQw", "dQl" '
root['/entry/data/dQw'].attrs['EX_doc'] = '.. index:: NXcanSAS (applications); dQw :math:`Q` **resolution** along the axis of scanning (the high-resolution *slit width* direction). Useful for defining resolution data from slit-smearing instruments such as Bonse-Hart geometry. Must have the same units as :math:`Q`. When present, the name of this field is also recorded in the *resolutions* attribute of *Q*, as in:: Q/@resolutions="dQw", "dQl" '
root['/entry/data/dQl'].attrs['EX_doc'] = '.. index:: NXcanSAS (applications); dQl :math:`Q` **resolution** perpendicular to the axis of scanning (the low-resolution *slit length* direction). Useful for defining resolution data from slit-smearing instruments such as Bonse-Hart geometry. Must have the same units as :math:`Q`. When present, the name of this field is also recorded in the *resolutions* attribute of *Q*, as in:: Q/@resolutions="dQw", "dQl" '
root['/entry/data/Qmean'].attrs['EX_doc'] = 'Mean value of :math:`Q` for this data point. Useful when describing data that has been binned from higher-resolution data. It is expected that ``Q`` is provided and that both ``Q`` and ``Qmean`` will have the same units. '
root['/entry/data/ShadowFactor'].attrs['EX_doc'] = 'A numerical factor applied to pixels affected by the beam stop penumbra. Used in data files from NIST/NCNR instruments. See: J.G. Barker and J.S. Pedersen (1995) *J. Appl. Cryst.* **28**, 105-114. '
root['/entry/title'].attrs['EX_doc'] = 'Title of this *SASentry*. Make it so that you can recognize the data by its title. Could be the name of the sample, the name for the measured data, or something else representative. '
root['/entry/run'].attrs['EX_doc'] = 'Run identification for this *SASentry*. For many facilities, this is an integer, such as en experiment number. Use multiple instances of ``run`` as needed, keeping in mind that HDF5 requires unique names for all entities in a group. '
root['/entry/instrument'].attrs['EX_doc'] = 'Description of the small-angle scattering instrument. Consider, carefully, the relevance to the SAS data analysis process when adding subgroups in this **NXinstrument** group. Additional information can be added but will likely be ignored by standardized data anlysis processes. The NeXus :ref:`NXbeam` base class may be added as a subgroup of this **NXinstrument** group *or* as a subgroup of the **NXsample** group to describe properties of the beam at any point downstream from the source. '
root['/entry/instrument/aperture'].attrs['EX_doc'] = ':ref:`NXaperture` is generic and limits the variation in data files. Possible NeXus base class alternatives are: :ref:`NXpinhole` or :ref:`NXslit`. '
root['/entry/instrument/aperture/shape'].attrs['EX_doc'] = 'describe the type of aperture (pinhole, 4-blade slit, Soller slit, ...) '
root['/entry/instrument/aperture/x_gap'].attrs['EX_doc'] = 'opening along the :math:`x` axis '
root['/entry/instrument/aperture/y_gap'].attrs['EX_doc'] = 'opening along the :math:`y` axis '
root['/entry/instrument/collimator'].attrs['EX_doc'] = 'Description of a collimating element (defines the divergence of the beam) in the instrument. To document a slit, pinhole, or the beam, refer to the documentation of the ``NXinstrument`` group above. '
root['/entry/instrument/collimator/length'].attrs['EX_doc'] = 'Amount/length of collimation inserted (as on a SANS instrument) '
root['/entry/instrument/collimator/distance'].attrs['EX_doc'] = 'Distance from this collimation element to the sample '
root['/entry/instrument/detector'].attrs['EX_doc'] = 'Description of a detector in the instrument. '
root['/entry/instrument/detector/name'].attrs['EX_doc'] = 'Identifies the name of this detector '
root['/entry/instrument/detector/SDD'].attrs['EX_doc'] = 'Distance between sample and detector. Note: In NXdetector, the ``distance`` field records the distance to the previous component ... most often the sample. This use is the same as ``SDD`` for most SAS instruments but not all. For example, Bonse-Hart cameras have one or more crystals between the sample and detector. We define here the field ``SDD`` to document without ambiguity the distance between sample and detector. '
root['/entry/instrument/detector/slit_length'].attrs['EX_doc'] = 'Slit length of the instrument for this detector, expressed in the same units as :math:`Q`. '
root['/entry/instrument/detector/x_position'].attrs['EX_doc'] = 'Location of the detector in :math:`x` '
root['/entry/instrument/detector/y_position'].attrs['EX_doc'] = 'Location of the detector in :math:`y` '
root['/entry/instrument/detector/roll'].attrs['EX_doc'] = 'Rotation of the detector about the :math:`z` axis (roll) '
root['/entry/instrument/detector/pitch'].attrs['EX_doc'] = 'Rotation of the detector about the :math:`x` axis (roll) '
root['/entry/instrument/detector/yaw'].attrs['EX_doc'] = 'Rotation of the detector about the :math:`y` axis (yaw) '
root['/entry/instrument/detector/beam_center_x'].attrs['EX_doc'] = 'Position of the beam center on the detector. This is the x position where the direct beam would hit the detector plane. This is a length and can be outside of the actual detector. The length can be in physical units or pixels as documented by the units attribute. The value can be any real number (positive, zero, or negative). '
root['/entry/instrument/detector/beam_center_y'].attrs['EX_doc'] = 'Position of the beam center on the detector. This is the y position where the direct beam would hit the detector plane. This is a length and can be outside of the actual detector. The length can be in physical units or pixels as documented by the units attribute. The value can be any real number (positive, zero, or negative). '
root['/entry/instrument/detector/x_pixel_size'].attrs['EX_doc'] = 'Size of each detector pixel. If it is scalar all pixels are the same size '
root['/entry/instrument/detector/y_pixel_size'].attrs['EX_doc'] = 'Size of each detector pixel. If it is scalar all pixels are the same size '
root['/entry/instrument/source'].attrs['EX_doc'] = 'Description of the radiation source. '
root['/entry/instrument/source/radiation'].attrs['EX_doc'] = 'Name of the radiation used. Note that this is **not** the name of the facility! This field contains a value from either the ``probe`` or ``type`` fields in :ref:`NXsource`. Thus, it is redundant with existing NeXus structure. '
root['/entry/instrument/source/beam_shape'].attrs['EX_doc'] = 'Text description of the shape of the beam (incident on the sample). '
root['/entry/instrument/source/incident_wavelength'].attrs['EX_doc'] = 'wavelength (:math:`\lambda`) of radiation incident on the sample '
root['/entry/instrument/source/wavelength_min'].attrs['EX_doc'] = 'Some facilities specify wavelength using a range. This is the lowest wavelength in such a range. '
root['/entry/instrument/source/wavelength_max'].attrs['EX_doc'] = 'Some facilities specify wavelength using a range. This is the highest wavelength in such a range. '
root['/entry/instrument/source/incident_wavelength_spread'].attrs['EX_doc'] = 'Some facilities specify wavelength using a range. This is the width (FWHM) of such a range. '
root['/entry/instrument/source/beam_size_x'].attrs['EX_doc'] = 'Size of the incident beam along the x axis. '
root['/entry/instrument/source/beam_size_y'].attrs['EX_doc'] = 'Size of the incident beam along the y axis. '
root['/entry/sample'].attrs['EX_doc'] = 'Description of the sample. '
root['/entry/sample/name'].attrs['EX_doc'] = '**ID**: Text string that identifies this sample. '
root['/entry/sample/thickness'].attrs['EX_doc'] = 'Thickness of this sample '
root['/entry/sample/transmission'].attrs['EX_doc'] = 'Transmission (:math:`I/I_0`) of this sample. There is no *units* attribute as this number is dimensionless. Note: the ability to store a transmission *spectrum*, instead of a single value, is provided elsewhere in the structure, in the *SAStransmission_spectrum* element. '
root['/entry/sample/temperature'].attrs['EX_doc'] = 'Temperature of this sample. '
root['/entry/sample/details'].attrs['EX_doc'] = 'Any additional sample details. '
root['/entry/sample/x_position'].attrs['EX_doc'] = 'Location of the sample in :math:`x` '
root['/entry/sample/y_position'].attrs['EX_doc'] = 'Location of the sample in :math:`y` '
root['/entry/sample/roll'].attrs['EX_doc'] = 'Rotation of the sample about the :math:`z` axis (roll) '
root['/entry/sample/pitch'].attrs['EX_doc'] = 'Rotation of the sample about the :math:`x` axis (roll) '
root['/entry/sample/yaw'].attrs['EX_doc'] = 'Rotation of the sample about the :math:`y` axis (yaw) '
root['/entry/process'].attrs['EX_doc'] = 'Description of a processing or analysis step. Add additional fields as needed to describe value(s) of any variable, parameter, or term related to the *SASprocess* step. Be sure to include *units* attributes for all numerical fields. '
root['/entry/process/name'].attrs['EX_doc'] = 'Optional name for this data processing or analysis step '
root['/entry/process/date'].attrs['EX_doc'] = 'Optional date for this data processing or analysis step. [#iso8601]_            .. [#iso8601] ISO-8601 standard time representation.         NeXus dates and times are reported in ISO-8601     (e.g., ``yyyy-mm-ddThh:mm:ss``)     or modified ISO-8601 (e.g., ``yyyy-mm-dd hh:mm:ss``).          See: http://www.w3.org/TR/NOTE-datetime     or http://en.wikipedia.org/wiki/ISO_8601 for more details. '
root['/entry/process/description'].attrs['EX_doc'] = 'Optional description for this data processing or analysis step '
root['/entry/process/term'].attrs['EX_doc'] = 'Specifies the value of a single variable, parameter, or term (while defined here as a string, it could be a number) related to the *SASprocess* step. Note: The name *term* is not required, it could take any name, as long as the name is unique within this group. '
root['/entry/process/note'].attrs['EX_doc'] = 'Any additional notes or subprocessing steps will be documented here.     An **NXnote** group can be added to any NeXus group at or below the   **NXentry** group. It is shown here as a suggestion of a good place   to *consider* its use. '
root['/entry/process/collection'].attrs['EX_doc'] = 'Describes anything about *SASprocess* that is not already described. Any content not defined in the canSAS standard can be placed at this point. Note: The name of this group is flexible, it could take any name, as long as it is unique within the **NXprocess** group. '
root['/entry/collection'].attrs['EX_doc'] = 'Free form description of anything not covered by other elements. '
root['/entry/TRANSMISSION_SPECTRUM'].attrs['EX_doc'] = 'The *SAStransmission_spectrum* element This describes certain data obtained from a variable-wavelength source such as pulsed-neutron source. '
root['/entry/TRANSMISSION_SPECTRUM/lambda'].attrs['EX_doc'] = 'Wavelength of the radiation. This array is of the same shape as ``T`` and ``Tdev``. '
root['/entry/TRANSMISSION_SPECTRUM/T'].attrs['EX_doc'] = 'Transmission values (:math:`I/I_0`) as a function of wavelength. This array is of the same shape as ``lambda`` and ``Tdev``. '
root['/entry/TRANSMISSION_SPECTRUM/Tdev'].attrs['EX_doc'] = '.. index:: NXcanSAS (applications); Tdev Estimated uncertainty (usually standard deviation) in :math:`T`. Must have the same units as :math:`T`. This is the field is named in the *uncertainties* attribute of *T*, as in:: T/@uncertainties="Tdev" This array is of the same shape as ``lambda`` and ``T``. '
 

# Create the ATTRIBUTES 
root['/entry'].attrs['default'] = 'SAMPLE-CHAR-DATA'
root['/entry'].attrs['canSAS_class'] = 'SAMPLE-CHAR-DATA'
root['/entry'].attrs['version'] = 'SAMPLE-CHAR-DATA'
root['/entry/data'].attrs['canSAS_class'] = 'SAMPLE-CHAR-DATA'
root['/entry/data'].attrs['signal'] = 'SAMPLE-CHAR-DATA'
root['/entry/data'].attrs['I_axes'] = 'SAMPLE-CHAR-DATA'
root['/entry/data'].attrs['Q_indices'] = '1'
root['/entry/data'].attrs['mask'] = 'SAMPLE-CHAR-DATA'
root['/entry/data'].attrs['Mask_indices'] = 'SAMPLE-CHAR-DATA'
root['/entry/data'].attrs['timestamp'] = '2021-03-29T15:51:36.601894'
root['/entry/data/Q'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/Q'].attrs['uncertainties'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/Q'].attrs['resolutions'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/Q'].attrs['resolutions_description'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/I'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/I'].attrs['uncertainties'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/I'].attrs['scaling_factor'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/Idev'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/Qdev'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/dQw'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/dQl'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/Qmean'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry/run'].attrs['name'] = 'SAMPLE-CHAR-DATA'
root['/entry/instrument'].attrs['canSAS_class'] = 'SAMPLE-CHAR-DATA'
root['/entry/instrument/aperture'].attrs['canSAS_class'] = 'SAMPLE-CHAR-DATA'
root['/entry/instrument/collimator'].attrs['canSAS_class'] = 'SAMPLE-CHAR-DATA'
root['/entry/instrument/detector'].attrs['canSAS_class'] = 'SAMPLE-CHAR-DATA'
root['/entry/instrument/source'].attrs['canSAS_class'] = 'SAMPLE-CHAR-DATA'
root['/entry/sample'].attrs['canSAS_class'] = 'SAMPLE-CHAR-DATA'
root['/entry/process'].attrs['canSAS_class'] = 'SAMPLE-CHAR-DATA'
root['/entry/process/collection'].attrs['canSAS_class'] = 'SAMPLE-CHAR-DATA'
root['/entry/collection'].attrs['canSAS_class'] = 'SAMPLE-CHAR-DATA'
root['/entry/TRANSMISSION_SPECTRUM'].attrs['canSAS_class'] = 'SAMPLE-CHAR-DATA'
root['/entry/TRANSMISSION_SPECTRUM'].attrs['signal'] = 'SAMPLE-CHAR-DATA'
root['/entry/TRANSMISSION_SPECTRUM'].attrs['T_axes'] = 'SAMPLE-CHAR-DATA'
root['/entry/TRANSMISSION_SPECTRUM'].attrs['name'] = 'SAMPLE-CHAR-DATA'
root['/entry/TRANSMISSION_SPECTRUM'].attrs['timestamp'] = '2021-03-29T15:51:36.609872'
root['/entry/TRANSMISSION_SPECTRUM/T'].attrs['uncertainties'] = 'SAMPLE-CHAR-DATA'
root['/'].attrs['default'] = 'entry'
root['/entry'].attrs['default'] = 'TRANSMISSION_SPECTRUM'
root['/entry/TRANSMISSION_SPECTRUM'].attrs['signal'] = 'T'
root['/entry/TRANSMISSION_SPECTRUM/T'].attrs['signal'] = '1'
root.attrs['file_name'] = os.path.abspath('NXcanSAS')
root.attrs['file_time'] = datetime.datetime.now().isoformat()
root.attrs['h5py_version'] = h5py.version.version
root.attrs['HDF5_Version'] = h5py.version.hdf5_version

# Close the file
root.close()


