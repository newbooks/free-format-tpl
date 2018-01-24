#!/usr/bin/python
"""Convert mcce format tpl to free format."""

import sys

mccedb = {}  # parameter database in mcce format
freedb = {}  # parameter database in free format


def atom_consistency(conf):
    passed = False
    natom = int(mccedb["NATOM", conf, "    "])
    for i in range(natom):
        try:
            key = ("ATOMNAME", conf, "%4d" % i)
            atomname = mccedb[key][:4]
        except:
            print "Error in fetching number %d atom for conformer %s" % (i, conf)
            return passed
        try:
            key = ("IATOM", conf, atomname)
            iatom = int(mccedb[key].strip())
        except:
            print "Error in finding index for atom \"%s\" of conformer %s" % (atomname, conf)
            return passed
        if iatom == i:
            passed = True

    return passed


if __name__ == "__main__":
    filename = sys.argv[1]
    lines = open(filename).readlines()
    for line in lines:
        end = line.find("#")
        line = line[:end]
        if len(line) < 20:
            continue
        key1 = line[:9].strip()
        key2 = line[9:15].strip()
        key3 = line[15:19]
        value = line[20:]
        mccedb[(key1, key2, key3)] = value

    # Collect all conformer names from the read file
    conformers = []
    for k in mccedb.keys():
        if k[0] == "CONFLIST":
            conformers += mccedb[k].split()
    print "Detected these conformers: [%s]" % ', '.join(map(str, conformers))
    # check consistency between ATOMNAME and IATOM
    for conf in conformers:
        if atom_consistency(conf):      # pased
            print "Consistency test passed for ATOM records of conformer %s." % conf
        else:
            print "There are discrepencies in ATOM records of conformer %s shown above." % conf


