#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 16.py
# date: 2012-10-11 author: kyon

import Image
def straighten(line):
    idx = 0
    while line[idx] != 195:
        idx += 1
    return line[idx:]+line[:idx]

im = Image.open('mozart.gif')
for y in range(im.size[1]):
    line = [im.getpixel((x,y)) for x in range(im.size[0])]
    line = straighten(line)
    [im.putpixel((x,y),line[x]) for x in range(len(line))]

im.show()
