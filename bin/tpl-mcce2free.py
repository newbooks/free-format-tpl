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
    lines = []
    for i in range(natom):
        key = ("ATOMNAME", conf, "%4d" % i)
        atomname = "{:<4}".format(mccedb[key][:4])
        key = ("CONNECT", conf, atomname)
        connect = mccedb[key].rstrip()
        orbital_type = connect[:9].strip()
        nconnected = len(connect[10:])/10+1
        connected_atoms = []
        for j in range(1, nconnected+1):
            serial = int(connect[j*10:j*10+5])
            catomname = '%4s' % ("{:<4}".format(connect[j*10+5: j*10+9]))
            if serial != 0:
                catomname = " ?  "
            connected_atoms.append(catomname)
        quoted = ['"%s"' % x for x in connected_atoms]
        line = "CONNECT, \"%s\", %s: %s\n" % (atomname, conf, ", ".join(quoted))
        lines.append(line)

    return lines

def make_charge(conf):
    natom = int(mccedb["NATOM", conf, "    "])
    lines = []
    for i in range(natom):
        key = ("ATOMNAME", conf, "%4d" % i)
        atomname = "{:<4}".format(mccedb[key][:4])
        key = ("CHARGE", conf, atomname)
        if mccedb.has_key(key):
            charge = float(mccedb[key])
        else:
            charge = 0.0
        line = "CHARGE, %s, \"%4s\": %6.3f\n" % (conf, atomname, charge)
        lines.append(line)

    return lines

def make_radius(conf):
    natom = int(mccedb["NATOM", conf, "    "])
    lines = []
    for i in range(natom):
        key = ("ATOMNAME", conf, "%4d" % i)
        atomname = "{:<4}".format(mccedb[key][:4])
        key = ("RADIUS", conf[:3], atomname)
        if mccedb.has_key(key):
            radius = float(mccedb[key])
        else:
            radius = 0.0
        line = "RADIUS, %s, \"%4s\": %6.3f, to_be_filled, to_be_filled\n" % (conf, atomname, radius)
        lines.append(line)
        #lines = list(set(lines))

    return lines


def make_confparm(conformers):
    lines = []
    for conf in conformers:
        if conf[-2:] == "BK" or conf[-2:] == "DM": continue
        key = ("PROTON", conf, "    ")
        nH = int(mccedb[key])
        key = ("ELECTRON", conf, "    ")
        ne = int(mccedb[key])
        key = ("PKA", conf, "    ")
        pKa0 = float(mccedb[key])
        key = ("EM", conf, "    ")
        Em0 = float(mccedb[key])
        key = ("RXN", conf, "    ")
        rxn = float(mccedb[key])

        line = "CONFORMER, %s: Em0=%6.1f, pKa0=%6.2f, ne=%2d, nH=%2d, rxn=%7.3f\n" % (conf, Em0, pKa0, ne, nH, rxn)
        lines.append(line)
    return lines


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
    tplout.append("\n# Atom definition\n")
    for conf in conformers:
        tplout += make_atom(conf)

    # Make charge records
    tplout.append("\n# Atom charges\n")
    for conf in conformers:
        tplout += make_charge(conf)

    # Make radius records
    tplout.append("\n# Atom radius, dielelctric boundary radius, van der Waals radius, and energy well depth\n")
    for conf in conformers:
        tplout += make_radius(conf)

    # Make conformer parameters
    tplout.append("\n# Conformer parameters that appear in head3.lst: ne, Em0, nH, pKa0, rxn\n")
    tplout += make_confparm(conformers)

    # Make rotatable bonds
    tplout.append("\n# Rotatable bonds. The atoms extended in the bond direction will all be rotated.\n")
    lines = []
    for key in mccedb.keys():
        if key[0] == "ROTAMER":
            residue = key[1]
            value = mccedb[key]
            atom1 = "\"%s\"" % value[:4]
            atom2 = "\"%s\"" % value[5:9]
            bond = "%s - %s" % (atom1, atom2)
            line = "ROTATE, %s: %s\n" % (residue, bond)
            lines.append(line)
    tplout += lines


    sys.stdout.writelines(tplout)
