from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd


f = lambda x : math.log(x)
f1 = lambda x : 1/x
f2 = lambda x : -1/(x**2)
def falsaPosicion(funcion, x0, x1, error = 1e-6):
  if funcion(x1) * funcion(x0) < 0:
    i = 1
    while abs(funcion((funcion(x0)*x1-funcion(x1)*x0)/(funcion(x0)-funcion(x1))))>error:
      print("iteracion", i, ": x1 =", x1, "x0 =", x0, "puntomedio =", (funcion(x0)*x1-funcion(x1)*x0)/(funcion(x0)-funcion(x1)))
      if funcion((funcion(x0)*x1-funcion(x1)*x0)/(funcion(x0)-funcion(x1)))*funcion(x0)<0:
        x1 = (funcion(x0)*x1-funcion(x1)*x0)/(funcion(x0)-funcion(x1))
      else:
        x0 = (funcion(x0)*x1-funcion(x1)*x0)/(funcion(x0)-funcion(x1))
      i += 1
    return (funcion(x0)*x1-funcion(x1)*x0)/(funcion(x0)-funcion(x1))
  else:
    print("Intervalo no valido")
    return
  
resultado =falsaPosicion(f, 2, 4, 1e-12)
print("Resultado de falsaPosicion para f:", resultado)