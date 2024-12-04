from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd

# prompt: genera un metodo para resolver sistemas de ecuaciones utilizando el metodo jacobi

import numpy as np


#El método de Jacobi es un método iterativo para resolver sistemas de ecuaciones lineales. Funciona bien si la matriz 𝐴 es diagonal dominante.
def jacobi(A, b, x0, tol=1e-6, max_iter=10000):
  """
  Resuelve un sistema de ecuaciones lineales utilizando el método de Jacobi.

  Args:
    A: Matriz de coeficientes del sistema.
    b: Vector de términos independientes.
    x0: Vector de aproximación inicial.
    tol: Tolerancia para la convergencia.
    max_iter: Número máximo de iteraciones.

  Returns:
    Vector de solución aproximada o None si no converge.
  """
  n = len(b)
  x = x0.copy()
  for k in range(max_iter):
    x_new = np.zeros(n)
    for i in range(n):
      x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    if np.linalg.norm(x_new - x) < tol:
      return x_new
    x = x_new
  return None  # No converge


# Ejemplo de uso
A = np.array([[10, -1, 2, 0],
              [-1, 11, -1, 3],
              [2, -1, 10, -1],
              [0, 3, -1, 8]])
b = np.array([6, 25, -11, 15])
x0 = np.zeros(4)    

x = jacobi(A, b, x0)

if x is not None:
  print("Solución aproximada:")
  print(x)
else:
  print("El método de Jacobi no converge.")
