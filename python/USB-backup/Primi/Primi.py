for v in range(99):
    n=int(input('inserire numero:'))
    div=int((n/2)+1)
    list=[]
    for i in range(2,div):
        y=n%i
        if y==0:
            list.append(i)
            print(n,'non è primo')
            break
        else:
            continue
    if len(list)==0:
        print(n,'è primo')
    print('-----')