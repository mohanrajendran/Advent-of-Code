from collections import defaultdict


def part1():
    with open('input') as f:
        counts = []
        for line in f.readlines():
            for i, c in enumerate(line.strip()):
                if len(counts) == i:
                    counts.append(defaultdict(int))
                counts[i][c] += 1

        res = []
        for i, c in enumerate(counts):
            leastCount = 0
            leastChar = ''
            for key in c:
                if c[key] > leastCount:
                    leastCount = c[key]
                    leastChar = key
            res.append(leastChar)

        print(''.join(res))


def part2():
    with open('input') as f:
        counts = []
        for line in f.readlines():
            for i, c in enumerate(line.strip()):
                if len(counts) == i:
                    counts.append(defaultdict(int))
                counts[i][c] += 1

        res = []
        for i, c in enumerate(counts):
            mostCount = 100000
            mostChar = ''
            for key in c:
                if c[key] < mostCount:
                    mostCount = c[key]
                    mostChar = key
            res.append(mostChar)

        print(''.join(res))


part1()
part2()
