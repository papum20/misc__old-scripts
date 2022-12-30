import random

def r() :
	ran = random.choice(range(11))
	return ran


ans ='no'
while ans not in ('si', 'Si', 'yes', 'Yes', 's', 'y') :
	o = int(input('\n\n\n1 - algorithm\n2 - random\n\nselect option: '))
	q = int(input('\nquestions: '))
	mod = int(input('answers: '))
	
	
	if o == 1 :
		uno = r()
		due = r()
		tre = r()
		print('\nalgorithm:', "".join(['( (n**',str(uno), ' +', str(due),') * (n -',str(tre),') ) %answers + 1']))
		for n in range(1, q+1) :
			print('n°:', n, '-->',  ( (n**uno +due) * (n - tre) ) %mod +1)
			
			
	if o == 2 :
		for i in range(1, q+1):
			print('n°:', i, '-->',  random.choice(range(1, mod+1)))
			
			
	ans = input('\n\nstop? ')