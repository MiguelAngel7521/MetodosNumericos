from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd



#es una extensión del método de Newton-Raphson que utiliza información adicional (la segunda derivada de la función) 
#para mejorar la precisión de la aproximación de la raíz. Es un método iterativo con convergencia cúbica, 
# lo que significa que converge mucho más rápido que Newton-Raphson si la aproximación inicial está cerca de la raíz

f = lambda x : math.log(x)
f1 = lambda x : 1/x
f2 = lambda x : -1/(x**2)

def Halley(funcion, derivada, derivada2, x0, error = 1e-6):
  i = 1
  while abs(funcion(x0))>error:
    print("iteracion", i, ": x0 =", x0, "f(x0) =", funcion(x0))
    x0 = x0 - 2*funcion(x0)*derivada(x0)/(2*derivada(x0)**2-funcion(x0)*derivada2(x0))
    i += 1
  return x0

resultado = Halley(f,f1,f2, 2)
print("Resultado de Halley para f:", resultado)