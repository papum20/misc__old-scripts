tot = 0
for c in range(-2018, 2019):
    for b in range(-2018, 2019):
        if c == (-6-2*b):
            tot+=1
            print(b,c)

print(tot)
