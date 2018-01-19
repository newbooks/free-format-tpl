# 1. ATOM sections, atom names, charge ele_radius, vdw_radius, and vdw energy well depth (kcal/mol)
ATOM, ALABK, " N  ": -0.350, 1.50, 1.750, 0.160
ATOM, ALABK, " CA ":  0.100, 2.00, 2.000, 0.150
ATOM, ALABK, " C  ":  0.550, 1.70, 2.000, 0.150
ATOM, ALABK, " H  ":  0.250, 1.00, 1.000, 0.020
ATOM, ALABK, " HA ":  0.000, 0.00, 1.000, 0.020
ATOM, ALABK, " O  ": -0.550, 1.40, 1.600, 0.200
ATOM, ALA01, " CB ":   0.00, 2.00, 2.000, 0.150
ATOM, ALA01, " HB1":   0.00, 0.00, 1.000, 0.020
ATOM, ALA01, " HB2":   0.00, 0.00, 1.000, 0.020
ATOM, ALA01, " HB3":   0.00, 0.00, 1.000, 0.020

# 2. CONNECT sections, bond information
CONNECT, ALABK, " N  ": sp3, " CA ", " H  ", -1
CONNECT, ALABK, " CA ": sp3, " N  ", " HA ", " C  ", " CB "
CONNECT, ALABK, " C  ": sp2, " CA ", " O  ", +1
CONNECT, ALABK, " H  ": s, " N  "
CONNECT, ALABK, " HA ": s, " CA "
CONNECT, ALABK, " O  ": sp2, " C  "
CONNECT, ALA01, " CB ": sp3, " HB1"
CONNECT, ALA01, " HB1": s, " CB "
CONNECT, ALA01, " HB2": s, " CB "
CONNECT, ALA01, " HB3": s, " CB "

# 3. Conformer parameters, all 0 if no protonation, no oxidation
PROTON,   ALA01:      0
PKA,      ALA01:      0.0
ELECTRON, ALA01:      0
EM,       ALA01:      0.0
RXN,      ALA01:      0.0

# 4. Rotamer parameters
