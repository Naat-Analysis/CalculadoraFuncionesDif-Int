'''Hacer en python un programa usando el paradigma orientado objeto donde tu puedas
colocar cualquier funcion de n variables y este objeto podrá derivar tanto simbolicada
y numericamente, integrar simbolicamente y numericamente, la opcion de graficar en 2 o 
en 3 dimensiones dependiendo de las variables que tengas.
'''
from Funciones import FunctionCalculator
from Graficacion import plot
from Calculos import parse_lim

def main():
    # Ingresar la función
    expresion = input("Introduce la expresión de la función (por ejemplo, 'x**2 + y**2 + z**2'): ")
    
    # Ingresar las variables
    variables = input("Introduce las variables (separadas por comas, por ejemplo, 'x,y,z'): ").split(',')
    
    calc = FunctionCalculator(expresion, variables)
    
    while True:
        print("\nOpciones:")
        print("1. Calcular derivada simbólica")
        print("2. Calcular integral simbólica")
        print("3. Calcular derivada numérica")
        print("4. Calcular integral numérica")
        print("5. Graficar función - Solo es posible hasta dos variables")
        print("6. Salir")
        
        choice = input("Elige una opción (1-6): ")
        
        if choice == '1':
            var = input(f"Introduce la variable para derivar ({', '.join(variables)}): ")
            print(f"Derivada respecto a {var}:", calc.derivada(var))

        elif choice == '2':
            var = input(f"Introduce la variable para integrar ({', '.join(variables)}): ")
            print(f"Integral respecto a {var}:", calc.integral(var))

        elif choice == '3':
            def func(*args):
                return eval(expresion, dict(zip(variables, args)))
            try:
                punto = tuple(map(float, input(f"Introduce el punto para derivada ({', '.join(variables)}), separados por comas: ").split(',')))
                if len(punto) != len(variables):
                    print(f"el numero de puntos debe ser igual al numero de variables({len(variables)})")
                    continue
                var = input(f"Introduce la variable para derivar ({', '.join(variables)}): ")
                print(f"Derivada numérica respecto a {var} en {punto}:", calc.derivadaNum(func, var, punto))
            except ValueError as e:
                print(f"Error al convertir los puntos a flotantes: {e}")

        elif choice == '4':
            def func(*args):
                return eval(expresion, dict(zip(variables, args)))
            lim_str = input(f"Introduce los límites de integración (separados por punto y coma, por ejemplo, '0,1;0,1;0,1'): ")
            lim = parse_lim(lim_str)
            print("Integral numérica:", calc.integralNum(func, lim))

        elif choice == '5':
            def func(*args):
                return eval(expresion, dict(zip(variables, args)))
            lim_str = input(f"Introduce los límites de la gráfica (separados por punto y coma, por ejemplo, '0,1;0,1;0,1'): ")
            lim = parse_lim(lim_str)
            plot(func,variables, lim, expresion)

        elif choice == '6':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()