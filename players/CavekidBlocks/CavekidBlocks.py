import sys, math, random
def count(a):
    s = 0
    for i in range(len(a)):
        if a[i] == 'P': s-=1
        elif a[i] == 'S': s+=1
        if s < 0: s = 0
    return s
kid = []
scary_adult = []
what2do = 'Sharpen the Stick! Why not? Adult may be doing the same. DONT trust adults!'
if len(sys.argv) > 1:
    kid, scary_adult = sys.argv[1].split(",")
    kid_stick_sharpness = count( kid )
    scary_adult_stick_sharpness = count( scary_adult )
    if (scary_adult_stick_sharpness >= 2):
        what2do = "Block! Block! Block! Adult's stick looks scary sharp."
    elif (kid_stick_sharpness > 0):
        what2do = 'Point your Stick to the adult. It may scary him.'
    else:
        what2do = 'Sharpen the Stick!'

    # Roll d20 for a courage check.
    dice = random.randint(1,20)
    if (dice > 15): what2do = 'Poke the adult! Critical Hit!'
    elif (dice <= 5): what2do = 'Block! Block! Block!'
print(what2do[0])