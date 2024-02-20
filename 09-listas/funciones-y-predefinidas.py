cantantes = ["Bad bunny", "Drake", "La mente", "Mago"]
numeros = [1, 5, 3, 13, 10]

# ORDENAR UNA LISTA
print(numeros)

numeros.sort()
print(numeros)

# AÑADIR ELEMENTOS
cantantes.append("Paramore")
cantantes.insert(2, "Grupo 5")
#print(cantantes)

# ELIMINAR ELEMENTOS
cantantes.pop(0)
cantantes.remove("Drake")

print(cantantes)

# DAR LA VUELTA A UNA LISTA
print(numeros)
numeros.reverse()
print(numeros)

# BUSCAR DENTRO DE UNA LISTA
print("Paramore" in cantantes)

# CONTAR ELEMENTOS
print(len(cantantes))

# CUANTAS VECES APARECE UN ELEMENTO EN UNA LISTA
numeros.append(10)
print(numeros.count(10))

# CONSEGUIR UN INDICE
print(cantantes.index("Paramore"))

# UNIR DOS LISTAS
cantantes.extend(numeros)
print(cantantes)