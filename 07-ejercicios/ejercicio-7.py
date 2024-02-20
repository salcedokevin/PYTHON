"""
hacer un programa que muestre los numeros impares entre 2 numeros que diga el usuario
"""

numero1 = int(input("Escriba el primer numero: "))
numero2 = int(input("Escriba el segundo numero: "))

if numero1 < numero2:
    for x in range(numero1, (numero2 + 1)):
        if x % 2 == 0:
            print(f"{x} es par")
        else:
            print(f"{x} es impar")
else:
    print("Numeros no validos")