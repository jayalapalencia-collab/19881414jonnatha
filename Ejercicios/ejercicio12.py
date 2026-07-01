# Ejercicio 12: Mayor y Menor
numeros = [23, 45, 12, 67, 34, 89, 21]
mayor = numeros[0]
menor = numeros[0]
for n in numeros:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n
print("Número mayor:", mayor)
print("Número menor:", menor)
