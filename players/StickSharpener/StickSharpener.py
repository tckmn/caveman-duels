import random, sys

if __name__ == '__main__':  
    histories = sys.argv[1].split(',')
    ownHistory = histories[0]
    try:
        print ("SBP"+"SBSBP"*5)[len(ownHistory)]
    except:
        print ["S", random.choice("BP")][ownHistory.count("S")-ownHistory.count("P")>0]