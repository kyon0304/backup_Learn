#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 7.py oxygen.html 处理图像的
# date: 2012-09-26 author: kyon

import Image

img = Image.open('oxygen.png')
data = list(img.getdata())

width = img.getbbox()[2]
height = img.getbbox()[3]
print 'width height:\n%d\t%d' % (width, height)

print 'grey rows:'
for h in range(height):
    pixel = data[h*width]
    if pixel[0] == pixel[1] == pixel[2]:
        print h,
print

print 'One line in grey rows:(line43)'
gw = 1
for w in range(width):
    pixel = data[43*width+w]
    if pixel[0] == pixel[1] == pixel[2]:
        gw += 1
        print pixel[0],
print

print 'exclude the repeat ones:(line45)'
string = ''
#for w in range(gw):
#    pixel = data[45*width+w]
#    if w < gw - 1:
#        nextpixel = data[45*width+w+1]
#    else:
#        nextpixel = pixel
#    if nextpixel == pixel:#这里栽了。。
#        continue
#    else:
#        string += chr(pixel[0])
#print string
#
for w in range(0, gw, 7):
    pixel = data[45*width+w]
    string += chr(pixel[0])
print string

#grey = img.convert('L')
#gdata = list(grey.getdata())
#print data[10]
#print gdata[10]

pos = string.split('[')[1].split(']')[0]
#lchars = string.split('[')[0].split(',')
#chars = lchars[0]+lchars[1]
#lchars = chars.split('.')
#chars = lchars[0]+lchars[1]
#lchars = chars.split()
#chars = ''
#for i in lchars:
#    chars += i
#print chars
#print pos
lpos = list(pos.split(','))
lpos = [int(i) for i in lpos]
ans = ''
for i in lpos:
    ans += chr(i)
print "answer!:", ans
#print lpos

#print 'another map:' 
#ans = ''
#for i in lpos:
#    ans += chars[i%len(chars)]
#print ans
