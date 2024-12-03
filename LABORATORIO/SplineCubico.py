import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if archivo:
        try:
            # Leer archivo CSV
            datos = pd.read_csv(archivo, header=None)
            X = np.array(datos[0])  
            Y = np.array(datos[1])  
            return X, Y
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer el archivo: {e}")
            return None, None
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")
        return None, None

def solicitar_valor_rpm(X):
    while True:
        try:
            # Mostrar un cuadro de entrada para soliciatr el valor de RPM
            p = simpledialog.askfloat(
                "Ingrese RPM", 
                f"Ingrese un valor de RPM dentro del rango [{X[0]} - {X[-1]}]:"
            )
            if p is None:
                raise ValueError("El usuario cancelo la entrada.")
            if X[0] <= p <= X[-1]:
                return p
            else:
                messagebox.showwarning("Error", "El valor ingresado esta fuera del rango. Intente de nuevo.")
        except ValueError:
            messagebox.showerror("Error", "Entrada no valida. Por favor ingrese un numero dentro del rango.")

def construir_matriz_sistema(X, Y):
    #Construye el sistema de ecuaciones para el spline cúbico
    n = len(X)
    num_ecuaciones = (n - 1) * 4
    A = np.zeros((num_ecuaciones, num_ecuaciones))
    b = np.zeros(num_ecuaciones)    

    ecuacion = 0

    # Criterio 1: Interpolación en los extremos de cada intervalo
    # Esto asegura que el spline pasa por los puntos dados (X[i], Y[i]) y (X[i+1], Y[i+1]).
    for i in range(n - 1): # Para cada intervalo [X[i], X[i+1]]
        x0, x1 = X[i], X[i + 1] # Extremos del intervalo actual

        # Ecuación para garantizar que el spline en x0 es igual a Y[i]
        # fi(x0) = ai * x0^3 + bi * x0^2 + ci * x0 + di = Y[i]
        A[ecuacion, i * 4:(i + 1) * 4] = [x0 ** 3, x0 ** 2, x0, 1]
        b[ecuacion] = Y[i] # Igualamos al valor Y[i] en el extremo izquierdo
        ecuacion += 1
        
        # Ecuación para garantizar que el spline en x1 es igual a Y[i+1]
        # fi(x1) = ai * x1^3 + bi * x1^2 + ci * x1 + di = Y[i+1]
        A[ecuacion, i * 4:(i + 1) * 4] = [x1 ** 3, x1 ** 2, x1, 1]
        b[ecuacion] = Y[i + 1]
        ecuacion += 1

    # Criterio 2: Continuidad de la primera derivada
    # Esto garantiza que las derivadas primeras de los polinomios de intervalos consecutivos son iguales.   
    for i in range(1, n - 1):
        x = X[i]# Punto de unión entre dos intervalos
        
        # Derivada de fi(x): 3 * ai * x^2 + 2 * bi * x + ci
        # Derivada de f(i-1)(x): 3 * a(i-1) * x^2 + 2 * b(i-1) * x + c(i-1)
        A[ecuacion, (i - 1) * 4:(i + 1) * 4] = [
            3 * x ** 2, 2 * x, 1, 0, -3 * x ** 2, -2 * x, -1, 0
        ]
        ecuacion += 1

    # Criterio 3: Continuidad de la segunda derivada
    # Esto garantiza que las derivadas segundas de los polinomios de intervalos consecutivos son iguales.
    for i in range(1, n - 1):
        x = X[i]
        
        # Segunda derivada de fi(x): 6 * ai * x + 2 * bi
        # Segunda derivada de f(i-1)(x): 6 * a(i-1) * x + 2 * b(i-1)
        # Igualamos las derivadas segundas en x
        A[ecuacion, (i - 1) * 4:(i + 1) * 4] = [
            6 * x, 2, 0, 0, -6 * x, -2, 0, 0
        ]
        ecuacion += 1

    # Criterio 4: Condiciones naturales en los extremos
    # Esto establece que la segunda derivada en los extremos del spline sea 0 (condiciones naturales).
    # En el extremo izquierdo (x = X[0])
    # Segunda derivada: 6 * a0 * X[0] + 2 * b0 = 0
    A[ecuacion, 0:2] = [6 * X[0], 2]
    ecuacion += 1
    A[ecuacion, -4:-2] = [6 * X[-1], 2]

    return A, b

def resolver_sistema(A, b):
    # Usamos numpy para encontrar la solución del sistema.
    return np.linalg.solve(A, b)

def evaluar_spline(X, coeficientes, p):
    # Itera sobre cada intervalo [X[i], X[i+1]] para encontrar el que contiene p
    for i in range(len(X) - 1):
        if X[i] <= p <= X[i + 1]:   # Si el punto p está en el intervalo actual
            c = coeficientes[i * 4:(i + 1) * 4] # Coeficientes del polinomio cúbico correspondiente
            # Evalúa el polinomio cúbico en el punto p
            return c[0] * p ** 3 + c[1] * p ** 2 + c[2] * p + c[3]
    raise ValueError("El valor p está fuera del rango de X.")

def graficar_spline(X, Y, coeficientes, p=None, valor_p=None):
    # Genera puntos finos en el rango de X para crear una curva suave
    X_fino = np.linspace(X[0], X[-1], 1000)  # Puntos finos entre X[0] y X[-1]
    Y_fino = np.zeros_like(X_fino)

    # Calcula el valor del spline en cada punto de X_fino
    for i, x in enumerate(X_fino):
        Y_fino[i] = evaluar_spline(X, coeficientes, x)

    # Configura la figura de la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(X_fino, Y_fino, label="Spline cúbico", color="blue")
    plt.scatter(X, Y, color="red", label="Puntos originales")

    # Si se proporciona un punto p y su valor estimado, lo grafica
    if p is not None and valor_p is not None:
        plt.scatter(p, valor_p, color="green", label=f"Punto evaluado {p:.2f} RPM: {valor_p:.2f} km/h.", zorder=5)

     # Personalizacion de la gráfica
    plt.title("Interpolación con Spline Cúbico")
    plt.xlabel("RPM")
    plt.ylabel("Velocidad (km/h)")
    plt.legend()
    plt.grid()
    plt.show()

def iniciar_Programa():
    ventana = tk.Tk() # Crea una ventana principal de la libreria Tkinter
    ventana.title("Spline Cúbico")
    ventana.geometry("400x200")

    def ejecutar_spline():
        # Carga datos desde un archivo CSV seleccionado por el usuario
        X, Y = seleccionar_archivo()
        if X is None or Y is None:
            return

        
        # Construye el sistema de ecuaciones del spline cúbico
        A, b = construir_matriz_sistema(X, Y)
        coeficientes = resolver_sistema(A, b)
        p = solicitar_valor_rpm(X)
        valor_p = evaluar_spline(X, coeficientes, p)

        messagebox.showinfo("Resultado", f"Velocidad estimada para {p:.2f} RPM: {valor_p:.2f} km/h.")
        graficar_spline(X, Y, coeficientes, p, valor_p)

    tk.Label(ventana, text="Simulador de Ford Mustang 2000", font=("Arial", 14)).pack(pady=10)
    tk.Button(ventana, text="Seleccionar Archivo CSV", command=ejecutar_spline).pack(pady=20)

    ventana.mainloop()

iniciar_Programa()