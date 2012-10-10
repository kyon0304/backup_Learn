#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 13.py disproportional.html
# xmlrpclib xml远程调用，以及12关中Bert is evil!
# date: 2012-10-10 author: kyon

import xmlrpclib as XR

server = XR.ServerProxy("http://huge:file@www.pythonchallenge.com/pc/phonebook.php")

print "Methods that are supported:"
print server.system.listMethods()

print "Answer is:", server.phone('Bert').split('-')[1]
