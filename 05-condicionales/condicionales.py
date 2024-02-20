# ejemplo 1

print("********************EJEMPLO 1********************")

#color = input("adivina cual es mi color favorito: ")
color = "rojo"

if color == "rojo":
    print("el color es ROJO")
else:
    print("color incorrecto")

"""
OPERADORES DE COMPARACION
== IGUAL
!= DIFERENTE
< MENOS QUE
> MAYOR QUE
<= MENOR IGUAL QUE
>= MAYOR IGUAL QUE

OPERADORES LOGICOS
and y
or o
! negacion
not no
"""

print("\n********************EJEMPLO 2********************")

year = 2020
#year = int(input("En que año estamos?: "))

if year >= 2021:
    print("estamos en 2021")
else:
    print("no estamos en 2021")

print("\n********************EJEMPLO 3********************")

nombre = "Kevin Salcedo"
ciudad = "Lima"
continente = "America"
edad = "17"
mayoria_edad = "18"

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if continente != "America":
        print("usuario es americano")
    else:
        print(f"es americano de la ciudad de {ciudad}")

else:
    print(f"{nombre} no es mayor de edad")

print("\n********************EJEMPLO 4********************")

#dia = int(input("Introduce el dia de la semana: "))
dia = 2

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else: 
    print("Es fin de semana")

print("\n********************EJEMPLO 5********************")

edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("Introduce tu edad: "))
edad_oficial = 18

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")

print("\n********************EJEMPLO 6********************")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es una pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")

print("\n********************EJEMPLO 7********************")

pais = "España"

if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es una pais de habla hispana")
else:
    print(f"{pais} SI es un pais de habla hispana")

print("\n********************EJEMPLO 7********************")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es una pais de habla hispana")
else:
    print(f"{pais} SI es un pais de habla hispana")