class VM:
    def __init__(self):
        self.a = 1
        self.b = 0
        self.pc = 0

    def run(self, instructions):
        while self.pc >= 0 and self.pc < len(instructions):
            self.execute(instructions[self.pc])

        print self.b

    def execute(self, instruction):
        s = instruction.split()

        if s[0] == 'hlf':
            self.half(s[1])
        elif s[0] == 'tpl':
            self.triple(s[1])
        elif s[0] == 'inc':
            self.increment(s[1])
        elif s[0] == 'jmp':
            self.jump(s[1])
        elif s[0] == 'jie':
            self.jump_even(s[1], s[2])
        elif s[0] == 'jio':
            self.jump_one(s[1], s[2])
        else:
            self.pc += 1

    def half(self, register):
        if register == 'a':
            self.a /= 2
        else:
            self.b /= 2

        self.pc += 1

    def triple(self, register):
        if register == 'a':
            self.a *= 3
        else:
            self.b *= 3

        self.pc += 1

    def increment(self, register):
        if register == 'a':
            self.a += 1
        else:
            self.b += 1

        self.pc += 1

    def jump(self, offset):
        self.pc += int(offset)

    def jump_even(self, register, offset):
        if register == 'a,':
            if self.a % 2 == 0:
                self.jump(offset)
            else:
                self.pc += 1
        else:
            if self.b % 2 == 0:
                self.jump(offset)
            else:
                self.pc += 1

    def jump_one(self, register, offset):
        if register == 'a,':
            if self.a == 1:
                self.jump(offset)
            else:
                self.pc += 1
        else:
            if self.b == 1:
                self.jump(offset)
            else:
                self.pc += 1

f = open('input.txt', 'r')
instructions = [l.strip() for l in f]
vm = VM()
vm.run(instructions)
