# Ejercicio 9: Contador de Vocales
texto = "Hola Mundo Python"
vocales = "aeiouAEIOU"
contador = 0
for letra in texto:
    if letra in vocales:
        contador += 1
print("Número de vocales en", texto, ":", contador)
