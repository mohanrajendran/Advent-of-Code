import re

def pair2(name):
    pattern = re.compile(r"(\w)(\w)\w*\1\2")
    match = pattern.search(name)
    if match:
        return True
    return False

def repeat_with_middle(name):
    pattern = re.compile(r"(\w)\w\1")
    match = pattern.search(name)
    if match:
        return True
    return False

def nice(name):
    return pair2(name) and repeat_with_middle(name)

f = open('input.txt', 'r')
count = 0
for name in f:
    if nice(name):
        count += 1

print count
