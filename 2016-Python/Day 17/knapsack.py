def memoize2(f):
    memo = {}
    def helper(x, y, numbers):
        if (x,y) not in memo:
            memo[(x,y)] = f(x, y, numbers)
        return memo[(x,y)]
    return helper

@memoize2
def num_ways(i, n, numbers):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if i == len(numbers):
        return 0

    return num_ways(i+1, n, numbers) + num_ways(i+1, n-numbers[i], numbers)

f = open('input.txt', 'r')
n = map(int, f)

print num_ways(0, 150, n)
