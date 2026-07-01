# Ejercicio 22: Frecuencia de Palabras
texto = "hola mundo hola python mundo mundo"
palabras = texto.split()
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
print("Frecuencia:", frecuencia)
