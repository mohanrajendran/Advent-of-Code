from itertools import permutations
import sys

class Table:
    def __init__(self):
        self.happiness = {}
        self.guests = []

    def add(self, line):
        s = line.split()
        guest1 = s[0]
        guest2 = s[-1][:-1]

        h = int(s[3])
        if s[2] == 'lose':
            h *= -1

        if guest1 not in self.happiness:
            self.happiness[guest1] = {}
        if guest1 not in self.guests:
            self.guests.append(guest1)

        self.happiness[guest1][guest2] = h

    def happily(self, p):
        h = 0

        for i in range(len(p)):
            g = p[i]
            gl = p[i-1]
            if i == len(p)-1:
                gr = p[0]
            else:
                gr = p[i+1]

            h += self.happiness[g][gl] + self.happiness[g][gr]

        return h


    def optimal(self):
        happy = -sys.maxint -1

        for p in permutations(self.guests):
            happy = max(happy, self.happily(p))

        return happy

f = open("input.txt", "r")
t = Table()
for line in f:
    t.add(line)
t.happiness['self'] = {}
for guest in t.guests:
    t.happiness['self'][guest] = 0
    t.happiness[guest]['self'] = 0
t.guests.append('self')

print t.optimal()
