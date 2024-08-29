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

miPersona = Persona('Juan Carlos', 'Rodriguez', 29, 'masculino')

miPersona.datosPersonales()

class Empleado(Persona):

    def datosEmpleados(self, vacaciones, salario):
        print(f'Sus dias de vacaciones son {vacaciones}')
        print(f'Su salario es de {salario} pesos argentinos')
        print('--------------------')

miEmpleado = Empleado('Juan Carlos', 'Rodriguez', 29, 'masculino')

miEmpleado.datosPersonales()

miEmpleado.datosEmpleados(15, 4000)

