from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd


def Euler(f, x0, y0, x, n):
  h = (x-x0)/n
  for i in range(n):
    y = y0 + f(x0, y0)*h
    print('paso', i,';',  x0, y0)
    y0 = y
    x0 += h
  print('paso', n,';', x0, y0)
  return y
#Ejemplo de uso
def f(x, y):
  return 3*x**2
resultado=Euler(f, 0, 2, 3, 50)
print("Resultado de Euler para f:", resultado)