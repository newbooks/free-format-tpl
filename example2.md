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

5. Edit a new file 11b.ftpl, add a conformer list line to indicate this ligand has 3 conformer types on top of backbone. Backbone conformer has 0 atoms but it has to be listed, otherwise    
```
CONFLIST, 11b: 11bBK, 11b01, 11b02, 11b-1
```

6. Refer to this diagram, make atom connectivity records:
![011 7-aminoheptanoic acid diagram](https://github.com/newbooks/free-format-tpl/raw/master/tpls/Capture.JPG)
  
7. Append protonated state 1 in 11b.ftpl, HXT on OXT:
```

```

8. Append protonated state 2 in 11b.ftpl, HXT on O:
```

```
