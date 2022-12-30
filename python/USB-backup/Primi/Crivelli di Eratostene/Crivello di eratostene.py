stop = 'n'
while stop == 'n':
        num = int(input("inserire n:"))
        criv = int((num+1) ** (1/2))
        i = 2
        fact = [1,]
        while i <= criv:
                if (num % i) == 0:
                        fact.append(i)
                if i == 2:
                    i += 1
                else:
                    i += 2
        if fact == [1]:
                print(num, 'è primo!')
        else:
                print(fact)
        print()
        print('fermare il programma? [Y/n]')
        print()
        stop = input()
        print()
        if stop == 'n':
                print('RIAVVIO...')
                print()
