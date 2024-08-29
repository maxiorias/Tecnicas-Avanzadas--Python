class auto:
    def __init__(self, marca, kilometros, anio):
        self.marca = marca
        self.kilometros = kilometros
        self.anio = anio
        print(f'se ha creado un auto marca {self.marca}')
        print()
    
    def __del__(self):
        print(f'se ha vendido un auto marca {self.marca}')
        print()
    
    def __str__(self):
        return 'el auto es un {}, tiene {}, y es del año {}'.format(self.marca, self.kilometros, self.anio)

auto_uno = auto('audi', 200.000, 1993)

print(str(auto_uno))
