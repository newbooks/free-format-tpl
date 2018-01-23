#!/usr/bin/python
"""Convert mcce format tpl to free format."""

import sys

mccedb = {}  # parameter database in mcce format
freedb = {}  # parameter database in free format

if __name__ == "__main__":
    file = sys.argv[1]
    lines = open(file).readlines()
    for line in lines:
        end = line.find("#")
        line = line[:end]
        if len(line) < 20: continue
        fields = line[:20].split()
        key1 = fields[0]
        if len(fields) > 1:
            key2 = fields[1]
        else:
            key2 = ""
        if len(fields) > 2:
            key3 = fields[2]
        else:
            key3 = ""

        value = line[20:].strip()
        mccedb[(key1,key2,key3)] = value

    # check consistency between ATOMNAME and IATOM
    conformers = []
    for k in mccedb.keys():
        if k[0] == "CONFLIST":
            conformers += mccedb[k].split()



    print conformers

