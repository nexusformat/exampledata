Dataset was indexed and integrated using these commands:

dials.import ../data
dials.find_spots imported.expt nproc=64
dials.index strong.refl imported.expt
dials.refine_bravais_settings indexed.expt indexed.refl
dials.refine bravais_setting_9.expt indexed.refl
dials.refine refined.expt refined.refl scan_varying=true
dials.integrate refined.* nproc=64

Then, 10 reflections were saved using this python code:

$ python libtbx.python make_10.py integrated.refl

Where make_10.py:
from dials.array_family import flex
import sys, os
fn = sys.argv[1]
refls = flex.reflection_table.from_file(fn)

print("Loaded %d refls", len(refls))
refls = refls[0:10]

print("Filtered to first %d refls", len(refls))

outname = os.path.splitext(fn)[0] + "_ten.refl"

print("Saving as %s"%outname)

refls.as_file(outname)

Finally, the reflections were converted to NeXus/NXreflections using:
dials.export format=nxs integrated.expt integrated_ten.refl

And renamed to thaumatin_integrated.nxs


For the multi experiment file, these commands were used:
cp integrated_ten.refl ten_1.refl
cp ten_1.refl ten_2.refl
cp integrated.expt integrated_1.expt
cp integrated_1.expt integrated_2.expt
dials.assign_experiment_identifiers integrated_1.expt ten_1.refl identifiers=ten1 output.experiments=integrated_1.expt output.reflections=ten_1.refl
dials.assign_experiment_identifiers integrated_2.expt ten_2.refl identifiers=ten2 output.experiments=integrated_2.expt output.reflections=ten_2.refl
dials.combine_experiments *
dials.export format=nxs combined.*
