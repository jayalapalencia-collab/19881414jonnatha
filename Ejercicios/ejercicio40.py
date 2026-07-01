# Ejercicio 40: Rotar Lista
lista = [1, 2, 3, 4, 5]
k = 2

k = k % len(lista)
rotada = lista[-k:] + lista[:-k]

print("Lista rotada", k, "posiciones:", rotada)
