#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 5.py pickle 序列化
# date: 2012-09-25 author: kyon

import pickle

f = open('banner.p')
content = pickle.load(f)

for row in content:
    thisrow = ''
    for col in row:
        thisrow += col[0]*col[1]
    print thisrow
