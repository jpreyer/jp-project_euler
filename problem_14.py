#!/usr/bin/env python

def even_term(n):
	return n/2
	
def odd_term(n):
	return 3*n +1

max = 0
for i in range(1,1000000):
	count=0
	start=i
	answer=start
	while 1:
		if answer == 1:
			count = count +1
			#print answer
			break
		else:
			#print answer
			count = count + 1
			if (answer % 2) == 0:
				answer=even_term(answer)
			else:
				answer=odd_term(answer)

	#print count,":",start
	if count > max:
		max = count
		maxnum = start
		

print "ANSWER:",maxnum,"(",max,")"