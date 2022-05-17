
from .Objetos import Perro, Auto



fiat600 = Auto('rojo', 'fiat')
gol = Auto('blanco', 'VW')

print(fiat600.color)
print(gol.marca)

fiat600.arrancar()


rojelio = Perro('salchicha', 'chiquito', 5)
firulais = Perro('colie', 'mediano', 8)
betun = Perro('rotweilr', 'grande', 10)

betun.ladrar()