from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd

# Utilizar luego de conseguir las matrices L y U con otro metodo

#Descomposición LU El objetivo es descomponer la matriz 𝐴 A en el producto de dos matrices: 𝐴 = 𝐿 𝑈, donde 𝐿 es una matriz triangular inferior y 𝑈 es una matriz triangular superior.
#  Se usa para resolver sistemas de ecuaciones de manera más eficiente.
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

#Metodo 

# Los elementos de la diagonal principal de L son 1.los Elementos de la diagonal principal de U pueden ser cualquier numero
def DoolittleLU(A):
    n = len(A)

    # Inicializar matrices L y U
    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n):
        # Factorización U
        print("Iteracion", i)
        print("Matriz L:")
        print(L)
        print("Matriz U:")
        print(U)
        for k in range(i, n):
            U[i][k] = A[i][k]
            for j in range(i):
                U[i][k] -= L[i][j] * U[j][k]

        # Factorización L
        for k in range(i+1, n):
            L[k][i] = A[k][i]
            for j in range(i):
                L[k][i] -= L[k][j] * U[j][i]
            L[k][i] /= U[i][i]

    return L, U

# Ejemplo de uso
A = np.array([[6, -2, 2, 4],
              [12, -8, 6, 10],
              [3, -13, 9, 3],
              [-6, 4, 1, -18]], dtype=float)
b = np.array([12, 34, 27, -38], dtype=float)

L, U = DoolittleLU(A)

print("Matriz L:")
print(L)
print("Matriz U:")
print(U)

x = SolucionLU(L, U, b)

print("Solución del sistema de ecuaciones:")
print(x)
