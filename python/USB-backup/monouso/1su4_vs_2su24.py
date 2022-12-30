import random

dado=[1,2,3,4,5,6]

sensateesperienze=int(input('quanti tentativi?'))

vittorie=0
for t in range(sensateesperienze):
    usciti=[]
    for x in range(4):
        lancio=random.choice(dado)
        print('lancio:',lancio)
        if lancio==6:
            usciti.append(lancio)
        else:
            continue
    print('usciti:', usciti)
    if len(usciti)>=1:
        vittorie+=1
    print('VITTORIE:', vittorie)
    print()

print('------------------------------------------')
print()
print('------------------------------------------')

viTTorie=0
for t2 in range(sensateesperienze):
    usciti2=[]
    for x2 in range(24):
        lancio2=random.choice(dado)
        print('lancio2:',lancio2)
        if lancio2==6:
            usciti2.append(lancio2)
        else:
            continue
    print('usciti2:', usciti2)
    if len(usciti2)>=2:
        viTTorie+=1
    print('VITTORIE2:', viTTorie)
    print()

print('------------------------------------------')
print('1 su 4 tiri:', vittorie)
print('2 su 24 tiri:', viTTorie)
print()
print('Percentuale1:', vittorie/sensateesperienze*100)
print('Percentuale2:', viTTorie/sensateesperienze*100)
print()
print('The winner is:')
if vittorie>viTTorie:
    print('1su4')
elif vittorie==viTTorie:
    print('PAREGGIO!?')
else:
    print('2su24')