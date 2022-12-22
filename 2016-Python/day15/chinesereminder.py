def getSuitableStarts(totalPos, initialPos, distance):
    initialWait = ((10 * totalPos) - (initialPos + distance)) % totalPos
    wait = initialWait
    while True:
        yield wait
        wait += totalPos


def mergeGens(gen1, gen2):
    while True:
        v1 = next(gen1)
        v2 = next(gen2)
        while v1 != v2:
            if v1 < v2:
                v1 = next(gen1)
            else:
                v2 = next(gen2)
        yield v1


def part1():
    with open('input') as f:
        gen = None
        for line in f.readlines():
            s = line.strip().split()
            distance = int(s[1][1:])
            totalPos = int(s[3])
            initialPos = int(s[-1][:-1])
            if gen is None:
                gen = getSuitableStarts(totalPos, initialPos, distance)
            else:
                gen = mergeGens(gen, getSuitableStarts(totalPos, initialPos, distance))
        print(next(gen))


def part2():
    with open('input') as f:
        gen = None
        count = 1
        for line in f.readlines():
            s = line.strip().split()
            distance = int(s[1][1:])
            totalPos = int(s[3])
            initialPos = int(s[-1][:-1])
            if gen is None:
                gen = getSuitableStarts(totalPos, initialPos, distance)
            else:
                gen = mergeGens(gen, getSuitableStarts(totalPos, initialPos, distance))
            count += 1

        gen = mergeGens(gen, getSuitableStarts(11, 0, count))
        print(next(gen))


part1()
part2()
