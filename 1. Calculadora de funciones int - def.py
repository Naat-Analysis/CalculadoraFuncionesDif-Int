'''Hacer en python un programa usando el paradigma orientado objeto donde tu puedas
colocar cualquier funcion de n variables y este objeto podrá derivar tanto simbolicada
y numericamente, integrar simbolicamente y numericamente, la opcion de graficar en 2 o 
en 3 dimensiones dependiendo de las variables que tengas.
'''

import sympy as sp #importamos las bibliotecas 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import quad, dblquad, tplquad #importamos para los limites de la integral


class FunctionCalculator:
    def __init__(self, expresion, variables):
        self.expresion = expresion
        self.variables = variables
        self.sym_expr = sp.sympify(expresion)
        self.sym_vars = sp.symbols(variables)
        
    def derivada(self, var):
        if var in self.variables:
            return sp.diff(self.sym_expr, var)
        else:
            raise ValueError(f"Variable '{var}' no está incluida en variables")
    
    def integral(self, var):
        if var in self.variables:
            return sp.integrate(self.sym_expr, var)
        else:
            raise ValueError(f"Variable '{var}' no está incluida en variables")
    
    def derivadaNum(self, func, var, punto, h=1e-5):
        if var in self.variables:
            idx = self.variables.index(var)
            punto = list(punto)
            f = lambda *args: func(*args)
            x0 = punto[idx]
            punto[idx] = x0 + h
            return (f(*punto) - f(*(punto[:idx] + [x0] + punto[idx+1:]))) / h
        else:
            raise ValueError(f"Variable '{var}' no está incluida en variables")
    
    def integralNum(self, func, lim): # Calcula la integral numérica de la función usando scipy.integrate.quad (1D), dblquad (2D) o tplquad (3D)
        def func_1d(x):
            return func(x) #Para una dim

        def func_2d(x, y):
            return func(x, y) #Para dos dim

        def func_3d(x, y, z):
            return func(x, y, z) #Para tres dim
        
        if len(self.variables) == 1:
            a, b = lim
            resultado, _ = quad(func_1d, a, b)
            return resultado
        elif len(self.variables) == 2:
            x_lim, y_lim = lim
            resultado, _ = dblquad(func_2d, x_lim[0], x_lim[1], lambda x: y_lim[0], lambda x: y_lim[1])
            return resultado
        elif len(self.variables) == 3:
            x_lim, y_lim, z_lim = lim
            resultado, _ = tplquad(func_3d, x_lim[0], x_lim[1], lambda x: y_lim[0], lambda x: y_lim[1], lambda x, y: z_lim[0], lambda x, y: z_lim[1])
            return resultado
        else:
            raise ValueError("Numerical integration is only implemented for up to 3 variables")
        return resultado
    