#Codigo de listas sobre las materias

print (" ")
print ("Torres Olvera Gael")
print (" ")

# Almacenar las materias en una lista
materias = ["Pensamiento matemático", "Español", "Inglés", "Química", "Civismo", "Francés"]

# Desplegar mensaje por cada materia
for materia in materias:
    print("Estoy cursando", materia)

# Crear una lista para las calificaciones
calificaciones = []

# Pedir al usuario las calificaciones
for materia in materias:
    calificacion = float(input(f"Ingrese la calificación para {materia}: "))
    calificaciones.append(calificacion)

# Mostrar las calificaciones
print("\nResultados de calificaciones:")
for i in range(len(materias)):
    print(f"En {materias[i]} has obtenido {calificaciones[i]}")
