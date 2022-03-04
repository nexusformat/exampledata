 
import numpy as np
from nexusformat.nexus import *
 
# Note this example script was generated by nxdl_to_hdf5.py using the current 
# installed version of the NEXUS definitions ver[v2020.10] 
 
root = NXroot()

# Create the GROUPS 
root['/entry'] = NXentry()
root['/entry'].attrs['EX_required'] = 'false'
root['/entry/monitor'] = NXmonitor()
root['/entry/monitor'].attrs['EX_required'] = 'false'
root['/entry/data'] = NXdata()
root['/entry/data'].attrs['EX_required'] = 'false'
root['/entry/counter_cross_reference'] = NXnote()
root['/entry/counter_cross_reference'].attrs['EX_required'] = 'false'
root['/entry/positioner_cross_reference'] = NXnote()
root['/entry/positioner_cross_reference'].attrs['EX_required'] = 'false'
root['/entry/spec'] = NXinstrument()
root['/entry/spec'].attrs['EX_required'] = 'false'
root['/entry/spec/UB'] = NXcrystal()
root['/entry/spec/UB'].attrs['EX_required'] = 'false'
root['/entry/G'] = NXnote()
root['/entry/G'].attrs['EX_required'] = 'false'
root['/entry/positioners'] = NXnote()
root['/entry/positioners'].attrs['EX_required'] = 'false'
root['/entry/MCA'] = NXnote()
root['/entry/MCA'].attrs['EX_required'] = 'false'
root['/entry/MCA/ROI'] = NXnote()
root['/entry/MCA/ROI'].attrs['EX_required'] = 'false'
root['/entry/metadata'] = NXnote()
root['/entry/metadata'].attrs['EX_required'] = 'false'
root['/entry/SPEC_user'] = NXuser()
root['/entry/SPEC_user'].attrs['EX_required'] = 'false'
root['/entry/_unrecognized'] = NXnote()
root['/entry/_unrecognized'].attrs['EX_required'] = 'false'

# Create the FIELDS 
 
# Valid enumeration values for root['/entry']['definition'] are: 
#	 NXspecdata
 
root['/entry/definition'] = NXfield('NXspecdata')
root['/entry/definition'].attrs['type'] = 'NX_CHAR'
root['/entry/definition'].attrs['EX_required'] = 'false'
 
root['/entry/scan_number'] = NXfield(1.0)
root['/entry/scan_number'].attrs['type'] = 'NX_NUMBER'
root['/entry/scan_number'].attrs['EX_required'] = 'false'
 
