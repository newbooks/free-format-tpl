# Free Format TPL files
The strict format of parameter files are prone to errors and discrepancies. This project develops a new parameter
format and offers an option to compile to old tpl file for compatibility.

# How to prepare a new TPL file
1. Start from a pdb file, run script ... to convert it to initial tpl file. The ideal pdbs of most residues and ligands can be found at
http://ligand-expo.rcsb.org/
2. Identify which atoms do not change position and charge. These are backbone atoms.
3. Identify side chain atoms. These change position or charge. For amino acids, side chain atoms are separated to make
consistent backbone atoms, even though they do not change positions or charges.
4. The ele_radii are used for defining dielectric boundary. Use covalent radii or ion radii based on the atom
electron state. For CHn groups, assign group radius to C and 0 to H for simplicity.
5. vdw_radius and e_depth are equivalent parameters of AB form Lennard Jones potential calculation. Refer to
http://ambermd.org/Questions/vdwequation.pdf
6. CONNECT records define bonds. Use -1 for bond to atom in previous residue, +1 for next residue, ? for uncertain
residue
7.