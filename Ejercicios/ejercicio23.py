# Ejercicio 23: Notas de Estudiantes
notas = {"Ana": 85, "Luis": 92, "Carlos": 78}
promedio = sum(notas.values()) / len(notas)
mejor_estudiante = max(notas, key=notas.get)
print("Promedio de notas:", promedio)
print("Estudiante con mayor nota:", mejor_estudiante, "(", notas[mejor_estudiante], ")")
