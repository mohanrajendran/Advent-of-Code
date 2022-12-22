from __future__ import annotations
import re

dfRe = re.compile(r'^\/dev\/grid\/node-x(\d+)-y(\d+)\s*(\d+)T\s*(\d+)T\s*(\d+)T\s*(\d+)%$')


class Node:
    def __init__(self, line):
        groups = dfRe.match(line.strip()).groups()
        self.x = int(groups[0])
        self.y = int(groups[1])
        self.size = int(groups[2])
        self.used = int(groups[3])
        self.avail = int(groups[4])
        self.perc = int(groups[5])


def part1():
    with open('input') as f:
        nodes = []
        for line in f.readlines()[2:]:
            nodes.append(Node(line))

        count = 0
        for i1 in range(len(nodes)):
            for i2 in range(len(nodes)):
                if i1 == i2:
                    continue
                n1 = nodes[i1]
                n2 = nodes[i2]

                if n1.used != 0 and n2.avail >= n1.used:
                    count += 1
        print(count)


def part2():
    with open('input') as f:
        nodes = {}
        maxy = -1
        maxx = -1
        emptyx = -1
        emptyy = -1
        for line in f.readlines()[2:]:
            n = Node(line)
            maxx = max(maxx, n.x)
            maxy = max(maxy, n.y)
            nodes[(n.x, n.y)] = n
            if n.used == 0:
                emptyx, emptyy = n.x, n.y

        for y in range(maxy + 1):
            for x in range(maxx + 1):
                if x == 0 and y == 0:
                    print('X', end='')
                elif x == emptyx and y == emptyy:
                    print("E", end='')
                elif x == maxx and y == 0:
                    print("G", end='')
                elif nodes[(x, y)].used >= nodes[(emptyx, emptyy)].avail:
                    print("#", end='')
                else:
                    print('.', end='')
            print()

        print(emptyx + emptyy + (maxx-1) + (maxx-1)*5 + 1)


part1()
part2()
