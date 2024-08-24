def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i              # Devuelve la posición del elemento encontrado
    return -1                     # Si no se encuentra el elemento, devuelve -1


lista = [1, 2, 4, 5, 7, 8]
objetivo = 5
resultado = busqueda_lineal(lista, objetivo)
if resultado != -1:
    print(f"El elemento {objetivo} se encuentra en la posición {resultado}")
else:
    print("El elemento no se encuentra en la lista")
