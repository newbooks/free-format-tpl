# Using free format tpl to help making a parameter file

In this second part, we will complete the parameter file making for ligand 011.

- Log on to hestia
- Copy my template directory
  ```
  cp -r ~jmao/011_template ./011
  ```
  This will give you a directory with file run.prm, name.txt and partially done parameter directory param04
- Check name.txt, it should do a simple split of 011 to 11a and 11b. Edit run.prm line
  ```
  /home/jmao/ligand_example                                          (MCCE_HOME)
  ```
  to point to your working directory
  
