import math

a = 1
b = 1/math.sqrt(2)
t = 1/4
p = 1

for i in range(int(input('2^n digits: '))):
	a1 = (a+b)/2
	b = math.sqrt(a*b)
	t = t - p*((a - a1)**2)
	p = 2*p
	a = a1

print(((a + b)**2)/(4*t))