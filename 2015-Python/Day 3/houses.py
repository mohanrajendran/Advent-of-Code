from sets import Set

def house_count(instruction):
    current = [0,0]
    visited = Set()
    visited.add(tuple(current))
    for c in instruction:
        if c == '^':
            current[1] += 1
        elif c == 'v':
            current[1] -= 1
        elif c == '<':
            current[0] -= 1
        elif c == '>':
            current[0] += 1

        tup = tuple(current)

        if tup not in visited:
            visited.add(tup)

    return len(visited)

f = open('input.txt', 'r')
for line in f:
    print house_count(line)
