import random
  
while True:    
	cwinner=0
	closer=0	
	print('1=si', '2=no')
	cambio=input('\ncambiare? ')
	for volte in range(int(input('\nquante volte? '))):
	    list=['1','2','3']
	    l2=[]
	    
	#    for i in list:
	    win=random.choice(list) 
	#        print(win) #
	    scelta=random.choice(list)
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
	print('\npercentuale win: ', cwinner/volte*100,'\n')
	for t in range(3):
		print('------------------------------------------')