# Ejercicio 29: Calculadora de IMC
peso = 70
altura = 1.75

imc = peso / (altura ** 2)
imc_redondeado = round(imc, 2)

if imc < 18.5:
    clasificacion = "Bajo Peso"
elif imc < 25:
    clasificacion = "Peso Normal"
elif imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print("IMC:", imc_redondeado, "- Clasificación:", clasificacion)
