import random



for i in range(10):
    n = random.choice(range(1,20))
    e = random.choice(range(1,100))
    print('{} {}\n'.format(n,e), ' '.join([str(random.choice(range(1,90))) for j in range(n)]))
