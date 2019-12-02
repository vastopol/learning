
# simplest useful disassembler
# see also
# https://pypi.org/project/maynard/
# https://bitbucket.org/larry/maynard/src/default/

import dis
# useful stuff in: dis, inspect, __future__

def disassemble(callable):
    print("def", callable.__name__ + ":")
    program = callable.__code__.co_code
    i = 0
    while i < len(program):
        op = program[i]
        if op < dis.HAVE_ARGUMENT:
            oparg = ''
            i += 1
        else:
            oparg = program[i+1] | (program[i+2] << 8)
            i += 3
        print("    ", dis.opname[op], oparg)
