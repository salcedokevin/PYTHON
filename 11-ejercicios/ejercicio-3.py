"""
Programa que compruebe si una variable esta vacia y si esta vacia
la rellene con un texto en minuscula y mostrarla en mayuscula
"""

texto = "   "

if len(texto.strip()) <= 0:
    texto = "texto en minuscula"

print(texto.upper())