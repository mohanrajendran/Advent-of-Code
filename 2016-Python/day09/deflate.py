def part1():
    with open('input') as f:
        compressed = f.readline().strip()
        idx = 0
        count = 0
        while idx < len(compressed):
            if compressed[idx] != '(':
                count += 1
                idx += 1
            else:
                # parse the chars to expand
                idx += 1
                chars = 0
                while compressed[idx] != 'x':
                    chars *= 10
                    chars += int(compressed[idx])
                    idx += 1
                # parse the number of times to expand
                idx += 1
                times = 0
                while compressed[idx] != ')':
                    times *= 10
                    times += int(compressed[idx])
                    idx += 1
                idx += 1
                count += (chars * times)
                idx += chars

        print(count)


def getDeflateLength(compressed, start, end):
    idx = start
    count = 0
    while idx < end:
        if compressed[idx] != '(':
            count += 1
            idx += 1
        else:
            # parse the chars to expand
            idx += 1
            chars = 0
            while compressed[idx] != 'x':
                chars *= 10
                chars += int(compressed[idx])
                idx += 1
            # parse the number of times to expand
            idx += 1
            times = 0
            while compressed[idx] != ')':
                times *= 10
                times += int(compressed[idx])
                idx += 1
            idx += 1
            count += (getDeflateLength(compressed, idx, idx + chars) * times)
            idx += chars
    return count


def part2():
    with open('input') as f:
        compressed = f.readline().strip()
        print(getDeflateLength(compressed, 0, len(compressed)))


part1()
part2()
