import collections

input = 1364


def openSpace(x: int, y: int) -> bool:
    val = x * x + 3 * x + 2 * x * y + y + y * y + input
    binVal = bin(val)
    num1s = sum(1 for b in binVal if b == '1')

    return num1s % 2 == 0


def getNeighbors(x: int, y: int) -> list:
    res = []
    for dx, dy in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
        nx, ny = x + dx, y + dy
        if nx >= 0 and ny >= 0 and openSpace(nx, ny):
            res.append((nx, ny))
    return res


def part1():
    dest = (31, 39)
    visited = set()
    queue = collections.deque()
    visited.add((1, 1))
    queue.append((0, 1, 1))

    while len(queue) > 0:
        steps, x, y = queue.popleft()
        if (x, y) == dest:
            print(steps)
            return
        for nx, ny in getNeighbors(x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((steps + 1, nx, ny))
    print("Unable to visit destination")

def part2():
    stepLimit = 50
    visited = set()
    count = 0
    queue = collections.deque()
    visited.add((1, 1))
    queue.append((0, 1, 1))

    while len(queue) > 0:
        steps, x, y = queue.popleft()
        if steps > stepLimit:
            print(count)
            return
        count += 1
        for nx, ny in getNeighbors(x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((steps + 1, nx, ny))
    print("Unable to visit destination")


part1()
part2()
