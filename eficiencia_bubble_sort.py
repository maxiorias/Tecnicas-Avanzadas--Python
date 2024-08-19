import time
import random

# Genera datos de prueba
arr = [random.randint(1, 1000000) for _ in range(5000)]

def ordenamiento_burbuja(arr):
    n = len(arr)
    for i in range(n - 1):  
        for j in range(n - 1): 
            if arr[j] > arr[j + 1]: 
                aux = arr[j] 
                arr[j] = arr[j + 1]
                arr[j + 1] = aux

# Medición de tiempo para ordenamiento burbuja
start_time = time.time()
ordenamiento_burbuja(arr.copy())
print("Tiempo de ejecución burbuja: %s segundos" % (time.time() - start_time))
