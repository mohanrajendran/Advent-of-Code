def getNext(line):
    padded = '.' + line + '.'
    res = []
    for i in range(len(line)):
        if padded[i:i + 3] in ['^..', '^^.', '.^^', '..^']:
            res.append('^')
        else:
            res.append('.')
    return ''.join(res)


def getSafeTiles(line):
    return sum(1 for c in line if c == '.')


def getSafeTilesOverRows(starting, rows):
    s = 0
    line = starting
    for r in range(rows):
        s += getSafeTiles(line)
        line = getNext(line)

    return s


def part1():
    with open('input') as f:
        line = f.readline().strip()
        print(getSafeTilesOverRows(line, 40))


def part2():
    with open('input') as f:
        line = f.readline().strip()
        print(getSafeTilesOverRows(line, 400000))

part1()
part2()
