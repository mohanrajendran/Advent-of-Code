from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


nextDirections = {
    'L': {
        Direction.NORTH: Direction.WEST,
        Direction.WEST: Direction.SOUTH,
        Direction.SOUTH: Direction.EAST,
        Direction.EAST: Direction.NORTH
    },
    'R': {
        Direction.NORTH: Direction.EAST,
        Direction.EAST: Direction.SOUTH,
        Direction.SOUTH: Direction.WEST,
        Direction.WEST: Direction.NORTH
    }
}

move = {
    Direction.NORTH: (0, 1),
    Direction.SOUTH: (0, -1),
    Direction.EAST: (1, 0),
    Direction.WEST: (-1, 0)
}


class Location():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = Direction.NORTH

    def step(self, instruction: int):
        turn = instruction[0]
        steps = int(instruction[1:])
        self.dir = nextDirections[turn][self.dir]
        visitedLocs = []
        for s in range(steps):
            self.x += move[self.dir][0]
            self.y += move[self.dir][1]
            visitedLocs.append(self.getCurrentLocation())
        return visitedLocs

    def getCurrentLocation(self):
        return (self.x, self.y)


def part1():
    with open('input') as f:
        instructions = f.readline().split(', ')
        location = Location()
        for instruction in instructions:
            location.step(instruction)

        x, y = location.getCurrentLocation()
        print(abs(x)+abs(y))


def part2():
    with open('input') as f:
        instructions = f.readline().split(', ')
        visited = set()
        location = Location()
        visited.add(location.getCurrentLocation())
        for instruction in instructions:
            for loc in location.step(instruction):
                if loc in visited:
                    print(abs(loc[0]) + abs(loc[1]))
                    return
                else:
                    visited.add(loc)


part1()
part2()
