import os
import sys
import random

def getLastMove(player, turn):
    path = 'players/FoolMeOnce/'+player+str(turn)+'.txt'
    if os.path.isfile(path):
        with open(path, 'r') as f:
            return f.read()
    else:
        return 'nofile'

def sharpness(history):
    sharpness = 0
    for c in history:
        if c is 'S':
            sharpness+=1
        elif c is 'P' and sharpness > 0:
            sharpness-=1
    return sharpness

def takeTurn(choice, history, turn):
    print(choice)
    with open('players/FoolMeOnce/me'+str(turn)+'.txt', 'w') as f:
        f.write(choice)
    #also record their last choice
    choice = history[-1]
    with open('players/FoolMeOnce/them'+str(turn)+'.txt', 'w') as f:
        f.write(choice)

#if its the first turn, always sharpen
if(len(sys.argv) == 1):
    print('S')

else:
    history = sys.argv[1].split(',')
    meSharp = sharpness(history[0])
    themSharp = sharpness(history[1])
    turn = len(history[0])

    #read opponents move and our move for this turn from last duel
    them = getLastMove('them', turn);
    me = getLastMove('me', turn);

    #if this is first duel, fool me once
    if(them is 'nofile' or me is 'nofile'):
        if themSharp is 0 and meSharp >0:
            takeTurn(random.SystemRandom().choice('PS'), history, turn)
        else:
            takeTurn('B', history, turn)

    #if we could have played a winning move, do it. otherwise do what we did last time
    elif(them is 'S' and meSharp > 0):
        takeTurn('P', history, turn)
    else:
        takeTurn(me, history, turn)