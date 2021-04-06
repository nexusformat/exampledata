# NeXus exampledata

Examples of (mostly) real world NeXus files with which to inspect, 
test and train reading software.

This repository is organised so that files in directories called
`hdf4` are NeXus HDF4, `hdf5` are NeXus HDF5 and `xml` are NeXus xml.
(See a cursory [critique](critique.md) of each file.)
Note that some are broken files
which are good for testing.
Please advise us if you have difficulties with any of these files.
For sure, we need more documentation here.

The files *writer_1_3.h5* and *writer_1_3__niac2014.h5*
are taken directly from the NeXus online documentation

## Autogenerated examples for all application definitions

In the `autogenerated_examples/nxdl` directory you will find examples of each
application definition in several forms, hdf5 files and python scripts that will 
create hdf5 files which contain the required structure (groups/fields/attributes) 
for each application definition. The data used for fields is meant only to show 
the type of data required, not actually valid data (spectra or images) for each field, 
the hope is that by studying the examples it will make it easier for users to 
understand what they need to do in order to create Nexus compliant files for their desired
application definition.

Directory contents of examples found in the `autogenerated_examples/nxdl` directory:
    
&nbsp;&nbsp;`*/applications`    Contains hdf5 files for each definition

&nbsp;&nbsp;`*/python_scripts/h5py`    Contains python scripts to create each definition using **h5py**

&nbsp;&nbsp;`*/python_scripts/nexusformat`    Contains python scripts to create each definition using **nexusformat**



## NeXus compliance of files

An automated analysis (via code [*critique.py*](critique.py)) of the files, by directory, 
in this *<exampledata>* repository is given in file: [critique](critique.md).
HDF5 files that satisfy the structure:

    <file_root>:
        entry (NXentry)

are automatically identified as *NeXus HDF5 file* at this time.

An analysis by the `critique.py` program (in this repository)
is available: [*critique*](critique.md)
