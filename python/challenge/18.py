#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 18.py balloons.py
# date: 2012-10-15 author: kyon

import gzip,difflib

deltas = gzip.open('deltas.gz').read()
deltas = deltas.splitlines()

left,right,png = [],[],['','','']
for row in deltas:
    left.append(row[:53])
    right.append(row[56:])
diff = list(difflib.ndiff(left,right))

for row in diff:
    byte = [chr(int(i,16)) for i in row[2:].split()]
    if row[0] == ' ':
        png[0] += ''.join(byte)
    elif row[0] == '+':
        png[1] += ''.join(byte) 
    elif row[0] == '-':
        png[2] += ''.join(byte) 

#f = gzip.open('deltas.gz')
#a = [];b=[]
#for eachline in f:
#    temp = eachline.split('   ')
#    a.append(temp[0])
#    b.append(temp[-1])
#f.close()
#
#a = [i.split() for i in a]
#b = [i.split() for i in b]
#for i in range(len(a)):
#    while len(a[i]) < len(b[i]):
#        a[i].append('00')
#
#out = []
#for i in range(len(a)):
#    out.append(map(lambda x,y:int(y,16)-int(x,16), a[i],b[i]))
#print len(out),out[0]
#
#zeroline = out[0]
#png = ['','','']
#for i in range(len(a)):
#    byte_a  = [chr(int(i,16)) for i in a[i]]
#    byte_b  = [chr(int(i,16)) for i in b[i]]
#    if out[i] == zeroline:
#        png[2] += ''.join(byte_a)
#    else:
#        png[0] += ''.join(byte_a)
#        png[1] += ''.join(byte_b)

for i in range(3):
    open("18_%d.png" % i, 'wb').write(png[i])
