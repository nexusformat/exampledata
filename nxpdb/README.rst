As per NIAC 2018, this directory contains examples of the use of
the NXpdb base class.

4n8z.cif  4n8z.h5  4n8z.h5.cif

These files show the cycle of operation of translating from Protein
Data Bank mmcif format to a NeXus/HDF5 transliteration and back
to Protein Data Bank mmcif format using the cycle of CBFlib cif2cbf
commands:

        bin/cif2cbf -5wn --nxpdb -i 4n8z.cif -o 4n8z.h5
 
        bin/cif2cbf -W  -5rn --nxpdb -i 4n8z.h5 -o 4n8z.h5.cif 

where the first command reads pdb entry 4n8z.cif [Xingyu Yin,  Alexander 
Scalia, Ludmila Leroy, Christina M. Cuttitta, Gina M. Polizzo, Daniel L. 
Ericson, Christian G. Roessler, Olven Campos, Millie Y. Ma, Rakhi Agarwal,
Rick Jackimowicz, Marc Allaire, Allen M. Orville, Robert M. Sweet and 
Alexei S. Soares,  "Hitting the target: fragment screening with acoustic 
in situ co‐crystallization of proteins plus fragment libraries on pin‐
mounted data‐collection micromeshes." Acta Crystallogr. D 70, no. 5 (2014):
1177 -- 1189].  The resulting file, 4n8z.h5 is an NXpdb compliant NeXus/HDF5
file containing a transliteration of the mmCIF file.  The second command,
tranliterates 4n8z.h5 back into an mmCIF file 4n8z.h5.cif.

Note that mmCIF is order independent and the orderings of 4n8z.cif and
4n8z.h5.cif are very different.


    -- H. J. Bernstein
       28 Octiber 2018 
