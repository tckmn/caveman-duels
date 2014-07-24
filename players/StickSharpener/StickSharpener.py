import random, sys  # Need Import Some Advance Techno Code

if __name__ == '__main__':  # If Techno Computer Name is Main

    try:  # Me Try Remember...
        me = sys.argv[1].split(',')[0]

        try:  # Me Try Sharpen Pointy Stick Quick! Me Needs Draw And Poke Caveman.
            print ("SBSBP"*5)[len(me)]

        except:  # Me Donno What To Do. Me Use Fancy Techno Algorithm!!!
            mePointy   = me.count("S") - me.count("P")
            meIsScary  = mePointy > 0
            meHasSword = mePointy > 5
            print ["S", random.choice("SBP"), "P"][meIsScary + meHasSword]

    except:  # Me Still Really Donno What To Do...
        print "S"