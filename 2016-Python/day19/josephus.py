from collections import deque

input = 3017957


def josephus(j):
    if j == 1:
        return 1
    elif j % 2 == 0:
        return 2 * josephus(j // 2) - 1
    else:
        return 2 * josephus(j // 2) + 1


def part1():
    print(josephus(input))


def part2():
    left = deque()
    right = deque()

    for i in range(1, input + 1):
        if i < input // 2 + 1:
            left.append(i)
        else:
            right.append(i)

    while len(left) > 0:
        right.popleft()

        if len(right) == len(left):
            right.append(left.popleft())
            left.append(right.popleft())
        else:
            right.append(left.popleft())

    print(right.pop())


part1()
part2()
