#!/usr/bin/env python
import sys, re

def whatAmIDoing(opnHist, meSharp, opnSharp) :

    match = re.search(r"([PSB]{3,})\1$", opnHist)    ### Super RegEx ftw!

    if meSharp >= 5 :
        return "P"
    if opnSharp == 4 and meSharp > 0 :
        return "P"
    if match :
        opnStrat = match.group()
        if opnStrat[0] == "S" :
            if meSharp > 0 :
                return "P"
            else :
                return "S"
        elif opnStrat[0] == "B" :
            return "S"
    if opnSharp <= 0 :
        return "S"
    return "B"

try :
    hist = sys.argv[1].split(",")
    sharp = map(lambda h : h.count("S") - h.count("P"), hist)
    answer = whatAmIDoing(hist[1], *sharp)
except Exception :
    answer = "S"
finally :
    print(answer)