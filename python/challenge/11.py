#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 11.py 奇偶位像素分离清晰化图像 5808.html
# date: 2012-10-08 author: kyon

import Image
#import StringIO

im = Image.open('cave.jpg')
size = im.size
dots = list(im.getdata())
print len(dots)

imo = Image.new('RGB',(640,240))
ime = Image.new('RGB',(640,240))
odots = []
edots = []
for i in range(len(dots)/2):
    odots.append(dots[2*i])
    edots.append(dots[2*i+1])
print len(odots),len(list(imo.getdata()))
imo.putdata(odots)
ime.putdata(edots)

imo.show()
ime.show()

#output = StringIO.StringIO()
#im.save(output, format='jpeg')
#output.seek(0)
#new_im = Image.open(output)
#new_im.show()
