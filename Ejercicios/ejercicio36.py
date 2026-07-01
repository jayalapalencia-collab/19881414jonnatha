# Ejercicio 36: Palíndromo
texto = "Anita lava la tina"
texto_limpio = texto.lower().replace(" ", "")

es_palindromo = True
izquierda = 0
derecha = len(texto_limpio) - 1
while izquierda < derecha:
    if texto_limpio[izquierda] != texto_limpio[derecha]:
        es_palindromo = False
        break
    izquierda += 1
    derecha -= 1

if es_palindromo:
    print(texto, "es un palíndromo")
else:
    print(texto, "no es un palíndromo")
