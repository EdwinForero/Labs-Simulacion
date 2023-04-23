import random

# Función que calcula la aptitud de una solución
def calcular_aptitud(solucion, objetivo):
    suma = sum(solucion)
    if suma > objetivo:
        return 0
    else:
        return suma

# Función que genera una solución aleatoria
def generar_solucion(tamano):
    solucion = []
    for i in range(tamano):
        solucion.append(random.randint(0, 100))
    return solucion

# Función que realiza la selección de soluciones
def seleccionar_padres(poblacion, objetivo):
    padres = []
    for i in range(2):
        seleccionados = random.sample(poblacion, 3)
        mejor_solucion = max(seleccionados, key=lambda x: calcular_aptitud(x, objetivo))
        padres.append(mejor_solucion)
    return padres

# Función que realiza el cruce de soluciones
def cruzar(padres):
    hijo = []
    for i in range(len(padres[0])):
        if random.random() > 0.5:
            hijo.append(padres[0][i])
        else:
            hijo.append(padres[1][i])
    return hijo

# Función que realiza la mutación de una solución
def mutar(solucion):
    for i in range(len(solucion)):
        if random.random() < 0.1:
            solucion[i] = random.randint(0, 100)
    return solucion

# Función principal del algoritmo genético
def algoritmo_genetico(tamano_poblacion, objetivo, num_generaciones):
    # Generar población inicial
    poblacion = [generar_solucion(10) for i in range(tamano_poblacion)]

    # Iterar por cada generación
    for generacion in range(num_generaciones):
        # Seleccionar padres
        padres = seleccionar_padres(poblacion, objetivo)

        # Realizar cruce
        hijo = cruzar(padres)

        # Realizar mutación
        hijo_mutado = mutar(hijo)

        # Reemplazar solución antigua por nueva en la población
        poblacion.remove(min(poblacion, key=lambda x: calcular_aptitud(x, objetivo)))
        poblacion.append(hijo_mutado)

    # Devolver la solución con la máxima aptitud
    return max(poblacion, key=lambda x: calcular_aptitud(x, objetivo))

# Ejecutar el algoritmo genético
solucion_optima = algoritmo_genetico(100, 500, 100)

# Imprimir la solución óptima encontrada
print("Solución óptima:", solucion_optima)
print("Suma:", sum(solucion_optima))
