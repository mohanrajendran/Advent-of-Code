def get_difference(str):
    count = 2
    for c in str:
        if c == '\"' or c == '\\':
            count += 1

    return count

f = open("input.txt", "r")
d = 0
for line in f:
    d += get_difference(line)

print d
