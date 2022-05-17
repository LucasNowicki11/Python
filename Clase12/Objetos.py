
class Auto():
    def __init__(self,color, marca):
        self.color = color
        self.marca = marca
    def arrancar(self):
        print('El auto acaba de arrancar')





#siempre utilizamos el self para alguna referencia al objeto
#no puedo llamar la funcion si no utilizo autito. 
#ya que es una funcion del auto


class Perro():
    patas = 4
    orejas =2

    def __init__(self, raza, tamaño, edad):
        self.raza = raza
        self.tamaño = tamaño
        self.edad = edad
    def ladrar(self):
        if self.tamaño == 'grande':
            print('El perro esta ladrando muy fuerte')
        elif self.tamaño == 'mediano':
            print('El perro esta ladrando no muy fuerte')
        elif self.tamaño == 'chiquito':
            print('Al perro ni se le escucha')








