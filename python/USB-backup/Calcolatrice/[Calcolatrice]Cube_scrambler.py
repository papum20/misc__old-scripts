import random

moves_a = [14, 11, 25]
pyraminx = ['R', 'L', 'U', 'B']
c3x3 = [['F', 'B'], ['R', 'L'], ['U', 'D']]



while True :
	choice = input('1)pyraminx;2) 2x2;3) 3x3;\n insert "x" to stop\nselect a puzzle: ')
	if choice in ['x'] :
		break
	if choice in [str(i) for i in range(1,4)] :
		choice = int(choice)
	else :
		print('\nerror...\n\n')
		continue
	
	count = 0
	print('- "a" = 10 scrmbls, {} moves -'.format(moves_a[choice -1]))
	cin = input('moves per scramble: ')
	if cin == 'a' :
		n_turn = moves_a[choice -1]
		n_scr = 10
	else :	
		try :
			n_turn = int(cin)
			n_scr = int(input('scrambles: '))
		except ValueError :
			print('\nerror...\n')
			continue
			
#####pyraminx#####
			
	if choice == 1 :
		for scrambles in range(n_scr) :
			count +=1
			scramble = []
			
			for i in range(random.choice(range(1,5))) :
				scramble.append(random.choice([e for e in pyraminx if e.lower() not in [k[0] for k in scramble] ]).lower() + random.choice(['', "'"]))
			repeat = ''
			while len(scramble) < n_turn :
				repeat = random.choice([e for e in pyraminx if e != repeat])
				scramble.append(repeat + random.choice(['', "'"]))
				
			print('\nscramble n° {}\n{}\n\n'.format (count, ' '.join(scramble)), ''.join(['-' for i in range(42)]))
	
#####2x2#####

	if choice == 2 :
		for scrambles in range(n_scr) :
			count += 1
			scramble = []
			
			ind = random.choice(range(3))
			while len(scramble) < n_turn :
				scramble.append (random.choice(c3x3[ind]) + random.choice(['', "'", '2']))
				ind = random.choice ([i for i in range(3) if i != ind])
				
			print('\nscramble n° {}\n{}\n\n'.format (count, ' '.join(scramble)), ''.join(['-' for i in range(42)]))
		
#####3x3#####			
	
	if choice == 3 :
				
		for scrambles in range(n_scr):
			count += 1
			scramble = []
			nottorepeat = []

						
			while len(scramble) < n_turn :
				list = random.choice (c3x3)
				mossa = random.choice (list)
				if mossa in nottorepeat:
					continue
				scramble.append (mossa + random.choice(['', "'", '2']))
				
					
				if len(nottorepeat) == 1 and nottorepeat[0] in list :
					nottorepeat.append(mossa)
				else :
					nottorepeat = [mossa]
	
			
			print('scramble n° {}\n{}'.format( count, ' '.join(scramble)) )
	
#####end#####
			
	
	print(''.join(['\n' for i in range(10)]))