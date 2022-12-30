while True:
	print('\n1 - onde\n2 - suono\n3 - luce\n4 - gr. fotometriche e formule..')
	mode = int(input('select mode: '))
	
	if mode == 1:
		print('\nv = ✓(Ft/dl); (tensione/densità lineare = m/L)')
		print('y = a cos(2π/T + fi0) = a cos(omega t + fi = a cos(2πx/lambda + fi) = a cos[2π(x-vt)/lambda + fi]')
		print('y = A cos(omega t + fi/2); A = 2 a cos(fi/2)')
		print('S1P - S2P = (k or k+1) lambda')
		
	if mode == 2:
		print('\nint. sonora I(W/m^2) = E/(A ∆t) = P/A = Ps/(4πr^2)')
		print('liv. int. son. Ls(dB) = 10 log(I/I 0); I 0 = 10^-12')
		print('eco: ∆t = 2d/v')
		print('modi norm.: lambda n = 2L/n (n mezze oscillazioni; nodi = n+1)')
		
	if mode == 3:
		print('\nn(rifraz.) = c/v')
		print('Snell (rifl): sen(i)/sen(r) = n2/n1')
		print('angolo limite: // con r = 90')
		print('Young: lambda/d = y/l')
		print('S1Bk - S2Bk = k lambda')
		print('d sen(alfa k) = k lambda')
		print('scura: d sen = (m-1/2) lambda')
		
	if mode == 4:
		print('\nIrradam. Er(W/m^2) = Energia/(A ∆t) = Ps/(4 π r^2)')
		print('Intens. radiaz. Ir = Energ./(omega ∆t); omega = A/r^2')
		print('Intens. luminosa = Ir soggettiva')
		print('candela(cd) = Int. lum., f=5.4x10^14, Ir = 1/683(W/sr (seradianti))')
		print('flusso lumin. phi(grande)L (lm) = quantità luce emessa / s, soggettiva; (lumen = 1cd sr')
		print('illuminam. EL (lx) = phi(big) /(4π r^3);')