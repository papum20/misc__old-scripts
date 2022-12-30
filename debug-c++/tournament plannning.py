import random


t = 10
for T in range(t):


    n = 10
    m = 100
    print(n,m)

    days = [random.choice(range(10)) for i in range(n)]
    days.sort()

    for i in range(n):
        s = random.choice(range(1,24))
        e = random.choice(range(s+1,25))
        b = 0
        p = 1
        print(days[i],s,e,b,p)

