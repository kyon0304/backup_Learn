#! /usr/bin/env python
# file: stack.py
# date: 2012-8-21

stack = []

def pushit():
    stack.append(raw_input("Enter new string to push: ").strip())
def popit():
    if(len(stack) == 0):
        print "The stack is empty."
    else:
        print 'String [',stack.pop(),'] is removed'
def viewstack():
    print stack

CMDs = {'u':pushit, 'o':popit, 'v':viewstack}

def showmenu():
    pr = '''
p(U)sh
p(O)p
(V)iew
(Q)uit

Enter your choice:'''

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (IndexError, KeyboardInterrupt, IOError):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'uovq':
                print 'Invalid option, try again'
            else:
                break
    
        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()
