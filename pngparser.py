#!/usr/bin/env   python
import sys
import os
def usage():
    sys.stderr.write("{0}: usage: {0} <filename>\n".format(os.path.basename(sys.argv[0])))
    sys.exit(1)

def length2int(size):
    n, k = 0, 1
    for i in size[::-1]:
        n += ord(i) * k
        k *= 0x100
    return n
def main():
    if len(sys.argv) == 1:
        usage()
    filename = sys.argv[1]
    try:
        f = open(filename, "r")
    except IOError, s:
        sys.stderr.write(str(s) + "\n")
        sys.exit(2)
    sign = f.read(8)
    if sign[1:4] != "PNG":
        sys.stderr.write("{0}: {1} is not a PNG file\n".format(os.path.basename(sys.argv[0]), filename))
        f.close()
        sys.exit(3)
    sys.stdout.write(sign)
    while True:
        chunkrawlength = f.read(4)
        chunklength = length2int(chunkrawlength)
        chunktype = f.read(4)
        chunkdata = f.read(chunklength)
        chunkcrc = f.read(4)
        """ working with chunks here """
        if chunktype == "IEND":
            break
    f.close()
    
    
if __name__ == "__main__":
    sys.exit(main())
