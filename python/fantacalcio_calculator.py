partite = open('fantacalcio.txt','r').readlines()
calendario = [ [[5,3],[4,2],[6,1]], [[3,6],[1,4],[2,5]], [[2,3],[5,1],[4,6]], [[4,3],[1,2],[6,5]], [[3,1],[5,4],[2,6]], [[5,3],[2,4],[1,6]], [[6,3],[4,1],[5,2]], [[3,2],[1,5],[6,4]], [[3,4],[2,1],[5,6]], [[1,3],[4,5],[6,2]] ]
classifica = [0,0,0,0,0,0]

count = 1
giornata = 0
partita = 0

for i in partite:
    if count%4 == 0:
        print('\n',classifica,'\n')
        count += 1
        continue

    count += 1

      
    p = i.split()
    a = float(p[0])
    b = float(p[1])
    ga = (a-60)//6 if a >= 66 else 0
    gb = (b-60)//6 if b >= 66 else 0
    
    if ga == gb and abs(a-b) >= 4:
        if a>b:
            ga += 1
        else:
            gb += 1
            
    elif abs(ga-gb) == 1 and abs(a-b) < 3:
        ga = max(ga,gb)
        gb = ga

    print(ga,gb)


    if ga > gb:
        classifica[calendario[giornata%10][partita][0]-1] += 3
    elif gb > ga:
        classifica[calendario[giornata%10][partita][1]-1] += 3
    else:
        classifica[calendario[giornata%10][partita][0]-1] += 1
        classifica[calendario[giornata%10][partita][1]-1] += 1


    if partita == 2:
        partita = 0
        giornata += 1
    else:
        partita += 1


print(classifica)
