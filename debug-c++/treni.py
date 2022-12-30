import random

n = random.choice(range(5,15))
print(n)
for i in range(n):
	print(' '.join([str(random.choice(range(1,15))),str(random.choice(range(1,15)))]))
print('\n')
