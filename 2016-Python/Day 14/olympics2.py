class Deer:
    def __init__(self, speed, runTime, restTime):
        self.speed = speed
        self.runTime = runTime
        self.restTime = restTime
        self.running = True
        self.phaseTime = 0
        self.distance = 0
        self.points = 0

    def increment(self):
        self.phaseTime += 1
        if self.running:
            self.distance += self.speed
            if self.phaseTime == self.runTime:
                self.phaseTime = 0
                self.running = False

        else:
            if self.phaseTime == self.restTime:
                self.phaseTime = 0
                self.running = True

f = open('input.txt', 'r')

deers = []

for line in f:
    s = line.split()
    speed = int(s[3])
    run = int(s[6])
    rest = int(s[-2])
    deers.append(Deer(speed, run, rest))

for t in range(2503):
    idx = 0
    maxDist = 0
    for (i, deer) in enumerate(deers):
        deer.increment()
        if deer.distance > maxDist:
            maxDist = deer.distance
            idx = i

    deers[idx].points += 1

print max(d.points for d in deers)
