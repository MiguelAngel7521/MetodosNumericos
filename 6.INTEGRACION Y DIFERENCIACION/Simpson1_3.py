from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd

def RSimpson1_3(f, a, b, n):
  h = (b-a)/n
  x = a
  Sfxj = 0
  Sfxi = 0
  for i in range(1, n):
    x += h
    if i % 2 == 0:
      Sfxj += f(x)
    else:
      Sfxi += f(x)
  return (h/3)*(f(a)+4*Sfxi+2*Sfxj+f(b))
#Ejemplo de uso
f = lambda x : math.sqrt(x)+math.e**(-2*x)
resultado = RSimpson1_3(f, 2, 3, 1000)
print("Resultado de RSimpson1_3 para f:", resultado)

# definir f funcion de x, a y b como limites inferior y superior y n numero de pasos
def RSimpson3_8(f, a, b, n):
  h = (b-a)/n
  x = [a + i * h for i in range(n + 1)]
  y = [f(xi) for xi in x]
  I = (3 * h / 8) * (y[0] + 3 * sum(y[1:n-1:3]) + 3 * sum(y[2:n:3]) + 2 * sum(y[3:n-2:3]) + y[n])

  return I
#Ejemplo de uso
f2 = lambda x : (x*(100-x))/(125)
resultado2 = RSimpson3_8(f2, 0, 5, 1000)
print("Resultado de RSimpson3_8 para f2:", resultado2)

