import sys, math, random
def count(a):
    s = 0
    for i in range(len(a)):
        if a[i] == 'P': s-=1
        elif a[i] == 'S': s+=1
        if s < 0: s = 0
    return s
me = him = []
answer = 'S'
if len(sys.argv) > 1:
    me, him = sys.argv[1].split(",")
    s_me = count( me )
    s_him = count( him )

    # Cases to attack:
    # 1. If we have a sword.             s_me  >= 5
    # 2. Enemy needs to sharp.           s_him == 0
    # 3. Enemy is close to have a sword. s_him == 4
    if (s_me >= 5 or s_him <= 0 or s_him == 4):
        answer = 'P'
    else:
        # Block 80% of the time.
        if (random.randint(1,5) == 1):
            answer = 'S'
        else:
            answer = 'B'
print(answer)