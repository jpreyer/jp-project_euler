#!/usr/bin/python

def split_and_square (S):
	total = 0
	for i in range (0, len(S)):
		total = total + (int(S[i]))**2

	return total

answer = 0
for n in range (1,10000000):
	tmp = n
	while n != 1 and n != 89:
		n = split_and_square (str(n))
	if n == 89:
			print tmp
			answer += 1
print "==================="
print answer
