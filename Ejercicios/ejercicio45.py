# Ejercicio 45: Fusión de Diccionarios
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 15, "c": 25, "d": 35}

fusionado = dict1.copy()
for clave, valor in dict2.items():
    if clave in fusionado:
        fusionado[clave] += valor
    else:
        fusionado[clave] = valor

print("Diccionarios fusionados:", fusionado)
