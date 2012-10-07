#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 9.py 连线 good.html
# date: 2012-10-07 author: kyon

f = open('good.txt')
dots = f.read().split(',')
dots = [int(i) for i in dots]

import Image, ImageDraw
im = Image.open('good.jpg')
draw = ImageDraw.Draw(im)
l = len(dots)/2-1
for i in range(l):
    dot = [dots[2*i],dots[2*i+1]]
    draw.point(dot, fill = 255)
im.show()
