#!/usr/bin/python

b = []
answer = []
i = 1
total = 0

f = open('numbers.txt', 'r')
for line in f:

	b.append (line.rstrip('\n'))
	i = i + 1
f.close()

j=49
total = 0
while j >= 0:
	#print j
	i = 0
	while i<100:
#		print "i : ", i
#		print b[i][49]
		total += int(b[i][j])
		i += 1
	j = j - 1
	digit = total%10
	#print digit
	answer.append(str(digit))
	total = (total-digit)/10


answer.append(str(total))
answer.reverse()
#print "total: ", total
#print "digit: ", digit
print ''.join(answer)
#for ii in answer:
#	print ii,
#	print
#print answer
