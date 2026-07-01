# Ejercicio 31: Validador de Contraseñas
contraseña = "Python3.9!"

tiene_longitud = len(contraseña) >= 8
tiene_mayuscula = any(c.isupper() for c in contraseña)
tiene_numero = any(c.isdigit() for c in contraseña)
caracteres_especiales = "!@#$%^&*()_+-=.,;:"
tiene_especial = any(c in caracteres_especiales for c in contraseña)

if tiene_longitud and tiene_mayuscula and tiene_numero and tiene_especial:
    print("Contraseña válida: cumple todos los criterios de seguridad")
else:
    print("Contraseña inválida: no cumple todos los criterios")
    if not tiene_longitud:
        print("- Debe tener al menos 8 caracteres")
    if not tiene_mayuscula:
        print("- Debe tener al menos una mayúscula")
    if not tiene_numero:
        print("- Debe tener al menos un número")
    if not tiene_especial:
        print("- Debe tener al menos un carácter especial")
