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
    return 'SSP'[sharpness_self]

if __name__ == "__main__":
    print(action(history_self, history_other))