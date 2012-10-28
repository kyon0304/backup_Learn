#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 22.py /pc/hex/copper.html
# date: 2012-10-25 author: kyon

import Image

im = Image.open('22_white.gif')
data = list(im.getdata())
print data[500:519]
print im.size
