import notas.nota as modelo

class Acciones:
    def Crear(self, usuario):
        print(f"Usuario {usuario[1]} crearemos una nueva nota")
        titulo = input("\nIntroduce el titulo de tu nota: ")
        descripcion = input("Mete el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.Guardar()

        if guardar[0] >= 1:
            print(f"Se guardo la nota: {nota.titulo}")
        else: 
            print("No se guardo la nota CTM!!!")

    def Mostrar(self, usuario):
        print(f"\nUsuario {usuario[1]} estas son tus notas:")

        nota = modelo.Nota(usuario[0])
        notas = nota.Listar()

        for datos in notas:
            print(f"{datos[2]}: {datos[3]}")

        #print(notas)
            
    def Borrar(self, usuario):
        print(f"{usuario[1]} vamos a borrar tu nota")

        titulo = input("Introduce el titulo de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)

        eliminar = nota.Eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")

        else:
            print("No se ha borrado la nota")