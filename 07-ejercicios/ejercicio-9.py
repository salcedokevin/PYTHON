"""
un programa que nos pida un numero indefinidamente hasta que el usuario ponga el numero 111
"""
contador = 1

while contador < 100:
    numero = int(input("Introduce un numero: "))
    if numero == 111:
        break
    else:
        print(f"has introducido el {numero}")