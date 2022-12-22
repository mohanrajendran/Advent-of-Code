input = '01110110101001000'

def getNext(state):
    res = []
    for c in state:
        res.append(c)
    res.append('0')
    for c in reversed(state):
        if c == '0':
            res.append('1')
        else:
            res.append('0')

    return ''.join(res)

def getCheckSum(state):
    if len(state) % 2 == 1:
        return state

    res = []
    for i in range(0, len(state), 2):
        if state[i] == state[i+1]:
            res.append('1')
        else:
            res.append('0')

    return getCheckSum(''.join(res))


def part1():
    s = input
    while len(s) < 272:
        s = getNext(s)

    print(getCheckSum(s[:272]))

def part2():
    s = input
    while len(s) < 35651584:
        s = getNext(s)

    print(getCheckSum(s[:35651584]))

part1()
part2()

