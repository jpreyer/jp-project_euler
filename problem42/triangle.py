#!/usr/bin/python

n = 100
t=1
triangle = [0]
total=0
answer=0
Max=1000

def triangle_number (max_number):
	t = 1
	while t < max_number:
		tn = t*(t+1)/2
		triangle.append (tn)
		t += 1

triangle_number (Max)
f = open('words.txt', 'r')
for line in f:
	words = line.split(',')

for s in words:
	total = 0
	s = s.strip('\"')

	for i in range (0,len(s)):
		total = total + ord(s[i]) - 64

	if total in triangle :
		#print s, " is a triangle number ", total
		answer += 1

print answer
