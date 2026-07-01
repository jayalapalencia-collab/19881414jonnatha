# Ejercicio 13: Eliminar Duplicados
lista = [1, 2, 2, 3, 4, 4, 5, 5, 5]
sin_duplicados = []
for elemento in lista:
    if elemento not in sin_duplicados:
        sin_duplicados.append(elemento)
print("Lista sin duplicados:", sin_duplicados)
