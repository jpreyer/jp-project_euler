#!/usr/bin/env python

def add_digit(n):
	d=[0] * 500
	total=0
	j=0
	p=0
	
	
	while n>0:
		d[j] = n % 10
		n = (n - d[j]) / 10
		j=j+1
	
	for p in d:
		total = total + p
	
	print "total = ", total
	



add_digit(2**1000)