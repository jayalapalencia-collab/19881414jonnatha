# Ejercicio 42: Encontrar Subsecuencia
lista_principal = [1, 2, 3, 4, 5, 6]
subsecuencia = [2, 4, 6]

indice = 0
for elemento in lista_principal:
    if indice < len(subsecuencia) and elemento == subsecuencia[indice]:
        indice += 1

es_subsecuencia = indice == len(subsecuencia)
print(subsecuencia, "es subsecuencia de", lista_principal, ":", es_subsecuencia)
