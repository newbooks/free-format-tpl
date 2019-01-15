#!/usr/bin/env python
"""
Cut the models from NMR structure
"""

import sys

pdbname = sys.argv[1]
iextension = pdbname.lower().find(".pdb")
if iextension > 0:
    pdbid = pdbname[:iextension]
else:
    pdbid = pdbname

lines = open(pdbname).readlines()

inmodel = False
exitmodel = False
for line in lines:
    fields = line.strip().split()
    if fields[0] == "MODEL":
        modelid = fields[1]
        inmodel = True
        exitmodel = False
        modellines = []
        continue
    elif fields[0] == "ENDMDL":
        inmodel = False
        exitmodel = True

    if inmodel:
        modellines.append(line)
    elif exitmodel:
        newfile = "%s.%s.pdb" % (pdbid, modelid)
        open(newfile, "w").writelines(modellines)
