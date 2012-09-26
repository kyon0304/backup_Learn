#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: createNew.py -- 使用模版创建新的python文件
# date: 2012-09-07 author: kyon

from datetime import *
import os

def getName():
    name = raw_input("input your file's name > ")
    while os.path.isfile(name):
        print '%s already exists!' % name
        name = raw_input("input your file's name > ")
        if name.lower() == 'q':
            break
    return name

def create(name):
    f = open(name, 'w')
    f.write("#! /usr/bin/env python\n")
    f.write("# -*- coding: UTF-8 -*-\n")
    f.write("# file: %s\n" % name)
    f.write("# date: ") 
    f.write(datetime.now().strftime("%Y-%m-%d"))
    f.write(" author: kyon\n\n")

if __name__ =='__main__':
    name = getName()
    if name.lower() != 'q':
        create(name)
        print 'create file:', name
    else:
        print 'quit without create any file!'
