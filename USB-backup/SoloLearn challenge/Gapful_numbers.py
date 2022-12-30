def f(x) :
	y = int(x[0] + x[len(x)-1])		
	if int(x) % y == 0 :
		return True
	else :
		return False


def t(m) :
	while True :
			try :
				m = input("insert number: ")
				if -100 < int(m) < 100 :
					raise Exception('No')
			except ValueError and Exception :
				print('invalid number')
				continue
			else:
				return m


print("A gapful number is a number of at least 3 digits that is\n divisible by the number formed by the first and last\n digit of the original number.\n")


while True :
	print('1 - gapful checker\n2 - list of gapful numbers to n')
	op = int(input("\nselect mode: "))


	if op == 1 :
		n = 'a'
		n = t(n)
		g = int(n[0] + n[len(n)-1])
		if f(n) :
			print('\n', int(n), " is gapful (", int(n), '/', g, ' = ', int(int(n)/g), ')\n\n\n')
		else :
			print('\n', int(n), " is not gapful\n\n\n")
	
	
	elif op == 2 :
		r = 'a'
		r = t(r)
		num = []
		for i in range(100,int(r)+1) :
			if f(str(i)) :
				num.append(i)
		print('\n', num, '\n\n\n')
		

	else :
		print('\n\n')
		continue