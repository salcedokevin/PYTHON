"""
programa que pida al usuario la nota de 15 alumnos 
y el programa tiene que decir quienes aprobaron y quieres jalaron
"""

"""
nota1 = int(input("Coloque la nota: "))

while nota1 >= 12:
    print(f"La nota {nota1} es aprobatoria")
    break

else:
    print(f"La nota {nota1} es desaprobatoria")
"""

contador = 1
aprobados = 0
suspendidos = 0

nro_alumnos = int(input("Escriba la cantidad de alumnos: "))

while contador <= nro_alumnos:
    nota = int(input(f"Que nota desea colocar al alumno {contador}?: "))
    if nota >=12:
        aprobados += 1
    else:
        suspendidos += 1
    contador += 1

print(f"Aprobados: {aprobados}")
print(f"Desaprobados: {suspendidos}")