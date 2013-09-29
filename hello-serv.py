#!/usr/bin/env python

import socket
import getopt
import sys
import os
import time

def usage():
    sys.stderr.write("{0}: usage: {0} -i <inet ver> -a <addr> -p <port>\n".format(os.path.basename(sys.argv[0])))
    sys.exit(1)

if __name__ == "__main__":

    i = None
    a = None
    p = None
    
    args, rest = getopt.getopt(sys.argv[1:], "i:a:p:")
    for key, val in args:
        if key == "-i":
            i = int(val)
        elif key == "-a":
            a = val
        elif key == "-p":
            p = int(val)

    if i is None or a is None or p is None:
        usage()

    if i == 4:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    elif i == 6:
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    s.bind((a, p))
    s.listen(100)
    while True:
        ss = s.accept()[0]
        try:
            while True:
                ss.send("Hello, world! (from IPv%d, %s, %d)\n" % (i, a, p))
                time.sleep(1)
        except Exception, ex:
            pass
