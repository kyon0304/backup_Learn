#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 4.py 循环链接
# date: 2012-09-25 author: kyon

import urllib
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
num = '12345'
for i in range(400):
    sp = urllib.urlopen(url+num)
    content = sp.read()
    num = content.split()[-1]
    print content
