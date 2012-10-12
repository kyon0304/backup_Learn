#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: login.py
# date: 2012-10-12 author: kyon

import urllib2, cookielib
import urllib

url = 'http://www.pythonchallenge.com/pc/return/romance.html'
#url = 'http://www.douban.com/login'
#data = {'username' : 'huge',
#         'password' : 'file'}
#data = urllib.urlencode(data)
#header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)'}

#req = urllib2.Request(url,data,header)
#page = urllib2.urlopen(req).read()
#print page

un,pwd = 'huge','file'
p = urllib2.HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, un, pwd)
handler = urllib2.HTTPBasicAuthHandler(p)
cj = cookielib.CookieJar()
opener = urllib2.build_opener(handler,urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64)')]
urllib2.install_opener(opener)
page = urllib2.urlopen(url).read()
print page
print cj

