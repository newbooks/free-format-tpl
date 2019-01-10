# Free Format TPL files

MCCE depends on very strict parameter files. Prepaation of the parameter files can be daunting. This free format tpl file format is to relax the strict rules previously seen in [MCCE](https://github.com/GunnerLab/mcce-develop)

This project defines the free format tpl rules. It contains tools to make new tpl file from scratch, and to convert the free format and mcce format back and forth.

The format of this tple file is simple. It is simply a key value pair separated by ":". Key can be up to three fields, separated by ",". Value is a string, and will be interprated by the mcce program based on the key. If space is a part of the key of value strings, it must ne quoted inside double quotes. ":" and "," are reserved, and can not be used in key and value. The following is an example:

```CONNECT, " N  ", GLUBK: sp2, " ?  ", " CA ", " H  "```

MCCE reads in lines from tpl files and save them in the same database. Therefore a tpl file can define more than one residue, and lines of one residue can be in multiple files.

If the same key appears more than one time, the values are appended to be the earlier value of the same key. Look at this example:

```
ROTATE, GLU: " CA " - " CB "
ROTATE, GLU: " CB " - " CG "
ROTATE, GLU: " CG " - " CD "
```

is equal to:

```ROTATE, GLU: " CA " - " CB ", " CB " - " CG ", " CG " - " CD "```



## How to convert mcce tple file to free format:
Run this command to convert mcce format to free format.
>bin/tpl-mcce2free.py tpls/glu.tpl > tpls/glu.ftpl 

Run this command to complete VDW parameters of RADIUS records.
>bin/vdw-complete.py tpls/glu.ftpl > tmpfile

>mv tmpfile tpls/glu.ftpl


## How to convert free format tpl file to mcce format:
Run this command to convert free format to mcce format.
>bin/tpl-free2mcce.py tpls/glu.ftpl


## How to prepare a free format TPL file from a molecule PDB file
1. Start from a pdb file, run script ... to convert it to initial tpl file. The ideal pdbs of most residues and ligands
can be found at http://ligand-expo.rcsb.org/
2. Identify backbone. Atoms that do not change position and charge are backbone atoms.
3. Identify side chain with conformational changes. Atoms other than backbone are side chain atoms. They
change position or charge in mcce simulation. For amino acids, side chain atoms are atoms other than
N, C, CA, and O, even though they do not change positions or charges.
4. The ele radii are used for defining dielectric boundary. For this purpose, we can simply use atom covalent radii or ion radii. Sometimes, it is acceptable approximation to group H atom into its bonded heavy atom. For example, we can set H radius to be 0 and C to be 2.0 for molecule CH3-CH2-CH3.
5. vdw radius and e depth are equivalent parameters of AB form Lennard Jones potential calculation. Refer to
http://ambermd.org/Questions/vdwequation.pdf for details. Program vadparam.py converts AB form to radius and e depth form.
6. CONNECT records define bonds. Use ? for connection to an atom outside residue
7. ROTATE records define rotational axis, which is normally a sigle bond.
8. PKA, EM, NETCHARGE and RXN are conformer electrostatic properties.


## Short tutorials
[Change H name to observe new PDB ATOM rules](https://github.com/newbooks/free-format-tpl/blob/master/example1.md)

[Make parameter file through free format tpl](https://github.com/newbooks/free-format-tpl/blob/master/example2.md)

Make a new tpl file from Amber parameters
