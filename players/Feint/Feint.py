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
        return 'SP'[len(history_self)]
    elif history_other[1] == 'P':
        # Fierce fight
        if sharpness_self == 0:
            return 'S'
        elif history_self[-(1 + history_self.count('P'))] == 'S':
            return 'P'
        else:
            return 'B'
    else:
        # Smart guy
        if sharpness_other == 1:
            return 'B'
        elif history_self[-1] != 'S' or history_self[-4:] == 'BSBS':
            return 'S'
        elif history_other.count('S') > history_other.count('B'):
            return 'P'
        else:
            return 'B'

if __name__ == "__main__":
    print(action(history_self, history_other))