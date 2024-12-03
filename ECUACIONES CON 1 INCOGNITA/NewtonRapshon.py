from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd


f = lambda x : math.cos(x)-x
f1 = lambda x : -math.sin(x)-1
def NewtonRaphson(funcion, derivada, x0, error = 1e-6):
  i = 1
  while abs(funcion(x0))>error:
    print("iteracion", i, ": x0 =", x0, "f(x0) =", funcion(x0))
    x0 = x0 - funcion(x0)/derivada(x0)
    i += 1
  return x0

resultado = NewtonRaphson(f, f1, 0.5)
print("Resultado de NewtonRaphson para f:", resultado)