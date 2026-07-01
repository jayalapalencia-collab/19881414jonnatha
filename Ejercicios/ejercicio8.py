# Ejercicio 8: Secuencia Fibonacci
a, b = 0, 1
secuencia = []
for i in range(10):
    secuencia.append(a)
    a, b = b, a + b
print("Secuencia Fibonacci:", ", ".join(str(n) for n in secuencia))
