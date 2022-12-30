def prime(a) :
	pr = True
	for d in range(2, int(a**(1/2) +1)) :
		if a%d == 0 :
			pr = False
			break
		if d == 2 :
			d -= 1
		d += 2
	return pr

while True :	
	n = int(input('insert an even number higher than 3: '))
	while n < 4 or n%2 != 0 :
		n = int(input('insert a valid number: '))
	
	for x in range(2, n//2 +1) :
		if prime(x) :
			if prime(n-x) :
				print(x,'+',n-x)
		if x == 2 :
			x -= 1
		x += 2

	print('\n\n')