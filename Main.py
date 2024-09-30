from Funciones import FunctionCalculator
from Graficacion import plot
from Calculos import parse_lim

def main():
    """
    Programa principal que permite interactuar con un objeto orientado a funciones matemáticas. 
    Ofrece opciones para derivar e integrar simbólica y numéricamente, así como graficar 
    funciones de hasta dos variables en 2D o 3D.

    Funcionalidades:
        1. Calcular derivada simbólica: Permite derivar simbólicamente con respecto a cualquier variable.
        2. Calcular integral simbólica: Permite integrar simbólicamente con respecto a cualquier variable.
        3. Calcular derivada numérica: Calcula la derivada numérica en un punto específico.
        4. Calcular integral numérica: Calcula la integral numérica en un rango especificado.
        5. Graficar función: Permite graficar la función en 2D (para una variable) o 3D (para dos variables).
        6. Salir: Finaliza el programa.

    Uso:
        El usuario ingresa una expresión de función, luego puede elegir qué operación realizar sobre esa función.
        Dependiendo de la opción seleccionada, el programa realizará derivadas, integrales o generará gráficos.

    Entradas:
        - Expresión matemática de la función en formato string.
        - Variables de la función, separadas por comas.
        - Opciones del menú interactivo para derivadas, integrales y gráficos.
        - Para las derivadas e integrales numéricas, se solicita un punto o un rango de integración.
    
    Salidas:
        - Derivadas e integrales simbólicas en formato string.
        - Derivadas e integrales numéricas como valores numéricos.
        - Gráficos de la función en 2D o 3D.
    """

    # Ingresar la expresión de la función
    expresion = input("Introduce la expresión de la función (por ejemplo, 'x**2 + y**2 + z**2'): ")
    
    # Ingresar las variables
    variables = input("Introduce las variables (separadas por comas, por ejemplo, 'x,y,z'): ").split(',')
    
    # Crear un objeto de FunctionCalculator para manejar la función ingresada
    calc = FunctionCalculator(expresion, variables)
    
    while True:
        # Menú de opciones
        print("\nOpciones:")
        print("1. Calcular derivada simbólica")
        print("2. Calcular integral simbólica")
        print("3. Calcular derivada numérica")
        print("4. Calcular integral numérica")
        print("5. Graficar función - Solo es posible hasta dos variables")
        print("6. Salir")
        
        choice = input("Elige una opción (1-6): ")
        
        # Derivada simbólica
        if choice == '1':
            var = input(f"Introduce la variable para derivar ({', '.join(variables)}): ")
            print(f"Derivada respecto a {var}:", calc.derivada(var))

        # Integral simbólica
        elif choice == '2':
            var = input(f"Introduce la variable para integrar ({', '.join(variables)}): ")
            print(f"Integral respecto a {var}:", calc.integral(var))

        # Derivada numérica
        elif choice == '3':
            def func(*args):
                return eval(expresion, dict(zip(variables, args)))
            try:
                # Ingresar el punto donde se quiere calcular la derivada numérica
                punto = tuple(map(float, input(f"Introduce el punto para derivada ({', '.join(variables)}), separados por comas: ").split(',')))
                if len(punto) != len(variables):
                    print(f"El número de puntos debe ser igual al número de variables ({len(variables)}).")
                    continue
                var = input(f"Introduce la variable para derivar ({', '.join(variables)}): ")
                print(f"Derivada numérica respecto a {var} en {punto}:", calc.derivadaNum(func, var, punto))
            except ValueError as e:
                print(f"Error al convertir los puntos a flotantes: {e}")

        # Integral numérica
        elif choice == '4':
            def func(*args):
                return eval(expresion, dict(zip(variables, args)))
            # Ingresar los límites de integración
            lim_str = input(f"Introduce los límites de integración (separados por punto y coma, por ejemplo, '0,1;0,1;0,1'): ")
            lim = parse_lim(lim_str)
            print("Integral numérica:", calc.integralNum(func, lim))

        # Graficar función
        elif choice == '5':
            def func(*args):
                return eval(expresion, dict(zip(variables, args)))
            # Ingresar los límites de la gráfica
            lim_str = input(f"Introduce los límites de la gráfica (separados por punto y coma, por ejemplo, '0,1;0,1;0,1'): ")
            lim = parse_lim(lim_str)
            plot(func, variables, lim, expresion)

        # Salir del programa
        elif choice == '6':
            break
        
        # Opción no válida
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
