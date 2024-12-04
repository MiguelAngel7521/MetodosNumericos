from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd

def f(x, y):
  return x**2 + 2*x - 2*y


#se basa en la serie de Taylor
def Adams2(f, x0, y0, y_1, x, n):
  h = (x-x0)/n
  x_1 = x0-h
  for i in range(n):
    y = y0+h*((3/2)*f(x0, y0)-(1/2)*f(x_1, y_1))
    print(x0, y0)
    y_1 = y0
    y0 = y
    x_1 = x0
    x0 += h
  print(x0, y0)
  return y
resultado1 = Adams2(f, 2, 8, 8.765217, 3, 8)
print("Resultado de Adams2 para f:", resultado1)

def Adams3(f, x0, y0, y_1, y_2, x, n):
  h = (x-x0)/n
  x_1 = x0-h
  x_2 = x_1-h
  for i in range(n):
    y = y0+h*((23/12)*f(x0, y0)-(16/12)*f(x_1, y_1)+(5/12)*f(x_2, y_2))
    print(x0, y0)
    y_2 = y_1
    y_1 = y0
    y0 = y
    x_2 = x_1
    x_1 = x0
    x0 += h
  print(x0, y0)
  return y
resultado2 = Adams3(f, 2, 8, 8.760017, 3.375, 4, 10000)
print("Resultado de Adams3 para f:", resultado2)

def Adams4(f, x0, y0, y_1, y_2, y_3, x, n):
  h = (x-x0)/n
  x_1 = x0-h
  x_2 = x_1-h
  x_3 = x_2-h
  for i in range(n):
    y = y0+h*((55/24)*f(x0, y0)-(59/24)*f(x_1, y_1)+(37/24)*f(x_2, y_2)-(9/24)*f(x_3, y_3))
    print(x0, y0)
    y_3 = y_2
    y_2 = y_1
    y_1 = y0
    y0 = y
    x_3 = x_2
    x_2 = x_1
    x_1 = x0
    x0 += h
  print(x0, y0)
  return y
resultado3 = Adams4(f, 2, 8, 8.765217, 3.375, 1.953125, 4, 8)
print("Resultado de Adams4 para f:", resultado3)