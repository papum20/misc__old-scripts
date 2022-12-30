import math

for v in range(99):
    n=int(input('inserire numero:'))
    div=int((n/2)+1)
    list=[]
    l2=[]
    
    for i in range(2,div):
        y=n%i
        if y==0:
            list.append(i)
        else:
            continue
            
    if len(list)==0:
        print(n,'è primo')
        
    else:
        for j in list:
            print('j',j)
            for k in list:
                if k<j:  
                    print('k',k)
                    z=j%k
                    print('z',z)
                    if z==0:
                        l=int(math.log(j,k))-1
                        print('l',l)
                        for w in range(l):
                            l2.append(k)
                            print(l2)
                        list.remove(j)
                        print(list)
                    else:
                        continue
                else:
                    continue
                continue
        for g in l2:    
            list.append(g)
        list.sort()
        print(n,'non è primo')
        print('i divisori di',n,'sono',list)
        
    print('-----')