# Codigo de los numeros de la loteria

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Inicializar una lista para los números ganadores
numeros_ganadores = []

#Preguntar cuántos números se van a ingresar
cantidad = int(input("¿Cuántos números triunfadores de la lotería quieres ingresar? "))

#Solicitar los números ganadores
for i in range(cantidad):
    numero = int(input(f"Ingrese el número ganador {i + 1}: "))
    numeros_ganadores.append(numero)

#Ordenar la lista de menor a mayor
numeros_ganadores.sort()

#Mostrar los números ordenados
print("\nNúmeros ganadores de la lotería, ordenados de menor a mayor:")
print(numeros_ganadores)
