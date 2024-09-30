import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot(func, variables, lim, expresion=None, num_punto=100):
    """
    Genera gráficos 2D o 3D para funciones de una o dos variables.

    Dependiendo del número de variables, la función generará:
    - Un gráfico 2D (línea) si la función tiene una variable.
    - Un gráfico 3D (superficie) si la función tiene dos variables.

    Args:
        func (callable): La función a graficar. Debe aceptar uno o dos argumentos (según el número de variables).
        variables (list of str): Lista con los nombres de las variables. Ejemplo: ['x'] o ['x', 'y'].
        lim (tuple or list of tuples): Los límites de los ejes. 
            - Para 1 variable: Una tupla con 2 elementos (límite inferior y superior).
            - Para 2 variables: Una lista de dos tuplas, cada una con 2 elementos, que representan los límites de cada variable.
        expresion (str, opcional): Expresión simbólica de la función, usada para el título del gráfico. Por defecto es None.
        num_punto (int, opcional): Número de puntos a calcular en cada eje para la graficación. Por defecto es 100.
    
    Raises:
        ValueError: Si el número de variables no es 1 o 2, o si los límites (`lim`) no tienen el formato adecuado.

    Ejemplos:
        >>> def f1(x): return np.sin(x)
        >>> plot(f1, ['x'], (0, 2*np.pi), expresion='sin(x)')

        >>> def f2(x, y): return np.sin(np.sqrt(x**2 + y**2))
        >>> plot(f2, ['x', 'y'], [(0, 5), (0, 5)], expresion='sin(sqrt(x^2 + y^2))')

    """
    
    if len(variables) == 1:  # Caso de una variable: gráfico 2D
        if len(lim) != 2:
            raise ValueError("Para una variable, lim debe ser una tupla con 2 elementos.")
        
        # Generamos los puntos en el eje x y calculamos los valores de y
        x = np.linspace(lim[0], lim[1], num_punto)
        y = np.array([func(xi) for xi in x])

        # Graficar en 2D
        plt.plot(x, y)
        plt.xlabel(variables[0])
        plt.ylabel(f"f({variables[0]})")
        plt.title(f"Gráfico para una variable: f({variables[0]}) = {expresion}")
        plt.grid(True)
        plt.show()

    elif len(variables) == 2:  # Caso de dos variables: gráfico 3D
        if len(lim) != 2 or len(lim[0]) != 2 or len(lim[1]) != 2:
            raise ValueError("Para dos variables, lim debe ser una lista de dos tuplas, cada una con 2 elementos.")
        
        # Generamos los puntos en los ejes x e y
        x = np.linspace(lim[0][0], lim[0][1], num_punto)
        y = np.linspace(lim[1][0], lim[1][1], num_punto)
        X, Y = np.meshgrid(x, y)  # Crear una malla 2D
        Z = np.array([[func(xi, yi) for xi in x] for yi in y])  # Calcular los valores de Z para cada par (x, y)

        # Crear la figura y el eje 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.plot_surface(X, Y, Z, cmap="viridis")  # Graficar la superficie en 3D

        # Etiquetas y título del gráfico
        ax.set_xlabel(variables[0])
        ax.set_ylabel(variables[1])
        ax.set_zlabel(f"f({variables[0]}, {variables[1]})")
        ax.set_title(f'Gráfico de dos variables: f({variables[0]}, {variables[1]}) = {expresion}')
        plt.grid(True)
        plt.show()

    else:
        raise ValueError("Solo está implementado hasta 2 variables en las gráficas.")
