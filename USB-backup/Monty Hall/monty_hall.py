import random

for w in range(20):   #tentativi
    count=[]
    for t in range(10000):   #precisione
        lis=list(range(3))  #numero di porte
        l2=[]
        for i in lis:
            win=random.choice(lis) 
    #        print(win) 
            scelta=random.choice(lis)
    #        print(scelta)
            canc=random.choice(lis)
            while len(l2)<1:   
                if canc!=scelta and canc!=win:
    #                print('canc',canc)
                    l2.append(canc)
                    lis.remove(canc)
                else:
    #                print('no,',canc)
                    canc=random.choice(lis)
                    if canc!=scelta and canc!=win:
    #                    print('canc',canc)
                        l2.append(canc)
                        lis.remove(canc)
                    else:
                        continue        
    #        count=0
            if scelta!=win:
    #            print('HAI VINTO!')
                count.append('a')
    #            print(count)
                break
            elif scelta==win:
    #            print('HAI PERSO!')
                break
    print(len(count))             



#input('scegli una porta tra 0,1,2')