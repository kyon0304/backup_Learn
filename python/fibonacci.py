#! /usr/bin/env python
# file: fibonacci.py
# date: 2012-09-13 author: kyon

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def main():
    n = raw_input('Input a num: ')
    print fibo(int(n))

main()
