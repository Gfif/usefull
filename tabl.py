#!/usr/bin/python
#-*-coding: utf-8 -*-

t = [[u'ш',u'б'],[u'м',u'н',u'к'],[u'ы',u'м',u'б',u'ш'],[u'б',u'ы',u'н',u'к',u'м'],[u'и',u'н',u'ш',u'м',u'к'],[u'н',u'ш',u'ы',u'и',u'к',u'б'],[u'ш',u'и',u'н',u'б',u'к',u'ы'],[u'к',u'н',u'ш',u'м',u'ы',u'б',u'и'],[u'б',u'к',u'ш',u'м',u'и',u'ы',u'н'],[u'н',u'к',u'и',u'б',u'м',u'ш',u'ы',u'б']]
import random
import time
while True:
    line = random.choice(t)
    char = random.choice(line)
    print t.index(line) + 1, line.index(char) + 1
    time.sleep(5)
    print char

