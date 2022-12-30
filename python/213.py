res = 0

for i in range(1, 10000):
    a = round(i,-3)
    b = i
    for j in range(1,4):
        b = round(b,-j)
    if(a!=b):
        res+=1
        print(i)
print(res)
