"""
Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario
"""

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

if numero_1 < numero_2:
    for contador in range(numero_1, numero_2):
        print(contador)
else:
    print("El numero 1 debe ser menor al numero 2")