# Practica1_2do_TorresOlvera

Torres Olvera Gael

En esta actividad realizamos una serie de codigos

# Almacenar en una lista los precios y mostrar en pantalla el menor y el mayor de los precios.

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Valores establecidos para la lista

a = int(input("Ingresa el valor que quieras: "))

b = int(input("Ingresa el valor que quieras: "))

c = int(input("Ingresa el valor que quieras: "))

d = int(input("Ingresa el valor que quieras: "))

e = int(input("Ingresa el valor que quieras: "))

f = int(input("Ingresa el valor que quieras: "))

g = int(input("Ingresa el valor que quieras: "))

Precios = [a, b, c, d, e, f, g] #Juntando los valores solicitados en una linea

#Ordenar la lista de mayor a menor

Precios.sort(reverse=True)

#Imprimir la lista ordenada

print("Lista ordenada de mayor a menor:")

print(Precios)

![image](https://github.com/user-attachments/assets/2a6e9ac1-b94a-4912-b114-40e4742b4058)
![image](https://github.com/user-attachments/assets/7a960d84-809d-4d94-8b1b-0a565e31ca40)
![image](https://github.com/user-attachments/assets/36625e92-a864-4725-9379-2c94e1a7d98c)


# Codigo de listas sobre las materias

print (" ")

print ("Torres Olvera Gael")

print (" ")

#Almacenar las materias en una lista

materias = ["Pensamiento matemático", "Español", "Inglés", "Química", "Civismo", "Francés"]

#Desplegar mensaje por cada materia

for materia in materias:

    print("Estoy cursando", materia)

#Crear una lista para las calificaciones

calificaciones = []

#Pedir al usuario las calificaciones

for materia in materias:

    calificacion = float(input(f"Ingrese la calificación para {materia}: "))
    
    calificaciones.append(calificacion)

#Mostrar las calificaciones

print("\nResultados de calificaciones:")

for i in range(len(materias)):

    print(f"En {materias[i]} has obtenido {calificaciones[i]}")

![image](https://github.com/user-attachments/assets/7f017355-f509-4c61-8e3d-b79fb1eecd09)
![image](https://github.com/user-attachments/assets/72d261a1-4516-4e3d-8979-f462550ba1b5)
![image](https://github.com/user-attachments/assets/86641eb8-cb03-44ad-b826-0506583df1d8)


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

![image](https://github.com/user-attachments/assets/f40c8809-31dd-45e1-8c99-5a47a4b7987d)
![image](https://github.com/user-attachments/assets/7aedde33-5f9a-4ca5-886f-025cfb0cca0a)
![image](https://github.com/user-attachments/assets/1394fe04-feed-4250-94a9-623f9d6b9115)


