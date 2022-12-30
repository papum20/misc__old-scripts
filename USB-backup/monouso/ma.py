def f(x):
	#return float(9*(x**4)+42*(x**3)+48*(x**2)+6*x-9)**(1/2)
	a=(3*x+3)/2
	return ((a)*(a-x)*(a-(x+1))*(a-(x+2)))**(1/2)
#print(f(int(input('a: '))))
for i in range(2000):
	print(i)
	print(f(i))