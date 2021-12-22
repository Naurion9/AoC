from itertools import product
from collections import defaultdict

def DicePoints(step: int):
    throw1 = (3 * step - 2) % 100
    throw2 = (3 * step - 1) % 100
    throw3 = (3 * step) % 100
    throw1 = 100 if throw1 == 0 else throw1
    throw2 = 100 if throw2 == 0 else throw2
    throw3 = 100 if throw3 == 0 else throw3
    return throw1 + throw2 + throw3 

def Part1(p1Pos, p2Pos):
    p1Points = 0
    p2Points = 0
    step = 0
    while True:
        step += 1
        throwPoints = DicePoints(step)
        if step % 2 == 0:
            moves = (p2Pos + throwPoints) % 10
            p2Pos = moves if moves != 0 else 10 
            p2Points += p2Pos
        else:
            moves = (p1Pos + throwPoints) % 10
            p1Pos = moves if moves != 0 else 10
            p1Points += p1Pos
        if p1Points == 1000 or p2Points == 1000:
            break
    print(f'Part 1 sol: {min(p1Points, p2Points)} * {step * 3} = {min(p1Points, p2Points) * step * 3}')

def AddSituations(situations: dict, diceRes: list, step: int):
    newSit = defaultdict(int)
    if step % 2 == 1:
        for points1, pos1, points2, pos2 in situations.keys():   
            for diceFace, occurrences in diceRes.items():
                newpos = (pos1 + diceFace) % 10 or 10
                newSit[points1 + newpos, newpos, points2, pos2] += situations[points1, pos1, points2, pos2] * occurrences
    else:
        for points1, pos1, points2, pos2 in situations.keys():   
            for diceFace, occurrences in diceRes.items():
                newpos = (pos2 + diceFace) % 10 or 10
                newSit[points1, pos1, points2 + newpos, newpos] += situations[points1, pos1, points2, pos2] * occurrences
    return newSit

def Part2(p1Pos, p2Pos):
    p1Points = 0
    p2Points = 0
    winP1 = 0
    winP2 = 0
    possibleRes = [sum(d) for d in product((1, 2, 3), repeat=3)]
    diceResCount = {r: possibleRes.count(r) for r in set(possibleRes)}
    situations = defaultdict(int)
    situations[p1Points, p1Pos, p2Points, p2Pos] = 1 
    step = 1 
    while situations:
        situations = AddSituations(situations, diceResCount, step)        
        for p1Points, posP1, p2Points, posP2 in list(situations.keys()):
            if p1Points >= 21:
                winP1 += situations[(p1Points, posP1, p2Points, posP2)]
                del situations[(p1Points, posP1, p2Points, posP2)]
            elif p2Points >= 21:
                winP2 += situations[(p1Points, posP1, p2Points, posP2)]
                del situations[(p1Points, posP1, p2Points, posP2)]
        step += 1
    print(f'Part 2 sol: {max(winP1, winP2)}')


p1Pos = 4
p2Pos = 9
Part1(p1Pos, p2Pos)
Part2(p1Pos, p2Pos)
