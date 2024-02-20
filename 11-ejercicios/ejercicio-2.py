"""
Programa que añada valores a una lista mientras que su longitud sea menor a 120
luego mostrar la lista
usar while y for
"""

coleccion = []

for numero in range(0, 120):
    coleccion.append(numero)
    #print(coleccion[numero])

print(coleccion)

##################################################

print("\nUSANDO WHILE")
coleccion = []
rango = 0

while rango < 120:
    coleccion.append(rango)
    rango += 1
print(coleccion)