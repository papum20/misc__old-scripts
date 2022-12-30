n = int(input())
a = ''
while n>0:
	a += '0' if n%2 == 0 else '1'
	n = int(n/2)
	
print(a[::-1])