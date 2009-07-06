#!/usr/bin/env python


def gen_triple (r,s):
    a1=r*r - s*s
    b1=2*r*s
    c1=r*r+s*s
    return [a1,b1,c1]



for i in range(2,1000):
    for j in range(1,i-1):
        [a,b,c] = gen_triple(i,j)
        sum = a+b+c
        if sum == 1000:
            print a,b,c
            print "answer is",a*b*c
