#! /usr/bin/env python
# file: createNew.py -- create new python file with template
# date: 2012-09-07 author: kyon

from datetime import *

name = raw_input("input your file's name > ")
f = open(name, 'w')
f.write("#! /usr/bin/env python\n")
f.write("# file: %s\n" % name)
f.write("# date: ") 
f.write(datetime.now().strftime("%Y-%m-%d"))
f.write(" author: kyon\n")
