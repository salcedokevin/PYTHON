"""
programa que permita sacar el porcentaje que de el usuario
"""

numero1 = int(input("Escriba el numero: "))
porcentaje = int(input("Escriba el porcentaje: "))

resultado = numero1 * (porcentaje*0.01)
print(f"El {porcentaje}% de {numero1} es: {resultado}")