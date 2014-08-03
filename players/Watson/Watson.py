# That's the actual logic. Initialization goes below.
def run():
    if his_sharpness[-10] - turn / 15 + 1 + turn % 3 - his_sharpness[-6] < 0:
        act(B=0, S=0, P=100) # 7.21% chance
    elif his_sharpness[-6] + 1 - his_sharpness[-2] < 0:
        act(B=0, S=0, P=100) # 4.15% chance
    elif his_history[-3] - my_history[-1] <= 0 and my_sharpness[-1] - turn / 10 <= 0:
        act(B=0, S=100, P=0) # 11.34% chance
    elif his_sharpness[-1] == 0:
        act(B=0, S=100, P=0) # 27.84% chance
    else:
        act(B=100, S=0, P=0) # 49.46% chance

# Boring stuff go here...

import sys, random

# Actions
block, sharpen, poke, idle = range(4)

# Converts textual history to internal format
def convert_history(textual_history):
    return ["BSP".index(action) for action in textual_history]

# Calculates sharpness after performing an action sequence
def calculate_sharpness(history):
    return history.count(sharpen) - history.count(poke)

# Returns a list containing the sharpness at the end of each turn
def sharpness_history(history):
    return [calculate_sharpness(history[:i + 1]) for i in range(len(history))]

# Acts based on the probability distribution (B%, S%, P%)
def act(B, S, P):
    r = random.random() * 100
    print "BSP"[(r >= B) + (r >= B + S)]

# Setup data
textual_history = sys.argv[1] if len(sys.argv) > 1 else ","
my_history, his_history = (convert_history(h) for h in textual_history.split(','))
my_sharpness, his_sharpness = (sharpness_history(h) for h in (my_history, his_history))
turn = len(my_history)
my_history, his_history = ([idle] * 16 + h for h in (my_history, his_history))
my_sharpness, his_sharpness = ([0] * 16 + s for s in (my_sharpness, his_sharpness))

# Make a move
run()