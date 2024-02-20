# VARIABLE GLOBAL
frase = "frase"
print(frase)

def holaMundo():
    #frase = "Hola Mundo!"
    print(frase)

    year = 2021
    print(year)

    global website
    website= "kevinsalcedo.pe"
    print(website)

    return str((year))

print(holaMundo())
print(website)