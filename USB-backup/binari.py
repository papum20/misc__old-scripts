import math

while 1:
	n = int(input("insert a number: "))
	res = ''

	for exp in range(int(math.log(n, 2)), -1, -1):
		res += '1' if 2**exp <= n else '0'
		n -= 2**exp if 2**exp <= n else 0
		res += ' ' if (exp)%3 == 0 else ''
			
	print(res, '\n')