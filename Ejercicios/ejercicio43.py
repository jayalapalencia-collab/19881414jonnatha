# Ejercicio 43: Partición de Lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("Pares:", pares)
print("Impares:", impares)
