def validTriangle(a, b, c):
    return a + b > c and b+c > a and c + a > b


def part1():
    with open('input') as f:
        count = 0
        for line in f.readlines():
            a, b, c = map(int, line.strip().split())
            if validTriangle(a, b, c):
                count += 1

        print(count)


def part2():
    with open('input') as f:
        count = 0
        acc = []
        for i, line in enumerate(f.readlines()):
            acc.extend(map(int, line.strip().split()))
            if i % 3 == 2:
                if validTriangle(acc[0], acc[3], acc[6]):
                    count += 1
                if validTriangle(acc[1], acc[4], acc[7]):
                    count += 1
                if validTriangle(acc[2], acc[5], acc[8]):
                    count += 1
                acc.clear()

        print(count)


part1()
part2()
