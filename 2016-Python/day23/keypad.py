def getValue(registers, ptr):
    if ptr in registers:
        return registers[ptr]
    else:
        return int(ptr)


def run(instructions, registers):
    pc = 0
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
        elif ops[0] == 'tgl':
            target = pc + getValue(registers, ops[1])
            if 0 <= target < len(instructions):
                if instructions[target][0] == 'inc':
                    instructions[target][0] = 'dec'
                elif instructions[target][0] == 'dec':
                    instructions[target][0] = 'inc'
                elif instructions[target][0] == 'tgl':
                    instructions[target][0] = 'inc'
                elif instructions[target][0] == 'jnz':
                    instructions[target][0] = 'cpy'
                elif instructions[target][0] == 'cpy':
                    instructions[target][0] = 'jnz'
            pc += 1
        else:
            pc += 1


def part1():
    with open('input') as f:
        instructions = list(map(lambda s: s.strip().split(), f.readlines()))

        registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
        run(instructions, registers)

        print(registers['a'])

def part2():
    with open('input') as f:
        instructions = list(map(lambda s: s.strip().split(), f.readlines()))

        registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
        run(instructions, registers)

        print(registers['a'])


part1()
part2()
