#! /usr/bin/env python
# file: scope.py
# date: 2012-09-12 author: kyon

j, k = 1, 2

def proc1():
    j, k = 3, 4
    print "j == %d and k == %d" % (j, k)

def proc2():
    j = 6
    proc1()
    print "j == %d and k == %d" % (j, k)

k = 7
proc1()
print "j == %d and k == %d" % (j, k)

j = 8
proc2()
print "j == %d and k == %d" % (j, k)
