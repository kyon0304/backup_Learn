#!/usr/bin/env python
#file: ex_ch5.py
#date: 2012-8-10

#5-5
#def changes():
#    import random
#    dollar = random.randint(1,101)
#    print dollar,'cents to be changed.'
#    change = 1
#    cents =[0,0,0,0]
#    cents[0],change = divmod(dollar, 25)
#    cents[1],change = divmod(change, 10)
#    cents[2],change = divmod(change, 5)
#    cents[3],change = divmod(change, 1)
#    return cents
#
#cents = changes()
#print 'Change with',cents[0],'25 cents,',cents[1],'10 cents,',cents[2],'5 cents,','and',cents[3],'1 cents.'

#5-6
def calc():
    import string
    equation = raw_input('Your input equation here:\n')
    print
    operator = ['+','-','**','/','*']
    i = 0
    while 1:
        nums = equation.split(operator[i++])
        if len(nums == 2):
            result = int(nums[0])
