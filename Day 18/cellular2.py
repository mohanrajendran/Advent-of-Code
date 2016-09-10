def live (a,i,j):
    if i < 0 or i >= len(a) or j < 0 or j >= len(a[0]):
        return 0

    return 1 if a[i][j] == '#' else 0

def advance(a):
    b = []

    for i in range(len(a)):
        t = []
        for j in range(len(a[0])):
            onNeighbors = 0
            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    if k == 0 and l == 0:
                        continue
                    onNeighbors += live(a, i+k, j+l)

            if a[i][j] == '#':
                if onNeighbors == 2 or onNeighbors == 3:
                    t.append('#')
                else:
                    t.append('.')
            else:
                if onNeighbors == 3:
                    t.append('#')
                else:
                    t.append('.')

        b.append(t)

    b[0][0] = '#'
    b[0][-1] = '#'
    b[-1][0] = '#'
    b[-1][-1] = '#'

    return b

def printCell(a):
    for line in a:
        print "".join(line)


f = open('input.txt', 'r')
a = [list(l.strip()) for l in f]

for i in range(100):
    a[0][0] = '#'
    a[0][-1] = '#'
    a[-1][0] = '#'
    a[-1][-1] = '#'
    a = advance(a)

print sum(sum(live(a,i,j) for i in range(len(a))) for j in range(len(a[0])))
