def increment(s):
    sofar = []
    current = None
    count = 0

    for c in s:
        if current == None:
            current = c
            count = 1
        elif c == current:
            count += 1
        else:
            sofar.append(str(count))
            sofar.append(current)
            current = c
            count = 1

    sofar.append(str(count))
    sofar.append(current)
    return "".join(sofar)

pattern = '1321131112'
for i in range(40):
    pattern = increment(pattern)

print len(pattern)
