#!/usr/bin/python
# Convert C12 C6 parameters to vdw_radius and e_depth

import sys
import math


class PARAM():
    def __init__(self):
        self.C12 = 0
        self.C6 = 0
        return

class ATOM_VDW():
    def __init__(self):
        self.e_depth = 0.0
        self.r_vdw = 0.0


if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()
    lines = [line.strip() for line in lines if line and line[:8] == "VDWAMBER"]

    atoms_vdw = {}
    params = {}

    for line in lines:
        fields = line.split()
        keypair = fields[2]
        if fields[1] == "C12":
            C12 = float(fields[3])
            if keypair in params:
                params[keypair].C12 = C12
            else:
                params[keypair] = PARAM()
                params[keypair].C12 = C12
        elif fields[1] == "C6":
            C6 = float(fields[3])
            if keypair in params:
                params[keypair].C6 = C6
            else:
                params[keypair] = PARAM()
                params[keypair].C6 = C6

    for key in params.keys():
        fields = key.split("-")
        if fields[0] == fields[1]:
            C12 = params[key].C12
            C6 = params[key].C6
            atom = fields[0]
            R = (C12/C6*2)**(1.0/6.0)/2.0
            if atom not in atoms_vdw:
                atoms_vdw[atom] = ATOM_VDW()
            atoms_vdw[atom].r_vdw = R
            E = C6*C6/C12/4.0
            atoms_vdw[atom].e_depth = E

    # recover all C6 and C12
    for line in lines:
        print line
        fields = line.split()
        keypair = fields[2]
        atom1, atom2 = keypair.split("-")
        r0 = atoms_vdw[atom1].r_vdw + atoms_vdw[atom2].r_vdw
        e = math.sqrt(atoms_vdw[atom1].e_depth * atoms_vdw[atom2].e_depth)
        if fields[1] == "C12":  # recover C12
            C12 = e*r0**12
            print "Recover  C12   %s-%s  %11.3f" % (atom1, atom2, C12)
        elif fields[1] == "C6":  # recover C12
            C6 = 2*e*r0**6
            print "Recover  C6    %s-%s  %11.6f" % (atom1, atom2, C6)

    for atom in atoms_vdw:
        print "%s r_vdw=%10.3f e_depth=%10.3f" % (atom, atoms_vdw[atom].r_vdw, atoms_vdw[atom].e_depth)