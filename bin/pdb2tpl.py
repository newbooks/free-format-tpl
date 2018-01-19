#!/bin/python
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "pdb2tpl.py pdbfile"
        sys.exit()

    lines = open(sys.argv[1]).readlines()
