#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 10.py 找规律 bull.html
# date: 2012-10-07 author: kyon

f = open('sequence.txt')
a = f.read().split('[')[1].split(',')[:-1]
print a

fw = open('log10.txt','w')
count  = 1
nexT = [] 
for i in range(30):
    for j in range(len(a[-1])-1):
        if a[-1][j] == a[-1][j+1]:
            count += 1
        else:
            nexT.append(str(count))
            count = 1
            nexT.append(a[-1][j])
    if a[-1][-2] != a[-1][-1]:
        nexT.append('1')
    else:
        nexT.append(str(count))
    nexT.append(a[-1][-1])
    a.append(''.join(nexT))
    count = 1
    nexT=[]
    fw.write(a[-1]+'\n')

print len(a[30])

f.close()
fw.close()
