import re
from collections import deque
import sets

f = open('input.txt', 'r')
r = []

finished = False

for line in f:
    s = line.strip().split()

    if len(s) == 0:
        finished = True
        continue

    if not finished:
        r.append((s[0], s[2]))
    else:
        t = s[0]

steps = 0
while t != 'e':
#while steps == 0:
    choice = None
    maxChange = 0
    for p in r:
        target = p[0]
        dest = p[1]
        if dest in t:
            change = len(target)
            if change > maxChange:
                maxChange = change
                choice = p

    if choice == None:
        print 'Error'
        break

    t = re.sub(choice[1], choice[0], t, 1)
    steps += 1

print steps
