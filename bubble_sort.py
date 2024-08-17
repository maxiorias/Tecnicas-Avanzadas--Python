lista = [8, 7, 1, 9, 0]  
n = len(lista)  
print(lista)

for i in range(n - 1):  
    for j in range(n - 1 ): 
        if lista[j] > lista[j + 1]: 
            aux = lista[j] 
            lista[j] = lista[j + 1]
            lista[j + 1] = aux

print(lista)  

#funcion intercambiar
