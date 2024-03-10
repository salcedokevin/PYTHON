import usuarios.usuario as modelo
import notas.acciones

class acciones:
    def registro(self):
        print("\nVAMOS A REGISTRARTE EN EL SISTEMA")
        nombre = input("CUAL ES TU NOMBRE: ")
        apellido = input("CUAL ES TU APELLIDO: ")
        email = input("CUAL ES TU EMAIL: ")
        contra = input("CUAL ES TU CONTRASEÑA: ")

        usuario = modelo.Usuario(nombre, apellido, email, contra)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Usuario {nombre} te has registrado con el email {email}")
        else:
            print("No te has registrado correctamente")

    def login(self):
        print("\nIDENTIFICATE")
        email = input("CUAL ES TU EMAIL: ")
        contra = input("CUAL ES TU CONTRASEÑA: ")

        try:
            usuario = modelo.Usuario('', '', email, contra)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, estas registrado desde el {login[5]}")
                self.proximasacciones(login)

        except Exception as e:
            #print(type(e))
            print(type(e).__name__,"-",e)
            print(f"Login incorrecto CTM!!!")

    def proximasacciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear notas (crear)
        - Mostrar notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir (salir)
        """)

        accion = input("Que quieres hacer?: ")
        hazel = notas.acciones.Acciones()

        if accion == "crear":
            hazel.Crear(usuario)
            self.proximasacciones(usuario)
        elif accion == "mostrar":
            hazel.Mostrar(usuario)
            self.proximasacciones(usuario)
        elif accion == "eliminar":
            hazel.Borrar(usuario)
            self.proximasacciones(usuario)
        elif accion == "salir":
            print(f"Adios {usuario[1]}")
            exit()