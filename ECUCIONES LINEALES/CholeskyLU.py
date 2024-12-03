from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd

# Utilizar luego de conseguir las matrices L y U con otro metodo
def SolucionLU(L, U, b):
    n = len(L)
    y = np.zeros(n)
    x = np.zeros(n)

    for i in range(n):
      b[i] /= L[i][i]
      L[i, :] /= L[i][i]

    # Resolver Ly = b
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
    print("Matriz z:")
    print(y)
    print(np.matmul(L, y))
    print(b)
    for i in range(n):
      y[i] /= U[i][i]
      U[i, :] /= U[i][i]

    # Resolver Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]

    return x
#Metodo de choleky
def CholeskyLU(A):
    n = len(A)
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i+1):
            if i == j:
                L[i][i] = np.sqrt(A[i][i] - sum(L[i][k] ** 2 for k in range(i)))
            else:
                L[i][j] = (A[i][j] - sum(L[i][k] * L[j][k] for k in range(j))) / L[j][j]
    U = L.copy()

    return L, U.transpose()
    # Ejemplo de uso
A = np.array([[4, 6, 8],
              [6, 25, 24],
              [8, 24, 77]], dtype=float)
b = np.array([18, 78, 213], dtype=float)

L, U = CholeskyLU(A)

print("Matriz L:")
print(L)
print("Matriz U:")
print(U)
print("Matriz b:")
print(b)

x = SolucionLU(L, U, b)

print("Solución del sistema de ecuaciones:")
print(x)