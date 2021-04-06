**The following is output from running nxvalidate against the resulting hdf file for each generated ex_h5py_DEFINITION.py script**
```
NXarchive.h5 passed validation
NXarpes.h5 passed validation
definition=NXcanSAS.nxdl.xml message="Required group missing" nxdlPath=/NXentry/NXdata sev=error dataPath=/entry dataFile=NXcanSAS.h5
1 errors and 9 warnings found when validating NXcanSAS.h5
NXdirecttof.h5 passed validation
NXfluo.h5 passed validation
NXindirecttof.h5 passed validation
NXiqproc.h5 passed validation
NXlauetof.h5 passed validation
NXmonopd.h5 passed validation
definition=NXmx.nxdl.xml message="Cannot even find the starting point of the depends_on chain, SAMPLE-CHAR-DATA" nxdlPath=/NXentry/NXsample/name sev=error dataPath=/entry/sample/depends_on dataFile=NXmx.h5
definition=NXmx.nxdl.xml message="Cannot even find the starting point of the depends_on chain, SAMPLE-CHAR-DATA" nxdlPath=/NXentry/NXinstrument/NXdetector sev=error dataPath=/entry/instrument/detector/depends_on dataFile=NXmx.h5
2 errors and 16 warnings found when validating NXmx.h5
NXrefscan.h5 passed validation
NXreftof.h5 passed validation
NXsas.h5 passed validation
NXsastof.h5 passed validation
NXscan.h5 passed validation
NXspe.h5 passed validation
NXsqom.h5 passed validation
NXstxm.h5 passed validation
definition=NXtas.nxdl.xml message="Link target /entry/instrument/analyzer/ef is invalid" nxdlPath=/NXentry/NXdata/ef dataPath=/entry/data/ef sev=error dataFile=NXtas.h5
1 errors and 18 warnings found when validating NXtas.h5
NXtofnpd.h5 passed validation
NXtofraw.h5 passed validation
NXtofsingle.h5 passed validation
NXtomo.h5 passed validation
NXtomophase.h5 passed validation
NXtomoproc.h5 passed validation
NXxas.h5 passed validation
NXxasproc.h5 passed validation
NXxbase.h5 passed validation
NXxeuler.h5 passed validation
NXxkappa.h5 passed validation
NXxlaue.h5 passed validation
NXxlaueplate.h5 passed validation
NXxnb.h5 passed validation
NXxrot.h5 passed validation

```
