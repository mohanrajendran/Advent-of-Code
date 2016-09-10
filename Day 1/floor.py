def move(instruction, floor):
    for c in instruction:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
    return floor

f = open('input.txt', 'r')

floor = 0
for line in f:
    floor = move(line, floor)

print floor

