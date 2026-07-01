# Ejercicio 46: Agenda Telefónica
agenda = {}

def agregar_contacto(agenda, nombre, telefono):
    agenda[nombre] = telefono
    print("Contacto agregado:", nombre, "->", telefono)

def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        print("Contacto encontrado:", nombre, "-", agenda[nombre])
        return agenda[nombre]
    else:
        print("Contacto", nombre, "no encontrado")
        return None

def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado:", nombre)
    else:
        print("No se puede eliminar,", nombre, "no existe")

agregar_contacto(agenda, "Juan", "123-4567")
buscar_contacto(agenda, "Juan")
eliminar_contacto(agenda, "Juan")
