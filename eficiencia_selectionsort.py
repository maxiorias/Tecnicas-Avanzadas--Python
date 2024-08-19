import time
import random

# Genera datos de prueba
arr = [random.randint(1, 1000000) for _ in range(5000)]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

start_time = time.time()

# Ordenamiento por selección    

selection_sort(arr)

end_time = time.time()

print(f"Tiempo de ejecución: {end_time - start_time} segundos")


