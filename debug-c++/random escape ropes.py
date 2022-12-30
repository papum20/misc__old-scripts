import random

for z in range(20):
    a = ['0']
    b = ['10']
    n = 0
    d = random.choice(range(1,11))
    for i in range(d-1):
        x = random.choice([1,2,3])
        if x == 1:
            n+=1
        elif x == 2:
            n = n
        else:
            if n == 0:
                x = random.choice([1,2])
                if x == 1:
                    n+=1
                elif x == 2:
                    n = n
            else:
                n-= 1
        a.append(str(n))
        b.append(str(random.choice([e for e in range(1,1001)])) )

    print(d)
    print(' '.join(a))
    print(' '.join(b))
    print(eval('+'.join(b)))
