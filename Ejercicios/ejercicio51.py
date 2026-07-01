# Ejercicio 51: Cifrado César
def cifrado_cesar(mensaje, desplazamiento):
    resultado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nueva_posicion = (ord(caracter) - base + desplazamiento) % 26
            resultado += chr(base + nueva_posicion)
        else:
            resultado += caracter
    return resultado

mensaje = "Hola Mundo"
desplazamiento = 3

cifrado = cifrado_cesar(mensaje, desplazamiento)
descifrado = cifrado_cesar(cifrado, -desplazamiento)

print("Mensaje cifrado:", cifrado)
print("Mensaje descifrado:", descifrado)
