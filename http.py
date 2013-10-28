#!/usr/bin/env      python

import httplib
from getopt import getopt
import sys
  
def usage(scriptname):
    print "Usage: " + scriptname + " [-s] <host>"
    return 0

def main():
    scriptname = sys.argv.pop(0)
    opts, args = getopt(sys.argv, "s")
    if not args or len(args) != 1:
        usage(scriptname)
        return 1
    else:
        host = args[0]
    if opts and opts[0][0] == "-s":
        conn = httplib.HTTPSConnection(host);
    else:
        conn = httplib.HTTPConnection(host);
    conn.request("GET", "/")
    resp = conn.getresponse()
    print resp.status, resp.reason
    if resp.status == 200 and resp.reason == "OK":
        return 0
    else:
        return 1;
    
if __name__ == "__main__":
    exit(main());

