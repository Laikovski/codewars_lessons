# Alphabet war - Wo lo loooooo priests join the war
# Task
#
# Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.
#
# The left side letters and their power:
#
#  w - 4
#  p - 3
#  b - 2
#  s - 1
#  t - 0 (but it's priest with Wo lo loooooooo power)
#
# The right side letters and their power:
#
#  m - 4
#  q - 3
#  d - 2
#  z - 1
#  j - 0 (but it's priest with Wo lo loooooooo power)

def alphabet_war(fight):
    lPower = {"w": 4, "p": 3, "b": 2, "s": 1}
    rPower = {"m": 4, "q": 3, "d": 2, "z": 1}
    convert = {"w": "m", "m": "w", "p": "q", "q": "p",
               "b": "d", "d": "b", "s": "z", "z": "s"}
    fight = list("a" + fight + "a")
    for i, c in enumerate(fight[:-1]):
        if i == 0: continue
        inL, inR = c in lPower, c in rPower
        adjacent = {fight[i - 1], fight[i + 1]}
        if adjacent == {"j", "t"}: continue
        if (inL and "j" in adjacent) or (inR and "t" in adjacent):
            fight[i] = convert[c]
    lScore = sum(lPower.get(x, 0) for x in fight)
    rScore = sum(rPower.get(x, 0) for x in fight)
    if lScore < rScore:
        return "Right side wins!"
    elif lScore > rScore:
        return "Left side wins!"
    else:
        return "Let's fight again!"