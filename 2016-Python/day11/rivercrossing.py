import re
import itertools
import collections

microchipRe = re.compile(" (\w+)-compatible microchip")
generatorRe = re.compile(" (\w+) generator")


class State:
    def __init__(self, items, floor=0):
        self.items = [sorted(item) for item in items]
        self.floor = floor

    def nextStates(self):
        if self.floor == 0:
            nextFloors = [1]
        elif self.floor == 3:
            nextFloors = [2]
        else:
            nextFloors = [self.floor - 1, self.floor + 1]

        nextStates = []
        for chipsToMove in [1, 2]:
            for nextFloor in nextFloors:
                for comb in itertools.combinations(self.items[self.floor], chipsToMove):
                    nextItems = []
                    for f, item in enumerate(self.items):
                        if f == self.floor:
                            nextItem = [i for i in item if i not in comb]
                        elif f == nextFloor:
                            nextItem = item[:]
                            nextItem.extend(comb)
                        else:
                            nextItem = item[:]
                        nextItems.append(nextItem)
                    nextState = State(nextItems, nextFloor)
                    if nextState.valid():
                        nextStates.append(nextState)
        return nextStates

    def valid(self):
        return all(self.validFloor(item) for item in self.items)

    def validFloor(self, item):
        generators = set(i[2:] for i in item if i[:2] == 'G-')
        if len(generators) == 0:
            return True

        microchips = [i[2:] for i in item if i[:2] == 'M-']
        return all((microchip in generators) for microchip in microchips)

    def isCompleted(self):
        return self.floor == 3 and all(len(item) == 0 for item in self.items[0:3])

    def __repr__(self):
        str = []
        for floor, item in enumerate(reversed(self.items)):
            if floor == 3-self.floor:
                str.append(f'E {item}')
            else:
                str.append(f'  {item}')
        return '\n'.join(str)

    def __hash__(self):
        return hash((self.floor, tuple(tuple(item) for item in self.items)))

    def __eq__(self, other):
        return hash(self) == hash(other)


def part1():
    with open('input') as f:
        items = []
        for line in f.readlines():
            item = []
            microchips = re.findall(microchipRe, line)
            generators = re.findall(generatorRe, line)
            item.extend(f'M-{microchip}' for microchip in microchips)
            item.extend(f'G-{generator}' for generator in generators)
            items.append(item)

        s = State(items)

        visited = set()
        queue = collections.deque()
        visited.add(s)
        queue.append([0, s])

        while len(queue) > 0:
            steps, state = queue.popleft()
            if state.isCompleted():
                print(steps)
                return

            nextStates = state.nextStates()
            for nextState in nextStates:
                if nextState not in visited:
                    visited.add(nextState)
                    queue.append([steps + 1, nextState])

def part2():
    with open('input') as f:
        items = []
        for line in f.readlines():
            item = []
            microchips = re.findall(microchipRe, line)
            generators = re.findall(generatorRe, line)
            item.extend(f'M-{microchip}' for microchip in microchips)
            item.extend(f'G-{generator}' for generator in generators)
            items.append(item)

        items[0].extend(['G-elerium', 'M-elerium', 'G-dilithium', 'M-dilithium'])

        s = State(items)

        visited = set()
        queue = collections.deque()
        visited.add(s)
        queue.append([0, s])

        while len(queue) > 0:
            steps, state = queue.popleft()
            if state.isCompleted():
                print(steps)
                return

            nextStates = state.nextStates()
            for nextState in nextStates:
                if nextState not in visited:
                    visited.add(nextState)
                    queue.append([steps + 1, nextState])

part1()
part2()
