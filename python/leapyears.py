#! /usr/bin/env python
# file: leapyears.py
# date: 2012-09-13 author: kyon

def judge(year):
    if year%4 == 0:
        if year%100 == 0:
            return False
        else:
            return True
    else:
        return False

def getLeap():
    years = [n for n in range(1900,2012)]
#    leapyears = filter(judge, years)
    leapyears = [n for n in years if judge(n)]
    print "leap years between 1900-2012:", leapyears

getLeap()
