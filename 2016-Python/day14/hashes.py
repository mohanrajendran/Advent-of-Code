import hashlib
import re
import functools

input = 'ahsbgdzn'
tripleRe = re.compile(r'(\w)\1\1')


@functools.lru_cache(1001)
def getHash(index, times=1):
    v = input + str(index)
    for i in range(times):
        v = hashlib.md5(v.encode('utf-8')).hexdigest()

    return v


def part1():
    found = 0
    idx = 0
    while found < 64:
        srcHash = getHash(idx)
        triples = tripleRe.search(srcHash)
        if triples:
            toSearch = triples.group(0)[0] * 5
            for next in range(1, 1001):
                nextHash = getHash(idx + next)
                if toSearch in nextHash:
                    found += 1

        idx += 1

    print(idx - 1)


def part2():
    found = 0
    idx = 0
    while found < 64:
        srcHash = getHash(idx, 2017)
        triples = tripleRe.search(srcHash)
        if triples:
            toSearch = triples.group(0)[0] * 5
            for next in range(1, 1001):
                nextHash = getHash(idx + next, 2017)
                if toSearch in nextHash:
                    found += 1

        idx += 1

    print(idx - 1)


part1()
part2()
