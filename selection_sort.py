def ordenamiento_seleccion(lista):
    for i in range(len(lista)):                    # n
        min = i                                    # 1
        for j in range(i + 1, len(lista)):       # (n-1) + (n-2) + ... + 1 = (n*(n-1))/2
            if lista[min] > lista[j]:              # 1
                min = j                            # 1
        aux = lista[i]                            # 1
        lista[i] = lista[min]                      # 1
        lista[min] = aux                          # 1
    return lista

lista = [2, 6, 4, 7, 1, 9, 0]
print(ordenamiento_seleccion(lista))