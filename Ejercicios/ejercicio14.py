# Ejercicio 14: Lista Invertida
original = [1, 2, 3, 4, 5]
invertida = []
for i in range(len(original) - 1, -1, -1):
    invertida.append(original[i])
print("Lista invertida:", invertida)
