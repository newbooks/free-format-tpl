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
        
        print line

