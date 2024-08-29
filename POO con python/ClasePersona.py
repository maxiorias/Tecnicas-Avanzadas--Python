class Persona:
    def __init__(self, nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

    def datosPersonales(self):
        print(f'El nombre de la persona es: {self.nombre}')
        print(f'El apellido de la persona es: {self.apellido}')
        print(f'La edad de la persona es: {self.edad}')
        print(f'El sexo de la persona es: {self.sexo}')
        print('--------------------')

empleado1 = Persona('Juan Carlos', 'Rodriguez', 29, 'masculino')

empleado1.datosPersonales()

    