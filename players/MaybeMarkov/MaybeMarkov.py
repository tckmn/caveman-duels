import sys, itertools
from operator import itemgetter
from collections import defaultdict

SHARPEN, POKE, BLOCK, HALP = 'SPB?'

all_actions = SHARPEN, POKE, BLOCK
always = 1

def do(action):
    print(action)
    exit(0)

if len(sys.argv) < 2:
    do(SHARPEN)

class status:
    def __init__(self, actions):
        self.step = len(actions)
        self.last = actions[-1]
        self.sh = self.sharpness = actions.count(SHARPEN) - actions.count(POKE)
        self.dull = self.sharpness <= 0
        self.has_sword = self.sharpness >= 5
        self.actions = actions
        self.ratio = {act:actions.count(act)/self.step for act in all_actions}
        self.can_do = set(all_actions)

        if self.dull:
            self.can_do.remove(POKE)

    def can(self, action):
        return action in self.can_do


me, he = map(status, sys.argv[-1].split(','))
turns = me.step

if he.has_sword:
    if me.can(POKE)                :do(POKE)
    if always                      :do(SHARPEN)

if me.has_sword:
    if he.last != POKE and me.last == BLOCK :do(POKE)
    if he.can(POKE)                :do(BLOCK)
    if always                      :do(POKE)

if not he.can(POKE)                :do(SHARPEN)

if turns <= 4                      :do(BLOCK)
if turns < 30:
    if he.ratio[SHARPEN] == 1:
        if me.can(POKE)            :do(POKE)
        if always                  :do(SHARPEN)
    if always                      :do(BLOCK)

if turns > 97:
    do(POKE)

def react_on(action):
    do({
        HALP    : BLOCK,
        SHARPEN : POKE,
        POKE    : BLOCK,
        BLOCK   : SHARPEN
    }[action])

states = tuple(itertools.product(all_actions, all_actions))
change = defaultdict(lambda:defaultdict(lambda:0))
count  = defaultdict(lambda:0)

for i in range(1, turns):
    prev = me.actions[i-1], he.actions[i-1]
    now  = me.actions[i]  , he.actions[i]
    change[prev][now] += 1
    count[prev] += 1

current = change[me.last, he.last]
prediction = HALP

if len(current) is 0:
    do(BLOCK)

if len(current) is 1:
    if tuple(current.values())[0] > turns / 7:
        prediction = tuple(current.keys())[0][1]

counts = itemgetter(1)

if len(current) > 1:
    key1, value1 = max(current.items(), key=counts)
    current[key1] *= 0.9
    key2, value2 = max(current.items(), key=counts)
    if key1 == key2:
        prediction = key1[1]

react_on(prediction)