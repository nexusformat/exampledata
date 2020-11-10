# Critique of *exampledata* files

* date: 2020-11-10 17:41:04.990698
* h5py version: 2.7.1
* unimplemented test cases are marked in the table with an asterisk

| path                                      | file                                   | File Type    | NXentry Count | Application Def's |
| ----------------------------------------- | -------------------------------------- | ------------ | ------------- | ----------------- |
| `./ANSTO/hdf4`                            | `PLP0006018.nx.hdf`                    | HDF5         | 1             | None found        |
| `./APS/CCDImageServer/hdf4`               | `Smither400.3_apr0300051.hdf`          | HDF4         | *             | *                 |
| `./APS/CCDImageServer/hdf4`               | `Smither400.3_apr0300052.hdf`          | HDF4         | *             | *                 |
| `./APS/CCDImageServer/hdf4`               | `Smither400.3_apr0300053.hdf`          | HDF4         | *             | *                 |
| `./APS/CCDImageServer/hdf4`               | `Smither400.3_apr0300054.hdf`          | HDF4         | *             | *                 |
| `./APS/CCDImageServer/hdf4`               | `Smither400.3_apr0300055.hdf`          | HDF4         | *             | *                 |
| `./APS/CCDImageServer/hdf4`               | `recon_0123.hdf`                       | HDF4         | *             | *                 |
| `./APS/CCDImageServer/hdf4`               | `recon_0124.hdf`                       | HDF4         | *             | *                 |
| `./APS/CCDImageServer/hdf4`               | `recon_0125.hdf`                       | HDF4         | *             | *                 |
| `./APS/EPICSareaDetector/hdf5`            | `AgBehenate_228.hdf5`                  | HDF5         | 1             | error             |
| `./APS/NXsas/hdf5`                        | `nexus-example.hdf5`                   | HDF5         | 1             | error             |
| `./APS/other/hdf5`                        | `ID34_not_complete.h5`                 | HDF5         | 1             | None found        |
| `./APS/scan2nexus`                        | `14BMC_0015.mda`                       | unrecognised | -             | -                 |
| `./APS/scan2nexus`                        | `2iddf_0106.mda`                       | unrecognised | -             | -                 |
| `./APS/scan2nexus`                        | `README`                               | unrecognised | -             | -                 |
| `./APS/scan2nexus`                        | `mts_0347.mda`                         | unrecognised | -             | -                 |
| `./APS/scan2nexus`                        | `mts_0348.mda`                         | unrecognised | -             | -                 |
| `./APS/scan2nexus`                        | `sample.mda.text`                      | unrecognised | -             | -                 |
| `./APS/scan2nexus`                        | `sample1.mda`                          | unrecognised | -             | -                 |
| `./APS/scan2nexus/hdf4`                   | `14BMC_0015.nexus`                     | HDF4         | *             | *                 |
| `./APS/scan2nexus/hdf4`                   | `2iddf_0106.nexus`                     | unrecognised | -             | -                 |
| `./APS/scan2nexus/hdf4`                   | `mts_0347.nexus`                       | HDF4         | *             | *                 |
| `./APS/scan2nexus/hdf4`                   | `mts_0348.nexus`                       | HDF4         | *             | *                 |
| `./APS/scan2nexus/hdf4`                   | `sample1.nexus`                        | HDF4         | *             | *                 |
| `./APS/scan2nexus/xml`                    | `14BMC_0015.xml`                       | XML          | *             | *                 |
| `./APS/scan2nexus/xml`                    | `2iddf_0106.xml`                       | XML          | *             | *                 |
| `./APS/scan2nexus/xml`                    | `mts_0347.xml`                         | XML          | *             | *                 |
| `./APS/scan2nexus/xml`                    | `mts_0348.xml`                         | XML          | *             | *                 |
| `./APS/scan2nexus/xml`                    | `sample1.xml`                          | XML          | *             | *                 |
| `./APS/tomo/hdf4`                         | `Tomography_metadata.hdf`              | HDF4         | *             | *                 |
| `./APS/tomo/hdf4`                         | `Tomography_raw.hdf`                   | HDF4         | *             | *                 |
| `./DLS/NXquadric/hdf5`                    | `sample_capillary.nxs`                 | HDF5         | 1             | None found        |
| `./DLS/i03_i04_NXmx/hdf5`                 | `Therm_6_2.nxs`                        | HDF5         | 1             | error             |
| `./DLS/i16/hdf5`                          | `538039.nxs`                           | HDF5         | not NeXus     | -                 |
| `./DLS/i16/hdf5/538039-pilatus100k-files` | `538039.hdf`                           | HDF5         | 1             | None found        |
| `./DLS/p45/hdf5`                          | `p45-1168-mic.hdf5`                    | HDF5         | 1             | None found        |
| `./DLS/p45/hdf5`                          | `p45-1168.nxs`                         | HDF5         | 1             | None found        |
| `./DLS/p45/hdf5`                          | `p45-2194.nxs`                         | HDF5         | 1             | None found        |
| `./DLS/p45/hdf5`                          | `p45-316.nxs`                          | HDF5         | 1             | None found        |
| `./DLS/reflections/hdf5`                  | `thaumatin_integrated.nxs`             | HDF5         | 1             | error             |
| `./DLS/reflections/hdf5`                  | `thaumatin_integrated_multisample.nxs` | HDF5         | 1             | error             |
| `./IPNS/LRMECS/hdf4`                      | `lrcs3701.nxs`                         | unrecognised | -             | -                 |
| `./IPNS/LRMECS/hdf5`                      | `lrcs3701.nx5`                         | HDF5         | 2             | None found        |
| `./Soleil/hdf5`                           | `file_1.nxs`                           | HDF5         | 1             | error             |
| `./Soleil/hdf5`                           | `file_2.nxs`                           | HDF5         | 1             | error             |
| `./SwissFEL`                              | `README`                               | unrecognised | -             | -                 |
| `./SwissFEL/hdf5`                         | `lyso009a_0087.JF07T32V01_master.h5`   | HDF5         | 1             | error             |
| `./code/hdf4`                             | `NXtest.hdf`                           | HDF4         | *             | *                 |
| `./code/hdf4`                             | `dmc01.hdf`                            | HDF4         | *             | *                 |
| `./code/hdf4`                             | `dmc02.hdf`                            | HDF4         | *             | *                 |
| `./code/hdf5`                             | `NXtest.h5`                            | HDF5         | 2             | None found        |
| `./code/hdf5`                             | `dmc01.h5`                             | HDF5         | 1             | None found        |
| `./code/hdf5`                             | `dmc02.h5`                             | HDF5         | 1             | None found        |
| `./code/hdf5`                             | `focus2007n001335.hdf`                 | HDF5         | 1             | None found        |
| `./code/hdf5`                             | `sans2009n012333.hdf`                  | HDF5         | 1             | None found        |
| `./hdf5`                                  | `simple3D.h5`                          | HDF5         | 1             | None found        |
| `./hdf5`                                  | `writer_1_3.h5`                        | HDF5         | 1             | None found        |
| `./hdf5`                                  | `writer_1_3__niac2014.h5`              | HDF5         | 1             | None found        |
| `./nxpdb`                                 | `4n8z.cif`                             | unrecognised | -             | -                 |
| `./nxpdb`                                 | `4n8z.h5.cif`                          | unrecognised | -             | -                 |
| `./nxpdb/hdf5`                            | `4n8z.h5`                              | HDF5         | 1             | None found        |
| `./xml`                                   | `verysimple.xml`                       | XML          | *             | *                 |

