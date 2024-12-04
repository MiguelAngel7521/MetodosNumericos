from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd




#RungeKutta1 es exactamente igual al metodo de Euler
def RungeKutta2(f, x0, y0, x, n):
  h = (x-x0)/n
  for i in range(n):
    k1 = f(x0, y0)
    k2 = f(x0+h, y0+k1*h)
    y = y0 + ((1/2)*k1+(1/2)*k2)*h
    print(x0, y0)
    y0 = y
    x0 += h
  print(x0, y0)
  return y
#Ejemplo de uso
def f(x, y):
  return 3*x**2
resultado1 = RungeKutta2(f, 0, 2, 3, 10)
print("Resultado de RungeKutta2 para f:", resultado1)




print("RungeKutta3")
def RungeKutta3(f, x0, y0, x, n):
  h = (x-x0)/n
  for i in range(n):
    k1 = f(x0, y0)
    k2 = f(x0+(1/2)*h, y0+(1/2)*k1*h)
    k3 = f(x0+h, y0-k1*h+2*k2*h)
    y = y0 + (1/6)*(k1+4*k2+k3)*h
    print(x0, y0)
    y0 = y
    x0 += h
  print(x0, y0)
  return y
resultado2 = RungeKutta3(f, 2, 8, 4, 8)
print("Resultado de RungeKutta3 para f:", resultado2)



def RungeKutta4(f, x0, y0, x, n):
  h = (x-x0)/n
  for i in range(n):
    k1 = f(x0, y0)
    k2 = f(x0+(1/2)*h, y0+(1/2)*k1*h)
    k3 = f(x0+(1/2)*h, y0+(1/2)*k2*h)
    k4 = f(x0+h, y0+k3*h)
    y = y0 + (1/6)*(k1+2*k2+2*k3+k4)*h
    print(x0, y0)
    y0 = y
    x0 += h
  print(x0, y0)
  return y
resultado3 = RungeKutta4(f, 0, 1, 3, 20)
print("Resultado de RungeKutta4 para f:", resultado3)