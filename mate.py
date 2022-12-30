import random

p = [1,2,3,4,5,6]
l = []
count = 0
while(True):
    l1 = []
    ind = 1
    while(len(l1)<6):
        x = random.choice(range(1,7))
        if x != ind and x not in l1:
            l1.append(x)
        else:
            continue
        ind += 1

    bo = True
    for i in range(6):
        if p[i] == l1[i]:
            bo = False
            break
    if bo == True:
        if l1 not in l:
            l.append(l1)
        count += 1
        print(l1)
        print(count)
