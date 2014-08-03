from sys import argv

class caveman():
    actions = ''
    sharpness = 0

    def __init__(self, actions):
        self.actions = actions
        for action in self.actions:
            if action is 'S':
                self.sharpness = self.sharpness + 1
            elif action is 'P':
                self.sharpness = self.sharpness - 1

history = ['','']
if len(argv) > 1:
    history = argv[1].split(',')

me = caveman(history[0])
he = caveman(history[1])

def print_and_exit(text):
    print text
    exit()

def try_sharpen():
    if he.sharpness is 0:
        if me.sharpness >= 5:
            print_and_exit('P')
        print_and_exit('S')

def find_in_history():
    sharpness = 0
    fpoints = []
    index = 0
    for action in he.actions:
        if sharpness is 0:
            fpoints.append(index)
        if action is 'S':
            sharpness = sharpness + 1
        elif action is 'P':
            sharpness = sharpness - 1
        index = index + 1
    if len(fpoints) > 1:
        move = he.actions[fpoints[-1]:]
        for fpoint in fpoints[:-1]:         
            if he.actions[fpoint:fpoint+len(move)] == move:
                if he.actions[fpoint+len(move)] is 'P':
                    if he.sharpness >= 5:
                        if me.sharpness > 0:
                            print_and_exit('P')
                        else:
                            print_and_exit('S')
                    elif he.sharpness is 4 and me.sharpness >= 5:
                        print_and_exit('P')
                    else:
                        print_and_exit('B')
                elif he.actions[fpoint+len(move)] is 'S':
                    if me.sharpness > 0:
                        print_and_exit('P')
                    else:
                        print_and_exit('S')
                elif he.actions[fpoint+len(move)] is 'B':
                    if me.sharpness >= 5:
                        print_and_exit('P')
                    else:
                        print_and_exit('S')

def try_poke():
    if me.sharpness > 0:
        print_and_exit('P')

def copy():
    if len(he.actions) > 0 and he.actions[-1] in ['S','B']:
        print_and_exit(he.actions[-1])

try_sharpen()
find_in_history()
try_poke()
copy()
print_and_exit('S')