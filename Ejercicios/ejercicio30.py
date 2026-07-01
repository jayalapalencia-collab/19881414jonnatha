# Ejercicio 30: Piedra, Papel o Tijeras
jugador1 = "piedra"
jugador2 = "tijeras"
opciones_validas = ["piedra", "papel", "tijeras"]

if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
    print("Entrada no válida")
elif jugador1 == jugador2:
    print("Empate")
else:
    gana_jugador1 = (
        (jugador1 == "piedra" and jugador2 == "tijeras") or
        (jugador1 == "papel" and jugador2 == "piedra") or
        (jugador1 == "tijeras" and jugador2 == "papel")
    )
    if gana_jugador1:
        print("Jugador 1 gana:", jugador1, "le gana a", jugador2)
    else:
        print("Jugador 2 gana:", jugador2, "le gana a", jugador1)
