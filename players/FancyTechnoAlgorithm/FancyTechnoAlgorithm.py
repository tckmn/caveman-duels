import random, sys  # Need import some advanced techno code

if __name__ == '__main__':  # If fancy techno computer program is main

    try:  # Me try use fancy techno algorithm!

        me, he     = sys.argv[1].split(",")
        mePointy   = me.count("S") - me.count("P")
        hePointy   = he.count("S") - he.count("P")
        meCanPoke  = mePointy > 0
        heCanPoke  = hePointy > 0
        meHasSword = mePointy >= 5
        heHasSword = hePointy >= 5
        meScary    = meCanPoke + meHasSword 
        heScary    = heCanPoke + heHasSword

        # Me donno fancy coding math algoritm.
        # Math confuse. Me code work, me happy.
        if he[-6:] == "SB"*3:
            print "SP"[meCanPoke]
        elif (len(he) > 30 and he[-3:].count("B") > 2) or \
             (hePointy > 2 and he.count("SSBB") > 0 and he.count("BBS") > 0):
            if meHasSword:
                print "P"
            else:
                print "SB"[me[-1] == "S"]
        elif hePointy > 3 and he.count("BBS") > 2:
            print "SP"[me[-1] == "S"]
        else:
            print random.choice(\
                [["S", "SP", "P" ],\
                 ["B", "B" , "P" ],\
                 ["S", "P" , "P" ]][heScary][meScary])

    except:  # Fancy techno algorithm Failed... Me just sharpen.
        print "S"