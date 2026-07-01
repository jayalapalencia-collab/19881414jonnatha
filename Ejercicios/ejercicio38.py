# Ejercicio 38: Lista de Números Primos
def es_numero_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

inicio, fin = 10, 50
primos = [n for n in range(inicio, fin + 1) if es_numero_primo(n)]
print("Números primos entre", inicio, "y", fin, ":", primos)
