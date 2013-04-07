#! /usr/bin/env/ python
import sys
sys.setrecursionlimit(1000000000)

def getChange(amount, changes):
    if amount == 0:
        return 1
    elif amount < 0 or len(changes) == 0:
        return 0
    else:
        return getChange(amount-changes[0], changes)+getChange(amount, changes[1:])

def main():
    amount = 10000
    changes = [1,5,10,50,100,500,1000,2000,5000]
    print getChange(amount, changes)

if __name__ == '__main__':
    main()
