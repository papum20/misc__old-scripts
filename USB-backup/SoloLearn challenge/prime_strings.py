while True:
	s = input('insert a string: ')
	lun = len(s)
	
	if lun == 1 :
		print('\n', s, 'is not a prime string\n\n\n')
		continue
	
	boo = True
	for i in range(1,lun // 2 + 1) :
		if lun % i != 0 :
			continue
		div = s[0:i]
		mdi = div * int((lun / i))
		if mdi == s :
			boo = False
			break
			
	if boo == False :
		print('\n', s, "is not a prime string (it's divisible by \"", div, '\")\n\n\n')
	else :
		print('\n', s, 'is a prime string\n\n\n')