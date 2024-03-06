import clases

persona = clases.Persona()
persona.setNombre("Kevin")
persona.setApellido("Salcedo")
persona.setAltura("156cm")
persona.setEdad("28 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellido()}")
print(persona.hablar())

informatico = clases.informatico()
informatico.setNombre("Roberto")
informatico.setApellido("Gonzales")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellido()}")

print(informatico.getLenguajes())
print(informatico.caminar())

print(informatico.experiencia)

tecnico = clases.tecnicoRedes()
tecnico.setNombre("Charlie")
print(tecnico.auditarredes, tecnico.getNombre(), tecnico.getLenguajes())