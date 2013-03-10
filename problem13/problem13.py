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
		total += int(b[i][j])
		i += 1
	j = j - 1
	digit = total%10
	answer.append(str(digit))
	total = (total-digit)/10


answer.append(str(total))
answer.reverse()
print ''.join(answer)
