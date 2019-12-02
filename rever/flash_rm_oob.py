# example remove the out of bounds data from flash chip dumps
# i.MX Memory Maddness - Damien Cauquil

import sys

page = 4096
oob = 224
block = page + oob
orig_dump = open(sys.argv[1], 'rb').read()
out_dump = open(sys.argv[2], 'wb')
nblocks = int(len(orig_dump) / block)
for i in range(nblocks):
    out_dump.write(orig_dump[i*block : (i+1)*page + oob])
out_dump.close()
orig_dump.close()
