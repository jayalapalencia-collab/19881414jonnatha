# Ejercicio 37: Máximo Común Divisor
a, b = 48, 18

x, y = a, b
while y != 0:
    x, y = y, x % y

print("MCD de", a, "y", b, ":", x)
