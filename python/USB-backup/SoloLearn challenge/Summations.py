while True :
	try :
		l = input('insert a range and an operation\n(please separe with spaces (i.e.: 1 3 + 4 )) : ').split()
		max = int( l[1] )	# =max. range
		op = l[2] + l[3]	# =operation
		res = 0		# =result
		exp = ''		# =expression
		if op[0] not in ['+','-','*','/','%','**'] :
			raise Exception
	except :
		print('invalid operation..')
		continue
	
	
	for n in range(int(l[0]), max + 1) :
		exp += (str(n) + op + (' + ' if n<max else '') )
		res += eval(str(n) + op)

	
	print('\n\n', exp, '\n\n\nresult = ', res, '\n\n\n\n')