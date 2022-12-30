import random

ch = 'abcdefghijklmnopqrstuvwxyz1234567890'

def check(p) :
	for i in range(len(p)//2 +1) :
		if p[i] != p[len(p) -1 -i] :
			return False
	return True
				

while True:
	op = input('1 - Palindrome checker\n2 - Random palindrome generator\n\nselect an option: ')
	
	
	if op == '1' :
		print('\n\n', check(input('\n\ninsert a string/number: ')))
		
		
	elif op == '2' :
		l = int(input('\n\nchoose the length: '))	
		p = "".join([random.choice(ch) for i in range(l//2)])
		if l %2 == 0 :
			p = p + p[::-1]		
		else :
			p = p + random.choice(ch) + p[::-1]
		print('\npalindrome:', p)
	
	
	else :
		print('invalid option\n\n')
		continue
		

	print('\n\n\n\n')