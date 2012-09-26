#! /usr/bin/env python
# file: 1.py
# date: 2012-09-25 author: kyon

chars = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#url = 'map'
#nchars = ''
#
#for letter in url:
#    if 96 < ord(letter) < 123:
#        x = ord(letter)+2
#        y = (x-96)%26+96
#        letter = chr(y)
#    nchars += letter
#
#print nchars

def makeRule():
    from string import lowercase as lc
    from string import maketrans
    trans = ''
    for l in lc:
        trans += chr( (ord(l)+2-96)%26+96  )
    return maketrans(lc, trans)

rule = makeRule()
print chars.translate(rule)
print 'map'.translate(rule)
