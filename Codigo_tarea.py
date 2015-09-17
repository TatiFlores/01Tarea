import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import *

wavelength=np.loadtxt('sun_AM0.dat', usecols=[0])
power=np.loadtxt('sun_AM0.dat', usecols=[1])

#Cambio de unidades
wavelength*=10 #[Angstrom]
power*=100 #[ergs/(s*cm2*A)]

semilogx(wavelength,power)
xlabel('$Longitud\,de\,onda\,[\AA] $')
ylabel('$Flujo\, [ergs \cdot s^{-1} \cdot cm^{2} \cdot \AA]$')
title('$Espectro\,solar$')
grid(True)
savefig("Espectro_solar")
show()

#integral=h*[f(a)+f(b)+sum_fi]
n= len(wavelength)-1  #numero de particiones
a=wavelength[0]
b=wavelength[n]
h=(b-a)/(2*n)

fa=power[0]#f(a)
fb=power[n]#f(b)
sum_fi=-fa-fb

for i in range(n):
    sum_fi+=power[i]

integral=h*(fa+fb+(2*sum_fi))
print integral
