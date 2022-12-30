for i in range(1000,int(input('n: '))+1):
    n = str(i)
    a = n[0]
    b = n[1]
    c = n[2]
    d = n[3]
    zero = 0
    uno = 0
    due = 0
    tre = 0
    
    for x in [a,b,c,d]:
        if int(x) == 0:
            zero += 1
    for x in [a,b,c,d]:
        if int(x) == 1:
            uno += 1
    for x in [a,b,c,d]:
        if int(x) == 2:
            due += 1
    for x in [a,b,c,d]:
        if int(x) == 3:
            tre += 1

    if zero == int(a) and uno == int(b) and due == int(c) and tre == int(d):
        print(i)
