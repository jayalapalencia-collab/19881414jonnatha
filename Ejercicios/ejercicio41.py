# Ejercicio 41: Aplanar Lista Anidada
anidada = [[1, 2], [3, 4, 5], [6]]

plana = []
for sublista in anidada:
    for elemento in sublista:
        plana.append(elemento)

print("Lista aplanada:", plana)
