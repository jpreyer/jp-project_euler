#!/usr/bin/env python

from math import sqrt,floor

def sieve (n):
    numbers=range (1,n)
    #print numbers
    mid=floor(sqrt(n))+1
    print n, mid
    for i  in range (2,floor(mid)):
        #print "i=",i
        try:
            numbers.index(i)
        except:
         #   print "i think that",i," had been removed"
            continue
        multi=2
        t=i*multi
            
        while t<n:
            #print numbers
          #  print "remove here t=",t
           # print numbers
            try:
                numbers.remove(t)
            except:
                print t
            
            multi=multi+1
            t=i*multi
    numbers.remove(1)    
    print numbers


sieve(100000)
