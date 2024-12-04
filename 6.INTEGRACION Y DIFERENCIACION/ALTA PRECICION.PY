from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd


#las formulas de alta precision parten de la serie de taylor
#1ra derivada 2termino
#2da derivada 3terminos
f = lambda x : (x*(100-x))/(125)
def formAltaPrecision2t(f, x, h):
  return (f(x+h)-f(x))/h
#Ejemplo de uso
resultado1 = formAltaPrecision2t(f, 5, 0.000001)
print("Resultado de AltaPrecision2t para f:", resultado1)


def formAltaPrecision3t(f, x, h):
  return (-f(x+2*h)+4*f(x+h)-3*f(x))/(2*h)
#Ejemplo de uso
resultado2 = formAltaPrecision3t(f, 5, 0.01)
print("Resultado de AltaPrecision3t para f:", resultado2)

def ExtrapolacionRichardson(f, x, h):
  h2 = h/2
  f1h1 = formAltaPrecision3t(f, x, h)
  print(f1h1)
  f1h2 = formAltaPrecision3t(f, x, h2)
  print(f1h2)
  return (4/3)*f1h2-(1/3)*f1h1
#Ejemplo de uso
resultado3 = ExtrapolacionRichardson(f, 5, 0.05)
print("Resultado de ExtrapolacionRichardson para f:", resultado3)