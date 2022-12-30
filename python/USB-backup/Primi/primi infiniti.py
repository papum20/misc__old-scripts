n = 2
while True :
	print(n) if all( (n % i != 0) for i in range(3, (int(n**(1/2)) +1), 2) ) :
		print(n)
	n += (1 if n == 2 else 2)