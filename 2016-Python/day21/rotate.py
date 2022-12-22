def parseInstructions(lines):
    instructions = []
    for line in lines:
        s = line.strip().split()
        if s[0] == 'swap' and s[1] == 'position':
            instructions.append(('swapPosition', int(s[2]), int(s[5])))
        elif s[0] == 'swap' and s[1] == 'letter':
            instructions.append(('swapLetter', s[2], s[5]))
        elif s[0] == 'rotate' and s[1] == 'based':
            instructions.append(('rotateBased', s[6]))
        elif s[0] == 'rotate':
            instructions.append(('rotate', s[1], int(s[2])))
        elif s[0] == 'reverse':
            instructions.append(('reverse', int(s[2]), int(s[4])))
        else:
            instructions.append(('move', int(s[2]), int(s[5])))

    return instructions


def swapPosition(s: str, pos1: int, pos2: int) -> str:
    l = list(s)
    l[pos1], l[pos2] = l[pos2], l[pos1]
    return ''.join(l)


def swapLetter(s: str, l1: str, l2: str) -> str:
    return swapPosition(s, s.find(l1), s.find(l2))


def rotate(s: str, direction: str, steps: int, unscramble: bool = False) -> str:
    if unscramble:
        direction = 'left' if direction == 'right' else 'right'
    steps %= len(s)
    if direction == 'right':
        steps = len(s) - steps
    return (s + s)[steps: steps + len(s)]


def rotateBased(s: str, letter: str, unscramble: bool = False) -> str:
    if unscramble:
        for i in range(len(s)):
            if rotateBased(rotate(s, 'left', i), letter) == s:
                return rotate(s, 'left', i)

    location = s.find(letter)
    rotates = 1 + location
    if location >= 4:
        rotates += 1
    return rotate(s, 'right', rotates)


def reverse(s: str, pos1: int, pos2: int) -> str:
    l = list(s)
    while pos1 < pos2:
        l[pos1], l[pos2] = l[pos2], l[pos1]
        pos1 += 1
        pos2 -= 1
    return ''.join(l)


def move(s: str, pos1: int, pos2: int, unscramble: bool = False) -> str:
    if unscramble:
        return move(s, pos2, pos1)
    c = s[pos1]
    removed = s[:pos1] + s[pos1 + 1:]
    return removed[:pos2] + c + removed[pos2:]


def part1():
    password = 'abcdefgh'
    with open('input') as f:
        instructions = parseInstructions(f.readlines())
        for i in instructions:
            if i[0] == 'swapPosition':
                password = swapPosition(password, i[1], i[2])
            elif i[0] == 'swapLetter':
                password = swapLetter(password, i[1], i[2])
            elif i[0] == 'rotateBased':
                password = rotateBased(password, i[1])
            elif i[0] == 'rotate':
                password = rotate(password, i[1], i[2])
            elif i[0] == 'reverse':
                password = reverse(password, i[1], i[2])
            else:
                password = move(password, i[1], i[2])

    print(password)


def part2():
    password = 'fbgdceah'
    with open('input') as f:
        instructions = parseInstructions(f.readlines())
        for i in reversed(instructions):
            if i[0] == 'swapPosition':
                password = swapPosition(password, i[1], i[2])
            elif i[0] == 'swapLetter':
                password = swapLetter(password, i[1], i[2])
            elif i[0] == 'rotateBased':
                password = rotateBased(password, i[1], True)
            elif i[0] == 'rotate':
                password = rotate(password, i[1], i[2], True)
            elif i[0] == 'reverse':
                password = reverse(password, i[1], i[2])
            else:
                password = move(password, i[1], i[2], True)

    print(password)

part1()
part2()
