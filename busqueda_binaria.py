# Lista desordenada
lista = [1, 6, 78, 23, 76, 0, 4]
n = len(lista)
# Ordenamiento de burbuja
for i in range(n - 1):  
    for j in range(n - 1): 
        if lista[j] > lista[j + 1]: 
            aux = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux

print("Lista ordenada:", lista)  

def busqueda_binaria(lista, x):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        
        if lista[medio] == x:
            return medio  
        elif lista[medio] < x:  
            inicio = medio + 1  
        else:
            fin = medio - 1  

    return -1                

objetivo = 23
resultado = busqueda_binaria(lista, objetivo)
if resultado != -1:
    print(f"El elemento {objetivo} se encuentra en la posición {resultado}")
else:
    print("El elemento no se encuentra en la lista")