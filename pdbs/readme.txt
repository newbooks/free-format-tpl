This directory hosts the input pdb file as start point for making initial tpl file.

The ideal pdbs of most residues and ligands can be found at
http://ligand-expo.rcsb.org/

I use experimental model coordinates to make tpl and calculate charges.

Procedure:
1. Prepare a model pdb file. Alter the CONECT record to reflect proper out of molecule connectivity, -1 for previous
molecule, +1 for the next molecule, ? for undetermined. This includes
removing OXT and HXT for amino acids.