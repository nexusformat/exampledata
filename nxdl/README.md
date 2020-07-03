# Nxdl exampledata

The intention of _**nxdl_to_hdf5.py**_ is to create hdf5 files from the nxdl.xml 
files, currently only `applications` and some `contributed_definitions` are 
supported as the code depends on the existance of an **NXentry** in the definition.

After several iterations the final approach taken with the task was to walk the XML file and build
a master dictionary separated into the different XML tags (group, field, link, attribute etc) then
create the file with this dict in a controlled order, this made it much easier to debug and section off where errors
were during the process.  

The current limitations of auto generation of the files is mainly due to the syntax 
involved in specifying link targets. Where no `name`
attribute is given for a group or field the `type` will be used, if a `name` 
attribute it used in an application definition the exact case sensitive name is 
required. Link targets however can use either the name of the field or group 
but also the type, and sometimes both at the same time as in the case of NXtomo
`/NXentry/NXinstrument/detector:NXdetector/data`. 
Cnxvalidate checks the string of the link target specified against what it finds in the 
file, so as a result most if not all of the link targets in the generated files will produce 
`Required link missing or not pointing to an HDF5 object` errors from nxvalidate. If the link 
target syntax was to specifiy exactly what the definition had defined the links would be correct and 
pass validation. 

**Arguments and Usage:**
```     
>python nxdl_to_hdf5.py --help
    usage: nxdl_to_hdf5.py [-h] [-f FILE | -d DIRECTORY]
                       [-s [SYMBOLS [SYMBOLS ...]]] [--nxdefdir NXDEFDIR] [-r]

    This is a script to generate hdf5 files from nxdl.xml definitions

    optional arguments:
      -h, --help            show this help message and exit
      -f FILE, --file FILE  The definition file to generate. ex: python
                            nxdl_to_hdf5.py --f NXstxm
      -d DIRECTORY, --directory DIRECTORY
                            generate all definitions in this directory one of
                            either ['applications', 'contributed_definitions'],
                            ex: applications
      -s [SYMBOLS [SYMBOLS ...]], --symbols [SYMBOLS [SYMBOLS ...]]
                            pass comma delimited set of key value pairs for each
                            desired symbol ex: python nxdl_to_hdf5.py --f NXstxm
                            --s numP=24, numE=1, numY=10, numX=10
      --nxdefdir NXDEFDIR   Specify an alternative location to the NXDL
                            definitions base directory (where nexpy is installed)
      -r, --report          Report on the Symbols that this definition uses
```


    
&nbsp;&nbsp;&nbsp;**-f  FILENAME**  To generate a single definition file pass the name of it.
   ```
    >python nxdl_to_hdf5.py -f NXiqproc
   ```

&nbsp;&nbsp;&nbsp;**-d DIRECTORY**  To generate all the definitions in one of the applications or contributed_definitions
        pass the name.
   ```
    >python nxdl_to_hdf5.py -d applications
   ```

&nbsp;&nbsp;&nbsp;**-s [SYMBOLS [SYMBOLS ...]]**  To define a pass symbols to be used during generation
    If the definition uses symbols inside but does not specify any in a `Symbols` table then each undefined symbol
    will be set to the value 1. If you want to generate a file using certain values for the symbols you can pass them in:
  ```
  >python nxdl_to_hdf5.py -f NXiqproc -s NE=5, NQX=3, NQY=3
    Process this specific definition [NXiqproc]
	Process using the following symbols [['NE=5,', 'NQX=3,', 'NQY=3']]

Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXiqproc.nxdl.xml]
	exporting: [NXiqproc]
finished exporting to [G:\tst_nexus\exampledata\nxdl\applications\NXiqproc.hdf5]
  ```
  
&nbsp;&nbsp;&nbsp;**--nxdefdir NXDEFDIR**  If you want to specify a different location than the standard _nexusformat/definitions_ 
    you can pass it in.
   ```
    >python nxdl_to_hdf5.py -nxdefdir /home/bergr/testing/nexusformat/definitions
   ```

&nbsp;&nbsp;&nbsp;**-r, --report** To report the names the specified definition is using.
  ```
    >python -f NXiqproc -r
    Processing [C:/controls/test/nexusformat/exampledata\..\definitions\applications\NXiqproc.nxdl.xml]
	exporting: [NXiqproc]
	-Symbol Warning: the symbol [NE] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [NQX] is being used but has not been defined in the Symbols table, setting to default value of 1
	-Symbol Warning: the symbol [NQY] is being used but has not been defined in the Symbols table, setting to default value of 1
  ```

[nxdl_to_hdf5_output](nxdl_to_hdf5_output.md) is the output of running nxdl_to_hdf5.py to generate all definitions in `applications`

[nxdl_validate_out](nxdl_validate_out.md) is the output of running **nxvalidate** against each generated file

