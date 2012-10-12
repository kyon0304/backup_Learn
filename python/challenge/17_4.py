#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 17_4.py 循环链接
# date: 2012-10-12 author: kyon

import urllib
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
num = '12345'
cookie = []
for i in range(400):
    sp = urllib.urlopen(url+num)
    content = sp.read()
    num = content.split()[-1]
    cookie.append(sp.info()['Set-Cookie'].split(';')[0].split('=')[1])
    print i, content
string = ''.join(cookie)
