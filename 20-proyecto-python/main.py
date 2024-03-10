"""
PROYECTO PYTHON MYSQL
-ABRIR ASISTENTE
-LOGIN O REGISTRO
-SI ELEGIMOS REGISTRO CREARA UN USUARIO EN LA BASE DE DATOS
-SI ELEGIMOS LOGIN IDENTIFICA AL USUARIO Y LE PREGUNTARA:
    -CREAR NOTA, MOSTRAR NOTA, BORRARLAS
"""

from usuarios import acciones, usuario
#import notas.nota as gaa

#print(gaa.Nota.Listar(usuario))

print("""
ACCIONES DISPONIBLES:
      -registro
      -login  
""")

hazEl = acciones.acciones()

accion = input("QUE QUIERES HACER?")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()