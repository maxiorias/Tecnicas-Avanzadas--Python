# a diferencia de las listas las tuplas no se pueden modificar

tupla = (11, "python", False, [1, 2, 3], False) # en la lista son corchetes, en las tuplas parentesis

print(tupla[1]) # imprime "python"

print(tupla[1][2]) #imprime la letra t de python

print(tupla.index(11)) #seria la posicion 0

print(tupla[3][2]) #me mostraria el elemento 2 que seria el numero 3, accede al tercer valor de la tupla y la recorre

print(tupla[1:]) # si pones el indice y : te muestra lo que sigue del contenido despues del indice

#tupla[1] = "java" # esto daría un error, las tuplas no se pueden modificar

print(tupla.count(False)) #me indica cuantas veces se encuentra el valor False dentro de la tupla que seria 2
print(tupla.count(4)) # 0 veces