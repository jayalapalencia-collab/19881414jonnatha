# Ejercicio 56: Comprobador de Edad Exacta
from datetime import date

def calcular_edad(dia, mes, anio):
    # Obtenemos la fecha actual
    hoy = date.today()
    
    # Intentamos crear el objeto de fecha para el nacimiento
    try:
        nacimiento = date(anio, mes, dia)
    except ValueError:
        return None, "La fecha ingresada no es válida. Por favor, verifica el día, mes y año."
    
    # Comprobamos que la fecha de nacimiento no sea en el futuro
    if nacimiento > hoy:
        return None, "¡La fecha de nacimiento no puede ser en el futuro!"

    # Calculamos la diferencia de años
    edad = hoy.year - nacimiento.year
    
    # Comparamos mes y día actual con mes y día de nacimiento.
    # Si la tupla (mes_actual, dia_actual) es menor que (mes_nacimiento, dia_nacimiento),
    # significa que aún no ha llegado su día de cumpleaños este año, por lo que restamos 1.
    ya_cumplio_este_anio = (hoy.month, hoy.day) >= (nacimiento.month, nacimiento.day)
    
    if not ya_cumplio_este_anio:
        edad -= 1

    return edad, ya_cumplio_este_anio

# Código principal interactivo
print("=== COMPROBADOR DE EDAD EXACTA ===")
try:
    dia_n = int(input("Introduce tu día de nacimiento (1-31): "))
    mes_n = int(input("Introduce tu mes de nacimiento (1-12): "))
    anio_n = int(input("Introduce tu año de nacimiento: "))
    
    edad_calculada, estado = calcular_edad(dia_n, mes_n, anio_n)
    
    if edad_calculada is None:
        print(f"Error: {estado}")
    else:
        print("\n--- Resultados ---")
        print(f"Fecha de nacimiento: {dia_n:02d}/{mes_n:02d}/{anio_n}")
        print(f"Fecha de hoy: {date.today().strftime('%d/%m/%Y')}")
        print(f"Edad exacta: {edad_calculada} años.")
        
        if estado:
            print("¡Ya cumpliste años este año!")
        else:
            # Ejemplo explicativo como el que diste: si va a cumplir 15 pero aún tiene 14
            proximo_cumple = edad_calculada + 1
            print(f"Aún no cumples años este año. Tienes {edad_calculada} años y cumplirás {proximo_cumple} años próximamente.")
            
except ValueError:
    print("Error: Por favor, introduce solo números enteros para la fecha.")
