#1. Escriba un programa que almacene en una Lista los cursos que has cursado o los que te gustaría cursar en Udemy. Luego muestre la lista por consola.

cursos = ["cyberseguridad", "java", "R", ".net"]

print(cursos)

#1. Escriba un programa que almacene personas en una lista, luego que le muestre por pantalla el mensaje de ‘Su nombre es ‘nombre’

nombres = []
   
nombres.append(input("Ingrese su nombre: "))
 
print("Su nombre es: ", nombres[0])
#1. Escribir un programa que guarde en una variable un diccionario con los siguientes valores {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y muestre en consola el símbolo o un mensaje de advertencia si esa divisa no se encuentra en el diccionario.

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
 
divisa = input('Ingrese la divisa: ')
 
if divisa in monedas:
    print(f'El simbolo de la divisa {divisa} es {monedas[divisa]}')
else:  
    print('Divisa no válida')
#1. En una tupla coloque los siguientes valores: números enteros, decimales, String, colecciones. Luego muestre en consola.

tupla = (10, 10.5, "Hola", ["Python", "Java", "JavaScript"])
 
for elemento in tupla:
    print(elemento) 