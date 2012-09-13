#! /usr/bin/env python
# file: average.py
# date: 2012-09-13 author: kyon

def average():
    print float(reduce(lambda x, y: x+y,range(0,10)))/len(range(0,10))

average()
