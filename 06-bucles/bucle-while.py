"""
BUCLE WHILE
Estructura de control que itera o repite la ejecucion de una serie 
de instrucciones tantas veces como sea necesario hasta que deje de
cumplirse la condicion

while condicion:
    bloque de instruccion
    actualizacion de contador
"""
print("\n***********************EJMPLO 1***********************")
contador = 1

while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador += 1

print("\n***********************EJMPLO 2***********************")
contador = 1
muestrame = str(0)

while contador <= 100:
    #print(f"Estoy en el numero: {contador}")
    muestrame = muestrame + ", " + str(contador)
    contador += 1
print(muestrame)

print("\n***********************EJMPLO 3***********************")
numero_usuario = int(input("De que numero quieres la tabla: "))

if numero_usuario < 1:
    numero_usuario = 1
print(f"Tabla del: {numero_usuario}")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1
else:
    print("Tabla terminada")