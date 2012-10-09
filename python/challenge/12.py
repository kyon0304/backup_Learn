#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 12.py 
# 处理gfx二进制文件(分为5张图像的数据)，处理原始数据而不是转换为string或其他
# evil.html
# date: 2012-10-09 author: kyon

f = open('evil2.gfx','rb')
data = f.read()
f.close()

for i in range(5):
    f = open("e%d.png" % i, 'wb')
    f.write(data[i::5])
    f.close()



#print content[:40]
#
#num = len(content)/5
#e0=[];e1=[];e2=[];e3=[];e4=[]
#for i in range(num):
#    e0.append(content[i])
#    e1.append(content[i+1])
#    e2.append(content[i+2])
#    e3.append(content[i+3])
#    e4.append(content[i+4])
#
#f0 = open('e0.jpg','w')
#f0.write(''.join(e0))
#f0.close()
#f0 = open('e1.jpg','w')
#f0.write(''.join(e1))
#f0.close()
#f0 = open('e2.jpg','w')
#f0.write(''.join(e2))
#f0.close()
#f0 = open('e3.jpg','w')
#f0.write(''.join(e3))
#f0.close()
#f0 = open('e4.jpg','w')
#f0.write(''.join(e4))
#f0.close()
