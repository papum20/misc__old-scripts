import random

for i in range(10):
#	n = random.choice(range(1,11))
        n = 3
        print(n)
        tot = 0
        a = ['0']
        for j in range(n-1):
                a.append(str(random.choice(range(int(a[j])+2))))
        print(' '.join(a))
        b = []
        for j in range(n):
                b.append(str(random.choice(range(1000))))
                tot += int(b[j])
        print(' '.join(b))
        print('TOT: ', tot)
