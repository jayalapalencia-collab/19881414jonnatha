# Ejercicio 33: Pirámide de Números
filas = 4

for i in range(1, filas + 1):
    izquierda = "".join(str(n) for n in range(1, i + 1))
    derecha = "".join(str(n) for n in range(i - 1, 0, -1))
    linea = izquierda + derecha
    print(linea.rjust(filas * 2 - 1))
