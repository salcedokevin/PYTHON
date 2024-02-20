"""
FOR

for variable in elemento iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES
"""
contador = 0
resultado = 0

for contador in range(0, 10):
    print("Voy por el: " + str(contador))
    resultado = resultado + contador

print(f"El resultado es: {resultado}")

# EJEMPLO TABLA DE MULTIPLICAR
print("\n******************EJEMPLO******************")

numero_usuario = int(input("De que numero quieres la tabla: "))

if numero_usuario >= 1:
    #numero_usuario = 1
    print(f"Tabla de multiplicar del numero {numero_usuario}")

    for numero_tabla in range(1,11):
        if numero_usuario == 45:
            print("No se puede mostrar")
            break

        print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
    else:
        print("tabla finalizada")