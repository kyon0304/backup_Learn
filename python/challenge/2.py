#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 2.py 找字母
# date: 2012-09-25 author: kyon

from string import lowercase as lc 
from string import digits as num
char = lc + num
chars = ''
f = open('2.txt')
for line in f:
    for c in line:
        if c in char:
            chars += c

f.close()

print chars
