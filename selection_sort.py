def ordenamiento_seleccion(lista):
    for i in range(len(lista)):
        min = i
        for j in range(i + 1, len(lista)):
            if lista[min] > lista[j]:
                min = j
        aux = lista[i]
        lista[i] = lista[min]
        lista[min] = aux
    return lista

# Ejemplo de uso
lista = [2, 6, 4, 7, 1, 9, 0]
print(ordenamiento_seleccion(lista))