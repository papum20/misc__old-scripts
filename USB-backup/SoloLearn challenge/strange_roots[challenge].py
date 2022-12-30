while True:
	n = int(input('insert a number: '))
	bo = False
	
	for i in range(len(str(n**2))) :
		for h in range(len(str(round(n**(1/2),3)))) :
			if str(n**2)[i] == str(round(n**(1/2),3))[h] :
				bo = True
				break
	
	if bo == True :
		print(n, 'has a strange root')
	else :
		print(n, 'has not a strange root')
	print('(root:', round(n**(1/2),3), '; square: ', n**2, ')\n\n\n')