#! /usr/bin/env python
# file: mult.py -- ex_chapter11-13
# date: 2012-09-13 author: kyon

from time import time

def timeit(func, *args, **kwargs):
    try:
        now = time()
        retval = func(*args, **kwargs)
        result = (time()-now, retval)
    except Exception, e:
        result = (False, str(e))
    return result

def mult1(n):
    seq = range(1,n+1)
    result = 1
    for i in seq:
        result *= i
    return result

def mult2(n):
    seq = range(1,n+1)
    return reduce(lambda x,y: x*y, seq)

def mult3(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*mult3(n-1)
    
def main():
    funcs = {mult1, mult2, mult3}
    for eachFunc in funcs:
        print '-' * 20
        retval = timeit(eachFunc, 10)
        if retval[0]:
            print '%s gets %s, costs %s ms.' % (eachFunc.__name__, retval[1], retval[0])
        else:
            print '%s Failed:' % (eachFunc.__name__), retval[1]

if __name__ == '__main__':
    main()
