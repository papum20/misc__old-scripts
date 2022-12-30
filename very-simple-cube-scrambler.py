
list_scr = [[i for i in range(1,17)]]
print(list_scr,round(len(list_scr[0])/7, 0) )

n = 0

while n<7:
    print(n)
    n+=2

for s in list_scr:
    n=0
    while n < len(s):
        print(s[n:(n+7 if n<= len(list_scr) else -1 )] )
        n+=7
    
#    for i in range(len(s)):
#        print(s[i], '\n' if (i+1)%7==0 else ' ')
    
#   print((' '.join(s[n:n+7]))+'\n' while n < )