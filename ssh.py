#!/usr/bin/python
import paramiko 
import sys
import getpass
from getopt import getopt

scriptname = sys.argv.pop(0)
args, rest = getopt(sys.argv, "h:p:u:")
port = 22
host = "localhost"
user = getpass.getuser()
for key, val in args:
    if key == "-h":
        host = val
    elif key == "-p":
        port = int(val)
    elif key == "-u":
        user = val

secret = getpass.getpass()
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
com = raw_input("--> ")
while(com):
    channel = client.get_transport().open_session()
    channel.get_pty()
    channel.settimeout(5)
    channel.exec_command(com)
    print channel.recv(100500)
    com = raw_input("--> ")
channel.close()
client.close()
