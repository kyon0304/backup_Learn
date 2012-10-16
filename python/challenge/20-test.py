#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 20-test.py
# date: 2012-10-16 author: kyon

import urllib2, base64

url ="http://www.pythonchallenge.com/pc/hex/idiot2.html"
#request = urllib2.Request("http://www.pythonchallenge.com/pc/hex/idiot2.html")
username,passwd = 'butter','fly'
p = urllib2.HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, passwd)
handler = urllib2.HTTPBasicAuthHandler(p)
opener = urllib2.build_opener(handler)
result = opener.open(url).info()
#base64string = base64.encodestring('%s:%s' % (username,passwd))
#request.add_header("Authorization","Basic %s" % base64string)
#result = urllib2.urlopen(request).info()
print result
