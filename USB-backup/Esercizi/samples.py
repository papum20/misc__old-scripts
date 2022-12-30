def find(l, elem, lun):
    for h in range(lun):
        for k in range(lun):
            if l[h][k] == elem:
                return [str(h), str(k)]
    return 'no'


def err3y(l1, l2, ide, lett, nn, xx):
    for j in l1 if ide[1]==lett else l2:
        if nn[j][xx] != '.':
            return True
    return False

def err3x(l1, l2, ide, lett, nn, yy):
    for j in l1 if ide[1]==lett else l2:
        if nn[yy][j] != '.':
            return True
    return False



nums = [str(i) for i in range(10)]
n = int(input('dimensioni: '))
m = int(input('moves: '))
moves = ('U', 'D', 'L', 'R')
list = [input('n: ') for i in range(n)]
nxn = [[i[h] for h in range(n)] for i in list]
mxm = [ input('m: ').split() for i in range(m)]

samples = []

for h in nxn:
    for k in h:
        if k in nums:
            samples.append(k)

#body

for t in mxm:
    if int(t[2]) < 1:
        print('1: error: invalid number of repetitions (REP<1).')
        continue

    x = int(find(nxn, t[0], n)[1])
    y = int(find(nxn, t[0], n)[0])


    if nxn[y][x] not in samples:
        print('2: error: SAMPLE_ID does not appear on the board.\n')
        continue
    
    if not 0 <= ((y+int(t[2]) if t[1]=='D' else y-int(t[2])) if t[1] in ['U','D'] else (x+int(t[2]) if t[1]=='R' else x-int(t[2])) ) < n :
        print('4: error: attempt to move the samples above the board boundaries.')
        continue



    if t[1] in ['U','D']:
        if err3y(range(y+1,y+int(t[2])+1), range(y-int(t[2]),y), t, 'D', nxn, x):
            print('3: error: attempt to move the samples on a non-empty place.')
            continue
        nxn[y+int(t[2]) if t[1]=='D' else y-int(t[2]) ][x] = nxn[y][x]
            
    if t[1] in ['L','R']:
        if err3x(range(x+1,x+int(t[2])+1), range(x-int(t[2]),x), t, 'R', nxn, y):
            print('3: error: attempt to move the samples on a non-empty place.')
            continue
        nxn[y][(x+int(t[2])) if t[1]=='R' else (x-int(t[2])) ] = nxn[y][x]



    nxn[y][x] = '.'
    print('0: malware sample successfully moved.\n')



for p in range(n):
    print(''.join(nxn[p]))