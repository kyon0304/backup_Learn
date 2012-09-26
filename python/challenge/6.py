#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 6.py channel.html
将.html替换为.zip下载文件并遍历，收集comments太坑爹了。。谁知道zipfile里面的file还有注释阿。。而且不是字符画的hockey，是组成字符画的oxgen这几个字母呢
# date: 2012-09-26 author: kyon

import zipfile

x = zipfile.ZipFile('channel.zip')
num = '90052'
ans = ''
while True:
    try:
        content = x.read(num+'.txt')
        ans += x.getinfo(num+'.txt').comment
        num = content.split()[-1]
        print content
    except (EOFError, KeyError, KeyboardInterrupt):
        print 'Congratulations!'
        break
print ans
x.close()
