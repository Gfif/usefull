#!/usr/bin/python

import random

f = open("group", "r")

list = []
for i in f:
    list.append(i)
for i in xrange(4):
    victim = random.choice(list)
    list.pop(list.index(victim))
    print victim

exit()

