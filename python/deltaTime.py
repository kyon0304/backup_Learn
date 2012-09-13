#! /usr/bin/env python
# file: deltaTime.py -- ex_chapter11-12
# date: 2012-09-13 author: kyon

from time import time
def timeit(f):
    def wrapper(*args, **kwargs):
        now = time()
        try:
            return f(*args, **kwargs)
        finally:
            print "function: %s\nargs:%r\nkwargs:%r" % (f.__name__, args, kwargs)
            print "delta time:", (time()-now)
    return wrapper

@timeit
def hello(name):
    print "hilo,", name

hello('kyon~')
