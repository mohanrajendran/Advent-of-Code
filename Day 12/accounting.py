import json

def parse(obj):
    if type(obj) is list:
        return sum(map(parse, obj))
    if type(obj) is int:
        return obj
    if type(obj) is dict:
        keys = obj.keys()
        return sum(parse(obj[k]) for k in keys)
    return 0

f = open('input.txt', 'r')
j = json.load(f)

print parse(j)
