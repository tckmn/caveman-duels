import sys, random
dg = False
if len(sys.argv) > 1:
    ow,ot = sys.argv[1].split(',')
else:
    ow = ot = ""
def gs(m):
    ow = 0
    ot = 0
    i = 0
    ms = m[0]
    mo = m[1]
    for _ in mo:
        if ms[i] == 'S':
            ow += 1
        elif ms[i] == 'P' and mo[i] in ['P','B']:
            ow -= 1
        if mo[i] == 'S':
            ot += 1
        elif mo[i] == 'P' and ms[i] in ['P','B']:
            ot -= 1
        if dg:
            print("Own: {}, Other: {}".format(ow,ot))
        i += 1
    return [ow, ot]

def sm(sh):
    if (type(sh) != list) and dg:
        raise ValueError('Invalid sh type.')
    ow, ot = sh
    if ow >= 5:
        ret = 'P'
    elif ow >= 0 and ot == 0:
        ret = 'S'
    elif ow > 0 and ot > 0:
        ret = 'P'
    elif ow == 0 and ot > 0:
        ret = 'B'
    else:
        ret = random.choice(['S','B','P']) #Should not happen
    return ret

if __name__ == "__main__":
    print(sm(gs([ow,ot])))