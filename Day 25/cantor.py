def increment(tup):
    row = tup[0]
    col = tup[1]
    val = tup[2]

    if row == 1:
        nRow = col+1
        nCol = 1
    else:
        nRow = row-1
        nCol = col+1

    nVal = (val * 252533) % 33554393

    return (nRow, nCol, nVal)

f = open('input.txt', 'r')
s = f.readline().split()
row = int(s[15][:-1])
column = int(s[17][:-1])

cur = (1,1,20151125)
while cur[0] != row or cur[1] != column:
    cur = increment(cur)

print cur[2]
