from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd

# definir f funcion de x, a y b como limites inferior y superior y n numero de pasos
def RTrapezoidal(f, a, b, n):
  h = (b-a)/n
  x = a
  Sfx = 0
  for i in range(1, n):
    x += h
    Sfx += f(x)
  return (h/2)*(f(a)+2*Sfx+f(b))
# Ejemplo de uso
def f(t):
  return 2 + 3*t - 0.5*t**2
f = lambda t : 2 + 3*t - 0.5*t**2
RTrapezoidal(f, 0, 4, 50000)
g = lambda x : math.e**x+x**2
RTrapezoidal(g, 2, 4, 500)
resultado = RTrapezoidal(f, 0, 4, 50000)
print("Resultado de RTrapezoidal para f:", resultado)

resultado_g = RTrapezoidal(g, 2, 4, 500)
print("Resultado de RTrapezoidal para*** g:", resultado_g)

# ROMBERT
# definir f funcion de x, a y b como limites inferior y superior y n numero de pasos
# se basa en la aplicacion sucesiva de la regla trapezoidal
def Romberg(f, a, b, n):
  I1 = RTrapezoidal(f, a, b, n)
  I2 = RTrapezoidal(f, a, b, n*2)
  print(I2)
  print(I1)
  return 4/3*(I2)-1/3*(I1)
#Ejemplo de uso
resultado = Romberg(f, 0, 4, 150)
print("Resultado de Rombert para f:", resultado)