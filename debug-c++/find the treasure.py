import random


T = 10
for t in range(T):

    r = random.choice(range(1,4))
    c = random.choice(range(1,4))
    print(r,c)


    for y in range(r):
        print(' '.join([str(random.choice([0,1])) for x in range(c)]))
