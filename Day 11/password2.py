def contains3(passwd):
    l = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(24):
        snip = l[i:i+3]

        if snip in passwd:
            return True

    return False

def forbidden(passwd):
    l = 'iol'

    for c in l:
        if c in passwd:
            return True

    return False

def pairs2(passwd):
    count = 0
    l = 'abcdefghijklmnopqrstuvwxyz'

    for c in l:
        snip = c+c

        if snip in passwd:
            count += 1

        if count == 2:
            return True

    return False

def valid(passwd):
    return contains3(passwd) and not forbidden(passwd) and pairs2(passwd)

def incr_at(passwd, pos):
    if pos == -1:
        return passwd
    if passwd[pos] == 'z':
        passwd[pos] = 'a'
        return incr_at(passwd, pos-1)

    passwd[pos] = chr(ord(passwd[pos]) + 1)

    return passwd

def incr(passwd):
    return "".join(incr_at(list(passwd), 7))

current = incr('hxbxxyzz')
while not valid(current):
    current = incr(current)
print current
