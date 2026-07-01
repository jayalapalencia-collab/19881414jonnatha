# Ejercicio 39: Intersección de Listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

interseccion = []
for elemento in lista1:
    if elemento in lista2 and elemento not in interseccion:
        interseccion.append(elemento)

print("Intersección:", interseccion)
