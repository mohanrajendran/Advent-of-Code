import re
import collections
import functools


class Count:
    def __init__(self, c, count):
        self.c = c
        self.count = count

    def __repr__(self) -> str:
        return f'[{self.c}, {self.count}]'


@functools.cmp_to_key
def cmp(c1: Count, c2: Count):
    if c1.count > c2.count:
        return 1
    elif c1.count < c2.count:
        return -1
    elif ord(c1.c) > ord(c2.c):
        return -1
    else:
        return 1


class Room:
    pattern = re.compile("^([a-z\-]+)-(\d+)\[(\w+)\]$")

    def __init__(self, s):
        matches = Room.pattern.match(s)
        self.name, self.sector, self.checksum = matches.groups()

    def isValid(self) -> bool:
        counts = collections.defaultdict(int)
        for char in self.name:
            if char == '-':
                continue
            counts[char] += 1
        keys = list(Count(key, counts[key]) for key in counts)
        keys.sort(key=cmp, reverse=True)
        return self.checksum == ''.join(map(lambda x: x.c, keys[:5]))

    def getSectorId(self) -> int:
        return int(self.sector)

    def rotate(self) -> str:
        rot = self.getSectorId() % 26
        res = []
        for c in self.name:
            if c == '-':
                res.append(' ')
            else:
                off = ord(c) - ord('a')
                newOff = (off + rot) % 26
                res.append(chr(ord('a') + newOff))

        return ''.join(res)


def part1():
    with open('input') as f:
        sums = 0
        for line in f.readlines():
            r = Room(line)
            if r.isValid():
                sums += r.getSectorId()

    print(sums)


def part2():
    with open('input') as f:
        for line in f.readlines():
            r = Room(line)
            if r.isValid():
                if r.rotate() == 'northpole object storage':
                    print(r.getSectorId())
                    return


part1()
part2()
