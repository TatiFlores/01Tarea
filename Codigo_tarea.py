import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import *

wavelength=np.loadtxt('sun_AM0.dat', usecols=[0])
power=np.loadtxt('sun_AM0.dat', usecols=[1])

#Cambio de unidades
wavelength*=10 #[A]
power*=100 #[ergs/(s*cm2*A)]

semilogx(wavelength,power)
xlabel('$Longitud\,de\,onda\,[\AA] $')
ylabel('$Flujo\, [ergs \cdot s^{-1} \cdot cm^{2} \cdot \AA]$')
title('$Espectro\,solar$')
grid(True)
savefig("Espectro_solar")
show()

#Calculo integral: metodo de trapecio y regla de simpson
n= len(wavelength)-1  #numero de particiones
a=wavelength[0]
b=wavelength[n]
fa=power[0]#f(a)
fb=power[n]#f(b)
h=(b-a)/n

#Metodo del trapecio (_t)
suma_t=-fa-fb  #la sumatoria de los fi no incluye a los terminos extremos
integral_t=0

for i in range(len(wavelength)):
    suma_t+=(2*power[i])

integral_t=(h*(fa+fb+suma_t))/2
print "Luminosidad total del sol/metodo del trapecio:",integral_t

#Regla de simpson (_s)
integral_s=0
suma_s=-fa

for i in range(n): #range(n) para que no llegue al ultimo termino ( f(b) )
    if(i%2==0):
        suma_s+=(2*power[i])
    else:
        suma_s+=(4*power[i])

integral_s= (h*(suma_s+fa+fb))/3
print "Luminosidad total del sol/regla de simpson:",integral_s
