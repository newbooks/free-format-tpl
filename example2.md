# Using free format tpl to help making a parameter file

In this second part, we will complete the parameter file making for ligand 011.

1. Log on to hestia

2. Copy my template directory
  ```
  cp -r ~jmao/011_template ./011
  ```
  This will give you a directory with file run.prm, name.txt and partially done parameter directory param04.

3. Check name.txt, it should do a simple split of 011 to 11a and 11b.
Edit run.prm lines
  ```
  /home/jmao/ligand_example/extra.tpl                         (EXTRA)
  /home/jmao/ligand_example/name.txt MCCE renaming rule.      (RENAME_RULES)
  /home/jmao/ligand_example                                   (MCCE_HOME)
  ```
  to point to your working directory.

4. Download 011_ideal.pdb
```
wget http://ligand-expo.rcsb.org/reports/0/011/011_ideal.pdb
cp 011_ideal.pdb prot.pdb
```

5. Go to param04 directory, edit a new file 11b.ftpl, add a conformer list line to indicate this ligand has 3 conformer types on top of backbone. Backbone conformer has 0 atoms but it has to be listed, otherwise
```
cd param04
vi 11b.ftpl
```
```
CONFLIST, 11b: 11bBK, 11b01, 11b02, 11b-1
```

6. Refer to this diagram, make atom connectivity records:
![011 7-aminoheptanoic acid diagram](https://github.com/newbooks/free-format-tpl/raw/master/tpls/Capture.JPG)

7. Append protonated state 1 in 11b.ftpl, HXT on OXT:
```
CONNECT, " C4 ", 11b01: sp3, " HAB", "HABA", " ?  ", " C3 "
CONNECT, " HAB", 11b01: s, " C4 "
CONNECT, "HABA", 11b01: s, " C4 "
CONNECT, " C3 ", 11b01: sp3, " HAV", "HAVA", " C4 ", " C2 "
CONNECT, " HAV", 11b01: s, " C3 "
CONNECT, "HAVA", 11b01: s, " C3 "
CONNECT, " C2 ", 11b01: sp3, " HAX", "HAXA", " C3 ", " C1 "
CONNECT, " HAX", 11b01: s, " C2 "
CONNECT, "HAXA", 11b01: s, " C2 "
CONNECT, " C1 ", 11b01: sp2, " O  ", " OXT", " C2 "
CONNECT, " OXT", 11b01: sp3, " C1 ", " HXT"
CONNECT, " O  ", 11b01: sp2, " C2 "
CONNECT, " HXT", 11b01: s, " OXT"
```

8. Append protonated state 2 in 11b.ftpl, HXT on O:
```
CONNECT, " C4 ", 11b02: sp3, " HAB", "HABA", " ?  ", " C3 "
CONNECT, " HAB", 11b02: s, " C4 "
CONNECT, "HABA", 11b02: s, " C4 "
CONNECT, " C3 ", 11b02: sp3, " HAV", "HAVA", " C4 ", " C2 "
CONNECT, " HAV", 11b02: s, " C3 "
CONNECT, "HAVA", 11b02: s, " C3 "
CONNECT, " C2 ", 11b02: sp3, " HAX", "HAXA", " C3 ", " C1 "
CONNECT, " HAX", 11b02: s, " C2 "
CONNECT, "HAXA", 11b02: s, " C2 "
CONNECT, " C1 ", 11b02: sp2, " O  ", " OXT", " C2 "
CONNECT, " OXT", 11b02: sp3, " C1 "
CONNECT, " O  ", 11b02: sp2, " C2 ", " HXT"
CONNECT, " HXT", 11b02: s, " O  "
```

9. Append deprotonated state in 11b.ftpl:
```
CONNECT, " C4 ", 11b-1: sp3, " HAB", "HABA", " ?  ", " C3 "
CONNECT, " HAB", 11b-1: s, " C4 "
CONNECT, "HABA", 11b-1: s, " C4 "
CONNECT, " C3 ", 11b-1: sp3, " HAV", "HAVA", " C4  ", " C2 "
CONNECT, " HAV", 11b-1: s, " C3 "
CONNECT, "HAVA", 11b-1: s, " C3 "
CONNECT, " C2 ", 11b-1: sp3, " HAX", "HAXA", " C3  ", " C1 "
CONNECT, " HAX", 11b-1: s, " C2 "
CONNECT, "HAXA", 11b-1: s, " C2 "
CONNECT, " C1 ", 11b-1: sp2, " O  ", " OXT", " C2  "
CONNECT, " OXT", 11b-1: sp3, " C1 "
CONNECT, " O  ", 11b-1: sp2, " C2 "
```

10. Test this ftpl file:
```
tpl-free2mcce.py 11b.ftpl
```
  You should see a reasonable output in mcce tpl format on screen.

11. Continue to edit 11b.ftpl to include CHARGE
```
CHARGE, 11b01, " C4 ": -0.2
CHARGE, 11b01, " HAB":  0.1
CHARGE, 11b01, "HABA":  0.1
CHARGE, 11b01, " C3 ": -0.2
CHARGE, 11b01, " HAV":  0.1
CHARGE, 11b01, "HAVA":  0.1
CHARGE, 11b01, " C2 ": -0.2
CHARGE, 11b01, " HAX":  0.1
CHARGE, 11b01, "HAXA":  0.1
CHARGE, 11b01, " C1 ":  0.550
CHARGE, 11b01, " OXT": -0.495
CHARGE, 11b01, " O  ": -0.490
CHARGE, 11b01, " HXT":  0.435

CHARGE, 11b02, " C4 ": -0.2
CHARGE, 11b02, " HAB":  0.1
CHARGE, 11b02, "HABA":  0.1
CHARGE, 11b02, " C3 ": -0.2
CHARGE, 11b02, " HAV":  0.1
CHARGE, 11b02, "HAVA":  0.1
CHARGE, 11b02, " C2 ": -0.2
CHARGE, 11b02, " HAX":  0.1
CHARGE, 11b02, "HAXA":  0.1
CHARGE, 11b02, " C1 ":  0.550
CHARGE, 11b02, " OXT": -0.490
CHARGE, 11b02, " O  ": -0.495
CHARGE, 11b02, " HXT":  0.435

CHARGE, 11b-1, " C4 ": -0.2
CHARGE, 11b-1, " HAB":  0.1
CHARGE, 11b-1, "HABA":  0.1
CHARGE, 11b-1, " C3 ": -0.2
CHARGE, 11b-1, " HAV":  0.1
CHARGE, 11b-1, "HAVA":  0.1
CHARGE, 11b-1, " C2 ": -0.2
CHARGE, 11b-1, " HAX":  0.1
CHARGE, 11b-1, "HAXA":  0.1
CHARGE, 11b-1, " C1 ":  0.10
CHARGE, 11b-1, " OXT": -0.55
CHARGE, 11b-1, " O  ": -0.55
```

12. Append dielectric boundary radius. Since RADIUS is the same ragardless of conformer types in mcce, we only need to define one set.
```
RADIUS, 11b01, " C4 ": 2.0
RADIUS, 11b01, " C3 ": 2.0
RADIUS, 11b01, " C2 ": 2.0
RADIUS, 11b01, " C1 ": 1.7
RADIUS, 11b01, " OXT": 1.4
RADIUS, 11b01, " O  ": 1.4
RADIUS, 11b01, " HXT": 1.0
```

13. Complete vdw radius
```
vdw-complete.py 11b.ftpl > a

```
Check the difference:
```
diff 11b.ftpl a
```
If everything is ok, the difference is added vdw radius and enegy well depth, copy this file back to 11b.ftpl
```
cp a 11b.ftpl
```

14. Add conformer parameters, leave rxn as 0.
```
CONFORMER, 11b01: Em0=   0.0, pKa0=  0.0, ne= 0, nH=  0, rxn= 0
CONFORMER, 11b02: Em0=   0.0, pKa0=  0.0, ne= 0, nH=  0, rxn= 0
CONFORMER, 11b-1: Em0=   0.0, pKa0=  4.5, ne= 0, nH= -1, rxn= 0
```

15. Run convert program:
```
tpl-free2mcce.py 11b.ftpl > 11b.tpl
```

16. Now it is ready to run mcce step 1, 2, 3 to get reference rxn, go to working directory above param04, and run
```
mcce
```
You should get head3.lst

17. Copy the dsolv in head3.lst term as rxn in 011.ftpl, convert to tpl and run mcce again.
```
vi 011.ftpl
```
```
tpl-free2mcce.py param04/11b.ftpl > param04/11b.tpl
```
```
mcce
```
The dsolv in head3.lst should be cloase to 0.

18. Titration, mcce step 4. Turn off step 1,2,3 and turn on step 4 in run.prm. Run mcce.

19. Check pK.out, you will see the amino group and carboxyl group do not interact much. Their pKas are close to their solution pKa.
