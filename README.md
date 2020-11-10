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

## NeXus compliance of files

An automated analysis (via code [*critique.py*](critique.py)) of the files, by directory, 
in this *<exampledata>* repository is given in file: [critique](critique.md).
HDF5 files that satisfy the structure:

    <file_root>:
        entry (NXentry)

are automatically identified as *NeXus HDF5 file* at this time.

An analysis by the `critique.py` program (in this repository)
is available: [*critique*](critique.md)
