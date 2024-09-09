# Función para convertir la entrada de texto en una lista de límites numéricos
def parse_lim(lim_str):
    limits = [tuple(map(float, b.split(','))) for b in lim_str.split(';')]
    if len(limits) == 1:
        return limits[0]
    elif len(limits) == 2:
        return limits[0], limits[1]
    elif len(limits) == 3:
        return limits[0], limits[1], limits[2]
    else:
        raise ValueError("Número de límites no válido")