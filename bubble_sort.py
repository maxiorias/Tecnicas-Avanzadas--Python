def ordenamiento_burbuja(lista):
    n = len(lista)                                 
    for i in range(n - 1):                         
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista

lista = [1, 6, 78, 23, 76, 0, 4]
print("Lista ordenada:", ordenamiento_burbuja(lista))
