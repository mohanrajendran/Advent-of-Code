def combo_generator(n, numbers):
    if numbers == 1:
        yield [n]
    else:
        for i in xrange(n+1):
            for j in combo_generator(n-i, numbers-1):
                a = [i]
                a.extend(j)
                yield a

def calories(c, cal):
    return sum(c[i] * cal[i] for i in range(len(c)))

def score(p, c):
    capacity = max(0, sum(p[i][0] * c[i] for i in range(len(c))))
    durability = max(0, sum(p[i][1] * c[i] for i in range(len(c))))
    flavor = max(0, sum(p[i][2] * c[i] for i in range(len(c))))
    texture = max(0, sum(p[i][3] * c[i] for i in range(len(c))))

    return capacity * durability * flavor * texture

f = open('input.txt', 'r')
a = []
cal = []
for line in f:
    s = line.split()
    c = int(s[2][:-1])
    d = int(s[4][:-1])
    f = int(s[6][:-1])
    t = int(s[8][:-1])
    cl = int(s[10])

    a.append([c,d,f,t])
    cal.append(cl)

maxScore = 0
for c in combo_generator(100, len(a)):
    if calories(c, cal) == 500:
        maxScore = max(score(a, c), maxScore)

print maxScore
