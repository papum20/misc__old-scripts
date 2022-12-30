import random

rows = [0]
columns = [0]


r = 0
while r < 25:
    r = random.choice(range(r+2, 31))
    rows.append(r)

c  = 0
while c < 25:
    c = random.choice(range(c+2, 31))
    columns.append(c)


print(' '.join([str(r+1),str(c+1)]))

for y in range(r+1):
    s = ''
    for x in range(c+1):
        if y in rows or x in columns:
            s += '#'
        else:
            s += random.choice(['@','.','.','.'])
    print(s)
