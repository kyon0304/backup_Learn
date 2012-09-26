#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 3.py "equality.html"
# date: 2012-09-25 author: kyon

#import string
import re

f = open('3.txt')
lines = f.read()
f.close()

#patt = '(([a-z]{1}[A-Z]{3}){2}[^A-Z]+)'
patt = '[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
print re.findall(patt, lines)

#for line in f:
#    for x in range(0, len(line)-7):
#        ch = line[x:x+7]
#        if ch[:3].isupper() and ch[4:].isupper() and ch[3].islower():
#            print ch
