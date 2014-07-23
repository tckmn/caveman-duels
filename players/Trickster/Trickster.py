import sys, math
a = "PPPS"
i = 0
if (len(sys.argv) > 1): i = math.floor(((len(sys.argv[1])-1)/2) % 4)
print(a[i])