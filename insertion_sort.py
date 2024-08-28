def ordenamiento_insercion(lista):
    for i in range(len(lista)):          # n
        actual = lista[i]                # 1
        indice = i                       # 1
        
        while indice > 0 and lista[indice - 1] > actual:  # n
            lista[indice] = lista[indice - 1]             # n
            indice -= 1                                   # n
        
        lista[indice] = actual                            # 1
    return lista

lista = [7, 3, 5, 4, 6, 32, 1]
print(ordenamiento_insercion(lista))


