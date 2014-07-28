import sys, random

if len(sys.argv) > 1:
    history_self, history_other = sys.argv[1].split(',')
else:
    history_self = history_other = ""

movemap = [ [(1.000000,0.000000),(0.473863,0.526137),(0.394636,0.605364),(0.490512,0.509488),(1.000000,0.000000)],
        [(0.695328,0.000000,0.304672),(0.275953,0.582347,0.141700),(0.192635,0.700391,0.106974),(0.196343,0.689662,0.113995),(0.289968,0.544619,0.165413)],
        [(0.570635,0.000000,0.429365),(0.236734,0.570126,0.193139),(0.167197,0.687133,0.145670),(0.173139,0.667169,0.159693),(0.264911,0.475316,0.259773)],
        [(0.490512,0.000000,0.509488),(0.196309,0.578888,0.224803),(0.135744,0.692358,0.171898),(0.140638,0.663397,0.195965),(0.220709,0.426989,0.352302)],
        [(1.000000,0.000000,0.000000),(0.147944,0.636760,0.215296),(0.089478,0.737358,0.173165),(0.087259,0.704604,0.208137),(0.128691,0.435655,0.435655)]  ]

def sharpness(history):
    ret = 0
    for action in history:
        if action == 'S':
            ret += 1
        elif action == 'P' and ret > 0:
            ret -= 1
    return ret

def action(history_self, history_other):
    sharpness_self = sharpness(history_self)
    sharpness_other = sharpness(history_other)
    if sharpness_self >= 5:
        return 'P'
    elif sharpness_other >= 5:
        return 'S'
    moves = movemap[sharpness_self][sharpness_other]
    v = random.random()
    if v < moves[0]:
        return 'S'
    elif v < moves[0] + moves[1]:
        return 'B'
    else:
        return 'P'

if __name__ == "__main__":
    print(action(history_self, history_other))