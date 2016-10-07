Diamond Light Source
====================

i16
---
The data collection was a theta scan where both detector and sample on a
six-circle kappa diffractometer are moved. The NeXus file conforms to the
NXmx application definition.

===================================  ============================================
538039.nxs                           Holds all metadata and links to image data
538039-pilatus100k-files/538039.hdf  Image data from scan
===================================  ============================================

reflections
-----------
Pilatus data from the example thaumatin dataset collected at DLS and provided
in the DIALS tutorial was indexed and integrated using the commands from that
tutorial. The integrated reflections were exported to NeXus using dials.export
format=nxs integrated_experiments.json integrated.pickle.

This datafile provides an example for NXreflections, a candidate application
definition for recording integrated Bragg reflection intensities.

The file was modified to only contain 10 Bragg reflections to save space in git.
