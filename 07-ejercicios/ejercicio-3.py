"""
escribir un programa que muestre los cuadrados de los 60 primeros numeros naturales,
usando for y con while
"""

contador = 0

while contador <= 60:
    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    contador += 1

#########################################################

for numero in range(61):
    cuadrado = numero * numero
    print(f"El cuadrado de {numero} es {cuadrado}")
