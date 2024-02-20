"""
Todas las tablas de multiplicar del 1 al 10
mostrando el titulo de la tabla y luego las multiplicaciones
"""

for contador in range(1,11):
    print(f"\nTabla del {contador}")
    for multiplicador in range(1,11):
        print(f"{contador} x {multiplicador} = {contador * multiplicador}")