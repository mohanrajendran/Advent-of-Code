from itertools import *

f = open('input.txt', 'r')
n = map(int, f)
v = 150

found = False
count = 0
for i in range(1, len(n)+1):
    for c in combinations(n, i):
        if sum(c) == v:
            found = True
            count += 1
    if found:
        break

print count

