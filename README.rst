NeXus exampledata
=================

Examples of (mostly) real world NeXus files to inspect, 
test and train reading software with.

Some files are HDF5, some HDF4, some XML, and some are broken files
which are good for testing.
Please advise us if you have difficulties with any of these files.
For sure, we need more documentation here.

..
   Really, we need to add some README files throughout,
   annotating the contents of each directory.
   Perhaps, also, having a top-level directory
   of really GOOD examples.

NeXus compliance of files
~~~~~~~~~~~~~~~~~~~~~~~~~

..	new way to find the default dataset
	https://github.com/nexusformat/definitions/issues/380

An automated analysis of the files, by directory, 
in this <exampledata> repository is shown below.
Only HDF5 files that satisfy the structure::

	<file_root>:
		entry (NXentry)
			data (NXdata)
				<dataset>:
					@signal = 1

are identified as *NeXus HDF5* files at this time.


.. --- CRITIQUE report starts after this line ---
.. date: 2015-05-31


<exampledata>
+++++++++++++
:.project:  not HDF5 file
:.pydevproject:  not HDF5 file
:MANIFEST.in:  not HDF5 file
:README.rst:  not HDF5 file
:critique.py:  not HDF5 file
:simple3D.h5:  NeXus HDF5 file, 1 **NXentry** group
:verysimple.xml:  not HDF5 file
:writer_1_3.h5:  NeXus HDF5 file, 1 **NXentry** group

<exampledata>/ANSTO
+++++++++++++++++++
:PLP0006018.nx.hdf:  NeXus HDF5 file, 1 **NXentry** group

<exampledata>/APS/CCDImageServer
++++++++++++++++++++++++++++++++
:README.txt:  not HDF5 file
:Smither400.3_apr0300051.hdf:  not HDF5 file
:Smither400.3_apr0300052.hdf:  not HDF5 file
:Smither400.3_apr0300053.hdf:  not HDF5 file
:Smither400.3_apr0300054.hdf:  not HDF5 file
:Smither400.3_apr0300055.hdf:  not HDF5 file
:recon_0123.hdf:  not HDF5 file
:recon_0124.hdf:  not HDF5 file
:recon_0125.hdf:  not HDF5 file

<exampledata>/APS/EPICSareaDetector/NeXus-plugin
++++++++++++++++++++++++++++++++++++++++++++++++
:AgBehenate_228.hdf5:  NeXus HDF5 file, 1 **NXentry** group

<exampledata>/APS/other
+++++++++++++++++++++++
:ID34_not_complete.h5:  NeXus HDF5 file, 1 **NXentry** group

<exampledata>/APS/scan2nexus
++++++++++++++++++++++++++++
:14BMC_0015.mda:  not HDF5 file
:14BMC_0015.nexus:  not HDF5 file
:14BMC_0015.xml:  not HDF5 file
:2iddf_0106.mda:  not HDF5 file
:2iddf_0106.nexus:  not HDF5 file
:2iddf_0106.xml:  not HDF5 file
:README:  not HDF5 file
:mts_0347.mda:  not HDF5 file
:mts_0347.nexus:  not HDF5 file
:mts_0347.xml:  not HDF5 file
:mts_0348.mda:  not HDF5 file
:mts_0348.nexus:  not HDF5 file
:mts_0348.xml:  not HDF5 file
:sample.mda.text:  not HDF5 file
:sample1.mda:  not HDF5 file
:sample1.nexus:  not HDF5 file
:sample1.xml:  not HDF5 file

<exampledata>/APS/tomo
++++++++++++++++++++++
:Tomography_metadata.hdf:  not HDF5 file
:Tomography_raw.hdf:  not HDF5 file

<exampledata>/IPNS/LRMECS
+++++++++++++++++++++++++
:lrcs3701.nx5:  NeXus HDF5 file, 2 **NXentry** groups
:lrcs3701.nxs:  not HDF5 file

<exampledata>/Soleil
++++++++++++++++++++
:file_1.nxs:  NeXus HDF5 file, 1 **NXentry** group
:file_2.nxs:  NeXus HDF5 file, 1 **NXentry** group

<exampledata>/code/hdf4
+++++++++++++++++++++++
:NXtest.hdf:  not HDF5 file
:dmc01.hdf:  not HDF5 file
:dmc02.hdf:  not HDF5 file

<exampledata>/code/hdf5
+++++++++++++++++++++++
:NXtest.h5:  HDF5 file, 2 **NXentry** groups
:dmc01.h5:  NeXus HDF5 file, 1 **NXentry** group
:dmc02.h5:  NeXus HDF5 file, 1 **NXentry** group
:focus2007n001335.hdf:  NeXus HDF5 file, 1 **NXentry** group
:sans2009n012333.hdf:  NeXus HDF5 file, 1 **NXentry** group

<exampledata>/code/xml
++++++++++++++++++++++
:NXtest.xml.txt:  not HDF5 file
:dmc01.xml.txt:  not HDF5 file
:dmc02.xml.txt:  not HDF5 file
