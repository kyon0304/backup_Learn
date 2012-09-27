#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 8.py integrity.html 原来用的压缩是bz2不是zlib阿。。
# date: 2012-09-27 author: kyon

un = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

from bz2 import decompress as dc

print 'username is:', dc(un)
print 'password is:', dc(pw)
