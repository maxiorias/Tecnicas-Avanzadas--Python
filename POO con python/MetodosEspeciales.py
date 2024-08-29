class auto:
    def __init__(self, marca, kilometros, anio):
        self.marca = marca
        self.kilometros = kilometros
        self.anio = anio
        #self.__ruedas = 4
        print(f'se ha creado un auto marca {self.marca}')
        print()
    
    #def __del__(self):
    #    print(f'se ha vendido un auto marca {self.marca}')
    #   print()

    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos
        if(self.enmarcha):
            return 'El auto esta encendido'
        else:
            return 'El auto esta apagado'
    
    def __str__(self):
        return 'el auto es un {}, tiene {} mil kilometros, y es del año {}'.format(self.marca, self.kilometros, self.anio)

print()
auto_uno = auto('audi', 200.000, 1993)
auto_dos = auto('fiat', 500, 2005)
##print(auto_uno.__ruedas)
##print(str(auto_uno))
print(str(auto_dos))
print(auto_uno.arrancar(True))
print(auto_dos.arrancar(False))
print()