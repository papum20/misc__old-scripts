n=0
for i in range(10,98):
    if (i+2)%2==0 or (i+2)%5==0:
        continue
    a = str(i)+str(i+1)+str(i+2)
    if int(a)%11==0:
        continue
    print(a)
    n+=1

print(n)
