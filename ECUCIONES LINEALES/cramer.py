from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd

import numpy as np

def cramer(A, b):
  n = len(b)
  det_A = np.linalg.det(A)
  if det_A == 0:
    print("El sistema no tiene solución única.")
    return None
  x = np.zeros(n)
  for i in range(n):
    A_i = A.copy()
    A_i[:, i] = b
    det_A_i = np.linalg.det(A_i)
    x[i] = det_A_i / det_A
  return x
A = np.array([[1, 1, 1],
              [2, -1, 1],
              [1, 2, -1]])
b = np.array([6, 3, 1])
cramer(A, b)

resultado = cramer(A, b)
print("Resultado:", resultado)