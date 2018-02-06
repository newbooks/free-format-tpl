#!/usr/bin/python
"""Convert free format tpl to mcce format."""

import sys

mccedb = {}  # parameter database in mcce format
freedb = {}  # parameter database in free format

peptide = {" N  ": (-1, " C  "),
           " C  ": (1,  " N  ")}

disulfur = ["CYD01"]

def residues_in_db():
    residues = []
    for key in freedb.keys():
        if key[0] == "CONFLIST" and key[1] not in residues:
            residues.append(key[1])
    return residues


def create_connect(key, value):
    atom = key[1]
    conf = key[2]
    fields = value.strip().split(",")
    orbital = fields[0]
    connected = [x.strip().strip("\"") for x in fields[1:]]

    nvalue = []
    for x in connected:
        if x == " ?  ":
            if atom in peptide:
                offset = "%-3d" % peptide[atom][0]
                connected_atom = peptide[atom][1]
            else:
                offset = "LIG"
                connected_atom = " ?  "
        else:
            offset = "0  "
            connected_atom = x
        if conf in disulfur and x == " SG ":
            offset = "LIG"
            connected_atom = " SG "


        nvalue.append("%s  %s" % (offset, connected_atom))

    nvalue_str = " ".join(nvalue)
    line = "CONNECT  %5s %4s %-5s     %s\n" % (conf, atom, orbital, nvalue_str)

    return line

if __name__ == "__main__":
    filename = sys.argv[1]
    lines = open(filename).readlines()

    natoms = {}
    iatom = []
    atomname = []
    i_counter = {}
    connect = []
    em0_records = []
    pka0_records = []
    ne_records = []
    nh_records = []
    rxn_records = []

    for line in lines:
        end = line.find("#")
        line = line[:end]
        fields = line.split(":")
        if len(fields) != 2:
            continue

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

        # make CONNECT on the go so CONNECT keeps the same order
        if key1 == "CONNECT":
            atom = key2
            conf = key3

            # CONNECT
            nline = create_connect((key1, key2, key3), value_string)
            connect.append(nline)

            # IATOM
            if conf in natoms:
                natoms[conf] += 1
            else:
                natoms[conf] = 1
            nline = "IATOM    %5s %4s %-3d\n" % (conf, atom, natoms[conf]-1)
            iatom.append(nline)

            # ATOMNAME
            nline = "ATOMNAME %5s  %3d %s\n" % (conf, natoms[conf]-1, atom)
            atomname.append(nline)

        elif key1 == "CONFORMER":
            conf = key2
            fields = [x.strip() for x in value_string.split(",")]
            for field in fields:
                subfields = [x.strip() for x in field.split("=")]
                if subfields[0].upper() == "EM0":
                    em0 = float(subfields[1])
                elif subfields[0].upper() == "PKA0":
                    pka0 = float(subfields[1])
                elif subfields[0].upper() == "NE":
                    ne = int(subfields[1])
                elif subfields[0].upper() == "NH":
                    nh = int(subfields[1])
                elif subfields[0].upper() == "RXN":
                    rxn = float(subfields[1])
            em0_records.append( "EM       %5s      %-.2f\n" % (conf, em0))
            pka0_records.append("PKA      %5s      %-.2f\n" % (conf, pka0))
            ne_records.append("ELECTRON %5s      %-2d\n" % (conf, ne))
            nh_records.append("PROTON   %5s      %-2d\n" % (conf, nh))
            rxn_records.append("RXN      %5s      %-.2f\n" % (conf, rxn))

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

    natom_records = []
    for conf in conformers:
        natom_records .append("NATOM    %5s      %-3d\n" % (conf, natoms[conf]))

    # atom records
    nlines.append("\n")
    nlines += natom_records
    nlines.append("\n")
    nlines += iatom
    nlines.append("\n")
    nlines += atomname
    nlines.append("\n")
    nlines += connect

    # conformer
    nlines.append("\n")
    nlines += nh_records
    nlines += pka0_records
    nlines += ne_records
    nlines += em0_records
    nlines += rxn_records





    sys.stdout.writelines(nlines)


