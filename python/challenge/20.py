#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 20.py /pc/hex/idiot2.html
# date: 2012-10-16 author: kyon

import urllib

url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg'
info = urllib.urlopen(url).info()
content = info['Content-Range']
print content
scope = [(30203, 2123456789), (30237, 2123456789),(30284, 2123456789),(30295, 2123456789),(30313, 2123456789),(30347, 2123456789),(2123456712, 2123456789),(2123456744,2123456789)]
hint = ''
for i in scope:
    opener = urllib.FancyURLopener({})
    opener.addheader("range", "bytes=%d-%d" % i)
    f = opener.open(url)
    print
    if int(f.info()['Content-Length']) < 50:
        hint = f.read()
        print "Content:", hint,
    try:
        print 'Content-Range:', f.info()['Content-Range']
    except:
        print f.info()

scope = (1152983631, 2123456789)
opener = urllib.FancyURLopener({})
opener.addheader("range", "bytes=%d-%d" % scope)
f = opener.open(url)
print f.info()

open('20.zip', 'w').write(f.read())

hint = hint[::-1]
nickname = 'invader'
print 'hint:', hint,"and nickname is: ", nickname
passwd = nickname[::-1]

import zipfile
#zipinfo = zipfile.ZipFile('20.zip').infolist()
zipinfo = zipfile.ZipFile('20.zip')
zipinfo.setpassword(passwd)
print zipinfo.read('readme.txt')
zipinfo.extractall()
