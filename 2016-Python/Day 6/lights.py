class Lights:
    def __init__(self):
        self.lights = [[False for _ in xrange(1000)] for _ in xrange(1000)]

    def num_lit(self):
        count = 0
        for i in xrange(1000):
            for j in xrange(1000):
                if self.lights[i][j]:
                    count += 1
        return count

    def toggle(self, x1, y1, x2, y2):
        for i in xrange(x1, x2+1):
            for j in xrange(y1, y2+1):
                self.lights[i][j] = not self.lights[i][j]

    def turn(self, x1, y1, x2, y2, option):
        for i in xrange(x1, x2+1):
            for j in xrange(y1, y2+1):
                self.lights[i][j] = option

    def parse(self, line):
        words = line.split()
        if words[0] == 'toggle':
            p1 = map(int, words[1].split(','))
            p2 = map(int, words[3].split(','))
            self.toggle(p1[0], p1[1], p2[0], p2[1])
        elif words[0] == 'turn':
            p1 = map(int, words[2].split(','))
            p2 = map(int, words[4].split(','))
            self.turn(p1[0], p1[1], p2[0], p2[1], words[1] == 'on')

l = Lights()
f = open('input.txt', 'r')
for line in f:
    l.parse(line)

print l.num_lit()
