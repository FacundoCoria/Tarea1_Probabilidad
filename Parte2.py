import random

def generadorCumples(personas):
    cumples = [random.randint(1, 365) for _ in range(personas)]
    
    if len(cumples) != len(set(cumples)):
        return True
    else:
        return False

def ejecutarDef(personas, simulaciones):
    victorias = 0
    derrotas = 0
    
    for _ in range(simulaciones):
        if generadorCumples(personas):
            victorias += 1
        else:
            derrotas += 1
    
    return victorias, derrotas

gruposPersonas = [10, 20, 30, 40, 50]
cantidadSimulaciones = [1000, 10000, 100000]
resultados = {}

for personas in gruposPersonas:
    for simulaciones in cantidadSimulaciones:
        victorias, derrotas = ejecutarDef(personas, simulaciones)
        probabilidadEmpirica = victorias / simulaciones
        resultados[(personas, simulaciones)] = (victorias, derrotas, probabilidadEmpirica)

for (personas, simulaciones), (victorias, derrotas, probabilidadEmpirica) in resultados.items():
    print(f"Personas = {personas}, Simulaciones = {simulaciones}")
    print(f"Victorias: {victorias}, Derrotas: {derrotas}")
    print(f"Probabilidad empírica de victoria: {probabilidadEmpirica*100:.4f}%")
    print("-" * 40)
