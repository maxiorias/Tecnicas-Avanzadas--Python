# Algoritmo de ordenamiento insercion 
def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        j = i
        while lista[j - 1] > lista[j] and j > 0:
            aux = lista[j - 1]
            lista[j - 1] = lista[j]
            lista[j] = aux
            j -= 1
    
    return lista


# Algoritmo de busqueda seleccionado
def busqueda_binaria(lista, buscarPaquete):
    primero = 0
    ultimo = len(lista) - 1
    
    while primero <= ultimo:
        medio = (ultimo + primero) // 2
        if buscarPaquete == lista[medio]:
            return medio
        elif buscarPaquete < lista[medio]:
            ultimo = medio - 1
        else:
            primero = medio + 1

    return -1


def altaPaquete(lista, paquete):
    lista.append(paquete)
    print("paquete dado de alta")
    return lista


def bajaPaquete(lista, paquete):
    lista.pop(paquete)
    print("ID fue dado de baja")

def modificacionPaquete(lista, paquete):
    print("ID actual %s " % paquete)
    nuevoID = input("Ingrese el nuevo ID: ")
    lista[paquete] = nuevoID
    print("ID fue modificado")



#lista con los iDs
listaPaquetes = []

while(True):
    print("Menu principal")

    print("Seleccione una opcion")
    print("1- Ordenar paquetes (clasificar).")
    print("2- Buscar un paquete.")
    print("3- Alta de producto con ID")
    print("4- Modificacion de ID")
    print("5- Baja de un ID")
    print("0- SALIR")
    
    opcion = input("ingrese una opcion: ")

    if opcion == '0':
        break

    match opcion:
        case 1:  #ordenar la lista
            ordenamiento_insercion(listaPaquetes)
            print("la lista fue ordenada")
        case 2:  #buscar un paquete
            paquete = input("Ingrese el ID del paquete a buscar: ")
            encontrado = busqueda_binaria(listaPaquetes, paquete)
            if encontrado == -1:
                print("ID de paquete no encontrado")
            else:
                print("ID de paquete hallado en la posicion %s" % encontrado)
                
        case 3: # Alta de paquete
            paquete = input("Ingrese el nuevo ID del paquete: ")
            encontrado = busqueda_binaria(listaPaquetes, paquete)
            if encontrado == -1:
                altaPaquete(listaPaquetes, paquete)
            else:
                print("ID de paquete YA EXISTE en la posicion %s" % encontrado)
                print("Pruebe con otro ID")
            
                       
        case 4: # Modificar paquete
            paquete = input("Ingrese el ID del paquete a modificar: ")
            encontrado = busqueda_binaria(listaPaquetes, paquete)
            if encontrado == -1:
                print("ID del paquete NO EXISTE")
            else:
                modificacionPaquete(listaPaquetes, encontrado)
               
        case 5: # Baja de un paquete
            paquete = input("Ingrese el ID del paquete a eliminar: ")
            encontrado = busqueda_binaria(listaPaquetes, paquete)
            if encontrado == -1:
                print("ID del paquete NO EXISTE")
            else:
                bajaPaquete(listaPaquetes, paquete)
            


    if(opcion == 0):
        break
    else:
        continue

    
    



   

