def vowel3(name):
    count = 0
    for c in name:
        if c in "aeiou":
            count += 1
        if count == 3:
            return True
    return False

def twice(name):
    ln = len(name)-1
    for l in xrange(ln):
        if name[l] == name[l+1]:
            return True
    return False

def bad(name):
    bad_names = ['ab','cd','pq','xy']
    for b in bad_names:
        if b in name:
            return True
    return False

def nice(name):
    return vowel3(name) and twice(name) and (not bad(name))

f = open('input.txt', 'r')
count = 0
for name in f:
    if nice(name):
        count += 1

print count
