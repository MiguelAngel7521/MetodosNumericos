from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd



#El método de Laguerre es un método iterativo para encontrar una raíz de un polinomio 𝑃(𝑥)
#Es especialmente útil porque converge rápidamente y puede encontrar raíces complejas.
def Laguerre(f, f1, f2, x0, n, error=1e-6):
  i = 0
  x1 = 0
  while(abs(f(x1))>error):
    G = (f1(x0))/(f(x0));
    H = G**2-((f2(x0))/(f(x0)));
    if(abs(G+sqrt((n-1)*(n*H-G**2)))>abs(G-sqrt((n-1)*(n*H-G**2)))):
      dx = n/(G+sqrt((n-1)*(n*H-G**2)));
    else:
      dx = n/(G-sqrt((n-1)*(n*H-G**2)));
    x1 = x0 - dx;
    #print(i, ".- G(x)=", G, " H(x)=", H, " dx=", dx, " x1=", x1, " f(x1)=", f(x1))
    i += 1
    x0 = x1
  return x1

def coeficientes(c, r):
  i = len(c)-1
  b1 = c[i]
  resultado = []
  resultado.insert(0, b1)
  while(i > 1):
    i -= 1
    b = c[i]+r*b1
    resultado.insert(0, b)
    b1 = b
  return resultado

def evaluar(c, x0, error):
  #print(c)
  def g(x):
    i = 0
    resultado = 0
    while (i < len(c)):
      resultado += c[i]*x**i
      i += 1
    return resultado
  i1 = 0
  c1 = []
  while (i1 < len(c)):
    c1.append(c[i1]*i1)
    i1 += 1
  c1.pop(0)
  #print(c1)
  def g1(x):
    i = 0
    resultado = 0
    while (i < len(c1)):
      resultado += c1[i]*x**i
      i += 1
    return resultado
  i2 = 0
  c2 = []
  while (i2 < len(c1)):
    c2.append(c1[i2]*i2)
    i2 += 1
  c2.pop(0)
  #print(c2)
  def g2(x):
    i = 0
    resultado = 0
    while (i < len(c2)):
      resultado += c2[i]*x**i
      i += 1
    return resultado
  return Laguerre(g, g1, g2, x0, len(c)-1, error)

def deflacion(c, x0, error = 1e-6):
  n = -1
  raices = []
  while(n != 1):
    n = len(c)-1
    r = evaluar(c, x0, error)
    raices.append(r)
    print (c, " raiz hallada=", r)
    c = coeficientes(c, r)
  print("Raices encontradas:")
  return print( raices )
# Ejemplo de uso para la ecuacion: x**4-22x**3+164x**2-458x+315
coef = [315, -458, 164, -22, 1]
deflacion(coef, 3, 1e-6)
