a=2
b=101
ans = {}
while a <= 100:
	for i in xrange (2, b):
		print "%d ** %d" % (a,  i)
		n=a**i
		d = {n:1}
		ans.update(d)
	a +=1

print len(ans.keys())
