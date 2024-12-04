from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd


#El método de Gauss convierte el sistema Ax=b 
#  un sistema triangular superior mediante operaciones elementales en filas.
def Gauss(A, b):

    n = len(b)
    Ab = np.column_stack((A, b))
    for i in range(n):
        p = Ab[i, i]
        for j in range(i + 1, n):
            f = Ab[j, i]/p
            Ab[j, :] -= f * Ab[i, :]
    print(Ab)
    s = [0] * n
    for i in range(n - 1, -1, -1):
        Ab[i,:] /= Ab[i,i]
        s[i] = Ab[i, -1]
        for j in range(i + 1, n):
            s[i] -= Ab[i, j] * s[j]
        print("resultado de s", s)
    return s
A = np.array([[1, 1, 1],
              [2, -1, 1],
              [1, 2, -1]],dtype=float)
b = np.array([6, 3, 1],dtype=float)
A[:, 0]
Gauss(A, b)
