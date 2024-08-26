import time
import random

# Genera una lista de prueba
def generar_lista():
    return [random.randint(1, 1000000) for _ in range(800000)]  # Aumenta el tamaño para mayor precisión

# Ordena la lista para la búsqueda binaria
def ordenar_lista(arr):
    arr.sort()

def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def busqueda_binaria(arr, x):
    inicio = 0
    fin = len(arr) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == x:
            return medio
        elif arr[medio] < x:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Genera la lista de prueba
arr = generar_lista()

# Ordena la lista para la búsqueda binaria
ordenar_lista(arr)

# Ejecuta la búsqueda lineal varias veces y mide el tiempo
x = random.choice(arr)  # Selecciona un valor que está en la lista
start_time = time.time()
for _ in range(1000):  # Ejecuta 1000 búsquedas lineales
    busqueda_lineal(arr, x)
print("Tiempo de ejecución búsqueda lineal: %s segundos" % (time.time() - start_time))

# Ejecuta la búsqueda binaria varias veces y mide el tiempo
start_time = time.time()
for _ in range(1000):  # Ejecuta 1000 búsquedas binarias
    busqueda_binaria(arr, x)
print("Tiempo de ejecución búsqueda binaria: %s segundos" % (time.time() - start_time))
