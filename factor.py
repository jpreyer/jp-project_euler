#!/usr/bin/env python
# Let's try to factor an integer.  How hard can that be?  :)

from math import sqrt,floor

def factor (n):
	factors = []
	mid=int(sqrt(n))+1	
	for i in range (1,mid):
		if ( n % i == 0):
#			print i," is a factor of ",n
			factors.append(i)
			d = n / i
#			print d," is also a factor of ",n
			factors.append(d)
	factors.sort()
	return factors


print factor(28)