root['/entry/title'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/title'].attrs['type'] = 'NX_CHAR'
root['/entry/title'].attrs['EX_required'] = 'false'
 
root['/entry/command'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/command'].attrs['type'] = 'NX_CHAR'
root['/entry/command'].attrs['EX_required'] = 'false'
 
root['/entry/date'] = NXfield('2022-03-04T14:56:25.717441')
root['/entry/date'].attrs['type'] = 'NX_DATE_TIME'
root['/entry/date'].attrs['EX_required'] = 'false'
 
# Valid enumeration values for root['/entry/monitor']['mode'] are: 
#	 monitor
#	 timer
 
root['/entry/monitor/mode'] = NXfield('monitor')
root['/entry/monitor/mode'].attrs['type'] = 'NX_CHAR'
root['/entry/monitor/mode'].attrs['EX_required'] = 'false'
 
root['/entry/monitor/preset'] = NXfield(1.0)
root['/entry/monitor/preset'].attrs['type'] = 'NX_NUMBER'
root['/entry/monitor/preset'].attrs['EX_required'] = 'false'
 
root['/entry/monitor/data'] = NXfield(1.0)
root['/entry/monitor/data'].attrs['type'] = 'NX_NUMBER'
root['/entry/monitor/data'].attrs['EX_required'] = 'false'
root['/entry/monitor/data'].attrs['nameType'] = 'any'
 
root['/entry/monitor/count_time'] = NXfield(1.0)
root['/entry/monitor/count_time'].attrs['type'] = 'NX_NUMBER'
root['/entry/monitor/count_time'].attrs['EX_required'] = 'false'
root['/entry/monitor/count_time'].attrs['nameType'] = 'any'
 
root['/entry/comments'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/comments'].attrs['type'] = 'NX_CHAR'
root['/entry/comments'].attrs['EX_required'] = 'false'
 
root['/entry/Q'] = NXfield(1.0)
root['/entry/Q'].attrs['type'] = 'NX_NUMBER'
root['/entry/Q'].attrs['EX_required'] = 'false'
 
root['/entry/TEMP_SP'] = NXfield(1.0)
root['/entry/TEMP_SP'].attrs['type'] = 'NX_NUMBER'
root['/entry/TEMP_SP'].attrs['EX_required'] = 'false'
 
root['/entry/DEGC_SP'] = NXfield(1.0)
root['/entry/DEGC_SP'].attrs['type'] = 'NX_NUMBER'
root['/entry/DEGC_SP'].attrs['EX_required'] = 'false'
 
root['/entry/data/data'] = NXfield(1.0)
root['/entry/data/data'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/data'].attrs['EX_required'] = 'false'
root['/entry/data/data'].attrs['nameType'] = 'any'
 
root['/entry/data/intensity_factor'] = NXfield(1.0)
root['/entry/data/intensity_factor'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/intensity_factor'].attrs['EX_required'] = 'false'
 
root['/entry/data/_mca_'] = NXfield(1.0)
root['/entry/data/_mca_'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/_mca_'].attrs['EX_required'] = 'false'
 
root['/entry/data/_mca_channel_'] = NXfield(1.0)
root['/entry/data/_mca_channel_'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/_mca_channel_'].attrs['EX_required'] = 'false'
 
root['/entry/data/_mca1_'] = NXfield(1.0)
root['/entry/data/_mca1_'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/_mca1_'].attrs['EX_required'] = 'false'
 
root['/entry/data/_mca1_channel_'] = NXfield(1.0)
root['/entry/data/_mca1_channel_'].attrs['type'] = 'NX_NUMBER'
root['/entry/data/_mca1_channel_'].attrs['EX_required'] = 'false'
 
root['/entry/spec/UB/orientation_matrix'] = NXfield(1.0)
root['/entry/spec/UB/orientation_matrix'].attrs['type'] = 'NX_FLOAT'
root['/entry/spec/UB/orientation_matrix'].attrs['EX_required'] = 'false'
 
root['/entry/G/G0'] = NXfield(1.0)
root['/entry/G/G0'].attrs['type'] = 'NX_NUMBER'
root['/entry/G/G0'].attrs['EX_required'] = 'false'
 
root['/entry/G/G1'] = NXfield(1.0)
root['/entry/G/G1'].attrs['type'] = 'NX_NUMBER'
root['/entry/G/G1'].attrs['EX_required'] = 'false'
 
root['/entry/G/G2'] = NXfield(1.0)
root['/entry/G/G2'].attrs['type'] = 'NX_NUMBER'
root['/entry/G/G2'].attrs['EX_required'] = 'false'
 
root['/entry/G/G4'] = NXfield(1.0)
root['/entry/G/G4'].attrs['type'] = 'NX_NUMBER'
root['/entry/G/G4'].attrs['EX_required'] = 'false'
 
root['/entry/positioners/positioner'] = NXfield(1.0)
root['/entry/positioners/positioner'].attrs['type'] = 'NX_NUMBER'
root['/entry/positioners/positioner'].attrs['EX_required'] = 'false'
root['/entry/positioners/positioner'].attrs['nameType'] = 'any'
 
root['/entry/MCA/preset_time'] = NXfield(1.0)
root['/entry/MCA/preset_time'].attrs['type'] = 'NX_NUMBER'
root['/entry/MCA/preset_time'].attrs['EX_required'] = 'false'
 
root['/entry/MCA/elapsed_live_time'] = NXfield(1.0)
root['/entry/MCA/elapsed_live_time'].attrs['type'] = 'NX_NUMBER'
root['/entry/MCA/elapsed_live_time'].attrs['EX_required'] = 'false'
 
root['/entry/MCA/elapsed_real_time'] = NXfield(1.0)
root['/entry/MCA/elapsed_real_time'].attrs['type'] = 'NX_NUMBER'
root['/entry/MCA/elapsed_real_time'].attrs['EX_required'] = 'false'
 
root['/entry/MCA/number_saved'] = NXfield(1.0)
root['/entry/MCA/number_saved'].attrs['type'] = 'NX_NUMBER'
root['/entry/MCA/number_saved'].attrs['EX_required'] = 'false'
 
root['/entry/MCA/first_saved'] = NXfield(1)
root['/entry/MCA/first_saved'].attrs['type'] = 'NX_INT'
root['/entry/MCA/first_saved'].attrs['EX_required'] = 'false'
 
root['/entry/MCA/last_saved'] = NXfield(1)
root['/entry/MCA/last_saved'].attrs['type'] = 'NX_INT'
root['/entry/MCA/last_saved'].attrs['EX_required'] = 'false'
 
root['/entry/MCA/reduction_coef'] = NXfield(1.0)
root['/entry/MCA/reduction_coef'].attrs['type'] = 'NX_NUMBER'
root['/entry/MCA/reduction_coef'].attrs['EX_required'] = 'false'
 
root['/entry/MCA/calib_a'] = NXfield(1.0)
root['/entry/MCA/calib_a'].attrs['type'] = 'NX_NUMBER'
root['/entry/MCA/calib_a'].attrs['EX_required'] = 'false'
 
root['/entry/MCA/calib_b'] = NXfield(1.0)
root['/entry/MCA/calib_b'].attrs['type'] = 'NX_NUMBER'
root['/entry/MCA/calib_b'].attrs['EX_required'] = 'false'
 
root['/entry/MCA/calib_c'] = NXfield(1.0)
root['/entry/MCA/calib_c'].attrs['type'] = 'NX_NUMBER'
root['/entry/MCA/calib_c'].attrs['EX_required'] = 'false'
 
root['/entry/MCA/ROI/roiN'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/MCA/ROI/roiN'].attrs['type'] = 'NX_CHAR'
root['/entry/MCA/ROI/roiN'].attrs['EX_required'] = 'false'
 
root['/entry/SPEC_user/SPEC_user'] = NXfield('SAMPLE-CHAR-DATA')
root['/entry/SPEC_user/SPEC_user'].attrs['type'] = 'NX_CHAR'
root['/entry/SPEC_user/SPEC_user'].attrs['EX_required'] = 'false'

# Create the DOC strings 
root['/entry'].attrs['EX_doc'] = 'one scan from a SPEC data file, starts with a **#S** line '
root['/entry/definition'].attrs['EX_doc'] = 'Official NeXus NXDL schema to which this subentry conforms. '
root['/entry/scan_number'].attrs['EX_doc'] = 'SPEC scan number '
root['/entry/title'].attrs['EX_doc'] = 'SPEC scan number and command, from **#S** line SPEC data file line:: #S 1 cscan en 690 750 60 0 *title*:: 1 cscan en 690 750 60 0 '
root['/entry/command'].attrs['EX_doc'] = 'SPEC scan command, from **#S** line, after the scan number. :SPEC data file line: ``#S 1 cscan en 690 750 60 0`` :command*: ``cscan en 690 750 60 0`` '
root['/entry/date'].attrs['EX_doc'] = 'date from **#D** line in scan header, in ISO8601 format '
root['/entry/monitor/mode'].attrs['EX_doc'] = 'Count to a preset value based on either clock time (timer) or received monitor counts (monitor). '
root['/entry/monitor/preset'].attrs['EX_doc'] = 'preset value for time or monitor * **#M** -- counting against this constant monitor count (see #T) * **#T** -- counting against this constant number of seconds (see #M) '
root['/entry/monitor/data'].attrs['EX_doc'] = 'array(s) of monitor data '
root['/entry/monitor/count_time'].attrs['EX_doc'] = 'array(s) of monitor data '
root['/entry/comments'].attrs['EX_doc'] = 'Any **#C** lines in this scan, stored as one string with newlines between comments '
root['/entry/Q'].attrs['EX_doc'] = '**#Q** -- :math:`Q` (:math:`hkl`) at start of scan array of [:math:`h` :math:`k` :math:`l`] '
root['/entry/TEMP_SP'].attrs['EX_doc'] = '**#X** -- temperature set point '
root['/entry/DEGC_SP'].attrs['EX_doc'] = '**#X** -- temperature set point (C) '
root['/entry/data'].attrs['EX_doc'] = 'detector (and MCA) data from this scan '
root['/entry/data/data'].attrs['EX_doc'] = 'one column of data from the scan HDF5 requires that each member of a group must have a unique name. Pick the name of column from **#L** but make it unique which means if the same name is used in more than one column, append a number to the extra instances to make them unique yet preserve their content, just in case they might be different. Example: ``seconds seconds`` becomes ``seconds`` and ``seconda_1``. '
root['/entry/data/intensity_factor'].attrs['EX_doc'] = '**#I** -- intensity normalizing factor '
root['/entry/counter_cross_reference'].attrs['EX_doc'] = 'associates values declared in **#J** and **#j** scan header lines '
root['/entry/positioner_cross_reference'].attrs['EX_doc'] = 'associates values declared in **#O** and **#o** scan header lines '
root['/entry/spec'].attrs['EX_doc'] = 'various metadata from the SPEC scan header that have well-known NeXus base clases '
root['/entry/spec/UB'].attrs['EX_doc'] = 'Orientation matrix of single crystal sample using Busing-Levy convention '
root['/entry/spec/UB/orientation_matrix'].attrs['EX_doc'] = '**#G3** line in scan header '
root['/entry/G'].attrs['EX_doc'] = 'SPEC geometry variables for this diffractometer geometry (instrument specific) TODO: give interpreted name for each array value (need to figure out how to get the names) '
root['/entry/G/G0'].attrs['EX_doc'] = 'geometry parameters from G[] array (geo mode, sector, etc) '
root['/entry/G/G1'].attrs['EX_doc'] = 'geometry parameters from U[] array (lattice constants, orientation reflections) '
root['/entry/G/G2'].attrs['EX_doc'] = 'not used, although some files has a single zero value '
root['/entry/G/G4'].attrs['EX_doc'] = 'geometry parameters from Q[] array (lambda, frozen angles, cut points, etc) '
root['/entry/positioners'].attrs['EX_doc'] = 'names and values of all positioners (**#O** and **#P** lines) in scan header '
root['/entry/positioners/positioner'].attrs['EX_doc'] = 'one positioner from the scan header HDF5 requires that each member of a group must have a unique name. SPEC assigns a unique name to each positioner, no extra work is neccesary to comply with the HDF5 rule for unique names in a group. '
root['/entry/MCA'].attrs['EX_doc'] = '**#@CALIB** -- coefficients to compute a scale based on the MCA channel number '
root['/entry/MCA/ROI/roiN'].attrs['EX_doc'] = 'numbered regions of interest, use an index number as part of the name '
root['/entry/metadata'].attrs['EX_doc'] = 'SPEC metadata (UNICAT-style #H and #V lines) This is a block that may be unique to SPEC files acquired at certain APS beam lines. Other facilities or instruments may use this block for storing key:value pairs of data where the values have suitable attributes (such as units). '
root['/entry/SPEC_user/SPEC_user'].attrs['EX_doc'] = 'user name from first **#C** line in file header '
root['/entry/_unrecognized'].attrs['EX_doc'] = 'Fallback for any SPEC data file control lines not otherwise placed into groups or fields elsewhere in this specification. '
 

# Create the ATTRIBUTES 
root['/entry/SAMPLE-CHAR-DATA'] = NXdata()
root['/entry/SAMPLE-CHAR-DATA'].set_default()
root['/entry/monitor'].attrs['description'] = 'SAMPLE-CHAR-DATA'
root['/entry/monitor/preset'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry/data'].attrs['description'] = 'SAMPLE-CHAR-DATA'
root['/entry/data'].attrs['signal'] = 'SAMPLE-CHAR-DATA'
root['/entry/data'].attrs['axes'] = 'SAMPLE-CHAR-DATA'
root['/entry/data'].attrs['AXISNAME_indices'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/data'].attrs['spec_name'] = 'SAMPLE-CHAR-DATA'
root['/entry/data/data'].attrs['units'] = 'SAMPLE-CHAR-DATA'
root['/entry/counter_cross_reference'].attrs['comment'] = 'SAMPLE-CHAR-DATA'
root['/entry/counter_cross_reference'].attrs['description'] = 'SAMPLE-CHAR-DATA'
root['/entry/positioner_cross_reference'].attrs['comment'] = 'SAMPLE-CHAR-DATA'
root['/entry/positioner_cross_reference'].attrs['description'] = 'SAMPLE-CHAR-DATA'
root['/entry/G'].attrs['comment'] = 'SAMPLE-CHAR-DATA'
root['/entry/G'].attrs['description'] = 'SAMPLE-CHAR-DATA'
root['/entry/positioners'].attrs['description'] = 'SAMPLE-CHAR-DATA'
root['/entry/MCA'].attrs['description'] = 'SAMPLE-CHAR-DATA'
root['/entry/MCA/ROI/roiN'].attrs['description'] = 'SAMPLE-CHAR-DATA'
root['/entry/MCA/ROI/roiN'].attrs['first_channel'] = 'SAMPLE-CHAR-DATA'
root['/entry/MCA/ROI/roiN'].attrs['last_channel'] = 'SAMPLE-CHAR-DATA'
root['/entry/metadata'].attrs['description'] = 'SAMPLE-CHAR-DATA'
root['/entry/_unrecognized'].attrs['comment'] = 'SAMPLE-CHAR-DATA'
root['/entry/_unrecognized'].attrs['description'] = 'SAMPLE-CHAR-DATA'
root.attrs['default'] = 'entry'
root['/entry/data'].set_default()
root['/entry/data'].attrs['signal'] = 'data'
root['/entry/data/data'].attrs['signal'] = '1'

# Save the file
root.save('NXspecdata.nxs', 'w')


