personas = {"maxi":31, "maria":22, "ricardo": 25, "pato": 55}

print(personas)

print(personas["maxi"]) #muestra el valor de 31. aca lo que hago es llamar a la clave(key)y accedo a su valor 31

#para modificar el diccionario

personas["maxi"] = 32 #modifico el valor de maxi

print(personas)

#para agregar una nueva clave-valor

personas["pepe"] = 33 #agrego una nueva clave-valor

print(personas)

#para eliminar una clave-valor

del personas["maria"] #elimino la clave-valor de maria

print(personas)

#para obtener todas las claves      

print(personas.keys())

#para obtener todos los valores 

   

print(personas.values())

#para obtener todas las claves y valores en pares

print(personas.items())

print(f"estan atendiendo a {2}")