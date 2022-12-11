import re

ipv7Re = re.compile("(\w+)")


def containsAbba(s: str) -> bool:
    for i in range(3, len(s)):
        if s[i] == s[i-3] and s[i-2] == s[i-1] and s[i] != s[i-1]:
            return True
    return False


def findBabs(s: str):
    res = []
    for i in range(2, len(s)):
        if s[i] == s[i-2] and s[i] != s[i-1]:
            res.append(s[i-1] + s[i] + s[i-1])
    return res


def containsBabs(s: str, babs):
    for bab in babs:
        if bab in s:
            return True
    return False


def part1():
    with open('input') as f:
        counts = 0
        for line in f.readlines():
            sequences = ipv7Re.findall(line.strip())
            without = sequences[::2]
            within = sequences[1::2]
            if all(not containsAbba(s) for s in within) \
                    and any(containsAbba(s) for s in without):
                counts += 1

        print(counts)


def part2():
    with open('input') as f:
        counts = 0
        for line in f.readlines():
            sequences = ipv7Re.findall(line.strip())
            without = sequences[::2]
            within = sequences[1::2]
            babs = set()
            for seq in without:
                for bab in findBabs(seq):
                    babs.add(bab)
            if any(containsBabs(s, babs) for s in within):
                counts += 1

        print(counts)


part1()
part2()
