#! /usr/bin/env python
# file: pfractorize.py 
# description: isprime getfactors primefractorization
# date: 2012-08-24

def isprime(num):
    if num < 2:
        return False
    count = num / 2
    for i in range(2,count+1):
        if num%i == 0:
            return False
    return True
def getfactors(num):
    #factor = []
    #for i in range(1,num+1):
    #    if num%i == 0:
    #        factor.append(i)
    #return factor
    return [i for i in range(1,num+1) if num%i == 0]

def interface():
    num = raw_input('Enter a number: ').split()[0]
    try:
        num = int(num)
        return num
        #print 'Is a prime number [%s]' % isprime(num)
        print '%d\'s facors lists: %s' % (num, getfactors(num))
    except(TypeError,KeyboardInterrupt,ValueError):
        print 'Please enter a number!'

def primefactorization(num):
    primes = [i for i in getfactors(num) if isprime(i)]
    c = 0
    factors = []
    while True:
        if num == 1:
            break
        (num,i) = divmod(num,primes[c])
        if i != 0:
            num = i + num*primes[c]
            c+=1
        else:
            factors.append(primes[c])
    return factors


if __name__ == '__main__':
    num = interface()
    #print 'Is a prime number [%s]' % isprime(num)
    #print '%d\'s facors lists: %s' % (num, getfactors(num))
    print primefactorization(num)
#    print isprime(num)
