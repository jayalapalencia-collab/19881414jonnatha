# Ejercicio 34: Suma de Dígitos
numero = 1234
n = numero
suma = 0
while n > 0:
    digito = n % 10
    suma += digito
    n //= 10
print("Suma de dígitos de", numero, ":", suma)
