import random

for k in range(10):
    n = random.choice(range(2,15))
    b = random.choice(range(10,150))
    print(n,b)
    print(' '.join([str(random.choice(range(20))) for i in range(n)]))
    print('\n')
