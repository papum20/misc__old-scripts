import random



n = random.choice(range(10,50))
print(n)
for i in range(n):
    print(random.choice(range(1,n+1)),' ',random.choice(range(1,100)))
