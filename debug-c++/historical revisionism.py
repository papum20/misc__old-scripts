import random


n = random.choice(range(1,16))
print(n)

print(' '.join([str(random.choice(range(1,40))) for i in range(n)]))
