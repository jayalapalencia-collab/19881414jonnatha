# Ejercicio 28: Tipo de Triángulo
lado1, lado2, lado3 = 5, 5, 5

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("Triángulo equilátero: todos los lados miden", lado1)
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Triángulo isósceles: dos lados iguales")
    else:
        print("Triángulo escaleno: todos los lados diferentes")
else:
    print("No es un triángulo válido")
