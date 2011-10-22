#!/usr/bin/env python

from math import sqrt,floor

def factor (n):
	factors = []
	mid=int(sqrt(n))+1
	for i in range (1,mid):
		if ( n % i == 0):
			factors.append(i)
			d = n / i
			if (i != d):
				factors.append(d)
	factors.sort()
	return factors

def triangle_number(n):
	i = 1
	sum = 0
	while i <= n:
		sum = sum + i
		i+=1

	return sum


for i in xrange (1,100000):
	T = triangle_number(i)
	L = factor(T)
	if (len(L) > 500):
		print i,": ",T,":  ",L,": ",len(L)
