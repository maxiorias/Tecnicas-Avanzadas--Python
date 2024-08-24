def ordenamiento_insercion(lista):
    for i in range(len(lista)):
        actual = lista[i]
        indice = i
        
        while indice > 0 and lista[indice - 1] > actual:
            lista[indice] = lista[indice - 1]
            indice -= 1
        
        lista[indice] = actual
    return lista

lista = [7, 3, 5, 4, 6, 32, 1]
print(ordenamiento_insercion(lista))


