def paper(line):
    sides = map(int, line.split('x'))
    area1 = sides[0] * sides[1]
    area2 = sides[1] * sides[2]
    area3 = sides[2] * sides[0]
    return 2*(area1 + area2 + area3) + min(area1, area2, area3)

f = open('input.txt')
needed = 0
for line in f:
    needed += paper(line)

print needed
