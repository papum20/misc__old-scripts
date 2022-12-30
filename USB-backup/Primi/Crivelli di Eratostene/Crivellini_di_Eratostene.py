import math

while True :
    n=int(input('inserire numero: '))
    m=n+1
    l1=list(range(3,m,2)) #primi
    l2=[]    #divisori primi
    l3=[]    #fattori primi
    s4=set()
    l5=[]

#crivello
    
    x=2
    rad=int(math.sqrt(n))
    while x <= rad:     
        for i in l1:
            if i%x == x:
                print('uguale') #
                continue
            elif i%x == 0:
                l1.remove(i)
                print('tolto',i) #
                continue
            else:
                continue
        else:
             x += 1
             print('piu') #
                 
    if n % 2 == 0 :
    	l1.append(2)
	
#l2 lista divisori primi  
     
    if n not in l1:
        for d in l1:
            if n%d == 0:
                l2.append(d)
            else:
                continue    
        print('l2',l2) #

##l3 fattori primi

        for d2 in l2:
            f=n
            for altrofat in l2:
               if altrofat!=d2:                       
                    y3=f%altrofat
                    while y3==0:
                        f /= altrofat
                        y3=f%altrofat
            y33=f%d2
            if y33==0:
                log=int(math.log(f,d2)-1)
                for l in range(log):
                    l3.append(d2)
                    print('l3',l3) #
            else:
                continue                  

#verso la fine, se è primo
                 
    print('-')
    if len(l1)>106:
        print(l1)
        print('-')
        
    if n in l1:
        print(n,'È PRIMO')
  
#aggiungi i fattori primi l3 in divisori primi l2
        
    else:
        for div in l3:
            l2.append(div)
        l2.sort()
        print('l2 fattori primi',l2) #
        print('l3 fattori primi',l3) #
        
#ora mettiamo le potenze

        print('l2',l2) #
        for div3 in l2:
            s4.add(div3)
        for div2 in s4:
            print('div2',div2) #
            esp=0
            print('esp',esp) #
            for sdiv in l2:
                print('sdiv',sdiv) #
                if div2==sdiv:
                    esp+=1
                    print('esp2',esp) #
   
            if esp>1:
                l5.append(str(div2))
                l5.append('^')
                l5.append(str(esp))
            else:
                l5.append(str(div2))
            l5.append(', ')
        l5.pop()
        print(s4)
        print('-')
        print(n,'NON È PRIMO')
        print('i fattori primi di ',n,'sono:\n',"".join(l5))
        print('-')
        
    print('fino a',n,'ci sono',len(l1),'numeri primi:\n',sorted(l1))      
    print('\n------------------------------------------\n')