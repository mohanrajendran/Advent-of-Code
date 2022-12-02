import hashlib

input = 'abbhdwsy'


def part1():
    res = []
    nonce = 0
    while True:
        p = input + str(nonce)
        h = hashlib.md5(p.encode('utf-8')).hexdigest()
        if h[:5] == '00000':
            res.append(h[5])

        if len(res) == 8:
            break

        nonce += 1

    print(''.join(res))


def part2():
    res = ['']*8
    found = 0
    nonce = 0
    while found < 8:
        p = input + str(nonce)
        h = hashlib.md5(p.encode('utf-8')).hexdigest()
        if h[:5] == '00000':
            if h[5] in '01234567' and res[int(h[5])] == '':
                res[int(h[5])] = h[6]
                found += 1

        nonce += 1

    print(''.join(res))


part1()
part2()
