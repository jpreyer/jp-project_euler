import math
def fib(n):
    ff = range(0,10000)
    ff[1] = 1
    ff[2] = 1

    if n == 1:
        return 1
    else:
        j=3
        while j <= n:
            ff[j] = ff[j-1] + ff[j-2]
            j += 1

    return ff[n]

for j in range (1,5000):
    fs = str(fib(j))
    if len(fs) == 1000:
        print j, "  ", len(fs)
        break
