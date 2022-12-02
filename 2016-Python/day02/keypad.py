delta = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

keypad1 = [
    '123',
    '456',
    '789'
]

keypad2 = [
    '00100',
    '02340',
    '56789',
    '0ABC0',
    '00D00'
]


class Keypad():
    def __init__(self, keypad):
        self.keypad = keypad
        self.setStart()

    def setStart(self):
        for x in range(len(self.keypad)):
            for y in range(len(self.keypad[0])):
                if self.keypad[x][y] == '5':
                    self.loc = (x, y)
                    return

    def step(self, direction):
        (dx, dy) = delta[direction]
        (x, y) = self.loc
        (nx, ny) = (x + dx, y + dy)
        if nx < 0 or ny < 0 \
                or nx == len(self.keypad) or ny == len(self.keypad[0]) \
                or self.keypad[nx][ny] == '0':
            return

        self.loc = (nx, ny)

    def getCurrentKey(self):
        (x, y) = self.loc
        return self.keypad[x][y]


def part1():
    keypad = Keypad(keypad1)
    with open('input') as f:
        lines = f.readlines()
        buttons = []
        for line in lines:
            for direction in line.strip():
                keypad.step(direction)
            buttons.append(keypad.getCurrentKey())

        print(''.join(buttons))


def part2():
    keypad = Keypad(keypad2)
    with open('input') as f:
        lines = f.readlines()
        buttons = []
        for line in lines:
            for direction in line.strip():
                keypad.step(direction)
            buttons.append(keypad.getCurrentKey())

        print(''.join(buttons))


part1()
part2()
