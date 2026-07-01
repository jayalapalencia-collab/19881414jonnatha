# Ejercicio 49: Registro de Calificaciones
registro = {
    "Ana": {
        "Matemáticas": [85, 90],
        "Historia": [88]
    },
    "Luis": {
        "Matemáticas": [80]
    }
}

for estudiante, materias in registro.items():
    todas_las_notas = []
    for notas in materias.values():
        todas_las_notas.extend(notas)
    promedio_estudiante = sum(todas_las_notas) / len(todas_las_notas)
    print("Promedio", estudiante, ":", promedio_estudiante)

notas_por_materia = {}
for materias in registro.values():
    for materia, notas in materias.items():
        if materia not in notas_por_materia:
            notas_por_materia[materia] = []
        notas_por_materia[materia].extend(notas)

for materia, notas in notas_por_materia.items():
    promedio_materia = sum(notas) / len(notas)
    print("Promedio", materia, ":", promedio_materia)
