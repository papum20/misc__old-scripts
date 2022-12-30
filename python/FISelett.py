print('\n1 - campo E\n2 - U,V\n3 - capacità,condensatori')
mode = int(input('\nselect mode: '))

if mode == 1:
        print('\nE=F/q=kQ/r^2')
        print('\nflusso q=∆V/∆t=Svcos@')
        print('\nflusso di E=EScos@;flusso superficie chiusa=Qtot/e')
        print('\nE:piano=sigma/2e;linea=lambda(densità lineare carica)/(2p e r);sfera out=kQ/r^2;sfera in=kQr(=d)/(R^3)')
        
if mode == 2:
        print('\nU=kQq/r')
        print('\nV=kQ/r=W/q=∆U/q=Ez(d da origine carica(es piano))')
        print('\nE=∆V/∆s')
        print('\ncircuitazione=somm.(E∆l cos@=-∆V);circ.(E)=0')
        
if mode == 3:
        print('\nE=sigma/e')
        print('\nC=Q/V;C sfera=4p e R')
        print('E condensatori:in=sigma/e;out=0;C=eS/d=er C0')
        print('in parallelo:V=V,C=C+C;in serie:Q=Q,1/C=1/C+1/C')
		
