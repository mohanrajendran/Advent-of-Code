def allowed(intervals, ip):
    for start, end in intervals:
        if ip >= start and ip <= end:
            return False
    return True


def part1():
    with open('input') as f:
        intervals = []
        for line in f.readlines():
            start, end = [int(i) for i in line.strip().split('-')]
            intervals.append((start, end))
        intervals.sort()

        for start, end in intervals:
            if allowed(intervals, end + 1):
                print(end + 1)
                return

def part2():
    with open('input') as f:
        intervals = []
        for line in f.readlines():
            start, end = [int(i) for i in line.strip().split('-')]
            intervals.append((start, end))
        intervals.sort()

        total, ip, index = 0, 0, 0
        while ip < 2 ** 32:
            lower, upper = intervals[index]
            if ip >= lower:
                if ip <= upper:
                    ip = upper + 1
                    continue
                index += 1
            else:
                total += 1
                ip += 1

        print(total)


part1()
part2()
