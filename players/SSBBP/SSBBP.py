import sys
print "Simple Sequence Beats Big Players".split(' ')[
    len(sys.argv[1]) / 2 % 5 if len(sys.argv) > 1 else 0
]