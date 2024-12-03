from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd


def f(x, y):
  return x**2*y
# definir la funcion que van a evaluar, debe ser de tipo: dx/dy = (tu funcion f(x, y))
# Enviar la funcion f, puntos calculados x0 y y0, punto a calcular x y n numero de pasos
# Enviar a demas un valor calculado anterior (y_1) n numero de pasos, y m numero de correctores
def HeunSinPrincipio(f, x0, y0, y_1, x, n, m):
  h = (x-x0)/n
  for i in range(n):
    y = y_1+f(x0, y0)*2*h
    print("Predictor y", i+1, ": ", y, sep = '')
    for j in range(m):
      y = y0+((f(x0, y0)+f(x0+h, y))/2)*h
      print("Corrector", j+1, ":", y)
    y_1 = y0
    x0 += h
    y0 = y
  print(x0, y0)
  return y
resultado = HeunSinPrincipio(f, 2, 8, 5.359375, 4, 8, 4)
print("Resultado de HeunSinPrincipio para f:", resultado)