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

#Metodo de Crout
# Enviar los coeficien en "A" y esta funcion te devolvera las matrices L y U
def CroutLU(A):
    n = len(A)

    # Inicializar matrices L y U
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1.0  # La diagonal principal de L tiene 1s
        print("Iteracion")
        print("Matriz L:")
        print(L)
        print("Matriz U:")
        print(U)
        # Factorización L
        for k in range(i, n):
            L[k][i] = A[k][i]
            for j in range(i):
                L[k][i] -= L[k][j] * U[j][i]

        # Factorización U
        for k in range(i, n):
            U[i][k] = A[i][k]
            for j in range(i):
                U[i][k] -= L[i][j] * U[j][k]
            U[i][k] /= L[i][i]

    return L, U

# Ejemplo de uso
A = np.array([[-3.715102, -0.737788, 1.72093, 5.548794],
              [-3.616011, -6.114161, 0.795442, -3.614025],
              [-0.394884, 0.343225, 4.895409, 9.863844],
              [-9.518878, 3.765614, -9.600773, -5.102836]], dtype=float)
b = np.array([-3.352827, -9.274186, -1.791818, -2.320388], dtype=float)

L, U = CroutLU(A)

print("Matriz L:")
print(L)
print("Matriz U:")
print(U)

x = SolucionLU(L, U, b)

print("Solución del sistema de ecuaciones:")
np.matmul(A, x)
