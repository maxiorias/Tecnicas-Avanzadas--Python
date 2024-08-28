conjunto = set() #quiere decir q vamos a crear un conjunto

conjunto = {2, "python", 2, "maxi", True}

print(conjunto)

#en los conjuntos no se peuede repetir los valores 

conjunto.add("java")

print(conjunto)

conjunto.remove("java")

print(conjunto)

#si intentas eliminar un valor que no existe, te dará un error

conjunto.discard("python")

print(conjunto)

#para saber si un valor está en el conjunto

print("java" in conjunto) #me retorna un booleano q dice falso

print(3 in conjunto) #me retorna un booleano q dice verdadero

conjunto.clear()

print(conjunto) #me retorna un conjunto vacio

