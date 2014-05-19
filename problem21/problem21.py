import math
n=4
A={}
B={}
while n <= 10000:
    L=[1]
    sum=0
    k=int(math.floor(math.sqrt(n))) + 1
    for i in xrange (2,k):
        if (n % i) == 0:
            L.append(i)
            t = n/i
            if (t != i):
                L.append(t)

    for j in L:
        sum += j

    A[n] = sum
    n += 1

sum1=0
for ii in A.keys():
    s1 = A[ii]
    if s1 > 3 and s1 < 10000:
        if A[s1] == ii and A[ii] == s1 and ii != A[ii]:
            sum1 += ii
            print ii, "  ", A[ii]

print sum1
