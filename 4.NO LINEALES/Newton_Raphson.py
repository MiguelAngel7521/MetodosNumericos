from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd

#newton raphson calcula la inversa del jacobiano en cada iteracion
# enviar vector de funciones, vector de variables y puntos iniciales
# No usar arrays de nunmpy
def Newton_Raphson(fx, X, x0, tol=1e-6, max_iter=100):
    J = fx.jacobian(X)
    for i in range(max_iter):
        fx0 = fx.subs({x:x0[0], y:x0[1]})
        Jx0 = J.subs({x:x0[0], y:x0[1]})
        J_1x0 = Jx0.inv()
        x1 = x0 - (J_1x0 * fx0)
        fx1 = fx.subs({x:x1[0], y:x1[1]})
        print("Iteracion", i)
        display("x0= ", x0, "f(x0)=", fx0, "J(x0)=", Jx0, "J-1(x0)=", J_1x0, "x1=", x1, "f(x1)=", fx1)
        if all(abs(i) < tol for i in fx1):
            return x1
        x0 = x1

# Ejemplo de uso

# definir las variables simbolicas usando symbols
x, y = symbols('x, y')
# definir el vector de las variables
X = [x, y]

# definir el vector del sistema de ecuaciones no lineales
# recordar que deben igualar todas las ecuaciones a 0 para copiar el otro miembro
# x**2-y**2=4  -->  x**2-y**2-4=0
# x*y=6       -->  x*y-6=0
fx = Matrix([x**2 - y**2 - 4, x*y - 6])

# Valor inicial aproximado (numeros cualquiera)
x0 = Matrix([2.0, 1.0])

# Resolución del sistema
solucion = Newton_Raphson(fx, X, x0)
print("Solución:", solucion)