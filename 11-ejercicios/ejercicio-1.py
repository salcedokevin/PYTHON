"""
-programa con una lista con 8 numeros enteros
-debe recorrerla y mostrarla
-hacer funcion que recorra lista de numeros y devuelva un string
-ordenarla y mostrarla
-mostrar su longitud
-buscar un elemento dentro de la lista en base a lo que el usuario pida
"""
lista_numeros = [10,59,100,54,860,1,878,65]

for lista in lista_numeros:
    print(lista)

def mostrar_lista(lista):
    resultado = ""
    for elemento in lista:
        resultado += "\nElementos de lista: " + str(elemento)
    return resultado

print(mostrar_lista(lista_numeros))


print("\nORDENAR Y MOSTRAR")
lista_numeros.sort()
print(mostrar_lista(lista_numeros))


print("\nLONGITUD DE LISTA")
print(len(lista_numeros))

x = int(input("Escriba el numero que necesita: "))
if x in lista_numeros:
    print(f"El numero {x} existe")
else:
    print(f"El numero {x} no existe")