import usuarios.usuario as modelo

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