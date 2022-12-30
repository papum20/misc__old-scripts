while True:
	while True:
		print('\n-inserire scelta:\n\n1 - primi n numeri primi\n2 - numeri primi fino a n')
		choice = int(input('\nscelta: '))
		if choice not in (1, 2):
			print('scelta non valida')
			continue
		break
		
	while True:
		try:
			print('\ninserire n:\n')
			n = int(input('n = '))
			if n <= 0:
				print('\ninserire un valore maggiore o uguale a 1')
				continue
			break
		except:
			print('\ninserire un valore numerico intero')
			continue

	if choice == 1:
		if n > 0:
			count = 2
			num = 3
			print(2)
			while count <= n:
				if num % 2 != 0 and all(num % i != 0 for i in range(3, int((num + 1) ** (1 / 2)) + 1, 2)):
					print(num)
					count += 1
				num += 1

	if choice == 2:
		if n < 2:
			print('nessun primo presente')
		else:
			print(2)
			for p in range(2, n):
				if p % 2 != 0 and all(p % i != 0 for i in range(3, int((p + 1) ** (1 / 2)) + 1, 2)):
					print(p)
						
	print('\nRiavviare il programma? [y/n]\n')
	if input() == 'y':
		break