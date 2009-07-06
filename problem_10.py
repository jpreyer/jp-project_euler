#!/usr/bin/env python

from math import sqrt,floor

def sieve (n):
    numbers=range (1,n)
    print numbers
    mid=floor(sqrt(n))
    print n, mid
    for i  in range (2,floor(mid)):
        print "i=",i
        if numbers.index(i):
            multi=2
            t=i*multi
            
            while t<n:
                #print numbers
                print "remove here t=",t
                print numbers
                try:
                    numbers.remove(t)
                except:
                    print "i think that",t," has been removed"
                print numbers
                multi=multi+1
                t=i*multi
    print numbers


sieve(50)
