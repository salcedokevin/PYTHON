# PROGRAMACION ORIENTADA A OBJETOS

# DEFINIR UNA CLASE

class Coche:
    #Atributos o propiedades, caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "F40"
    velocidad = 300
    caballaje = 500
    plazas = 2

    #Metodos son acciones que hace el coche(funciones)
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo
    
    def acelerar(self):
        self.velocidad += 1
        
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
# DEFINICION CLASE
# CREAR UN OBJETO O INSTANCIAR UNA CLASE
coche = Coche()

coche.setColor("Amarillo")
coche.setModelo("Murcielago")

print("\n--------COCHE 1----------")
print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad nueva: ", coche.velocidad)
print("\n--------COCHE 2----------")

# CREAR MAS OBJETOS
coche2 = Coche()
coche2.setColor("Verde")
coche2.setModelo("Huracan")

print(coche2.marca, coche2.getModelo(), coche2.getColor())