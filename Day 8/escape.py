def get_difference(str):
    original_length = len(str)

    idx = 0
    new_length = 0
    while idx < original_length:
        #ignore leading quote
        if idx == 0:
            idx += 1
            continue
        #ignore trailing quote
        if idx == original_length-1:
            idx += 1
            continue

        #encounter slash
        if str[idx] == "\\":
            new_length += 1
            idx += 1
            #next is quote or backslash
            if str[idx] == "\\" or str[idx] == "\"":
                idx += 1
            elif str[idx] == "x":
                idx += 3

            continue

        idx += 1
        new_length += 1

    return original_length - new_length

f = open("input.txt", "r")
d = 0
for line in f:
    d += get_difference(line)

print d
