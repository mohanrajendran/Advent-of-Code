from sets import Set
import re

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

s = Set()

for p in r:
    target = p[0]
    dest = p[1]

    for occ in re.finditer(target, t):
        n = t[:occ.start()] + dest + t[occ.end():]
        s.add(n)

print len(s)
