import time
import random

# Genera una lista de prueba
def generar_lista():
    return [random.randint(1, 1000000) for _ in range(6000)]

def ordenamiento_burbuja(arr):
    n = len(arr)
    for i in range(n - 1):  
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]: 
                aux = arr[j] 
                arr[j] = arr[j + 1]
                arr[j + 1] = aux

def ordenamiento_seleccion(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def ordenamiento_insercion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Medición de tiempo para cada algoritmo

# Ordenamiento de burbuja
arr = generar_lista()
start_time = time.time()
ordenamiento_burbuja(arr)
print("Tiempo de ejecución burbuja: %s segundos" % (time.time() - start_time))

# Ordenamiento por selección
arr = generar_lista()
start_time = time.time()
ordenamiento_seleccion(arr)
print("Tiempo de ejecución selección: %s segundos" % (time.time() - start_time))

# Ordenamiento por inserción
arr = generar_lista()
start_time = time.time()
ordenamiento_insercion(arr)
print("Tiempo de ejecución inserción: %s segundos" % (time.time() - start_time))
