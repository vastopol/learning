#!/usr/bin/python3

# Template

#----------------------------------------

# Modules
import sys

# Classes
from project.program import Program

#----------------------------------------

def main(arg):
    ifile = open(arg,"r")
    ofile = open(arg+".out","w")
    p = Program(ifile,ofile)
    p.function()

#----------------------------------------

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: Missing Arguments")
        print("Usage: $ ./program <files>")
        sys.exit(1)
    files = sys.argv[1:]
    for file in files:
        main(file)
