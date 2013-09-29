from socket import *
from time import sleep

s = socket(AF_INET, SOCK_STREAM)
s.connect(("sibears.ru", 6666))
for i in xrange(1001):
    print s.recv(10000)
    s.send("Iwatchyou!!!")
s.close()
exit(0)
