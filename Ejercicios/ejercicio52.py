# Ejercicio 52: To-Do List
tareas = []

def agregar_tarea(tareas, descripcion, prioridad):
    tareas.append({"descripcion": descripcion, "prioridad": prioridad, "completada": False})

def completar_tarea(tareas, descripcion):
    for tarea in tareas:
        if tarea["descripcion"] == descripcion:
            tarea["completada"] = True
            return
    print("Tarea", descripcion, "no encontrada")

def eliminar_tarea(tareas, descripcion):
    for i, tarea in enumerate(tareas):
        if tarea["descripcion"] == descripcion:
            del tareas[i]
            return
    print("Tarea", descripcion, "no encontrada")

agregar_tarea(tareas, "Completar proyecto", "ALTA")
agregar_tarea(tareas, "Revisar código", "MEDIA")
agregar_tarea(tareas, "Documentar", "BAJA")

orden_prioridad = {"ALTA": 1, "MEDIA": 2, "BAJA": 3}
tareas_ordenadas = sorted(tareas, key=lambda t: orden_prioridad[t["prioridad"]])

print("Tareas ordenadas por prioridad:")
for i, tarea in enumerate(tareas_ordenadas, 1):
    print(i, ". [", tarea["prioridad"], "]", tarea["descripcion"])
