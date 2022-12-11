import re

rectRe = re.compile("^rect (\d+)x(\d+)$")
rowRotRe = re.compile("^rotate row y=(\d+) by (\d+)$")
colRotRe = re.compile("^rotate column x=(\d+) by (\d+)$")


class Screen:
    def __init__(self):
        self.screen = [['.'] * 50 for i in range(6)]

    def apply(self, instruction):
        if rectRe.match(instruction):
            groups = rectRe.match(instruction).groups()
            for row in range(int(groups[1])):
                for col in range(int(groups[0])):
                    self.screen[row][col] = '#'
        elif rowRotRe.match(instruction):
            groups = rowRotRe.match(instruction).groups()
            row = int(groups[0])
            rot = int(groups[1])
            copy = [self.screen[row][i] for i in range(50)]
            for i in range(50):
                source = (i - rot + 50) % 50
                self.screen[row][i] = copy[source]
        elif colRotRe.match(instruction):
            groups = colRotRe.match(instruction).groups()
            col = int(groups[0])
            rot = int(groups[1])
            copy = [self.screen[i][col] for i in range(6)]
            for i in range(6):
                source = (i - rot + 6) % 6
                self.screen[i][col] = copy[source]

    def count(self):
        counts = 0
        for row in self.screen:
            for c in row:
                if c == '#':
                    counts += 1
        return counts

    def __repr__(self):
        return '\n'.join(map(lambda r: ''.join(r), self.screen))


def part1():
    s = Screen()
    with open('input') as f:
        for line in f.readlines():
            s.apply(line.strip())

    print(s.count())


def part2():
    s = Screen()
    with open('input') as f:
        for line in f.readlines():
            s.apply(line.strip())

    print(s)


part1()
part2()
