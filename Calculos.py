# Función para convertir la entrada de texto en una lista de límites numéricos
def parse_lim(lim_str):
    """
    Convierte una cadena de texto que contiene límites numéricos en una lista de tuplas de flotantes.
    
    La cadena de entrada debe tener el formato:
    - 'a,b' para un conjunto de límites (1D),
    - 'a,b;c,d' para dos conjuntos de límites (2D),
    - 'a,b;c,d;e,f' para tres conjuntos de límites (3D).
    
    Los límites están separados por punto y coma (;) y cada tupla de límites está separada por coma (,).
    
    Args:
        lim_str (str): Cadena que representa los límites en formato 'a,b;c,d' o similar.
        
    Returns:
        tuple: Retorna una tupla con uno, dos o tres elementos, dependiendo del número de límites.
               Cada elemento es una tupla de dos valores flotantes que representan el límite inferior
               y el límite superior.
               
               - Si es 1D: (a, b)
               - Si es 2D: ((a, b), (c, d))
               - Si es 3D: ((a, b), (c, d), (e, f))
    
    Raises:
        ValueError: Si el número de límites no es 1, 2 o 3.
    
    Ejemplos:
        >>> parse_lim('0,1')
        (0.0, 1.0)
        
        >>> parse_lim('0,1;2,3')
        ((0.0, 1.0), (2.0, 3.0))
        
        >>> parse_lim('0,1;2,3;4,5')
        ((0.0, 1.0), (2.0, 3.0), (4.0, 5.0))
    """
    
    # Convierte la cadena de entrada en una lista de tuplas de límites numéricos
    limits = [tuple(map(float, b.split(','))) for b in lim_str.split(';')]
    
    # Devuelve el resultado dependiendo del número de límites
    if len(limits) == 1:
        return limits[0]  # 1D
    elif len(limits) == 2:
        return limits[0], limits[1]  # 2D
    elif len(limits) == 3:
        return limits[0], limits[1], limits[2]  # 3D
    else:
        raise ValueError("Número de límites no válido")  # Excepción para números de límites fuera de lo esperado
