from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd
#El método de Muller es una extensión del método de la secante que utiliza una parábola en lugar de una línea para aproximar las raíces.
# esto lo hace especialmente útil para encontrar raíces complejas.
# Consiste en obtener una parabola que pasa por 3 puntos elegidos. dichos coeficientes son reemplazados en la ecuacion cuadratica
#para obtener el valor de la parabola que intersecta X
#la parabola se define f(x)=ax**2+bx+c
def muller(f, x0, x1, x2, error=1e-6):
  i = 1
  h1 = x1 - x0
  h2 = x2 - x1
  d1 = (f(x1) - f(x0))/h1
  d2 = (f(x2) - f(x1))/h2
  d = (d2 - d1)/(h2 + h1)

  while True:
    b = d2 + h2*d
    D = (b**2 - 4*f(x2)*d)**(1/2)

    if abs(b - D) < abs(b + D):
      E = b + D
    else:
      E = b - D

    h = -2*f(x2)/E
    p = x2 + h

    print('Iteración:', i, ' x:', p, ' Error:', abs(h))

    if abs(h) < error:
      return p

    x0 = x1
    x1 = x2
    x2 = p

    h1 = x1 - x0
    h2 = x2 - x1
    d1 = (f(x1) - f(x0))/h1
    d2 = (f(x2) - f(x1))/h2
    d = (d2 - d1)/(h2 + h1)
    i += 1


# definir la funcion f y un punto cualquiera
def Muller(f, x0, error=1e-6):
  x1 = x0+0.5
  x2 = x1+0.5
  i = 0
  x3 = 0
  while(abs(f(x3))>error):
    h0 = x1-x0
    h1 = x2-x1
    rho0 = (f(x1)-f(x0))/h0
    rho1 = (f(x2)-f(x1))/h1
    c = f(x2)
    a = (rho1-rho0)/(h0+h1)
    b = rho1 + (a*h1)
    if(abs(b+sqrt(b**2-4*a*c))>abs(b-sqrt(b**2-4*a*c))):
      x3 = x2+((-2*c)/(b+sqrt(b**2-4*a*c)))
    else:
      x3 = x2+((-2*c)/(b-sqrt(b**2-4*a*c)))
    print(i, ".- x0=",x0," x1=",x1," x2=",x2," h0=",h0," h1=",h1," ρ0=",rho0," ρ1=",rho1," a=",a," b=",b," c=",c," x3=",x3," f(x3)=",f(x3))
    i += 1
    x0 = x1
    x1 = x2
    x2 = x3
  return x2