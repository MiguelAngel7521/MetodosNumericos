from sympy import *
import math
init_printing( )
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, Math
from cmath import sqrt
import pandas as pd

#Broyden calcula la inversa del jacobiano solo la primera vez, y despues utiliza A-1 para recalcular, mientras que newton raphson la calcula en cada iteracion
# Lo mismo que en newton raphson
# No usar arrays de nunmpy
def Broyden(fx, X, x0, tol=1e-6, max_iter=100):
    J = fx.jacobian(X)
    v = list(zip(X, x0))
    display("v=", v)
    fx0 = fx.subs(v)
    Jx0 = J.subs(v)
    J_1x0 = Jx0.inv()
    x1 = x0 - (J_1x0 * fx0)
    v1 = list(zip(X, x1))
    fx1 = fx.subs(v1)
    Ax0_1 = J_1x0
    print("Iteracion 0")
    display("x0= ", x0, "f(x0)=", fx0, "J(x0)=", Jx0, "J-1(x0)=", J_1x0, "x1=", x1, "f(x1)=", fx1)
    for i in range(max_iter):
        Dx = x1 - x0
        Dfx = fx1 - fx0
        Ax1_1 = Ax0_1+(((Dx-Ax0_1*Dfx)*Dx.T*Ax0_1)/det(Dx.T*Ax0_1*Dfx))
        x2 = x1 - (Ax1_1 * fx1)
        v2 = list(zip(X, x2))
        fx2 = fx.subs(v2)
        print("Iteracion", i+1)
        display("x0=", x0, "x1=", x1, "Δx=", Dx, "f(x0)=", fx0, "f(x1)=", fx1, "Δf(x)", Dfx, "A(x0)-1=", Ax0_1, "A(x1)-1", Ax1_1, "x2=", x2, "f(x2)=", fx2)
        if all(abs(i) < tol for i in fx2):
            return x2
        x0 = x1
        x1 = x2
        fx0 = fx1
        fx1 = fx2
        Ax0_1 = Ax1_1

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
x0 = Matrix([1.0, 2.0])

# Resolución del sistema
solucion = Broyden(fx, X, x0)
print("Solución:", solucion)