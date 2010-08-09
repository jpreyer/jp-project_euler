#!/usr/bin/env python
# Template to use for python programs
# take output file, then wc -m and take that result and subtract 1000 and 27 from it.  I'll clean it up later... -jp
# answer is 21124

cardinal = ["thousand","hundred","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
ordinal = ["zero", "one", "two", "three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]


def split_number(n):
	d=[0] * 4
	word=""
	j = 0
	m = 1000
	while n>0:
		#print n
		if n < 20:
			#print n," ",ordinal[n],"\n"
			word = word+ordinal[n]
			
			#n=0
			break
		else:
			d[j] = n / m
		#	print d[j]
			if j==0:
				#print j,": ",ordinal[d[j]]," ", cardinal[j]
				
				if d[j] == 0:
					word = word+""
				else:
					word = word+ordinal[d[j]]+cardinal[j]
			else:
				if j == 1:
					#print j,": ",ordinal[d[j]]," ", cardinal[j]
					if d[j] == 0:
						word = word+""
					else:
						word = word+ordinal[d[j]]+cardinal[j]+"and"
				else:
					#print j,"::: ",d[j],cardinal[d[j]]
					#if d[j] == 0 and d[j-1] != 0:
					word = word+cardinal[d[j]]
					#else:
					#	word = word+"and"+cardinal[d[j]]
			n = n - d[j] * m
			m = m /10
			j = j+1

	print word

for i in range (1,1000):
	split_number (i)

