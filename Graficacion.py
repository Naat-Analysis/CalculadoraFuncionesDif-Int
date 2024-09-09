import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot(func, variables, lim, expresion=None, num_punto=100):
    if len(variables) == 1:
        if len(lim) != 2:
            raise ValueError("Para una variable, lim debe ser una tupla con 2 elementos.")
        
        x = np.linspace(lim[0], lim[1], num_punto) # Gráfico 2D
        y = np.array([func(xi) for xi in x])

        plt.plot(x, y) #Creamos la figura en 1D
        plt.xlabel(variables[0])
        plt.ylabel(f"f({variables[0]})")

        # plt.title(f"Gráfico para una variable variables en dos dimensiones: ")
        plt.title(f"Gráfico para una variable: f({variables[0]}) = {expresion}")
        plt.grid(True)
        plt.show()

    elif len(variables) == 2:
        if len(lim) != 2 or len(lim[0]) != 2 or len(lim[1]) != 2:
            raise ValueError("Para dos variables, lim debe ser una lista de dos tuplas, cada una con 2 elementos.")
        
        x = np.linspace(lim[0][0], lim[0][1], num_punto)
        y = np.linspace(lim[1][0], lim[1][1], num_punto)
        X, Y = np.meshgrid(x, y)
        Z = np.array([[func(xi, yi) for xi in x] for yi in y])

        fig = plt.figure() # Crear la figura y el eje 3D
        ax = fig.add_subplot(111, projection="3d")
        ax.plot_surface(X, Y, Z, cmap="viridis") # Graficar la superficie
    
        ax.set_xlabel(variables[0])  # Agregar etiquetas y título
        ax.set_ylabel(variables[1])
        ax.set_zlabel(f"f({variables[0], variables[1]})")

        # ax.set_title('Gráfico de dos variables en 3 dimensiones')
        ax.set_title(f'Gráfico de dos variables: f({variables[0]}, {variables[1]}) = {expresion}')
        plt.grid(True)
        plt.grid(True)
        plt.show()

    else:
        raise ValueError(f"Solo está implementado hasta 2 variables en las gráficas: ")
