import sys, random

if len(sys.argv) > 1:
    history_self, history_other = sys.argv[1].split(',')
else:
    history_self = history_other = ""

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
    elif len(history_self) < 2:
        return 'S'
    elif len(history_self) < 6:
        return 'B'
    elif len(history_self) == 6:
        return 'P'
    elif 5 + 5 * sharpness_self < random.randrange(len(history_self)):
        return 'S'
    elif sharpness_other == 0:
        if sharpness_self == 0 or random.randrange(sharpness_self) == 0:
            return 'S'
        else:
            return 'P'
    elif sharpness_other == sharpness_self:
        return 'P'
    else:
        return 'B'

if __name__ == "__main__":
    print(action(history_self, history_other))