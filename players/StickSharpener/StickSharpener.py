import random, sys  # Need Import Some Advanced Techno Code

if __name__ == '__main__':  # If Fancy Techno Computer Is Main

    try:  # Me Try Fancy Techno Algorithm!

        me, he = sys.argv[1].split(',')

        mePointy   = me.count("S") - me.count("P")
        hePointy   = he.count("S") - he.count("P")
        meCanPoke  = mePointy > 0
        heCanPoke  = hePointy > 0
        meHasSword = mePointy >= 5
        heHasSword = hePointy >= 5
        heScary = meCanPoke + meHasSword 
        meScary = heCanPoke + heHasSword
        print random.choice(\
            [["S" , "SP", "P" ],\
             ["B" , "BP", "P" ],\
             ["P" , "P" , "P" ]][heScary][meScary])

    except:  # Fancy Techno Algorithm Fails... Me Just Sharpen
        print "S"