# Ejercicio 54: Analizador de Texto
texto = """Python es un lenguaje de programación. 
Es muy popular en la actualidad. Python es versátil."""

palabras = texto.replace(".", "").replace("\n", " ").split()
total_palabras = len(palabras)

frecuencia_palabras = {}
for palabra in palabras:
    palabra_normalizada = palabra.lower()
    frecuencia_palabras[palabra_normalizada] = frecuencia_palabras.get(palabra_normalizada, 0) + 1

palabra_mas_frecuente = max(frecuencia_palabras, key=frecuencia_palabras.get)
veces = frecuencia_palabras[palabra_mas_frecuente]

longitud_total = sum(len(palabra) for palabra in palabras)
longitud_promedio = round(longitud_total / total_palabras, 1)

oraciones = [o.strip() for o in texto.replace("\n", " ").split(".") if o.strip()]
total_oraciones = len(oraciones)

print("Estadísticas del texto:")
print("- Palabras totales:", total_palabras)
print("- Palabra más frecuente:", palabra_mas_frecuente, "(", veces, "veces)")
print("- Longitud promedio:", longitud_promedio, "caracteres")
print("- Oraciones:", total_oraciones)
