h = 10
r = 5
F = 10

Vtank = 3.14*r**2*h
t = int(input('enter the time '))

Vwtr = F*t

if Vwtr> Vtank:
	print('overflow ')
	print('Volume ',Vwtr-Vtank)
elif Vwtr == Vtank:
	print('tank full ')
else:
	print('underflow condition ')
	ht = Vwtr/(3.14*r**2)
	hr = h - ht
	print('filled height ',ht,'remaining height ',hr)		
