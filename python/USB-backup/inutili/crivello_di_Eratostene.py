import math

for t in range(99):
    n=int(input('inserire n'))
    z=n+1
    criv=list(range(2,z))
    #print(criv)
    c=list(range(2,int(math.sqrt(n))))
    for j in criv:
        for i in c:
            k=j%i
            if j==i:
                continue
            elif k==0:
                criv.remove(j) 
            else:
                break
    print(criv)
    print('-----')