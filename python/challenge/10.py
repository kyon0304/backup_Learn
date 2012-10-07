#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 10.py 找规律 bull.html
# date: 2012-10-07 author: kyon

f = open('sequence.txt')
a = f.read().split('[')[1].split(',')[:-1]
print a

count  = 1
nexT = [] 
l = len(a) - 1
for i in range(l):
    if a[i] == a[i+1]:
        count += 1
    else:
        nexT.append(str(count))
        nexT.append(a[i])
a.append(''.join(nexT))

print a
