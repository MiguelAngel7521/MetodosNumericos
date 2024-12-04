from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd

f = lambda t : 2 + 3*t - 0.5*t**2
# Solo enviar la funcion y los limites
def CuadraturaGauss(f, a, b):
  if a == -1 and b == 1:
    return f(-(1/math.sqrt(3))) + f(1/math.sqrt(3))
  else:
    xd = ((b+a)+(b-a)*(1/math.sqrt(3)))/2
    _xd = ((b+a)+(b-a)*(-1/math.sqrt(3)))/2
    dxd = (b-a)/2
    print(f(_xd)*dxd)
    print(f(xd)*dxd)
    return f(_xd)*dxd+f(xd)*dxd
resultado =CuadraturaGauss(f, 0, 4)
print("Resultado de CuadraturaGauss para f:", resultado)