#!/usr/bin/env python
# This uses the Sieve of Atkin to generate primes.  in its current form
# it solves problem 10

from math import sqrt,floor


limit=2000000

mid=int(sqrt(limit))+1
is_prime = {0:-1, 1:-1, 2:1, 3:1, 4:-1}
for j in range (5, limit):
	is_prime[j] = -1

for x in range (1, mid):
	for y in range (1, mid):

		n = 4*(x**2) + y**2
		if ((n <= limit) and ((n % 12 == 1) or (n % 12 == 5))):
			is_prime[n] = is_prime[n] * -1

		n = 3*(x**2) + y**2
		if (n <= limit) and (n % 12 == 7):
			is_prime[n] = is_prime[n] * -1
	
		n = 3*(x**2) - y**2
		if (x>y) and (n <= limit) and (n % 12 == 11):
			is_prime[n] = is_prime[n] * -1


for n in range (5, mid):
	if is_prime[n] == 1:
		k = n * n
		p=1
		yy= k*p
		while yy < limit:
			is_prime[yy] = -1
			p = p +1
			yy= k*p

TOTAL=0
print "HEY>>>>>>>>> ",is_prime[965]
for h in range (2, limit):
	if is_prime[h] == 1:
		TOTAL = TOTAL + h

print TOTAL
