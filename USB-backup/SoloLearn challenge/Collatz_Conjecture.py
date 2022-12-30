while True :
	count = 0
	n = int(float(input('\nInsert number: ')))
	while int(n) < 1 :
		n = int(float(input('\nInsert number: ')))
	
	while n != 1 :
		count += 1
		if n%2 == 0 :
			n /= 2		
		else :
			n = n * 3 + 1
		print(count, ') ', int(n))
		
	print('\nmoves: ', count)