#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 19.py /hex/bin.html
# date: 2012-10-15 author: kyon
# 大小端的问题，重新排字节序

import base64,array,wave
#ImageChops,Image

buffers = open('19.txt','r').read()
data = base64.b64decode(buffers)
open('indian.wav','wb').write(data)

wi = wave.open('indian.wav','rb')
wo = wave.open('indian_inv.wav','wb')
wo.setparams(wi.getparams())

a = array.array('i')
a.fromstring(wi.readframes(wi.getnframes()))
a.byteswap()

wo.writeframes(a.tostring())
wi.close(),wo.close()

#im = Image.open('19_map.jpg')
#out = ImageChops.invert(im)
#out.show()
