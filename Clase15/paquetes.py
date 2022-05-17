#hay que crear un archivo vacio que se llame __init__.py
#asi python entiende que es un paquete

from datetime import datetime

dt = datetime.now()
print( dt.year, dt.month, dt.day, dt.hour)