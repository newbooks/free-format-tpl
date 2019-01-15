# Example of changing H name to observe new PDB rules

## Hydrogen naming in PDB 3.0 format
In the past, hydrogen atom in ATOM or HETATM is from column 13 to 16 and H is always on column 14.  However, hydrogen atom name rule in PDB 3.0 format has changed. If the name of a hydrogen has four characters, it is left-justified starting in column 13; if it has fewer than four characters, it is left-justified starting in column 14. Therefore, if we want to use the H coordinates, we need to prepare tpl files that use the new H naming rules.

## Convert the H names
In this example, we will prepare a new tpl with the H records observing PDB 3.0 format.

Get the free-format-tpl package from guthub
    ```git clone https://github.com/newbooks/free-format-tpl.git free-format-tpl

###Prepare a test directory:
    ```mkdir test```
    ```cd test```
    ```mkdir param04```
    ```cp ~mcce/mcce-develop/param04/00always_needed.tpl ./param04/```
    ```cp ../tpls/glu.tpl ./param04```
    ```cp ~mcce/mcce-develop/run.prm.quick ./run.prm```
    ```wget http://ligand-expo.rcsb.org/reports/G/GLU/GLU_ideal.pdb```
    ```cp GLU_ideal.pdb prot.pdb```

Edit run.prm to:
1. run step 1 to 4
2. set MCCE_HOME to ./
3. set TERMINALS to f

Edit prot.pdb to:
1. remove HTX, OXT, H2 atoms from the file as they are on terminal residue.
2. remove HE2 as this atom exists on only one of three conformers

Run mcce, and you will see the error of atom names.
    ```cd test```
    ```mcce```

###Convert to free format

   ```../bin/tpl-mcce2free.py param04/glu.tpl > tmpfile```

Review tmpfile, you will see RADIUS have missing fields. This is because we are going to VDW atom radius instead of 
C6 and C12 parameters. If we are to convert it back to mcce tpl file, we can leave them alone. Otherwise, 
we can complete them with C6, C12 parameters in amble.tpl. 

Complete radius parameters

   ```../bin/vdw-complete.py tmpfile > glu.ftpl```

Identify H names that need to be updated:

```
"1HB " to " HB1"
"2HB " to " HB2"
"1HG " to " HG1"
"2HG " to " HG2"
```
Replace the names:

```
sed -i 's/"1HB "/" HB2"/g' glu.ftpl 
sed -i 's/"2HB "/" HB3"/g' glu.ftpl 
sed -i 's/"1HG "/" HG2"/g' glu.ftpl 
sed -i 's/"2HG "/" HG3"/g' glu.ftpl 
```

Convert free format to mcce format:

```../bin/tpl-free2mcce.py glu.ftpl > param04/glu.tpl```

The advantage of updating H names through free format tpl is minimizing mistakes. The program checks the name consistency and writes out a strict format tpl file avoiding human mistakes. 