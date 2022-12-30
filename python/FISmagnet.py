print('\n1 - teoria\n2 - correnti,spire\n3 - F,moto\n4 - flusso,circ')
mode = int(input('\nselect mode: '))

if mode == 1:
    print('\ncampo:retta da S a N')
    print('linee campo:da N a S')
    print('km=mu/(2pi)')
    print('mu=4pi 10^-7 N/A^2')
    
if mode == 2:
    print('\nAmpere:F tra correnti=(km i1 i2 l)/d')
    print('F magn=(i l) X B (vettoriale)')
    print('Biot-savart:B=km i/d')
    print('spira:campo:perpendicolare a piano')
    print('spira:B=(mu/2)(i/R (raggio))')
    print('spira:B a distanza y:(mu i R^2)/(2sqrt(R^2+y^2)^3)')
    print('solenoide:campo:zero fuori,parallelo a asse dentro')
    print('solenoide:B=(mu i (N spire))/l')

if mode == 3:
    print('\nlorentz:Fq=qv X B (vettoriale)')
    print('selettore velocita:v=E/B')
    print('tensione di Hall:deltaVh=dvB')
    print('velocita perpendicolare a campo:moto circolare')
    print('..r=(mv)/(abs(q)B);T=(2pi m)/(abs(q)B)')
    print('..moto c.:a(centrip)=v^2/r;v=(2pi r)/T')
    print('obliqua:moto elicoidale:\n')
    print('..r=mv(perp)/(abs(q)B)')
    print('deltaS(passo)=v(paral)T=(v(par)2pi m)/(abs(q)B)')

if mode == 4:
    print('\nflussoB=sommatoria(B deltaS(area) (scalare))')
    print('flusso piano=(B S(area) (scalare))')
    print('flusso area chiusa=0')
    print('circuitazioneB=sommatoria(B deltal(spostamento) (scalare))')
    print('correnti concatenate:stesso contorno;B non conservativo')
    print('circ.B=mu sommatoria(i(k) (correnti concatenate))')
