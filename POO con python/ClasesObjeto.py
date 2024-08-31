class Gelatina:              # crea una clase
    def __init__(self, sabor, color, tamanio):    #contructor def como una funcion y dos guiones bajoes __init__
        self.sabor = sabor                        #siempre se usa la palabra reservada self y despues los atributos      
        self.color = color                        #que va a tener la clase, en este caso Gelatina
        self.tamanio = tamanio
    
    def imprimir(self):
        print(f'La gelatina es de {self.sabor}')
        print(f'La gelatina se ve de color {self.color}')
        print(f'La gelatina es de un tamaño {self.tamanio}')

gelatina1 = Gelatina('frutilla', 'rosa', 'grande')  # crea una instancia de la clase Gelatina

gelatina1.imprimir()                                 # invoca al metodo imprimir de la instancia creada

print(" ")

gelatina2 = Gelatina('limon', 'amarilla', 'considerable') 

gelatina2.imprimir()
