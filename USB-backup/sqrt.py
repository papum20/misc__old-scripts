while True:
	num=float(input('inserire numero: '))
	rad=0.0
	piu=1
	while rad*rad!=num:
		rad+=piu
#		print(rad) #
#		print('+',piu) #
		if rad*rad>num:
			rad-=piu
			piu/=10
#			print(',if',rad) #
		if piu<0.0001:
			break
	
	#round	
		
	print('la radice di',num,'è:',rad,'\n')