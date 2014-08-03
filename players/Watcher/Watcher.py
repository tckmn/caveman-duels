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

def weighted_random(dict):
    i = random.randrange(sum(dict.values()))
    for k, v in dict.items():
        i -= v
        if i < 0:
            return k

def action(history_self, history_other):
    sharpness_self = sharpness(history_self)
    sharpness_other = sharpness(history_other)
    if sharpness_self >= 5:
        return 'P'
    elif sharpness_other == 0:
        return 'S'  #Guaranteed safe
    elif sharpness_other == 1:
        #If the opponent isn't interested in a sword, time is on our side
        block_count = len(history_self) - len(history_self.rstrip('B'))
        if block_count > 3 and random.randrange(block_count) > 3:
            return 'S'
        else:
            return 'B'
    elif sharpness_other >= 5:
        return 'S'
    else:
        #Search for a weakness
        for i in range(10, 2, -1):
            if history_other[-i:] == history_other[-i*2:-i]:
                predicted_action = history_other[-i]
                if predicted_action == 'S':
                    if sharpness_self > 0:
                        return 'P'
                    else:
                        return 'S'
                elif predicted_action == 'B':
                    return 'S'
                elif predicted_action == 'P':
                    return 'B'
        #Presumably the opponent is random - respond with some educated randomness
        if sharpness_self == 0:
            return random.choice(['S','S','B'])
        return weighted_random({
            'S': sharpness_self,
            'B': 1,
            'P': sharpness_other,
        })

if __name__ == "__main__":
    print(action(history_self, history_other))