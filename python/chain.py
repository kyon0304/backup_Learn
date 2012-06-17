#!/usr/bin/python
# chain.py
# 2012-2-25

import urllib
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
rurl = "http://www.google.com.hk"
webpage = urllib.request.urlopen(url+start)
text = webpage.read()
print(text)
