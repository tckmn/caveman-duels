import sys, math, random
def countSharpness(a):
    s = 0
    for i in range(len(a)):
        if a[i] == 'P': s-=1
        elif a[i] == 'S': s+=1
        if s < 0: s = 0
    return s
def getHistory():
    me = ""
    him = ""
    if len(sys.argv) > 1:
        me, him = sys.argv[1].split(",")
    return me,him
if __name__ == '__main__':
    me, him = getHistory()
    me_s = countSharpness(me)
    him_s = countSharpness(him)
    answer = 'B'
    # First Case
    if (len(me) == 0):
        answer = 'S'
    # I have a sword
    elif (me_s == 5):
        answer = 'P'
    # Cant let he gets a sword
    elif (him_s == 4):
        answer = 'P'
    # His sword is dull
    elif (him_s == 0):
        # He may try to sharp
        # Cant attack? Sharp my stick
        if (me_s == 0): answer = 'S'
        else:
            if (random.randint(0,33) != 0): answer = 'S'
            else: answer = 'P'
    elif (len(him) % 5 == 0):
        # Decide what to do based on the
        # opponent last 3 movements.
        hist = him[-3:]
        # Does he like to block?
        if (hist.count('B') >= 2): answer = 'S'
    print(answer)