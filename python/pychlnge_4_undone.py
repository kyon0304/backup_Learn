#! /usr/bin/python
# Filename: pychlng_4.py

from urllib import urlopen
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=85501"
webpage = urlopen(url)
text = webpage.read()
print text
