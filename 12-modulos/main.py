"""
Modulos: son funcionalidades ya hechas para utilizar
Se pueden conseguir modulos que ya vienen en el lenguaje,
modulos en internet, y tambien podemos crear nuestros modulos
"""

# Importar modulo propio
# import mimodulo
# from mimodulo import holaMundo
from mimodulo import *

#print(mimodulo.holaMundo("Kevin Salcedo"))
#print(mimodulo.calculadora(1, 2, True))

print(holaMundo("Kevin Salcedo"))
print(calculadora(1, 3, True))

# MODULO DE FECHAS
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y , %H:%M:%S")
print("Mi fecha personalizada: " + fecha_personalizada)

print(datetime.datetime.now().timestamp())

# MODULO MATEMATICA
import math

print("Raiz cuadrada de 10 es ", math.sqrt(10))

print("Numero pi: ", float(math.pi))

print("Redondear: ", math.ceil(6.52658))
print("Redondear: ", math.floor(6.52658))

# MODULO RANDOM
import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15, 67))