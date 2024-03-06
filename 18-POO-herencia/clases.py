# HERENCIA ES LA POSBILIDAD DE COMPARTIR ATRIBUTOS Y METODOS ENTRE CLASES

class Persona:
    """
    nombre
    apellido
    altura
    edad
    """

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo"
    
class informatico(Persona):
    """
    lenguajes
    experiencia
    """
    def __init__(self):
        self.lenguajes = "HTTML, CSS, JAVA, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def repararPC(self):
        return "He reparado tu pc"
    
class tecnicoRedes(informatico):
    def __init__(self):
        super().__init__()
        self.auditarredes = "experto"
        self.experienciaredes = 15

    def auditoria(self):
        return "Estoy auditando"