# Example of changing H name to observe new PDB rules

## Hydrogen naming in PDB 3.0 format
In the past, hydrogen atom in ATOM or HETATM is from column 13 to 16 and H is always on column 14.  However, hydrogen atom name rule in PDB 3.0 format has changed. If the name of a hydrogen has four characters, it is left-justified starting in column 13; if it has fewer than four characters, it is left-justified starting in column 14. Therefore, if we want to use the H coordinates, we need to prepare tpl files that use the new H naming rules.

## Convert the H names
In this example, we will prepare a new tpl with the H records observing PDB 3.0 format.

Convert to free format

   ```tpl-mcce2free.py tpls/glu.tpl > tmpfile```

Complete radius parameters

   ```bin/vdw-complete.py tmpfile > glu.ftpl```

Identify H names that need to be updated:

```
"1HB " to " HB1"
"2HB " to " HB2"
"1HG " to " HG1"
"2HG " to " HG2"
```
Replace the names:

```
sed -i 's/"1HB "/" HB1"/g' glu.ftpl 
sed -i 's/"2HB "/" HB2"/g' glu.ftpl 
sed -i 's/"1HG "/" HG1"/g' glu.ftpl 
sed -i 's/"2HG "/" HG2"/g' glu.ftpl 
```

Convert free format to mcce format:

```tpl-free2mcce.py glu.ftpl```

The advantage of updating H names through free format tpl is minimizing mistakes. The program checks the name consistency and writes out a strict format tpl file avoiding human mistakes. 