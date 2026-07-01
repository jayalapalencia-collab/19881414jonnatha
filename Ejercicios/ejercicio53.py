# Ejercicio 53: Generador de Contraseñas
import random
import string

def generar_contraseña(longitud=12, mayusculas=True, numeros=True, simbolos=True):
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += "!@#$%^&*"

    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

contraseña_generada = generar_contraseña(12)
print("Contraseña generada:", contraseña_generada)
