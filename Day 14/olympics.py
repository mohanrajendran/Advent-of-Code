time = 2503

def dist(line):
    global time
    s = line.split()
    speed = int(s[3])
    run = int(s[6])
    rest = int(s[-2])


    t = time
    d = 0

    running = True
    while t > 0:
        if running:
            runTime = min(t, run)
            d += runTime * speed
            t -= run
        else:
            t -= rest
        running = not running

    return d

f = open('input.txt', 'r')
maxDist = 0;

for line in f:
    maxDist = max(dist(line), maxDist)

print maxDist
