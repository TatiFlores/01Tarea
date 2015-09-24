import numpy as np
import scipy.integrate

wavelength = np.loadtxt('sun_AM0.dat', usecols=[0])
power = np.loadtxt('sun_AM0.dat', usecols=[1])

#Cambio de unidades
#wavelength*=10 #[A]
#power*=100 #[ergs/(s*cm2*A)]

energia=scipy.integrate.trapz(power, wavelength)
print energia

def func(x):
    '''Retorna la funcion que se desea integrar entre 0 y inf'''
    return x**3/(np.exp(x)-1)

laotraenergy=scipy.integrate.quad(func,0,np.inf)
print laotraenergy
