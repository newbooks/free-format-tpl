# Free Format TPL files
The strict format of parameter files are prone to errors and discrepancies. This project develops a new parameter
format and utilities to make new tpl file from a molecule, and convert the free format and mcce format back and forth.

# How to prepare a free format TPL file from a molecule PDB file
1. Start from a pdb file, run script ... to convert it to initial tpl file. The ideal pdbs of most residues and ligands
can be found at http://ligand-expo.rcsb.org/
2. Identify backbone. Atoms that do not change position and charge are backbone atoms.
3. Identify side chain with conformational changes. Atoms other than backbone are side chain atoms. They
change position or charge in mcce simulation. For amino acids, side chain atoms are atoms other than
N, C, CA, and O, even though they do not change positions or charges.
4. The ele radii are used for defining dielectric boundary. Use covalent radii or ion radii based on the atom
electron state. For CHn groups, assign group radius to C and 0 to H for simplicity.
5. vdw radius and e depth are equivalent parameters of AB form Lennard Jones potential calculation. Refer to
http://ambermd.org/Questions/vdwequation.pdf for details.
6. CONNECT records define bonds. Use -1 for bond to atom in previous residue, +1 for next residue, ? for uncertain
residue
7. ROTATE records define rotational freedom.
8. PKA, EM, NETCHARGE and RXN are conformer electrostatic properties.

# How to convert free format tpl file to mcce format and vice versa.
1. Run tpl-free2mcce.py filename to convert free format to mcce format.
2. Run tpl-mcce2free.py filename to convert mcce format to free format.
