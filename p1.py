'''
En este codigo se grafica el espectro solar
'''


import numpy as np
from pylab import *

wavelength = np.loadtxt('sun_AM0.dat', usecols=[0])
power = np.loadtxt('sun_AM0.dat', usecols=[1])

#Cambio de unidades
wavelength*= 10 #[A]
power*= 100 #[ergs/(s*cm2*A)]

semilogx(wavelength,power)
xlabel('$Longitud\,de\,onda\,[\AA] $')
ylabel('$Intensidad\, [ergs \cdot s^{-1} \cdot cm^{2} \cdot \AA]$')
title('$Espectro\,solar$')
grid(True)
savefig("Espectro_solar")
show()
