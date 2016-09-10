from itertools import *
import sys

def winnable(enemyStats, playerStats):
    eHp = enemyStats[0]
    eDm = enemyStats[1]
    eAr = enemyStats[2]

    pHp = playerStats[0]
    pDm = playerStats[1]
    pAr = playerStats[2]

    # player attacks
    damage = max(1, pDm - eAr)
    eHp = eHp - damage
    if eHp <= 0:
        return True

    # enemy attacks
    damage = max(1, eDm - pAr)
    pHp = pHp - damage
    if pHp <= 0:
        return False

    return winnable((eHp, eDm, eAr), (pHp, pDm, pAr))

weapons = [(8,4), (10,5), (25,6), (40,7), (74,8)]
armors = [(13,1), (31,2), (53,3), (75,4), (102,5), (0,0)]
rings = [(25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3), (0,0,0), (0,0,0)]

f = open('input.txt', 'r')
hp = int(f.readline().split(':')[1])
damage = int(f.readline().split(':')[1])
armor = int(f.readline().split(':')[1])

maxCost = 0

for w in combinations(weapons,1):
    for a in combinations(armors, 1):
        for r in combinations(rings, 2):
            enemy = (hp, damage, armor)
            player = (100,
                      w[0][1] + r[0][1] + r[1][1],
                      a[0][1] + r[0][2] + r[1][2])
            cost = w[0][0] + a[0][0] + r[0][0] + r[1][0]

            if not winnable(enemy, player):
                maxCost = max(cost, maxCost)

print maxCost

