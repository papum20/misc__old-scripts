import random



n = random.choice(range(8,11))
l = [i for i in range(n)]
m = random.choice(range(n-1,16))
print(n,' ',m)

if n%2==0:
    for i in range(n//2):
        a = random.choice(l)
        l.remove(a)
        b = random.choice(l)
        l.remove(b)
        print(a, ' ',b, ' ',random.choice(range(3,15)))
    l = [i for i in range(n)]
    for i in range(m-n//2):
        a = random.choice(l)
        l.remove(a)
        b = random.choice(l)
        print(a, ' ',b, ' ',random.choice(range(3,15)))
        l.append(a)

else:
    for i in range(n//2):
        a = random.choice(l)
        l.remove(a)
        b = random.choice(l)
        l.remove(b)
        print(a, ' ',b, ' ',random.choice(range(3,15)))
    print(l[0], ' ',random.choice([j for j in range(l[0])]+[j for j in range(l[0]+1,n)]), ' ',random.choice(range(3,15)))
    l = [i for i in range(n)]
    for i in range(m-n//2-1):
        a = random.choice(l)
        l.remove(a)
        b = random.choice(l)
        print(a, ' ',b, ' ',random.choice(range(3,15)))
        l.append(a)
    
