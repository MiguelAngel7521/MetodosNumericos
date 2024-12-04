from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd

#METODO ABIERTO
#UN SOLO VALOR SUPUESTO
#Este método utiliza la derivada de 
# Este método utiliza la derivada de 𝑓 ( 𝑥 ) f(x) para aproximar la raíz. Es muy eficiente cuando se tiene una buena estimación inicial 𝑥 0 x 0 ​ y 𝑓 ( 𝑥 ) f(x) es suficientemente suave.
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