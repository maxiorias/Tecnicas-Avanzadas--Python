import time
import random

# Genera datos de prueba
arr = [random.randint(1, 1000000) for _ in range(5000)]

#busqueda por inserccion

def busqueda_insercion(arr, x):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key

start_time = time.time()

# Ordenamiento por inserción

busqueda_insercion(arr, arr[0])

end_time = time.time()

execution_time = end_time - start_time

print("Tiempo de ejecución: ", execution_time, "segundos")

