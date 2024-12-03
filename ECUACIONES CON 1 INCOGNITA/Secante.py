import math
import pandas as pd

f = lambda x: math.log(x) if x > 0 else float('nan')
f1 = lambda x: 1 / x if x != 0 else float('nan')

def Secante(funcion, x0, error=1e-6):
    x1 = x0 + 0.001  # Asegurarse de que x1 no sea igual a x0
    i = 1
    try:
        x2 = x0 - funcion(x0) * (x1 - x0) / (funcion(x1) - funcion(x0))
    except ValueError as e:
        print(f"Error en la iteración {i}: {e}")
        print(f"x0 = {x0}, x1 = {x1}, funcion(x0) = {funcion(x0)}, funcion(x1) = {funcion(x1)}")
        return None

    print("iteracion", i, ": x0 =", x0, "f(x0) =", funcion(x0))
    while abs(funcion(x0)) > error:
        i += 1
        x0 = x1
        x1 = x2
        try:
            x2 = x0 - funcion(x0) * (x1 - x0) / (funcion(x1) - funcion(x0))
        except ValueError as e:
            print(f"Error en la iteración {i}: {e}")
            print(f"x0 = {x0}, x1 = {x1}, funcion(x0) = {funcion(x0)}, funcion(x1) = {funcion(x1)}")
            return None
        print("iteracion", i, ": x0 =", x0, "f(x0) =", funcion(x0))
    return x0

resultado = Secante(f, 149)
print("Resultado de Secante para f:", resultado)