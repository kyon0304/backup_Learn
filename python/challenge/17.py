#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 17.py pc/stuff/violin.php
# date: 2012-10-13 author: kyon

from urllib2 import Request, urlopen
from urllib import quote_plus
url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
info = 'the flowers are on their way'
req = Request(url, headers={'Cookie':'info='+quote_plus(info)})
print urlopen(req).read()
