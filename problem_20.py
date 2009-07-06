#!/usr/bin/python

numbers=range(1,101)


def factorial (n):
	fact = 1;
	numbers = range(1,n+1)
	for i in numbers:
		fact = fact * i
	if n == 1:
		return 1
	else:
		return fact


N=factorial(100)
sum=0
while N>1:
	dig=N % 10
	sum = sum + dig
	N = (N-dig)/10

print "ANSWER=",sum
