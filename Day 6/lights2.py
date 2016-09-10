class Lights:
    def __init__(self):
        self.lights = [[0 for _ in xrange(1000)] for _ in xrange(1000)]

    def brightness(self):
        count = 0
        for i in xrange(1000):
            for j in xrange(1000):
                count += self.lights[i][j]
        return count

    def toggle(self, x1, y1, x2, y2):
        for i in xrange(x1, x2+1):
            for j in xrange(y1, y2+1):
                self.lights[i][j] += 2

    def turn(self, x1, y1, x2, y2, on):
        for i in xrange(x1, x2+1):
            for j in xrange(y1, y2+1):
                if on:
                    self.lights[i][j] += 1
                else:
                    self.lights[i][j] = max(0, self.lights[i][j]-1)

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

print l.brightness()
