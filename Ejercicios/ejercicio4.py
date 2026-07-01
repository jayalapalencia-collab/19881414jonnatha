# Ejercicio 4: Calculadora Simple
num1 = 10
num2 = 5
operador = "+"

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2
else:
    resultado = None
    print("Operador no válido")

if resultado is not None:
    print(num1, operador, num2, "=", resultado)
