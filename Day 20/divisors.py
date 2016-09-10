import math

def presents(n):
    count = 0
    for i in range(1, int(math.sqrt(n)+1)):
        if n % i == 0:
            count += (i*10)
            r = n / i
            if r != i:
                count += (r*10)

    return count

target = 29000000
i = 0
found = False
while not found:
    i += 1
    if presents(i) >= target:
        found = True

print i
