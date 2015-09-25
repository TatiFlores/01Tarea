import numpy as np
import scipy.integrate

wavelength = np.loadtxt('sun_AM0.dat', usecols=[0])
power = np.loadtxt('sun_AM0.dat', usecols=[1])


energia = scipy.integrate.trapz(power, wavelength)
print 'integral p2 calculado con scipy',energia

def f(x):
        '''Retorna la funcion que se desea integrar entre 0 y pi/2'''
        return (((np.tan(x))**3.)*((np.cos(x))**(-2.0)))/(np.exp(np.tan(x))-1)

laotraenergy=scipy.integrate.quad(f,0.0001,np.pi/2)[0]
print 'integral p calculado con scipy',laotraenergy
