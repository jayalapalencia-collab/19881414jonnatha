# Ejercicio 50: Adivina el Número
import random

numero_secreto = random.randint(1, 100)
intentos = 0
numeros_a_probar = [50, 75, 88, 94, 97]
adivino = False

for intento_actual in numeros_a_probar:
    intentos += 1
    if intento_actual == numero_secreto:
        print("¡Adivinaste! El número era", numero_secreto)
        print("Intentos:", intentos)
        adivino = True
        break
    elif intento_actual > numero_secreto:
        print(intento_actual, ": muy alto")
    else:
        print(intento_actual, ": muy bajo")

if not adivino:
    print("No adivinaste. El número era", numero_secreto)
