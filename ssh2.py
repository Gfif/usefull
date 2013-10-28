#!/usr/bin/python
import paramiko 
import sys
import getpass
from getopt import getopt

scriptname = sys.argv.pop(0)
port = 22 
user = "gfif"
hosts = open("hosts", "r")
secret = getpass.getpass()
for host in hosts:
    host = host[:-1]
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print user, "@", host, ":", port
    client.connect(hostname=host, username=user, password=secret, port=port)
    for com in ["sudo adduser schoolctf\n", "schoolctf" , "schoolctf", "\n", "\n", "\n", "\n", "\n"]:
        channel = client.get_transport().open_session()
        channel.get_pty()
        channel.settimeout(5)
        channel.exec_command(com)
        print channel.recv(100500)
        channel.close()
        client.close()
