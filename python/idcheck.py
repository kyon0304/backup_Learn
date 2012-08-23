#! /usr/bin/env python
# file: idcheck.py
# date: 2012-8-22


def check():
    import keyword
    letters = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)] + ['_']
    digits = [str(range(0,10))]
    ld = letters + digits
    myid = raw_input('Input your id: ')
    if(len(myid) == 1):
        if myid not in letters:
            print 'Invalid name!'
        else:
            print 'Approved!'
    else:
        if myid in keyword.kwlist:
            print "It's a keyword, invalid!"
        else:    
            for letter in myid:
                if myid[0] in digits:
                    print 'Invalid!'
                    break
                elif letter not in ld:
                    print 'Invalid!'
                    break
            else:
                print 'Approved!'
    
def main():
    while True:
        try:
            check()
        except (IOError,KeyboardInterrupt,IndexError,EOFError):
            print 
            print 'End Check!'
            break

if __name__ == '__main__':
    main()
