'''
Este codigo corresponde a la pregunta 3 de la tarea 1.
Su objetivo es integrar numericamente la funcion de planck,
para lo que se utilizan las reglas del punto medio y de
simpson
'''
import numpy as np
import matplotlib.pyplot as plt
from astropy import constants as const
from astropy import units as u

def simpson_puntomedio(n, a, b, f):
    '''
    Recibe una funcion y dos puntos en sus extremos y
    encuentra la integral bajo la curva usando la regla de
    simpson, y usando la regla del punto medio para sus
    extremos
    '''
    #n: numero de particiones
    #a y b: los intervalos de la integral
    #f: La funcion a integrar
    h = (b - a) / n
    suma = 0.0
    for i in range(1, n):
        x = a + i * h
        if (i==1):
            suma = suma + (x - a) * f((x + a) / 2)
        elif (i == (n-1)):
            suma = suma + (b - x) * f((x + b) / 2)
        elif(i % 2 == 0):
            suma = suma + 2 * f(x) * (h / 3)
        else:
            suma = suma + 4 * f(x) * (h / 3)
    return (suma)

def func(x):
    '''Retorna la funcion que se desea integrar entre 0 y pi/2'''
    return (((np.tan(x))**3.)*((np.cos(x))**(-2.0)))/(np.exp(np.tan(x))-1)

T=5778*u.K
h=const.h.cgs
kb=const.k_B.cgs
c=const.c.cgs

n=2
eps=10
while eps>=0.0001:
    integral=simpson_puntomedio(n, 0, (np.pi/2), func)
    eps=np.abs(integral - ((np.pi)**4) / 15)
    n+=1

energia=integral*((2 * np.pi * h / c**2) * (kb * T / h)**4)
print 'Energia total por unidad de area emitida por un cuerpo negro con T=5778 [K]: ', energia

ideal=T**4 * const.sigma_sb
print 'Caso ideal: ', ideal.cgs
