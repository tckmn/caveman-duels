"""Sir Pokealot"""

import sys, random

def makeMove(player, rival):
    next_move = 'B'
    if len(player.history) == 0:
        next_move = 'S'
        return next_move
    if player.inStalemate():
        if player.isHostile():
            next_move = 'P'
        else:
            next_move = 'S'
        return next_move        
    if rival.isHostile():
        next_move = 'B'
    if ((rival.isFatal() or rival.isNearFatal()) and player.isHostile()) or player.isFatal():
        next_move = 'P'
        return next_move
    if not rival.isHostile():
        if player.isHostile():
            if not player.isNearFatal():
                next_move = 'P'
            else:
                next_move = 'S'
        else:
            next_move = 'S'
        return next_move
    if rival.getPattern() == 'sharpener' and not rival.isFatal() and player.isHostile():
        next_move = 'P'
    elif rival.getPattern() == 'blocker' and not rival.isFatal():
        next_move = 'S'
    elif rival.getPattern() == 'poker' and not rival.isHostile() and player.isHostile():
        next_move = 'P'
    else:
        next_move = 'B'
    return next_move


class Caveman:
    def __init__(self):
        self.history = ''
        self.sharpness = 0
        self.blocks = 0
        self.pokes = 0

    def getStats(self):
        for move in self.history:
            if move == 'S':
                self.sharpness += 1
            elif move == 'P':
                self.pokes += 1
                self.sharpness -= 1
            else:
                self.blocks += 1

    def getPattern(self):
        if 1 < len(self.history) < 5:
            if self.sharpness == len(self.history):
                return 'sharpener'
            if self.blocks >= len(self.history)-1:
                return 'blocker'
            if self.pokes == self.sharpness or self.pokes == self.sharpness - 1:
                return 'poker'
        return 'smartypants'

    def isHostile(self):
        return self.sharpness > 0

    def isNearFatal(self):
        return self.sharpness == 4

    def isFatal(self):
        return self.sharpness > 4

    def inStalemate(self):
        return len(self.history) > 90

player = Caveman()
rival  = Caveman()

if len(sys.argv) > 1:
    player.history, rival.history = sys.argv[1].split(',')

player.getStats()
rival.getStats()

print(makeMove(player, rival))