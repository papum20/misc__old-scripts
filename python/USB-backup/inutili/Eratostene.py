import math

for v in range(99):
    n=int(input('inserire numero:'))
    m=n+1
    l1=list(range(2,m))
    x=2
    rad=int(math.sqrt(n))
    for t in range(rad):
        while x<=rad:     
            for i in l1:
                y=i%x
#                print('y',y)
                if i==x:
                    print('uguale')
                    continue
                elif y==0:
                    l1.remove(i)
                    print('tolto',i)
                    continue
                else:
                    for w in range(10):
                        continue
            else:
                 x=x+1
                 print('piu')
    print(l1)
    print(n in l1)
    print('fino a',n,'ci sono',len(l1),'numeri primi')
    print('-----')