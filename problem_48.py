#!/usr/bin/env python

n = 1
t=0
total=0
while n <1001:
	t= n**n%10000000000
#	print n,"^",n, n**n%10000000000
	total += t
	n = n+1
print "answer is: ", total%10000000000
