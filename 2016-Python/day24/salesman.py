from collections import deque


def findStart(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '0':
                return x, y


def findStops(grid):
    stops = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] in '0123456789':
                stops.add(grid[y][x])
    return stops

def part1():
    with open('input') as f:
        grid = list(map(lambda x: x.strip(), f.readlines()))
        fx, fy = findStart(grid)
        stops = findStops(grid)
        queue = deque()
        visited = set()

        queue.append((0, fx, fy, ()))
        visited.add((fx, fy, ()))

        while len(queue) > 0:
            steps, x, y, seen = queue.popleft()
            seen = set(seen)
            if grid[y][x] != '.':
                seen.add(grid[y][x])
            if seen == stops:
                print(steps)
                return

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if grid[ny][nx] != '#':
                    nextState = (nx, ny, tuple(sorted(list(seen))))
                    if nextState not in visited:
                        visited.add(nextState)
                        queue.append((steps + 1, nx, ny, tuple(sorted(seen))))

def part2():
    with open('input') as f:
        grid = list(map(lambda x: x.strip(), f.readlines()))
        fx, fy = findStart(grid)
        stops = findStops(grid)
        queue = deque()
        visited = set()

        queue.append((0, fx, fy, ()))
        visited.add((fx, fy, ()))

        while len(queue) > 0:
            steps, x, y, seen = queue.popleft()
            seen = set(seen)
            if grid[y][x] != '.':
                seen.add(grid[y][x])
            if seen == stops and grid[y][x] == '0':
                print(steps)
                return

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if grid[ny][nx] != '#':
                    nextState = (nx, ny, tuple(sorted(list(seen))))
                    if nextState not in visited:
                        visited.add(nextState)
                        queue.append((steps + 1, nx, ny, tuple(sorted(seen))))


part1()
part2()
