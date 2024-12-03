from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd
def fr(X, Y):
  if len(X) == 1:
      return Y[0]
  else:
      if len(X) == 2:
        return (Y[0]-Y[1])/(X[0]-X[1])
      else:
        return (fr(X[0:-1], Y[0:-1])-fr(X[1:], Y[1:]))/(X[0]-X[-1])

# utiliza una funcion recursiva f(x) -> f[x] te genera una ecuacion polinomica
# Enviar el vector de variables "x" y sus funciones "y" en fx
# Si no se envia un punto especifico "p", la funcion devuelve otra funcion, que se puede usar para calcular puntos
def DifDivNewton(X, fX, p = 0):
  b = []
  n = len(X)
  for i in range(n):
    b.append(fr(X[i::-1], fX[i::-1]))
  display(b)
  if p == 0:
    def f(x):
      r = 0
      for i in range(n):
        s = b[i]
        for j in range(i):
          s *= (x - X[j])
        r += s
      return r
    return f
  else:
    r = 0
    for i in range(n):
      s = b[i]
      for j in range(i):
        s *= (p - X[j])
      r += s
    return r
#ordenados desde x
X = [9.1, 13.7, 18.3, 22.9]
fX = [20.6, 13.9, 11.7, 11.1]
funcionnewton = DifDivNewton(X, fX)
funcionnewton(6)