from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd


# METODO QUE ENCIERRA LA RAIZ 
# Es un método simple y robusto que funciona dividiendo el intervalo en dos partes iguales y seleccionando la subparte que contiene la raíz.
f = lambda x : x+math.log10(x)-5
def biseccion(funcion, liminf, limsup, error = 1e-12):
  if funcion(limsup) * funcion(liminf) < 0:
    i = 1
    while abs(funcion((liminf+limsup)/2))>error:
      print("iteracion", i, ": limsup =", limsup, "liminf =", liminf, "puntomedio =", (limsup+liminf)/2)
      if funcion((liminf+limsup)/2)*funcion(liminf)<0:
        limsup = (liminf+limsup)/2
      else:
        liminf = (liminf+limsup)/2
      i += 1
    return (liminf+limsup)/2
  else:
    print("Intervalo no valido")
    return
  
resultado =biseccion(f, 3, 5)
print("Resultado de biseccion para f:", resultado)