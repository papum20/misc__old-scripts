import random

for k in range(10):

    c = random.choice(range(1,100))
    y = random.choice(range(1,11))
    d = random.choice(range(1,11))

    print('{} {} {}'.format(str(c),str(d),str(y)))
    for i in range(2):
        print(' '.join([str(random.choice(range(21))) for j in range(d)]))

    print('\n')
          

