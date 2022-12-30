import random

for k in range(10):

    n = random.choice(range(1,10))
    print(n)
    for i in range(n):
        m = random.choice(range(n))
        l = random.choice(range(m+1))
        print(m,' ',l)
        
        f = [j for j in range(n)]
        f.remove(i)
        while(len(f) > m):
            f.remove(f[random.choice(range(len(f)))])
        print(' '.join([str(j) for j in f]))

    print('\n')
