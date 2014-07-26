import sys, math
a = "PPS"
i = 0
if (len(sys.argv) > 1): i = math.floor(((len(sys.argv[1])-1)/2) % 3)
print(a[i])