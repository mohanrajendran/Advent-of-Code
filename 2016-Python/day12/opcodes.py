def run(instructions, registers):
    pc = 0
    while pc < len(instructions):
        ops = instructions[pc]
        if ops[0] == 'cpy':
            if ops[1] in ['a', 'b', 'c', 'd']:
                value = registers[ops[1]]
            else:
                value = int(ops[1])
            registers[ops[2]] = value
            pc += 1
        elif ops[0] == 'inc':
            registers[ops[1]] += 1
            pc += 1
        elif ops[0] == 'dec':
            registers[ops[1]] -= 1
            pc += 1
        elif ops[0] == 'jnz':
            if ops[1] in ['a', 'b', 'c', 'd']:
                value = registers[ops[1]]
            else:
                value = int(ops[1])
            if value != 0:
                pc += int(ops[2])
            else:
                pc += 1
def part1():
    with open('input') as f:
        instructions = list(map(lambda s: s.strip().split(), f.readlines()))

        registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        run(instructions, registers)

        print(registers['a'])

def part2():
    with open('input') as f:
        instructions = list(map(lambda s: s.strip().split(), f.readlines()))

        registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
        run(instructions, registers)

        print(registers['a'])

part1()
part2()