#!/usr/bin/python
"""Convert free format tpl to mcce format."""

import sys

mccedb = {}  # parameter database in mcce format
freedb = {}  # parameter database in free format

def residues_in_db():
    residues = []
    for key in freedb.keys():
        if key[0] == "CONFLIST" and key[1] not in residues:
            residues.append(key[1])
    return residues


if __name__ == "__main__":
    filename = sys.argv[1]
    lines = open(filename).readlines()
    for line in lines:
        end = line.find("#")
        line = line[:end]
        fields = line.split(":")
        if len(fields) != 2: continue

        key_string = fields[0].strip()
        keys = key_string.split(",")
        key1 = keys[0].strip().strip("\"")
        if len(keys) > 1:
            key2 = keys[1].strip().strip("\"")
        else:
            key2 = ""
        if len(keys) > 2:
            key3 = keys[2].strip().strip("\"")
        else:
            key3 = ""

        value_string = fields[1].strip()

        freedb[(key1, key2, key3)] = value_string

    # check if this database contains only one residue
    residues = residues_in_db()
    if len(residues) > 1:
        print "Multiple residues detected: %s" % ",".join(residues)
        sys.exit()

    residue = residues[0]

    nlines = []

    # CONFLIST
    fields = freedb["CONFLIST", residue, ""].split(",")
    conformers = []
    for field in fields:
        conf = field.strip()
        if len(conf) >= 1:
            conformers.append("%5s" % conf)
    key = "CONFLIST %3s        " % (residue)
    value = " ".join(conformers)
    line = "%s%s\n" %(key, value)
    nlines.append(line)

    # NATOMS, IATOM, ATOMNAME, CONNECT
    natoms = []
    iatom = []
    atomname = []
    connect = []
    for key in freedb.keys():
        if key[0] == "CONNECT":
            atomname = key[1]
            conf = key[2]





    sys.stdout.writelines(nlines)


