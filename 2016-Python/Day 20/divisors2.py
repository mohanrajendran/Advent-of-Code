import math

def presents(n):
    count = 0
    for i in range(1, min(51,int(math.sqrt(n)+1))):
        if n % i == 0:
            r = n / i
            if r <= 50:
                count += (i*11)
            if i <= 50 and r != i:
                count += (r*11)

    return count

target = 29000000
i = 0
found = False
while not found:
    i += 1
    if presents(i) >= target:
        found = True

print i
