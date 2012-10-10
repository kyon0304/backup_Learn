#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 14.py italy.html
# date: 2012-10-10 author: kyon
# 严重声明，这道题我赤果果的作弊了，不止hint，连代码都是看了别人的。。
# 将1个像素高的线条按着面包的螺旋方向绕起来（正方形），还是蛮有意思的
import Image
im = Image.open('wire.png')

directions = [(1,0), (0,1), (-1,0), (0,-1)]
x,y,p = -1,0,0
newIm = Image.new('RGB',(100,100))
doubled_steps = 200

while doubled_steps//2 > 0:
    for v in directions:
        step = doubled_steps//2
        for s in range(step):
            x,y = x+v[0],y+v[1]
            newIm.putpixel((x,y), im.getpixel((p,0)))
            p+=1
        doubled_steps-=1

newIm.show()
