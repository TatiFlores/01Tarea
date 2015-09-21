from math import *

#Funcion que nos ayuda a evaluar las funciones
def fx(x, f):
    return eval(f)

#n: numero de x
#a y b: los intervalos de la integral
#f: La funcion a integrar
def simpson(n, a, b, f):
    h = (b - a) / n
    suma = 0.0
    for i in range(1, n):
        x = a + i * h
        if(i % 2 == 0):
            suma = suma + 2 * fx(x, f)
        else:
            suma = suma + 4 * fx(x, f)
    suma = suma + fx(a, f) + fx(b, f)
    integral = suma * (h / 3)
    return (integral)
