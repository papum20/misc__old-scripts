import random

cwinner=0
closer=0  
print('1=si', '2=no')
  
while True:    
    list=['1','2','3']
    l2=[]
    
#    for i in list:
    win=random.choice(list) 
#        print(win) #
    scelta=input('\nscegli una porta tra 1,2,3:')
    if scelta not in list:
    	print('\nreinserire\n')
    	continue
    print('Hai scelto la', scelta)
    canc=random.choice(list)
    while len(l2)<1:   
        if canc!=scelta and canc!=win:
            print('Eliminiamo la',canc)
            l2.append(canc)
            list.remove(canc)
            break
        else:
        	canc=random.choice(list)
        	continue

    cambio=input('\nvuoi cambiare la tua scelta?')
    while cambio not in ('si','no','1','2'):
    	cambio=input('\nvuoi cambiare la tua scelta?')
    for x in list:
    	while x!=scelta:    
    		if cambio in ('no','2'):
    			print('no')
    		elif cambio in ('si','1'):
    			scelta=x
    			print('si')
    		break
    		
    if scelta==win:
        print('HAI VINTO!')
        cwinner=cwinner+1
    
    elif scelta!=win:
        print('HAI PERSO!')
        closer=closer+1
    print('win is',win)
    print('\nVITTORIE=',cwinner,';','SCONFITTE=',closer)
    print('------------------------------------------')
    continue       

#import random

#cwinner=0
#closer=0  
#print('1=si', '2=no')
#  
#while True:    
#    #count=[]
#    list=[1,2,3]
#    l2=[]
#    
#    for i in list:
#    	win=random.choice(list)
#    	print(win) #
#    	scelta=int(input('scegli una porta tra 1,2,3: '))
#    	print('Hai scelto la', scelta)
#    	canc=random.choice(list)
#    	print('canc1', canc) #
#		while len(l2)<1:
#			if canc!=scelta and canc!=win:
#				print('Eliminiamo la',canc)
#		        l2.append(canc)
#		        list.remove(canc)
#		        break
#		    else:
#	#            	print('no,',canc) #
#		    	canc=random.choice(list)
#	#            	print('canc', canc) #
#	 	   	continue
#                if canc!=scelta and canc!=win:
#                    print('Eliminiamo la',canc)
#                    l2.append(canc)
#                    list.remove(canc)
#                else:
#                    continue        
#            count=0

#        cambio=input('\nvuoi cambiare la tua scelta?')
#        for x in list:    
#            if cambio=='no':
#                print('no')
#                break
#            elif cambio=='2':    ##
#                print('no')
#                break    ##
#            elif cambio=='si' and x!=scelta:
#                scelta=x
#                print('si')
#                break
#            elif cambio=='1' and x!=scelta:    ##
#                scelta=x    ##
#                print('si')
#                break    ##
#        if scelta==win:
#            print('HAI VINTO!')
#            cwinner=cwinner+1

#                count.append('a')
#                print(count)
#    
#            break
#        elif scelta!=win:
#            print('HAI PERSO!')
#            closer=closer+1
#            break
#    print('win is',win)
#    print()
#    print('VITTORIE=',cwinner,';','SCONFITTE=',closer)
#    print('------------------------------------------')
#    print(len(count))                