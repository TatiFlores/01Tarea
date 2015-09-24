'''Este codigo muestra la integracion de la la funcion
graficada en la pregunta p1, con lo que se obtiene la
constante solar, y a partir de lo cual puede obtener
la luminosidad total del sol'''

import numpy as np
from math import *
from astropy import units as u
from astropy import constants as const

wavelength = np.loadtxt('sun_AM0.dat', usecols=[0])
power = np.loadtxt('sun_AM0.dat', usecols=[1])

def trapecio(x,y,n):
    '''
    Recibe dos arreglos y la cantidad de particiones, y
    encuentra la integral bajo la curva usando la regla del
    trapecio
    '''
    integral_trap=0
    for i in range(n):
        dx = x[i+1] - x[i]
        integral_trap+= (y[i] + y[i+1]) * (dx / 2)
    return integral_trap

#Calculo integral buscada
K_t = trapecio(wavelength, power, (len(wavelength)-1))
K_t*= (u.W / (u.m)**2)
Ls_t = K_t * 4 * np.pi * const.au**2
print "Constante solar [W/m^2]:", K_t
print "Luminosidad total del sol [W]:", Ls_t
