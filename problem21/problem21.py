import math
n=4
while n <= 10000:
    L=[1]
    sum=0
    k=int(math.floor(math.sqrt(n))) + 1
    for i in xrange (2,k):
        if (n % i) == 0:
            L.append(i)
            L.append(n / i)

    for j in L:
        sum += j

    print "d(",n,") = ", sum, "  ", sorted(L)
    n += 1
