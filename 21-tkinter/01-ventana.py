"""
TKINTER ES UN MODULO PARA CREAR INTERFACES GRAFICAS PARA USUARIOS
"""

from tkinter import *
import os.path

# CREAR LA VENTANA RAIZ
ventana = Tk()

# TITULO DE LA VENTANA
ventana.title("PRACTICANDO PYTHON CTM!!!")

# COMPROBAR SI EXISTE UN ARCHIVO
ruta_icono = os.path.abspath('.imagenes/img.ico')

if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('./21-tkinter/imagenes/img.ico')

# MOSTRAR TEXTO EN EL PROGRAMA
texto = Label(ventana, text=ruta_icono)
texto.pack()

# ICONO DE LA VENTANA
ventana.iconbitmap("./21-tkinter/imagenes/img.ico")

# CAMBIO EN EL TAMAÑO DE LA VENTANA
ventana.geometry("750x450")

# BLOQUEAR TAMAÑO DE LA VENTANA
ventana.resizable(0, 0)

# ARRANCAR Y MOSTRAR LA VENTANA HASTA QUE SE CIERRE
ventana.mainloop()