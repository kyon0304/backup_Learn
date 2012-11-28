#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: genThumbnail.py
# date: 2012-11-28 author: kyon

from PIL import Image

size = 128, 128

infile = "test2.jpg"
outfile = "test.thumb.jpg"
im = Image.open(infile)
im.thumbnail(size, Image.NEAREST)#(.ANTIALIAS)
im.save(outfile, "JPEG")
