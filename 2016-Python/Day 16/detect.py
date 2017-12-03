detected = {}
detected['children'] = 3
detected['cats'] = 7
detected['samoyeds'] = 2
detected['pomeranians'] = 3
detected['akitas'] = 0
detected['vizslas'] = 0
detected['goldfish'] = 5
detected['trees'] = 3
detected['cars'] = 2
detected['perfumes'] = 1

f = open('input.txt', 'r')
for line in f:
    found = True
    s = line.split()
    num = int(s[1][:-1])
    for i in range(3, len(s),2):
        item = s[i-1][:-1]
        if i == len(s)-1:
            count = int(s[i])
        else:
            count = int(s[i][:-1])
        if detected[item] != count:
            found = False
            break

    if found:
        print num
