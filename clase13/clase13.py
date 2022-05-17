#   class Perro():
#       def __init__(self, nombre, edad):
#           self.nombre = nombre
#           self.edad = edad
#   
#       def __str__(self):
#           return f'El nombre del perro es {self.nombre} y su #   edad es {self.edad}'



#perro_1 = Perro('Bruno', 10)
#print(perro_1)

#perro_2 = Perro('Mike', 4)
#print(perro_2)

#   class Vector():
#       def __init__(self, data):
#           self._data = data
#   
#       def __str__(self):
#           return f"The values are: {self._data}"
#       
#       def __len__(self):
#           return len(self._data)
#       
#       def __getitem__(self, pos):
#           return self._data[pos]
#       
#       def __setitem__(self, pos, value):
#           self._data[pos] = value
#   
#   v = Vector([1,2])
#   v[1]

#   print(v)
#   print(len(v))
#   
#   print(v[0]) #getitem
#   

#v[0] = 5
#print(v) #setitem

#class Persona:
#    def __init__(self,nombre,apellido,perro):
#        self.nombre = nombre
#        self.apellido = apellido
#        self.perro = perro
#
#    def __getitem__(self, pos):
#        return self.perro[pos]
#
#
#
#perro1 = Perro('Carlos', 15)
#
#perro2 = Perro('Firulais', 5)
#
#persona_1 = Persona('Gaston', 'Juarez', [perro1,perro2])
#
#print(persona_1.perro[1].edad)

#poniendo __ antes de un elemento protege de que no se pueda acceder
# un concepto relacionado con la programación, orientada a objetos, 
# y hace referencia al ocultamiento de los estados internos de una clase al exterior. 
# Dicho de otra manera, encapsular consiste en hacer que los atributos o métodos internos a una clase 
# no se puedan acceder ni modificar desde fuera, sino que tan solo el propio objeto pueda acceder a ellos. 
#AltZ para salto automatico

class User():
    def __init__(self,nombre,contraseña):
        self.nombre = nombre
        self.__contraseña = contraseña

    def validar_contraseña(self):
        if self.__contraseña == contraseña:
            print('La contraseña es correcta')
        else:
            print('La contraseña es incorrecta')

    def cambiar_contraseña(self,contraseña):
        self.__validar_contraseña()

usuario1 = User('Luca', '123123')

password = input('Ingrese su contraseña: ')


