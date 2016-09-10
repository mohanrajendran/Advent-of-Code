import json

def parse(obj):
    if type(obj) is list:
        return sum(map(parse, obj))
    if type(obj) is int:
        return obj
    if type(obj) is dict:
        values = obj.values()
        for v in values:
            if type(v) is unicode and v == 'red':
                return 0
        return sum(parse(k) for k in values)
    return 0

f = open('input.txt', 'r')
j = json.load(f)

print parse(j)
