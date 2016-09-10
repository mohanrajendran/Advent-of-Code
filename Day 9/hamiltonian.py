from itertools import permutations

class Nodes:
    def __init__(self):
        self.edges = {}
        self.vertices = []

    def add(self, line):
        s = line.split()
        start = s[0]
        end = s[2]
        dist = int(s[4])

        if start not in self.vertices:
            self.vertices.append(start)
        if end not in self.vertices:
            self.vertices.append(end)

        if start not in self.edges:
            self.edges[start] = {}
        if end not in self.edges:
            self.edges[end] = {}

        self.edges[start][end] = dist
        self.edges[end][start] = dist

    def find_dist(self, tour, distSoFar):
        if len(tour) == 1:
            return distSoFar
        else:
            if tour[1] not in self.edges[tour[0]]:
                return 0
            else:
                return self.find_dist(tour[1:], distSoFar + self.edges[tour[0]][tour[1]])

    def largest(self):
        dist = 0

        for p in permutations(self.vertices):
            dist = max(self.find_dist(p, 0), dist)

        return dist

f = open("input.txt", "r")
n = Nodes()
for line in f:
    n.add(line)

print n.largest()
