#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 15.py uzi.html
# I totally didn't find anything valuable..
# date: 2012-10-10 author: kyon

import datetime, calendar

for year in range(1006,1996,10):
    d = datetime.date(year, 1, 26)
    if d.isoweekday() == 1 & calendar.isleap(year):
        print d

