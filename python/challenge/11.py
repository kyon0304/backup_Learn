#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 11.py 奇偶变换清晰化图像 5808.html
# date: 2012-10-08 author: kyon

import Image,StringIO

im = Image.open('cave.jpg')
size = im.size

output = StringIO.StringIO()
im.save(output, format='jpeg')
output.seek(0)
new_im = Image.open(output)
new_im.show()
