# Ejercicio 35: Conversor de Bases
decimal = 42
n = decimal
residuos = []

if n == 0:
    residuos = [0]
while n > 0:
    residuos.append(n % 2)
    n //= 2
residuos.reverse()

binario = "".join(str(r) for r in residuos)
print(decimal, "en binario:", binario)
