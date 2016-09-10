from sets import Set

def house_count(instruction):
    santa = [0,0]
    robo = [0,0]
    visited = Set()
    visited.add(tuple(santa))

    santaMove = True

    for c in instruction:
        if santaMove:
            current = santa
        else:
            current = robo
        if c == '^':
            current[1] += 1
        elif c == 'v':
            current[1] -= 1
        elif c == '<':
            current[0] -= 1
        elif c == '>':
            current[0] += 1

        tup = tuple(current)

        visited.add(tup)

        if santaMove:
            santa = current
        else:
            robo = current

        santaMove = not santaMove

    return len(visited)

f = open('input.txt', 'r')
for line in f:
    print house_count(line)
