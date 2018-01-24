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
            atomname = "{:<4}".format(mccedb[key][:4])
        except:
            print "Error in fetching number %d atom. Check ATOMNAME record of conformer %s" % (i, conf)
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


def make_atom(conf):
    natom = int(mccedb["NATOM", conf, "    "])
    for i in range(natom):
        key = ("ATOMNAME", conf, "%4d" % i)
        atomname = "{:<4}".format(mccedb[key][:4])
        key = ("CONNECT", conf, atomname)
        connect = mccedb(key)
        print connect
    return


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
            print "There are discrepancies in ATOM records of conformer %s shown above." % conf

    # Make conflist
    tplout = []
    residue_names = [x[:3] for x in conformers]
    residues = list(set(residue_names))
    for residue in residues:
        line = "CONFLIST, %s: " % residue
        conflist = []
        for conf in conformers:
            if conf[:3] == residue:
                conflist.append(conf)
        line += ", ".join(conflist)
        line += "\n"
        tplout.append(line)

    # Make atom records
    for conf in conformers:
        make_atom(conf)



    sys.stdout.writelines(tplout)
