# enviar el vector de coeficientes "a" en el mismo orden que en deflacion, enviar ademas r y s, (parametros)
from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd



#El método de Bairstow encuentra raíces de un polinomio dividiendo el problema en raíces cuadráticas.
# Es ideal para encontrar raíces reales y complejas, y no requiere estimaciones iniciales complejas.
def Bairstow(a, r, s, error=1e-6, max_iterations=10000):
    n = len(a)
    roots = []
    aux1 = r
    aux2 = s
    count = 0
    fac = 0

    for _ in range(max_iterations):
        print(count, ".- ", a)
        b = [0] * n
        c = [0] * n

        b[-1] = a[-1]
        b[-2] = a[-2] + r * b[-1]

        for i in range(n - 3, -1, -1):
            b[i] = a[i] + r * b[i + 1] + s * b[i + 2]
        print(b)

        c[-1] = b[-1]
        c[-2] = b[-2] + r * c[-1]

        for i in range(n - 3, -1, -1):
            c[i] = b[i] + r * c[i + 1] + s * c[i + 2]
        print(c)
        dr = (b[1] * c[2] - b[0] * c[3]) / (c[2] ** 2 - c[1] * c[3])
        ds = (b[0] * c[2] - b[1] * c[1]) / (c[2] ** 2 - c[1] * c[3])

        r -= dr
        s -= ds
        print("dr=", dr, "ds=", ds, "r=", r, "s=", s)
        count += 1

        if abs(b[0]) < error and abs(b[1]) < error:
            fac += 1
            roots.append((r+sqrt(r**2-4*1*-s))/2)
            roots.append((r-sqrt(r**2-4*1*-s))/2)
            print("roots: ", roots, fac)
            count = 0
            a = b[2:]
            n -= 2
            if n <= 3:
                break
            r = aux1
            s = aux2
    print(a)
    if(n == 3):
      roots.append((-a[1]+sqrt(a[1]**2-4*a[0]*a[2]))/(2*a[2]))
      roots.append((-a[1]-sqrt(a[1]**2-4*a[0]*a[2]))/(2*a[2]))
    else:
      roots.append(-a[0]/a[1])
    print("Raices encontradas:", roots)
    return roots
# Ejemplo de uso
cf = [315, -458, 164, -22, 1]
Bairstow(cf, 3, 1)
