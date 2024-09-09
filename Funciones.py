import sympy as sp
import numpy as np
from scipy.integrate import quad, dblquad, tplquad

class FunctionCalculator:
    """
    Clase para calcular derivadas e integrales tanto simbólicas como numéricas de una función dada.
    
    Atributos:
        expresion (str): Expresión matemática en forma de cadena.
        variables (list): Lista de variables utilizadas en la expresión.
        sym_expr (sp.Basic): Expresión simbólica de la función.
        sym_vars (list): Lista de variables simbólicas.
    """
    
    def __init__(self, expresion, variables):
        """
        Inicializa una instancia de FunctionCalculator.
        
        Args:
            expresion (str): Expresión matemática en forma de cadena.
            variables (list): Lista de variables utilizadas en la expresión.
        """
        self.expresion = expresion
        self.variables = variables
        self.sym_expr = sp.sympify(expresion)
        self.sym_vars = sp.symbols(variables)
        
    def derivada(self, var):
        """
        Calcula la derivada simbólica de la expresión con respecto a una variable dada.
        
        Args:
            var (str): Variable con respecto a la cual calcular la derivada.
        
        Returns:
            sp.Basic: Derivada simbólica de la expresión.
        
        Raises:
            ValueError: Si la variable no está incluida en las variables.
        """
        if var in self.variables:
            return sp.diff(self.sym_expr, var)
        else:
            raise ValueError(f"Variable '{var}' no está incluida en las variables")
    
    def integral(self, var):
        """
        Calcula la integral simbólica de la expresión con respecto a una variable dada.
        
        Args:
            var (str): Variable con respecto a la cual calcular la integral.
        
        Returns:
            sp.Basic: Integral simbólica de la expresión.
        
        Raises:
            ValueError: Si la variable no está incluida en las variables.
        """
        if var in self.variables:
            var_symbol = sp.Symbol(var)
            return sp.integrate(self.sym_expr, var_symbol)
        else:
            raise ValueError(f"Variable '{var}' no está incluida en las variables")
    
    def derivadaNum(self, func, var, punto, h=1e-5):
        """
        Calcula la derivada numérica de una función en un punto dado con respecto a una variable dada.
        
        Args:
            func (callable): Función cuya derivada se calculará.
            var (str): Variable con respecto a la cual calcular la derivada.
            punto (list): Coordenadas del punto en el que se calculará la derivada.
            h (float): Tamaño del paso para el cálculo numérico (por defecto es 1e-5).
        
        Returns:
            float: Derivada numérica de la función en el punto dado.
        
        Raises:
            ValueError: Si la variable no está incluida en las variables.
        """
        if var in self.variables:
            idx = self.variables.index(var)
            punto = list(punto)
            f = lambda *args: func(*args)
            x0 = punto[idx]
            punto[idx] = x0 + h
            return (f(*punto) - f(*(punto[:idx] + [x0] + punto[idx+1:]))) / h
        else:
            raise ValueError(f"Variable '{var}' no está incluida en las variables")
    
    def integralNum(self, func, lim):
        """
        Calcula la integral numérica de una función dada en un intervalo o dominio dado, dependiendo del número de variables.
        
        Args:
            func (callable): Función que se integrará.
            lim (tuple): Limites de integración. Para 1D, es una tupla de dos elementos; para 2D, es una tupla de dos tuplas; 
                         para 3D, es una tupla de tres tuplas.
        
        Returns:
            float: Integral numérica de la función en el dominio dado.
        
        Raises:
            ValueError: Si el número de variables no está entre 1 y 3.
        """
        
        def func_1d(x): # Funciones para diferentes dimensiones
            return func(x)

        def func_2d(x, y):
            return func(x, y)

        def func_3d(x, y, z):
            return func(x, y, z)
        
        if len(self.variables) == 1: # Selección según la cantidad de variables
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
            raise ValueError("La integral numérica solo está implementada para 3 variables")
