class Circuit:
    def __init__(self):
        self.deps = {}
        self.evaluated = {}

    def parse(self, line):
        tokens = line.split()
        arity = tokens.index('->')

        target = tokens[arity+1]
        operation = tokens[:arity]

        self.deps[target] = operation

    def evaluate(self, target):
        if target in self.evaluated:
            return self.evaluated[target]

        if target.isdigit():
            self.evaluated[target] = int(target)
            return self.evaluated[target]

        operation = self.deps[target]

        # one element operation - assignment
        if len(operation) == 1:
            self.evaluated[target] = self.evaluate(operation[0])

        # two element operation - NOT
        elif len(operation) == 2:
            v = self.evaluate(operation[1])
            self.evaluated[target] = v ^ 0xffff

        # three element operation - LSHIFT, RSHIFT, AND, OR
        elif len(operation) == 3:
            v1 = self.evaluate(operation[0])
            v2 = self.evaluate(operation[2])
            op = operation[1]

            #bitwise AND
            if op == 'AND':
                self.evaluated[target] = v1 & v2
            if op == 'OR':
                self.evaluated[target] = v1 | v2
            if op == 'LSHIFT':
                self.evaluated[target] = (v1 << v2) % 65536
            if op == 'RSHIFT':
                self.evaluated[target] = v1 >> v2

        return self.evaluated[target]

f = open('input.txt', 'r')
c = Circuit()
for line in f:
    c.parse(line)

print c.evaluate('a')
