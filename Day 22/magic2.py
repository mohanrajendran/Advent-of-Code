from heapq import *
from copy import *

class Player:
    def __init__(self):
        self.hp = 50
        self.mana = 500
        self.armor = 0
        self.shieldTurns = 0
        self.rechargeTurns = 0

class Enemy:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.damage = dmg
        self.poisonTurns = 0


f = open('input.txt', 'r')
hp = int(f.readline().split(':')[1])
dmg = int(f.readline().split(':')[1])

heap = []
heappush(heap, (0, Player(), Enemy(hp, dmg)))
gameOver = False

while not gameOver:
    # get current state
    state = heappop(heap)
    manaUsed = state[0]
    player = state[1]
    enemy = state[2]

    player.hp -= 1

    if player.hp <= 0:
        continue

    # apply effects
    ## shield
    if player.shieldTurns > 0:
        player.armor = 7
        player.shieldTurns -= 1
    else:
        player.armor = 0

    ## poison
    if enemy.poisonTurns > 0:
        enemy.hp -= 3
        enemy.poisonTurns -= 1

    ## recharge
    if player.rechargeTurns > 0:
        player.mana += 101
        player.rechargeTurns -= 1

    if enemy.hp <= 0:
        print manaUsed
        gameOver = True
        break

    # Player turns
    newStates = []
    ## magic missile
    if player.mana >= 53:
        np = copy(player)
        ne = copy(enemy)
        np.mana -= 53
        ne.hp -= 4
        newStates.append((manaUsed+53, np, ne))
    ## drain
    if player.mana >= 73:
        np = copy(player)
        ne = copy(enemy)
        np.hp += 2
        np.mana -= 73
        ne.hp -= 2
        newStates.append((manaUsed+73, np, ne))
    ## shield
    if player.shieldTurns == 0 and player.mana >= 113:
        np = copy(player)
        ne = copy(enemy)
        np.shieldTurns = 6
        newStates.append((manaUsed+113, np, ne))
    ## poison
    if enemy.poisonTurns == 0 and player.mana >= 173:
        np = copy(player)
        ne = copy(enemy)
        np.mana -= 173
        ne.poisonTurns = 6
        newStates.append((manaUsed+173, np, ne))
    ## recharge
    if player.rechargeTurns == 0 and player.mana >= 229:
        np = copy(player)
        ne = copy(enemy)
        np.mana -= 229
        np.rechargeTurns = 5
        newStates.append((manaUsed+229, np, ne))

    # continue if no move found
    if len(newStates) == 0:
         continue

    # player turn
    for newState in newStates:
        manaUsed = newState[0]
        player = newState[1]
        enemy = newState[2]

        if enemy.hp <= 0:
            print manaUsed
            gameOver = True
            break

        # apply effects
        ## shield
        if player.shieldTurns > 0:
            player.armor = 7
            player.shieldTurns -= 1
        else:
            player.armor = 0

        ## poison
        if enemy.poisonTurns > 0:
            enemy.hp -= 3
            enemy.poisonTurns -= 1

        ## recharge
        if player.rechargeTurns > 0:
            player.mana += 101
            player.rechargeTurns -= 1

        if enemy.hp <= 0:
            print manaUsed
            gameOver = True
            break

        # enemy attacks
        np = copy(player)
        ne = copy(enemy)
        damage = max(1, ne.damage - np.armor)
        np.hp -= damage

        heappush(heap, (manaUsed, np, ne))
