class Clase1:
    def metodo1(self):
        print("Soy el método 1 de la Clase1")

class Clase2:
    def metodo2(self):
        print("Soy el método 2 de la Clase2")

class Clase3(Clase1, Clase2):
    def metodo3(self):
        print("Soy el método 3 de la Clase3")

c = Clase3()

c.metodo1()  # Output: Soy el método 1 de la Clase1

c.metodo2()  # Output: Soy el método 2 de la Clase2

c.metodo3()  # Output: Soy el método 3 de la Clase3