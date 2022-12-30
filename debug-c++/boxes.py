
boxes = [4]



for n in range(2,5001):

    m = 999999
    i1 = 0
    i2 = 0
    l = len(boxes)
    if l %2 == 0:
        for i in range(l//2):
            if boxes[i] + boxes[l-1-i] < m:
                m = boxes[i] + boxes[l-1-i]
                i1 = i
                i2 = l-1-i
    else:
         for i in range(l//2+1):
            if boxes[i] + boxes[l-1-i] < m:
                m = boxes[i] + boxes[l-1-i]
                i1 = i
                i2 = l-1-i

    
    b = 999999
    d1 = 0
    d2 = 0
    for i in range(1,n//2+1):
        if n%i == 0:
            if 2*(i + n/i) < b:
                b = int(2*(i +n/i))
                d1 = int(i)
                d2 = n//i
                


    boxes.append(int(m if m<b else b))


##    print('{}{}: {}+{}={} / {}*{}={}          {}'.format('A'if m<b else 'B',n,i1+1,i2+1,m,d1,d2,b,boxes[n-1]))
    







print(boxes)
