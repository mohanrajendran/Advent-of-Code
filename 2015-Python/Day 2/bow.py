def ribbon(line):
    sides = map(int, line.split('x'))
    perimeter1 = 2*(sides[0] + sides[1])
    perimeter2 = 2*(sides[1] + sides[2])
    perimeter3 = 2*(sides[2] + sides[0])
    volume = sides[0] * sides[1] * sides[2]

    return volume + min(perimeter1, perimeter2, perimeter3)


f = open('input.txt')
needed = 0
for line in f:
    needed += ribbon(line)

print needed
