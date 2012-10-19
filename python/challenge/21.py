#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 21.py offline readme.txt&package.pack
# date: 2012-10-16 author: kyon

import zlib, bz2

st = open('package.pack').read()
#st = zlib.decompress(st)
#print `st[-1]`, `st[:4]`
log = ''
log_len = len(log)
while True:
    try:
        st = zlib.decompress(st)
        log += ' '
    except:
        try:
            st = bz2.decompress(st)
            log += '#'
        except:
            if log_len == len(log): break
            st = st[::-1]
            print log[log_len:]
            log_len = len(log)

open('21_package.unpack','wb').write(st)
