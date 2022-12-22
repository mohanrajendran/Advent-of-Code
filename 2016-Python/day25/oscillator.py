class OscillatorTracker:
    def __init__(self):
        self.seenRegisters = {0: set(), 1: set()}
        self.prev = 1

    def tick(self, output, registers):
        if (output != 0 and output != 1) or output == self.prev:
            return 'INVALID'

        self.prev = output
        reg = (registers['a'], registers['b'], registers['c'], registers['d'])
        if reg in self.seenRegisters[output]:
            return 'VALID'
        else:
            self.seenRegisters[output].add(reg)
            return 'INCONCLUSIVE'


def getValue(registers, ptr):
    if ptr in registers:
        return registers[ptr]
    else:
        return int(ptr)


def run(instructions, registers):
    pc = 0
    ot = OscillatorTracker()
    while pc < len(instructions):
        ops = instructions[pc]
        if ops[0] == 'cpy':
            registers[ops[2]] = getValue(registers, ops[1])
            pc += 1
        elif ops[0] == 'inc':
            registers[ops[1]] += 1
            pc += 1
        elif ops[0] == 'dec':
            registers[ops[1]] -= 1
            pc += 1
        elif ops[0] == 'jnz':
            if getValue(registers, ops[1]) != 0:
                pc += int(getValue(registers, ops[2]))
            else:
                pc += 1
        elif ops[0] == 'out':
            result = ot.tick(getValue(registers, ops[1]), registers)
            if result == 'INVALID':
                return False
            elif result == 'VALID':
                return True
            pc += 1
        else:
            pc += 1


def part1():
    with open('input') as f:
        instructions = list(map(lambda s: s.strip().split(), f.readlines()))

        idx = 0
        while True:
            registers = {'a': idx, 'b': 0, 'c': 0, 'd': 0}
            if run(instructions, registers):
                print(idx)
                return

            idx += 1


part1()
