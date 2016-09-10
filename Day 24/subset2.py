from itertools import *
import sys
from sets import Set

def partitionable(packages, target, n):
    if n == 0:
        return True

    for i in range(1, len(packages)+1) :
        for selection in combinations(packages, i):
            if sum(selection) == target:
                remaining = packages - Set(selection)
                if partitionable(remaining, target, n-1):
                    return True
    return False


f = open('input.txt', 'r')
packages = Set(map(int, f))
target = sum(packages)/4

count = 1
found = False

while not found:
    entanglement = sys.maxint

    for selection in combinations(packages, count):
        if sum(selection) == target:
            remaining = packages - Set(selection)
            if partitionable(remaining, target, 2):
                ent = reduce(lambda x,y: x*y, selection, 1)
                if not found:
                    entanglement = ent
                    found = True
                else:
                    entanglement = min(ent, entanglement)

    if found:
        print entanglement

    count += 1
    if count > len(packages):
        break
