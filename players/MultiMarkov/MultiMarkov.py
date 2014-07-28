#!/usr/bin/env python
import sys, itertools, collections

# how much history should we consider for the markov chain?
L = 2

def sharp(hist):
    return min(hist.count('S') - hist.count('P') , 5)

# takes a dict and two player's histories
# fills the dict with the opponent's next move,
# based on current sharpnesses and the last L moves of each player
def train(A, a_hist, b_hist):
    # keep track of the last L moves for each player
    a_past = a_hist[0:L]
    b_past = b_hist[0:L]
    if len(a_hist)<L+1:
        return
    a_shrp = sharp(a_past)
    b_shrp = sharp(b_past)
    a_hist = a_hist[L:]
    b_hist = b_hist[L:]
    # step through the string and track sharpness as we go
    while len(b_hist):
        b_m = b_hist[0]
        b_hist = b_hist[1:]
        if __debug__:
            print a_shrp, b_shrp, a_past, b_past, b_m
        A[a_shrp,b_shrp,a_past,b_past,b_m] += 1
        a_m = a_hist[0]
        a_hist = a_hist[1:]
        a_past = a_past[-(L-1):] + a_m
        b_past = b_past[-(L-1):] + b_m
        if b_m == 'P':
            b_shrp -= 1
        if b_m == 'S':
            b_shrp += 1
        if a_m == 'P':
            a_shrp -= 1
        if a_m == 'S':
            a_shrp += 1
    b_m = 'P'
    if __debug__:
        print a_shrp, b_shrp, a_past, b_past, b_m
    # assume that they won or will win with a poke
    # TODO: only assume when considering non-current matches
    # TODO: figure out if I won, instead
    A[a_shrp,b_shrp,a_past,b_past,b_m] += 1



# get the move history for each player
if len(sys.argv) > 1:
    pa, pb = sys.argv[1].split(',')
else:
    pa, pb = '', ''

# TODO: track and train based on all historical matches
# filedir='players/MultiMarkov'
# matchfiles = sorted([ f for f in os.listdir(filedir) if f.startswith('match')])
# if len(matchfiles) > 0:
#   candidate = matchfiles[-1]
#   with open(filedir + '/' + matchfiles[-1]) as cf:
#       turn = len(cf.readline())
#       if turn == len(pa): # newline included in turn count, not in pa.turn count
#           matchnum = int(candidate[5:])
#       else:
#           matchnum = int(candidate[5:])+1
# else:
#   matchnum = 0
# with open(filedir + '/match' + str(matchnum).rjust(20,'0'),'w+') as f:
#   f.write(pa + '\n')
#   f.write(pb + '\n')

# dict[pa sharpness, pb sharpness, pa last L moves, pb last L moves]
# { S:count, P:count, B:count }
# M will contain counts for every enemy faced so far combined
# N will contain counts for the current enemy
# M =
N = collections.Counter()

train(N, pa, pb)

a_shrp = sharp(pa)
b_shrp = sharp(pb)
# recent past for pa and pb
a_past = pa[-L:]
b_past = pb[-L:]
if __debug__:
    print a_shrp, b_shrp, a_past, b_past

# add up all the s,p,b seen as next moves
# for every scenario in the neighborhood of the current scenario
s = 0
p = 0
b = 0
# sharpness neighborhood is tricky, since 0 and 5 are special cases
for a_shrp_t in [[0],[1,2],[1,2,3],[2,3,4],[3,4],[5]][a_shrp]:
    for b_shrp_t in [[0],[1,2],[1,2,3],[2,3,4],[3,4],[5]][b_shrp]:
        # filtering of move neighborhood happens below
        for a_past_t in [''.join(cc) for cc in itertools.product('SPB',repeat=L)]:
            for b_past_t in [''.join(cc) for cc in itertools.product('SPB',repeat=L)]:
                # only consider move lists exactly one move different from the real situation
                if \
                    sum(c1 != c2 for c1,c2 in zip(a_past,a_past_t))==1 or \
                    sum(c1 != c2 for c1,c2 in zip(b_past,b_past_t))==1:
                    if __debug__:
                        print a_shrp_t,b_shrp_t,a_past_t,b_past_t,N[a_shrp_t,b_shrp_t,a_past_t,b_past_t,'S'], N[a_shrp_t,b_shrp_t,a_past_t,b_past_t,'P'], N[a_shrp_t,b_shrp_t,a_past_t,b_past_t,'B']
                    s += N[a_shrp_t,b_shrp_t,a_past_t,b_past_t,'S']
                    p += N[a_shrp_t,b_shrp_t,a_past_t,b_past_t,'P']
                    b += N[a_shrp_t,b_shrp_t,a_past_t,b_past_t,'B']

# now add the current scenario, with as much weight per outcome as all other scenarios combined
t = s+p+b
if __debug__:
    print a_shrp,b_shrp,a_past,b_past, \
        N[a_shrp,b_shrp,a_past,b_past,'S'], \
        N[a_shrp,b_shrp,a_past,b_past,'P'], \
        N[a_shrp,b_shrp,a_past,b_past,'B']
s += N[a_shrp,b_shrp,a_past,b_past,'S']*(t+1)
p += N[a_shrp,b_shrp,a_past,b_past,'P']*(t+1)
b += N[a_shrp,b_shrp,a_past,b_past,'B']*(t+1)
if __debug__:
    print 'S:' + str(s),'P:' + str(p),'B:' + str(b)

if (sharp(pa)>4):
    print 'P' # poke with a sword
elif (p >= s and p >= b and sharp(pb)>0):
    print 'B' # block an incoming poke
elif (s >= b and sharp(pa) > 0):
    print 'P' # poke if we expect them to sharpen
else:
    print 'S' # sharpen if we expect them to block