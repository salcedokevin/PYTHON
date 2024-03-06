from coche import Coche

carro = Coche("Amarillo", "Audi", "R8", 400, 700, 2)
carro1 = Coche("Rojo", "Toyoya", "Corolla", 250, 150, 4)
carro2 = Coche("Verde", "Ford", "Mustang", 280, 120, 2)
carro3 = Coche("Negro", "Mitsubishi", "Lancer", 250, 100, 4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# DETECTAR TIPADO
carro3 = 3
if type(carro3) == Coche:
    print("Es un objeto de tipo carro")
else:
    print("No es un objeto tipo carro")

# VISIBILIDAD
    