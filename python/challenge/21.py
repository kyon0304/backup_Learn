#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 21.py offline readme.txt&package.pack
# date: 2012-10-16 author: kyon

import zlib

data = open('package.pack').read()
dc = zlib.decompress(data)
print `dc[-1]`, `data[0]`
