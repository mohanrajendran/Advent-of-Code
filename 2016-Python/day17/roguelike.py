from collections import deque
from hashlib import md5

input = 'hhhxzeay'


def nextDirections(x, y, pathSoFar):
    h = md5((input + pathSoFar).encode("utf-8")).hexdigest()
    nextDir = []
    # up
    if y != 0 and h[0] in 'bcdef':
        nextDir.append('U')
    # down
    if y != 3 and h[1] in 'bcdef':
        nextDir.append('D')
    # left
    if x != 0 and h[2] in 'bcdef':
        nextDir.append('L')
    # right
    if x != 3 and h[3] in 'bcdef':
        nextDir.append('R')
    return nextDir


def part1():
    queue = deque()
    queue.append((0, 0, 0, ''))

    while len(queue) > 0:
        steps, x, y, pathSoFar = queue.popleft()
        if x == 3 and y == 3:
            print(pathSoFar)
            return

        for nextDir in nextDirections(x, y, pathSoFar):
            if nextDir == 'U':
                queue.append((steps + 1, x, y - 1, pathSoFar + 'U'))
            if nextDir == 'D':
                queue.append((steps + 1, x, y + 1, pathSoFar + 'D'))
            if nextDir == 'L':
                queue.append((steps + 1, x - 1, y, pathSoFar + 'L'))
            if nextDir == 'R':
                queue.append((steps + 1, x + 1, y, pathSoFar + 'R'))


def part2():
    queue = deque()
    queue.append((0, 0, 0, ''))
    maxSoFar = 0

    while len(queue) > 0:
        steps, x, y, pathSoFar = queue.popleft()
        if x == 3 and y == 3:
            maxSoFar = steps
        else:
            for nextDir in nextDirections(x, y, pathSoFar):
                if nextDir == 'U':
                    queue.append((steps + 1, x, y - 1, pathSoFar + 'U'))
                if nextDir == 'D':
                    queue.append((steps + 1, x, y + 1, pathSoFar + 'D'))
                if nextDir == 'L':
                    queue.append((steps + 1, x - 1, y, pathSoFar + 'L'))
                if nextDir == 'R':
                    queue.append((steps + 1, x + 1, y, pathSoFar + 'R'))

    print(maxSoFar)


part1()
part2()
