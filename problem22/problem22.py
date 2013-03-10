#!/usr/bin/python

answer = 0
f = open('names.txt', 'r')
for line in f:
	names = line.split(',')
names.sort()
for index in range(len(names)):
	score = 0
	names[index] = names[index].strip('\"')
	for i in range (0,len(names[index])):
		score = score + ord(names[index][i]) - 64
	score = score * (index+1)
	#print names[index],"\t",score
	answer = answer + score

print answer
