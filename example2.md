# Using free format tpl to help making a parameter file

In this second part, we will complete the parameter file making for ligand 011.

1. Log on to hestia

2. Copy my template directory
  ```
  cp -r ~jmao/011_template ./011
  ```
  This will give you a directory with file run.prm, name.txt and partially done parameter directory param04.
  
3. Check name.txt, it should do a simple split of 011 to 11a and 11b. Edit run.prm line
  ```
  /home/jmao/ligand_example                                          (MCCE_HOME)
  ```
  to point to your working directory.
  
4. Download 011_ideal.pdb
```
wget http://ligand-expo.rcsb.org/reports/0/011/011_ideal.pdb
```

5. Go to param04 directory, edit a new file 11b.ftpl, add a conformer list line to indicate this ligand has 3 conformer types on top of backbone. Backbone conformer has 0 atoms but it has to be listed, otherwise    
```
cd param04
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
CONNECT, " C3 ", 11b01: sp3, " HAV", "HAVA", " C4  ", " C2 "
CONNECT, " HAV", 11b01: s, " C3 "
CONNECT, "HAVA", 11b01: s, " C3 "
CONNECT, " C2 ", 11b01: sp3, " HAX", "HAXA", " C3  ", " C1 "
CONNECT, " HAX", 11b01: s, " C2 "
CONNECT, "HAXA", 11b01: s, " C2 "
CONNECT, " C1 ", 11b01: sp2, " O  ", " OXT", " C2  "
CONNECT, " OXT", 11b01: sp3, " C1 ", " HXT"
CONNECT, " O  ", 11b01: sp2, " C2 "
CONNECT, " HXT", 11b01: s, " OXT"
```

8. Append protonated state 2 in 11b.ftpl, HXT on O:
```
CONNECT, " C4 ", 11b02: sp3, " HAB", "HABA", " ?  ", " C3 "
CONNECT, " HAB", 11b02: s, " C4 "
CONNECT, "HABA", 11b02: s, " C4 "
CONNECT, " C3 ", 11b02: sp3, " HAV", "HAVA", " C4  ", " C2 "
CONNECT, " HAV", 11b02: s, " C3 "
CONNECT, "HAVA", 11b02: s, " C3 "
CONNECT, " C2 ", 11b02: sp3, " HAX", "HAXA", " C3  ", " C1 "
CONNECT, " HAX", 11b02: s, " C2 "
CONNECT, "HAXA", 11b02: s, " C2 "
CONNECT, " C1 ", 11b02: sp2, " O  ", " OXT", " C2  "
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
