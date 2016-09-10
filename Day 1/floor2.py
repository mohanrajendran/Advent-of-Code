def move(c, floor):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    return floor

f = open('input.txt', 'r')

floor = 0
idx = 0
for line in f:
    for c in line:
        floor = move(c, floor)
        idx += 1
        if floor < 0:
            break
    if floor < 0:
        break

print idx

